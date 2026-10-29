#!/usr/bin/env python3
"""Exact finite operands for L106; factored rationals avoid enormous expansion.

The canonical proof establishes the affine identities and imports L104's
audited logarithmic enclosure after matching its operands. No sampling.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TABLE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
ENCLOSURE = ROOT / 'lemmas/L104-d35-fixed-row0-unit-exclusion.md'
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


B, kap = 9250245, F(23, 11)
budgets = [1, 1, 12]+[0]*21+[B-14]
rows = []
for i, j, old_h in base:
    h = 5 if i == 0 else 32670656 if i == 24 else old_h
    b, a = budgets[i], 2+18*budgets[i]
    rows.append(dict(i=i, J=j, H=h, b=b, a=a,
                     p=3*j+h, q=4*j+h+a,
                     eta=f'23/11-(12/11)*(16/27)^{j}-(16/27)^{j}*(2/3)^{h}'))
    check(f'row{i} nonnegative budget', b, '>=', 0)
    check(f'row{i} J lower', j, '>=', 8)
    check(f'row{i} H positive', h, '>', 0)
    check(f'row{i} tail minimum', a, '>=', 2)
    check(f'row{i} tail residue', a % 18, '=', 2)
check('b0', budgets[0], '=', 1)
check('b1', budgets[1], '=', 1)
check('b2', budgets[2], '=', 12)
check('budget total', sum(budgets), '=', B)
K, N = sum(r['p'] for r in rows), sum(r['q'] for r in rows)
check('K matches audited L104', K, '=', 397573379)
check('N matches audited L104', N, '=', 630138897)
check('eta power majorant', F(16, 27)**8, '<', F(1, 2))
check('eta strict lower exceeds1', kap/2, '>', 1)
lm, lp = F(10584, 10**14), F(10585, 10**14)
check('Lambda lower positive', lm, '>', 0)
check('Lambda upper below1', lp, '<', 1)
dup = lp/(1-lp)
check('D strict upper', dup, '<', F(1, 100))
all_n_lower = 1/dup
all_s_lower = all_n_lower+kap
check('all n strict lower', all_n_lower, '>', 100)
check('all s strict lower', all_s_lower, '>', F(540, 11))
cuts = []
for start in range(25):
    p = q = 0
    prefixes = []
    for k in range(25):
        r = rows[(start+k) % 25]
        prefixes.append(dict(input_row=r['i'], p=p, q=q))
        p += r['p']
        q += r['q']
    check(f'cut{start} full p', p, '=', K)
    check(f'cut{start} full q', q, '=', N)
    check(f'cut{start} first prefix p', prefixes[0]['p'], '=', 0)
    check(f'cut{start} first prefix q', prefixes[0]['q'], '=', 0)
    cuts.append(dict(start=start, prefixes=prefixes,
                     B='sum_k eta[input_row[k]]*2^q[k]/3^p[k]',
                     n='B/(2^N/3^K-1)', s='n+23/11'))
r2, second = rows[2], cuts[2]['prefixes'][1]
check('row2 p', r2['p'], '=', 218)
check('row2 q', r2['q'], '=', 464)
check('cut2 second row', second['input_row'], '=', 3)
check('cut2 second prefix p', second['p'], '=', 218)
check('cut2 second prefix q', second['q'], '=', 464)
check('power comparison factor41', 3**41, '<', 2**65)
check('power comparison factor13', 3**13, '<', 2**21)
check('small integer power comparison', 3**218, '<', 2**346)
check('reciprocal c2 exponent', 464-346, '=', 118)
required = F(4, 11)*2**112
s2_lower = F(2**118)/dup+kap
check('s2 strict lower exceeds2^118', s2_lower, '>', 2**118)
check('coarse s2 lower exceeds target', 2**118, '>', required)
failures = [c['name'] for c in checks if not c['passed']]
result = dict(scope='endpoint-only d35 counterexample; no J/H guards',
    sources=[dict(path=str(p.relative_to(ROOT)),
                  sha256=hashlib.sha256(p.read_bytes()).hexdigest())
             for p in (TABLE, ENCLOSURE)],
    rows=rows, K=K, N=N, exact_tuple=cuts,
    definitions=dict(c='3^p/2^q', D='2^N/3^K-1',
                     equation='n[i+1]=c[i]*(n[i]+eta[i])',
                     closure='n[25]=n[0]'),
    imported_enclosure=dict(lower=lm, upper=lp,
                            status='L104 audited input; logs not recomputed'),
    bounds=dict(D_upper=dup, eta_lower=kap/2, all_n_lower=all_n_lower,
                all_s_lower=all_s_lower, required_s_lower=F(540, 11),
                s2_lower=s2_lower, coarse_s2_lower=2**118,
                row2_threshold=required, coarse_gap=2**118-required),
    checks=checks,
    summary=dict(verdict='CAP_REFUTED' if not failures else 'UNCERTIFIED',
                 checks=len(checks), failures=failures, samples=0,
                 independent_audit=False),
    limitations='Exact tuple is factored rational; closure and identities proved in L106. No full guards, actual-word or Collatz conclusion.')
out = HERE / 'd35-full-support-row2-counterexample-certificate.json'
out.write_text(json.dumps(result, default=str, indent=2)+'\n')
print(f'Verdict={result["summary"]["verdict"]}; checks={len(checks)}; failures={failures}')
print(f'Budgets: b0=b1=1,b2=12,b24={B-14},others0; total={sum(budgets)}; K={K}; N={N}')
print(f'All s_i > {all_s_lower}; required >=540/11')
print(f's2 > {2**118}; proposed cap < {required}; gap={2**118-required}')
print(f'Certificate: {out.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
