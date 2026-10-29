"""Reload supervisor code only at a completed-turn boundary, without inference."""
import hashlib
import os
from pathlib import Path
import sys


def code_snapshot(directory):
    files = {p.name: p.read_bytes() for p in sorted(Path(directory).glob('*.py'))
             if not p.name.startswith('test_')}
    digest = hashlib.sha256()
    for name, data in files.items():
        digest.update(name.encode() + b'\0' + data + b'\0')
    return digest.digest(), files


class Reloader:
    def __init__(self, directory):
        self.directory = Path(directory)
        self.loaded, _ = code_snapshot(self.directory)
        self.rejected = None

    def check(self, announce):
        current, files = code_snapshot(self.directory)
        if current == self.loaded:
            return False
        try:
            for name, data in files.items():
                compile(data, str(self.directory / name), 'exec')
        except (SyntaxError, ValueError) as exc:
            if self.rejected != current:
                announce(f'Supervisor update has invalid Python; retaining loaded code: {exc}')
                self.rejected = current
            return False
        announce('Supervisor code changed; reloading between turns. Saved checkpoints and quota waits are retained.')
        # No child invocation is active here. The close-on-exec process lock is
        # released and main reacquires it; a competing launcher can only win the
        # normal exclusive lock, never run concurrently against the same state.
        # A one-shot budget renewal has already been persisted by main. Do not
        # repeat it every time an unrelated code update reloads the supervisor.
        argv = []
        skip = False
        for arg in sys.argv:
            if skip:
                skip = False
            elif arg == '--resume-research':
                skip = True
            elif not arg.startswith('--resume-research='):
                argv.append(arg)
        os.execv(sys.executable, [sys.executable, *argv])
        return True
