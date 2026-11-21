#!/usr/bin/env python3
"""Independent exact replay of every mathematical field in certificate1631."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'extension_constants_1631.json'
saved = json.loads(SOURCE.read_text())
checks = []


def rat(q):
    q = Q(q)
    return {'numerator': str(q.numerator), 'denominator': str(q.denominator)}


def decode(q):
    assert set(q) == {'numerator', 'denominator'}
    return Q(int(q['numerator']), int(q['denominator']))


def verify(name, actual, expected):
    checks.append({'name': name, 'passed': actual == expected})


def exp_series(x, n):
    # Direct powers/factorials, independent of the production recurrence.
    x = Q(x)
    assert 0 < x < n + 2
    total = sum((x**k / factorial(k) for k in range(n + 1)), Q(0))
    omitted = x**(n + 1) / factorial(n + 1)
    ratio = x / (n + 2)
    upper = total + omitted / (1 - ratio)
    return total, upper, {
        'argument': rat(x), 'degree': n, 'partial_sum': rat(total),
        'first_omitted': rat(omitted), 'tail_ratio_upper': rat(ratio),
        'upper': rat(upper)}


def atan_series(x, n):
    x = Q(x)
    assert 0 < x < 1 and n % 2 == 0
    lower = sum((x**(4*j + 1) / (4*j + 1)
                 - x**(4*j + 3) / (4*j + 3)
                 for j in range(n // 2)), Q(0))
    upper = lower + x**(2*n + 1) / (2*n + 1)
    return lower, upper, {'argument': rat(x), 'terms': n,
                           'lower': rat(lower), 'upper': rat(upper)}


expected_keys = {
    'scope', 'exp12_series', 'pi_machin', 'scalar_intervals', 'root',
    'denominator_lower_series', 'denominator_upper_series', 'A_g',
    'A_g_rounded', 'checks', 'failures'}
verify('certificate_fields_complete', set(saved), expected_keys)
e_series_lo, e_series_hi, series12 = exp_series(12, 120)
verify('complete_exp12_series', saved['exp12_series'], series12)
a_lo, a_hi, a5 = atan_series(Q(1, 5), 24)
b_lo, b_hi, a239 = atan_series(Q(1, 239), 8)
verify('complete_machin_series', saved['pi_machin'], {
    'identity': 'pi=16 atan(1/5)-4 atan(1/239)',
    'atan5': a5, 'atan239': a239})
# These exact identities also check the tangent and positive-angle arguments.
verify('machin_double_tangent', 2*Q(1, 5)/(1-Q(1, 5)**2), Q(5, 12))
verify('machin_quadruple_tangent', 2*Q(5, 12)/(1-Q(5, 12)**2), Q(120, 119))
verify('machin_subtraction_tangent',
       (Q(120, 119)-Q(1, 239))/(1+Q(120, 119)*Q(1, 239)), Q(1))
verify('machin_angle_lower_positive', 4*Q(5, 26)-Q(1, 239) > 0, True)

e_lo, e_hi = Q('162754.7914190039'), Q('162754.7914190040')
pi_lo, pi_hi = Q('3.141592653589793'), Q('3.141592653589794')
y_lo, y_hi = e_lo/12**4, e_hi/12**4
verify('complete_scalar_intervals', saved['scalar_intervals'], {
    'exp12': [rat(e_lo), rat(e_hi)], 'pi': [rat(pi_lo), rat(pi_hi)],
    'y0': [rat(y_lo), rat(y_hi)]})

rad_lo, rad_hi = 6*y_lo/pi_hi, 6*y_hi/pi_lo
root_lo, root_hi = decode(saved['root']['lower']), decode(saved['root']['upper'])
verify('root_lower_actual_square', root_lo**2 <= rad_lo, True)
verify('root_upper_actual_square', root_hi**2 > rad_hi, True)
verify('root_endpoints_positive', 0 < root_lo < root_hi, True)
verify('complete_root_evidence', saved['root'], {
    'lower_radicand': rat(rad_lo), 'upper_radicand': rat(rad_hi),
    'lower': rat(root_lo), 'upper': rat(root_hi),
    'lower_square_le_lower_radicand': True,
    'upper_square_gt_upper_radicand': True})

c = Q(13, 30)
den_lo, _, series_lo = exp_series(c*y_lo, 80)
_, den_hi, series_hi = exp_series(c*y_hi, 80)
verify('complete_denominator_lower_series', saved['denominator_lower_series'], series_lo)
verify('complete_denominator_upper_series', saved['denominator_upper_series'], series_hi)
lower, upper = Q(10, 13)*root_lo/den_hi, Q(10, 13)*root_hi/den_lo
threshold = Q('0.099276')
rounded_lo, rounded_hi = Q('0.099275864521823'), Q('0.099275864521825')
verify('complete_unrounded_A_g_evidence', saved['A_g'], {
    'lower': rat(lower), 'upper': rat(upper),
    'required_strict_upper': rat(threshold), 'upper_slack': rat(threshold-upper)})
verify('complete_rounded_A_g_evidence', saved['A_g_rounded'], {
    'lower': rat(rounded_lo), 'upper': rat(rounded_hi),
    'required_strict_upper': rat(threshold),
    'certified_slack_lower': rat(Q(1, 10**7))})

comparisons = [
    ('exp12_lower', e_series_lo, '>', e_lo),
    ('exp12_upper', e_series_hi, '<', e_hi),
    ('pi_lower', 16*a_lo-4*b_hi, '>', pi_lo),
    ('pi_upper', 16*a_hi-4*b_lo, '<', pi_hi),
    ('y0_above_monotonicity_threshold', y_lo, '>', Q(15, 13)),
    ('A_g_upper', upper, '<', threshold),
    ('A_g_slack', threshold-upper, '>', Q(1, 10**7)),
    ('A_g_rounded_lower', lower, '>', rounded_lo),
    ('A_g_rounded_upper', upper, '<', rounded_hi)]
recomputed = []
for name, actual, relation, required in comparisons:
    passed = actual < required if relation == '<' else actual > required
    recomputed.append({'name': name, 'actual': rat(actual),
                       'relation': relation, 'required': rat(required), 'passed': passed})
    verify('independent_' + name, passed, True)
verify('complete_nine_saved_comparisons', saved['checks'], recomputed)
verify('saved_failure_list', saved['failures'], [])

destination = HERE / 'audit_extension_constants_1632.json'
certificate = {
    'source': str(SOURCE.relative_to(Path.cwd())),
    'method': 'Independent direct powers/factorials and paired arctangent terms; '
              'every mathematical source field compared exactly, including full rational sums.',
    'checks': checks,
    'failures': [check['name'] for check in checks if not check['passed']],
    'bounds': {'actual_strict_lower': str(rounded_lo), 'actual_strict_upper': str(rounded_hi),
               'required_strict_upper': str(threshold), 'strict_slack_lower': str(Q(1, 10**7))},
    'unrounded_A_g': {'lower': rat(lower), 'upper': rat(upper),
                      'slack': rat(threshold-upper)},
    'analytic_scope': 'Finite endpoint arithmetic only; canonical C048d contains the uniform proof.'}
destination.write_text(json.dumps(certificate, indent=2) + '\n')
print(f'Independent exact replay: {len(checks)} checks; failures: {certificate["failures"]}')
print(f'Actual A_g in ({float(rounded_lo):.15f}, {float(rounded_hi):.15f}); '
      f'required < {float(threshold):.6f}; strict slack > 0.0000001')
print(f'Complete audit certificate: {destination.relative_to(Path.cwd())}')
if certificate['failures']:
    raise SystemExit(1)
