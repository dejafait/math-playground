#!/usr/bin/env python3
"""Audit frozen1148: preserve originals, replay every node, check ABI/output.

Analytic obligations are in C750j. No cap, pulse, mesh or phase is varied.
The replay uses the reviewed original interval backend; exact rational
decimal/sum checks and a freshly compiled C ABI probe are independent
checks, not a second implementation of quadrature or proof of MPFR.
"""
import contextlib
import ctypes as ct
from fractions import Fraction as F
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
from unittest.mock import patch

sys.dont_write_bytecode = True
here = Path(__file__).resolve().parent
root = here.parents[1]
source = here / 'certify_1148.py'
original_path = here / 'certificate-1148.json'
replay_path = here / 'certificate-1148-replay-1150.json'
original_bytes = original_path.read_bytes()
original = json.loads(original_bytes)
write_text = Path.write_text
load_module = importlib.util.spec_from_file_location
decimal_checks = {'endpoints_checked': 0, 'failures': []}


def exact_binary(m, value):
    """Base-two PREC digits give the exact finite MPFR significand."""
    exponent = ct.c_long()
    p = m.lib.mpfr_get_str(None, ct.byref(exponent), 2, m.PREC,
                          ct.byref(value.raw), m.DOWN)
    digits = ct.string_at(p).decode()
    m.lib.mpfr_free_str(p)
    n = len(digits.lstrip('-'))
    power = exponent.value - n
    # MPFR gives a special exponent for zero; handle it before shifting.
    mantissa = int(digits, 2)
    if mantissa == 0:
        return F(0)
    return F(mantissa) * (F(2) ** power)


def audited_spec(*args, **kwargs):
    spec = load_module(*args, **kwargs)
    exec_module = spec.loader.exec_module

    def load_and_instrument(m):
        exec_module(m)
        original_dump = m.I.dump

        def checked_dump(interval):
            result = original_dump(interval)
            lo, hi = map(F, result)
            passed = lo <= exact_binary(m, interval.lo) <= exact_binary(m, interval.hi) <= hi
            decimal_checks['endpoints_checked'] += 2
            if not passed:
                decimal_checks['failures'].append(result)
            return result

        m.I.dump = checked_dump

    spec.loader.exec_module = load_and_instrument
    return spec


def redirect(path, data, *args, **kwargs):
    if path.resolve() != original_path:
        raise AssertionError(f'Unexpected certificate write: {path}')
    return write_text(replay_path, data, *args, **kwargs)


with patch.object(Path, 'write_text', redirect), \
     patch.object(importlib.util, 'spec_from_file_location', audited_spec), \
     contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(source))
replay = json.loads(replay_path.read_text())
m = ns['m']

# Recompile the existing independent C probe without changing its source.
with tempfile.TemporaryDirectory(prefix='.abi1150-', dir=here) as work:
    exe = Path(work) / 'probe'
    subprocess.run(['cc', '-std=c11', '-I/opt/homebrew/include',
                    str(here / 'abi_1146.c'), '-L/opt/homebrew/lib',
                    '-Wl,-rpath,/opt/homebrew/lib', '-lmpfr', '-lgmp',
                    '-o', str(exe)], check=True)
    abi = json.loads(subprocess.check_output([str(exe)], text=True))
sizes = [ct.sizeof(m.Raw), ct.sizeof(ct.c_long), ct.sizeof(ct.c_int),
         ct.sizeof(ct.c_long), ct.sizeof(ct.c_ulong)]
offsets = [getattr(m.Raw, key).offset for key in ('prec','sign','exp','limbs')]


def endpoints(key):
    return tuple(map(F, replay[key]))


checks = {
    'all_replayed_fields_identical': replay == original,
    'original_certificate_byte_preserved': original_path.read_bytes() == original_bytes,
    'all_original_claims_true': len(replay['claims']) == 12 and all(replay['claims'].values()),
    'original_verification_failures_empty': replay['failures'] == [],
    'three_failed_mathematical_tests_preserved': len(replay['failed_mathematical_tests']) == 3
        and replay['failed_mathematical_tests'] == original['failed_mathematical_tests'],
    'all_dump_endpoints_outward': decimal_checks['failures'] == [],
    'abi_sizes_match': abi['sizes'] == sizes,
    'abi_offsets_match': abi['offsets'] == offsets,
    'abi_rounding_match': abi['rounding'] == [m.DOWN, m.UP] == [3,2],
    'abi_version_and_precision_match': abi['version'] == abi['header_version']
        == replay['mpfr_version'] == '4.2.2' and abi['precision'] == m.PREC == 384,
    'frozen_parameters': replay['scheme']['T'] == 256
        and replay['scheme']['panel_width'] == '1/16'
        and replay['scheme']['gauss_order'] == 2
        and replay['scheme']['panels'] == 4096
        and replay['scheme']['phase_count'] == 4096
        and replay['scheme']['tested_phase'] == 'exactly 0',
}

# Independent exact decimal traversal of every saved node/contribution.
# Sums of rounded term endpoints are enclosures too. Their intersection
# with the replay's accumulators checks all blocks, not just a preview.
sumlo, sumhi = F(0), F(0)
node_failures, block_checks = [], []
nodes = replay['positive_frequency_nodes']
blocks = replay['cumulative_blocks']
for index, row in enumerate(nodes):
    panel, sign = divmod(index, 2)[0], (-1 if index % 2 == 0 else 1)
    tlo, thi = map(F, row['t'])
    qlo, qhi = map(F, row['q'])
    flo, fhi = map(F, row['F2'])
    vlo, vhi = map(F, row['term'])
    passed = (row['panel'] == panel and row['sign'] == sign
              and F(panel,16) < tlo <= thi < F(panel+1,16)
              and 0 < qlo <= qhi and 0 <= flo <= fhi and 0 <= vlo <= vhi)
    if not passed:
        node_failures.append(index)
    sumlo, sumhi = sumlo + vlo, sumhi + vhi
    if (index+1) % 512 == 0:
        block = blocks[(index+1)//512-1]
        alo, ahi = map(F, block['quadratic_sum'])
        block_checks.append({'panels_completed': (index+1)//2,
                             'recorded_index_correct': block['panels_completed'] == (index+1)//2,
                             'sum_intersection': max(sumlo,alo) <= min(sumhi,ahi),
                             'sum_discrepancy_below_1e_minus_100':
                                 abs(sumlo-alo) < F('1e-100') and abs(sumhi-ahi) < F('1e-100')})
checks['every_node_panel_geometry_and_sign'] = not node_failures and len(nodes) == 8192
checks['every_cumulative_sum_checked'] = len(block_checks) == 16 and all(
    row['recorded_index_correct'] and row['sum_intersection']
    and row['sum_discrepancy_below_1e_minus_100'] for row in block_checks)
checks['all_signed_features_counted'] = replay['scheme']['feature_columns'] == 2*len(nodes) == 16384
checks['sum_endpoint_width_below_1e_minus_100'] = sumhi-sumlo < F('1e-100')

# Every numerical weakening printed in C750j, compared as exact rationals.
bounds = {
    'capped_energy': ('.29186289','.29231410'),
    'required_capped_energy': ('.29282701','.29282702'),
    'capped_form': ('-.00096412','-.00051291155'),
    'kernel_fourth_derivative_majorant': (None,'2210.326825'),
    'supported_operator_error': (None,'.002862830'),
    'phase_cover_error': (None,'.002850085'),
    'quadratic_error': (None,'.000225599834'),
    'base_coercivity': ('1.83702738',None),
    'paid_base_coercivity': ('1.83131447',None),
    'gram_norm_lower_quotient': ('1.00510150','1.00510151'),
    'paid_gram_norm_lower_quotient': ('1.00823698','1.00823700'),
    'scalar_arithmetic_width': (None,'7.188e-113'),
}
for key, (lower,upper) in bounds.items():
    lo,hi = endpoints(key)
    checks[key+'_ordered'] = lo <= hi
    if lower is not None:
        checks[key+'_display_lower'] = F(lower) < lo
    if upper is not None:
        checks[key+'_display_upper'] = hi < F(upper)

# No binary64 decision: certify negativity and Gram failure directly from
# independently accumulated decimal term bounds, with printed full errors.
blo,bhi = endpoints('base_pulse_energy')
elo,ehi = endpoints('quadratic_error')
nlo,nhi = endpoints('norm_squared')
dlo,dhi = endpoints('paid_base_coercivity')
checks['independent_exact_sum_paid_residual_negative'] = bhi - sumlo + ehi < F('-.00051291155')
checks['independent_exact_sum_gram_lower_over_one'] = sumlo / bhi > F('1.00510150')
checks['independent_exact_sum_paid_gram_lower_over_one'] = sumlo/(dhi*nhi) > F('1.00823698')
checks['positive_denominators'] = blo > 0 and dlo > 0 and nlo > 0
for key,path in [('script_sha256',source),('backend_sha256',ns['backend'])]:
    checks[key+'_matches_current_file'] = hashlib.sha256(path.read_bytes()).hexdigest() == replay[key]

failures = [key for key,passed in checks.items() if not passed]
out = {
    'scope':'Fixed C750j conceptual and arithmetic audit only; original J allocation unresolved.',
    'independence':'Original quadrature and reviewed MPFR backend replayed; exact rational full-sum/output checks and fresh C ABI probe. Not a second quadrature implementation or formal library verification.',
    'abi':abi,'ctypes_sizes':sizes,'ctypes_offsets':offsets,'backend_library':m.lib_path,
    'decimal_checks':decimal_checks,'node_failure_indices':node_failures,
    'full_node_count':len(nodes),'full_cumulative_block_checks':block_checks,
    'checks':checks,'failures':failures,'display_bounds_checked':bounds,
    'independent_sum_bounds_exact_rational':[str(sumlo),str(sumhi)],
    'independent_paid_residual_upper_exact_rational':str(bhi-sumlo+ehi),
    'original_sha256':hashlib.sha256(original_bytes).hexdigest(),
    'replay_sha256':hashlib.sha256(replay_path.read_bytes()).hexdigest(),
    'audit_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'abi_source_sha256':hashlib.sha256((here/'abi_1146.c').read_bytes()).hexdigest(),
    'replay_path':str(replay_path.relative_to(root)),
    'capped_form':replay['capped_form'],'required_residual':'>=0',
    'gram_norm_lower_quotient':replay['gram_norm_lower_quotient'],'required_gram_norm':'<=1',
    'paid_gram_norm_lower_quotient':replay['paid_gram_norm_lower_quotient'],
    'failed_mathematical_tests':replay['failed_mathematical_tests'],
}
path = here / 'certificate-audit-1150.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print('Audit checks passed:',sum(checks.values()),'required:',len(checks))
print('All nodes:',len(nodes),'blocks:',len(block_checks),'outward endpoints:',decimal_checks['endpoints_checked'])
print('ABI sizes/offsets:',abi['sizes'],abi['offsets'],'MPFR:',abi['version'])
print('Paid capped residual < -0.00051291155; required >=0.')
print('Gram lower >1.00510150 (paid >1.00823698); required <=1.')
print('Audit failures:',failures,'node failures:',len(node_failures),'decimal failures:',len(decimal_checks['failures']))
print('Failed mathematical tests retained:',out['failed_mathematical_tests'])
print('Preserved original; full replay:',replay_path)
print('Full audit:',path)
if failures:
    raise SystemExit(1)
