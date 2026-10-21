#!/usr/bin/env python3
"""Exact own-input J-guard classification of the approved 24 allocations.

Huge roots are defined by factored rational expressions; rational bounds
certify their domains and guards without expanding those expressions.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parent.parent
text = (NOTEBOOK/'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
table = [tuple(map(int, m)) for m in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', text, re.M)]
assert len(table) == 25 and [r[0] for r in table] == list(range(25))
S, BITS, TERMS = 10**12, 192, 96
checks, logs = [], {}


def less(name, actual, required):
    actual, required = Q(actual), Q(required)
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       margin=str(required-actual), passed=actual < required))


def base_log(t):
    x = (t-1)/(t+1)
    assert 0 <= x <= Q(1, 3)
    scale = 2**BITS
    rounded = []
    for k in range(TERMS):
        term = scale*2*x**(2*k+1)/(2*k+1)
        rounded.append(term.numerator//term.denominator)
    lo = Q(sum(rounded), scale)
    remainder = Q(9, 4*(2*TERMS+1)*3**(2*TERMS+1))
    return lo, lo+Q(TERMS, scale)+remainder, dict(
        x=str(x), rounded_summands=rounded,
        rounding_budget=str(Q(TERMS, scale)), remainder_upper=str(remainder))


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


l2, u2 = log_bounds(2)
l3, u3 = log_bounds(3)
lc, uc = log_bounds(Q(11, 4))
EL, EU = 693147180559, 693147180560
TL, TU = 1098612288668, 1098612288669
CL, CU = 1011600911678, 1011600911679
for name, lo, hi, lower, upper in [
        ('log2', l2, u2, EL, EU), ('log3', l3, u3, TL, TU),
        ('log(11/4)', lc, uc, CL, CU)]:
    less(name+' lower', Q(lower, S), lo)
    less(name+' upper', hi, Q(upper, S))
AL, AU, BL, BU = 3*TL-4*EU, 3*TU-4*EL, TL-EU, TU-EL
less('alpha lower positive', 0, AL)
less('beta lower positive', 0, BL)

# Counts and the imported, audited L055 Lambda interval are unchanged.
K, L, N = 397573379, 232565518, 630138897
LMIN, LMAX = Q(10584, 10**14), Q(10585, 10**14)
less('Lambda lower independently reproduced', LMIN, N*l2-K*u3)
less('Lambda upper independently reproduced', N*u2-K*l3, LMAX)
less('Lambda upper below one', LMAX, 1)

# Uniform changed-tail prefix bounds, including j=0.
eta0 = Q(23, 11)-Q(12, 11)*Q(16, 27)**8-Q(16, 27)**8*Q(2, 3)**40
less('eta0 above two', 2, eta0)
less('row0 tail20 multiplier above 1e8/2^18', Q(10**8, 2**18), Q(3**64, 2**92))
less('row0 uniform multiplier above two', 2, Q(10**8, 2**18))
less('rows1..23 tail20 baseline above two', 2, Q(3**117, 2**152))
BMAX = Q(23, 11)*(1+Q(2*2**18, 10**8))
n_lower = 2*(1-LMAX)/LMAX
n_upper = BMAX/LMIN
less('n0 lower above 18 billion', 18*10**9, n_lower)
less('prefix normalized shifted upper below 20 billion', n_upper+BMAX+Q(23, 11), 20*10**9)
less('domain follows from lower root', Q(540, 11), 18*10**9)
lowlog, _ = log_bounds(18*10**9)
less('lower normalized log above 23.61', Q(2361, 100), lowlog)
exp24_terms = [Q(24**k, factorial(k)) for k in range(41)]
less('exp24 finite lower sum above 20 billion', 20*10**9, sum(exp24_terms))

allocations = []
for moved in range(24):
    rows = [dict(i=i, J=j, H=h, a=20 if i == moved else (166504394 if i == 24 else 2))
            for i, j, h in table]
    integer_checks = dict(
        literal_order=[r['i'] for r in rows] == list(range(25)),
        parameter_domain=all(r['J'] >= 2 and r['H'] >= 3 and r['a'] >= 2 and r['a'] % 18 == 2 for r in rows),
        odd_total=sum(3*r['J']+r['H'] for r in rows) == K,
        even_total=sum(r['J']+r['a'] for r in rows) == L,
        total_exponent=sum(4*r['J']+r['H']+r['a'] for r in rows) == N,
        growing_prefix_baselines=all(r['J'] >= 15 and r['H'] >= 72 and r['a'] <= 20 for r in rows[1:24]))
    v, w, pk, pn = 2361*S//100, 24*S, 0, 0
    guard_records, prefixes = [], []
    for r in rows:
        i, j, h, a = r['i'], r['J'], r['H'], r['a']
        prefixes.append(dict(i=i, three_exponent=pk, two_exponent=pn))
        lower_margin, upper_margin = v+CL-4*j*EU, w+CU-4*j*EL
        verdict = ('PASS_STRICT' if lower_margin > 0 else
                   'FAIL_STRICT' if upper_margin < 0 else 'UNRESOLVED')
        guard_records.append(dict(i=i, J=j, log_s_lower_scaled=v,
            log_s_upper_scaled=w, margin_lower_scaled=lower_margin,
            margin_upper_scaled=upper_margin, verdict=verdict))
        pk += 3*j+h
        pn += 4*j+h+a
        if i < 24:
            v += j*AL+h*BL-a*EU
            w += j*AU+h*BU-a*EL
    integer_checks['closing_product'] = (pk, pn) == (K, N)
    rejected = [g['i'] for g in guard_records if g['verdict'] == 'FAIL_STRICT']
    unresolved = [g['i'] for g in guard_records if g['verdict'] == 'UNRESOLVED']
    verdict = ('REJECTED_BY_J_GUARD' if rejected else
               'ALL_J_GUARDS_PASS' if not unresolved else 'UNRESOLVED')
    allocations.append(dict(moved_tail_row=moved, rows=rows, prefixes=prefixes,
        closing_prefix=dict(three_exponent=pk, two_exponent=pn),
        domain='ALL_s_i_ABOVE_18_BILLION', verdict=verdict,
        first_failed_guard=rejected[0] if rejected else None,
        unresolved_guard_indices=unresolved, guards=guard_records,
        integer_checks=integer_checks))

failures = [c['name'] for c in checks if not c['passed']]
failures += [f'allocation {a["moved_tail_row"]}: {k}' for a in allocations
             for k, passed in a['integer_checks'].items() if not passed]
failures += [f'allocation {a["moved_tail_row"]}: no decisive classification'
             for a in allocations if a['verdict'] == 'UNRESOLVED']
survivors = [a['moved_tail_row'] for a in allocations if a['verdict'] == 'ALL_J_GUARDS_PASS']
result = dict(target='24 literal-order single-tail redistributions; necessary J guards only',
    inputs=['L051 (3)-(4)', 'L055 table and Lambda interval'],
    counts=dict(K=K, L=L, N=N),
    definition=dict(c_i='3^(3J_i+H_i)/2^(4J_i+H_i+a_i)',
        eta_i='23/11-(12/11)*(16/27)^J_i-(16/27)^J_i*(2/3)^H_i',
        C_i='product(c_t for t<i), C_0=1', B='sum(eta_i/C_i, i=0..24)',
        n0='B/(2^N/3^K-1)', n_i='C_i*(n0+sum(eta_t/C_t, t<i))', s_i='n_i+23/11'),
    bounds=dict(lambda_lower=str(LMIN), lambda_upper=str(LMAX), eta0=str(eta0),
        B_lower='2', B_upper=str(BMAX), n0_lower=str(n_lower), n0_upper=str(n_upper),
        normalized_shifted_upper=str(n_upper+BMAX+Q(23, 11)),
        height='23.61+log C_i < log s_i < 24+log C_i, i=0..24'),
    constants=dict(S=S, EL=EL, EU=EU, TL=TL, TU=TU, CL=CL, CU=CU,
                   AL=AL, AU=AU, BL=BL, BU=BU),
    allocations=allocations, survivors=survivors,
    checks=checks, logs=logs, log2_detail=ell_detail,
    exp24_terms=[str(t) for t in exp24_terms], failures=failures,
    limitations='No H guards, seed, integrality, parity, exact valuations or actual cycle asserted')
path = HERE/'single-tail-redistribution-certificate.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print(f'Rational checks: {len(checks)}; allocation integer checks: {sum(len(a["integer_checks"]) for a in allocations)}; failures: {failures}')
print('All 24 exact cyclic tuples: n0>18e9; all s_i>18e9; required s_i>=540/11')
print(f'Certified all-J survivors (moved row): {survivors}')
for a in allocations:
    if a['first_failed_guard'] is not None:
        g = a['guards'][a['first_failed_guard']]
        print(f'j={a["moved_tail_row"]}: guard i={g["i"]} fails; RHS-LHS < {Q(g["margin_upper_scaled"], S)} < 0')
    else:
        margin = min(g['margin_lower_scaled'] for g in a['guards'])
        print(f'j={a["moved_tail_row"]}: all 25 guards pass; RHS-LHS > {Q(margin, S)} > 0')
print(f'Certificate: {path}')
assert not failures
