#!/usr/bin/env python3
"""Codex subscription-loop supervisor (Python standard library, macOS/Linux)."""
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
from research import assess, resume
from codex import check, command
from portfolio import registry, migrate, choose

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
                    announce('Another loop is editing the repository; waiting for its checkpoint.')
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
        for key in ('retry_at', 'failures', 'unknowns', 'no_progress', 'exploration_turns', 'stalled_turns'):
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


def proved(problem=None):
    return any(line.strip() in {'STATUS: PROVED', 'STATUS: DISPROVED'} for line in ((ROOT / problem if problem else ROOT) / 'PROGRESS.md').read_text().splitlines())


def checkpoint_digest(problem=None):
    notebook = ROOT / problem if problem else ROOT
    digest = hashlib.sha256()
    files = [notebook / 'PROGRESS.md', *sorted((notebook / 'history').glob('*.md'))]
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


def run_process(argv, stdin, directory, timeout, verbose=False, notebook=None):
    events = Events()
    handlers = logs(directory)
    started = time.monotonic()
    env = dict(os.environ, NO_COLOR='1', TERM='dumb')
    process = None
    timed_out = False
    try:
        process = subprocess.Popen(argv, cwd=notebook or ROOT, env=env, stdin=subprocess.PIPE,
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


def validate(problem=None):
    result = subprocess.run([sys.executable, 'scripts/docs/check_structure.py'] + (['--problem', problem] if problem else []), cwd=ROOT,
                            capture_output=True, text=True, timeout=60)
    if result.returncode:
        raise RuntimeError('Documentation validation failed after the step:\n' + result.stdout + result.stderr)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check local CLI/login configuration without a model request.')
    parser.add_argument('--dry-run', action='store_true', help='Show the Codex command without creating files or calling the CLI.')
    parser.add_argument('--resume-research', metavar='PROBLEM', help='Renew only this problem’s research budget; retain quota cooldowns.')
    parser.add_argument('--problem', help='Run only this registered problem instead of the full rotation.')
    parser.add_argument('--once', action='store_true', help='Attempt one step (still honors a saved cooldown), then exit.')
    parser.add_argument('--verbose', action='store_true', help='Also stream raw CLI output to the terminal.')
    parser.add_argument('--timeout', type=int, default=7200, help='Maximum seconds per invocation (default: 7200).')
    args = parser.parse_args()
    if args.timeout < 1:
        parser.error('--timeout must be positive')
    rows = registry(ROOT)
    ids = {row['id'] for row in rows}
    if (args.problem and args.problem not in ids) or (args.resume_research and args.resume_research not in ids):
        parser.error('Unknown problem ID')
    for name in ('PROMPT.md', 'GOAL.md'):
        if not (ROOT / name).is_file():
            raise RuntimeError(f'Missing {name}.')
    prompt = (ROOT / 'PROMPT.md').read_text()
    if not prompt.strip() or len(prompt.encode()) > 16000:
        raise RuntimeError('PROMPT.md must be nonempty and at most 16 KB.')
    if args.dry_run:
        argv, stdin = command('codex', '<contents of PROMPT.md>')
        print('Repository:', ROOT)
        print('Command:', ' '.join(argv))
        print('Prompt source: root PROMPT.md via stdin')
        print('Rotation:', ', '.join(row['id'] for row in rows if row['enabled']))
        print('Selected problem:', args.problem or 'round-robin')
        print('Output:', ROOT / 'scripts/loop-codex')
        return 0
    executable = check(ROOT)
    if args.check:
        announce('codex: installed; local subscription-auth checks passed. No model request made.')
        return 0
    signal.signal(signal.SIGINT, on_signal)
    signal.signal(signal.SIGTERM, on_signal)
    directory = ROOT / 'scripts/loop-codex'
    directory.mkdir(mode=0o700, exist_ok=True)
    state_path = directory / 'state.json'
    with lock(directory / 'process.lock'):
        state = migrate(read_state(state_path))
        if args.resume_research:
            resume(state['problems'].setdefault(args.resume_research, {}))
        save_state(state_path, state)
        while not STOP:
            problem, next_problem = choose(rows, state, proved, args.problem)
            if problem is None:
                validate()
                announce('No eligible problems remain: disabled, resolved, or research-halted.')
                return 2 if any(p.get('research_halt') for p in state['problems'].values()) else 0
            notebook = ROOT / problem
            local = state['problems'].setdefault(problem, {})
            retry_at = state.get('retry_at', 0)
            if retry_at > time.time():
                when = datetime.fromtimestamp(retry_at, timezone.utc).isoformat(timespec='seconds')
                announce(f'codex: paused until {when} ({state.get("outcome", "cooldown")}). Ctrl+C stops.')
                wait_until(retry_at)
            if STOP:
                break
            with lock(ROOT / 'scripts/loop/workspace.lock', wait=True) as acquired:
                if not acquired or STOP:
                    break
                if proved(problem):
                    validate(problem)
                    state['next_problem'] = next_problem
                    save_state(state_path, state)
                    continue
                executable = check(ROOT)
                prompt = (ROOT / 'PROMPT.md').read_text()
                if not prompt.strip() or len(prompt.encode()) > 16000:
                    raise RuntimeError('PROMPT.md must be nonempty and at most 16 KB.')
                before = checkpoint_digest(problem)
                before_progress = (notebook / 'PROGRESS.md').read_text()
                prompt = (f'Active problem: {problem}. Working directory: {notebook}. '
                          'Shared instructions are ../GOAL.md and ../PROMPT.md. '
                          'All notebook paths are relative to this working directory. '
                          f'Use --problem {problem} with the shared documentation checker.\n\n' + prompt)
                argv, stdin = command(executable, prompt)
                state.update(outcome='running', retry_at=0, started_at=time.time())
                save_state(state_path, state)
                output = directory / problem
                output.mkdir(exist_ok=True)
                announce(f'codex: starting {problem}; logs in {output.relative_to(ROOT)}.')
                started = time.monotonic()
                kind, reset, code = run_process(argv, stdin, output, args.timeout, args.verbose, notebook)
                local['elapsed_seconds'] = local.get('elapsed_seconds', 0) + time.monotonic() - started
                if kind == 'success':
                    try:
                        validate(problem)
                    except RuntimeError as exc:
                        local['research_halt'] = str(exc)
                    changed = checkpoint_digest(problem) != before
                    reason = assess(local, before_progress, (notebook / 'PROGRESS.md').read_text(), changed)
                    if reason and not proved(problem):
                        local['research_halt'] = reason
                    if local.get('research_halt'):
                        announce(f"Research halted for {problem}: {local['research_halt']}")
                local['last_outcome'] = kind
                if kind not in ('quota', 'transient', 'interrupted', 'fatal'):
                    local['turns'] = local.get('turns', 0) + 1
                    state['next_problem'] = next_problem
                if kind == 'interrupted':
                    state.update(outcome=kind, exit_code=code)
                    save_state(state_path, state)
                    break
                failures = 0 if kind == 'success' else state.get('failures', 0) + 1
                unknowns = local.get('unknowns', 0) + 1 if kind == 'unknown' else (0 if kind == 'success' else local.get('unknowns', 0))
                local['unknowns'] = unknowns
                if unknowns >= 3:
                    local['research_halt'] = 'Three unclassified failures for this notebook; inspect its logs.'
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
            # Release the repository during cooldowns.
            announce(f'codex: {kind} (exit {code}).')
            if kind == 'fatal':
                raise RuntimeError(f'Action needed; inspect {output.relative_to(ROOT)}/stderr.log and stdout.log, fix the reported login/configuration/validation issue, then restart.')
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
