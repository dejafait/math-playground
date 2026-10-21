#!/usr/bin/env python3
"""Exact rational certificate for L053; only the approved r=24 system."""
from fractions import Fraction as Q
from pathlib import Path
import json

BITS, TERMS = 192, 96
SCALE = 2**BITS
logs, checks = {}, []


def base_log(t):
    x = (t-1)/(t+1)
    assert 0 <= x <= Q(1, 3)
    terms = [SCALE*2*x**(2*j+1)/(2*j+1) for j in range(TERMS)]
    rounded = [v.numerator//v.denominator for v in terms]
    lo = Q(sum(rounded), SCALE)
    error = Q(9, 4*(2*TERMS+1)*3**(2*TERMS+1))
    hi = lo+Q(TERMS, SCALE)+error
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
    logs[str(t)] = dict(binary_exponent=k, reduced_argument=str(v),
                        lower=str(lo), upper=str(hi), detail=detail)
    return lo, hi


def less(name, actual, required):
    actual, required = Q(actual), Q(required)
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       relation='<', margin=str(required-actual),
                       passed=actual < required))


def floor_q(t):
    return t.numerator//t.denominator


l2, u2 = log_bounds(2)
l3, u3 = log_bounds(3)
lc, uc = log_bounds(Q(11, 4))
rho, count = Q(189, 100), Q(14, 5)
R23 = sum((rho**i for i in range(23)), Q(0))
R24 = sum((rho**i for i in range(24)), Q(0))
less('R23', R23, 2570000)
less('R24', R24, 4850000)
less('log24 exponential comparison', 24, Q(27, 10)**4)
less('length remainder', Q(1656, 1034), 2)
A = Q(8, 5)*count*4850000*Q(133, 10)
B = Q(8, 5)*count*4850000*13+2
M = 6900000000
lm, um = log_bounds(M)
less('logM', um, Q(227, 10))
less('whole-ray derivative', A, M)
less('whole-ray value', A*Q(227, 10)+B, M)
p, q, inverse = 9809721694, 6189245291, 397573379
eps_lo, eps_hi = q*l3-p*u2, q*u3-p*l2
less('epsilon positive', 0, eps_lo)
less('epsilon upper', eps_hi, Q(958, 10**13))
less('log2 lower', Q(6931, 10000), l2)
less('quarter-log separation', Q(1, 4),
     Q(6931, 10000)-Q(2*M, 3)*Q(958, 10**13))
D0 = Q(2208*q+23, 11)
less('minimum height below 28', D0, Q(163, 60)**28)
K_cap = count*4850000*29
less('K coarse upper', K_cap, 394000000)
less('minimum height above 15', count*4850000*16, 225640000)
two_small_cap = count*31*2570001
less('two small heights impossible', two_small_cap, 225640000)
tail_upper = Q(23*23, 11)/(Q(27, 10)**30-Q(23, 11))
less('other 23 reciprocal terms', tail_upper, Q(1, 10**11))
less('minimum real height exceeds million', 10**6, Q(27, 10)**15)
less('endpoint positive shift error', Q(92, 11*10**6), Q(1, 100000))

assert 630138897*q-inverse*p == 1
residues = [dict(z=z, K=(inverse*z) % q) for z in range(1, 63)]
survivors = [row for row in residues if 225640000 < row['K'] < 394000000]
assert survivors == [dict(z=32, K=343857546)]
height_caps = {}
for z, height in [(32, Q(21)), (63, Q(98, 5))]:
    # The same weaker K<394000000 bound works for both cases.
    lam = (z*Q(6931, 10000)-394000000*Q(958, 10**13))/q
    denom = lam-Q(1, 10**11)
    less(f'z={z} mass denominator positive', 0, denom)
    D = Q(23, 11)+Q(23, 11)/denom
    ld, ud = log_bounds(D)
    less(f'z={z} minimum log-height', ud, height)
    height_caps[str(z)] = dict(lambda_lower=str(lam),
                               mass_denominator=str(denom), s0_upper=str(D),
                               h0_upper=str(height))
less('z=32 count contradiction', count*4850000*22, 343857546)

S = 10**12
E, T, C = 693147180559, 1098612288669, 1011600911679
less('compact log2 lower for floors', Q(E, S), l2)
less('compact log3 upper for floors', u3, Q(T, S))
less('compact c upper for floors', uc, Q(C, S))
alpha_num, beta_num = 3*T-4*E, T-E
alpha_hi, beta_hi = Q(alpha_num, S), Q(beta_num, S)
less('positive alpha lower', 0, 3*l3-4*u2)
less('positive beta lower', 0, l3-u2)
U_num = 19600000000000
greedy = []
total = 0
for i in range(24):
    U = Q(U_num, S)
    j_arg = Q(U_num+C, 4*E)
    J = (U_num+C)//(4*E)
    h_arg = Q(U_num+J*alpha_num, E)
    H = (U_num+J*alpha_num)//E
    next_num = U_num+J*alpha_num+H*beta_num-2*E+10**7
    next_U = Q(next_num, S)
    assert J >= 2 and H >= 3
    assert J <= j_arg < J+1 and H <= h_arg < H+1
    total += 3*J+H
    greedy.append(dict(i=i, U_numerator=U_num, U=str(U), J_argument=str(j_arg), J=J,
                       H_argument=str(h_arg), H=H, odd_count_upper=3*J+H,
                       next_U=str(next_U), next_numerator=next_num))
    U_num = next_num
less('z>=63 total odd-count contradiction', total, 225640000)


def decimal_interval(t):
    t = Q(t)
    unit = 10**12
    lower = floor_q(t*unit)
    return [str(Q(lower, unit)), str(Q(lower+1, unit))]


inspection = dict(
    checks=[dict(name=row['name'], actual=decimal_interval(row['actual']),
                 required=decimal_interval(row['required']),
                 margin_lower=str(Q(floor_q(Q(row['margin'])*10**12), 10**12)),
                 passed=row['passed']) for row in checks],
    greedy=[dict(i=row['i'], U_numerator=row['U_numerator'], J=row['J'], H=row['H'],
                 J_argument=decimal_interval(row['J_argument']),
                 H_argument=decimal_interval(row['H_argument']),
                 odd_count_upper=row['odd_count_upper']) for row in greedy])
result = dict(target='L051 (1)-(4) at r=24',
    precision=dict(bits=BITS, terms=TERMS, log2_detail=ell_detail), logs=logs,
    operands=dict(R23=str(R23), R24=str(R24), A=str(A), B=str(B), M=M,
                  p=p, q=q, epsilon_lower=str(eps_lo), epsilon_upper=str(eps_hi),
                  D0=str(D0), K_cap=str(K_cap), two_small_cap=str(two_small_cap),
                  tail_upper=str(tail_upper), inverse=inverse,
                  modular_identity=630138897*q-inverse*p,
                  floor_scale=S, E=E, T=T, C=C,
                  alpha_upper=str(alpha_hi), beta_upper=str(beta_hi)),
    residues=residues, survivors=survivors, height_caps=height_caps,
    greedy=greedy, greedy_total=total, checks=checks, inspection=inspection,
    failures=[row['name'] for row in checks if not row['passed']])
path = Path(__file__).with_name('twenty-four-height-certificate.json')
path.write_text(json.dumps(result, indent=2)+'\n')
print(f"Checks: {len(checks)}; failures: {result['failures']}")
print(f"Whole-ray ceiling N<{M}; value margin: {M-A*Q(227,10)-B}")
print(f"K<{K_cap}; required K>225640000; modular survivors z<63: {survivors}")
print(f"z=32: K<298760000 but K=343857546")
print(f"z>=63: K<={total}; required K>225640000; margin: {225640000-total}")
print(f"Certificate: {path}")
if result['failures']:
    raise SystemExit(1)
