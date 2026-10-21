#!/usr/bin/env python3
"""L091 finite arithmetic. No sampling of the allocation simplex.

The quantified proof imports L090's cap and L084's analytic enclosures.
This checks all required data, retaining failed full-support operands.
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
prior_path = HERE / 'h-transfer-family-certificate.json'
prior_raw = prior_path.read_bytes()
prior_tables = json.loads(prior_raw)['tables']
benchmark_path = HERE / 'd5-remaining-early-recipients-certificate.json'
benchmark_raw = benchmark_path.read_bytes()
benchmark = json.loads(benchmark_raw)
benchmark_margins = {m['j']: F(m['margin']) for m in benchmark['margins']}
assert sorted(benchmark_margins) == list(range(1, 23))
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


prefix_offset_upper = F(81, 44)-F(3, 11)*F(3, 2)**7
recipient_Q_lower = F(12, 11)*F(3, 2)**72+1
check('uniform prefix tail2 offset', prefix_offset_upper, '<', 0)
check('uniform recipient tail20 Q', recipient_Q_lower, '>', kappa*2**20)
check('positive margin increment u-ell', u-ell, '>', 0)
exp_terms = [T**k/factorial(k) for k in range(41)]
check('U below exp24 positive lower sum', U, '<', sum(exp_terms, F(0)))
E, lam = F(552, 4*2**60-23), F(10584, 10**14)
check('L090 positive residual', lam-E, '>', 0)
R = kappa/(lam-E)+kappa
check('L090 root cap below U', R, '<', U)
tables = []
for d in range(6, 34):
    rows = [(i, j, h-d if i == 0 else h+d if i == 24 else h)
            for i, j, h in original]
    prior = prior_tables[d-1]
    check(f'd{d} prior index', prior['d'], '=', d)
    assert prior['rows'] == [list(row) for row in rows]
    check(f'd{d} minimum prefix H', min(h for _, _, h in rows[:22]),
          '=', 40-d)
    check(f'd{d} prefix H floor', 40-d, '>', 6)
    check(f'd{d} minimum recipient H', min(h for _, _, h in rows[1:23]),
          '=', 72)
    Q0 = F(12, 11)*F(3, 2)**(40-d)+1
    check(f'd{d} failed full row0 tail20 datum retained', Q0, '<', kappa*2**20)
    A = D = original_A = original_D = 0
    prefixes, margins = [], []
    for i, j, h in rows:
        prefixes.append(dict(i=i, A=A, D=D))
        check(f'd{d} incoming{i} A matches L084', A, '=', prior['prefixes'][i]['A'])
        check(f'd{d} incoming{i} D matches L084', D, '=', prior['prefixes'][i]['D_tail2'])
        A += 3*j+h
        D += 4*j+h+2
        _, oj, oh = original[i]
        original_A += 3*oj+oh
        original_D += 4*oj+oh+2
        if 1 <= i <= 22:
            next_J = rows[i+1][1]
            C = D+18+4*next_J
            M = C*ell-T-v-A*u
            stored = prior['S']['margins'][i]
            check(f'd{d} recipient{i} positive A', A, '>', 0)
            check(f'd{d} recipient{i} positive log2 coefficient', C, '>', 0)
            check(f'd{d} recipient{i} A matches L084', A, '=', stored['A'])
            check(f'd{d} recipient{i} D matches L084', D, '=', stored['D'])
            check(f'd{d} recipient{i} M matches L084', M, '=', F(stored['margin']))
            check(f'd{d} recipient{i} A shift', A-original_A, '=', -d)
            check(f'd{d} recipient{i} D shift', D-original_D, '=', -d)
            check(f'd{d} recipient{i} d5 margin shift', M,
                  '=', benchmark_margins[i]+(d-5)*(u-ell))
            check(f'd{d} recipient{i} rejection', M, '>', F(1175, 100))
            margins.append(dict(j=i, next_input=i+1, A=A, D=D,
                                next_J=next_J, log2_coefficient=C, margin=M))
    assert [m['j'] for m in margins] == list(range(1, 23))
    check(f'd{d} total K', A, '=', 397573379)
    check(f'd{d} total N', D+18*9250245, '=', 630138897)
    tables.append(dict(d=d, rows=rows, prefixes=prefixes, margins=margins,
                       failed_row0_Q=Q0))

minimum, minimum_d, minimum_j = min(
    (m['margin'], table['d'], m['j']) for table in tables for m in table['margins'])
failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    scope='Literal d=6..33 endpoint/domain/J subsystem, full allocation simplex',
    imports='L090: b0=0 and s0<U; L084 (2): analytic ell,u,v; DLMF 4.2.19',
    source_sha256=hashlib.sha256(raw).hexdigest(),
    prior_certificate_sha256=hashlib.sha256(prior_raw).hexdigest(),
    d5_certificate_sha256=hashlib.sha256(benchmark_raw).hexdigest(),
    constants=dict(kappa=kappa, U=U, T=T, ell=ell, u=u, v=v,
                   E=E, lambda_lower=lam, R=R),
    offsets=dict(prefix_H_floor=7, prefix_tail2_upper=prefix_offset_upper,
                 recipient_H_floor=72, recipient_Q_lower=recipient_Q_lower,
                 required_Q=kappa*2**20),
    exponential_terms=exp_terms, tables=tables, checks=checks,
    summary=dict(checks=len(checks), tables=len(tables), recipients=28*22,
                 minimum_margin=minimum, minimum_d=minimum_d, minimum_j=minimum_j,
                 required_margin=F(1175, 100), failures=failures, passed=not failures),
    limitations='No cyclic-order, last-pair/survivor, H/seed, integrality, realization or actual-word conclusion.')
path = HERE / 'uniform-remaining-early-recipients-certificate.json'
path.write_text(json.dumps(result, indent=2, default=str)+'\n')
print(f'Checks: {len(checks)}; failures: {failures}')
print(f'Prefix offset upper={prefix_offset_upper}; required <0')
print(f'Recipient Q lower={recipient_Q_lower}; required >{kappa*2**20}')
print(f'Tables: {len(tables)}/28; recipients: 616/616; '
      f'minimum M({minimum_d},{minimum_j})={minimum}; required >1175/100>0')
print(f'Certificate: {path.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
