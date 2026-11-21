#!/usr/bin/env python3
"""Full conditional C948a audit; never imports/runs or overwrites a producer.

Factorial gamma normalization replaces the producer's odd products.
Euclidean quotient/remainder enclosures replay every Bernstein contraction.
Theta inclusion and the signed derivative prefixes remain explicit inputs.
"""
import hashlib
import json
import re
import sys
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from math import factorial, comb, prod
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE / 'c948a-complete-budget-audit-92.json'
D, J, N, G = 2816, 1411, 2822, 10**120
report = dict(status='IN_PROGRESS', checks=[], failures=[], inputs_sha256={},
              replay_rows=[], python=sys.version,
              scope='Conditional full enclosure and conceptual-specialization audit; '
                    'theta inclusion and signed derivative multiplication inherited.')


def save():
    OUT.write_text(json.dumps(report, indent=2) + '\n')


def check(name, passed):
    report['checks'].append(dict(name=name, passed=bool(passed)))
    if not passed:
        report['failures'].append(name)
        report['status'] = 'FAILED'
        save()
        raise AssertionError(name)


def read(name):
    raw = (BASE / name).read_bytes()
    report['inputs_sha256'][name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def shown(x):
    with localcontext() as c:
        c.prec = 16
        c.rounding = ROUND_FLOOR
        lo = str(Decimal(x.numerator) / Decimal(x.denominator))
        c.rounding = ROUND_CEILING
        hi = str(Decimal(x.numerator) / Decimal(x.denominator))
    check('checked rational display ' + str(len(report['checks'])), F(lo) <= x <= F(hi))
    return dict(lower=lo, upper=hi)


def enclose_integer_ratio(num, den):
    assert den > 0
    quotient, remainder = divmod(num, den)
    assert num == quotient*den + remainder and 0 <= remainder < den
    return quotient, quotient + int(remainder != 0)


save()
claim = read('l938-signed-response-complete-90.json')
saved = read('l938-response-bernstein-enclosures-90.json')
prefix = read('l938-signed-response-coefficients-89.json')
response = read('l938-signed-response-89.json')
kernel = read('actual-h2-energy-cell-48.json')
old = read('l938-negative-tail-allowance-87.json')
for name, count in [('complete90', 29626), ('response89', 10270)]:
    data = claim if name == 'complete90' else response
    check(name + ' saved flags only', len(data['checks']) == count
          and not data['failures'] and all(v['passed'] is True for v in data['checks']))
for name in ['l938-signed-response-coefficients-89.json', 'actual-h2-energy-cell-48.json',
             'l938-negative-tail-allowance-87.json']:
    check('input identity only ' + name,
          report['inputs_sha256'][name] == claim['inputs_sha256'][name])
check('saved enclosure identity only', claim['bernstein_sha256'] ==
      report['inputs_sha256']['l938-response-bernstein-enclosures-90.json'])
check('response prefix identity only', response['coefficient_sha256'] ==
      report['inputs_sha256']['l938-signed-response-coefficients-89.json'])
ap = kernel['approximation']
check('fixed parameters', (ap['degree'], ap['nodes'], ap['theta_terms'], ap['precision'])
      == (256, 257, 8, 200) and int(ap['chebyshev_denominator']) == G
      and int(ap['power_denominator']) == G*4**256)
check('full input dimensions', prefix['cut'] == saved['cut'] == J
      and prefix['full_degree'] == saved['degree'] == D
      and int(saved['grid']) == G and len(prefix['gradients']) == len(saved['rows']) == 7
      and all(len(v) == J+1 for v in prefix['gradients'])
      and len(ap['power_numerators']) == len(ap['chebyshev_coefficients']) == 257)
C = int(prefix['C'])
check('common positive normalization', C == 2*factorial(12)*G*4**518 and C > 0)

# Reconstruct full epsilon, without claiming new theta-node inclusion.
errors = []
for i, item in enumerate(ap['chebyshev_coefficients']):
    lo, hi = F(item['enclosure']['lower']), F(item['enclosure']['upper'])
    center = F(int(item['chosen_numerator']), G)
    radius = max(abs(center-lo), abs(center-hi))
    check('kernel coefficient allowance ' + str(i), item['k'] == i and lo <= hi
          and radius == F(item['absolute_error']))
    errors.append(radius)
epsilon = 8*10**9*F(2, 3)**256 + sum(errors, F(0))
check('full unchanged epsilon', epsilon == F(ap['epsilon']) == F(old['exact']['epsilon'])
      and sum(errors, F(0)) == F(ap['coefficient_error_sum']) and 0 < epsilon < F('1e-34'))

# Canonical rows, all multiplicities, the two positive beta normalizations.
canonical = (BASE.parent.parent / 'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md').read_text()
rows = [(int(c), tuple(map(int, a.split(',')))) for c, a in
        re.findall(r'^\|\s*(-?\d+)\s*\|\s*\(([0-9,]+)\)\s*\|$', canonical, re.M)]
check('all34 rows', len(rows) == len(kernel['algebra']['terms']) == 34)
for i, ((c, a), term) in enumerate(zip(rows, kernel['algebra']['terms'])):
    check('row and labelled parameters ' + str(i), c == term['coefficient']
          and list(a) == term['exponents_A0_to_A6'] and len(a) == 7
          and min(a) >= 0 and sum(a) == sum(k*v for k, v in enumerate(a)) == 12)
    for k in range(7):
        if a[k]:
            b = [v-int(t == k) for t, v in enumerate(a)]
            check('deleted row ' + str(i) + ',' + str(k), sum(b) == 11
                  and sum(t*v for t, v in enumerate(b)) == 12-k and min(b) >= 0)
W = sum((F(abs(c), prod(factorial(k)**v for k, v in enumerate(a))) for c, a in rows), F(0))
Z = W/(2**36*factorial(17))
check('whole simplex normalization', W == F(293, 540) and Z == F(old['exact']['Z']))
beta = [F(factorial(34-2*k)*factorial(2*k),
          4**17*factorial(17-k)*factorial(k)*factorial(17)) for k in range(7)]
check('all prefix beta masses', beta == list(map(F, claim['prefix']['beta_masses_over_pi'])))
cells = [F((i+1)**18-i**18, 18*4**18) for i in range(16, 32)]
energy = sum(cells, F(0))
check('all sixteen positive cell masses', all(v > 0 for v in cells)
      and energy == F(8**18-4**18, 18) == F(claim['prefix']['energy_mass']))

# Every scalar gamma normalization uses factorials, not odd products.
fac = [factorial(i) for i in range(2*(17+J)+1)]
all_maxima, all_indices = [], []
updates = 0
for k in range(7):
    block = saved['rows'][k]
    check('complete saved row dimensions ' + str(k), block['k'] == k
          and len(block['power_lower']) == len(block['power_upper']) == J+1
          and len(block['bernstein']) == D+1)
    scalars = []
    for l, value in enumerate(prefix['gradients'][k]):
        h = 17-k+l
        num = int(value)*4**h*fac[h]*8**l*G
        den = 2*C**11*fac[2*k]*fac[2*h]
        lo, hi = enclose_integer_ratio(num, den)
        check('factorial scalar enclosure ' + str(k) + ',' + str(l),
              lo == int(block['power_lower'][l]) and hi == int(block['power_upper'][l])
              and lo*den <= num <= hi*den and 0 <= hi-lo <= 1)
        scalars.append((lo, hi))
    row = []
    for j in range(D+1):
        last = min(J, j)
        lower, upper = scalars[last]
        for degree in reversed(range(last)):
            mul, den = j-degree, D-degree
            assert 0 < mul <= den
            qlo, _ = enclose_integer_ratio(lower*mul, den)
            _, qhi = enclose_integer_ratio(upper*mul, den)
            lower = scalars[degree][0] + qlo
            upper = scalars[degree][1] + qhi
            updates += 1
        check('full Bernstein replay ' + str(k) + ',' + str(j),
              [lower, upper] == list(map(int, block['bernstein'][j]))
              and lower <= upper and upper-lower <= 3*(last+1))
        row.append((lower, upper))
    endpoint_max = max(max(abs(a), abs(b)) for a, b in row)
    index = next(j for j, (a, b) in enumerate(row) if max(abs(a), abs(b)) == endpoint_max)
    maximum = F(endpoint_max, G)
    check('recomputed complete maximum ' + str(k), endpoint_max == int(block['maximum_numerator'])
          and index == block['maximum_index'] == claim['prefix']['maximum_indices'][k]
          and maximum == F(claim['prefix']['maxima'][k]))
    all_maxima.append(maximum)
    all_indices.append(index)
    report['replay_rows'].append(dict(k=k, scalars=[[str(a), str(b)] for a, b in scalars],
        bernstein=[[str(a), str(b)] for a, b in row], maximum=str(maximum), index=index))
    save()
    print('Full audited Bernstein row', k, ':', D+1, 'inclusions; maximum <=', shown(maximum)['upper'], flush=True)

prefix_bound = energy*sum((a*b for a, b in zip(all_maxima, beta)), F(0))
check('full prefix recombination', prefix_bound == F(claim['prefix']['complete_coefficient_norm_upper'])
      and 0 < prefix_bound < F('5.665664337771549e-18'))

# Full unchanged kernel polynomial, positive rational row majorants.
rho = F(1, 32)
qplus = []
power = list(map(int, ap['power_numerators']))
for k in range(7):
    integers = []
    for l, value in enumerate(power):
        a, rem1 = divmod(factorial(2*(k+l)), factorial(k+l))
        b, rem2 = divmod(factorial(12), factorial(2*k))
        check('Q exact normalization ' + str(k) + ',' + str(l), rem1 == rem2 == 0)
        integers.append(abs(value)*a*b*4**(262-k-l))
    # Direct summation is independent of the producer's rational Horner.
    qplus.append(sum((F(v, C)*rho**l for l, v in enumerate(integers)), F(0)))
    check('full Q positive evaluation ' + str(k), qplus[-1] == F(claim['tail']['qplus'][k]))
majorants = []
for k in range(7):
    v = sum((abs(c)*a[k]*prod(qplus[t]**(a[t]-int(t == k)) for t in range(7))
             for c, a in rows if a[k]), F(0))
    check('full derivative majorant ' + str(k), v > 0 and v == F(claim['tail']['derivative_majorants'][k]))
    majorants.append(v)
first = J+1
ratio = F(256, 1431)
check('complete omitted-degree range and ratio', first == claim['tail']['first_degree'] == 1412
      and rho == F(claim['tail']['r']) and first <= D
      and ratio == F(claim['tail']['geometric_ratio']) == 8/rho/(first+19) and 0 < ratio < 1)
tail = F(8**18*256**first, factorial(first+18))/(1-ratio)*sum(
    (v/F(2*4**k*factorial(k)) for k, v in enumerate(majorants)), F(0))
cap = F('1.225e-82')
check('full omitted-degree bound', tail == F(claim['tail']['complete_norm_upper'])
      and cap == F(claim['tail']['rational_cap']) and 0 < tail < cap)

# Independently recombine the unchanged scalar enclosures and full remainder.
pi_lo, pi_hi = F(ap['pi']['lower']), F(ap['pi']['upper'])
check('inherited positive pi endpoints', 3 < pi_lo <= pi_hi < 4
      and pi_lo == F(old['exact']['pi_lower']) and pi_hi == F(old['exact']['pi_upper']))
x = F(4, 5)
exp_lo = sum((x**i/factorial(i) for i in range(33)), F(0))
exp_hi = exp_lo + x**33/factorial(33)/(1-x/34)
check('full exponential remainder', exp_lo == F(old['exact']['exp_lower'])
      and exp_hi == F(old['exact']['exp_upper']) and 0 < x/34 < 1)
second_lo = exp_lo*comb(12, 2)*epsilon**2*8**10*pi_lo**6*Z*energy
second_hi = exp_hi*comb(12, 2)*epsilon**2*8**10*pi_hi**6*Z*energy
check('complete Taylor remainder normalization', second_hi == F(claim['result']['second_order_upper'])
      == F(response['second_order']['upper'])
      and second_lo == F(response['second_order']['lower']) and 0 < second_lo <= second_hi < F('1.496e-67'))
linear = exp_hi*epsilon*pi_hi**6*(prefix_bound+cap)
total = linear + second_hi
margin = F('8.935649629627030e-35')
check('exact total and decisive margin', linear == F(claim['result']['first_order_upper'])
      and total == F(claim['result']['total_upper'])
      and margin == F(claim['result']['required_strict_upper'])
      and F('8.078176384036186e-50') <= total <= F('8.078176384036187e-50')
      and 0 < total < F('8.079e-50') < margin)
for label, value, bounds in [
    ('prefix', prefix_bound, claim['prefix']['enclosure']),
    ('tail', tail, claim['tail']['enclosure']),
    ('total', total, claim['result']['total_upper_enclosure']),
    ('ratio', total/margin, claim['result']['margin_ratio_upper'])]:
    check('saved display ' + label, F(bounds['lower']) <= value <= F(bounds['upper']))
report['exact'] = dict(epsilon=str(epsilon), W=str(W), Z=str(Z),
    beta=list(map(str, beta)), cell_masses=list(map(str, cells)), qplus=list(map(str, qplus)),
    derivative_majorants=list(map(str, majorants)), prefix=str(prefix_bound), tail=str(tail),
    second_order_lower=str(second_lo), second_order_upper=str(second_hi),
    first_order_upper=str(linear), total_upper=str(total), required_strict_upper=str(margin))
report['summary'] = dict(scalar_enclosures=7*(J+1), bernstein_enclosures=7*(D+1),
    horner_updates=updates, all_maxima_indices=all_indices, omitted_degree_first=first,
    omitted_degree_last=D, cells=16, residual_interval=[0, 1], degrees=[D, N],
    prefix=shown(prefix_bound), tail=shown(tail), total=shown(total), ratio=shown(total/margin),
    required_strict_upper=str(margin), inherited_contracts=['theta inclusion',
        'signed derivative-prefix multiplication', 'directed arithmetic and Python exact execution'])
report['status'] = 'PASSED_CONDITIONAL_FULL_AUDIT'
report['audit_script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
save()
print('Result:', report['status'], '; checks:', len(report['checks']), '; failures:', report['failures'])
print('Total <=', report['summary']['total']['upper'], '; required <', margin)
print('All new enclosures and exact evidence:', OUT)
