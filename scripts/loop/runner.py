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
from research import assess, resume, recover, field, balance_instruction
from literature import prepare, instruction, validate_turn, READY
from codex import check, command
from routing import select as select_route, recommendation, telemetry, INSTRUCTION as ROUTING_INSTRUCTION
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
        observed = telemetry(events.thread_id)
        observed.update(thread_id=events.thread_id, usage=events.usage)
        (directory / 'telemetry.json').write_text(json.dumps(observed))
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


def show_status(rows, state, only=None):
    for row in rows:
        slug = row['id']
        if only and slug != only:
            continue
        local = state['problems'].get(slug, {})
        status = field((ROOT / slug / 'PROGRESS.md').read_text(), 'STATUS') or 'UNKNOWN'
        if not row['enabled']:
            scheduling = 'disabled'
        elif local.get('research_halt'):
            scheduling = 'halted: ' + local['research_halt']
        elif local.get('research_recovery'):
            scheduling = 'recovery queued: ' + local['research_recovery']
        elif proved(slug):
            scheduling = 'resolved'
        else:
            scheduling = 'eligible'
        route = local.get('last_route', {})
        mix = local.get('turn_mix', [])
        print(f"{slug}: enabled={row['enabled']}; {status}; {scheduling}; recent mathematical={mix.count('RESEARCH')}, literature={mix.count('LITERATURE')}; requested={route.get('model', 'unknown')}/{route.get('effort', 'unknown')}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--status', action='store_true', help='Show every problem’s scheduling state and reason; no model call or state changes.')
    parser.add_argument('--recover-research', action='store_true', help='Queue recovery for saved stops and exit without calling the model.')
    parser.add_argument('--check', action='store_true', help='Check local CLI/login configuration without a model request.')
    parser.add_argument('--dry-run', action='store_true', help='Show the Codex command without creating files or calling the CLI.')
    parser.add_argument('--resume-research', metavar='PROBLEM', help='Renew only this problem’s research budget; retain quota cooldowns.')
    parser.add_argument('--problem', help='Run only this registered problem instead of the full rotation.')
    parser.add_argument('--once', action='store_true', help='Attempt one step (still honors a saved cooldown), then exit.')
    parser.add_argument('--verbose', action='store_true', help='Also stream raw CLI output to the terminal.')
    parser.add_argument('--timeout', type=int, default=7200, help='Maximum seconds per invocation (default: 7200).')
    args = parser.parse_args()
    if sum((args.status, args.recover_research, args.check, args.dry_run)) > 1:
        parser.error('Choose only one of --status, --recover-research, --check, --dry-run')
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
    if args.status:
        show_status(rows, migrate(read_state(ROOT / 'scripts/loop-codex/state.json')), args.problem)
        return 0
    if args.check:
        check(ROOT)
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
        for row in rows:
            if row['enabled'] and (not args.problem or row['id'] == args.problem):
                reason = recover(state['problems'].setdefault(row['id'], {}))
                if reason:
                    announce(f"Recovery queued for {row['id']}: {reason}")
        save_state(state_path, state)
        if args.recover_research:
            show_status(rows, state, args.problem)
            return 0
        while not STOP:
            problem, next_problem = choose(rows, state, proved, args.problem)
            if problem is None:
                validate()
                announce('No eligible problems remain. Per-problem reasons:')
                show_status(rows, state, args.problem)
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
                if proved(problem) and not local.get('research_recovery'):
                    validate(problem)
                    state['next_problem'] = next_problem
                    save_state(state_path, state)
                    continue
                try:
                    executable = check(ROOT)
                except (RuntimeError, OSError, subprocess.TimeoutExpired) as exc:
                    state.update(outcome='configuration', retry_at=time.time() + 300)
                    save_state(state_path, state)
                    announce(f'Configuration needs attention: {exc} Retrying in 5 minutes; Ctrl+C stops.')
                    if args.once:
                        return 1
                    continue
                prompt = (ROOT / 'PROMPT.md').read_text()
                if not prompt.strip() or len(prompt.encode()) > 16000:
                    raise RuntimeError('PROMPT.md must be nonempty and at most 16 KB.')
                before = checkpoint_digest(problem)
                before_progress = (notebook / 'PROGRESS.md').read_text()
                literature_context = prepare(notebook, before_progress)
                recovery = local.get('research_recovery')
                first_stop = local.get('first_research_stop', {}).get('reason', '')
                metadata_ready = (bool(recovery) and (recovery.startswith(('Ready assessments', 'Incomplete or duplicate',
                                                                         'Missing literature', 'Literature assessment',
                                                                         'Recovery remains stalled')) )
                                  and literature_context['decision'] in READY
                                  and first_stop.startswith(('Ready assessments', 'Incomplete or duplicate',
                                                             'Missing literature', 'Literature assessment')))
                if metadata_ready:
                    local.pop('require_new_target', None)
                if recovery:
                    if literature_context['decision'] not in READY:
                        literature_context['decision'] = 'REVIEW_REQUIRED'
                    literature_context['reason'] = 'Recovery required: ' + recovery
                prompt = (f'Active problem: {problem}. Working directory: {notebook}. '
                          'Shared instructions are ../GOAL.md and ../PROMPT.md. '
                          'All notebook paths are relative to this working directory. '
                          f'Use --problem {problem} with the shared documentation checker.\n\n'
                          + instruction(literature_context) + balance_instruction(local, literature_context['decision'] in READY) + '\n' + prompt)
                if recovery:
                    prompt += ('\nSupervisor recovery turn: ' + recovery
                               + '. Repair the reported process issue or reassess the exhausted approach. '
                               'For a stalled or exhausted route, document a materially different mechanism or gap '
                               'and a concrete next test; do not repeat the same retrieval or rename a failed route. '
                               'If the saved assessment is ready, perform a concrete mathematical attempt; '
                               'otherwise repair or complete the source assessment. '
                               'Do not claim progress merely to reset counters. Any rejected resolution remains '
                               'unverified: use STATUS: IN_PROGRESS until a later valid critical review.\n')
                    if local.get('require_new_target'):
                        prompt += ('A different Next action is required. The current route is exhausted or '
                                   'has repeatedly failed recovery. Preserve its obstruction in ATTEMPTS; '
                                   'compare up to three distinct mechanisms and select a different one. '
                                   'If a source cannot be accessed, park dependent work and choose an '
                                   'independent target. Do not repeat the same access attempts. Save a '
                                   'assessment for the new target; a literature turn may finish approving it.\n')
                route = select_route(before_progress, local, literature_context['decision'] in READY)
                prompt += ROUTING_INSTRUCTION + f'\nCurrent settings: {route["model"]}, {route["effort"]}. One bounded step, then checkpoint.\n'
                argv, stdin = command(executable, prompt, route)
                local['last_route'] = route
                state.update(outcome='running', retry_at=0, started_at=time.time())
                save_state(state_path, state)
                output = directory / problem
                output.mkdir(exist_ok=True)
                announce(f'codex: starting {problem} with {route["model"]}/{route["effort"]} ({route["reason"]}); logs in {output.relative_to(ROOT)}.')
                (output / 'telemetry.json').unlink(missing_ok=True)
                started = time.monotonic()
                try:
                    kind, reset, code = run_process(argv, stdin, output, args.timeout, args.verbose, notebook)
                except (OSError, subprocess.TimeoutExpired) as exc:
                    announce(f'Invocation failed: {exc}; will retry.')
                    kind, reset, code = 'unknown', None, -1
                observation_path = output / 'telemetry.json'
                observed = json.loads(observation_path.read_text()) if observation_path.exists() else telemetry(None)
                record = dict(route, **observed, elapsed_seconds=time.monotonic() - started, outcome=kind, validation='not_accepted')
                local['routing_history'] = (local.get('routing_history', []) + [record])[-10:]
                local['elapsed_seconds'] = local.get('elapsed_seconds', 0) + time.monotonic() - started
                if kind == 'success':
                    try:
                        validate(problem)
                    except RuntimeError as exc:
                        local['research_halt'] = str(exc)
                    changed = checkpoint_digest(problem) != before
                    after_progress = (notebook / 'PROGRESS.md').read_text()
                    reason = local.get('research_halt') or validate_turn(notebook, literature_context, after_progress)
                    if not reason and recovery and proved(problem):
                        reason = 'Recovery must leave a rejected resolution IN_PROGRESS for later critical review.'
                    if (not reason and recovery and field(after_progress, 'STEP_OUTCOME') == 'STALLED'
                            and prepare(notebook, after_progress)['decision'] not in READY):
                        reason = 'Recovery remains stalled; reassess the route instead of renewing its budget.'
                    if (not reason and recovery and local.get('require_new_target')
                            and field(after_progress, 'Next action') == literature_context['target']):
                        reason = 'Recovery must select a different target after repeated failure or an exhausted approach.'
                    if not reason and recovery:
                        # Require a fresh valid report before renewing the approach budget.
                        probe = dict(local)
                        assess(probe, before_progress, after_progress, changed)
                        if probe.get('no_progress'):
                            reason = 'Recovery needs a fresh valid research step report.'
                        else:
                            resume(local)
                            local.pop('research_recovery', None)
                            local.pop('require_new_target', None)
                            local['recovery_attempts'] = 0
                    if (not reason and not recovery and literature_context['decision'] in READY
                            and field(after_progress, 'STEP_KIND') == 'LITERATURE'
                            and not field(after_progress, 'LITERATURE_REASON')):
                        reason = 'Ready target needs a mathematical attempt or a specific LITERATURE_REASON.'
                    if not reason:
                        reason = assess(local, before_progress, after_progress, changed)
                        if not local.get('no_progress'):
                            local['next_route'] = recommendation(after_progress) or {}
                    record['validation'] = reason or ('invalid_step_report' if local.get('no_progress') else 'accepted')
                    if reason:
                        local['research_halt'] = reason
                    if local.get('research_halt'):
                        announce(f"Research stop for {problem}: {local['research_halt']}")
                with (output / 'routing.jsonl').open('a') as handle:
                    handle.write(json.dumps(dict(record, started_at=state['started_at'])) + '\n')
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
                if local.get('research_halt'):
                    reason = recover(local)
                    announce(f'Recovery queued for {problem}: {reason}')
                if kind == 'success':
                    delay = 5 if changed else 60
                elif kind == 'fatal':
                    delay = 300
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
                announce(f'Configuration/service error; retrying in 5 minutes. Details: {output.relative_to(ROOT)}/stderr.log and stdout.log. Ctrl+C stops.')
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
