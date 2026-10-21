#!/usr/bin/env python3
"""Exact finite arithmetic for the approved d=5 recipient-zero comparison.

The uniform implication is proved in L085; no allocations are sampled.
The analytic Lambda enclosure is imported from audited L055/L084.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
rows = [(int(i), int(j), int(h)) for i, j, h in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$',
    (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text(),
    re.M)]
assert [i for i, _, _ in rows] == list(range(25))
rows = [(i, j, h - 5 if i == 0 else h + 5 if i == 24 else h)
        for i, j, h in rows]
B = 9250245
K = sum(3*j+h for _, j, h in rows)
N = sum(4*j+h for _, j, h in rows) + 2*len(rows) + 18*B
kappa = F(23, 11)
lam = F(10584, 10**14)
E = F(23*(len(rows)-1), 4*2**(4*rows[1][1])-23)
R = kappa/(lam-E)+kappa
U = F(20000000000)
_, j0, h0 = rows[0]
j1 = rows[1][1]
G0 = F(3**(3*j0+h0), 2**(4*j0+h0))
Q0 = F(12, 11)*F(3, 2)**h0+1
offset = kappa-Q0/2**20
endpoint = G0*U/2**20+offset
threshold = F(4, 11)*2**(4*j1)

checks = []
def check(name, actual, relation, required):
    passed = {'<': actual < required, '>': actual > required,
              '==': actual == required}[relation]
    checks.append(dict(name=name, actual=actual, relation=relation,
                       required=required, difference=actual-required,
                       passed=passed))

check('row count', len(rows), '==', 25)
check('minimum H', min(h for _, _, h in rows), '>', 2)
check('minimum J increment', min(rows[i+1][1]-rows[i][1]
                               for i in range(24)), '>', 0)
check('K invariant', K, '==', 397573379)
check('N invariant', N, '==', 630138897)
check('positive residual', lam-E, '>', 0)
check('guard-conditioned cap', R, '<', U)
check('failed old offset datum preserved', Q0, '<', kappa*2**20)
check('actual signed offset positive', offset, '>', 0)
check('signed endpoint upper', endpoint, '<', F(2*10**12))
check('row-1 threshold lower', threshold, '>', F(4*10**17))
check('strict signed rejection', endpoint, '<', threshold)

failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    scope='d=5, literal order, integer b_i>=0, sum b_i=9250245, b_0>=1; '
          'all cyclic endpoints, lower domains and own-input J guards',
    imported_analytic_input='L055 (2), independently audited in L084 (2): '
          '10584/10^14 < N log 2-K log 3 < 10585/10^14; not recertified here',
    rows=rows, B=B, K=K, N=N, lambda_lower=lam, E=E, residual=lam-E,
    cap=R, U=U, G0=G0, Q0=Q0, signed_offset=offset,
    endpoint_upper=endpoint, row1_threshold=threshold,
    strict_separation=threshold-endpoint, checks=checks,
    summary=dict(checks=len(checks), failures=failures, passed=not failures),
    limitations='No sampled roots, feasibility, other recipients, order reduction, '
                'integer realization, actual-word application or universal descent.')
path = HERE / 'd5-signed-recipient-zero-certificate.json'
path.write_text(json.dumps(result, indent=2, default=str)+'\n')
print(f'Checks: {len(checks)}; failures: {failures}')
print(f'Cap actual R={R}; required U={U}; R<U: {R < U}')
print(f'Signed endpoint upper={endpoint}; certified <2000000000000')
print(f'Required row-1 input >= {threshold}; certified >400000000000000000')
print(f'Strict rejection: {endpoint < threshold}')
print(f'Certificate: {path.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
