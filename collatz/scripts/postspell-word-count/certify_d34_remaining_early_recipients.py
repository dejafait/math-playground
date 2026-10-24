#!/usr/bin/env python3
"""L099 exact data test; the full-simplex implication is proved in L099.

Imports L098's audited cap and L084's analytic enclosures. No root sampling.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
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
rows = [(i, j, h-34 if i == 0 else h+34 if i == 24 else h)
        for i, j, h in base]
prior_path = HERE / 'h-transfer-family-certificate.json'
prior_raw = prior_path.read_bytes()
prior = json.loads(prior_raw)['tables'][33]
assert prior['d'] == 34 and prior['rows'] == [list(row) for row in rows]
kappa, U, T = F(23, 11), F(20000000000), F(24)
ell, u, v = (F(x, 10**12) for x in
             (693147180559, 1098612288669, 1011600911679))
checks = []


def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    passed = {'<': actual < required, '>': actual > required,
              '=': actual == required}[relation]
    checks.append(dict(name=name, actual=actual, relation=relation,
                       required=required, difference=actual-required,
                       passed=passed))


for key, val in dict(U=U, T=T, ell=ell, u=u, v=v).items():
    check(f'L084 S constant {key}', F(prior['S'][key]), '=', val)
prefix_upper = F(81, 44)-F(3, 11)*F(3, 2)**6
Q_lower = F(12, 11)*F(3, 2)**72+1
check('prefix H floor', min(h for _, _, h in rows[:22]), '=', 6)
check('prefix tail2 upper', prefix_upper, '<', 0)
check('recipient H floor', min(h for _, _, h in rows[1:23]), '=', 72)
check('recipient Q lower', Q_lower, '>', kappa*2**20)
Q0 = F(12, 11)*F(3, 2)**6+1
check('failed row0 tail20 datum preserved', Q0, '<', kappa*2**20)
lam, E = F(10584, 10**14), F(552, 4*2**60-23)
R = kappa/(lam-E)+kappa
check('positive cap residual', lam-E, '>', 0)
check('guard-conditioned cap', R, '<', U)
check('cap matches independent L084 data', R, '=', F(prior['S']['cap']))
exp_terms = [T**k/factorial(k) for k in range(41)]
exp_lower = sum(exp_terms, F(0))
check('U below exp24 lower sum', U, '<', exp_lower)
offsets = []
for i, _, h in rows[:23]:
    floor = min(h, 72)
    Q = F(12, 11)*F(3, 2)**floor+1
    tail2 = kappa-Q/4
    check(f'row{i} O index', prior['O']['offsets'][i]['i'], '=', i)
    check(f'row{i} O floor', prior['O']['offsets'][i]['H_floor'], '=', floor)
    check(f'row{i} O offset', tail2, '=', F(prior['O']['offsets'][i]['offset_upper']))
    if i <= 21:
        check(f'prefix row{i} negative tail2 upper', tail2, '<', 0)
    if i >= 1:
        stored = prior['S']['offsets'][i]
        check(f'recipient{i} S index', stored['i'], '=', i)
        check(f'recipient{i} S floor', stored['H_floor'], '=', floor)
        check(f'recipient{i} S Q', Q, '=', F(stored['Q_lower']))
        check(f'recipient{i} negative tail20 upper', kappa-Q/2**20, '<', 0)
    offsets.append(dict(i=i, H_floor=floor, Q_lower=Q, tail2_upper=tail2,
                        tail20_upper=kappa-Q/2**20))
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
    if 1 <= i <= 22:
        next_J = rows[i+1][1]
        C = D+18+4*next_J
        M = C*ell-T-v-A*u
        saved = prior['S']['margins'][i]
        for key, val in dict(j=i, A=A, D=D, margin=M).items():
            check(f'recipient{i} matches L084 {key}', val, '=', F(saved[key]))
        check(f'recipient{i} A shift', A-base_A, '=', -34)
        check(f'recipient{i} D shift', D-base_D, '=', -34)
        check(f'recipient{i} positive A', A, '>', 0)
        check(f'recipient{i} positive log2 coefficient', C, '>', 0)
        check(f'recipient{i} rejection', M, '>', F(231, 10))
        margins.append(dict(j=i, next_input=i+1, A=A, D=D, next_J=next_J,
                            log2_coefficient=C, margin=M,
                            scaled_margin=10**12*M))
assert [m['j'] for m in margins] == list(range(1, 23))
check('total K', A, '=', 397573379)
check('total N', D+18*9250245, '=', 630138897)
minimum, minimum_j = min((m['margin'], m['j']) for m in margins)
failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    scope='L099 literal d34 endpoint/domain/J full integer allocation simplex',
    imports='L098 audited b0=0 and cap; L084 analytic enclosures; DLMF 4.2.19',
    sources=[dict(path=str(p.relative_to(ROOT)), sha256=hashlib.sha256(b).hexdigest())
             for p, b in [(source, raw), (prior_path, prior_raw)]],
    rows=rows, B=9250245,
    constants=dict(kappa=kappa, U=U, T=T, ell=ell, u=u, v=v, R=R),
    uniform_offsets=dict(prefix_H_floor=6, prefix_tail2_upper=prefix_upper,
                         recipient_H_floor=72, recipient_Q_lower=Q_lower,
                         required_Q=kappa*2**20, failed_row0_Q=Q0),
    offsets=offsets, prefixes=prefixes, margins=margins,
    exponential_terms=exp_terms, exp24_lower=exp_lower, checks=checks,
    summary=dict(checks=len(checks), recipients=len(margins), minimum_j=minimum_j,
                 minimum_margin=minimum, required_margin=F(231, 10),
                 failures=failures, passed=not failures),
    limitations='Construction evidence only; no independent audit, assembly, '
                'actual-word transfer or universal-descent result.')
path = HERE / 'd34-remaining-early-recipients-certificate.json'
path.write_text(json.dumps(result, indent=2, default=str)+'\n')
print(f'Checks: {len(checks)}; failures: {failures}')
print(f'Prefix offset upper={prefix_upper}; required <0')
print(f'Recipient Q lower={Q_lower}; required >{kappa*2**20}')
print(f'Recipients: {len(margins)}/22; minimum M({minimum_j})={minimum}; required >231/10>0')
print(f'Certificate: {path.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
