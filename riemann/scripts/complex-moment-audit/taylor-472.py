#!/usr/bin/env python3
"""Exact scalar checks for L790; analytic reductions are proved in that file."""
from fractions import Fraction as F
import json
from math import factorial
from pathlib import Path


checks = []


def check(name, actual, required):
    actual, required = F(actual), F(required)
    passed = actual < required
    checks.append({
        "name": name,
        "actual": str(actual),
        "relation": "<",
        "required": str(required),
        "passed": passed,
    })
    print(f"{name}: {actual} < {required}: {'PASS' if passed else 'FAIL'}")


k0 = 10**9
check("Cauchy radius / k inside analytic radius / k", F(1, 40), F(1, 20))
check("drift fraction versus permitted relative loss", F(3, 200), F(1, 25))
check("saddle action normalized upper", F(4, 6) / F(24, 25)**2, 5)
check("curvature lower exceeds one", 1, 6 * F(21, 25) * 300)
check("curvature upper below coarse twenty", F(14185, 1000), 20)
check("exponential partial sum implies log(20)<4", 20,
      sum((F(4)**j / factorial(j) for j in range(5)), F(0)))
check("exponential partial sum implies log(10)<3", 10,
      sum((F(3)**j / factorial(j) for j in range(4)), F(0)))
check("curvature logarithm coarse base-height upper", 33, k0)
check("relative-error logarithm upper", F(9, 491), F(19, 1000))

components = {
    "saddle_action": F(5, 1600 * 3 * 2),
    "curvature_log": F(1, 2),
    "relative_error_log": F(19, 1000 * k0),
    "gamma": (F(1, 3 * k0) + F(2, 3 * 2)) / 40**3,
}
total = sum(components.values(), F(0))
assert total == F(96101000003649, 192000000000000)
check("uniform normalized total versus audit margin", total, F(2503, 5000))
check("uniform normalized total versus requested threshold", total, 3)
failures = [c["name"] for c in checks if not c["passed"]]
certificate = {
    "summary": {
        "lemma": "L790",
        "scope": "integer k>=10^9, integer d>=3; monotonicity proved in lemma",
        "checks": len(checks),
        "all_passed": not failures,
        "failures": failures,
        "actual_normalized_upper": str(total),
        "required_normalized_upper": "3",
        "audit_margin": "2503/5000",
        "qualification": "Exact scalar verification only; not an analytic proof or source ancillary replay",
    },
    "components_at_d3_k1e9": {key: str(value) for key, value in components.items()},
    "checks": checks,
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Failures: {failures}; full certificate: {path}")
assert not failures, failures
