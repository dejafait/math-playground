#!/usr/bin/env python3
"""Exact rational support checks for L691; not an analytic proof audit."""

import json
from fractions import Fraction as Q
from pathlib import Path


def exact(value):
    return {"numerator": value.numerator, "denominator": value.denominator,
            "decimal_preview": float(value)}


def main():
    d, R, U = Q(5, 4), Q(11, 8), Q(121, 64)
    e0, eps, b = Q(117, 100), Q(1, 100000), Q(2, 25)
    amax = Q(29, 20)
    angular = (1 / (d - 1 - eps) + 1 / (e0 - 1 - eps)
               + U / (U * (1 - eps) - amax)
               + U / (U * (1 - eps) - d))
    mixed = 1 / (e0 - 1 - eps) ** 2 + U / (U * (1 - eps) - R) ** 2
    outer_rate = Q(1, 500) - 20 * eps
    lower_rate = 1 / (500 * b) - 50 * eps
    # Only the elementary lower bound pi>3 is used here.
    upper_rate_lower = Q(20, 9) - 50 * eps
    tests = [
        ("angular_log_derivative", angular, "<", Q(20)),
        ("mixed_log_derivative", mixed, "<", Q(50)),
        ("outer_decay_rate", outer_rate, "=", Q(9, 5000)),
        ("central_lower_decay_rate", lower_rate, ">", Q(1, 50)),
        ("central_upper_decay_rate_using_pi_gt_3", upper_rate_lower, ">", Q(2)),
        ("lower_side_convexity_margin", U - (2 * d - 1), ">", Q(0)),
        ("anchor_distance_clearance", d - 1 - eps, ">", Q(0)),
        ("rectangle_distance_clearance", e0 - 1 - eps, ">", Q(0)),
        ("rectangle_denominator_clearance", U * (1 - eps) - amax, ">", Q(0)),
        ("central_denominator_clearance", U * (1 - eps) - R, ">", Q(0)),
        ("zero_frequency_minimum", 1 - Q(1, 8) - Q(1, 8), "=", Q(3, 4)),
    ]
    checks = []
    for name, actual, relation, required in tests:
        passed = {"<": actual < required, ">": actual > required,
                  "=": actual == required}[relation]
        checks.append({"name": name, "actual": exact(actual), "relation": relation,
                       "required": exact(required), "passed": passed})
    failures = [check["name"] for check in checks if not check["passed"]]
    artifact = {
        "step_id": "2026-11-03-two-half-logarithmic-homotopy-98",
        "lemma": "lemmas/L691-two-half-displacement-complete-logarithmic-bound.md",
        "scope": "Exact rational clearances and rate margins only; all analytic arguments remain in L691.",
        "inherited_evidence": "L690 fixed-contour bound -1/500 and finite left-sum error 8; not replayed.",
        "unverified_here": ["split-contour identity", "dominated analytic limit",
                            "nonidentity of limiting composition", "singular-log convergence",
                            "absolute onset value", "full independent-shift cube"],
        "checks": checks, "failures": failures, "all_passed": not failures,
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")
    print(f"Exact rational checks: {len(checks)-len(failures)}/{len(checks)} passed.")
    for check in checks:
        actual = check["actual"]["decimal_preview"]
        required = check["required"]["decimal_preview"]
        print(f"{check['name']}: actual {actual:.12g}; required {check['relation']} {required:.12g}; {check['passed']}")
    print(f"Failures: {failures}")
    print(f"Certificate: {output.relative_to(Path.cwd())}")
    print("No numerical onset, torus-root verification, full-cube bound or analytic audit is claimed.")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
