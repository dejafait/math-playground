#!/usr/bin/env python3
"""Exact certificate for the stopped r=25 comparison, not feasibility.

Logarithm enclosures use the integrated geometric remainder in L051.
All authoritative arithmetic is integer/Fraction arithmetic.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

BITS, TERMS = 192, 96
SCALE = 2**BITS
logs, checks = {}, []


def base_log(t):
    x = (t-1)/(t+1)
    assert 0 <= x <= Q(1, 3)
    rounded = []
    for j in range(TERMS):
        term = SCALE*2*x**(2*j+1)/(2*j+1)
        rounded.append(term.numerator//term.denominator)
    lo = Q(sum(rounded), SCALE)
    remainder = Q(9, 4*(2*TERMS+1)*3**(2*TERMS+1))
    hi = lo+Q(TERMS, SCALE)+remainder
    return lo, hi, dict(x=str(x), rounded_summands=rounded,
                        rounding_budget=str(Q(TERMS, SCALE)),
                        remainder_upper=str(remainder))


ell_lo, ell_hi, ell_detail = base_log(Q(2))


def log_bounds(t):
    t = Q(t)
    assert t >= 1
    k, v = 0, t
    while v >= 2:
        k, v = k+1, v/2
    lo, hi, detail = base_log(v)
    lo, hi = lo+k*ell_lo, hi+k*ell_hi
    logs[str(t)] = dict(binary_exponent=k, reduced_argument=str(v),
                        lower=str(lo), upper=str(hi), detail=detail)
    return lo, hi


def less(name, actual, required):
    actual, required = Q(actual), Q(required)
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       relation='<', margin=str(required-actual),
                       passed=actual < required))


l2, u2 = log_bounds(2)
l3, u3 = log_bounds(3)
lc, uc = log_bounds(Q(11, 4))
rho, count = Q(189, 100), Q(14, 5)
R24 = sum((rho**i for i in range(24)), Q(0))
R25 = sum((rho**i for i in range(25)), Q(0))
less('R24 upper', R24, 4850000)
less('R25 upper', R25, 9170000)
less('log25 below four', 25, Q(27, 10)**4)
less('r25 length remainder', Q(1725, 1034), 2)
A = Q(8, 5)*count*9170000*Q(133, 10)
B = Q(8, 5)*count*9170000*13+2
M = 14000000000
_, logM_hi = log_bounds(M)
less('logM upper', logM_hi, Q(117, 5))
less('whole-ray derivative', A, M)
less('whole-ray value', A*Q(117, 5)+B, M)

p, q = 9809721694, 6189245291
K, N = 397573379, 630138897
L = N-K
eps_lo, eps_hi = q*l3-p*u2, q*u3-p*l2
lam_lo, lam_hi = N*l2-K*u3, N*u2-K*l3
less('epsilon positive', 0, eps_lo)
less('epsilon upper', eps_hi, Q(958, 10**13))
less('coarse separation expression is negative', u2-Q(2*M, 3)*eps_lo, 0)
assert N*q-K*p == 1
less('branch primitive odd threshold', 225640000, K)
less('branch length inequality', N, Q(8, 5)*K+Q(1725, 1034))
less('branch below ceiling', N, M)
less('branch Lambda lower', Q(10584, 10**14), lam_lo)
less('branch Lambda upper', lam_hi, Q(10585, 10**14))
J_values, H_values, a_values = [2]*25, [3]*25, [2]*25
H_values[-1] += K-225
a_values[-1] += L-100
assert all(j >= 2 for j in J_values)
assert all(h >= 3 for h in H_values)
assert all(a >= 0 and a % 18 == 2 for a in a_values)
assert sum(3*j+h for j, h in zip(J_values, H_values)) == K
assert sum(j+a for j, a in zip(J_values, a_values)) == L

# Use rounded, certified rational lower bound for the branch's Lambda.
lambda_lower = Q(10584, 10**14)
D0 = Q(23, 11)+Q(575, 11)/lambda_lower
_, logD0_hi = log_bounds(D0)
less('branch h0 below 27', logD0_hi, 27)
less('branch h0 above 14', count*9170000*15, K)
two_small_cap = count*29*4850001
less('second height at most 28 impossible for branch', two_small_cap, K)
tail_upper = Q(552, 11)/(Q(163, 60)**28-Q(23, 11))
mass_denominator = lambda_lower-tail_upper
less('refined mass denominator positive', 0, mass_denominator)
D = Q(23, 11)+Q(23, 11)/mass_denominator
logD_lo, logD_hi = log_bounds(D)
height_cap = Q(603, 25)
less('refined cap lower diagnostic', Q(2411, 100), logD_lo)
less('refined cap upper', logD_hi, height_cap)
less('all heights exceed log million', 10**6, Q(27, 10)**14)
less('endpoint shift error', Q(92, 11*10**6), Q(1, 100000))

S = 10**12
E, T, C = 693147180559, 1098612288669, 1011600911679
less('floor log2 lower', Q(E, S), l2)
less('floor log3 upper', u3, Q(T, S))
less('floor log(11/4) upper', uc, Q(C, S))
alpha, beta = 3*T-4*E, T-E
less('alpha positive', 0, 3*l3-4*u2)
less('beta positive', 0, l3-u2)
v = int(height_cap*S)
assert Q(v, S) == height_cap
rows, total = [], 0
for i in range(25):
    j_num, j_den = v+C, 4*E
    J = j_num//j_den
    h_num, h_den = v+J*alpha, E
    H = h_num//h_den
    assert J >= 2 and H >= 3
    assert J*j_den <= j_num < (J+1)*j_den
    assert H*h_den <= h_num < (H+1)*h_den
    odd = 3*J+H
    next_v = v+J*alpha+H*beta-2*E+10**7
    rows.append(dict(i=i, v=v, J_numerator=j_num, J_denominator=j_den, J=J,
                     H_numerator=h_num, H_denominator=h_den, H=H,
                     odd_count_upper=odd, next_v=next_v))
    total += odd
    v = next_v
less('envelope misses branch K', K, total)
less('envelope misses primitive threshold', 225640000, total)
assert total == 534432492


def compact(t):
    t = Q(t)
    n = (t*10**12).numerator//(t*10**12).denominator
    return [str(Q(n, 10**12)), str(Q(n+1, 10**12))]


failures = [row['name'] for row in checks if not row['passed']]
result = dict(
    target='L051 (1)-(4) at r=25; endpoint-product/integer-envelope comparison',
    verdict='STOPPED_COMPARISON_NOT_SIMULTANEOUS_FEASIBILITY',
    logs=logs, log2_detail=ell_detail,
    operands=dict(R24=str(R24), R25=str(R25), A=str(A), B=str(B), M=M,
                  p=p, q=q, epsilon_lower=str(eps_lo), epsilon_upper=str(eps_hi),
                  lambda_lower_exact=str(lam_lo), lambda_upper_exact=str(lam_hi),
                  lambda_lower_used=str(lambda_lower), D0=str(D0),
                  two_small_cap=str(two_small_cap), tail_upper=str(tail_upper),
                  mass_denominator=str(mass_denominator), D=str(D),
                  height_cap=str(height_cap), S=S, E=E, T=T, C=C),
    branch=dict(K=K, N=N, L=L, d=1, K0=K, L0=L, z=N*q-K*p,
                aggregate_parameters_only=dict(J=J_values, H=H_values, a=a_values),
                not_claimed=['own-index realization', 'seed realization',
                             'exact endpoints', 'simultaneous feasibility', 'cycle']),
    floors=rows, total=total, excess_over_branch=total-K,
    checks=checks, failures=failures,
    inspection=dict(checks=[dict(name=row['name'], actual=compact(row['actual']),
                                 required=compact(row['required']), passed=row['passed'])
                            for row in checks],
                    floors=[dict(i=row['i'], J=row['J'], H=row['H'],
                                 odd_count_upper=row['odd_count_upper']) for row in rows]))
path = Path(__file__).with_name('twenty-five-envelope-stop-certificate.json')
path.write_text(json.dumps(result, indent=2)+'\n')
print(f"Checks: {len(checks)}; failures: {failures}")
print(f"Whole-ray ceiling N<{M}; value margin: {M-A*Q(117,5)-B}")
print(f"Branch: z=1, K={K}, N={N}; required primitive K>225640000")
print(f"Conditional branch height: 14<h0<{height_cap}; second junctions >28")
print(f"Envelope K<={total}; exceeds branch by {total-K}; contradiction fails")
print(f"No simultaneous witness or r=25 exclusion. Certificate: {path}")
if failures:
    raise SystemExit(1)
