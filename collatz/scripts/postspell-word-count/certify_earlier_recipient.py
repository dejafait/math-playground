#!/usr/bin/env python3
"""Exact finite evidence for L072; its written proof covers all t/orders."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
source = (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
table = [tuple(map(int, r)) for r in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', source, re.M)]
assert len(table) == 25 and [r[0] for r in table] == list(range(25))
S, ell, u, v = 10**12, 693147180559, 1098612288669, 1011600911679
lm = Q(10584, 10**14)
checks = []


def less(name, actual, required):
    actual, required = Q(actual), Q(required)
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       margin=str(required-actual), passed=actual < required))


def tails(j, t):
    return [20 if i == j else 2+18*t if i == 23
            else 166504394-18*t if i == 24 else 2 for i in range(25)]


minimum_upper = Q(575, 11)/lm+Q(23, 11)
exp27 = [Q(27**k, factorial(k)) for k in range(41)]
exp24 = [Q(24**k, factorial(k)) for k in range(41)]
offset_lower = Q(12, 11)*Q(3, 2)**40/2**20
Bmax = Q(23, 11)*(1+Q(2*2**18, 10**8))
normalized_upper = Bmax/lm+Bmax+Q(23, 11)
less('minimum shifted upper below threshold', minimum_upper, 500_000_000_000)
less('exp27 finite positive sum above threshold', 500_000_000_000, sum(exp27))
less('negative shifted prefix offset', Q(23, 11), offset_lower)
less('worst row0 multiplier exceeds weakened baseline', Q(10**8, 2**18), Q(3**64, 2**92))
less('weakened row0 baseline exceeds two', 2, Q(10**8, 2**18))
less('rows1..23 tail20 baseline exceeds two', 2, Q(3**117, 2**152))
less('uniform normalized shifted upper below 20 billion', normalized_upper, 20*10**9)
less('exp24 finite positive sum above 20 billion', 20*10**9, sum(exp24))
less('log11over4 below two via exp2', Q(11, 4), 5)

supports = []
all_pairs = []
for recipient in range(22):
    boundary = []
    for t in (1, 9250244):
        ts = tails(recipient, t)
        boundary.append(dict(t=t, tails=ts, tail_sum=sum(ts),
                             bounds_and_congruences=all(a >= 2 and a % 18 == 2 for a in ts)))
    # Prefix denominator t-coefficients are kept separately from reference exponents.
    A = D = coefficient = 0
    reference = []
    for i in range(26):
        reference.append(dict(i=i, three_exponent=A, two_exponent_at_t0=D,
                              two_exponent_t_coefficient=coefficient))
        if i < 25:
            _, J, H = table[i]
            A += 3*J+H
            D += 4*J+H+tails(recipient, 0)[i]
            coefficient += 18 if i == 23 else -18 if i == 24 else 0
    pairs = []
    for k in range(24):
        pk = reference[k]['three_exponent']
        dk = reference[k]['two_exponent_at_t0']
        old_dk = sum(4*J+H+2 for _, J, H in table[:k])+18*int(22 < k)
        delta = dk-old_dk
        for displaced in range(k+1, 25):
            lhs = 4*table[displaced][1]*ell
            rhs = 29*S+pk*u-dk*ell
            record = dict(recipient=recipient, position=k, displaced_row=displaced,
                          A=pk, D=dk, row22_support_D=old_dk,
                          D_difference=delta, difference_formula=18*(int(recipient < k)-int(22 < k)),
                          lhs_lower_scaled=lhs, rhs_upper_scaled=rhs,
                          margin_scaled=lhs-rhs,
                          passed=lhs > rhs and delta >= 0 and delta == 18*(int(recipient < k)-int(22 < k)))
            pairs.append(record)
    all_pairs.extend(pairs)
    p = reference[24]['three_exponent']
    q = reference[24]['two_exponent_at_t0']+18
    guard_q = q+4*table[24][1]
    operands = [24*S, p*u, -guard_q*ell, v]
    guard_upper = Q(sum(operands), S)
    less(f'recipient {recipient} boundary row24 upper below -3.79', guard_upper, Q(-379, 100))
    t1 = tails(recipient, 1)
    table_checks = dict(
        boundaries_valid=all(b['tail_sum'] == 166504460 and b['bounds_and_congruences'] for b in boundary),
        first24_boundary_tails_at_most20=all(a <= 20 for a in t1[:24]),
        fixed_prefix_offsets=all(H >= 40 and tails(recipient, 0)[i] <= 20 for i, J, H in table[:23]),
        row0_baseline=table[0] == (0, 8, 40) and t1[0] <= 20,
        other_boundary_growth=all(J >= 15 and H >= 72 and t1[i] <= 20 for i, J, H in table[1:24]),
        prefix_t_coefficients=[r['two_exponent_t_coefficient'] for r in reference] == [0]*24+[18, 0],
        closing_exponents=(A, D, coefficient) == (397573379, 630138897, 0),
        boundary_guard_exponents=(p, q, guard_q) == (271907921, 306970784, 430963900),
        complete_first_displacement_pairs=len(pairs) == 300,
        all_prefix_improvements=all(r['passed'] for r in pairs),
    )
    supports.append(dict(recipient=recipient, boundaries=boundary, reference_prefixes=reference,
                         pairs=pairs, table_checks=table_checks,
                         boundary_guard=dict(p=p, q=q, combined_two_exponent=guard_q,
                                             operands=operands, upper=str(guard_upper), required='>=0')))

global_checks = dict(
    increasing_J=all(table[i][1] < table[i+1][1] for i in range(24)),
    J_H_bounds=all(J >= 8 and H >= 40 for _, J, H in table),
    sum_J=sum(J for _, J, H in table) == 66061058,
    sum_H=sum(H for _, J, H in table) == 199390205,
    complete_supports=[s['recipient'] for s in supports] == list(range(22)),
    complete_pair_count=len(all_pairs) == 6600,
)
failures = [c['name'] for c in checks if not c['passed']]
failures += [name for name, ok in global_checks.items() if not ok]
failures += [f"recipient {s['recipient']}: {name}" for s in supports for name, ok in s['table_checks'].items() if not ok]
failures += [f"pair {r['recipient']},{r['position']},{r['displaced_row']}" for r in all_pairs if not r['passed']]
smallest = min(all_pairs, key=lambda r: r['margin_scaled'])
result = dict(
    target='Earlier fixed recipient j=0..21; integer t=1..9250244; arbitrary intact cyclic order; endpoint/domain/J only',
    inputs=['L051 conventions', 'L055 full table/count/log bounds', 'L064 bounds', 'L070/L071 methods'],
    constants=dict(scale=S, log2_lower_scaled=ell, log3_upper_scaled=u, log11over4_upper_scaled=v, lambda_lower=str(lm)),
    table=[dict(i=i, J=J, H=H) for i, J, H in table],
    symbolic=dict(
        unchanged_tail_sum='44+20+(2+18t)+(166504394-18t)=166504460',
        fixed_recipient_range='0<=j<=21',
        parameter_interval='1<=t<=9250244, integer',
        reference='t=0 defines coefficients only; not an admitted parameter',
        literal_root='D=exp(Lambda)-1>0; C=C24(0)>0; A=sum_(i<24)eta_i/C_i(0)>0; x=2^(-18t)',
        n24='eta24/D+C*A*(1+D)*x/D; strictly decreasing in t',
        prefix_difference='D_k(j)-D_k(22)=18*(1[j<k]-1[22<k])>=0 for k<=23',
        coverage='minimum rotation; first displaced row >k; every nonidentity permutation covered; literal rejected by monotonicity'),
    exact_bounds=dict(minimum_shifted_upper=str(minimum_upper), prefix_offset_subtraction_lower=str(offset_lower),
                      B_upper=str(Bmax), normalized_shifted_upper=str(normalized_upper)),
    checks=checks, global_checks=global_checks, supports=supports,
    exp27_terms=[str(x) for x in exp27], exp27_sum=str(sum(exp27)),
    exp24_terms=[str(x) for x in exp24], exp24_sum=str(sum(exp24)),
    summary=dict(support_count=len(supports), pair_count=len(all_pairs), weakest_pair=smallest,
                 rational_checks=len(checks), table_checks=len(global_checks)+sum(len(s['table_checks']) for s in supports),
                 failures=failures),
    limitations='Certificate supports the written proof; separate critical audit pending; no H/seed/integer/actual-word/universal conclusion')
path = HERE/'earlier-recipient-certificate.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print(f'All 22 supports and 6600 pair comparisons; required margins >0; least {Q(smallest["margin_scaled"], S)}')
print(f'Normalized shifted upper {normalized_upper} < required 20000000000')
print(f'Literal row24 margin upper {supports[0]["boundary_guard"]["upper"]} < -3.79; required >=0')
print(f'{len(checks)} rational checks, {result["summary"]["table_checks"]} table checks; failures: {failures}')
print(f'Certificate: {path}')
assert not failures
