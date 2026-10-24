#!/usr/bin/env python3
"""Exact finite radius checks for L456; no zeta-value verification."""

from fractions import Fraction
import json
from pathlib import Path


def ratio(value):
    return {"numerator": value.numerator, "denominator": value.denominator}


def main():
    r0, r1, r2, r3 = (Fraction(n, 256) for n in (255, 273, 284, 286))
    boundary, endpoint, center = Fraction(7, 8), Fraction(15, 16), Fraction(2)
    rho = Fraction(1, 256)
    # Polynomial coefficients in ascending powers of d=b-1.
    midpoint_square = [Fraction(1, 256), Fraction(1, 8), Fraction(1)]
    product = [Fraction(0), Fraction(1, 8), Fraction(1)]
    difference = [a - b for a, b in zip(midpoint_square, product)]
    checks = {
        "ordered_positive_radii": 0 < r0 < r1 < r2 < r3,
        "outer_disk_strictly_right_of_boundary": center - r3 > boundary,
        "inner_disk_strictly_right_of_one": center - r0 > 1,
        "complete_endpoint_cauchy_circle_fits": center - endpoint + rho <= r1,
        "explicit_exponent_strictly_below_two_thirds": r1**3 < r0 * r2**2,
        "explicit_exponent_strictly_above_one_half": r1**2 > r0 * r2,
        "all_center_polynomial_difference_is_positive_constant": difference
        == [Fraction(1, 256), Fraction(0), Fraction(0)],
    }
    failures = [name for name, passed in checks.items() if not passed]
    report = {
        "scope": "Exact rational disk checks only; analytic proof is in L456.",
        "radii": [ratio(v) for v in (r0, r1, r2, r3)],
        "boundary": ratio(boundary),
        "endpoint": ratio(endpoint),
        "cauchy_radius": ratio(rho),
        "exponent_checks": {
            "cubic_left": 273**3,
            "cubic_right": 255 * 284**2,
            "square_left": 273**2,
            "square_right": 255 * 284,
            "general_center_polynomial_difference": [ratio(v) for v in difference],
        },
        "checks": checks,
        "failures": failures,
        "freezing_threshold": {
            "available_derivative_power": ratio(Fraction(2, 3)),
            "required_sufficient_fixed_power": "strictly less than 1/2",
            "available_M_over_sqrt_r_power": ratio(Fraction(1, 6)),
            "fixed_center_interpolation_exponent": "strictly greater than 1/2",
            "little_o_established": False,
            "actual_derivative_or_sum_failure_established": False,
        },
    }
    path = Path(__file__).resolve().with_name("fixed-circle-threshold-certificate.json")
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(f"{'PASS' if not failures else 'FAIL'}: {len(checks)} exact radius/polynomial checks")
    print("Available derivative power: 2/3; sufficient fixed power: <1/2.")
    print("Fixed-center exponent: >1/2; relative freezing: NOT ESTABLISHED.")
    print(f"Failures: {failures}; certificate: {path.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
