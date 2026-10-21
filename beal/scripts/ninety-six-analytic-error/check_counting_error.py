#!/usr/bin/env python3
"""Exact integer premises for L057; no ideal enumeration or floating point."""

import json
from pathlib import Path


def main():
    degree = 36
    cap = 10**6
    d12 = -307926804295486824275116956724109113198514489839954427904
    d3 = -41229056
    d0 = 3**30 * 11**33
    dmax = abs(d12)**3 * abs(d3)**12
    ratio_lower = 10 * 2**985 * 37**92 * 70**35
    comparisons = {
        "discriminant_interval_nonempty": dmax - d0,
        "D0_gt_3_pow_100": d0 - 3**100,
        "cap_squared_lt_10_pow_37": 10**37 - cap**2,
        "ratio_lower_gt_10_pow_506": ratio_lower - 10**506,
        "ratio_lower_gt_required_one_half": 2 * ratio_lower - 1,
    }
    failures = [name for name, difference in comparisons.items() if difference <= 0]
    result = {
        "inputs": {
            "degree": degree,
            "X_cap": cap,
            "d12": d12,
            "d3": d3,
            "D0": d0,
            "Dmax": dmax,
        },
        "exponents": {
            "counting_exp_numerator_over_five": 141 * degree + 25,
            "upper_residue_exp": degree - 1,
            "cancelled_exp_numerator_over_five": 141 * degree + 25 - 5 * (degree - 1),
            "power_of_37_numerator_over_two": 5 * (degree + 1),
            "power_of_70": degree - 1,
            "remaining_log_power": degree - (degree - 1),
        },
        "uniform_comparison": {
            "domain": "D0 <= D <= Dmax, 0 < X <= 10^6",
            "E_over_U_strict_integer_lower_bound": ratio_lower,
            "E_over_U_strict_power_of_ten_lower_bound": "10^506",
            "necessary_E_over_U_upper_bound": {"numerator": 1, "denominator": 2, "strict": True},
            "conclusion": "No raw symmetric Sunley interval in this domain has positive endpoints with ratio below two.",
            "actual_discriminant_residue_count_and_error": "not computed",
        },
        "exact_positive_differences": comparisons,
        "failures": failures,
        "proof_scope": "Integer premises only; L057 proves the transcendental inequalities and interval implication.",
    }
    assert result["exponents"] == {
        "counting_exp_numerator_over_five": 5101,
        "upper_residue_exp": 35,
        "cancelled_exp_numerator_over_five": 4926,
        "power_of_37_numerator_over_two": 185,
        "power_of_70": 35,
        "remaining_log_power": 1,
    }
    path = Path(__file__).with_name("counting-error-certificate.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print("Uniform certified E/U > 10^506; required E/U < 1/2.")
    print("Raw symmetric interval feasibility: FAIL throughout 0 < X <= 10^6.")
    print(f"Arithmetic failures: {len(failures)}; actual ideal counts/errors: not computed.")
    print(f"Certificate: {path.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
