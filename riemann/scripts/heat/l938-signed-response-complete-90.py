#!/usr/bin/env python3
"""Enclose the complete L948 Bernstein allowance, with every degree paid.

Use signed prefixes in a positive Bernstein composition, and an exact
positive-polynomial bound for the omitted degrees. No kernel changes.
"""
import hashlib
import json
import sys
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction as Q
from math import factorial
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE / 'l938-signed-response-complete-90.json'
COEFF = BASE / 'l938-response-bernstein-enclosures-90.json'
D, N, CUT, GRID = 2816, 2822, 1411, 10**120
report = dict(status='IN_PROGRESS', checks=[], failures=[], inputs_sha256={})


def save():
    OUT.write_text(json.dumps(report, indent=2) + '\n')


def check(name, ok):
    report['checks'].append(dict(name=name, passed=bool(ok)))
    if not ok:
        report['failures'].append(name)
        report['status'] = 'FAILED'
        save()
        raise AssertionError(name)


def read(name):
    raw = (BASE / name).read_bytes()
    report['inputs_sha256'][name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def display(lo, hi):
    with localcontext() as ctx:
        ctx.prec = 16
        ctx.rounding = ROUND_FLOOR
        a = str(Decimal(lo.numerator) / Decimal(lo.denominator))
        ctx.rounding = ROUND_CEILING
        b = str(Decimal(hi.numerator) / Decimal(hi.denominator))
    check('outward display ' + str(len(report['checks'])), Q(a) <= lo <= hi <= Q(b))
    return dict(lower=a, upper=b)


save()
source = read('l938-signed-response-89.json')
data = read('l938-signed-response-coefficients-89.json')
old = read('l938-negative-tail-allowance-87.json')
kernel = read('actual-h2-energy-cell-48.json')
check('saved prefix hash', report['inputs_sha256']['l938-signed-response-coefficients-89.json']
      == source['coefficient_sha256'])
check('unchanged kernel hash', report['inputs_sha256']['actual-h2-energy-cell-48.json']
      == source['inputs_sha256']['actual-h2-energy-cell-48.json']
      == old['inputs_sha256']['actual-h2-energy-cell-48.json'])
check('unchanged scalar input hash', report['inputs_sha256']['l938-negative-tail-allowance-87.json']
      == source['inputs_sha256']['l938-negative-tail-allowance-87.json'])
check('inherited producer consistency', len(source['checks']) == 10270
      and not source['failures'] and all(x['passed'] is True for x in source['checks']))
ap = kernel['approximation']
check('unchanged settings', (ap['degree'], ap['nodes'], ap['theta_terms'], ap['precision'])
      == (256, 257, 8, 200) and int(ap['chebyshev_denominator']) == GRID)
grad = [list(map(int, row)) for row in data['gradients']]
check('all exact signed prefixes', data['cut'] == CUT and data['full_degree'] == D
      and len(grad) == 7 and all(len(row) == CUT+1 for row in grad))
C = int(data['C'])
check('unchanged normalization', C == 2*factorial(12)*int(ap['power_denominator'])*4**262)
epsilon = Q(ap['epsilon'])
check('full epsilon', epsilon == Q(old['exact']['epsilon']))
pi_lo, pi_hi = (Q(old['exact']['pi_'+s]) for s in ('lower', 'upper'))
exp_lo, exp_hi = (Q(old['exact']['exp_'+s]) for s in ('lower', 'upper'))
margin = Q('8.935649629627030e-35')
second_hi = Q(source['second_order']['upper'])
check('inherited complete second-order allowance', 0 < second_hi < Q('1.496e-67') < margin)
report['qualification'] = ('Saved derivative multiplication and full theta inclusion inherited; '
    'hashes and previous checks establish consistency, not independent audits. New bounds use '
    'exact Python integer/Fraction operations; numerical displays are checked against rationals.')
save()

# Enclose t_kl=f_kl*8^l on the fixed rational grid. The denominator uses
# 4^h h!/(2h)! = 2^h/O_h, O_h the product of positive odd integers.
odd = [1]
for h in range(1, 18+CUT):
    odd.append(odd[-1]*(2*h-1))
C11 = C**11
blocks, maxima, witnesses = [], [], []
for k, row in enumerate(grad):
    low, high = [], []
    for l, d in enumerate(row):
        h = 17-k+l
        num = d * 2**(h+3*l) * GRID
        den = 2*C11*factorial(2*k)*odd[h]
        lo, hi = num//den, -((-num)//den)
        check('scalar inclusion '+str(k)+','+str(l),
              lo*den <= num <= hi*den and 0 <= hi-lo <= 1)
        low.append(lo)
        high.append(hi)
    # c_j = sum_l t_l binom(j,l)/binom(D,l). Backward Horner has
    # multiplier (j-l)/(D-l) in [0,1]. Floor/ceiling divisions enclose
    # every step, including negative accumulators, by exact inequalities.
    bounds = []
    maximum, witness = -1, None
    for j in range(D+1):
        last = min(j, CUT)
        lo, hi = low[last], high[last]
        for l in range(last-1, -1, -1):
            num, den = j-l, D-l
            lo = low[l] + (lo*num)//den
            hi = high[l] - ((-hi*num)//den)
        check('Bernstein enclosure width '+str(k)+','+str(j),
              0 <= hi-lo <= 3*(last+1))
        bounds.append([str(lo), str(hi)])
        v = max(abs(lo), abs(hi))
        if v > maximum:
            maximum, witness = v, j
    maxima.append(Q(maximum, GRID))
    witnesses.append(witness)
    blocks.append(dict(k=k, power_lower=list(map(str, low)), power_upper=list(map(str, high)),
                       bernstein=bounds, maximum_numerator=str(maximum), maximum_index=witness))
    print('Complete degree2816 Bernstein row', k, '; max |coefficient| <=',
          display(maxima[-1], maxima[-1])['upper'], flush=True)

COEFF.write_text(json.dumps(dict(degree=D, cut=CUT, grid=str(GRID), rows=blocks), indent=2)+'\n')
report['bernstein_artifact'] = COEFF.name
report['bernstein_sha256'] = hashlib.sha256(COEFF.read_bytes()).hexdigest()
beta = [Q(odd[17-k]*odd[k], 2**17*factorial(17)) for k in range(7)]
energy_mass = Q(8**18-4**18, 18)
prefix_bound = energy_mass*sum((m*b for m,b in zip(maxima,beta)), Q(0))
report['prefix'] = dict(maxima=list(map(str,maxima)), maximum_indices=witnesses,
    beta_masses_over_pi=list(map(str,beta)), energy_mass=str(energy_mass),
    complete_coefficient_norm_upper=str(prefix_bound), enclosure=display(prefix_bound,prefix_bound))
save()

# Every missing coefficient of the signed derivative is dominated by
# the derivative of P with absolute row coefficients at Q_k^+(r).
# This pays the ENTIRE remainder l>=1412, including degrees above the
# saved prefix, rather than extrapolating a numerical decay pattern.
r = Q(1,32)
power = list(map(int, ap['power_numerators']))
qplus = []
for k in range(7):
    v = Q(0)
    for l in range(256, -1, -1):
        h = k+l
        q = Q(abs(power[l])*factorial(2*h),
              int(ap['power_denominator'])*2*4**h*factorial(h)*factorial(2*k))
        v = v*r+q
    qplus.append(v)
tail_majorants = []
for k in range(7):
    v = Q(0)
    for term in kernel['algebra']['terms']:
        alpha = term['exponents_A0_to_A6'][:]
        if not alpha[k]:
            continue
        z = Q(abs(term['coefficient'])*alpha[k])
        alpha[k] -= 1
        for q,n in zip(qplus,alpha):
            z *= q**n
        v += z
    tail_majorants.append(v)
L = CUT+1
ratio = 8/r/(L+19)
check('positive factorial tail ratio', 0 < ratio < 1 and L == 1412)
tail_bound = (8**18*(8/r)**L/Q(factorial(L+18))/(1-ratio)
              *sum((v/Q(2*4**k*factorial(k)) for k,v in enumerate(tail_majorants)),Q(0)))
tail_cap = Q('1.225e-82')
check('complete omitted-degree norm cap', 0 < tail_bound < tail_cap)
report['tail'] = dict(first_degree=L, r=str(r), qplus=list(map(str,qplus)),
    derivative_majorants=list(map(str,tail_majorants)), geometric_ratio=str(ratio),
    complete_norm_upper=str(tail_bound), rational_cap=str(tail_cap),
    enclosure=display(tail_bound,tail_bound))
first_hi = exp_hi*epsilon*pi_hi**6*(prefix_bound+tail_cap)
total_hi = first_hi+second_hi
report['result'] = dict(first_order_upper=str(first_hi), second_order_upper=str(second_hi),
    total_upper=str(total_hi), total_upper_enclosure=display(total_hi,total_hi),
    required_strict_upper=str(margin), margin_ratio_upper=display(total_hi/margin,total_hi/margin),
    all_sixteen_cells=True, full_energy_degree=D, full_residual_degree=N,
    complete_degrees_paid=True, omitted_terms='NONE',
    conclusion='Upper bound for the complete prescribed coefficient allowance, not an actual error lower bound.')
check('complete replacement allowance below margin', 0 < total_hi < margin)
report['producer_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
report['status'] = 'COMPLETE_REPLACEMENT_BUDGET_PASSED'
save()
print('Result:', report['status'], '; total <=', report['result']['total_upper_enclosure']['upper'])
print('Required <', margin, '; ratio <=', report['result']['margin_ratio_upper']['upper'])
print('Checks:', len(report['checks']), '; failures:', report['failures'], '; certificate:', OUT)
