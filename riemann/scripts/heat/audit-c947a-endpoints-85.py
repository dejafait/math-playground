#!/usr/bin/env python3
"""Independent L947 endpoint audit; C947a's calculus audit is canonical prose.

Uses ordinary-power-basis convolution and LCM integration, not the
producer's factorial-basis product or its two integration routines.
Inherited L938/C944a/L946 audits are read completely, not rerun.
"""
import hashlib
import json
import re
import sys
from fractions import Fraction as Q
from math import factorial, lcm, prod
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE / 'c947a-endpoint-audit-85.json'
PRODUCT = BASE / 'c947a-ordinary-product-85.json'
report = {'status': 'IN_PROGRESS', 'checks': [], 'failures': [],
          'inputs_sha256': {}, 'python': sys.version,
          'scope': 'L947 endpoints 1/4,4; tilt1/10; unchanged contracts; no budget refinement'}


def save():
    OUT.write_text(json.dumps(report, indent=2) + '\n')


def check(name, condition):
    passed = bool(condition)
    report['checks'].append({'name': name, 'passed': passed})
    if not passed:
        report['failures'].append(name)
        report['status'] = 'FAILED'
        save()
        raise AssertionError(name)


def digest(name):
    result = hashlib.sha256((BASE / name).read_bytes()).hexdigest()
    report['inputs_sha256'][name] = result
    return result


def read(name):
    digest(name)
    return json.loads((BASE / name).read_text())


def audit_flags(label, source, count=None):
    check(label + ' no failures', source['failures'] == [])
    if count is not None:
        check(label + ' complete count', len(source['checks']) == count)
    for i, entry in enumerate(source['checks']):
        check(label + ' flag ' + str(i), entry['passed'] is True)
    for name, expected in source['inputs_sha256'].items():
        check(label + ' hash ' + name, digest(name) == expected)


def rational_equal(name, value, saved):
    check(name, value == Q(saved))


def contains(name, interval, lower, upper=None):
    if upper is None:
        upper = lower
    check(name, Q(interval['lower']) <= lower <= upper <= Q(interval['upper']))


save()
data = read('actual-h2-energy-cell-48.json')
poly = read('actual-h2-energy-cell-polynomial-48.json')
old = read('l938-tilted-endpoints-81.json')
a50 = read('actual-h2-energy-cell-audit-50.json')
a75 = read('l944-c944a-audit-75.json')
a78 = read('l946-cover-audit-78.json')
for label, source, count in [('step50', a50, 5101), ('step75', a75, 15620),
                             ('step78', a78, 56097)]:
    check(label + ' passed state', source['status'] == 'PASSED')
    audit_flags(label, source, count)
audit_flags('step81', old)
check('step81 claimed endpoint contrast', old['status'] == 'SCOPED_ENDPOINT_CONTRAST_PASS')
check('step81 unchanged producer', digest('l938-tilted-endpoints-81.py') == old['producer_sha256'])
identity = a50['integer_identity']
check('inherited exact identity scope', identity['degree'] == 3072
      and identity['residual'] == '0' and identity['difference_bound_lt_half_base'] is True)

ap = data['approximation']
check('fixed degree/nodes/theta/precision',
      (ap['degree'], ap['nodes'], ap['theta_terms'], ap['precision']) == (256, 257, 8, 200))
check('fixed grid and power denominator', int(ap['chebyshev_denominator']) == 10**120
      and int(ap['power_denominator']) == 10**120 * 4**256)
check('all257 records', len(ap['chebyshev_coefficients']) == 257)
eta = []
for i, row in enumerate(ap['chebyshev_coefficients']):
    lo, hi = Q(row['enclosure']['lower']), Q(row['enclosure']['upper'])
    chosen = Q(int(row['chosen_numerator']), 10**120)
    radius = max(abs(lo-chosen), abs(hi-chosen))
    check('coefficient allowance ' + str(i), row['k'] == i and lo <= hi
          and radius == Q(row['absolute_error']))
    eta.append(radius)
epsilon = 8*10**9*Q(2, 3)**256 + sum(eta, Q(0))
check('full epsilon', sum(eta, Q(0)) == Q(ap['coefficient_error_sum'])
      and epsilon == Q(ap['epsilon']) and 0 < epsilon < Q(1, 10**34))

canonical = (BASE.parent.parent / 'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md').read_text()
table = [(int(c), tuple(map(int, s.split(','))))
         for c, s in re.findall(r'^\|\s*(-?\d+)\s*\|\s*\(([0-9,]+)\)\s*\|$', canonical, re.M)]
rows = data['algebra']['terms']
check('all34 rows', len(table) == len(rows) == 34)
beta_weights = []
weights = []
for i, ((c, alpha), row) in enumerate(zip(table, rows)):
    labels = [k for k, a in enumerate(alpha) for _ in range(a)]
    check('canonical labelled row ' + str(i), c == row['coefficient']
          and list(alpha) == row['exponents_A0_to_A6'] and len(alpha) == 7
          and all(type(a) is int and a >= 0 for a in alpha)
          and len(labels) == 12 and sum(labels) == 12)
    # Gamma(k+1/2)/sqrt(pi) = (2k)!/(4^k k!), cancelling each (2k)!.
    b = Q(abs(c), 2**12 * factorial(17))
    for k in labels:
        check('positive beta parameter ' + str(i) + ',' + str(len(beta_weights)) + ',' + str(k),
              Q(2*k+1, 2) > 0)
        b *= Q(factorial(2*k), 4**k * factorial(k)) / factorial(2*k)
    w = Q(abs(c), prod(factorial(k) for k in labels))
    check('row beta normalization ' + str(i), b == w / (2**36 * factorial(17)))
    beta_weights.append(b)
    weights.append(w)
W, Z = sum(weights, Q(0)), sum(beta_weights, Q(0))
check('absolute weight and Z', W == Q(293, 540)
      and Z == Q(293, 13199033127778602178314240000))

rr = [int(v) for v in poly['numerators']]
D = int(poly['denominator'])
check('all3073 signed inputs', len(rr) == 3073)
check('retained normalization denominator',
      D == (2*factorial(12)*int(ap['power_denominator'])*4**262)**12)
maximum = max(map(abs, rr))
check('inherited complete coefficient bound', maximum == int(identity['saved_max_abs_coefficient'])
      and maximum + int(identity['actual_polynomial_coefficient_bound'])
      < 2**(identity['base_power_of_two']-1))

x = Q(2, 5)
exp_sum = sum((x**j / factorial(j) for j in range(33)), Q(0))
exp_tail = x**33 / factorial(33) / (1-x/34)
check('exact exp upper below 3/2', exp_sum + exp_tail < Q(3, 2))
constants = {'epsilon': epsilon, 'W': W, 'Z': Z, 'factor_bound': Q(8),
             'exp_upper': Q(3, 2), 'exp_series_sum': exp_sum, 'exp_tail_bound': exp_tail}
for name, value in constants.items():
    rational_equal('constant ' + name, value, old['constants'][name])
report['constants'] = {k: str(v) for k, v in constants.items()}
report['beta_weights_without_pi6'] = list(map(str, beta_weights))
report['inherited_scope'] = ('All saved audit flags and hashes read; step50 polynomial identity, '
    'theta nodes, step75 differentiation and step78 compact cover reused. No library verification.')
save()
print('Inherited records and complete constants checked; ordinary integer convolution begins.', flush=True)

# Standard monomial coefficients: v_p/pi^6 = t^17 sum B_l t^l/(D H).
H = factorial(3089)
B = []
for ell, value in enumerate(rr):
    multiplier, remainder = divmod(H, factorial(17+ell))
    check('ordinary basis exact division ' + str(ell), remainder == 0)
    B.append(value * multiplier)
# T32 = sum T_j t^j/(10^32*32!). This uses no binomial coefficient formula.
f32 = factorial(32)
T = [10**(32-j) * (f32 // factorial(j)) for j in range(33)]
cc = [0] * 3105
for ell, value in enumerate(B):
    for j, multiplier in enumerate(T):
        cc[ell+j] += value * multiplier
check('complete saved product dimensions', old['product']['degree'] == 3104
      and old['product']['factorial_offset'] == 17
      and int(old['product']['denominator']) == D*10**32
      and len(old['product']['numerators']) == 3105)
residuals = []
for m, (value, saved) in enumerate(zip(cc, old['product']['numerators'])):
    residual = value*factorial(17+m) - int(saved)*H*f32
    check('full signed product coefficient ' + str(m), residual == 0)
    residuals.append(str(residual))
ordinary_denominator = D*H*10**32*f32
PRODUCT.write_text(json.dumps({'degree': 3104, 'power_offset': 17,
    'denominator': str(ordinary_denominator), 'numerators': list(map(str, cc)),
    'factorial_basis_cross_residuals': residuals}, indent=2) + '\n')
report['ordinary_product'] = {'path': PRODUCT.name, 'sha256': digest(PRODUCT.name),
                              'all3105_cross_residuals_zero': all(v == '0' for v in residuals)}
save()
print('All3105 signed coefficients agree; independent LCM integration begins.', flush=True)

common = lcm(*range(18, 3123))
integrated = []
for m, value in enumerate(cc):
    multiplier, remainder = divmod(common, 18+m)
    check('LCM integration exact division ' + str(m), remainder == 0)
    integrated.append(value * multiplier)
report['integration_lcm'] = str(common)
pi_lo, pi_hi = Q(ap['pi']['lower']), Q(ap['pi']['upper'])
check('inherited pi ordered positive', 3 < pi_lo <= pi_hi < 4)
check('saved pi matches', Q(old['pi_enclosure']['lower']) == pi_lo
      and Q(old['pi_enclosure']['upper']) == pi_hi)
report['endpoints'] = {}
report['summary'] = {}
for E, expected_sign in [(Q(1, 4), 'NEGATIVE'), (Q(4), 'POSITIVE')]:
    # Two parity sums of standard-basis antiderivative terms, with LCM divisors.
    n, q = E.numerator, E.denominator
    parity = [0, 0]
    for m, value in enumerate(integrated):
        parity[m % 2] += value * n**(18+m) * q**(3104-m)
    center = Q(sum(parity), ordinary_denominator*common*q**3122)
    mass = Z*E**18/18
    rK = 18*epsilon*8**11*mass
    supT = Q(3, 2)*(E/10)**33/factorial(33)
    abs_mass = 8**12*mass
    rT = supT*abs_mass
    radius = rK+rT
    lo, hi = center-radius, center+radius
    # Positive scaling, with explicit negative and positive cases.
    actual_lo = lo*(pi_lo if lo >= 0 else pi_hi)**6
    actual_hi = hi*(pi_hi if hi >= 0 else pi_lo)**6
    key = str(E)
    exact = {'center_over_pi6': center, 'kernel_error_over_pi6': rK,
             'taylor_sup_error': supT, 'absolute_vp_mass_over_pi6': abs_mass,
             'taylor_error_over_pi6': rT, 'radius_over_pi6': radius,
             'lower_over_pi6': lo, 'upper_over_pi6': hi,
             'actual_lower': actual_lo, 'actual_upper': actual_hi,
             'signed_center_over_radius': center/radius}
    check('all endpoint fields ' + key, set(exact) == set(old['endpoints'][key]))
    for name, value in exact.items():
        rational_equal('endpoint ' + key + ' ' + name, value, old['endpoints'][key][name])
    check('both errors positive ' + key, rK > 0 and rT > 0)
    check('stipulated strict sign ' + key,
          hi < 0 if expected_sign == 'NEGATIVE' else lo > 0)
    check('actual margin exceeds required1 ' + key, abs(center/radius) > 1)
    saved_summary = old['summary'][key]
    check('saved sign and threshold ' + key, saved_summary['sign'] == expected_sign
          and saved_summary['required_absolute_ratio_for_strict_sign'] == '>1')
    contains('outward actual U ' + key, saved_summary['U_interval'], actual_lo, actual_hi)
    for name in ['center_over_pi6', 'kernel_error_over_pi6', 'taylor_error_over_pi6',
                 'signed_center_over_radius']:
        contains('outward ' + key + ' ' + name, saved_summary[name], exact[name])
    report['endpoints'][key] = {k: str(v) for k, v in exact.items()}
    report['endpoints'][key]['ordinary_even_integral_numerator'] = str(parity[0])
    report['endpoints'][key]['ordinary_odd_integral_numerator'] = str(parity[1])
    report['endpoints'][key]['ordinary_integral_denominator'] = str(ordinary_denominator*common*q**3122)
    report['summary'][key] = saved_summary
    print('E=' + key + ': ' + expected_sign + '; ratio=' + str(saved_summary['signed_center_over_radius'])
          + '; required |ratio|>1; U=' + str(saved_summary['U_interval']), flush=True)
    save()

report['status'] = 'PASSED'
report['verifier_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
report['check_count'] = len(report['checks'])
report['decision'] = ('L947 endpoint certificate independently passes under inherited contracts. '
                      'C947a compact calculus audited separately in canonical prose; no global conclusion.')
save()
print('PASSED; checks=' + str(len(report['checks'])) + '; failures=' + str(report['failures'])
      + '; report=' + str(OUT) + '; full product=' + str(PRODUCT), flush=True)
