#!/usr/bin/env python3
"""Exact arithmetic for the approved literal d=6,...,33 recipient-zero test.

The quantified implication is proved in L090. No allocation is sampled.
The unchanged analytic Lambda enclosure is imported from audited L055/L084.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
base = [(int(i), int(j), int(h)) for i, j, h in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$',
    (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text(),
    re.M)]
assert [i for i, _, _ in base] == list(range(25))
B = 9250245
kappa = F(23, 11)
lam = F(10584, 10**14)
E = F(23*24, 4*2**60-23)
residual = lam-E
R = kappa/residual+kappa
U = F(20000000000)
threshold = F(4, 11)*2**60
coefficient = F(27, 16)**8*U-F(12, 11)
checks = []


def check(name, actual, relation, required):
    passed = {'<': actual < required, '>': actual > required,
              '==': actual == required}[relation]
    record = dict(name=name, actual=actual, relation=relation,
                  required=required, difference=actual-required, passed=passed)
    checks.append(record)
    return record


common_checks = [
    check('row count', len(base), '==', 25),
    check('first J', base[0][1], '==', 8),
    check('next J', base[1][1], '==', 15),
    check('minimum J increment', min(base[i+1][1]-base[i][1]
                                   for i in range(24)), '>', 0),
    check('positive residual', residual, '>', 0),
    check('guard-conditioned cap', R, '<', U),
    check('positive H coefficient', coefficient, '>', 0),
    check('row1 guard lower', threshold, '>', F(4*10**17)),
]
cases = []
for d in range(6, 34):
    rows = [(i, j, h-d if i == 0 else h+d if i == 24 else h)
            for i, j, h in base]
    K = sum(3*j+h for _, j, h in rows)
    N = sum(4*j+h for _, j, h in rows)+2*len(rows)+18*B
    _, j0, h0 = rows[0]
    G = F(3**(3*j0+h0), 2**(4*j0+h0))
    Q = F(12, 11)*F(3, 2)**h0+1
    offset = kappa-Q/2**20
    endpoint = (G*U-Q)/2**20+kappa
    factored = F(3, 2)**h0*coefficient/2**20+kappa-F(1, 2**20)
    case_checks = [
        check(f'd{d} minimum H', min(h for _, _, h in rows), '>', 2),
        check(f'd{d} sum J', sum(j for _, j, _ in rows), '==', 66061058),
        check(f'd{d} sum H', sum(h for _, _, h in rows), '==', 199390205),
        check(f'd{d} K', K, '==', 397573379),
        check(f'd{d} N', N, '==', 630138897),
        check(f'd{d} signed offset positive', offset, '>', 0),
        check(f'd{d} factored endpoint agrees', factored, '==', endpoint),
        check(f'd{d} endpoint common upper', endpoint, '<', F(2*10**12)),
        check(f'd{d} strict own-input rejection', endpoint, '<', threshold),
    ]
    cases.append(dict(d=d, rows=rows, K=K, N=N, G0=G, Q0=Q,
                      signed_offset=offset, endpoint_upper=endpoint,
                      factored_endpoint=factored,
                      strict_separation=threshold-endpoint, checks=case_checks))

maximum = max(cases, key=lambda c: c['endpoint_upper'])
uniform_checks = [
    check('maximum at d6', maximum['d'], '==', 6),
    check('maximum signed endpoint', maximum['endpoint_upper'], '<', F(2*10**12)),
    check('uniform strict separation', threshold-maximum['endpoint_upper'], '>', 0),
]
failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    scope='Literal d=6,...,33; integer b_i>=0, sum b_i=9250245; '
          'all cyclic endpoints, s_i>=540/11, non-strict own-input J guards; b_0>=1',
    imported_analytic_input='L055 (2), L084 (2) and its independent audit: '
          '10584/10^14 < N log2-K log3 < 10585/10^14; not recertified here',
    B=B, kappa=kappa, lambda_lower=lam, E=E, residual=residual, cap=R, U=U,
    row1_threshold=threshold, common_checks=common_checks,
    uniform_comparison=dict(coefficient=coefficient, maximum_d=maximum['d'],
         maximum_endpoint=maximum['endpoint_upper'], endpoint_bound=2*10**12,
         threshold=threshold, minimum_separation=threshold-maximum['endpoint_upper'],
         checks=uniform_checks),
    cases=cases,
    case_verdicts=[dict(d=c['d'], checks=len(c['checks']),
                        passed=all(q['passed'] for q in c['checks'])) for c in cases],
    summary=dict(tables=len(cases), checks=len(checks), failures=failures,
                 passed=not failures),
    limitations='No other recipients, orders, last-pair/survivor analysis, '
                 'feasibility, integer/actual-word exclusion or universal descent.')
path = HERE / 'uniform-recipient-zero-certificate.json'
path.write_text(json.dumps(result, indent=2, default=str)+'\n')
print(f'Tables: {len(cases)}; checks: {len(checks)}; failures: {failures}')
print(f'Cap actual R={R}; required R<U={U}; passed: {R < U}')
print(f'Maximum signed endpoint at d={maximum["d"]}: {maximum["endpoint_upper"]}')
print(f'Required endpoint <2000000000000: {maximum["endpoint_upper"] < 2*10**12}')
print(f'Row1 guard requires >= {threshold}; uniform strict rejection: {not failures}')
print(f'Certificate: {path.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
