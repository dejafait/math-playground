#!/usr/bin/env python3
"""Exact scalar checks for L562; not a verification of its analytic proof."""

import json
from fractions import Fraction
from pathlib import Path


def exact(value):
    value = Fraction(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def main():
    A, m, r = 2**20, 270, 256
    b = Fraction(1, 4)
    d, N = A - 1, m + 1
    epsilon = b / d
    series_ratio = 2 * r * epsilon
    bernoulli_loss = r * series_ratio
    beta = bernoulli_loss / (1 - bernoulli_loss)
    theta = 1 - beta
    checks = {
        "partition_length_within_real_alphabet": r <= m,
        "geometric_series_converges": 0 < series_ratio < 1,
        "bernoulli_loss_below_half": 0 < bernoulli_loss < Fraction(1, 2),
        "beta_exact": beta == Fraction(32768, 1015807),
        "relative_error_below_0033": beta < Fraction(33, 1000),
        "theta_exact_and_positive": theta == Fraction(983039, 1015807) > 0,
        "nonnegative_factorial_row_indices": N - r + 1 == 16,
        "causal_derivatives_below_edge_regularity": r - 1 == 255 <= N - 1,
        "bilateral_regularity_suffices": 2 * r - 2 == 510 <= 542,
    }
    failures = [name for name, passed in checks.items() if not passed]
    result = {
        "scope": "L562 exact scalar thresholds only; analytic proof unaudited",
        "fixed_parameters": {"A": A, "b": exact(b), "m": m, "r": r},
        "bounds": {
            "epsilon": exact(epsilon),
            "series_ratio": exact(series_ratio),
            "bernoulli_loss": exact(bernoulli_loss),
            "bernoulli_loss_required_upper_strict": exact(Fraction(1, 2)),
            "relative_error_upper": exact(beta),
            "relative_error_required_upper_strict": exact(1),
            "determinant_comparison_lower": exact(theta),
            "determinant_comparison_required_lower_strict": exact(0),
        },
        "checks": checks,
        "failures": failures,
        "unverified_by_script": [
            "Schur identities and all-partition dimension-ratio proof",
            "infinite Cauchy--Binet convergence and signs",
            "causal-factor transform and zero-extension regularity",
            "ordered Wronskian transfer and Andreief integral",
            "retained L561 density and negative-sign inputs",
        ],
    }
    output = Path(__file__).with_name("global-comparison-certificate.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Scalar checks: {len(checks) - len(failures)}/{len(checks)} passed")
    print(f"Relative error <= {beta}; required < 1")
    print(f"Determinant comparison >= {theta}; required > 0")
    print(f"Failures: {failures}")
    print(f"Certificate: {output}")
    print("The analytic proof is not verified by these scalar checks.")
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
