#!/usr/bin/env python3
"""Exact finite comparisons for L069; symbolic coverage is in its proof."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
source = (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
table = [tuple(map(int, row)) for row in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', source, re.M)]
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
less('exp27 partial sum exceeds 500 billion', 500_000_000_000, sum(terms))
less('log 11/4 below two via exp2 partial sum', Q(11, 4), 5)
less('tail2 shifted offset negative at H>=5', Q(81, 44), Q(3, 11)*Q(3, 2)**5)

prefixes, pairs, weakest = [], [], []
A = D = 0
for k in range(24):
    prefixes.append(dict(position=k, A=A, D=D))
    for j in range(k+1, 25):
        J = table[j][1]
        lhs, rhs = 4*J*ell, 29*S+A*u-D*ell
        margin = lhs-rhs
        record = dict(position=k, row=j, J=J, A=A, D=D,
                      lhs_lower_scaled=lhs, rhs_upper_scaled=rhs,
                      margin_scaled=margin, passed=margin > 0)
        pairs.append(record)
        if j == k+1:
            weakest.append(record.copy())
    # Only rows 0..22 enter the load-bearing prefixes k<=23.
    A += 3*table[k][1]+table[k][2]
    D += 4*table[k][1]+table[k][2]+2

table_checks = dict(
    indexed_rows=[r[0] for r in table] == list(range(25)),
    increasing_J=all(table[i][1] < table[i+1][1] for i in range(24)),
    parameter_lower_bounds=all(j >= 8 and h >= 40 for _, j, h in table),
    odd_count=sum(3*j+h for _, j, h in table) == 397573379,
    total_tail_budget=23*2+2+166504412 == 166504460,
    total_length=sum(4*j+h for _, j, h in table)+166504460 == 630138897,
    max_parameter_tails=2+18*9250245 == 166504412 and 166504412-18*9250245 == 2,
    first_displacement_coverage=len(pairs) == 300 and len(weakest) == 24 and
        {(p['position'], p['row']) for p in pairs} ==
        {(k, j) for k in range(24) for j in range(k+1, 25)},
)
failures = [c['name'] for c in checks if not c['passed']]
failures += [name for name, passed in table_checks.items() if not passed]
failures += [f"pair {p['position']},{p['row']}" for p in pairs if not p['passed']]
smallest = min(pairs, key=lambda p: p['margin_scaled'])
result = dict(
    target='L068 intact cyclic orders, integer 2<=t<=9250245; endpoint/domain/J subsystem',
    imported_bounds=dict(source='L055 audited (2),(6)', lambda_lower=str(lm),
                         log2_lower_scaled=ell, log3_upper_scaled=u, scale=S),
    rows=[dict(i=i, J=j, H=h) for i, j, h in table],
    symbolic=dict(minimum='m=min(n_i)>=47', product='Lambda=sum log(1+eta_i/n_i)',
                  bound='m<575/(11*lambda_lower)',
                  rotation='start at any minimum; no hypothesis locating it',
                  prefixes='first displaced k<=23 has literal preceding rows <k, all tails 2',
                  conclusion='all minimum-normalized nonliteral orders fail; literal rejected by L068'),
    minimum_shifted_upper=str(minimum_upper), checks=checks, table_checks=table_checks,
    exp27_terms=[str(v) for v in terms], prefixes=prefixes, pairs=pairs, weakest=weakest,
    summary=dict(pair_count=len(pairs), minimum=smallest, failures=failures),
    limitations='Finite checks supplement L069 symbolic proof; no H/seed, integrality or actual-cycle conclusion; independent audit pending')
path = HERE / 'permuted-last-pair-certificate.json'
path.write_text(json.dumps(result, indent=2)+'\n')
print(f'Minimum shifted input upper {minimum_upper} < 500000000000 < exp(27)')
print(f"All {len(pairs)} margins required >0; minimum {Q(smallest['margin_scaled'], S)} at ({smallest['position']},{smallest['row']})")
print(f'{len(checks)} rational checks; {len(table_checks)} table checks; failures: {failures}')
print(f'Certificate: {path}')
assert not failures
