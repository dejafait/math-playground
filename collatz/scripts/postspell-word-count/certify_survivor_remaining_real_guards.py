#!/usr/bin/env python3
"""Certify only the approved L064 j=23 H guards, seed and aggregate premises.

L064 supplies exact closure, minimum/domain and normalized height bounds.
No expanded enormous root, new allocation or integer realization is tested.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parent.parent
table_text = (NOTEBOOK / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
table = [tuple(map(int, r)) for r in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', table_text, re.M)]
assert len(table) == 25 and [r[0] for r in table] == list(range(25))
S, BITS, TERMS = 10**12, 192, 96
EL, EU = 693147180559, 693147180560
TL, TU = 1098612288668, 1098612288669
AL, AU = 3*TL-4*EU, 3*TU-4*EL
BL, BU = TL-EU, TU-EL
K, L, N = 397573379, 232565518, 630138897
LMIN, LMAX = Q(10584, 10**14), Q(10585, 10**14)
checks, logs = [], {}


def less(name, actual, required):
    actual, required = Q(actual), Q(required)
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       relation='<', margin=str(required-actual), passed=actual < required))


def base_log(t):
    x = (t-1)/(t+1)
    assert 0 <= x <= Q(1, 3)
    scale = 2**BITS
    rounded = []
    for m in range(TERMS):
        term = scale*2*x**(2*m+1)/(2*m+1)
        rounded.append(term.numerator // term.denominator)
    lower = Q(sum(rounded), scale)
    remainder = Q(9, 4*(2*TERMS+1)*3**(2*TERMS+1))
    return lower, lower+Q(TERMS, scale)+remainder, dict(
        argument=str(t), x=str(x), rounded_summands=rounded,
        rounding_budget=str(Q(TERMS, scale)), remainder_upper=str(remainder))


ell_lo, ell_hi, ell_detail = base_log(Q(2))


def log_bounds(t):
    t = Q(t)
    assert t >= 1
    k, u = 0, t
    while u >= 2:
        k, u = k+1, u/2
    lower, upper, detail = base_log(u)
    lower, upper = lower+k*ell_lo, upper+k*ell_hi
    logs[str(t)] = dict(binary_exponent=k, reduced_argument=str(u),
                        lower=str(lower), upper=str(upper), detail=detail)
    return lower, upper


l2, u2 = log_bounds(2)
l3, u3 = log_bounds(3)
less('log2 grid lower', Q(EL, S), l2)
less('log2 grid upper', u2, Q(EU, S))
less('log3 grid lower', Q(TL, S), l3)
less('log3 grid upper', u3, Q(TU, S))
less('positive alpha grid lower', 0, AL)
less('positive beta grid lower', 0, BL)
less('Lambda lower', LMIN, N*l2-K*u3)
less('Lambda upper', N*u2-K*l3, LMAX)
less('Lambda upper below one', LMAX, 1)
less('aggregate length inequality', N, Q(8, 5)*K+Q(1725, 1034))

# Reuse L064's audited root and normalized bounds with these exact tails.
BMAX = Q(9031479, 4296875)
root_lower = 2*(1-LMAX)/LMAX
normalized_upper = BMAX/LMIN+BMAX+Q(23, 11)
less('L064 root lower exceeds 18 billion', 18*10**9, root_lower)
less('L064 normalized shifted upper below 20 billion', normalized_upper, 20*10**9)
less('domain from root lower', Q(540, 11), 18*10**9)
loglow, _ = log_bounds(18*10**9)
_, loghigh = log_bounds(20*10**9)
logNlow, logNhigh = log_bounds(N)
log25low, log25high = log_bounds(25)
less('height lower exceeds 23.61', Q(2361, 100), loglow)
less('initial height upper below 24', loghigh, 24)
seed_lower = Q(133, 10)*logNlow+8+log25low
seed_upper = Q(133, 10)*logNhigh+8+log25high
less('seed upper cap strictly exceeds 24', 24, seed_lower)
less('seed positivity from L064 height lower', 0, Q(2361, 100))

rows = [dict(i=i, J=j, H=h, a=20 if i == 23 else (166504394 if i == 24 else 2))
        for i, j, h in table]
integer_checks = dict(
    exactly_approved_literal_tuple=[r['i'] for r in rows] == list(range(25)),
    moved_tail_only_at_23=all(r['a'] == (20 if r['i'] == 23 else
                            (166504394 if r['i'] == 24 else 2)) for r in rows),
    parameter_domain=all(r['J'] >= 2 and r['H'] >= 3 and r['a'] >= 2 for r in rows),
    tail_congruences=all(r['a'] % 18 == 2 for r in rows),
    sum_J=sum(r['J'] for r in rows) == 66061058,
    sum_H=sum(r['H'] for r in rows) == 199390205,
    sum_a=sum(r['a'] for r in rows) == 166504460,
    K_total=sum(3*r['J']+r['H'] for r in rows) == K,
    L_total=sum(r['J']+r['a'] for r in rows) == L,
    N_total=sum(4*r['J']+r['H']+r['a'] for r in rows) == N,
    K_plus_L=K+L == N,
    explicit_scaling_d1=(K > 225640000 and L > 0))

v, w, pk, pn = 2361*S//100, 24*S, 0, 0
guards, prefixes = [], []
for r in rows:
    i, j, h, a = r['i'], r['J'], r['H'], r['a']
    prefixes.append(dict(i=i, three_exponent=pk, two_exponent=pn))
    low = v+j*AL-h*EU
    high = w+j*AU-h*EL
    verdict = 'PASS_STRICT' if low > 0 else 'FAIL_STRICT' if high < 0 else 'UNRESOLVED'
    guards.append(dict(i=i, J=j, H=h, own_input=i,
        log_s_lower_scaled=v, log_s_upper_scaled=w,
        J_alpha_lower_scaled=j*AL, H_log2_upper_scaled=h*EU,
        margin_lower_scaled=low, margin_upper_scaled=high, verdict=verdict))
    less(f'own-input strict H guard {i}', h*EU, v+j*AL)
    integer_checks[f'prefix_lower_identity_{i}'] = v == 2361*S//100+pk*TL-pn*EU
    integer_checks[f'prefix_upper_identity_{i}'] = w == 24*S+pk*TU-pn*EL
    pk, pn = pk+3*j+h, pn+4*j+h+a
    if i < 24:
        v, w = v+j*AL+h*BL-a*EU, w+j*AU+h*BU-a*EL
integer_checks['closing_exponents'] = (pk, pn) == (K, N)
failures = [c['name'] for c in checks if not c['passed']]
failures += [name for name, passed in integer_checks.items() if not passed]
unresolved = [g['i'] for g in guards if g['verdict'] == 'UNRESOLVED']
weakest = min(guards, key=lambda g: g['margin_lower_scaled'])
summary = dict(H_guards_pass=sum(g['verdict'] == 'PASS_STRICT' for g in guards),
    required_H_guards=25, weakest_H_index=weakest['i'],
    weakest_H_margin_lower=str(Q(weakest['margin_lower_scaled'], S)),
    seed_height_lower='23.61', seed_height_upper='24',
    seed_cap_lower=str(seed_lower), seed_cap_lower_floor=seed_lower.__floor__(),
    seed_margin_lower=str(seed_lower-24),
    rational_checks=len(checks), integer_checks=len(integer_checks),
    failures=failures, unresolved_H_indices=unresolved)
result = dict(target="L064 j=23 survivor: all H guards and L051 (2) seed",
    verdict='ALL_REMAINING_REAL_GUARDS_PASS' if not failures and not unresolved else 'NOT_CERTIFIED',
    inputs=['L064 exact tuple, minimum/domain, height bounds and J verdict',
            'L055 literal table and logarithm method', 'L051 (1)-(4)'],
    counts=dict(K=K, L=L, N=N, d=1, K0=K, L0=L),
    parameters=rows, prefixes=prefixes, closing_exponents=dict(three=pk, two=pn),
    exact_definition=dict(c_i='3^(3J_i+H_i)/2^(4J_i+H_i+a_i)',
        eta_i='23/11-(12/11)*(16/27)^J_i-(16/27)^J_i*(2/3)^H_i',
        C_i='product(c_t for t<i), C_0=1', B='sum(eta_i/C_i, i=0..24)',
        n0='B/(2^N/3^K-1)', n_i='C_i*(n0+sum(eta_t/C_t, t<i))', s_i='n_i+23/11'),
    imported_bounds=dict(B_upper=str(BMAX), root_lower=str(root_lower),
        normalized_shifted_upper=str(normalized_upper), lambda_lower=str(LMIN),
        lambda_upper=str(LMAX), height='23.61+log C_i < log s_i < 24+log C_i'),
    constants=dict(S=S, EL=EL, EU=EU, TL=TL, TU=TU, AL=AL, AU=AU, BL=BL, BU=BU),
    H_guards=guards, seed=dict(height_lower='23.61', height_upper='24',
        cap_lower=str(seed_lower), cap_upper=str(seed_upper)),
    checks=checks, integer_checks=integer_checks, logs=logs, log2_detail=ell_detail,
    summary=summary, failures=failures,
    limitations='No integer, parity, residue, exact-valuation or primitive-orbit realization; no universal descent')
path = HERE / 'survivor-remaining-real-guards-certificate.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print(f"H guards: {summary['H_guards_pass']}/25; smallest margin > {summary['weakest_H_margin_lower']} > 0 at i={weakest['i']}")
print(f"Seed: 0 < 23.61 < h0 < 24 < {summary['seed_cap_lower_floor']} < required cap")
print(f"Aggregate counts: K={K}, L={L}, N={N}, d=1, K0={K} > 225640000; exact tails and congruences checked")
print(f"Checks: {len(checks)} rational, {len(integer_checks)} integer; failures={failures}; unresolved={unresolved}")
print(f'Full certificate: {path}')
assert not failures and not unresolved
