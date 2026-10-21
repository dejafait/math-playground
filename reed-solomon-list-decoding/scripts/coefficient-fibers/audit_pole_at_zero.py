#!/usr/bin/env python3
"""Independently audit L019's saved arithmetic using Pascal addition."""

import json
from fractions import Fraction
from pathlib import Path


def main():
    folder = Path(__file__).parent
    saved = json.loads((folder / "pole-at-zero-results.json").read_text())
    fixed = saved["fixed_instance"]
    row = [1] + [0] * 66
    for n in range(1, 1025):
        for j in range(min(n, 66), 0, -1):
            row[j] += row[j - 1]
    total = row[66]
    classes = 65537 * 1024
    quotient, remainder = divmod(total, classes)
    lower = quotient + bool(remainder)
    ambient = 1
    for _ in range(28):
        ambient *= 65537
    threshold = Fraction(ambient, 2**128)
    ratio = Fraction(lower, 1) / threshold
    checks = {
        "pascal_matches_saved_total": total == int(fixed["total_subsets"]),
        "class_count": classes == fixed["parameter_classes"],
        "ceiling": lower == int(fixed["certified_list_lower"]),
        "ambient": ambient == int(fixed["ambient_q"]),
        "threshold": threshold == Fraction(fixed["actual_threshold"]),
        "ratio": ratio == Fraction(fixed["lower_over_threshold"]),
        "total_bounds": 2**348 < total < 2**349,
        "list_bounds": 2**322 < lower < 2**323,
        "threshold_bounds": 2**320 < threshold < 2**321,
        "strict_unsafety": lower * 2**128 > ambient,
        "ratio_bounds": Fraction(7204, 1000) < ratio < Fraction(7205, 1000),
        "radius": fixed["unsafe_error_index"] == 1024 - 66 == 958,
        "safe_index_cap": fixed["t_star_upper"] == 957,
        "original_checks": saved["all_checks_passed"] is True,
    }
    failures = [name for name, passed in checks.items() if not passed]
    result = {
        "method": "Pascal addition; Euclidean division; repeated ambient multiplication",
        "total_subsets": str(total), "parameter_classes": classes,
        "quotient": str(quotient), "remainder": remainder,
        "certified_lower": str(lower), "required_threshold": str(threshold),
        "strict_comparison_margin": str(lower * 2**128 - ambient),
        "lower_over_threshold": str(ratio), "checks": checks, "failures": failures,
        "limitations": "Arithmetic audit only; list correspondence and extension completeness require L019's proof.",
    }
    artifact = folder / "pole-at-zero-audit-results.json"
    artifact.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Audit checks: {len(checks)}; failures: {failures}")
    print("Actual lower > 2^322; required threshold < 2^321; ratio strictly between 7.204 and 7.205.")
    print(f"Certificate: {artifact}")
    assert not failures


if __name__ == "__main__":
    main()
