#!/usr/bin/env python3
"""First and only authorized test if the fixed allowance exceeds the margin.

Exact rational evaluation; no polynomial, Bernstein or outer-tail production.
The analytic kernel enclosure remains an inherited, qualified L938 input.
"""
import hashlib
import json
import re
import sys
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction as Q
from math import factorial, prod
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE / 'l938-negative-tail-allowance-87.json'
report = dict(status='IN_PROGRESS', checks=[], failures=[], inputs_sha256={},
              scope='Unchanged L938; tilt1/10; interval[4,8]; full uniform allowance only',
              python=sys.version)


def save():
    OUT.write_text(json.dumps(report, indent=2) + '\n')


def check(name, condition):
    report['checks'].append(dict(name=name, passed=bool(condition)))
    if not condition:
        report['failures'].append(name)
        report['status'] = 'FAILED'
        save()
        raise AssertionError(name)


def read(name):
    raw = (BASE / name).read_bytes()
    report['inputs_sha256'][name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def enclosure(lo, hi):
    with localcontext() as ctx:
        ctx.prec = 16
        ctx.rounding = ROUND_FLOOR
        left = str(Decimal(lo.numerator) / Decimal(lo.denominator))
        ctx.rounding = ROUND_CEILING
        right = str(Decimal(hi.numerator) / Decimal(hi.denominator))
    check('outward display ' + str(len(report['checks'])), Q(left) <= lo <= hi <= Q(right))
    return dict(lower=left, upper=right)


save()
data = read('actual-h2-energy-cell-48.json')
audit = read('actual-h2-energy-cell-audit-50.json')
check('inherited audited kernel certificate hash',
      audit['inputs_sha256']['actual-h2-energy-cell-48.json']
      == report['inputs_sha256']['actual-h2-energy-cell-48.json'])
check('inherited step50 state and complete flag count', audit['status'] == 'PASSED'
      and len(audit['checks']) == 5101 and audit['failures'] == [])
for i, entry in enumerate(audit['checks']):
    check('inherited step50 flag ' + str(i), entry['passed'] is True)
report['inherited_scope'] = ('Full step50 flags and selected kernel-certificate hash checked; '
    'analytic enclosure and theta-node producer inherited, not rerun. '
    'No convolution-polynomial identity is used in this allowance test. '
    'Decimal/exponential and exact-integer implementation contracts retained.')

ap = data['approximation']
check('fixed degree/nodes/theta/precision',
      (ap['degree'], ap['nodes'], ap['theta_terms'], ap['precision']) == (256, 257, 8, 200))
check('fixed grid', int(ap['chebyshev_denominator']) == 10**120
      and int(ap['power_denominator']) == 10**120 * 4**256)
check('all257 coefficients', len(ap['chebyshev_coefficients']) == 257)
etas = []
for i, row in enumerate(ap['chebyshev_coefficients']):
    lo, hi = Q(row['enclosure']['lower']), Q(row['enclosure']['upper'])
    chosen = Q(int(row['chosen_numerator']), 10**120)
    eta = max(abs(chosen-lo), abs(chosen-hi))
    check('full coefficient allowance ' + str(i), row['k'] == i and lo <= hi
          and eta == Q(row['absolute_error']))
    etas.append(eta)
analytic_error = 8*10**9*Q(2, 3)**256
epsilon = analytic_error + sum(etas, Q(0))
check('unchanged full epsilon', sum(etas, Q(0)) == Q(ap['coefficient_error_sum'])
      and epsilon == Q(ap['epsilon']) and 0 < epsilon < Q(1, 10**34))

canonical = (BASE.parent.parent / 'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md').read_text()
table = [(int(c), tuple(map(int, s.split(',')))) for c, s in
         re.findall(r'^\|\s*(-?\d+)\s*\|\s*\(([0-9,]+)\)\s*\|$', canonical, re.M)]
rows = data['algebra']['terms']
check('all34 canonical rows', len(table) == len(rows) == 34)
weights = []
for i, ((c, alpha), row) in enumerate(zip(table, rows)):
    check('canonical row ' + str(i), c == row['coefficient']
          and list(alpha) == row['exponents_A0_to_A6'] and len(alpha) == 7
          and all(type(a) is int and a >= 0 for a in alpha)
          and sum(alpha) == 12 and sum(k*a for k, a in enumerate(alpha)) == 12)
    weight = Q(abs(c), prod(factorial(k)**a for k, a in enumerate(alpha)))
    beta = Q(abs(c), 2**12 * factorial(17))
    for k, a in enumerate(alpha):
        check('positive beta parameter ' + str(i) + ',' + str(k), Q(2*k+1, 2) > 0)
        beta *= Q(1, 4**k * factorial(k))**a
    check('complete beta weight ' + str(i), beta == weight/(2**36 * factorial(17)))
    weights.append(weight)
W = sum(weights, Q(0))
Z = W/(2**36 * factorial(17))
check('exact W and Z', W == Q(293, 540)
      and Z == Q(293, 13199033127778602178314240000))


def atan_enclosure(q):
    terms = 128
    s = sum((Q((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(terms)), Q(0))
    return s, s + Q(1, (2*terms+1)*q**(2*terms+1))


a, b = atan_enclosure(5), atan_enclosure(239)
pi_lo, pi_hi = Q(ap['pi']['lower']), Q(ap['pi']['upper'])
check('positive inherited pi and full rational Machin check',
      3 < pi_lo <= 16*a[0]-4*b[1] <= 16*a[1]-4*b[0] <= pi_hi < 4)

# Positive exponential series: ratios in the tail are at most x/34.
# This encloses exp(4/5), without a new transcendental library call.
x = Q(4, 5)
exp_lo = sum((x**j/factorial(j) for j in range(33)), Q(0))
exp_first_omitted = x**33/factorial(33)
exp_tail = exp_first_omitted/(1-x/34)
exp_hi = exp_lo + exp_tail
check('positive geometric tail ratio', 0 < x/34 < 1)
check('outward exponential scale', Q(2) < exp_lo < exp_hi < Q(9, 4))

threshold = Q('8.935649629627030e-35')
beta_mass = Z * Q(8**18-4**18, 18)
kernel_factor = 12 * epsilon * 8**11
allow_lo = exp_lo * kernel_factor * pi_lo**6 * beta_mass
allow_hi = exp_hi * kernel_factor * pi_hi**6 * beta_mass
# Independent integrated normalization, including 18!, not 17!.
direct_lo = exp_lo * kernel_factor * pi_lo**6 * W * Q(8**18-4**18, 2**36 * factorial(18))
direct_hi = exp_hi * kernel_factor * pi_hi**6 * W * Q(8**18-4**18, 2**36 * factorial(18))
check('independent integrated normalizations', (allow_lo, allow_hi) == (direct_lo, direct_hi))
check('exact fixed threshold', threshold == Q(893564962962703, 10**49))
check('strict allowance obstruction', threshold < allow_lo <= allow_hi)

report['exact'] = {key: str(value) for key, value in dict(
    analytic_error=analytic_error, coefficient_error_sum=sum(etas, Q(0)), epsilon=epsilon,
    W=W, Z=Z, beta_mass_over_pi6=beta_mass, kernel_factor=kernel_factor,
    pi_lower=pi_lo, pi_upper=pi_hi, exp_lower=exp_lo, exp_upper=exp_hi,
    exp_first_omitted=exp_first_omitted, exp_geometric_tail=exp_tail,
    allowance_lower=allow_lo, allowance_upper=allow_hi, threshold=threshold,
    allowance_threshold_ratio_lower=allow_lo/threshold,
    allowance_threshold_ratio_upper=allow_hi/threshold).items()}
report['summary'] = dict(
    allowance=enclosure(allow_lo, allow_hi), required_strict_upper_bound=str(threshold),
    allowance_threshold_ratio=enclosure(allow_lo/threshold, allow_hi/threshold),
    exponential=enclosure(exp_lo, exp_hi), epsilon=enclosure(epsilon, epsilon))
report['status'] = 'FIXED_UNIFORM_ALLOWANCE_STOP'
report['decision'] = ('Stop the prescribed certificate before signed-polynomial and outer-tail work; '
    'its full additive allowance already exceeds the margin. No B_4 lower bound or sign conclusion.')
report['producer_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
save()
print('Result:', report['status'])
print('Full allowance:', report['summary']['allowance'])
print('Required complete upper bound <', str(threshold), '; ratio:', report['summary']['allowance_threshold_ratio'])
print('Checks:', len(report['checks']), '; failures:', report['failures'], '; certificate:', OUT)
