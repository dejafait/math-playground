#!/usr/bin/env python3
"""Exact rational consistency checks; not an independent theta/FFT replay.

Every final cell endpoint, error allowance and sign is checked. The
transcendental node production and the large polynomial multiplication
remain subject to their analytic/code proof and a later separate audit.
"""
from decimal import Decimal
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import sys

sys.set_int_max_str_digits(0)
base = Path(__file__).parent
source = base / 'actual-h2-energy-cell-48.json'
data = json.loads(source.read_text())
ap = data['approximation']
test = data['mass_test']
checks = []


def check(name, result):
    checks.append({'check': name, 'passed': bool(result)})
    if not result:
        raise AssertionError(name)


def interval(raw):
    return F(Decimal(raw['lower'])), F(Decimal(raw['upper']))


def arctan(q):
    s = sum((F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(128)), F(0))
    t = F(1, 257*q**257)
    return s, s+t


a, b = arctan(5), arctan(239)
pl, ph = interval(ap['pi'])
check('full Machin enclosure', pl <= 16*a[0]-4*b[1] <= 16*a[1]-4*b[0] <= ph)
check('pi elementary range', 3 < pl < ph < 4)
x = F(27, 2)
exp_upper = sum((x**j/factorial(j) for j in range(65)), F(0))
exp_upper += x**65/factorial(65)/(1-x/66)
exp_lower = sum((F(3)**j/factorial(j) for j in range(9)), F(0))
check('exp(27/2) upper', exp_upper < 10**6)
check('exp(3) lower', exp_lower > 20)
tail = F(256*9**4*10**6, 20**81)
check('full theta tail formula', F(ap['full_theta_tail_bound']) == tail)
check('cosine Taylor error formula', F(ap['cosine_remainder']) == F(4**258, factorial(258)))
coefficient_error = F(0)
for c in ap['chebyshev_coefficients']:
    lo, hi = interval(c['enclosure'])
    chosen = F(int(c['chosen_numerator']), int(ap['chebyshev_denominator']))
    error = max(abs(lo-chosen), abs(hi-chosen))
    check(f"Chebyshev coefficient {c['k']} full error", error == F(c['absolute_error']))
    coefficient_error += error
analytic = F(8*10**9*2**256, 3**256)
epsilon = F(ap['epsilon'])
check('coefficient error sum', coefficient_error == F(ap['coefficient_error_sum']))
check('analytic error formula', analytic == F(ap['analytic_interpolation_error']))
check('complete epsilon formula', epsilon == analytic+coefficient_error)
check('epsilon threshold', 0 < epsilon < F(1, 10**34))
for node in ap['node_enclosures']:
    xl, xh = interval(node['energy'])
    ul, uh = interval(node['sqrt_energy'])
    kl, kh = interval(node['kernel'])
    check(f"node {node['j']} rational sqrt containment", 0 < ul*ul <= xl <= xh <= uh*uh < 9)
    check(f"node {node['j']} positive enclosing kernel", 0 < kl <= kh)

weight, gaussian = F(0), F(0)
for t in data['algebra']['terms']:
    exponents = t['exponents_A0_to_A6']
    factor = 1
    for k, alpha in enumerate(exponents):
        factor *= factorial(k)**alpha
    check('homogeneous row '+str(exponents), sum(exponents) == 12 and
          sum(k*alpha for k, alpha in enumerate(exponents)) == 12 and exponents[0]>=6)
    weight += F(abs(t['coefficient']), factor)
    gaussian += F(t['coefficient'], factor)
check('absolute beta weight', weight == F(test['absolute_beta_weight']) == F(293, 540))
check('constant-kernel cancellation', gaussian == 0)
common_error = F(12*8**11, 2**36*factorial(18))*epsilon*weight
check('complete error formula', common_error == F(test['common_error_without_pi6_or_cell_power']))
den = int(test['common_polynomial_integral_denominator'])
signs = []
for c in test['cells']:
    j = c['j']
    rational_mass = F(int(c['polynomial_integral_numerator']), den)
    actual_polynomial_bounds = sorted((rational_mass*pl**6, rational_mass*ph**6))
    lo, hi = interval(c['polynomial_integral_interval'])
    check(f'cell {j} rational polynomial mass containment',
          lo <= actual_polynomial_bounds[0] <= actual_polynomial_bounds[1] <= hi)
    error = F(Decimal(c['full_kernel_error_upper']))
    required = common_error*F((j+1)**18-j**18, 4**18)*ph**6
    check(f'cell {j} full-kernel error allowance', error >= required > 0)
    full_lo, full_hi = interval(c['full_mass_interval'])
    check(f'cell {j} final containment', full_lo <= lo-error <= hi+error <= full_hi)
    sign = 1 if full_lo>0 else -1 if full_hi<0 else 0
    check(f'cell {j} certified sign', sign == c['certified_sign'])
    signs.append(sign)
triples = [[i,j,k] for i in range(32) for j in range(i+1,32) for k in range(j+1,32)
           if signs[i] and signs[j] == -signs[i] and signs[k] == signs[i]]
check('all 32 signs inspected', signs == test['summary']['signs'] == [-1]*2+[1]*13+[0]*17)
check('complete alternating-triple search', triples == test['summary']['alternating_triples'] == [])
for name, raw in data['arithmetic'].items():
    check(name+' precision', raw['precision'] == 200)
    expected = {'down': 'ROUND_FLOOR', 'up': 'ROUND_CEILING', 'near': 'ROUND_HALF_EVEN'}[name]
    check(name+' rounding', raw['rounding'] == expected)
    for signal in ('InvalidOperation','DivisionByZero','Overflow','Underflow','Subnormal'):
        key = "<class 'decimal."+signal+"'>"
        check(name+' trap/flag '+signal, raw['traps'][key] and not raw['flags'][key])

report = {
    'source': source.name, 'checks': checks,
    'summary': {'checks_passed': len(checks), 'failures': [], 'signs': signs,
                'alternating_triples': triples, 'epsilon_upper_required': '1e-34',
                'epsilon_upper_actual': ap['epsilon_interval']['upper'],
                'scope': 'Exact rational final-enclosure and saved-data checks; no independent node or polynomial-production replay.'},
    'elementary_exponential_bounds': {'exp_3_lower': str(exp_lower), 'exp_27_over_2_upper': str(exp_upper)}
}
path = base/'actual-h2-energy-cell-checks-48.json'
path.write_text(json.dumps(report, indent=2)+'\n')
print(f"{len(checks)} exact-rational checks passed; signs 2 negative / 13 positive / 17 uncertain; "
      f"alternating triples 0 (required >=1); epsilon <1e-34; {path}")
