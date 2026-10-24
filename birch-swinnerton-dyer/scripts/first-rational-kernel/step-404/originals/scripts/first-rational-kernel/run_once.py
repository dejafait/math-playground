"""One aggregate execution. No resume, retry, producer subprocess or network."""
import time
START = time.monotonic()
import signal


class StopWork(Exception):
    pass


def alarm(signum, frame):
    raise StopWork('work_reserve_deadline_174_seconds')


signal.signal(signal.SIGALRM, alarm)
signal.setitimer(signal.ITIMER_REAL, max(0.001, 174-(time.monotonic()-START)))
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import shutil
import sys
import traceback

sys.dont_write_bytecode = True
BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
OUT = BASE/'step-404'
LIMIT_BYTES = 134217728
STATE = {'stage': 'setup', 'panels': 0}
WRITTEN = 0
INVENTORY = {}
PANEL_HANDLE = None


def hashed(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(name, obj):
    global WRITTEN
    content = (json.dumps(obj, separators=(',', ':'), sort_keys=True)+'\n').encode()
    path = OUT/name
    old = path.stat().st_size if path.exists() else 0
    if WRITTEN-old+len(content)+65536 > LIMIT_BYTES:
        raise StopWork('output_budget_reserve')
    path.write_bytes(content)
    WRITTEN += len(content)-old


def progress(stage, panels):
    STATE.update(stage=stage, panels=panels)
    save('working-status.json', {**STATE, 'elapsed_seconds': time.monotonic()-START})
    print(json.dumps({'stage': stage, 'panels': panels,
                      'elapsed_seconds': round(time.monotonic()-START, 3)}), flush=True)


def emit_panel(record):
    global WRITTEN
    content = json.dumps(record, separators=(',', ':'))+'\n'
    size = len(content.encode())
    if WRITTEN+size+65536 > LIMIT_BYTES:
        raise StopWork('output_budget_reserve')
    PANEL_HANDLE.write(content)
    PANEL_HANDLE.flush()
    WRITTEN += size
    STATE.update(stage='production', panels=record['index']+1)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


failure = None
report = None
try:
    OUT.mkdir()  # Exclusive; existing partial evidence prevents a retry.
    sources = [BASE/'producer.py', BASE/'replay.py', BASE/'run_once.py']
    inputs = [ROOT/'lemmas/L031-independent-twist-five-ratio-certificate.md',
              ROOT/'lemmas/L101-conductor389-second-derivative-error-budget.md',
              ROOT/'lemmas/L102-capped-rational-taylor-kernel-enclosures.md',
              ROOT/'drafts/2026-10-22-rational-kernel-critical-audit.md',
              ROOT/'drafts/literature/2026-10-22-first-rational-kernel-implementation.md',
              ROOT/'ATTEMPTS/043-complex-order-two-quadratic-coefficient-import.md',
              ROOT/'ATTEMPTS/045-index-128-table-source-adaptation-stop.md',
              ROOT/'ATTEMPTS/046-fixed-derivative-backend-unavailable.md']
    for path in sources+inputs:
        rel = str(path.relative_to(ROOT))
        raw = path.read_bytes()
        dest = OUT/'originals'/rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if WRITTEN+len(raw)+65536 > LIMIT_BYTES:
            raise StopWork('input_copy_budget')
        dest.write_bytes(raw)
        WRITTEN += len(raw)
        INVENTORY[rel] = {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}
    # Count the selected static execution sources as well as their fixed copies.
    WRITTEN += sum(p.stat().st_size for p in sources)
    save('input-inventory.json', INVENTORY)
    save('manifest.json', {'step': 'BSD-2026-10-22-404-first-rational-kernel',
         'encoding': 'integer pair [lo,hi] means [lo/2^256,hi/2^256]; rational [numerator,positive_denominator]',
         'n': 1, 'grid_fractional_bits': 256, 'panels': 1016,
         'left_endpoint': '(index+8)/8', 'right_endpoint': '(index+9)/8',
         'factor_degrees': [128, 64, 64], 'product_slots': [193, 257],
         'coefficient_pairs_per_panel': [8385, 12545], 'log_terms': 128,
         'scalar_exp_terms': 128, 'scalar_squares': 16,
         'final_enlargement_grid_units': 2**72, 'arctangent_terms': [24, 25],
         'time_cap_seconds': 180, 'work_deadline_seconds': 174,
         'byte_cap': LIMIT_BYTES, 'diagnostic_stdout_allowance': 8192,
         'python': sys.version, 'no_floating_transcendentals': True,
         'source_paths': [str(p.relative_to(ROOT)) for p in sources],
         'replay': 'separate signed-rounding arithmetic, sign cases, reversed factor/loop traversal; no producer imports'})
    producer = load_module('kernel_producer', BASE/'producer.py')
    replay = load_module('kernel_independent_replay', BASE/'replay.py')
    STATE.update(stage='parameter', panels=0)
    parameter = producer.parameter()
    save('parameter.json', parameter)
    replay.verify_parameter(json.loads((OUT/'parameter.json').read_text()))
    # Reset the preliminary parameter-verification ledger: complete replay
    # below reconstructs it again and compares its own whole-run ledger.
    replay.LEDGER.clear()
    progress('production', 0)
    PANEL_HANDLE = (OUT/'panels.jsonl').open('x')
    result = producer.run(parameter, emit_panel, progress)
    PANEL_HANDLE.close()
    PANEL_HANDLE = None
    save('kernel.json', result)
    progress('replay', 0)
    with (OUT/'panels.jsonl').open() as handle:
        records = (json.loads(line) for line in handle)
        report = replay.run(json.loads((OUT/'parameter.json').read_text()), records,
                            json.loads((OUT/'kernel.json').read_text()), progress)
    save('replay.json', report)
    STATE.update(stage='complete', panels=1016)
except BaseException as exc:
    failure = {'type': type(exc).__name__, 'message': str(exc),
               'state': dict(STATE), 'traceback': traceback.format_exc()}
finally:
    # Only reporting/preservation runs after the fixed work deadline.
    signal.setitimer(signal.ITIMER_REAL, 0)
    if PANEL_HANDLE is not None:
        PANEL_HANDLE.close()
    preservation = []
    for relative, info in INVENTORY.items():
        original = ROOT/relative
        fixed = OUT/'originals'/relative
        preservation.append({'path': relative,
                             'original_matches': hashed(original) == info['sha256'],
                             'fixed_matches': hashed(fixed) == info['sha256']})
    if not all(row['original_matches'] and row['fixed_matches'] for row in preservation):
        if failure is None:
            failure = {'type': 'PreservationFailure', 'message': 'fixed/original input mismatch', 'state': dict(STATE)}
    if OUT.exists():
        save('preservation.json', {'files': preservation, 'count': len(preservation),
                                 'all_match': all(r['original_matches'] and r['fixed_matches'] for r in preservation)})
        if failure is not None:
            save('first-failure.json', failure)
        elapsed = time.monotonic()-START
        # Includes static sources, fixed copies, all files, stdout allowance,
        # and room for this final status file. No source generation occurs.
        actual_disk = sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
        static_bytes = sum((BASE/n).stat().st_size for n in ('producer.py', 'replay.py', 'run_once.py'))
        inclusive_bytes = actual_disk+static_bytes+8192+8192
        inclusive_seconds = math.ceil(elapsed)+2
        resources_ok = inclusive_seconds <= 180 and inclusive_bytes <= LIMIT_BYTES
        status = {'status': 'PASS' if failure is None and report is not None and resources_ok else 'STOP',
                  'state': STATE, 'first_failure': failure,
                  'complete_replay': report is not None, 'elapsed_before_final_write_seconds': elapsed,
                  'conservative_inclusive_seconds': inclusive_seconds,
                  'actual_disk_before_status_bytes': actual_disk,
                  'conservative_inclusive_bytes': inclusive_bytes,
                  'required_seconds': 180, 'required_bytes': LIMIT_BYTES,
                  'resource_checks': resources_ok, 'preserved_inputs': len(preservation),
                  'all_inputs_preserved': all(r['original_matches'] and r['fixed_matches'] for r in preservation)}
        save('status.json', status)
        final_elapsed = time.monotonic()-START
        assert final_elapsed <= inclusive_seconds, ('report_time_bound', final_elapsed, inclusive_seconds)
        print(json.dumps({'status': status['status'], 'stage': STATE,
                          'actual_seconds': final_elapsed, 'inclusive_seconds': inclusive_seconds,
                          'inclusive_bytes': inclusive_bytes, 'required_seconds': 180,
                          'required_bytes': LIMIT_BYTES, 'failure': None if failure is None else failure['message'],
                          'path': str((OUT/'status.json').relative_to(ROOT))}), flush=True)
