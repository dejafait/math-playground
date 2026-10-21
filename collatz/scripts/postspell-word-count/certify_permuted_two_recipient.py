#!/usr/bin/env python3
"""Exact comparisons for L071; full order/parameter coverage is symbolic."""
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
S, ell, u = 10**12, 693147180559, 1098612288669
lm = Q(10584, 10**14)
checks = []


def less(name, actual, required):
    actual, required = Q(actual), Q(required)
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       relation='<', margin=str(required-actual), passed=actual < required))


minimum_upper = Q(575, 11)/lm + Q(23, 11)
less('positive imported Lambda lower', 0, lm)
less('minimum shifted junction upper', minimum_upper, 500_000_000_000)
terms = [Q(27**k, factorial(k)) for k in range(41)]
less('exp27 positive partial sum exceeds threshold', 500_000_000_000, sum(terms))
less('log 11/4 below two via exp2 partial sum', Q(11, 4), 5)
# For every literal prefix row: a<=20, H>=40, so the shifted offset
# 23/11 - 2^(-a)*((12/11)*(3/2)^H+1) is strictly negative.
offset_subtraction_lower = Q(12, 11)*Q(3, 2)**40/2**20
less('negative shifted offset for a<=20 H>=40', Q(23, 11), offset_subtraction_lower)
less('L070 literal guard upper is negative', Q(-474883782659, 125000000000), 0)

prefixes, pairs, weakest = [], [], []
A = D = 0
for k in range(24):
    prefixes.append(dict(position=k, A=A, D=D))
    for j in range(k+1, 25):
        J = table[j][1]
        lhs, rhs = 4*J*ell, 29*S+A*u-D*ell
        record = dict(position=k, row=j, J=J, A=A, D=D,
                      lhs_lower_scaled=lhs, rhs_upper_scaled=rhs,
                      margin_scaled=lhs-rhs, passed=lhs > rhs)
        pairs.append(record)
        if j == k+1:
            weakest.append(record.copy())
    A += 3*table[k][1]+table[k][2]
    D += 4*table[k][1]+table[k][2]+(20 if k == 22 else 2)

boundaries = [dict(t=t, tails=[2]*22+[20, 2+18*t, 166504394-18*t])
              for t in (1, 9250244)]
table_checks = dict(
    indexed_rows=[r[0] for r in table] == list(range(25)),
    increasing_J=all(table[i][1] < table[i+1][1] for i in range(24)),
    parameter_bounds=all(j >= 8 and h >= 40 for _, j, h in table),
    sum_J=sum(j for _, j, h in table) == 66061058,
    sum_H=sum(h for _, j, h in table) == 199390205,
    odd_count=sum(3*j+h for _, j, h in table) == 397573379,
    total_length=sum(4*j+h for _, j, h in table)+166504460 == 630138897,
    constant_tail_budget=44+20+2+166504394 == 166504460,
    boundary_tail_sums=all(sum(b['tails']) == 166504460 for b in boundaries),
    boundary_tail_domain=all(a >= 2 and a % 18 == 2 for b in boundaries for a in b['tails']),
    changed_final_prefix=prefixes[23] == dict(position=23, A=144318712, D=162928807),
    full_pair_coverage=len(pairs) == 300 and len(weakest) == 24 and
        {(p['position'], p['row']) for p in pairs} ==
        {(k, j) for k in range(24) for j in range(k+1, 25)},
)
failures = [c['name'] for c in checks if not c['passed']]
failures += [name for name, passed in table_checks.items() if not passed]
failures += [f"pair {p['position']},{p['row']}" for p in pairs if not p['passed']]
smallest = min(pairs, key=lambda p: p['margin_scaled'])
result = dict(
    target='L070 intact triples in every cyclic order; integer 1<=t<=9250244; endpoint/domain/J only',
    imports=dict(source='L055 audited (2),(6); L070 audited literal exclusion',
                 lambda_lower=str(lm), log2_lower_scaled=ell, log3_upper_scaled=u, scale=S),
    rows=[dict(i=i, J=j, H=h) for i, j, h in table], boundaries=boundaries,
    symbolic=dict(tail_sum='44+20+(2+18t)+(166504394-18t)=166504460',
                  product='Lambda=sum log(1+eta_i/n_i), n_i>=47, 0<eta_i<23/11',
                  rotation='start at any minimum; rotate outgoing rows with inputs and closing edge',
                  prefixes='k<=23; literal preceding rows<=22; tail20 included only in D_23',
                  coverage='first displaced row j>k; weakest j=k+1 by strictly increasing J',
                  literal='match all endpoints/domain/J to L070 at same t'),
    minimum_shifted_upper=str(minimum_upper),
    offset_subtraction_lower=str(offset_subtraction_lower),
    checks=checks, table_checks=table_checks,
    exp27_terms=[str(v) for v in terms], exp27_sum=str(sum(terms)),
    prefixes=prefixes, pairs=pairs, weakest=weakest,
    summary=dict(pair_count=len(pairs), minimum=smallest, failures=failures),
    limitations='No H/seed, growth, minimum-location, integrality or actual-word conclusion; separate critical audit pending')
path = HERE / 'permuted-two-recipient-certificate.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print(f'Minimum shifted input upper {minimum_upper} < 500000000000 < exp(27)')
print(f'Offset subtraction lower {offset_subtraction_lower} > required 23/11')
print(f"All {len(pairs)} margins required >0; minimum {Q(smallest['margin_scaled'], S)} at ({smallest['position']},{smallest['row']})")
print(f"Changed final-prefix margin: {Q(weakest[23]['margin_scaled'], S)} > 0")
print(f'{len(checks)} rational and {len(table_checks)} table checks; failures: {failures}')
print(f'Certificate: {path}')
assert not failures
