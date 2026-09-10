#!/usr/bin/env python3
"""Shared subscription-loop supervisor (Python standard library, macOS/Linux)."""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
import selectors
import signal
import subprocess
import sys
import time

from events import Events
from providers import VENDORS, check, command

ROOT = Path(__file__).resolve().parents[2]
STOP = False
QUOTA_DELAYS = (300, 900, 1800, 3600)
TRANSIENT_DELAYS = (30, 60, 120, 300, 900)


def announce(message):
    stamp = datetime.now().astimezone().isoformat(timespec='seconds')
    print(f'[{stamp}] {message}', flush=True)


def on_signal(signum, frame):
    global STOP
    STOP = True


def wait_until(stamp):
    while not STOP and time.time() < stamp:
        time.sleep(min(1, max(0, stamp - time.time())))


@contextmanager
def lock(path, wait=False):
    """Kernel releases locks even on a crash; never unlink the lock inode."""
    with path.open('a+') as handle:
        waiting = False
        while True:
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if not wait:
                    raise RuntimeError(f'Another loop is already using {path.name}.')
                if STOP:
                    yield False
                    return
                if not waiting:
                    announce('Another provider is editing the repository; waiting for its checkpoint.')
                    waiting = True
                time.sleep(1)
        try:
            yield True
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def read_state(path):
    if not path.exists():
        return {}
    try:
        state = json.loads(path.read_text())
        if not isinstance(state, dict):
            raise ValueError('not an object')
        for key in ('retry_at', 'failures', 'unknowns', 'no_progress'):
            value = state.get(key, 0)
            if not isinstance(value, (int, float)) or not 0 <= value < 1e12:
                raise ValueError('invalid numeric field')
        return state
    except ValueError as exc:
        raise RuntimeError(f'Invalid retry state: {path}. Inspect it before restarting.') from exc


def save_state(path, state):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(state, indent=2) + '\n')
    temporary.replace(path)


def proved():
    return any(line.strip() == 'STATUS: PROVED' for line in (ROOT / 'PROGRESS.md').read_text().splitlines())


def checkpoint_digest():
    digest = hashlib.sha256()
    files = [ROOT / 'PROGRESS.md', *sorted((ROOT / 'history').glob('*.md'))]
    for path in files:
        digest.update(str(path.relative_to(ROOT)).encode())
        digest.update(path.read_bytes())
    return digest.digest()


def logs(directory):
    """Fixed-size rotating logs, including during a long individual invocation."""
    handlers = []
    for stream in ('stdout', 'stderr'):
        handler = RotatingFileHandler(directory / f'{stream}.log', maxBytes=2 * 1024 * 1024, backupCount=2, encoding='utf-8')
        handler.setFormatter(logging.Formatter('%(message)s'))
        handlers.append(handler)
    return handlers


def write_log(handler, text):
    # Also cap a single event so rotation cannot be defeated by a huge line.
    for offset in range(0, len(text), 65536):
        record = logging.LogRecord('loop', logging.INFO, '', 0, text[offset:offset + 65536].rstrip('\n'), (), None)
        handler.emit(record)


def terminate_group(process):
    # Wait for descendants too: CLI exit alone does not prove its tools exited.
    for sig, grace in ((signal.SIGINT, 5), (signal.SIGTERM, 3), (signal.SIGKILL, 1)):
        try:
            os.killpg(process.pid, sig)
        except ProcessLookupError:
            break
        deadline = time.monotonic() + grace
        while time.monotonic() < deadline:
            process.poll()  # Reap the group leader if it exited.
            try:
                os.killpg(process.pid, 0)
            except ProcessLookupError:
                process.wait()
                return
            time.sleep(0.05)
    process.wait()


def run_process(argv, stdin, directory, timeout, verbose=False):
    events = Events()
    handlers = logs(directory)
    started = time.monotonic()
    env = dict(os.environ, NO_COLOR='1', TERM='dumb')
    process = None
    timed_out = False
    try:
        process = subprocess.Popen(argv, cwd=ROOT, env=env, stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
        # PROMPT.md is deliberately small, below pipe capacity on supported hosts.
        try:
            if stdin is not None:
                process.stdin.write(stdin.encode())
            process.stdin.close()
        except BrokenPipeError:
            pass
        with selectors.DefaultSelector() as selector:
            buffers = {0: b'', 1: b''}
            selector.register(process.stdout, selectors.EVENT_READ, 0)
            selector.register(process.stderr, selectors.EVENT_READ, 1)
            while selector.get_map():
                if STOP or time.monotonic() - started >= timeout:
                    timed_out = not STOP
                    terminate_group(process)
                    break
                for key, _ in selector.select(timeout=0.5):
                    index = key.data
                    chunk = os.read(key.fileobj.fileno(), 65536)
                    if not chunk:
                        selector.unregister(key.fileobj)
                        if buffers[index]:
                            events.line(buffers[index].decode(errors='replace'), stderr=index == 1)
                        continue
                    write_log(handlers[index], chunk.decode(errors='replace'))
                    if verbose:
                        print(chunk.decode(errors='replace'), end='', flush=True)
                    buffers[index] += chunk
                    while b'\n' in buffers[index]:
                        line, buffers[index] = buffers[index].split(b'\n', 1)
                        events.line(line.decode(errors='replace'), stderr=index == 1)
                    if len(buffers[index]) > 1024 * 1024:
                        buffers[index] = b''  # Never retain unbounded tool output.
            # A CLI may close its streams before exiting.
            while process.poll() is None and not STOP:
                if time.monotonic() - started >= timeout:
                    timed_out = True
                    break
                time.sleep(0.1)
            if STOP or timed_out:
                terminate_group(process)
        returncode = process.wait()
        if STOP:
            return 'interrupted', None, returncode
        if timed_out:
            return 'unknown', None, returncode
        kind, reset = events.outcome(returncode)
        return kind, reset, returncode
    finally:
        if process is not None:
            terminate_group(process)
            for stream in (process.stdin, process.stdout, process.stderr):
                stream.close()
        for handler in handlers:
            handler.close()


def validate():
    result = subprocess.run([sys.executable, 'scripts/docs/check_structure.py'], cwd=ROOT,
                            capture_output=True, text=True, timeout=60)
    if result.returncode:
        raise RuntimeError('Documentation validation failed after the step:\n' + result.stdout + result.stderr)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('vendor', choices=VENDORS)
    parser.add_argument('--check', action='store_true', help='Check local CLI/login configuration without a model request.')
    parser.add_argument('--dry-run', action='store_true', help='Show the adapter command without creating files or calling the CLI.')
    parser.add_argument('--once', action='store_true', help='Attempt one step (still honors a saved cooldown), then exit.')
    parser.add_argument('--verbose', action='store_true', help='Also stream raw CLI output to the terminal.')
    parser.add_argument('--timeout', type=int, default=7200, help='Maximum seconds per invocation (default: 7200).')
    args = parser.parse_args()
    if args.timeout < 1:
        parser.error('--timeout must be positive')
    for name in ('PROMPT.md', 'GOAL.md', 'PROGRESS.md'):
        if not (ROOT / name).is_file():
            raise RuntimeError(f'Missing {name}.')
    prompt = (ROOT / 'PROMPT.md').read_text()
    if not prompt.strip() or len(prompt.encode()) > 16000:
        raise RuntimeError('PROMPT.md must be nonempty and at most 16 KB.')
    if args.dry_run:
        argv, stdin = command(args.vendor, args.vendor, '<contents of PROMPT.md>')
        print('Repository:', ROOT)
        print('Command:', ' '.join(argv))
        print('Prompt source: root PROMPT.md' + (' via stdin' if stdin else ' via --prompt-file'))
        print('Output:', ROOT / f'scripts/loop-{args.vendor}')
        return 0
    executable = check(args.vendor, ROOT)
    if args.check:
        announce(f'{args.vendor}: installed; local subscription-auth checks passed. No model request made.')
        if args.vendor == 'grok':
            announce('Grok has no documented auth-status command: cached login and account allowance still need a first-run check.')
        return 0
    signal.signal(signal.SIGINT, on_signal)
    signal.signal(signal.SIGTERM, on_signal)
    directory = ROOT / f'scripts/loop-{args.vendor}'
    directory.mkdir(mode=0o700, exist_ok=True)
    state_path = directory / 'state.json'
    with lock(directory / 'process.lock'):
        state = read_state(state_path)
        while not STOP:
            if proved():
                validate()
                announce('STATUS: PROVED; stopping. Structural validation does not verify the mathematics.')
                return 0
            retry_at = state.get('retry_at', 0)
            if retry_at > time.time():
                when = datetime.fromtimestamp(retry_at, timezone.utc).isoformat(timespec='seconds')
                announce(f'{args.vendor}: paused until {when} ({state.get("outcome", "cooldown")}). Ctrl+C stops.')
                wait_until(retry_at)
            if STOP:
                break
            with lock(ROOT / 'scripts/loop/workspace.lock', wait=True) as acquired:
                if not acquired or STOP:
                    break
                if proved():
                    validate()
                    return 0
                executable = check(args.vendor, ROOT)
                prompt = (ROOT / 'PROMPT.md').read_text()
                if not prompt.strip() or len(prompt.encode()) > 16000:
                    raise RuntimeError('PROMPT.md must be nonempty and at most 16 KB.')
                before = checkpoint_digest()
                argv, stdin = command(args.vendor, executable, prompt)
                state.update(outcome='running', retry_at=0, started_at=time.time())
                save_state(state_path, state)
                announce(f'{args.vendor}: starting a research step; logs in {directory.relative_to(ROOT)}.')
                kind, reset, code = run_process(argv, stdin, directory, args.timeout, args.verbose)
                if kind == 'success':
                    validate()
                    changed = checkpoint_digest() != before
                    state['no_progress'] = 0 if changed else state.get('no_progress', 0) + 1
                    if state['no_progress'] >= 3:
                        kind = 'fatal'
                        announce('Three successful CLI exits without changed progress/history; stopping to avoid a no-progress loop.')
                if kind == 'interrupted':
                    state.update(outcome=kind, exit_code=code)
                    save_state(state_path, state)
                    break
                failures = 0 if kind == 'success' else state.get('failures', 0) + 1
                unknowns = state.get('unknowns', 0) + 1 if kind == 'unknown' else 0
                if unknowns >= 3:
                    kind = 'fatal'
                if kind == 'success':
                    delay = 5 if changed else 60
                elif kind == 'quota':
                    delay = QUOTA_DELAYS[min(int(failures) - 1, len(QUOTA_DELAYS) - 1)]
                else:
                    delay = TRANSIENT_DELAYS[min(max(int(failures) - 1, 0), len(TRANSIENT_DELAYS) - 1)]
                retry_at = max(time.time() + delay, reset + 60 if reset else 0)
                state.update(outcome=kind, exit_code=code, failures=failures, unknowns=unknowns,
                             retry_at=retry_at, finished_at=time.time())
                save_state(state_path, state)
            # Release the repository during provider-specific cooldowns.
            announce(f'{args.vendor}: {kind} (exit {code}).')
            if kind == 'fatal':
                raise RuntimeError(f'Action needed; inspect {directory.relative_to(ROOT)}/stderr.log and stdout.log, fix the reported login/configuration/validation issue, then restart.')
            if args.once:
                return 0 if kind == 'success' else 1
    announce('Stopped; saved work is retained. The next run will inspect any unfinished step.')
    return 130


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (RuntimeError, OSError, subprocess.TimeoutExpired) as exc:
        print(f'Loop stopped: {exc}', file=sys.stderr)
        sys.exit(2)
