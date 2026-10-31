#!/usr/bin/env python3
"""Audit every stored L527 interval and the complete certificate aggregation.

The generator is separately replayed. This verifier uses Fraction arithmetic,
not its interval class, to check all stored products and outward aggregation.
Elementary-function validity and analytic quadrature errors are proved in L527;
this program does not claim to verify the operator asymptotic.
"""

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'coefficient-certificate.json'
OUT = HERE / 'coefficient-audit.json'
data = json.loads(SOURCE.read_text())
failures = []
checks = 0
records = 0


def check(condition, label):
    global checks
    checks += 1
    if not condition:
        failures.append(label)


def interval(record):
    return (Q(int(record['lower_numerator']), int(record['denominator'])),
            Q(int(record['upper_numerator']), int(record['denominator'])))


def inspect(value, path=''):
    global records
    if isinstance(value, dict):
        if 'lower_numerator' in value:
            records += 1
            lo, hi = interval(value)
            check(lo <= hi, path + ': ordered endpoints')
            check(int(value['denominator']) == 10**40, path + ': scale')
            check([Q(s) for s in value['decimal_enclosure']] == [lo, hi],
                  path + ': exact decimal display')
        else:
            for key, child in value.items():
                inspect(child, path + '/' + key)
    elif isinstance(value, list):
        for j, child in enumerate(value):
            inspect(child, path + '/' + str(j))


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    values = [a*b for a in x for b in y]
    return min(values), max(values)


def square(x):
    return (Q(0) if x[0] <= 0 <= x[1] else min(a*a for a in x),
            max(a*a for a in x))


def divide(x, y):
    assert y[0] > 0
    return mul(x, (1/y[1], 1/y[0]))


def widen(x, radius):
    return x[0] - radius, x[1] + radius


def encloses(record, required, label):
    lo, hi = interval(record)
    check(lo <= required[0] and required[1] <= hi, label)


inspect(data)
grid = data['grid']
nx, nt, T = grid['nx_on_minus_one_one'], grid['nt_on_zero_T'], grid['T']
check((nx, nt, T) == (512, 2048, 32), 'specified grid')
check(len(data['positive_half_bump_nodes']) == nx//2, 'all bump nodes')
check(len(data['outer_nodes']) == nt, 'all outer nodes')

# Independent exact arithmetic checks of the analytic constants in (19)--(22).
check(4*4**4*Q(3, 8)**4 + 8*3**3*Q(3, 8)**3
      + 2*2**2*Q(3, 8)**2 < 33, 'b second derivative bound')
check(2*Q(9, 8)**2 + 2*Q(3, 8)*33 == Q(873, 32),
      'normalization second derivative bound')
check(2*(Q(3, 8)**2 + Q(3, 4)*Q(1, 4))
      + 4*Q(3, 4)*Q(3, 8)*Q(26, 5)
      + Q(3, 4)**2*Q(847, 25) < 26, 'outer second derivative bound')
check(33 + Q(9, 4)*T + Q(3, 8)*T*T == 489,
      'inner second derivative bound')
errors = data['errors']
for key, value in [('normalization_midpoint', Q(873, 96*nx*nx)),
                   ('inner_midpoint', Q(489, 3*nx*nx)),
                   ('outer_midpoint', Q(26*T**3, 24*nt*nt))]:
    encloses(errors[key], (value, value), key)

# All 256 recorded bump enclosures contribute to the normalization.
norm_sum = (Q(0), Q(0))
for j, record in enumerate(data['positive_half_bump_nodes']):
    value = interval(record)
    check(0 <= value[0] <= value[1] <= Q(3, 8), f'bump {j}: range')
    norm_sum = add(norm_sum, square(value))
normalization = widen(mul((Q(4, nx),)*2, norm_sum),
                      interval(errors['normalization_midpoint'])[1])
encloses(data['bump_L2_squared'], normalization, 'complete normalization')
norm = interval(data['bump_L2_squared'])
check(norm[0] > 0, 'strictly positive normalization')

# All 2048 stored Fourier/phase products, not a sample, enter the integral.
total = (Q(0), Q(0))
for j, node in enumerate(data['outer_nodes']):
    check(node['j'] == j, f'node {j}: index')
    expected_t = Q((2*j+1)*T, 2*nt)
    encloses(node['t'], (expected_t, expected_t), f'node {j}: grid')
    phase = interval(node['phase_cosine'])
    check(-1 <= phase[0] <= phase[1] <= 1, f'node {j}: phase range')
    product = mul(square(interval(node['unnormalized_fourier'])), phase)
    encloses(node['integrand'], product, f'node {j}: full signed product')
    total = add(total, interval(node['integrand']))
truncated = widen(mul((Q(T, nt),)*2, total),
                  interval(errors['outer_midpoint'])[1])
encloses(data['unnormalized_truncated_integral'], truncated,
         'complete outer aggregation')
tail = divide((Q(81, 32*T*T),)*2, norm)
encloses(errors['normalized_tail'], tail, 'Plancherel tail with normalization')
pi = interval(data['elementary_enclosures']['pi'])
normalized = divide(interval(data['unnormalized_truncated_integral']),
                    mul(pi, norm))
encloses(data['coefficient_interval'],
         widen(normalized, interval(errors['normalized_tail'])[1]),
         'coefficient with both signed tails')
coefficient = interval(data['coefficient_interval'])
encloses(data['required_threshold'], mul(pi, (Q(1, 4),)*2), 'pi/4 threshold')
ratio = divide(mul((Q(-4),)*2, coefficient), pi)
encloses(data['gamma_limit_interval'], add((Q(-1),)*2, ratio), 'gamma limit')
gamma = interval(data['gamma_limit_interval'])
threshold = interval(data['required_threshold'])
check(Q(1511, 10000) < coefficient[0] <= coefficient[1] < Q(2343, 10000),
      'stated c_h interval')
check(Q(-1299, 1000) < gamma[0] <= gamma[1] < Q(-1192, 1000),
      'stated gamma interval')
check(coefficient[1] < threshold[0] and gamma[0] > -2, 'strict -2 obstruction')
check(data['failures'] == [] and all(data['comparison'].values()),
      'saved decisions agree')

report = {
    'passed': not failures,
    'scope': 'Complete stored interval/aggregation audit after generator replay; '
             'elementary algorithms and analytic errors inspected in L527 audit.',
    'certificate_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'generator_sha256': hashlib.sha256(
        (HERE / 'coefficient_certificate.py').read_bytes()).hexdigest(),
    'interval_records_checked': records,
    'bump_nodes_checked': nx//2,
    'outer_nodes_checked': nt,
    'exact_rational_checks': checks,
    'coefficient_interval': data['coefficient_interval'],
    'required_threshold': data['required_threshold'],
    'gamma_limit_interval': data['gamma_limit_interval'],
    'failures': failures,
}
OUT.write_text(json.dumps(report, indent=2) + '\n')
print('PASS' if not failures else 'FAIL')
print('Full evidence:', records, 'interval records;', nx//2, 'bump nodes;',
      nt, 'outer nodes;', checks, 'exact rational checks')
print('Actual c_h bounds:', data['coefficient_interval']['decimal_enclosure'])
print('Required c_h for absorption: >= pi/4;',
      data['required_threshold']['decimal_enclosure'])
print('Actual gamma bounds:', data['gamma_limit_interval']['decimal_enclosure'],
      '; required <= -2')
print('Failures:', failures)
print('Certificate:', OUT)
if failures:
    raise SystemExit(1)
