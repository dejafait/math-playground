#!/usr/bin/env python3
"""Replay unchanged1144, preserve originals, check ABI and every display bound."""
import ctypes as ct
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
from unittest.mock import patch

sys.dont_write_bytecode = True
here = Path(__file__).resolve().parent
source = here / 'certify_1144.py'
original_path = here / 'certificate-1144.json'
initial_path = here / 'certificate-1144-initial.json'
replay_path = here / 'certificate-1144-replay-1146.json'
old_bytes = original_path.read_bytes()
initial_bytes = initial_path.read_bytes()
original = json.loads(old_bytes)
initial = json.loads(initial_bytes)
write_text = Path.write_text

def redirect(path, data, *args, **kwargs):
    if path.resolve() != original_path:
        raise AssertionError(f'Unexpected certificate write: {path}')
    return write_text(replay_path, data, *args, **kwargs)

with patch.object(Path, 'write_text', redirect):
    ns = runpy.run_path(str(source))

replay = json.loads(replay_path.read_text())
m = ns['m']
with tempfile.TemporaryDirectory(prefix='.abi1146-', dir=here) as work:
    exe = Path(work) / 'probe'
    subprocess.run(['cc', '-std=c11', '-I/opt/homebrew/include',
                    str(here / 'abi_1146.c'), '-L/opt/homebrew/lib',
                    '-Wl,-rpath,/opt/homebrew/lib', '-lmpfr', '-lgmp',
                    '-o', str(exe)], check=True)
    abi = json.loads(subprocess.check_output([str(exe)], text=True))

ctypes_sizes = [ct.sizeof(m.Raw), ct.sizeof(ct.c_long), ct.sizeof(ct.c_int),
                ct.sizeof(ct.c_long), ct.sizeof(ct.c_ulong)]
ctypes_offsets = [getattr(m.Raw, key).offset for key in ('prec','sign','exp','limbs')]
checks = {
    'all_replayed_fields_identical': replay == original,
    'original_certificate_preserved': original_path.read_bytes() == old_bytes,
    'initial_certificate_preserved': initial_path.read_bytes() == initial_bytes,
    'no_verification_failures': replay['failures'] == [],
    'all_claims_true': all(replay['claims'].values()),
    'allocation_failure_retained': replay['allocation_test_passed'] is False,
    'both_failed_tests_retained': len(replay['failed_tests']) == 2,
    'initial_upper_failure_retained': initial['failures'] == ['upper_below_one'],
    'abi_sizes_match': abi['sizes'] == ctypes_sizes,
    'abi_offsets_match': abi['offsets'] == ctypes_offsets,
    'abi_rounding_match': abi['rounding'] == [m.DOWN, m.UP] == [3,2],
    'abi_versions_and_precision_match': abi['version'] == abi['header_version']
        == replay['mpfr_version'] == '4.2.2' and abi['precision'] == m.PREC == 384,
    'fixed_grid_match': replay['fixed_grid'] == initial['fixed_grid']
        == {'T':256,'h':'1/64','frequency_cells':16384,'simpson_panels':8192},
    'all_cumulative_blocks_match_initial': replay['quadrature_blocks'] == initial['quadrature_blocks'],
}
# Exact decimal comparisons, never binary64. These are every numeric
# weakening in C750i's conclusion and directed-computation paragraph.
bounds = {
    'simpson_error': (None,'2.657925e-8'),
    'inverse_rayleigh_enclosure': ('0.2925602441470644','0.3152920166028328'),
    'uniform_kernel_error': (None,'0.675793334'),
    'frequency_tail_norm': (None,'0.180084149'),
    'norm_upper': (None,'1.014419622'),
    'threshold': (None,'0.2691114763335869'),
    'threshold_miss': ('0.0234487678134775',None),
    'allocation_norm_lower': ('0.1358917539178126',None),
}
for key,(lower,upper) in bounds.items():
    lo, hi = map(F, replay[key])
    checks[key+'_ordered'] = lo <= hi
    if lower is not None:
        checks[key+'_display_lower'] = F(lower) < lo
    if upper is not None:
        checks[key+'_display_upper'] = hi < F(upper)
checks['decisive_exact_comparison'] = F(replay['norm_lower'][0]) > F(replay['threshold'][1])
checks['strict_miss_over_02344876'] = F(replay['norm_lower'][0])-F(replay['threshold'][1]) > F('.02344876')
# Compare every shared non-bookkeeping field, including nested derivative
# bounds and sums, with the initial certificate, not just a preview.
initial_changed_fields = sorted(key for key in original.keys() & initial.keys()
                                if original[key] != initial[key])
checks['all_numeric_enclosures_match_initial'] = (
    initial_changed_fields == ['claims','failures','script_sha256']
    and initial.keys() <= original.keys()
    and sorted(original.keys()-initial.keys()) ==
        ['failed_tests','initial_certificate','initial_failure_note'])
for key,path in [('script_sha256',source),('backend_sha256',ns['backend'])]:
    checks[key+'_matches_current_source'] = hashlib.sha256(path.read_bytes()).hexdigest() == replay[key]

failures = [key for key,passed in checks.items() if not passed]
out = {
    'scope':'Correctness audit/replay of fixed C750i only; original supported inequality unresolved.',
    'abi':abi, 'ctypes_sizes':ctypes_sizes,'ctypes_offsets':ctypes_offsets,
    'checks':checks,'failures':failures,
    'original_sha256':hashlib.sha256(old_bytes).hexdigest(),
    'initial_sha256':hashlib.sha256(initial_bytes).hexdigest(),
    'replay_sha256':hashlib.sha256(replay_path.read_bytes()).hexdigest(),
    'replay_path':str(replay_path.relative_to(here.parents[1])),
    'abi_source_sha256':hashlib.sha256((here/'abi_1146.c').read_bytes()).hexdigest(),
    'audit_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'display_bounds_checked':bounds,
    'initial_changed_shared_fields':initial_changed_fields,
    'decisive_lower':replay['norm_lower'],'required_threshold':replay['threshold'],
    'full_upper':replay['norm_upper'],'threshold_miss':replay['threshold_miss'],
    'failed_mathematical_tests':replay['failed_tests'],
}
path = here / 'certificate-audit-1146.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print('Audit checks passed:',sum(checks.values()),'required:',len(checks))
print('ABI sizes/offsets:',abi['sizes'],abi['offsets'],'MPFR:',abi['version'])
print('Audit failures:',failures)
print('Preserved original and initial certificates; exact fixed-grid replay:',replay_path)
print('Full audit certificate:',path)
if failures:
    raise SystemExit(1)
