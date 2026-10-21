#!/usr/bin/env python3
"""Exact L076 benchmark; the universal implication is proved in the lemma.

Reuse audited L055 Lambda and L064 logarithm enclosures. No new-table
search, unknown feasible junction, or enumeration of allocations is used.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import factorial
import json
import re

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parent.parent
source = (NOTEBOOK / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
rows = [tuple(map(int, row)) for row in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', source, re.M)]
assert len(rows) == 25 and [row[0] for row in rows] == list(range(25))
published = (NOTEBOOK / 'lemmas/L064-single-tail-redistribution-j-guard-classification.md').read_text()
old_margins = [tuple(map(int, row)) for row in re.findall(
    r'^\|(\d+)\|(\d+)\|(-\d+)\|$', published, re.M)]
assert len(old_margins) == 23
checks = []


def check(name, actual, required, relation):
    actual, required = Q(actual), Q(required)
    passed = {'<': actual < required, '>': actual > required,
              '=': actual == required}[relation]
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       relation=relation, difference=str(actual-required), passed=passed))


r, budget = len(rows), 9250245
K = sum(3*J+H for _, J, H in rows)
N = sum(4*J+H for _, J, H in rows)+2*r+18*budget
lam, cap, T = Q(10584, 10**14), Q(20*10**9), Q(24)
scale = 10**12
ell, u, v = Q(693147180559, scale), Q(1098612288669, scale), Q(1011600911679, scale)
E = Q(23*(r-1), 4*2**(4*rows[1][1])-23)
check('positive residual', lam-E, 0, '>')
R = Q(23, 11)/(lam-E)+Q(23, 11)
check('root cap', R, cap, '<')
exp_terms = [T**k/factorial(k) for k in range(41)]
check('positive exponential partial sum', sum(exp_terms), cap, '>')
minimum_H = min(H for _, _, H in rows[:r-2])
offset_bound = Q(12, 11)*Q(3, 2)**minimum_H+1
check('smallest early H tail20 offset test', offset_bound, Q(23, 11)*2**20, '>')
check('odd count', K, 397573379, '=')
check('total count', N, 630138897, '=')

margins = []
A = D = 0
for j in range(r-2):
    _, J, H = rows[j]
    A += 3*J+H
    D += 4*J+H+2
    next_J = rows[j+1][1]
    M = (D+18+4*next_J)*ell-T-v-A*u
    old_j, old_input, old_upper = old_margins[j]
    assert (old_j, old_input) == (j, j+1)
    check(f'recipient {j} strict rejection', M, Q(932, 100), '>')
    check(f'recipient {j} exact L064 margin match', M, Q(-old_upper, scale), '=')
    margins.append(dict(first_recipient=j, next_input=j+1, A=A, D=D,
                        next_J=next_J, margin=str(M),
                        scaled_margin=int(M*scale), published_upper=old_upper))

integer_checks = dict(
    r_at_least_three=r >= 3,
    integer_domain=all(J >= 2 and H >= 3 for _, J, H in rows),
    increasing_J=all(rows[i][1] < rows[i+1][1] for i in range(r-1)),
    budget_positive=budget > 0,
    nonzero_index_floor=all(J >= rows[1][1] for _, J, _ in rows[1:]),
    offset_floor_all_early=all(H >= minimum_H for _, _, H in rows[:r-2]),
    all_recipient_indices=[m['first_recipient'] for m in margins] == list(range(r-2)),
    both_boundaries=(margins[0]['first_recipient'], margins[-1]['first_recipient']) == (0, r-3))
failures = [c['name'] for c in checks if not c['passed']]
failures += [name for name, passed in integer_checks.items() if not passed]
minimum = min(Q(m['margin']) for m in margins)
certificate = dict(
    purpose='L076 complete fixed-table specialization; not a new-table search',
    imports=['L055 table and lambda < Lambda', 'L064 logarithm enclosures and margin table',
             'L073 audited benchmark comparisons'],
    rows=rows, budget=budget, K=K, N=N,
    constants=dict(lambda_lower=str(lam), E=str(E), residual=str(lam-E), R=str(R),
                   U=str(cap), T=str(T), ell=str(ell), u=str(u), v=str(v)),
    exponential_terms=[str(t) for t in exp_terms],
    offset=dict(minimum_early_H=minimum_H, Q_lower=str(offset_bound)),
    checks=checks, integer_checks=integer_checks, margins=margins,
    zero_budget_case='No tests required; nonnegative entries with zero sum are all zero.',
    summary=dict(rational_checks=len(checks), integer_checks=len(integer_checks),
                 recipients=len(margins), minimum_margin=str(minimum),
                 required_margin='233/25', first_margin=margins[0]['margin'],
                 final_margin=margins[-1]['margin'], failures=failures))
path = HERE / 'variable-table-early-support-certificate.json'
path.write_text(json.dumps(certificate, indent=2)+'\n')
print(f'Checks: {len(checks)} rational, {len(integer_checks)} integer; failures: {failures}')
print(f'Root cap: {R} < required {cap}; residual: {lam-E} > required 0')
print(f'Recipients: {len(margins)}/{r-2}; minimum margin {minimum} > required 233/25')
print(f'Certificate: {path.relative_to(NOTEBOOK)}')
assert not failures
