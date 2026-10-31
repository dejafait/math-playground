#!/usr/bin/env python3
"""Replay only L491's rational arithmetic; analytic proof is in the lemma."""
from fractions import Fraction as F
import json
from pathlib import Path


def encode(value):
    return str(value) if isinstance(value, F) else value


checks = []


def check(name, actual, required, strict=False):
    passed = actual < required if strict else actual <= required
    checks.append({
        "name": name,
        "actual": encode(actual),
        "required": encode(required),
        "relation": "<" if strict else "<=",
        "passed": passed,
    })


# Upper bound claimed in the source is smaller than an exact component.
source_lower = F(1, 200) + F(100, 10001)
check("source_76_bound_below_exact_imaginary_component", F(2, 194),
      source_lower, strict=True)
check("half_time_bound", F(11, 100), F(1, 8))
check("Q_extra_terms_below_one", F(1, 400) + F(4, 198), F(1))
check("center_constant", F(1) + F(4, 8) * 3, F(5, 2))
check("derivative_constant_before_denominator_coarsening",
      F(1, 2) + 4 + F(2, 8), F(19, 4))
check("combined_log_coefficient", F(1, 2) + F(1, 8), F(1))
check("combined_constant", F(5, 2) + F(19, 2), F(20))
threshold = F(10020 * 6, 12 * 10000**3)
check("threshold_simplification", threshold, F(5010, 10**12))
check("required_tolerance", threshold, F(1, 100), strict=True)

failures = [item["name"] for item in checks if not item["passed"]]
certificate = {
    "lemma": "L491",
    "scope": "Exact rational arithmetic only; no automated branch or continuum proof.",
    "source_discrepancy": {
        "source_bound": str(F(2, 194)),
        "exact_imaginary_component": str(source_lower),
        "positive_difference": str(source_lower - F(2, 194)),
        "positive_common_denominator_numerator": 30001 * 97 - 200 * 10001,
    },
    "checks": checks,
    "uniform_analytic_bound": "(log(X/(4*pi))+20)/X; proved in canonical L491",
    "rational_upper_bound": str(threshold),
    "required_tolerance": "1/100",
    "failures": failures,
    "passed": not failures,
}
output = Path(__file__).with_name("l491-arithmetic-certificate.json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"L491 rational checks: {len(checks)}; failures: {failures}")
print(f"Actual upper bound: {threshold}; required: <1/100")
print(f"Full certificate: {output.relative_to(Path.cwd())}")
raise SystemExit(bool(failures))
