#!/usr/bin/env python3
"""Exact arithmetic supporting L891; not verification of its analytic proof."""

import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path


def main():
    exp_upper = sum((F(1, factorial(n)) for n in range(5)), F(0)) + F(1, 100)
    exp_11_10_lower = sum((F(11, 10)**n / factorial(n) for n in range(6)), F(0))
    k1_lower = F(9, 10) + F(2, 15) + F(1, 24) + F(1, 64)
    k3_upper = 2 * (F(1) - F(1) + F(3, 5) - F(1, 7))
    margin = -F(1, 8) + F(1, 4)*F(14, 15)*F(13, 12) - F(1, 6)*F(5, 6)*k3_upper
    checks = {
        "e_upper_less_than_11_over_4": exp_upper < F(11, 4),
        "exp_11_over_10_partial_sum_exceeds_3": exp_11_10_lower > 3,
        "exp_4_over_5_upper_below_5_over_2": F(55, 24) < F(5, 2),
        "exp_9_over_7_upper_below_4": F(77, 20) < 4,
        "last_interval_exponent_below_2": F(169, 87) < 2,
        "e_squared_upper_below_8": F(121, 16) < 8,
        "k1_lower_equals_349_over_320": k1_lower == F(349, 320),
        "k1_lower_exceeds_13_over_12": k1_lower > F(13, 12),
        "k3_upper_equals_32_over_35": k3_upper == F(32, 35),
        "squared_jacobian_auxiliary_constant_below_1": F(243, 256) < 1,
        "full_mass_lower_bound_equals_1_over_1260": margin == F(1, 1260),
        "full_mass_lower_bound_positive": margin > 0,
        "finite_remainder_allocation": F(1, 1260) - F(4, 10080) == F(1, 2520),
        "signed_change_remainder_allocation": -F(1, 6) + F(4, 48) == -F(1, 12),
    }
    failures = [name for name, value in checks.items() if not value]
    result = {
        "status": "EXACT_ARITHMETIC_PASS" if not failures else "FAIL",
        "scope": "Finite rational inequalities in L891 only; analytic steps are in the lemma.",
        "values": {
            "e_series_upper": str(exp_upper),
            "exp_11_over_10_partial_sum": str(exp_11_10_lower),
            "k1_lower": str(k1_lower),
            "k3_upper": str(k3_upper),
            "model_mass_lower_bound": str(margin),
            "required_for_descent": "full mass < 0",
            "finite_mass_lower_bound_factor": "epsilon^3 * (abs(h_alpha)+abs(h_beta)) / (2520*(2*pi)^2)",
        },
        "checks": checks,
        "failures": failures,
        "unverified": [
            "Independent audit of L891's algebra, integration, compact Taylor bound and actual endpoint transfer.",
            "Existence of stationary actual-G data satisfying the clean strip and slope restrictions.",
            "Numerical values of the data-dependent constants in L891(23).",
        ],
    }
    path = Path(__file__).with_name("common-scale-exact-checks-79.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"{result['status']}: {len(checks)} rational checks; failures={len(failures)}")
    print(f"Analytic model lower bound={margin}; required for descent < 0")
    print("Finite analytic bound: epsilon^3*H/[2520*(2*pi)^2] > 0 under L891 hypotheses")
    print(f"Full arithmetic certificate: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
