"""Replay every L700 enclosure and check the complete stored certificate.

The original generator is executed unchanged, with only __file__ selecting
a separate output path. Exact Fraction checks independently validate the
stored elementary-constant intervals and every paid phase-cell margin.
No floating diagnostic or approximate Picard profile is an input.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import sys

base = Path(__file__).resolve().parent
source = base / 'centered-gap-residue-certificate-131.py'
original_path = source.with_suffix('.json')
replay_path = base / 'centered-gap-residue-certificate-replay-133.json'
report_path = Path(__file__).with_suffix('.json')
original_bytes = original_path.read_bytes()
original = json.loads(original_bytes)
namespace = {'__name__': '__main__', '__file__': str(replay_path.with_suffix('.py'))}
exec(compile(source.read_text(), str(source), 'exec'), namespace)
replay = json.loads(replay_path.read_text())

failures = []


def check(name, condition):
    if not condition:
        failures.append(name)
    return bool(condition)


def bounds(value):
    return tuple(F(x) for x in value)


def atan_bounds(q):
    # 120 terms, ending negative, then an explicit next-term upper bound.
    partial = sum((F((-1)**k, (2*k+1)*q**(2*k+1)) for k in range(120)), F(0))
    return partial, partial + F(1, 241*q**241)


a5, a239 = atan_bounds(5), atan_bounds(239)
pi_bounds = 16*a5[0]-4*a239[1], 16*a5[1]-4*a239[0]
stored_pi = bounds(original['pi'])
pi_ok = check('pi containment', stored_pi[0] <= pi_bounds[0] <= pi_bounds[1] <= stored_pi[1])
ln2 = 2*sum((F(1, (2*k+1)*3**(2*k+1)) for k in range(100)), F(0))
ln2_tail = F(2, 201*3**201)/(1-F(1, 9))
stored_log = bounds(original['log_K'])
log_ok = check('log K containment', stored_log[0] <= 15*ln2 <= 15*(ln2+ln2_tail) <= stored_log[1])
J, K, grid = original['J'], original['K'], original['grid']
check('fixed parameters', (J, K, grid, original['precision']) == (64, 32768, 2048, 70))
delta = F(J, K) + F(J*J, 2*K)/(1-F(J, K+1))
delta_upper = F(original['infinite_product_phase_error_upper'])
grid_upper = F(original['continuous_grid_cost_upper'])
check('infinite product cost', delta <= delta_upper)
check('continuous grid cost', F(J, grid)*stored_pi[1] <= grid_upper)
check('required margin', F(original['required_paid_margin']) == F(1, 2))
check('original unchanged', original_path.read_bytes() == original_bytes)
check('complete replay equality', original == replay)
check('empty generator failures', original['failures'] == replay['failures'] == [])
check('product count', len(original['products']) == J)
check('phase cell count', len(original['grid_witnesses']) == grid)

product_checks = []
for index, p in enumerate(original['products'], 1):
    same = p == replay['products'][index-1]
    scaled = [bounds(p[field]) for field in ('scaled_real', 'scaled_imag')]
    units = [bounds(p[field]) for field in ('unit_real', 'unit_imag')]
    ok = (p['j'] == index and same and p['binary_shift'] > 0
          and all(hi-lo == 1 and lo.denominator == hi.denominator == 1 for lo, hi in scaled)
          and any(lo > 0 or hi < 0 for lo, hi in scaled)
          and all(lo <= hi for lo, hi in units))
    check(f'product {index}', ok)
    product_checks.append({'j': index, 'complete_record_matches': same,
                           'integer_scaling_and_unit_intervals_valid': ok})

cell_checks = []
paid_values = []
for index, row in enumerate(original['grid_witnesses']):
    paid = F(row['paid_margin_lower'])
    pos, neg = F(row['positive_lower']), F(row['negative_magnitude_lower'])
    paid_values.append(paid)
    same = row == replay['grid_witnesses'][index]
    ok = (row['k'] == index and same and 1 <= row['positive_j'] <= J
          and 1 <= row['negative_j'] <= J and row['positive_j'] != row['negative_j']
          and paid <= min(pos, neg)-delta_upper-grid_upper and paid > F(1, 2))
    check(f'phase cell {index}', ok)
    cell_checks.append({'k': index, 'complete_record_matches': same,
                        'exact_rational_payment_and_strict_margin_valid': ok})

worst = min(paid_values)
worst_index = paid_values.index(worst)
check('actual minimum', worst == F(original['actual_paid_margin_lower']))
check('minimum index', worst_index == original['worst_grid_index'])
report = {
    'kind': 'L700 complete certificate replay and exact-rational payment audit',
    'python': sys.version,
    'source': source.name,
    'source_sha256': sha256(source.read_bytes()).hexdigest(),
    'original_certificate_sha256': sha256(original_bytes).hexdigest(),
    'replay_certificate_sha256': sha256(replay_path.read_bytes()).hexdigest(),
    'original_preserved': original_path.read_bytes() == original_bytes,
    'complete_replay_equal': original == replay,
    'pi_exact_rational_containment': pi_ok,
    'log_K_exact_rational_containment': log_ok,
    'product_count': len(product_checks), 'phase_cell_count': len(cell_checks),
    'actual_paid_margin_lower': original['actual_paid_margin_lower'],
    'required_paid_margin': '0.5', 'worst_grid_index': worst_index,
    'product_checks': product_checks, 'cell_checks': cell_checks,
    'failures': failures,
    'qualification': 'Arithmetic replay plus reviewed generator; analytic transfer and quantifiers are proved in L700. No formal verification.'
}
report_path.write_text(json.dumps(report, indent=2)+'\n')
print('Audit:', 'PASS' if not failures else 'FAIL')
print('Products checked:', len(product_checks), '; phase cells checked:', len(cell_checks))
print('Actual paid lower margin:', original['actual_paid_margin_lower'], '; required > 0.5')
print('Failures:', failures)
print('Full audit:', report_path)
print('Full replay:', replay_path)
assert not failures
