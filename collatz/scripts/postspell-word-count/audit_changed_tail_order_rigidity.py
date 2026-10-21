#!/usr/bin/env python3
"""Independent L067 audit; does not import or execute any certifier."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE / 'changed-tail-order-rigidity-certificate.json'
saved = json.loads(SOURCE.read_text())
rows = []
for line in (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text().splitlines():
    cells = line.strip('|').split('|')
    if len(cells) == 3 and all(c.isdigit() for c in cells):
        i, j, h = map(int, cells)
        rows.append(dict(index=i, J=j, H=h, a=20 if i == 23 else 166504394 if i == 24 else 2))
checks = []


def check(name, actual, required, relation='='):
    passed = actual == required if relation == '=' else actual < required
    checks.append(dict(name=name, actual=actual, required=required,
                       relation=relation, passed=passed))


check('indices', [r['index'] for r in rows], list(range(25)))
check('all saved attached rows', saved['rows'], rows)
K = sum(3*r['J']+r['H'] for r in rows)
N = sum(4*r['J']+r['H']+r['a'] for r in rows)
check('exact totals J H tails K N', [sum(r['J'] for r in rows), sum(r['H'] for r in rows),
      sum(r['a'] for r in rows), K, N], [66061058, 199390205, 166504460, 397573379, 630138897])
S = 10**12
ell, upper2, lower3, u = 693147180559, 693147180560, 1098612288668, 1098612288669
lm, lp = F(10584, 10**14), F(10585, 10**14)
series = {}


def log_interval(t, name):
    x = (t-1)/(t+1)
    assert 0 < x <= F(1, 2)
    # Unrounded rational terms, direct at t=2 and 3, unlike binary reduction.
    terms = [2*x**(2*i+1)/(2*i+1) for i in range(128)]
    remainder = 2*x**257/(257*(1-x*x))
    low = sum(terms)
    series[name] = dict(argument=t, x=x, terms=terms, remainder=remainder,
                        lower=low, upper=low+remainder)
    return low, low+remainder


l2, u2 = log_interval(F(2), 'log2')
l3, u3 = log_interval(F(3), 'log3')
lc, uc = log_interval(F(11, 4), 'log11over4')
lh, uh = log_interval(F(18*10**9, 2**34), 'height_mantissa')
lh, uh = lh+34*l2, uh+34*u2
lambda_bounds = [N*l2-K*u3, N*u2-K*l3]
log_bounds = dict(log2=[l2, u2], log3=[l3, u3], log11over4=[lc, uc],
                  log18b=[lh, uh], Lambda=lambda_bounds)
for name, a, b in [
    ('log2 lower', F(ell, S), l2), ('log2 upper', u2, F(upper2, S)),
    ('log3 lower', F(lower3, S), l3), ('log3 upper', u3, F(u, S)),
    ('Lambda lower', lm, lambda_bounds[0]), ('Lambda upper', lambda_bounds[1], lp),
    ('literal log-height lower', F(2361, 100), lh),
    ('literal log constant lower', F(1011600911678, S), lc),
    ('literal alpha lower', F(523248143764, S), 3*l3-4*u2),
    ('literal beta lower', F(405465108108, S), l3-u2),
]:
    check(name, a, b, '<')
check('saved imported intervals', saved['imported_intervals'], dict(
    source='L055 (2) and (6), independently audited there',
    log2=[str(F(ell, S)), str(F(upper2, S))],
    log3=[str(F(lower3, S)), str(F(u, S))], Lambda=[str(lm), str(lp)]))

baseline = F(3**64, 2**74)
changed = F(3**104, 2**132)
eta = F(23, 11)-F(12*16**8, 11*27**8)-F(16**8*2**40, 27**8*3**40)
bmax = F(23, 11)*(1+F(2, 10**8))
nmin, smax = 2/lp-2, bmax/lm+F(23, 11)
exp_terms = [F(24**i, factorial(i)) for i in range(41)]
support = [
    ('changed baseline dominates tail-2 baseline', baseline, changed),
    ('changed baseline exceeds 100 million', F(10**8), changed),
    ('changed-baseline ratio exceeds one', F(1), F(3**40, 2**58)),
    ('uniform first multiplier baseline', F(10**8), baseline),
    ('uniform first eta baseline', F(2), eta),
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
records = []
for name, a, b in support:
    check(name, a, b, '<')
    records.append(dict(name=name, actual=str(a), required=str(b),
                        relation='<', margin=str(b-a), passed=a < b))
check('all saved support operands and margins', saved['checks'], records)
check('all saved exponential terms', saved['exp24_terms'], list(map(str, exp_terms)))
check('saved root bounds', saved['bounds'], dict(B_upper=str(bmax), n0_lower=str(nmin), s0_upper=str(smax)))
check('written eta', eta, F(7122556955297586891012225981605, 3433683820292512484657849089281))
check('written root lower', nmin, F(39999999995766, 2117))
check('written root upper', smax, F(95833335260143, 4851))
check('written changed ratio integers', [3**40, 2**58], [12157665459056928801, 288230376151711744])
check('written exp24 sum', sum(exp_terms), F(202750314819830504045671593478515759301, 7661655986496068058455078125))

pairs, weakest, prefixes, literal = [], [], [], []
for k in range(25):
    # Each prefix is independently summed, not propagated from its predecessor.
    A = sum(3*r['J']+r['H'] for r in rows[:k])
    D = sum(4*r['J']+r['H']+r['a'] for r in rows[:k])
    v = 2361*S//100+A*lower3-D*upper2
    jmargin = v+1011600911678-4*rows[k]['J']*upper2
    direct_margin = F(2361, 100)+A*l3-(D+4*rows[k]['J'])*u2+lc
    literal.append(dict(index=k, A=A, D=D, v=v, J=rows[k]['J'],
                        scaled_margin=jmargin, independent_lower=direct_margin))
    check(f'literal J guard {k}', 0, jmargin, '<')
    check(f'independent literal J lower {k}', F(jmargin, S), direct_margin, '<')
    if k == 24:
        continue
    rhs = F(26*S+A*u-D*ell, S)
    prefixes.append(dict(position=k, three_exponent=A, two_exponent=D,
                         h_upper=str(rhs-2), guard_rhs_upper=str(rhs)))
    for j in range(k+1, 24):
        m = (4*rows[j]['J']+D)*ell-A*u-26*S
        p = dict(position=k, displaced_row=j, J=rows[j]['J'],
                 lhs_lower=str(F(4*rows[j]['J']*ell, S)), rhs_upper=str(rhs),
                 margin=str(F(m, S)), scaled_margin=m, passed=m > 0)
        pairs.append(p)
        check(f'first displacement {k},{j}', 0, m, '<')
        if j == k+1:
            weakest.append(p.copy())
check('all saved prefixes', saved['prefixes'], prefixes)
check('all saved pair operands', saved['pairs'], pairs)
check('all saved weakest operands', saved['weakest'], weakest)
text63 = (ROOT / 'lemmas/L063-fixed-allocation-j-guard-order-rigidity.md').read_text()
written63 = [tuple(map(int, p)) for p in re.findall(r'^\|(\d+)\|(\d+)\|$', text63, re.M)]
check('all 23 canonical L063 margins', written63, [(p['position'], p['scaled_margin']) for p in weakest])
text64 = (ROOT / 'lemmas/L064-single-tail-redistribution-j-guard-classification.md').read_text()
written64 = text64.split('For j=23 the lower numerators')[1].split('```text')[1].split('```')[0]
check('all 25 canonical L064 literal margins', list(map(int, written64.split())),
      [r['scaled_margin'] for r in literal])
minimum = min(pairs, key=lambda p: p['scaled_margin'])
check('minimum', F(minimum['margin']), F(779441541677, 50000000000))
check('minimum above stated threshold', F(1558, 100), F(minimum['margin']), '<')
check('literal minimum', min(r['scaled_margin'] for r in literal), 402427610954)
ints = dict(
    parameters=all(r['J'] >= 8 and r['H'] >= 40 for r in rows),
    increasing_J=all(rows[i]['J'] < rows[i+1]['J'] for i in range(24)),
    tail_allocation=all(r['a'] == 2 for r in rows[:23]) and rows[23]['a'] == 20 and rows[24]['a'] == 166504394,
    odd_total=K == 397573379, even_total=N-K == 232565518,
    full_product_two_exponent=N == 630138897,
    changed_row_lower_hypotheses=rows[23]['J'] >= 8 and rows[23]['H'] >= 80,
    complete_first_displacement_coverage=len(pairs) == 276 and len(weakest) == 23 and
        {(p['position'], p['displaced_row']) for p in pairs} ==
        {(k, j) for j in range(1, 24) for k in range(j)},
)
check('saved integer assertions', saved['integer_checks'], ints)
for name, ok in ints.items():
    check(name, ok, True)
check('saved summary', saved['summary'], dict(pair_count=276, weakest_count=23, minimum=minimum, failures=[]))


def encode(value):
    if isinstance(value, F):
        return str(value)
    raise TypeError(type(value))


failures = [c['name'] for c in checks if not c['passed']]
result = dict(source=str(SOURCE.relative_to(ROOT)), sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              rows=rows, series=series, log_bounds=log_bounds, checks=checks,
              bounds=dict(B_upper=bmax, n0_lower=nmin, s0_upper=smax),
              exp24_terms=exp_terms, supporting_comparisons=records,
              prefixes=prefixes, pairs=pairs, weakest=weakest, literal_guards=literal,
              summary=dict(checks=len(checks), failures=failures, minimum=minimum,
                           literal_minimum=F(min(r['scaled_margin'] for r in literal), S)),
              scope='Independent arithmetic audit of L067; all-order quantifiers require its written proof.')
path = HERE / 'changed-tail-order-rigidity-audit-certificate.json'
path.write_text(json.dumps(result, default=encode, indent=2)+'\n')
print(f'{len(checks)} exact checks; 276 first-displacement pairs and 25 literal guards; failures: {failures}')
print(f"Minimum rejection > {minimum['margin']} > 15.58; required > 0")
print(f'n0 > {nmin} > 18000000000; s0 < {smax} < 20000000000')
print(f'Certificate: {path.relative_to(ROOT)}')
assert not failures
