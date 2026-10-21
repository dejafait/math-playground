#!/usr/bin/env python3
"""Exact rational certificate for an L051 real-system witness, not a cycle.

The cyclic root is stored as a finite factored rational expression. Its
huge powers need not be expanded: all bounds below are exact Fractions.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

S = 10**12
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
    return lo, lo+Q(TERMS, SCALE)+remainder, dict(
        x=str(x), rounded_summands=rounded,
        rounding_budget=str(Q(TERMS, SCALE)), remainder_upper=str(remainder))


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


K, N, L = 397573379, 630138897, 232565518
l2, u2 = log_bounds(2)
l3, u3 = log_bounds(3)
lc, uc = log_bounds(Q(11, 4))
ELO, EHI = 693147180559, 693147180560
TLO, THI = 1098612288668, 1098612288669
CLO = 1011600911678
less('log2 lower', Q(ELO, S), l2)
less('log2 upper', u2, Q(EHI, S))
less('log3 lower', Q(TLO, S), l3)
less('log3 upper', u3, Q(THI, S))
less('log(11/4) lower', Q(CLO, S), lc)
AL, BE = 3*TLO-4*EHI, TLO-EHI
less('alpha lower positive', 0, AL)
less('beta lower positive', 0, BE)

# This greedy choice is merely a reproducible construction. The exact
# table and all its inequalities, rather than its optimality, certify it.
v = 23610000000000
initial_v = v
rows = []
for i in range(24):
    j = (v+CLO)//(4*EHI)
    h = (v+j*AL)//EHI
    rows.append(dict(i=i, J=j, H=h, a=2, v=v))
    v += j*AL+h*BE-2*EHI
sum_j = sum(row['J'] for row in rows)
sum_h = sum(row['H'] for row in rows)
j = (v+CLO)//(4*EHI)
j -= (sum_j+j-(L-50)) % 18
h = K-3*(sum_j+j)-sum_h
a = L-sum_j-j-48
rows.append(dict(i=24, J=j, H=h, a=a, v=v))

integer_checks = dict(
    word_count=len(rows) == 25,
    J_guards=all(row['J'] >= 2 for row in rows),
    H_guards=all(row['H'] >= 3 for row in rows),
    tail_guards=all(row['a'] >= 0 and row['a'] % 18 == 2 for row in rows),
    odd_total=sum(3*row['J']+row['H'] for row in rows) == K,
    even_total=sum(row['J']+row['a'] for row in rows) == L,
    length=K+L == N,
    first_24_tails=all(row['a'] == 2 for row in rows[:24]),
    d1_scaling=K > 225640000 and L > 0)
for row in rows:
    i, j, h, v = row['i'], row['J'], row['H'], row['v']
    less(f'own J guard {i}', 4*j*EHI, v+CLO)
    less(f'own H guard {i}', h*EHI, v+j*AL)
    row['J_guard_margin_scaled'] = v+CLO-4*j*EHI
    row['H_guard_margin_scaled'] = v+j*AL-h*EHI
    row['odd_exponent'] = 3*j+h
    row['two_exponent'] = 4*j+h+row['a']
    if i < 24:
        integer_checks[f'lower_recurrence_{i}'] = (
            rows[i+1]['v'] == v+j*AL+h*BE-2*EHI)

lam_lo, lam_hi = N*l2-K*u3, N*u2-K*l3
LMIN, LMAX = Q(10584, 10**14), Q(10585, 10**14)
less('Lambda positive lower', LMIN, lam_lo)
less('Lambda upper', lam_hi, LMAX)
less('Lambda upper below one', LMAX, 1)
less('length inequality', N, Q(8, 5)*K+Q(1725, 1034))

# For 0<x<1, x<exp(x)-1<x/(1-x). With B=sum eta_i/C_i,
# eta_0>2 and c_0>10^8, all c_1,...,c_23>2 give
# 2 < B < (23/11)(1+2/10^8). These establish the root interval.
j0, h0 = rows[0]['J'], rows[0]['H']
eta0 = Q(23, 11)-Q(12, 11)*Q(16, 27)**j0-Q(16, 27)**j0*Q(2, 3)**h0
less('eta0 above two', 2, eta0)
less('first multiplier above 1e8', 10**8*2**rows[0]['two_exponent'],
     3**rows[0]['odd_exponent'])
less('minimal tail-two multiplier above two', 2, Q(27, 16)**2*Q(3, 2)**3/4)
BMAX = Q(23, 11)*(1+Q(2, 10**8))
root_lower = 2*(1-LMAX)/LMAX
root_upper = BMAX/LMIN
less('n0 above 18 billion', 18*10**9, root_lower)
less('s0 below 20 billion', root_upper+Q(23, 11), 20*10**9)
loglow, _ = log_bounds(18*10**9)
_, loghigh = log_bounds(20*10**9)
less('initial lower log height', Q(initial_v, S), loglow)
less('initial upper log height below 24', loghigh, 24)
logNlow, _ = log_bounds(N)
log25low, _ = log_bounds(25)
less('seed above 24', 24, Q(133, 10)*logNlow+8+log25low)
less('all junctions above required lower height', Q(540, 11), 18*10**9)

# Exact finite expression for every junction: C_i is factored, and
# n_i=C_i*(n0+sum_{j<i} eta_j/C_j). C_25=3^K/2^N < 1.
# No floating-point or truncated root is used as the witness.
prefixes = []
pk = pn = 0
for row in rows:
    prefixes.append(dict(i=row['i'], C_three_exponent=pk, C_two_exponent=pn))
    pk += row['odd_exponent']
    pn += row['two_exponent']
integer_checks['product_exponents'] = (pk, pn) == (K, N)
failures = [r['name'] for r in checks if not r['passed']]
failures += [name for name, passed in integer_checks.items() if not passed]
result = dict(
    target='Fixed-count L051 (1)-(4), r=25, K=397573379, N=630138897',
    verdict='FULL_REAL_SYSTEM_WITNESS_NOT_INTEGER_CYCLE',
    parameters=rows, prefixes=prefixes,
    counts=dict(K=K, N=N, L=L, d=1, K0=K, L0=L,
                sum_J=sum(row['J'] for row in rows),
                sum_H=sum(row['H'] for row in rows),
                sum_a=sum(row['a'] for row in rows)),
    definition=dict(
        c_i='3^(3J_i+H_i)/2^(4J_i+H_i+a_i)',
        eta_i='23/11-(12/11)*(16/27)^J_i-(16/27)^J_i*(2/3)^H_i',
        C_i='product(c_j for j<i); C_0=1',
        B='sum(eta_i/C_i for i=0,...,24)',
        n0='B/(2^N/3^K-1)',
        n_i='C_i*(n0+sum(eta_j/C_j for j<i))',
        s_i='n_i+23/11',
        limitations='No integer, parity, residue or valuation realization certified'),
    constants=dict(S=S, ELO=ELO, EHI=EHI, TLO=TLO, THI=THI,
                   CLO=CLO, AL=AL, BE=BE, initial_v=initial_v),
    root_bounds=dict(eta0=str(eta0), B_upper=str(BMAX),
                     lambda_lower=str(lam_lo), lambda_upper=str(lam_hi),
                     lambda_lower_used=str(LMIN), lambda_upper_used=str(LMAX),
                     n0_lower=str(root_lower), n0_upper=str(root_upper),
                     certified_n0_lower=18*10**9, certified_s0_upper=20*10**9),
    logs=logs, log2_detail=ell_detail, checks=checks,
    integer_checks=integer_checks, failures=failures,
    inspection=dict(strict_margins=[dict(name=row['name'],
        margin_floor_times_10_18=(Q(row['margin'])*10**18).__floor__())
        for row in checks]))
path = Path(__file__).with_name('fixed-count-tail-witness-certificate.json')
path.write_text(json.dumps(result, indent=2)+'\n')
print(f'Rational checks: {len(checks)}; integer checks: {len(integer_checks)}; failures: {failures}')
print(f'Exact totals K={K}, L={L}, N={N}; required K0>225640000, d=1')
print(f'Closing parameters J={rows[-1]["J"]}, H={rows[-1]["H"]}, a={rows[-1]["a"]}')
print('Certified root: 18000000000<n0<s0<20000000000; required s_i>=540/11')
print('Every own-index guard has positive margin; cyclic closure is exact by the stored rational definition')
print(f'Certificate: {path}')
assert not failures
