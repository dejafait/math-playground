#!/usr/bin/env python3
"""Certify one necessary guard failure for the fixed L060 order only."""
from fractions import Fraction as Q
from pathlib import Path
from math import factorial
import json
import re

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parent.parent
text = (NOTEBOOK / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
table = [tuple(map(int, m)) for m in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', text, re.M)]
assert len(table) == 25 and [r[0] for r in table] == list(range(25))
literal = [dict(index=i, J=j, H=h, a=2 if i < 24 else 166504412)
           for i, j, h in table]
order = list(range(25))
order[0], order[8] = order[8], order[0]
order[7], order[12] = order[12], order[7]
rows = [dict(position=p, **literal[i]) for p, i in enumerate(order)]
checks = []


def less(name, actual, required):
    actual, required = Q(actual), Q(required)
    checks.append(dict(name=name, relation='<', actual=str(actual),
                       required=str(required), margin=str(required-actual),
                       passed=actual < required))


K, L, N = 397573379, 232565518, 630138897
integer_checks = dict(
    fixed_order=order == [8,1,2,3,4,5,6,12,0,9,10,11,7,13,14,15,16,17,18,19,20,21,22,23,24],
    intact_permutation=sorted(order) == list(range(25)),
    large_tail_fixed=rows[-1]['index'] == 24 and rows[-1]['a'] == 166504412,
    first_24_tails_two=all(r['a'] == 2 for r in rows[:24]),
    parameter_hypotheses=all(r['J'] >= 2 and r['H'] >= 3 and r['a'] >= 0 and r['a'] % 18 == 2 for r in rows),
    odd_count=sum(3*r['J']+r['H'] for r in rows) == K,
    even_count=sum(r['J']+r['a'] for r in rows) == L,
    length=K+L == N,
    primitive_scaling_d1=K > 225640000 and L > 0,
    all_J_ge_8_H_ge_40=all(r['J'] >= 8 and r['H'] >= 40 for r in rows),
    first_J1230_H5849=rows[0]['J'] == 1230 and rows[0]['H'] == 5849)
prefixes = []
pk = pn = 0
for r in rows:
    prefixes.append(dict(position=r['position'], index=r['index'],
                         three_exponent=pk, two_exponent=pn))
    pk += 3*r['J']+r['H']
    pn += 4*r['J']+r['H']+r['a']
integer_checks['complete_product_exponents'] = (pk,pn) == (K,N)

# The actual first row dominates (J,H,a)=(8,40,2) in J and H.
# Its c0 bound is thus recomputed by a small exact baseline comparison.
baseline_c = Q(3**64, 2**74)
baseline_eta = Q(23,11)-Q(12,11)*Q(16,27)**8-Q(16,27)**8*Q(2,3)**40
less('first multiplier baseline exceeds 1e8', 10**8, baseline_c)
less('first eta baseline exceeds two', 2, baseline_eta)
less('each first-24 multiplier exceeds two', 2, Q(27,16)**2*Q(3,2)**3/4)
lambda_low, lambda_high = Q(10584,10**14), Q(10585,10**14)
# These Lambda endpoints are imported from the separately audited L055,
# not asserted as a new logarithm evaluation or read from a preview.
less('imported Lambda interval positive', 0, lambda_low)
less('imported Lambda interval ordered', lambda_low, lambda_high)
less('imported Lambda upper below one', lambda_high, 1)
B_upper = Q(23,11)*(1+Q(2,10**8))
n_lower = 2*(1-lambda_high)/lambda_high
s_upper = B_upper/lambda_low+Q(23,11)
less('n0 above 18 billion', 18*10**9, n_lower)
less('s0 below 20 billion', s_upper, 20*10**9)
less('minimum lower-junction guard', Q(540,11), 18*10**9)
less('length inequality', N, Q(8,5)*K+Q(1725,1034))

# Positive exponential terms prove exp(24)>20e9 and exp(2)>11/4.
exp24_terms = [Q(24**j, factorial(j)) for j in range(41)]
less('exp24 finite lower sum above 20 billion', 20*10**9, sum(exp24_terms))
less('exp2 finite lower sum above 11/4', Q(11,4), Q(1+2+2))
# log 2 = 2*sum (1/3)^(2j+1)/(2j+1); retain its first two terms.
log2_lower = 2*(Q(1,3)+Q(1,81))
less('log2 positive-series lower bound above 2/3', Q(2,3), log2_lower)
guard_lhs_lower = 4*rows[0]['J']*Q(2,3)
guard_rhs_upper = Q(24+2)
less('violated J guard: RHS upper below LHS lower', guard_rhs_upper, guard_lhs_lower)

failures = [c['name'] for c in checks if not c['passed']]
failures += [name for name, passed in integer_checks.items() if not passed]
result = dict(
    verdict='FIXED_ORDER_REAL_SYSTEM_REJECTED_BY_MINIMUM_J_GUARD',
    scope='Only L060 swaps (0,8),(7,12); no other order or parameter change',
    order=order, rows=rows, prefixes=prefixes,
    counts=dict(K=K,L=L,N=N,d=1,K0=K,L0=L),
    lambda_input=dict(source='L055 equation (2), separately audited',
                      lower=str(lambda_low),upper=str(lambda_high)),
    definition=dict(c='3^(3J+H)/2^(4J+H+a)',
                    eta='23/11-(12/11)*(16/27)^J-(16/27)^J*(2/3)^H',
                    C='product(c_j for j<i); C_0=1',
                    B='sum(eta_i/C_i for i=0,...,24)',
                    n0='B/(2^N/3^K-1)',
                    n_i='C_i*(n0+sum(eta_j/C_j for j<i))',
                    s_i='n_i+23/11'),
    bounds=dict(B_lower='2',B_upper=str(B_upper),n0_lower=str(n_lower),
                s0_upper=str(s_upper),minimum_position=0,minimum_original_index=8,
                minimum_unique_reason='First 24 multipliers exceed 2 and eta positive'),
    guard_failure=dict(position=0,original_index=8,J=1230,
                       required='4J log2 <= log(s0)+log(11/4)',
                       lhs_strict_lower=str(guard_lhs_lower),rhs_strict_upper=str(guard_rhs_upper),
                       separation=str(guard_lhs_lower-guard_rhs_upper),
                       remaining_guard_checks='Not needed after one certified necessary failure'),
    exp24_terms=[str(t) for t in exp24_terms],
    checks=checks,integer_checks=integer_checks,failures=failures,
    limitations='No integrality or actual orbit claimed; all other orders and universal descent open')
path = HERE/'joint-witness-real-guard-certificate.json'
path.write_text(json.dumps(result,indent=2)+'\n')
print(f'Rational checks {len(checks)}; integer checks {len(integer_checks)}; failures {failures}')
print('Unique designated minimum: position 0, original row 8; 18e9<n0<s0<20e9')
print(f'Required J guard fails: LHS>{guard_lhs_lower}, RHS<{guard_rhs_upper}; separation>{guard_lhs_lower-guard_rhs_upper}')
print(f'Certificate: {path}')
assert not failures
