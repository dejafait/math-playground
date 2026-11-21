"""Exact rational margins for L698; not an analytic proof verification."""

from fractions import Fraction as Q
import json
from pathlib import Path


def rational(value):
    value = Q(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def main():
    d, R, A = Q(5, 4), Q(11, 8), Q(27, 10)
    U, K2 = R * R, Q(353, 200)
    pole_radius_squared = Q(1, 4) + (U + R * d) / K2
    checks = []

    def check(name, actual, relation, required):
        actual, required = Q(actual), Q(required)
        passed = {
            "<": actual < required,
            "<=": actual <= required,
            "=": actual == required,
            ">": actual > required,
            ">=": actual >= required,
        }[relation]
        checks.append({
            "name": name,
            "actual": rational(actual),
            "relation": relation,
            "required": rational(required),
            "passed": passed,
        })

    check("rho_squared_identity", K2 / U, "=", Q(2824, 3025))
    check("rho_squared_strictly_below_one", K2 / U, "<", 1)
    check("beta_real_part_lower_bound", d + R * Q(4, 9), "=", Q(67, 36))
    check("beta_modulus_upper_bound", d + 4 * R, "=", Q(27, 4))
    check("extra_variation_mass_upper_bound", Q(27, 4) / Q(67, 36), "<", 6)
    check("small_disk_prefactor_denominator", R + d / 4, "=", Q(27, 16))
    check("positive_second_moment_upper_bound", (A / d) ** 2 * Q(288, 225), "<", 6)
    check("resolvent_inverse_y_coefficient", 7 * Q(27, 4), "<", 48)
    check("two_factor_tail_coefficient", 48 * d, "=", 60)
    check("omitted_shifted_ordinate_lower_bound", Q(9, 20) - A / (15 * 8), ">", Q(2, 5))
    check("complete_tail_coefficient", Q(19200) / (9 * A * A), "<", 300)
    # 2q-1/2 - (12q+3)/10 = (4/5)(q-1)+0 for every q>=1.
    check("endpoint_index_margin_at_q_one", 2 - Q(1, 2) - Q(15, 10), "=", 0)
    check("endpoint_index_margin_slope", 2 - Q(12, 10), ">", 0)
    check("pole_radius_squared_identity", pole_radius_squared, "=", Q(6481, 2824))
    check("all_spatial_poles_outside_151_over_100", pole_radius_squared, ">", Q(151, 100) ** 2)
    check("outer_denominator_lower_bound", d * (Q(151, 100) - Q(301, 200)), "=", Q(1, 160))
    check("interpolation_inner_target_order", Q(1, 4), "<", Q(3, 2))
    check("interpolation_target_outer_order", Q(3, 2), "<", Q(301, 200))
    check("interpolation_weight_numerator_ratio", Q(301, 200) / Q(3, 2), "=", Q(301, 300))
    check("interpolation_weight_denominator_ratio", Q(301, 200) / Q(1, 4), "=", Q(301, 50))
    check("retained_positive_comb_rate", Q(7, 40) - Q(1, 40), "=", Q(3, 20))
    failures = [item["name"] for item in checks if not item["passed"]]
    certificate = {
        "step_id": "2026-11-03-centered-gap-complete-spatial-124",
        "scope": "Exact rational margins only; no verification of the analytic proof or effective gap, arc, rate or onset.",
        "constants": {key: rational(value) for key, value in {
            "d": d, "R": R, "U": U, "A": A, "K_squared": K2,
        }.items()},
        "checks": checks,
        "failures": failures,
        "passed": not failures,
        "unchecked": [
            "The assumed fixed centered-gap profile and its local existence proofs.",
            "Complex measure domination, concentration, comb limits and interval pairing.",
            "Uniform arc choice and applicability of Hadamard's three-circles theorem.",
            "The symbolic positive-rate allocation and the final full-polynomial argument.",
        ],
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Rational checks: {len(checks) - len(failures)}/{len(checks)} passed; failures: {failures}")
    for name in (
        "complete_tail_coefficient",
        "all_spatial_poles_outside_151_over_100",
        "outer_denominator_lower_bound",
    ):
        item = next(item for item in checks if item["name"] == name)
        left, right = item["actual"], item["required"]
        print(f"{name}: {left['numerator']}/{left['denominator']} {item['relation']} {right['numerator']}/{right['denominator']}")
    print(f"Certificate: {output}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
