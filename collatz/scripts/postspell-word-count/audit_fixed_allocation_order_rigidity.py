#!/usr/bin/env python3
"""Independent exact audit of L063; never imports or runs its generator."""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE / 'fixed-allocation-order-rigidity-certificate.json'
saved = json.loads(SOURCE.read_text())
text55 = (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
text63 = (ROOT / 'lemmas/L063-fixed-allocation-j-guard-order-rigidity.md').read_text()
rows = []
for line in text55.splitlines():
    cells = line.strip('|').split('|')
    if len(cells) == 3 and all(c.isdigit() for c in cells):
        i, j, h = map(int, cells)
        rows.append(dict(index=i, J=j, H=h, a=2 if i < 24 else 166504412))
checks = []


def check(name, actual, required, relation='='):
    ok = actual == required if relation == '=' else actual < required
    checks.append(dict(name=name, actual=actual, required=required,
                       relation=relation, passed=ok))


check('canonical indices', [r['index'] for r in rows], list(range(25)))
check('complete saved rows', saved['rows'], rows)
S = 10**12
ell, upper2, lower3, u = 693147180559, 693147180560, 1098612288668, 1098612288669
lm, lp = F(10584, 10**14), F(10585, 10**14)
K = sum(3*r['J']+r['H'] for r in rows)
N = sum(4*r['J']+r['H']+r['a'] for r in rows)

# A second enclosure uses unrounded terms with their exact geometric tail.
series = {}


def direct_log(t, name):
    x = (t-1)/(t+1)
    terms = [2*x**(2*i+1)/(2*i+1) for i in range(120)]
    low = sum(terms)
    remainder = 2*x**241/(241*(1-x*x))
    series[name] = dict(argument=t, x=x, terms=terms, remainder=remainder,
                        lower=low, upper=low+remainder)
    return low, low+remainder


l2, u2 = direct_log(F(2), 'log2')
l3, u3 = direct_log(F(3), 'log3')
lc, uc = direct_log(F(11, 4), 'log11over4')
# Binary reduction of 18 billion; the exponent and mantissa are certified.
height = 18*10**9
power = height.bit_length()-1
mantissa = F(height, 2**power)
lh, uh = direct_log(mantissa, 'log18b_mantissa')
lh, uh = lh+power*l2, uh+power*u2
log_bounds = dict(log2=[l2, u2], log3=[l3, u3], log11over4=[lc, uc],
                  log18b=[lh, uh], Lambda=[N*l2-K*u3, N*u2-K*l3])
for name, actual, required in [
    ('log2 lower', F(ell, S), l2), ('log2 upper', u2, F(upper2, S)),
    ('log3 lower', F(lower3, S), l3), ('log3 upper', u3, F(u, S)),
    ('Lambda lower', lm, log_bounds['Lambda'][0]),
    ('Lambda upper', log_bounds['Lambda'][1], lp),
    ('literal root log lower', F(2361, 100), lh),
    ('literal guard constant', F(1011600911678, S), lc),
    ('literal alpha lower', F(523248143764, S), 3*l3-4*u2),
    ('literal beta lower', F(405465108108, S), l3-u2),
]:
    check(name, actual, required, '<')
check('saved imported intervals', saved['imported_intervals'], dict(
    source='L055 (2) and (6), independently audited there',
    log2=[str(F(ell, S)), str(F(upper2, S))],
    log3=[str(F(lower3, S)), str(F(u, S))], Lambda=[str(lm), str(lp)]))

baseline_c = F(3**64, 2**74)
baseline_eta = F(23, 11)-F(12*16**8, 11*27**8)-F(16**8*2**40, 27**8*3**40)
bmax = F(23, 11)*(1+F(1, 10**8)*2)
nmin = 2/lp-2
smax = bmax/lm+F(23, 11)
exp_terms = [F(24**i, factorial(i)) for i in range(41)]
expected_support = [
    ('uniform first multiplier baseline', F(10**8), baseline_c),
    ('uniform first eta baseline', F(2), baseline_eta),
    ('all growing multipliers', F(2), F(19683, 8192)),
    ('shifted additive term negative for H>=5', F(81, 44), F(729, 352)),
    ('positive imported Lambda lower', F(0), lm),
    ('ordered imported Lambda endpoints', lm, lp),
    ('imported Lambda upper below one', lp, F(1)),
    ('uniform n0 lower', F(18*10**9), nmin),
    ('uniform s0 upper', smax, F(20*10**9)),
    ('uniform lower junction guard', F(540, 11), F(18*10**9)),
    ('exp24 partial sum exceeds 20 billion', F(20*10**9), sum(exp_terms)),
    ('exp2 partial sum exceeds 11/4', F(11, 4), F(5)),
]
expected_records = []
for name, a, b in expected_support:
    check(name, a, b, '<')
    expected_records.append(dict(name=name, actual=str(a), required=str(b),
                                 relation='<', margin=str(b-a), passed=a < b))
check('all saved supporting operands and margins', saved['checks'], expected_records)
check('all 41 saved exponential terms', saved['exp24_terms'], list(map(str, exp_terms)))
check('saved root bounds', saved['bounds'], dict(B_upper=str(bmax), n0_lower=str(nmin), s0_upper=str(smax)))
check('written eta fraction', baseline_eta, F(7122556955297586891012225981605, 3433683820292512484657849089281))
check('written lower root fraction', nmin, F(39999999995766, 2117))
check('written upper root fraction', smax, F(95833335260143, 4851))
check('written exponential sum', sum(exp_terms), F(202750314819830504045671593478515759301, 7661655986496068058455078125))

pairs, weakest, prefixes, literal_guards = [], [], [], []
for k in range(25):
    # Recompute every prefix as a separate sum, without the generator's recurrence.
    A = sum(3*r['J']+r['H'] for r in rows[:k])
    D = sum(4*r['J']+r['H']+r['a'] for r in rows[:k])
    v = 23610000000000+sum(r['J']*523248143764+r['H']*405465108108-2*upper2 for r in rows[:k])
    jmargin = v+1011600911678-4*rows[k]['J']*upper2
    literal_guards.append(dict(index=k, v=v, J=rows[k]['J'], scaled_margin=jmargin))
    check(f'literal own-index J guard {k}', 0, jmargin, '<')
    if k == 24:
        continue
    rhs = F(26*S+A*u-D*ell, S)
    prefixes.append(dict(position=k, three_exponent=A, two_exponent=D,
                         h_upper=str(rhs-2), guard_rhs_upper=str(rhs)))
    for j in range(k+1, 24):
        m = (4*rows[j]['J']+D)*ell-A*u-26*S
        lhs = F(4*rows[j]['J']*ell, S)
        record = dict(position=k, displaced_row=j, J=rows[j]['J'],
                      lhs_lower=str(lhs), rhs_upper=str(rhs), margin=str(F(m, S)),
                      scaled_margin=m, passed=m > 0)
        pairs.append(record)
        check(f'first displacement ({k},{j})', 0, m, '<')
        if j == k+1:
            weakest.append(record.copy())
check('every saved prefix operand', saved['prefixes'], prefixes)
check('all 276 saved pairs with complete operands', saved['pairs'], pairs)
check('all 23 saved weakest cases', saved['weakest'], weakest)
written_weakest = []
for line in text63.splitlines():
    cells = line.strip('|').split('|')
    if len(cells) == 2 and all(c.isdigit() for c in cells):
        written_weakest.append(tuple(map(int, cells)))
check('all written weakest margins', written_weakest,
      [(p['position'], p['scaled_margin']) for p in weakest])
minimum = min(pairs, key=lambda p: p['scaled_margin'])
check('written global minimum', F(minimum['margin']), F(779441541677, 50000000000))
check('stated strict 15.58 threshold', F(1558, 100), F(minimum['margin']), '<')
ints = dict(
    parameters=all(r['J'] >= 8 and r['H'] >= 40 for r in rows),
    increasing_J=all(rows[i]['J'] < rows[i+1]['J'] for i in range(24)),
    tail_allocation=all(r['a'] == 2 for r in rows[:24]) and rows[24]['a'] == 166504412,
    odd_total=K == 397573379,
    even_total=N-K == 232565518,
    full_product_two_exponent=N == 630138897,
    complete_first_displacement_coverage=len(pairs) == 276 and len(weakest) == 23 and
        {(p['position'], p['displaced_row']) for p in pairs} ==
        {(k, j) for j in range(1, 24) for k in range(j)},
)
check('saved integer assertions', saved['integer_checks'], ints)
for name, value in ints.items():
    check(name, value, True)
check('saved summary with minimum operands', saved['summary'],
      dict(pair_count=276, weakest_count=23, minimum=minimum, failures=[]))
failures = [c['name'] for c in checks if not c['passed']]
result = dict(source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              rows=rows, series=series, log_bounds=log_bounds,
              root_bounds=dict(B_upper=bmax, n0_lower=nmin, s0_upper=smax),
              exp24_terms=exp_terms, prefixes=prefixes, pairs=pairs,
              weakest=weakest, literal_J_guards=literal_guards, checks=checks,
              summary=dict(checks=len(checks), pair_count=len(pairs), weakest_count=len(weakest),
                           minimum=minimum, failures=failures))
out = HERE / 'fixed-allocation-order-rigidity-audit-certificate.json'
out.write_text(json.dumps(result, default=str, indent=2)+'\n')
print(f'{len(checks)} exact audit checks; failures: {failures}')
print(f'All 276 margins required >0; actual minimum {minimum["margin"]}; 23 weakest cases matched.')
print(f'Uniform n0 > {nmin} > 18000000000; s0 < {smax} < 20000000000.')
print(f'Independent Lambda interval strictly inside ({lm}, {lp}); all 25 literal J margins >0.')
print(f'Full certificate: {out}')
assert not failures
