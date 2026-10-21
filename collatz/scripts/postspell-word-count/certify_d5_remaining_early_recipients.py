#!/usr/bin/env python3
"""Finite d5 first-recipient arithmetic; quantified proof is in L086.

No allocations are sampled. Analytic enclosures and the root cap are
imported from audited L084/L085, rather than recomputed here.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
source = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
raw = source.read_bytes()
original = [tuple(map(int, x)) for x in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', raw.decode(), re.M)]
assert [i for i, _, _ in original] == list(range(25))
rows = [(i, j, h-5 if i == 0 else h+5 if i == 24 else h)
        for i, j, h in original]
prior_path = HERE / 'h-transfer-family-certificate.json'
prior_raw = prior_path.read_bytes()
prior = json.loads(prior_raw)['tables'][4]
kappa, U, T = F(23, 11), F(20_000_000_000), F(24)
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


check('prior table d', prior['d'], '=', 5)
check('K', sum(3*j+h for _, j, h in rows), '=', 397573379)
check('N', sum(4*j+h for _, j, h in rows)+50+18*9250245,
      '=', 630138897)
for (i, j, h), stored in zip(rows, prior['rows']):
    assert [i, j, h] == stored
check('minimum prefix H', min(h for _, _, h in rows[:22]), '=', 35)
check('minimum recipient H', min(h for _, _, h in rows[1:23]), '=', 72)
# These are uniform upper/lower operands, avoiding enormous powers.
prefix_offset_upper = F(81, 44)-F(3, 11)*F(3, 2)**35
recipient_Q_lower = F(12, 11)*F(3, 2)**72+1
check('all prefix tail2 offsets negative', prefix_offset_upper, '<', 0)
check('all recipient tail20 offsets negative', recipient_Q_lower,
      '>', kappa*2**20)
Q0 = F(12, 11)*F(3, 2)**35+1
check('failed row0 tail20 datum preserved', Q0, '<', kappa*2**20)
exp_terms = [T**k/factorial(k) for k in range(41)]
check('U below exp24 lower sum', U, '<', sum(exp_terms, F(0)))
E = F(552, 4*2**60-23)
lam = F(10584, 10**14)
check('L085 cap residual', lam-E, '>', 0)
R = kappa/(lam-E)+kappa
check('L085 cap below U', R, '<', U)

prefixes, margins = [], []
A = D = original_A = original_D = 0
for i, j, h in rows:
    prefixes.append(dict(i=i, A=A, D=D))
    check(f'incoming{i} A matches L084', A, '=', prior['prefixes'][i]['A'])
    check(f'incoming{i} D matches L084', D, '=', prior['prefixes'][i]['D_tail2'])
    A += 3*j+h
    D += 4*j+h+2
    _, original_j, original_h = original[i]
    original_A += 3*original_j+original_h
    original_D += 4*original_j+original_h+2
    if 1 <= i <= 22:
        next_J = rows[i+1][1]
        M = (D+18+4*next_J)*ell-T-v-A*u
        prior_margin = prior['S']['margins'][i]
        check(f'recipient{i} A', A, '=', prior_margin['A'])
        check(f'recipient{i} D', D, '=', prior_margin['D'])
        check(f'recipient{i} margin matches L084', M, '=', F(prior_margin['margin']))
        check(f'recipient{i} strict rejection', M, '>', F(1134, 100))
        check(f'recipient{i} changed A shift', A-original_A, '=', -5)
        check(f'recipient{i} changed D shift', D-original_D, '=', -5)
        margins.append(dict(j=i, next_input=i+1, A=A, D=D,
                            next_J=next_J, margin=M))

check('complete A', A, '=', 397573379)
check('complete D plus budget', D+18*9250245, '=', 630138897)
assert [m['j'] for m in margins] == list(range(1, 23))
minimum = min(m['margin'] for m in margins)
minimum_row = next(m['j'] for m in margins if m['margin'] == minimum)
failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    scope='L085 literal d=5 endpoint/domain/J subsystem; first recipient 1..22',
    imports='L085: b0=0 and s0<U; L084 (2): analytic ell,u,v enclosures; '
            'positive-real exp series DLMF 4.2.19 as assessed',
    source_sha256=hashlib.sha256(raw).hexdigest(),
    prior_certificate_sha256=hashlib.sha256(prior_raw).hexdigest(),
    rows=rows, constants=dict(U=U, T=T, ell=ell, u=u, v=v, E=E,
                             lambda_lower=lam, R=R),
    offsets=dict(prefix_H_floor=35, prefix_tail2_upper=prefix_offset_upper,
                 recipient_H_floor=72, recipient_Q_lower=recipient_Q_lower,
                 required_Q=kappa*2**20, failed_row0_Q=Q0),
    exponential_terms=exp_terms, prefixes=prefixes, margins=margins,
    checks=checks, summary=dict(checks=len(checks), recipients=len(margins),
        minimum_margin=minimum, minimum_row=minimum_row,
        required_margin=F(1134, 100), failures=failures, passed=not failures),
    limitations='No arbitrary order, last-pair verdict, H/seed, feasibility, '
                'integer/actual-word exclusion or universal descent.')
path = HERE / 'd5-remaining-early-recipients-certificate.json'
path.write_text(json.dumps(result, indent=2, default=str)+'\n')
print(f'Checks: {len(checks)}; failures: {failures}')
print(f'Prefix tail2 offset upper={prefix_offset_upper}; required <0')
print(f'Recipient Q lower={recipient_Q_lower}; required >{kappa*2**20}')
print(f'Recipients: {len(margins)}/22; minimum M_{minimum_row}={minimum}; '
      f'required >1134/100 (in particular >0)')
print(f'Certificate: {path.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
