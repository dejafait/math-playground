#!/usr/bin/env python3
"""Finite exact comparisons for L073; uniform allocation coverage is in its proof.

Logarithm enclosures are imported from L064, not inferred from decimals.
No floating-point arithmetic or enumeration of the allocation simplex is used.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parent.parent
source = (NOTEBOOK / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
rows = [tuple(map(int, r)) for r in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', source, re.M)]
assert len(rows) == 25 and [r[0] for r in rows] == list(range(25))
checks = []


def less(name, actual, required):
    actual, required = Q(actual), Q(required)
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       margin=str(required-actual), passed=actual < required))


epsilon = Q(24*23, 4*2**60-23)
lambda_lower = Q(10584, 10**14)
less('other-input mass upper below lambda lower', epsilon, lambda_lower)
s0_upper = Q(23, 11)/(lambda_lower-epsilon)+Q(23, 11)
less('guard-conditioned s0 upper below 20 billion', s0_upper, 20*10**9)
less('tail20 negative shifted offset at H40', Q(23, 11)*2**20,
     Q(12, 11)*Q(3, 2)**40+1)

S = 10**12
EL, EU = 693147180559, 693147180560
TL, TU = 1098612288668, 1098612288669
CU = 1011600911679
AU, BU = 3*TU-4*EL, TU-EL
prefix_upper = 24*S
margins = []
for j in range(23):
    _, J, H = rows[j]
    prefix_upper += J*AU+H*BU-2*EL
    next_J = rows[j+1][1]
    upper = prefix_upper-18*EL+CU-4*next_J*EL
    margins.append(dict(first_recipient=j, failed_input=j+1,
                        base_prefix_upper_scaled=prefix_upper,
                        guard_upper_numerator=upper, scale=S))
    less(f'first recipient {j} guard margin below -9.32', Q(upper, S), -Q(932, 100))

integer_checks = dict(
    all_parameters_in_domain=all(J >= 2 and H >= 40 for _, J, H in rows),
    other_J_at_least_15=all(J >= 15 for _, J, _ in rows[1:]),
    odd_count=sum(3*J+H for _, J, H in rows) == 397573379,
    total_count=sum(4*J+H for _, J, H in rows)+50+18*9250245 == 630138897,
    all_first_recipients_covered=[m['first_recipient'] for m in margins] == list(range(23)))
failures = [c['name'] for c in checks if not c['passed']]
failures += [name for name, passed in integer_checks.items() if not passed]
certificate = dict(
    purpose='Exact finite comparisons for the all-allocation proof L073',
    imports='L055 indexed pairs and Lambda; L064 logarithm enclosures and log(20e9)<24',
    rows=rows, other_mass_upper=str(epsilon), lambda_lower=str(lambda_lower),
    s0_upper=str(s0_upper), checks=checks, integer_checks=integer_checks,
    margins=margins, failures=failures)
path = HERE / 'arbitrary-literal-early-support-certificate.json'
path.write_text(json.dumps(certificate, indent=2)+'\n')
print(f'Exact checks: {len(checks)} rational, {len(integer_checks)} integer; failures: {failures}')
print(f's0 upper: {s0_upper} < required {20*10**9}')
worst = max(m['guard_upper_numerator'] for m in margins)
print(f'Largest guard upper bound: {worst}/{S} < required -932/100; all 23 first recipients covered')
print(f'Certificate: {path.relative_to(NOTEBOOK)}')
assert not failures
