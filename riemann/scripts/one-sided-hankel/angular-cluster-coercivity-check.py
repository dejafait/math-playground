#!/usr/bin/env python3
"""Exact constant checks for L647; not an analytic-proof verifier."""

from fractions import Fraction as Q
import json
from pathlib import Path


def rational(value):
    value = Q(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


checks = []


def check(name, actual, relation, required):
    actual, required = Q(actual), Q(required)
    passed = {
        "<": actual < required,
        "<=": actual <= required,
        ">": actual > required,
        ">=": actual >= required,
        "=": actual == required,
    }[relation]
    checks.append({
        "name": name,
        "actual": rational(actual),
        "relation": relation,
        "required": rational(required),
        "passed": passed,
    })


d, R, eta, epsilon = Q(5, 4), Q(11, 8), Q(1, 100), Q(1, 10000)
U = R * R
strip_radius = d + Q(1, 100)
check("strip_radius", strip_radius, "=", Q(63, 50))
check("grid_distance", d - 1, ">=", Q(1, 4))
check("denominator_clearance", U - strip_radius, ">", Q(5, 8))
check("logarithmic_derivative_bound", 4 + Q(8, 5), "<", 6)
check("second_derivative_bound", 16 + Q(64, 25), "<", 20)
check("first_real_part_bound", -(d - Q(1, 4)) / (d + Q(1, 4))**2,
      "=", Q(-4, 9))
check("second_real_part_bound", Q(1, 4) / (U - d / 4), "=", Q(16, 101))
check("short_interval_real_part", Q(-4, 9) + Q(16, 101), "<", Q(-1, 4))
check("integrated_real_part", Q(-1, 4) * Q(1, 4), "=", Q(-1, 16))
check("phase_derivative_sign", Q(-1, 16) + 20 * epsilon, "<", Q(-1, 32))
check("positive_imaginary_numerator_1", U - d*d, ">", Q(1, 4))
check("positive_imaginary_numerator_2", U - Q(1, 4), ">", Q(3, 2))
check("positive_imaginary_denominator_1", d*d + Q(1, 4), "<", 2)
check("positive_imaginary_denominator_2", U*U + d*d/4, "<", 5)
imag_integrand_lower = Q(1, 4) * Q(1, 4) * Q(3, 2) / (2 * 5)
check("imaginary_integrand_lower", imag_integrand_lower, "=", Q(3, 320))
imag_integral_lower = imag_integrand_lower * Q(1, 4)
check("imaginary_integral_lower", imag_integral_lower, "=", Q(3, 1280))
profile_lower = epsilon * imag_integral_lower - 10 * epsilon**2
check("profile_lower_exact", profile_lower, "=", Q(43, 320000000))
check("positive_profile_threshold", profile_lower, ">", Q(1, 10000000))
check("holomorphic_inner_radius", strip_radius / U, "<", Q(3, 4))
check("holomorphic_outer_radius", d, ">", Q(6, 5))
check("pole_clearance", strip_radius, "<", R - eta)
check("spatial_kernel_clearance", R - strip_radius, ">", Q(1, 10))
check("census_onset_at_six", 1 + Q(6, 6), "<=", Q(6, 3))
check("anchor_squared_norm", 1 / (U - d*d), "=", Q(64, 21))

failures = [entry["name"] for entry in checks if not entry["passed"]]
certificate = {
    "lemma": "L647",
    "scope": "Exact rational constants only; the analytic proof is in the canonical lemma.",
    "checks": checks,
    "failures": failures,
    "summary": {
        "passed": len(checks) - len(failures),
        "total": len(checks),
        "profile_lower_bound": rational(profile_lower),
        "required_positive_profile_bound": rational(Q(1, 10000000)),
        "operator_target_exponent": rational(Q(1, 32)),
        "full_energy_target_exponent": rational(Q(1, 16)),
        "analytic_claims_not_computationally_verified": [
            "Finite maximizer set and positive exponential-polynomial construction.",
            "Uniform response limits, angular concentration, and integerized admissibility.",
            "E_n/D_n tends to zero while both root energies have positive rate F_*.",
        ],
    },
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"L647 rational checks: {len(checks)-len(failures)}/{len(checks)} passed.")
print(f"Profile lower bound: {profile_lower} > 1/10000000; "
      "detector target exponent: 1/32 (energy 1/16), unresolved.")
print(f"Failures: {failures}")
print(f"Certificate: {path}")
raise SystemExit(bool(failures))
