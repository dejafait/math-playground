#!/usr/bin/env python3
"""Exact constants for C645x; analytic contour bounds are in the lemma.

No sampled contour, floating-point optimization, or angular screen is used.
The output contains every rational log bound and inequality checked here.
"""

from fractions import Fraction as F
import json
from pathlib import Path


def rational(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def log_bounds(q, terms=64):
    assert q > 1
    v = (q - 1) / (q + 1)
    lower = 2 * sum((v ** (2 * k + 1) / (2 * k + 1) for k in range(terms)), F(0))
    remainder = 2 * v ** (2 * terms + 1) / ((2 * terms + 1) * (1 - v * v))
    return lower, lower + remainder


def linear_bounds(terms, bounds):
    lower, upper = F(0), F(0)
    for coefficient, name in terms:
        lo, hi = bounds[name]
        lower += coefficient * (lo if coefficient >= 0 else hi)
        upper += coefficient * (hi if coefficient >= 0 else lo)
    return lower, upper


def main():
    log_args = {
        "11/10": F(11, 10), "201/121": F(201, 121), "9/5": F(9, 5),
        "275/248": F(275, 248), "3025/1041": F(3025, 1041), "31/6": F(31, 6),
        "11/9": F(11, 9), "121/49": F(121, 49), "9": F(9),
    }
    logs = {name: log_bounds(q) for name, q in log_args.items()}
    expressions = {
        "lambda": [(F(1), "11/10"), (F(201, 80), "201/121"), (-F(9, 4), "9/5")],
        "kappa_31_25": [(F(1), "275/248"), (F(1041, 1984), "3025/1041"), (-F(6, 25), "31/6")],
        "kappa_9_8": [(F(1), "11/9"), (F(49, 72), "121/49"), (-F(1, 8), "9")],
    }
    values = {name: linear_bounds(expr, logs) for name, expr in expressions.items()}
    scale = 10 ** 12
    rounded = {name: (F((lo * scale).__floor__(), scale), F((hi * scale).__ceil__(), scale)) for name, (lo, hi) in values.items()}
    rounding_checks = {name: rlo <= values[name][0] <= values[name][1] <= rhi for name, (rlo, rhi) in rounded.items()}
    R, d, h = F(11, 8), F(5, 4), F(1, 8)
    U, ymin, ymax = R * R, F(53, 100), F(27, 50)
    gamma, required = F(251, 8000), F(1, 32)
    checks = {}

    def check(name, lhs, relation, rhs):
        passed = {"<": lhs < rhs, "<=": lhs <= rhs, ">": lhs > rhs, "=": lhs == rhs}[relation]
        checks[name] = {"lhs": rational(lhs), "relation": relation, "rhs": rational(rhs), "pass": passed}

    check("anchor_rate_lower", rounded["lambda"][0], ">", F(47, 1000))
    check("horizontal_radial_loss", rounded["kappa_31_25"][1], "<", F(7, 25))
    check("right_radial_loss", rounded["kappa_9_8"][1], "<", F(3, 5))
    check("lattice_pole_clearance", d * d + ymax * ymax, "<", F(273, 200) ** 2)
    check("horizontal_min_radius", F(9, 8) ** 2 + ymin * ymin, ">", F(31, 25) ** 2)
    check("right_spatial_radius", F(9, 8) ** 2 + ymax * ymax, "<", U)
    check("left_gaussian_spatial_damping", 1 - 1 / U, ">", F(0))
    check("horizontal_inside_margin", ymin * ymin - F(7, 25), "=", F(9, 10000))
    check("right_kernel_margin_using_pi_gt_3", F(3, 4) - F(3, 5), "=", F(3, 20))
    check("conservative_contour_rate", F(47, 1000) - h * h, "=", gamma)
    check("rate_gap", gamma - required, "=", F(1, 8000))
    check("perimeter_norm_constant", (4 * ymax + 4 * h) * 2 / R, "<", F(4))
    check("mass_ratio_for_n_ge_400", F(1, 400) + F(1, 5), "<", F(1, 3))
    check("height_lower_for_n_ge_100", ymax - F(1, 100), "=", ymin)
    check("kernel_denominator_for_n_ge_100", F(3 * 100, 4), ">", F(1))
    check("left_rectangle_coordinate", d + h, "=", R)
    check("right_rectangle_coordinate", d - h, "=", F(9, 8))

    failures = [name for name, item in checks.items() if not item["pass"]]
    failures.extend("rounding_" + name for name, passed in rounding_checks.items() if not passed)
    output = {
        "status": "PASS" if not failures else "FAIL",
        "scope": "Exact constants only. Complete uniform contour proof and fractional-residue qualification are in C645x.",
        "log_series_terms": 64,
        "log_bounds": {name: {"argument": rational(log_args[name]), "lower": rational(lo), "upper": rational(hi)} for name, (lo, hi) in logs.items()},
        "expressions": {name: [{"coefficient": rational(c), "log": q} for c, q in expr] for name, expr in expressions.items()},
        "value_bounds": {name: {"lower": rational(lo), "upper": rational(hi)} for name, (lo, hi) in values.items()},
        "rounded_value_bounds": {name: {"lower": rational(lo), "upper": rational(hi), "exact_containment": rounding_checks[name]} for name, (lo, hi) in rounded.items()},
        "readable_bounds": {name: {"lower_decimal_preview": float(lo), "upper_decimal_preview": float(hi)} for name, (lo, hi) in values.items()},
        "required_rate": rational(required), "proved_conservative_rate": rational(gamma),
        "checks": checks, "failures": failures,
        "not_established": ["admissible integer-residue countersequence", "full angular Hankel upper bound", "Xi realization", "independent proof audit"],
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    total_checks = len(checks) + len(rounding_checks)
    print(f"{output['status']}: {total_checks - len(failures)}/{total_checks} exact constant checks")
    print(f"Proved rate {gamma}; required rate {required}; gap {gamma - required}")
    print(f"Failures: {failures}; full certificate: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
