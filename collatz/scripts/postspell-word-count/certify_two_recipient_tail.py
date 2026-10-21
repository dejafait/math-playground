#!/usr/bin/env python3
"""Exact finite checks for L070; the canonical proof covers the interval."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parent.parent
source = (NOTEBOOK / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
table = [tuple(map(int, row)) for row in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', source, re.M)]
assert len(table) == 25 and [r[0] for r in table] == list(range(25))
S = 10**12
# Strict outward enclosures imported from independently audited L064.
EL, EU = 693147180559, 693147180560
TL, TU = 1098612288668, 1098612288669
CU = 1011600911679
LMIN, LMAX = Q(10584, 10**14), Q(10585, 10**14)
TMAX = 9250244
checks = []


def less(name, actual, required):
    actual, required = Q(actual), Q(required)
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       difference=str(required-actual), passed=actual < required))


eta0 = Q(23, 11)-Q(12, 11)*Q(16, 27)**8-Q(16, 27)**8*Q(2, 3)**40
less('eta0 above two', 2, eta0)
less('positive Lambda lower', 0, LMIN)
less('Lambda upper below one', LMAX, 1)
n_lower = 2*(1-LMAX)/LMAX
less('uniform unshifted lower exceeds 18 billion', 18*10**9, n_lower)
less('shifted lower domain follows from unshifted lower', Q(540, 11), n_lower+Q(23, 11))
less('unchanged row0 multiplier above 1e8', 10**8, Q(3**64, 2**74))
less('tail20 baseline for rows1..23 exceeds two', 2, Q(3**117, 2**152))
BMAX = Q(23, 11)*(1+Q(2, 10**8))
normalized_upper = BMAX/LMIN+BMAX+Q(23, 11)
less('t1 normalized shifted input below 20 billion', normalized_upper, 20*10**9)
exp_terms = [Q(24**k, factorial(k)) for k in range(41)]
less('exp24 positive finite sum exceeds 20 billion', 20*10**9, sum(exp_terms))

def tails(t):
    return [20 if i == 22 else 2+18*t if i == 23
            else 166504394-18*t if i == 24 else 2 for i in range(25)]

rows = [dict(i=i, J=j, H=h, a=a) for (i, j, h), a in zip(table, tails(1))]
table_checks = dict(
    literal_indices=[r['i'] for r in rows] == list(range(25)),
    all_J_at_least_8_H_at_least_40=all(r['J'] >= 8 and r['H'] >= 40 for r in rows),
    fixed_first23_tails=[r['a'] for r in rows[:23]] == [2]*22+[20],
    t1_growth_baseline=all(r['J'] >= 15 and r['H'] >= 72 and r['a'] <= 20 for r in rows[1:24]),
    uniform_first23_growth=all(r['J'] >= 15 and r['H'] >= 72 and r['a'] <= 20 for r in rows[1:23]),
    odd_total=sum(3*r['J']+r['H'] for r in rows) == 397573379,
    even_total=sum(r['J']+r['a'] for r in rows) == 232565518,
    exponent_total=sum(4*r['J']+r['H']+r['a'] for r in rows) == 630138897,
    t1_tail_budget=sum(tails(1)) == 166504460,
    tmax_tail_budget=sum(tails(TMAX)) == 166504460,
    moving_tail_coefficient_sum=18-18 == 0,
    t1_tails=tails(1)[22:] == [20, 20, 166504376],
    tmax_tails=tails(TMAX)[22:] == [20, 166504394, 2],
    endpoint_tail_bounds_and_congruences=all(a >= 2 and a % 18 == 2
        for t in (1, TMAX) for a in tails(t)),
)
pk = pn = 0
prefixes = []
for r in rows:
    prefixes.append(dict(i=r['i'], three_exponent=pk, two_exponent=pn))
    pk += 3*r['J']+r['H']
    pn += 4*r['J']+r['H']+r['a']
table_checks['closing_exponents'] = (pk, pn) == (397573379, 630138897)
p, q = prefixes[24]['three_exponent'], prefixes[24]['two_exponent']
guard_q = q+4*rows[24]['J']
margin_scaled = 24*S+p*TU-guard_q*EL+CU
less('t1 row24 own-input J margin is negative', Q(margin_scaled, S), 0)
less('t1 row24 rejection exceeds 3.79', Q(margin_scaled, S), Q(-379, 100))
table_checks['t1_prefix_exponents'] = (p, q, guard_q) == (271907921, 306970784, 430963900)
failures = [c['name'] for c in checks if not c['passed']]
failures += [name for name, passed in table_checks.items() if not passed]
result = dict(
    target='Literal two-recipient endpoint/domain/J system; integer 1<=t<=9250244',
    inputs=['L051 endpoint/J conventions', 'L055 table and positive Lambda', 'L064 audited log enclosures'],
    constants=dict(S=S, EL=EL, EU=EU, TL=TL, TU=TU, CU=CU,
                   lambda_lower=str(LMIN), lambda_upper=str(LMAX)),
    symbolic=dict(reference_tails='a22=20,a23=2,a24=166504394 at t=0 (reference only)',
        x='2^(-18t)', C='C24(0)>0', A='sum(eta_j/C_j(0),j<24)>2',
        D='2^N/3^K-1>0', B='A+eta24/(C*x)',
        n0='B/D', n24='eta24/D+C*A*(1+D)*x/D',
        monotonicity='n0..n23 increase; n24 decreases strictly; proven in L070'),
    uniform_domain=dict(unshifted_lower=str(n_lower), required_shifted='540/11'),
    t1=dict(rows=rows, prefixes=prefixes, closing_exponents=dict(three=pk, two=pn),
        B_upper=str(BMAX), normalized_shifted_upper=str(normalized_upper),
        row24_guard=dict(index=24, three_exponent=p, combined_two_exponent=guard_q,
            operands=[24*S, p*TU, -guard_q*EL, CU],
            margin_upper_scaled=margin_scaled, margin_upper=str(Q(margin_scaled, S)),
            required_margin='>=0')),
    checks=checks, table_checks=table_checks, exp24_terms=[str(v) for v in exp_terms],
    failures=failures,
    interval_verdict='Every integer 1..9250244 fails own-input row24 by symbolic monotonicity',
    limitations='Finite arithmetic supports written proof; no H/seed/integer/parity/valuation/actual-word bridge',
)
path = HERE/'two-recipient-tail-certificate.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print(f'Checks: {len(checks)} rational, {len(table_checks)} table; failures: {failures}')
print(f'All t: n_i > {n_lower} > 18000000000; required s_i >= 540/11')
print(f't=1 row24: margin < {Q(margin_scaled, S)} < -3.79; required >=0')
print('Every admitted t fails row24 by the canonical monotonicity proof.')
print(f'Certificate: {path}')
assert not failures
