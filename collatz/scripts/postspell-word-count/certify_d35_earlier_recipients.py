#!/usr/bin/env python3
"""L103 finite exact data; its proof supplies full-simplex coverage.

Imports L055's table, L076's cap argument and L084's audited analytic
enclosures. No parameter sampling, auxiliary roots or actual-word claims.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
source = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
raw = source.read_bytes()
base = [tuple(map(int, row)) for row in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', raw.decode(), re.M)]
assert [i for i, _, _ in base] == list(range(25))
rows = [(i, j, 5 if i == 0 else 32670656 if i == 24 else h)
        for i, j, h in base]
prior_path = HERE / 'h-transfer-family-certificate.json'
prior_raw = prior_path.read_bytes()
prior = json.loads(prior_raw)['tables'][34]
assert prior['d'] == 35 and prior['rows'] == [list(row) for row in rows]
kap, U, T, B = F(23, 11), F(20000000000), F(24), 9250245
ell, q, w = (F(x, 10**12) for x in
             (693147180559, 1098612288669, 1011600911679))
lam, E = F(10584, 10**14), F(552, 4*2**60-23)
checks = []


def check(name, actual, relation, required):
    a, b = F(actual), F(required)
    passed = {'=': a == b, '<': a < b, '>': a > b,
              '>=': a >= b}[relation]
    checks.append(dict(name=name, actual=a, relation=relation, required=b,
                       difference=a-b, passed=passed))


for key, value in dict(U=U, T=T, ell=ell, u=q, v=w).items():
    check(f'L084 S constant {key}', F(prior['S'][key]), '=', value)
check('positive budget', B, '>', 0)
for i, j, h in rows:
    check(f'row{i} J domain', j, '>=', 2)
    check(f'row{i} H domain', h, '>=', 3)
    if i:
        check(f'row{i} increasing J', j, '>', rows[i-1][1])
check('J1 for residual', rows[1][1], '=', 15)
check('positive cap residual', lam-E, '>', 0)
R = kap/(lam-E)+kap
check('cap', R, '<', U)
check('cap matches L084 independent datum', R, '=', F(prior['S']['cap']))
exp_terms = [T**k/factorial(k) for k in range(41)]
exp_lower = sum(exp_terms, F(0))
check('U below exp24 lower sum', U, '<', exp_lower)
prefix_upper = F(81, 44)-F(3, 11)*F(3, 2)**5
recipient_q = F(12, 11)*F(3, 2)**72+1
check('prefix H floor', min(h for _, _, h in rows[:21]), '=', 5)
check('uniform prefix tail2 offset', prefix_upper, '<', 0)
check('recipient H floor', min(h for _, _, h in rows[1:22]), '=', 72)
check('uniform recipient Q lower', recipient_q, '>', kap*2**20)
Q0 = F(12, 11)*F(3, 2)**5+1
check('failed full-package row0 tail20 datum retained', Q0, '<', kap*2**20)
offsets = []
for i, _, h in rows[:22]:
    floor = min(h, 72)
    Q = F(12, 11)*F(3, 2)**floor+1
    tail2, tail20 = kap-Q/4, kap-Q/2**20
    saved = prior['O']['offsets'][i]
    check(f'row{i} O index', saved['i'], '=', i)
    check(f'row{i} O floor', saved['H_floor'], '=', floor)
    check(f'row{i} O offset', F(saved['offset_upper']), '=', tail2)
    if i <= 20:
        check(f'prefix row{i} negative tail2 offset upper', tail2, '<', 0)
    if i >= 1:
        saved = prior['S']['offsets'][i]
        check(f'recipient{i} S index', saved['i'], '=', i)
        check(f'recipient{i} S floor', saved['H_floor'], '=', floor)
        check(f'recipient{i} S Q', F(saved['Q_lower']), '=', Q)
        check(f'recipient{i} negative tail20 offset upper', tail20, '<', 0)
    offsets.append(dict(i=i, H_floor=floor, Q_lower=Q,
                        tail2_upper=tail2, tail20_upper=tail20))
A = D = base_A = base_D = 0
prefixes, margins = [], []
for i, j, h in rows:
    prefixes.append(dict(i=i, A=A, D=D))
    check(f'incoming{i} A matches L084', A, '=', prior['prefixes'][i]['A'])
    check(f'incoming{i} D matches L084', D, '=', prior['prefixes'][i]['D_tail2'])
    A += 3*j+h
    D += 4*j+h+2
    _, bj, bh = base[i]
    base_A += 3*bj+bh
    base_D += 4*bj+bh+2
    if 1 <= i <= 21:
        next_J = rows[i+1][1]
        C = D+18+4*next_J
        M = C*ell-T-w-A*q
        saved = prior['S']['margins'][i]
        for key, value in dict(j=i, A=A, D=D, margin=M).items():
            check(f'recipient{i} matches L084 {key}', value, '=', F(saved[key]))
        check(f'recipient{i} A shift', A-base_A, '=', -35)
        check(f'recipient{i} D shift', D-base_D, '=', -35)
        check(f'recipient{i} positive A', A, '>', 0)
        check(f'recipient{i} positive log2 coefficient', C, '>', 0)
        check(f'recipient{i} rejection', M, '>', F(47, 2))
        margins.append(dict(j=i, next_input=i+1, A=A, D=D, next_J=next_J,
                            log2_coefficient=C, margin=M,
                            scaled_margin=10**12*M))
assert [m['j'] for m in margins] == list(range(1, 22))
check('total K', A, '=', 397573379)
check('total N', D+18*B, '=', 630138897)
minimum, minimum_j = min((m['margin'], m['j']) for m in margins)
failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    scope='L103 literal d35 endpoint/domain/J full integer simplex, conditional b0=0',
    imports='L055 table; L076 cap proof(6)-(7); audited L084 analytic enclosures',
    sources=[dict(path=str(p.relative_to(ROOT)), sha256=hashlib.sha256(b).hexdigest())
             for p, b in [(source, raw), (prior_path, prior_raw)]],
    rows=rows, B=B,
    constants=dict(kappa=kap, U=U, T=T, ell=ell, log3_upper=q,
                   logv_upper=w, lambda_lower=lam, E=E, R=R),
    uniform_offsets=dict(prefix_H_floor=5, prefix_tail2_upper=prefix_upper,
                         recipient_H_floor=72, recipient_Q_lower=recipient_q,
                         required_Q=kap*2**20, failed_row0_Q=Q0),
    offsets=offsets, prefixes=prefixes, margins=margins,
    exponential_terms=exp_terms, exp24_lower=exp_lower, checks=checks,
    summary=dict(checks=len(checks), recipients=len(margins), minimum_j=minimum_j,
                 minimum_margin=minimum, required_margin=F(47, 2),
                 failures=failures, passed=not failures, parameter_samples=0),
    limitations='Construction evidence only; b0=0 is assumed; no separate critical '
                'audit, assembly, realization, actual-word transfer or universal descent.')
path = HERE / 'd35-earlier-recipients-certificate.json'
path.write_text(json.dumps(result, indent=2, default=str)+'\n')
print(f'Checks: {len(checks)}; failures: {failures}')
print(f'Cap R={R}; required <{U}; exp24 lower sum >{exp_lower.__floor__()}')
print(f'Prefix tail2 offset upper={prefix_upper}; required <0')
print(f'Recipient Q lower={recipient_q}; required >{kap*2**20}')
print(f'Recipients: {len(margins)}/21; minimum M({minimum_j})={minimum}; required >47/2>0')
print(f'Parameter samples: 0; certificate: {path.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
