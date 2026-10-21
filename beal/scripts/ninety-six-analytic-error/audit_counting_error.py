#!/usr/bin/env python3
"""Independent exact audit of L057's certificate, without importing its producer."""

import json
from fractions import Fraction
from math import prod
from pathlib import Path


def power(base, exponent):
    return prod([base] * exponent)


def main():
    folder = Path(__file__).resolve().parent
    original = json.loads((folder / "counting-error-certificate.json").read_text())
    # These are imported L051 field/order inputs, not computed field discriminants.
    n = 36
    d12 = -307926804295486824275116956724109113198514489839954427904
    d3 = -41229056
    cap = power(10, 6)
    lower = prod([3] * 30 + [11] * 33)
    upper = abs(prod([d12] * 3 + [d3] * 12))
    exponential = Fraction(282, 10) * n + 5
    cancelled = exponential - (n - 1)
    base_power = Fraction(5 * (n + 1), 2)
    exp_floor = cancelled.numerator // cancelled.denominator
    base_floor = base_power.numerator // base_power.denominator
    q = prod([10] + [2] * exp_floor + [n + 1] * base_floor
             + [2 * (n - 1)] * (n - 1))
    differences = {
        "discriminant_interval_nonempty": upper - lower,
        "D0_gt_3_pow_100": lower - power(3, 100),
        "cap_squared_lt_10_pow_37": power(10, n + 1) - cap * cap,
        "ratio_lower_gt_10_pow_506": q - power(10, 506),
        "ratio_lower_gt_required_one_half": q + q - 1,
    }
    expected = {
        "inputs": {"degree": n, "X_cap": cap, "d12": d12, "d3": d3,
                   "D0": lower, "Dmax": upper},
        "exponents": {
            "counting_exp_numerator_over_five": int(exponential * 5),
            "upper_residue_exp": n - 1,
            "cancelled_exp_numerator_over_five": int(cancelled * 5),
            "power_of_37_numerator_over_two": int(base_power * 2),
            "power_of_70": n - 1,
            "remaining_log_power": n - (n - 1),
        },
        "uniform_comparison": {
            "domain": "D0 <= D <= Dmax, 0 < X <= 10^6",
            "E_over_U_strict_integer_lower_bound": q,
            "E_over_U_strict_power_of_ten_lower_bound": "10^506",
            "necessary_E_over_U_upper_bound": {
                "numerator": 1, "denominator": 2, "strict": True},
            "conclusion": "No raw symmetric Sunley interval in this domain has positive endpoints with ratio below two.",
            "actual_discriminant_residue_count_and_error": "not computed",
        },
        "exact_positive_differences": differences,
        "failures": [],
        "proof_scope": "Integer premises only; L057 proves the transcendental inequalities and interval implication.",
    }
    checks = {"complete_schema": set(original) == set(expected)}
    checks.update({"complete_field_" + key: original.get(key) == value
                   for key, value in expected.items()})
    checks.update({"positive_" + key: value > 0
                   for key, value in differences.items()})
    checks.update({
        "counting_exponent_exact": exponential == Fraction(5101, 5),
        "cancelled_exponent_exact": cancelled == Fraction(4926, 5),
        "strict_exponential_floor": exp_floor == 985 and cancelled > exp_floor,
        "strict_base_floor": base_floor == 92 and base_power > base_floor,
        "positive_domain": upper >= lower > 1 and cap > 0,
    })
    failures = [key for key, passed in checks.items() if not passed]
    result = {
        "method": "Fraction exponents and repeated integer products; original producer not imported or run.",
        "source_certificate": original,
        "independent_expected": expected,
        "checks": checks,
        "failures": failures,
        "scope": "Exact certificate premises only; L057 contains the separate all-real-X and interval proof audit. L051-L052 field facts remain imported.",
    }
    output = folder / "counting-error-audit-certificate.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print("Certified E/U > 10^506; required E/U < 1/2 for 0 < X <= 10^6.")
    print(f"Complete original fields checked: {len(expected)}; checks: {len(checks)}; failures: {len(failures)}.")
    print("Actual error, ideal count and residue: not computed.")
    print(f"Certificate: {output.relative_to(Path.cwd())}")
    if failures:
        print("Failed checks: " + ", ".join(failures))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
