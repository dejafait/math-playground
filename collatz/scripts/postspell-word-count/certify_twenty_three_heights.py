#!/usr/bin/env python3
"""Exact rational support for L052, only at twenty-three occurrences.

Log enclosures use the integrated geometric remainder and downward
dyadic rounding already documented in L051. No floating point is used.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

BITS, TERMS = 192, 96
SCALE = 2**BITS
checks, logs = [], {}


def base_log(t):
    x = (t - 1) / (t + 1)
    assert 0 <= x <= Q(1, 3)
    summands = [SCALE * 2*x**(2*j+1)/(2*j+1) for j in range(TERMS)]
    rounded = [s.numerator // s.denominator for s in summands]
    lo = Q(sum(rounded), SCALE)
    error = Q(9, 4*(2*TERMS+1)*3**(2*TERMS+1))
    hi = lo + Q(TERMS, SCALE) + error
    return lo, hi, dict(x=str(x), rounded_summands=rounded,
                       rounding_budget=str(Q(TERMS, SCALE)),
                       remainder_upper=str(error))


ell_lo, ell_hi, ell_detail = base_log(Q(2))


def log_bounds(t):
    t = Q(t)
    assert t >= 1
    k, v = 0, t
    while v >= 2:
        k, v = k+1, v/2
    lo, hi, detail = base_log(v)
    lo, hi = lo+k*ell_lo, hi+k*ell_hi
    logs[str(t)] = dict(argument=str(t), binary_exponent=k,
                        reduced_argument=str(v), lower=str(lo),
                        upper=str(hi), detail=detail)
    return lo, hi


def less(name, actual, required):
    actual, required = Q(actual), Q(required)
    checks.append(dict(name=name, actual=str(actual), relation='<',
                       required=str(required), margin=str(required-actual),
                       passed=actual < required))


l2, u2 = log_bounds(2)
l3, u3 = log_bounds(3)
lc, uc = log_bounds(Q(11, 4))
less('log2 lower', Q(6931, 10000), l2)
less('log3 upper', u3, Q(10987, 10000))
less('c upper', uc, Q(41, 40))
less('delta upper', Q(10987, 6931), Q(793, 500))
delta_upper, ell_lower, c_upper = Q(793, 500), Q(6931, 10000), Q(41, 40)
rho, beta, count = Q(189, 100), Q(31, 100), Q(14, 5)
less('transfer coefficient', 3*delta_upper**2/4, rho)
less('transfer additive', delta_upper*(3*delta_upper-4)*c_upper/4, beta)
less('shifted transfer', beta+1, rho)
less('odd-count coefficient', 3*(delta_upper+1)/(4*ell_lower), count)
less('odd-count additive', (3*delta_upper-1)*c_upper/(4*ell_lower), Q(7, 5))

R = sum((rho**j for j in range(23)), Q(0))
assert R == Q(189**23-100**23, 89*100**22)
less('geometric sum', R, 2600000)
less('log23 via exponential lower bound', 23, Q(27, 10)**4)
less('length additive constant', Q(1587, 1034), 2)
A = Q(8, 5)*count*2600000*Q(133, 10)
B = Q(8, 5)*count*2600000*13+2
M = 3600000000
assert A == 154918400 and B == 151424002
lm, um = log_bounds(M)
less('logM upper', um, Q(111, 5))
less('whole-ray derivative guard', A, M)
less('whole-ray value guard', A*Q(111, 5)+B, M)

p, q = 9809721694, 6189245291
eps_lo, eps_hi = q*l3-p*u2, q*u3-p*l2
less('epsilon positive', 0, eps_lo)
less('epsilon compact upper', eps_hi, Q(958, 10**13))
less('compact half-log comparison', 2*M*Q(958, 10**13), Q(6931, 10000))
less('same-pair half-log guard', 2*M*eps_hi, l2)
less('log2 exceeds 2/3', Q(2, 3), l2)
D = Q(1587*q+23, 11)
less('minimum-height exponential comparison', D, Q(27, 10)**28)
K_upper = count*2600000*29
less('odd-count contradiction', K_upper, 225640000)

result = dict(
    target='L051 (1)-(4) at r=23',
    precision=dict(bits=BITS, terms=TERMS, log2_detail=ell_detail),
    logs=logs,
    operands=dict(rho=str(rho), beta=str(beta), count=str(count),
                  R=str(R), R_upper='2600000', A=str(A), B=str(B), M=M,
                  p=p, q=q, epsilon_lower=str(eps_lo), epsilon_upper=str(eps_hi),
                  D=str(D), K_upper=str(K_upper), K_required='225640000'),
    checks=checks,
    failures=[c['name'] for c in checks if not c['passed']],
)
path = Path(__file__).with_name('twenty-three-height-certificate.json')
path.write_text(json.dumps(result, indent=2)+'\n')
print(f"Checks: {len(checks)}; failures: {result['failures']}")
print(f"N ceiling: {M}; monotonicity margin: {M-A*Q(111,5)-B}")
print(f"K upper: {K_upper}; required lower: >225640000; gap: {225640000-K_upper}")
print(f"Certificate: {path}")
if result['failures']:
    raise SystemExit(1)
