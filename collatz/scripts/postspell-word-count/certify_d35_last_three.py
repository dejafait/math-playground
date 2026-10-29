#!/usr/bin/env python3
"""Exact finite data for L102's approved d35 three-tail test.

L076's cyclic cap proof and L084's audited analytic bounds are imports.
The full-domain implication is proved in L102, not by parameter sampling.
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
base = [tuple(map(int, x)) for x in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', raw.decode(), re.M)]
assert [x[0] for x in base] == list(range(25))
rows = [(i, j, 5 if i == 0 else 32670656 if i == 24 else h)
        for i, j, h in base]
prior_path = HERE / 'h-transfer-family-certificate.json'
prior_raw = prior_path.read_bytes()
prior = json.loads(prior_raw)['tables'][34]
assert prior['d'] == 35 and prior['rows'] == [list(row) for row in rows]
kap, U, T, B = F(23, 11), F(20000000000), F(24), 9250245
ell, log3_upper, logv_upper = (F(x, 10**12) for x in
    (693147180559, 1098612288669, 1011600911679))
lm, E = F(10584, 10**14), F(552, 4*2**60-23)
checks = []


def check(name, actual, relation, required):
    a, b = F(actual), F(required)
    passed = {'=': a == b, '<': a < b, '>': a > b,
              '>=': a >= b}[relation]
    checks.append(dict(name=name, actual=a, relation=relation,
                       required=b, difference=a-b, passed=passed))


for key, value in dict(U=U, T=T, ell=ell, u=log3_upper,
                       v=logv_upper).items():
    check(f'L084 S constant {key}', F(prior['S'][key]), '=', value)
check('budget positive', B, '>', 0)
for i, j, h in rows:
    check(f'row{i} J domain', j, '>=', 2)
    check(f'row{i} H domain', h, '>=', 3)
    if i:
        check(f'row{i} increasing J', j, '>', rows[i-1][1])
K = sum(3*j+h for _, j, h in rows)
N = sum(4*j+h+2 for _, j, h in rows)+18*B
check('total K', K, '=', 397573379)
check('total N', N, '=', 630138897)
check('J1 for residual', rows[1][1], '=', 15)
check('positive residual', lm-E, '>', 0)
R = kap/(lm-E)+kap
check('cap', R, '<', U)
check('cap equals independent L084 datum', R, '=', F(prior['S']['cap']))
exp_terms = [T**k/factorial(k) for k in range(41)]
exp_lower = sum(exp_terms, F(0))
check('U below exp24 lower sum', U, '<', exp_lower)
prefix_upper = F(81, 44)-F(3, 11)*F(3, 2)**5
check('prefix minimum H', min(h for _, _, h in rows[:22]), '=', 5)
check('prefix uniform tail2 offset', prefix_upper, '<', 0)
offsets = []
for i, _, h in rows[:23]:
    floor = min(h, 72)
    q = F(12, 11)*F(3, 2)**floor+1
    o = kap-q/4
    check(f'row{i} L084 O index', prior['O']['offsets'][i]['i'], '=', i)
    check(f'row{i} L084 O floor', prior['O']['offsets'][i]['H_floor'], '=', floor)
    check(f'row{i} L084 O offset', F(prior['O']['offsets'][i]['offset_upper']), '=', o)
    if i < 22:
        check(f'prefix row{i} tail2 offset', o, '<', 0)
    offsets.append(dict(i=i, H_floor=floor, Q_lower=q, tail2_upper=o))
check('recipient H floor', rows[22][2], '>=', 72)
recipient_q = F(12, 11)*F(3, 2)**72+1
check('recipient Q lower', recipient_q, '>', kap*2**20)
check('recipient S index', prior['S']['offsets'][22]['i'], '=', 22)
check('recipient Q matches L084', recipient_q, '=', F(prior['S']['offsets'][22]['Q_lower']))
check('recipient offset', kap-recipient_q/2**20, '<', 0)
q0 = F(12, 11)*F(3, 2)**5+1
check('failed full-package row0 tail20 test retained', q0, '<', kap*2**20)
A = sum(3*j+h for _, j, h in rows[:23])
D = sum(4*j+h+2 for _, j, h in rows[:23])
Jnext = rows[23][1]
C = D+18+4*Jnext
M = C*ell-T-logv_upper-A*log3_upper
for key, val in dict(j=22, A=A, D=D, margin=M).items():
    check(f'row22 matches L084 S {key}', val, '=', F(prior['S']['margins'][22][key]))
check('prefix A shift', A-sum(3*j+h for _, j, h in base[:23]), '=', -35)
check('prefix D shift', D-sum(4*j+h+2 for _, j, h in base[:23]), '=', -35)
check('A positive', A, '>', 0)
check('log2 coefficient positive', C, '>', 0)
check('row23 rejection margin', M, '>', F(25))
check('scaled row23 margin', 10**12*M, '=', 25450077965484)
failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    scope='Literal d35 u>=1,v>=0,u+v<=B three-tail endpoint/domain/J subsystem',
    imports='L055 table; L076 cap proof(6)-(7); audited L084 analytic enclosures',
    sources=[dict(path=str(p.relative_to(ROOT)), sha256=hashlib.sha256(b).hexdigest())
             for p, b in [(source, raw), (prior_path, prior_raw)]],
    rows=rows, B=B,
    constants=dict(kappa=kap, U=U, T=T, ell=ell, log3_upper=log3_upper,
                   logv_upper=logv_upper, lambda_lower=lm, E=E, R=R),
    exponential_terms=exp_terms, exp24_lower=exp_lower,
    offsets=offsets,
    recipient=dict(i=22, H_floor=72, Q_lower=recipient_q,
                   required_Q=kap*2**20, tail20_upper=kap-recipient_q/2**20),
    row23=dict(A=A, D=D, J=Jnext, log2_coefficient=C,
               margin=M, scaled_margin=10**12*M),
    checks=checks,
    summary=dict(checks=len(checks), failures=failures, passed=not failures,
                 prefix_tail2_upper=prefix_upper, required_offset='strictly below 0',
                 rejection_margin=M, required_margin='strictly above 25 > 0',
                 uniform_domain='integers u>=1,v>=0,u+v<=9250245',
                 parameter_samples=0),
    limitations='Construction evidence, not independent audit; no other support/order '
                'exhaustion, realization, actual-word transfer or universal descent.')
path = HERE / 'd35-last-three-certificate.json'
path.write_text(json.dumps(result, default=str, indent=2)+'\n')
print(f'Checks: {len(checks)}; failures: {failures}')
print(f'Cap R={R}; required <{U}; exp24 partial sum >{exp_lower.__floor__()}')
print(f'Prefix tail2 offset upper={prefix_upper}; required <0')
print(f'Recipient Q lower={recipient_q}; required >{kap*2**20}')
print(f'Row23 J rejection margin={M}; required >25>0; parameter samples=0')
print(f'Certificate: {path.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
