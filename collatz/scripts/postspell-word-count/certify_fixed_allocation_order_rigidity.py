#!/usr/bin/env python3
"""Exact sufficient J-guard comparisons for every first displaced row.

Uses the audited logarithm and Lambda intervals of L055 as inputs.
Symbolic all-order coverage and affine closure are proved in L063.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
source = (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
table = [tuple(map(int, m)) for m in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', source, re.M)]
assert len(table) == 25 and [r[0] for r in table] == list(range(25))
rows = [dict(index=i, J=j, H=h, a=2 if i < 24 else 166504412) for i, j, h in table]
S = 10**12
l2, u2, l3, u3 = [Q(v, S) for v in (693147180559, 693147180560, 1098612288668, 1098612288669)]
lm, lp = Q(10584, 10**14), Q(10585, 10**14)
checks = []


def less(name, actual, required):
    actual, required = Q(actual), Q(required)
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       relation='<', margin=str(required-actual), passed=actual < required))


integer_checks = dict(
    parameters=all(r['J'] >= 8 and r['H'] >= 40 for r in rows),
    increasing_J=all(rows[i]['J'] < rows[i+1]['J'] for i in range(24)),
    tail_allocation=all(r['a'] == 2 for r in rows[:24]) and rows[24]['a'] == 166504412,
    odd_total=sum(3*r['J']+r['H'] for r in rows) == 397573379,
    even_total=sum(r['J']+r['a'] for r in rows) == 232565518,
    full_product_two_exponent=sum(4*r['J']+r['H']+r['a'] for r in rows) == 630138897,
)
baseline_c = Q(3**64, 2**74)
baseline_eta = Q(23, 11)-Q(12, 11)*Q(16, 27)**8-Q(16, 27)**8*Q(2, 3)**40
less('uniform first multiplier baseline', 10**8, baseline_c)
less('uniform first eta baseline', 2, baseline_eta)
less('all growing multipliers', 2, Q(27,16)**2*Q(3,2)**3/4)
less('shifted additive term negative for H>=5', Q(81,44), Q(3,11)*Q(3,2)**5)
less('positive imported Lambda lower', 0, lm)
less('ordered imported Lambda endpoints', lm, lp)
less('imported Lambda upper below one', lp, 1)
B_upper = Q(23,11)*(1+Q(2,10**8))
n_lower = 2*(1-lp)/lp
s_upper = B_upper/lm+Q(23,11)
less('uniform n0 lower', 18*10**9, n_lower)
less('uniform s0 upper', s_upper, 20*10**9)
less('uniform lower junction guard', Q(540,11), 18*10**9)
terms = [Q(1)]
for k in range(1, 41):
    terms.append(terms[-1]*24/k)
less('exp24 partial sum exceeds 20 billion', 20*10**9, sum(terms))
less('exp2 partial sum exceeds 11/4', Q(11,4), 5)

prefixes, pairs, weakest = [], [], []
A = D = 0
for k in range(24):
    rhs = 26+A*u3-D*l2
    prefixes.append(dict(position=k, three_exponent=A, two_exponent=D,
                         h_upper=str(rhs-2), guard_rhs_upper=str(rhs)))
    for j in range(k+1, 24):
        lhs = 4*rows[j]['J']*l2
        margin = lhs-rhs
        record = dict(position=k, displaced_row=j, J=rows[j]['J'],
                      lhs_lower=str(lhs), rhs_upper=str(rhs),
                      margin=str(margin), scaled_margin=int(margin*S), passed=margin > 0)
        assert margin*S == record['scaled_margin']
        pairs.append(record)
        if j == k+1:
            weakest.append(record.copy())
    A += 3*rows[k]['J']+rows[k]['H']
    D += 4*rows[k]['J']+rows[k]['H']+2
integer_checks['complete_first_displacement_coverage'] = (
    len(pairs) == 276 and len(weakest) == 23
    and {(p['position'],p['displaced_row']) for p in pairs} ==
        {(k,j) for k in range(23) for j in range(k+1,24)})
failures = [c['name'] for c in checks if not c['passed']]
failures += [name for name, ok in integer_checks.items() if not ok]
failures += [f"guard pair {p['position']},{p['displaced_row']}" for p in pairs if not p['passed']]
smallest = min(pairs, key=lambda p: Q(p['margin']))
result = dict(
    verdict='ONLY_LITERAL_ORDER_SATISFIES_J_GUARDS_AND_CYCLIC_ENDPOINTS' if not failures else 'SUFFICIENT_COMPARISON_FAILED',
    scope='L055 rows 0..23 permuted intact, row 24 fixed last; all-order coverage by first displacement',
    imported_intervals=dict(source='L055 (2) and (6), independently audited there',
                            log2=[str(l2),str(u2)],log3=[str(l3),str(u3)],Lambda=[str(lm),str(lp)]),
    rows=rows, bounds=dict(B_upper=str(B_upper),n0_lower=str(n_lower),s0_upper=str(s_upper)),
    exp24_terms=[str(t) for t in terms], checks=checks, integer_checks=integer_checks,
    prefixes=prefixes,pairs=pairs,weakest=weakest,
    summary=dict(pair_count=len(pairs),weakest_count=len(weakest),minimum=smallest,failures=failures),
    limitations='Necessary subsystem only; literal existence imported from L055; no integer exclusion assembled; separate critical audit pending')
path = HERE / 'fixed-allocation-order-rigidity-certificate.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print(f"All {len(pairs)} first-displacement margins required >0; minimum {smallest['margin']} at ({smallest['position']},{smallest['displaced_row']})")
print(f"Uniform s0 upper {s_upper} < {20*10**9}; {len(checks)} rational and {len(integer_checks)} integer checks; failures: {failures}")
print(f'Certificate: {path}')
assert not failures
