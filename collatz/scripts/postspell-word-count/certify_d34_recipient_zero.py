#!/usr/bin/env python3
"""Finite rational arithmetic for the approved d34 recipient-zero test.

L098 supplies the quantified argument; no allocations or roots are sampled.
The invariant Lambda enclosure is imported from audited L055/L084.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
source = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
base = [(int(i), int(j), int(h)) for i, j, h in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', source.read_text(), re.M)]
assert [i for i, _, _ in base] == list(range(25))
rows = [(i, j, h-34 if i == 0 else h+34 if i == 24 else h)
        for i, j, h in base]
B = 9250245
sum_J = sum(j for _, j, _ in rows)
sum_H = sum(h for _, _, h in rows)
sum_a = 2*len(rows)+18*B
K = 3*sum_J+sum_H
N = 4*sum_J+sum_H+sum_a
kappa = F(23, 11)
lam = F(10584, 10**14)
E = F(23*(len(rows)-1), 4*2**(4*rows[1][1])-23)
residual = lam-E
R = kappa/residual+kappa
U = F(20000000000)
_, j0, h0 = rows[0]
G0 = F(27, 16)**j0 * F(3, 2)**h0
Q0 = F(12, 11)*F(3, 2)**h0+1
offset = kappa-Q0/2**20
endpoint = (G0*U-Q0)/2**20+kappa
coefficient = F(27, 16)**j0*U-F(12, 11)
factored = F(3, 2)**h0*coefficient/2**20+kappa-F(1, 2**20)
threshold = F(4, 11)*2**(4*rows[1][1])
checks = []


def check(name, actual, relation, required):
    passed = {'<': actual < required, '>': actual > required,
              '==': actual == required}[relation]
    checks.append(dict(name=name, actual=actual, relation=relation,
                       required=required, difference=actual-required,
                       passed=passed))


check('row count', len(rows), '==', 25)
check('changed H0', h0, '==', 6)
check('changed H24', rows[24][2], '==', 32670655)
check('minimum H', min(h for _, _, h in rows), '>', 2)
check('first J', j0, '==', 8)
check('next J', rows[1][1], '==', 15)
check('minimum J increment', min(rows[i+1][1]-rows[i][1]
                               for i in range(24)), '>', 0)
check('sum J invariant', sum_J, '==', 66061058)
check('sum H invariant', sum_H, '==', 199390205)
check('total tails', sum_a, '==', 166504460)
check('K invariant', K, '==', 397573379)
check('N invariant', N, '==', 630138897)
check('positive residual', residual, '>', 0)
check('guard-conditioned cap', R, '<', U)
check('failed old offset datum preserved', Q0, '<', kappa*2**20)
check('actual signed offset positive', offset, '>', 0)
check('direct and factored endpoints agree', endpoint, '==', factored)
check('signed endpoint upper', endpoint, '<', F(15000000))
check('row1 threshold lower', threshold, '>', F(4*10**17))
check('strict signed rejection', endpoint, '<', threshold)

failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    scope='Literal d34; integer b_i>=0, sum b_i=9250245; all cyclic '
          'endpoints, s_i>=540/11, non-strict own-input J guards; b_0>=1',
    source=dict(path=str(source.relative_to(ROOT)),
                sha256=hashlib.sha256(source.read_bytes()).hexdigest()),
    imported_analytic_input='L055 (2), L084 (2) and independent audit: '
          '10584/10^14 < N log2-K log3 < 10585/10^14; not recertified here',
    rows=rows, B=B, sum_J=sum_J, sum_H=sum_H, sum_a=sum_a, K=K, N=N,
    cap=dict(lambda_lower=lam, E=E, residual=residual, R=R, U=U),
    signed_comparison=dict(G0=G0, Q0=Q0, signed_offset=offset,
        coefficient=coefficient, endpoint=endpoint, factored_endpoint=factored,
        endpoint_bound=15000000, endpoint_slack=F(15000000)-endpoint,
        row1_threshold=threshold, strict_separation=threshold-endpoint),
    checks=checks,
    summary=dict(checks=len(checks), failures=failures, passed=not failures),
    limitations='No other recipients, order reduction, last-pair assembly, '
                'feasibility, integer realization, actual-word application '
                'or universal descent. Construction check, not critical audit.')
path = HERE / 'd34-recipient-zero-certificate.json'
path.write_text(json.dumps(result, indent=2, default=str)+'\n')
print(f'Checks: {len(checks)}; failures: {failures}')
print(f'Cap actual R={R}; required R<U={U}; passed: {R < U}')
print(f'Signed endpoint={endpoint}; required <15000000; passed: {endpoint < 15000000}')
print(f'Row1 guard requires >= {threshold}; strict rejection: {endpoint < threshold}')
print(f'Certificate: {path.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
