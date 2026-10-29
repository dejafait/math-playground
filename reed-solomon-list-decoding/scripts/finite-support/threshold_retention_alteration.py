#!/usr/bin/env python3
"""Exact arithmetic for L130; the canonical proof supplies the existence step."""
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path


def rational(value):
    value = Fraction(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def falling(n, k):
    return factorial(n) // factorial(n - k)


def main():
    q, n, k, threshold = 137, 962, 7, 1532496
    total, star = q**3, q**2
    left = total - star
    denominator = comb(n, k)
    rows = []
    for j in range(k + 1):
        subset_count = comb(k, j) * comb(n - k, k - j)
        # Independently count ordered images of the seven domain points.
        injection_count = comb(k, j) * falling(k, j) * falling(n - k, k - j)
        probability = Fraction(subset_count, denominator)
        rows.append({
            "intersection": j,
            "subset_count": subset_count,
            "injection_count": injection_count,
            "probability": rational(probability),
            "ordered_image_probability": rational(Fraction(injection_count, falling(n, k))),
            "forbidden": j >= 4,
        })
    tail = sum(row["subset_count"] for row in rows if row["forbidden"])
    probability = Fraction(tail, denominator)
    expectation = left * total * probability
    edge_cap = expectation.numerator // expectation.denominator
    retained_right = total - edge_cap
    # A different, deliberately weaker fourth-subset union bound.
    union_probability = Fraction(comb(k, 4) * falling(k, 4), falling(n, 4))
    checks = {
        "ground_size": n == 1024 - 60 - 2,
        "conditional_bijection_ground": n == 7 * q + 4 - 1,
        "hypergeometric_partition": sum(r["subset_count"] for r in rows) == denominator,
        "injection_partition": sum(r["injection_count"] for r in rows) == falling(n, k),
        "every_probability_agrees": all(r["probability"] == r["ordered_image_probability"] for r in rows),
        "tail_below_independent_union_bound": probability <= union_probability,
        "floor_brackets_expectation": edge_cap <= expectation < edge_cap + 1,
        "left_threshold": left >= threshold,
        "right_threshold": retained_right >= threshold,
        "deletion_budget": edge_cap <= total - threshold,
        "ambient_overlap_below_required": 0 < 18632,
    }
    failures = [name for name, passed in checks.items() if not passed]
    certificate = {
        "scope": "L130 exact arithmetic; finite-averaging and packing proof in canonical lemma",
        "parameters": {"q": q, "H": 1024, "K": 60, "Y": n, "residual_size": k,
                       "total_blocks": total, "left_star_deleted": star,
                       "retention_required_each": threshold, "overlap_required_for_proposed_bridge": 18632},
        "conditional_sample_space_size": factorial(n),
        "conditional_probability_justification": "A fixed right block has a uniform seven-subset image after fixing a dummy at a; each image has 7!955! extensions.",
        "subset_denominator": denominator,
        "intersection_distribution": rows,
        "forbidden_subset_count": tail,
        "forbidden_pair_probability": rational(probability),
        "expected_conflict_edges": rational(expectation),
        "fourth_subset_union_probability": rational(union_probability),
        "existence_edge_cap": edge_cap,
        "retained_bounds": {"left": left, "right": retained_right,
                            "left_margin": left - threshold, "right_margin": retained_right - threshold,
                            "right_deletion_budget": total - threshold,
                            "ambient_common_star_overlap": 0},
        "checks": checks,
        "failures": failures,
    }
    output = Path(__file__).with_name("threshold-retention-alteration.json")
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Expected conflicts: {expectation}; existence edge cap: {edge_cap}")
    print(f"Retained left >= {left}, right >= {retained_right}; required each: {threshold}")
    print("Ambient overlap: 0; proposed required overlap: 18632")
    print(f"Checks: {len(checks) - len(failures)}/{len(checks)}; failures: {failures}")
    print(f"Certificate: scripts/finite-support/{output.name}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
