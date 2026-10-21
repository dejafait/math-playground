#!/usr/bin/env python3
"""Exact boundary certificate for the approved uniform last-pair family.

The canonical proof supplies the symbolic monotonicity and full interval
coverage. This certificate checks its finite table and rational operands;
it does not expand billion-bit powers or numerically simulate an orbit.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parent.parent
source = (NOTEBOOK / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
table = [tuple(map(int, r)) for r in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', source, re.M)]
assert len(table) == 25 and [r[0] for r in table] == list(range(25))
S = 10**12
# Strict outward logarithm bounds imported from audited L064.
EL, EU = 693147180559, 693147180560
TL, TU = 1098612288668, 1098612288669
CU = 1011600911679
AU, BU = 3*TU-4*EL, TU-EL
LMIN, LMAX = Q(10584, 10**14), Q(10585, 10**14)
K, L, N, TMAX = 397573379, 232565518, 630138897, 9250245
checks = []


def less(name, actual, required):
    actual, required = Q(actual), Q(required)
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       difference=str(required-actual), passed=actual < required))


eta0 = Q(23, 11)-Q(12, 11)*Q(16, 27)**8-Q(16, 27)**8*Q(2, 3)**40
less('eta0 above two', 2, eta0)
less('positive Lambda imported lower', 0, LMIN)
less('Lambda upper below one', LMAX, 1)
n_lower = 2*(1-LMAX)/LMAX
less('uniform n0 and n24 lower above 18 billion', 18*10**9, n_lower)
less('all unshifted inputs above required shifted domain', Q(540, 11), 18*10**9)

# This growth bound is restricted to the t=2 test, not the full family.
less('row0 multiplier above 1e8', 10**8, Q(3**64, 2**74))
less('rows1..23 baseline with tail38 above two', 2, Q(3**117, 2**170))
BMAX = Q(23, 11)*(1+Q(2, 10**8))
normalized_upper = BMAX/LMIN+BMAX+Q(23, 11)
less('t2 normalized shifted input below 20 billion', normalized_upper, 20*10**9)
exp_terms = [Q(24**k, factorial(k)) for k in range(41)]
less('exp24 finite lower sum above 20 billion', 20*10**9, sum(exp_terms))

rows = [dict(i=i, J=j, H=h, a=38 if i == 23 else (166504376 if i == 24 else 2))
        for i, j, h in table]
table_checks = dict(
    literal_indices=[r['i'] for r in rows] == list(range(25)),
    all_J_at_least_8_H_at_least_40=all(r['J'] >= 8 and r['H'] >= 40 for r in rows),
    row24_eta_comparison=rows[24]['J'] >= 8 and rows[24]['H'] >= 40,
    first23_unchanged_tails=all(r['a'] == 2 for r in rows[:23]),
    t2_growing_baseline=all(r['J'] >= 15 and r['H'] >= 72 and r['a'] <= 38 for r in rows[1:24]),
    odd_total=sum(3*r['J']+r['H'] for r in rows) == K,
    even_total=sum(r['J']+r['a'] for r in rows) == L,
    total_exponent=sum(4*r['J']+r['H']+r['a'] for r in rows) == N,
    total_tail_budget=sum(r['a'] for r in rows) == 166504460,
    endpoint_tail23=2+18*TMAX == 166504412,
    endpoint_tail24=166504412-18*TMAX == 2,
    tail_congruences=all(r['a'] >= 2 and r['a'] % 18 == 2 for r in rows),
)
w, pk, pn = 24*S, 0, 0
prefixes = []
for r in rows:
    i, j, h, a = r['i'], r['J'], r['H'], r['a']
    prefixes.append(dict(i=i, three_exponent=pk, two_exponent=pn,
                         log_s_upper_scaled=w))
    pk += 3*j+h
    pn += 4*j+h+a
    if i < 24:
        w += j*AU+h*BU-a*EL
table_checks['closing_exponents'] = (pk, pn) == (K, N)
margin_upper = w+CU-4*rows[24]['J']*EL
less('own-input row24 J margin at t2 is negative', Q(margin_upper, S), 0)
less('row24 rejection exceeds 3.79 natural-log units', Q(margin_upper, S), Q(-379, 100))
failures = [c['name'] for c in checks if not c['passed']]
failures += [name for name, ok in table_checks.items() if not ok]
result = dict(
    target='All integer 0<=t<=9250245; literal last-pair redistribution; lower domain and J guards only',
    inputs=['L051 endpoint (4) and J guard (3)', 'L055 table/Lambda/t0', 'L064 logarithm bounds and j23 t1'],
    constants=dict(S=S, EL=EL, EU=EU, TL=TL, TU=TU, CU=CU, AU=AU, BU=BU,
                   lambda_lower=str(LMIN), lambda_upper=str(LMAX)),
    symbolic=dict(x='2^(-18t)', C='C24(0)>0', A='sum(eta_j/C_j(0), j<24)>2',
        D='2^N/3^K-1>0', B='A+eta24/(C*x)', n0='B/D',
        n24='eta24/D+C*A*(1+D)*x/D',
        directions='n0..n23 strictly increase; n24 strictly decreases'),
    uniform_domain=dict(unshifted_lower=str(n_lower), required_shifted='540/11',
                        mechanism='n0>A/D>2/D; n1..n23>C_i*n0 with C_i>1; n24>eta24/D>2/D'),
    t2=dict(rows=rows, prefixes=prefixes, closing_exponents=dict(three=pk, two=pn),
        B_upper=str(BMAX), normalized_shifted_upper=str(normalized_upper),
        rejected_guard=24, log_s24_upper_scaled=w,
        margin_upper_scaled=margin_upper, margin_upper=str(Q(margin_upper, S))),
    checks=checks, table_checks=table_checks,
    diagnostic_probes=[dict(name='initial unnecessary margin<-4 request',
        actual=str(Q(margin_upper, S)), requested='-4',
        passed=Q(margin_upper, S) < -4,
        qualification='Failed stronger bound preserved; classification requires only margin<0')],
    exp24_terms=[str(v) for v in exp_terms], failures=failures,
    interval_classification=[dict(first=0, last=1, domain='PASS', J='PASS_BY_L055_L064'),
        dict(first=2, last=TMAX, domain='PASS', J='FAIL_ROW24_BY_MONOTONICITY')],
    limitations='No H/seed or integer/parity/valuation/primitive realization; symbolic proof is in L068')
path = HERE/'uniform-last-pair-certificate.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print(f'Rational checks: {len(checks)}; table checks: {len(table_checks)}; failures: {failures}')
print(f'All t: unshifted inputs > {n_lower} > 18000000000; shifted domain required 540/11')
print(f't=2, own-input row24: RHS-LHS < {Q(margin_upper, S)} < -3.79; required >=0')
print('Initial unnecessary margin<-4 probe failed; preserved in diagnostic_probes')
print('Coverage: t=0,1 pass (imported); every t=2..9250245 fails row24 (symbolic monotonicity)')
print(f'Certificate: {path}')
assert not failures
