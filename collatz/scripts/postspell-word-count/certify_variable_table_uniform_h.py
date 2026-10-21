#!/usr/bin/env python3
"""L083 benchmark data, with complete exact rational evidence on disk.

The universal implication is a written proof. This certificate checks its
changed/original table applications without constructing giant cyclic roots.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
raw = SOURCE.read_bytes()
original = [tuple(map(int, row)) for row in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', raw.decode(), re.M)]
assert len(original) == 25 and [row[0] for row in original] == list(range(25))
checks = []


def check(name, actual, relation, required):
    a, b = Q(actual), Q(required)
    passed = {'<': a < b, '<=': a <= b, '=': a == b,
              '>': a > b, '>=': a >= b}[relation]
    checks.append(dict(name=name, actual=a, relation=relation, required=b,
                       difference=a-b, passed=passed))


def log_bounds(x):
    z = (x-1)/(x+1)
    assert 0 < z <= Q(1, 2)
    terms = [2*z**(2*k+1)/(2*k+1) for k in range(100)]
    lower = sum(terms, Q(0))
    remainder = 2*z**201/(201*(1-z*z))
    return dict(argument=x, z=z, terms=terms, remainder_upper=remainder,
                lower=lower, upper=lower+remainder)


logs = {str(x): log_bounds(Q(x)) for x in (2, 3)}
lm, lp = Q(10584, 10**14), Q(10585, 10**14)
ell, u = Q(693147180559, 10**12), Q(1098612288669, 10**12)
kap = Q(23, 11)
check('log2 lower grid', ell, '<', logs['2']['lower'])
check('log3 upper grid', logs['3']['upper'], '<', u)
exp_terms = [Q(24)**k/factorial(k) for k in range(41)]
exp_lower = sum(exp_terms, Q(0))
check('exp24 partial sum exceeds U', 20*10**9, '<', exp_lower)
prefix_lowers = [Q(1)] + [Q(10**8 * 2**(i-1)) for i in range(1, 25)]
reciprocal_sum = sum((1/x for x in prefix_lowers), Q(0))
qcap = kap*(1+Q(2, 10**8))
wcap = kap/min(prefix_lowers)
normalized_cap = qcap/lm+qcap+wcap
check('full incoming reciprocal cap', kap*reciprocal_sum, '<', qcap)
check('normalized cap below U', normalized_cap, '<', 20*10**9)
tail2_floor = Q(27, 16)**2 * Q(3, 2)**3 / 4
tail20_floor = Q(27, 16)**8 * Q(3, 2)**39 / 2**20
check('tail2 multiplier floor', tail2_floor, '>', 2)
check('tail20 multiplier floor', tail20_floor, '>', 2)
tables = {}
for name in ('changed', 'original'):
    rows = [dict(i=i, J=j, H=(39 if i == 0 else 32670622 if i == 24 else h)
                 if name == 'changed' else h) for i, j, h in original]
    K = sum(3*x['J']+x['H'] for x in rows)
    N = sum(4*x['J']+x['H'] for x in rows)+2*25+18*9250245
    check(name+' K', K, '=', 397573379)
    check(name+' N', N, '=', 630138897)
    lambda_low = N*logs['2']['lower']-K*logs['3']['upper']
    lambda_high = N*logs['2']['upper']-K*logs['3']['lower']
    check(name+' Lambda lower', lm, '<', lambda_low)
    check(name+' Lambda upper', lambda_high, '<', lp)
    check(name+' positive lower', lm, '>', 0)
    check(name+' upper below one', lp, '<', 1)
    x0 = rows[0]
    c0 = Q(3**(3*x0['J']+x0['H']), 2**(4*x0['J']+x0['H']+2))
    check(name+' row0 c0', c0, '>', 10**8)
    for x in rows[1:23]:
        check(f"{name} row{x['i']} J tail2 floor", x['J'], '>=', 2)
        check(f"{name} row{x['i']} H tail2 floor", x['H'], '>=', 3)
    check(name+' row23 J tail20 floor', rows[23]['J'], '>=', 8)
    check(name+' row23 H tail20 floor', rows[23]['H'], '>=', 39)
    prefixes = []
    A = D0 = Dm = 0
    for x, lower in zip(rows, prefix_lowers):
        i, j, h = x['i'], x['J'], x['H']
        positive, negative = A+3*j, D0+4*j+h
        F = 24+positive*u-negative*ell
        prefixes.append(dict(i=i, A=A, D_at_0=D0, D_at_m=Dm,
                             L=lower, H_log3_coefficient=positive,
                             H_negative_log2_coefficient=negative,
                             uniform_H_margin_strict_upper=F))
        if name == 'original':
            check(f'original row{i} sufficient rejection test fails', F, '>', 0)
        A += 3*j+h
        D0 += 4*j+h+(2 if i < 24 else 166504412)
        Dm += 4*j+h+(2 if i < 23 else 20 if i == 23 else 166504394)
    check(name+' complete closing odd exponent', A, '=', K)
    check(name+' closing exponent at t0', D0, '=', N)
    check(name+' closing exponent at t1', Dm, '=', N)
    row18 = prefixes[18]
    if name == 'changed':
        check('changed row18 uniform rejection', row18['uniform_H_margin_strict_upper'], '<', 0)
        check('changed row18 bound matches C082a', row18['uniform_H_margin_strict_upper'],
              '=', -Q(457745289, 50000000000))
    tables[name] = dict(rows=rows, counts=dict(K=K, N=N),
                        Lambda_interval=[lambda_low, lambda_high],
                        row0_multiplier=c0, incoming_prefixes=prefixes,
                        row18=row18,
                        rejected_rows=[x['i'] for x in prefixes
                                       if x['uniform_H_margin_strict_upper'] <= 0])

failures = [x['name'] for x in checks if not x['passed']]
result = dict(target='L083 uniform incoming-prefix/H tests, changed and original benchmarks',
    source=dict(path=str(SOURCE.relative_to(ROOT)), sha256=hashlib.sha256(raw).hexdigest()),
    parameters=dict(r=25, B=9250245, tau=2, m=1, survivors=[0, 1]),
    certificate_constants=dict(lambda_lower=lm, lambda_upper=lp, ell=ell, u=u,
        T=24, U=20*10**9, incoming_L=prefix_lowers, Q=qcap, W=wcap),
    full_reciprocal_sum=reciprocal_sum, normalized_cap=normalized_cap,
    multiplier_floor=dict(tail2=tail2_floor, tail20=tail20_floor),
    logs=logs, exp24_terms=exp_terms, exp24_partial_sum=exp_lower,
    tables=tables, checks=checks, failures=failures,
    summary=dict(checks=len(checks), failures=failures,
        changed_row18_upper=tables['changed']['row18']['uniform_H_margin_strict_upper'],
        required_rejection_upper=0, original_rejected_rows=tables['original']['rejected_rows']),
    limitations='General uniformity is proved in L083; O/S/C tests are imported from L079 for the changed table. No new feasibility, integrality, or universal descent claim.')
path = HERE / 'variable-table-uniform-h-certificate.json'
path.write_text(json.dumps(result, indent=2, default=str)+'\n')
print('Changed table: every survivor t=0,1 has row18 H margin strictly below '
      f"{result['summary']['changed_row18_upper']}; required margin >0.")
print(f'Normalized cap {normalized_cap} < U=20000000000 < exp(24).')
print(f"Original table: rejection rows {tables['original']['rejected_rows']}; "
      f"row18 upper {tables['original']['row18']['uniform_H_margin_strict_upper']} >0.")
print(f'Checks: {len(checks)}; failures: {failures}. Certificate: {path.relative_to(ROOT)}')
assert not failures
