#!/usr/bin/env python3
"""Exact rational arithmetic replay for L738, not Fourier quadrature.

The analytic bounds, entire differentiation and admissibility must be
checked in L738 itself. This script certifies only its scalar comparisons.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

checks = []
def compare(name, actual, required, sense):
    slack = actual-required if sense == '>' else required-actual
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       sense=sense, slack=str(slack), passed=slack > 0))

delta, eta = Q(1, 10**8), Q(1, 10**7)
compare('e lower finite series', Q(8, 3), Q(5, 2), '>')
compare('e upper series and geometric tail', Q(65, 24)+Q(1, 100), Q(11, 4), '<')
compare('e fifth-power upper bound', Q(11, 4)**5, Q(200), '<')
compare('e tenth-power lower bound', Q(5, 2)**10, Q(9000), '>')
compare('normalized value damping error', Q(303, 400)*delta, eta, '<')
# sqrt(pi)>1, so this is a strict upper bound for E_1.
compare('normalized first-derivative error upper bound', Q(101, 50)*delta, eta, '<')
compare('normalized second-derivative damping error', Q(303, 160)*delta, eta, '<')
compare('normalized interval F lower bound', Q(1, 16200)-eta, Q(1, 20000), '>')
compare('normalized interval F second-derivative lower bound', Q(7, 64800)-eta, Q(1, 10000), '>')
compare('normalized F prime at 6 upper bound', -Q(1, 19683)+eta, -Q(1, 20000), '<')
compare('endpoint 7 bracket lower bound', Q(3, 400)-(Q(7, 2)+Q(17, 400))/9000, Q(7, 1000), '>')
compare('normalized F prime at 7 lower bound', Q(7, 27000)-eta, Q(1, 4000), '>')

failures = [c['name'] for c in checks if not c['passed']]
certificate = dict(
    lemma='L738', scope='Scalar rational comparisons only; no sampling, quadrature, or parameter search.',
    analytic_assumptions='L738 proves Gaussian comparison, differentiation, all admissibility conditions, and sqrt(pi)>1 is standard.',
    delta=str(delta), normalized_error_budget=str(eta),
    checks=checks, failures=failures, passed=not failures,
)
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(certificate, indent=2)+'\n')
for c in checks:
    print(f"{c['name']}: {c['actual']} {c['sense']} {c['required']}; pass={c['passed']}")
print(f"Failures: {failures}; certificate: {path.relative_to(Path.cwd())}")
raise SystemExit(bool(failures))
