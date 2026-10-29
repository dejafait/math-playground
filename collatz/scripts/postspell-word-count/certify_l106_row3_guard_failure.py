#!/usr/bin/env python3
"""Exact finite operands for C106a; imports the audited L104 enclosure.

No huge powers, rounded orbit, or numerical logarithms are evaluated.
The canonical proof supplies the cyclic identities and strict inequalities.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TABLE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
INPUTS = [TABLE, ROOT / 'lemmas/L104-d35-fixed-row0-unit-exclusion.md',
          ROOT / 'lemmas/L106-d35-full-support-row2-cap-counterexample.md']
base = [tuple(map(int, r)) for r in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', TABLE.read_text(), re.M)]
assert [r[0] for r in base] == list(range(25))
checks = []


def check(name, actual, relation, required):
    a, b = F(actual), F(required)
    passed = {'=': a == b, '<': a < b, '>': a > b,
              '>=': a >= b}[relation]
    checks.append(dict(name=name, actual=a, relation=relation,
                       required=b, difference=a-b, passed=passed))


budgets = [1, 1, 12]+[0]*21+[9250231]
rows = []
for i, j, old_h in base:
    h = 5 if i == 0 else 32670656 if i == 24 else old_h
    a = 2+18*budgets[i]
    rows.append(dict(i=i, J=j, H=h, b=budgets[i], a=a,
                     p=3*j+h, q=4*j+h+a))
check('budget total', sum(budgets), '=', 9250245)
K, N = sum(r['p'] for r in rows), sum(r['q'] for r in rows)
check('K matches audited L104', K, '=', 397573379)
check('N matches audited L104', N, '=', 630138897)
for i in range(3, 24):
    check(f'row{i} tail', rows[i]['a'], '=', 2)
    check(f'row{i} H at least6', rows[i]['H'], '>=', 6)
    check(f'row{i} J positive', rows[i]['J'], '>', 0)
check('tail2 growth lower', F(3, 2)**6/4, '>', 2)
geometric = sum((F(1, 2)**k for k in range(22)), F(0))
check('first22 reciprocal-prefix majorant', geometric, '<', 2)
check('small power majorant', 3**5, '<', 2**8)
products = []
for indices in ([2], [1, 2], [0, 1, 2]):
    p = sum(rows[i]['p'] for i in indices)
    q = sum(rows[i]['q'] for i in indices)
    t, r = divmod(p, 5)
    exponent = 8*t+2*r
    if r:
        check(f'remainder power{indices}', 3**r, '<', 2**(2*r))
    check(f'product exponent gap{indices}', exponent, '<', q)
    check(f'direct product below1{indices}', 3**p, '<', 2**q)
    products.append(dict(indices=indices, p=p, q=q, quotient=t,
                         remainder=r, upper_power_of_two=exponent))
prefixes = []
p = q = 0
for k in range(25):
    row = rows[(3+k) % 25]
    prefixes.append(dict(k=k, input_row=row['i'], p=p, q=q))
    p += row['p']
    q += row['q']
for k, indices in ((22, [0, 1, 2]), (23, [1, 2]), (24, [2])):
    pr = prefixes[k]
    check(f'closing prefix{k} p', pr['p'], '=', K-sum(rows[i]['p'] for i in indices))
    check(f'closing prefix{k} q', pr['q'], '=', N-sum(rows[i]['q'] for i in indices))
    check(f'closing prefix{k} input', pr['input_row'], '=', k-22)
kap = F(23, 11)
lm, lp = F(10584, 10**14), F(10585, 10**14)
check('Lambda lower positive', lm, '>', 0)
check('Lambda upper below half', lp, '<', F(1, 2))
check('exponential upper majorant', 1/(1-lp), '<', 2)
cap = 8*kap/lm+kap
coarse = 10**12
check('s3 strict cap below coarse', cap, '<', coarse)
check('J3 literal', rows[3]['J'], '=', 52)
threshold = F(4, 11)*2**(4*rows[3]['J'])
check('coarse below required J3', coarse, '<', threshold)
failures = [c['name'] for c in checks if not c['passed']]
data = dict(scope='L106 fixed tuple only; one failed own-input J guard',
    sources=[dict(path=str(p.relative_to(ROOT)),
                  sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in INPUTS],
    rows=rows, totals=dict(K=K, N=N), cut3_prefixes=prefixes,
    suffix_products=products,
    imported_enclosure=dict(lower=lm, upper=lp,
        status='Audited L104 input after identical K,N; not recomputed'),
    bounds=dict(first22_reciprocal_sum_upper=geometric,
        each_final_reciprocal_prefix_strict_upper=2,
        numerator_strict_upper=8*kap, D_strict_lower=lm,
        s3_strict_upper=cap, coarse_s3_strict_upper=coarse,
        row3_J_required_lower=threshold, strict_separation=threshold-cap),
    checks=checks,
    summary=dict(verdict='ROW3_J_GUARD_FAILS' if not failures else 'UNCERTIFIED',
                 checks=len(checks), failures=failures, independent_audit=False),
    limitations='Other49 guards untested. Does not assert actual-word feasibility or universal descent.')
out = HERE / 'l106-row3-guard-failure-certificate.json'
out.write_text(json.dumps(data, default=str, indent=2)+'\n')
print(f'Verdict={data["summary"]["verdict"]}; checks={len(checks)}; failures={failures}')
print(f's3 < {cap} < {coarse}; row3 J requires s3 >= {threshold}')
print(f'Certificate: {out.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
