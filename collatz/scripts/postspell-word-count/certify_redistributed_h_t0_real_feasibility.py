#!/usr/bin/env python3
"""One approved t=0 full-system test: certify one necessary H-guard failure.

Exact rational arithmetic; no expanded giant root or wider allocation search.
Full operands, logarithm terms/remainders and comparison certificates go to disk.
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
original = [tuple(map(int, x)) for x in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', raw.decode(), re.M)]
assert len(original) == 25 and [x[0] for x in original] == list(range(25))
rows = [dict(i=i, J=j, H=39 if i == 0 else 32670622 if i == 24 else h,
             a=2 if i < 24 else 166504412) for i, j, h in original]
checks = []


def check(name, actual, relation, required):
    a, b = Q(actual), Q(required)
    passed = {'<': a < b, '<=': a <= b, '=': a == b,
              '>': a > b, '>=': a >= b}[relation]
    checks.append(dict(name=name, actual=a, relation=relation,
                       required=b, difference=a-b, passed=passed))


def log_bounds(argument):
    z = (argument-1)/(argument+1)
    assert 0 < z <= Q(1, 2)
    m = 100
    terms = [2*z**(2*k+1)/(2*k+1) for k in range(m)]
    lo = sum(terms, Q(0))
    remainder = 2*z**(2*m+1)/((2*m+1)*(1-z*z))
    return dict(argument=argument, z=z, terms=terms,
                remainder_upper=remainder, lower=lo, upper=lo+remainder)


logs = {str(x): log_bounds(Q(x)) for x in (2, 3)}
l2, u2 = logs['2']['lower'], logs['2']['upper']
l3, u3 = logs['3']['lower'], logs['3']['upper']
K = sum(3*x['J']+x['H'] for x in rows)
L = sum(x['J']+x['a'] for x in rows)
N = K+L
for name, actual, required in [
    ('sum J', sum(x['J'] for x in rows), 66061058),
    ('sum H', sum(x['H'] for x in rows), 199390205),
    ('sum tails', sum(x['a'] for x in rows), 166504460),
    ('K', K, 397573379), ('L', L, 232565518), ('N', N, 630138897)]:
    check(name, actual, '=', required)
for x in rows:
    check(f"row {x['i']} J domain", x['J'], '>=', 2)
    check(f"row {x['i']} H domain", x['H'], '>=', 3)
    check(f"row {x['i']} tail domain", x['a'], '>=', 2)
    check(f"row {x['i']} tail congruence", x['a'] % 18, '=', 2)
check('explicit d=1 odd count threshold', K, '>', 225640000)
check('explicit d=1 even count positive', L, '>', 0)
check('aggregate length inequality', N, '<', Q(8, 5)*K+Q(1725, 1034))
lm, lp = Q(10584, 10**14), Q(10585, 10**14)
lambda_lo, lambda_hi = N*l2-K*u3, N*u2-K*l3
check('fresh Lambda lower', lm, '<', lambda_lo)
check('fresh Lambda upper', lambda_hi, '<', lp)
check('positive Lambda lower', lm, '>', 0)
check('Lambda upper below one', lp, '<', 1)
kap = Q(23, 11)
eta_subtraction_upper = Q(12, 11)*Q(16, 27)**2+Q(16, 27)**2*Q(2, 3)**3
check('every eta positive from parameter floors', eta_subtraction_upper, '<', kap)
# Every subtraction is positive, giving eta_i<kap. First 24 tails are 2.
c0 = Q(3**63, 2**73)
check('fresh changed row0 c0', c0, '>', 10**8)
c_floor = Q(27, 16)**2*Q(3, 2)**3/4
check('other incoming c_i floor', c_floor, '>', 2)
prefixes = []
a_sum = d_sum = 0
for x in rows:
    i, j, h, tail = x['i'], x['J'], x['H'], x['a']
    lower = Q(1) if i == 0 else Q(10**8*2**(i-1))
    prefixes.append(dict(i=i, three_exponent=a_sum, two_exponent=d_sum,
                         product_lower=lower))
    if i < 24:
        check(f'incoming row {i} tail exactly 2', tail, '=', 2)
    a_sum += 3*j+h
    d_sum += 4*j+h+tail
check('closing product odd exponent', a_sum, '=', K)
check('closing product denominator exponent', d_sum, '=', N)
R_plus = kap*(1+Q(2, 10**8))
check('full inverse prefix bound',
      kap*sum(1*x['product_lower']**-1 for x in prefixes), '<', R_plus)
normalized_upper = R_plus/lm+R_plus+kap
check('fresh all-input normalized shifted root cap', normalized_upper, '<', 20*10**9)
exp24_terms = [Q(24)**k/factorial(k) for k in range(41)]
exp24_lower = sum(exp24_terms, Q(0))
check('exp24 strict partial-sum bound', 20*10**9, '<', exp24_lower)
S = 10**12
EL, EU, TL, TU = 693147180559, 693147180560, 1098612288668, 1098612288669
for name, actual, rel, required in [
    ('log2 grid lower', Q(EL, S), '<', l2),
    ('log2 grid upper', u2, '<', Q(EU, S)),
    ('log3 grid lower', Q(TL, S), '<', l3),
    ('log3 grid upper', u3, '<', Q(TU, S))]:
    check(name, actual, rel, required)
# h_i<24+log C_i, and log C_i=A_i log3-D_i log2.
i = 18
x, p = rows[i], prefixes[i]
positive_coefficient = p['three_exponent']+3*x['J']
negative_coefficient = p['two_exponent']+4*x['J']+x['H']
margin_upper = 24+Q(positive_coefficient*TU-negative_coefficient*EL, S)
check('own-input row18 H margin upper strictly negative', margin_upper, '<', 0)
failures = [x['name'] for x in checks if not x['passed']]
result = dict(
    target='Redistributed-H t=0 affine cyclic root: L051 (1)-(4)',
    verdict='INFEASIBLE_H_GUARD_18' if not failures else 'NOT_CERTIFIED',
    source=dict(path=str(SOURCE.relative_to(ROOT)), sha256=hashlib.sha256(raw).hexdigest()),
    parameters=rows, counts=dict(K=K, L=L, N=N, d=1, K0=K, L0=L),
    root=dict(c_i='3^(3J_i+H_i)/2^(4J_i+H_i+a_i)',
        eta_i='23/11-(12/11)*(16/27)^J_i-(16/27)^J_i*(2/3)^H_i',
        C_i='product_(j<i)c_j, C_0=1', R='sum_(i=0..24)eta_i/C_i',
        n0='R/(2^N/3^K-1)',
        n_i='C_i*(n0+sum_(j<i)eta_j/C_j)', s_i='n_i+23/11',
        closure='C_25=3^K/2^N; n_25=C_25*(n0+R)=n0',
        lambda_lower=lm, lambda_upper=lp, R_upper=R_plus,
        normalized_shifted_upper=normalized_upper,
        normalized_height_upper='h_i-log C_i < 24 for every 0<=i<=24'),
    prefixes=prefixes, logs=logs, lambda_interval=[lambda_lo, lambda_hi],
    exp24_terms=exp24_terms,
    failed_necessary_guard=dict(i=i, J=x['J'], H=x['H'], own_input=i,
        prefix_three=p['three_exponent'], prefix_two=p['two_exponent'],
        log3_coefficient=positive_coefficient, log2_negative_coefficient=negative_coefficient,
        actual_margin='h_18+J_18*log(27/16)-H_18*log2',
        margin_strict_upper=margin_upper, required_relation='actual margin > 0'),
    checks=checks, failures=failures,
    summary=dict(certification_checks=len(checks), failures=failures,
        guard_index=i, margin_strict_upper=margin_upper,
        required_margin_lower=0, all_other_guards_tested=False),
    limitations='One failed necessary constraint suffices; no verdict for t=1, other allocations/tables, or universal descent.')
path = HERE / 'redistributed-h-t0-real-feasibility-certificate.json'
path.write_text(json.dumps(result, indent=2, default=lambda x: str(x))+'\n')
print(f'Verdict: {result["verdict"]}; own-input H guard {i} requires margin >0')
print(f'Actual margin < {margin_upper}; required >0')
print(f'Changed prefix C18=3^{p["three_exponent"]}/2^{p["two_exponent"]}')
print(f'Normalized shifted root < {normalized_upper} < 20000000000 < exp(24)')
print(f'Checks: {len(checks)}; certification failures: {failures}; other guards not decided')
print(f'Certificate: {path.relative_to(ROOT)}')
assert not failures
