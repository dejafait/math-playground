#!/usr/bin/env python3
"""Exact arithmetic for C467d; analytic premises are proved in the lemma."""

import json
from fractions import Fraction as Q
from pathlib import Path


def rational(value):
    value = Q(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


checks = []


def check(name, actual, relation, required):
    actual, required = Q(actual), Q(required)
    passed = {
        "=": actual == required,
        ">": actual > required,
        "<": actual < required,
        ">=": actual >= required,
        "<=": actual <= required,
    }[relation]
    checks.append({
        "name": name,
        "actual": rational(actual),
        "relation": relation,
        "required": rational(required),
        "passed": passed,
    })


a, horizon, c = Q(1, 16), Q(1, 1920), Q(15, 64)
norm_sq = 3 * a * a
background_sq = 40**2 * norm_sq
pair_sq_sum = 3 * norm_sq
pair_inverse_sum_floor = 9 / pair_sq_sum
decay = 2 * pair_inverse_sum_floor - 120 - 3 * background_sq
k0, inner_scale = 10**6, Q(999, 1000)
maximum_scaled_coordinate = inner_scale / (1 - Q(1, k0))
bump_exponent_cap = Q(3000, k0)
bump_floor = 1 - bump_exponent_cap
phase_floor = Q(97, 100)
boundary_loss_cap = 2 * Q(9, 1000)
initial_ratio_floor = phase_floor * bump_floor * (1 - boundary_loss_cap)
capacity_ratio_ceiling = 1 / (1 + 335 * horizon / 2)
initial_threshold, capacity_threshold = Q(47, 50), Q(23, 25)

check("norm_squared", norm_sq, "=", Q(3, 256))
check("radial_derivative_at_largest_initial_level", -12 + 80 * norm_sq, "<", 0)
check("background_squared", background_sq, "=", Q(75, 4))
check("pair_squared_distance_sum", pair_sq_sum, "=", Q(9, 256))
check("inverse_pair_sum_floor", pair_inverse_sum_floor, "=", 256)
check("weighted_decay_rate", decay, "=", Q(1343, 4))
check("chosen_decay_rate", decay, ">", 335)
check("inner_cube_inside_initial_support", maximum_scaled_coordinate, "<", 1)
check("bump_denominator_floor", 1 - maximum_scaled_coordinate**2, ">", Q(1, 1000))
check("bump_exponent_cap", bump_exponent_cap, "=", Q(3, 1000))
check("bump_floor", bump_floor, "=", Q(997, 1000))
check("phase_floor", 1 - c*c/2, ">", phase_floor)
check("geometric_exponential_majorant_domain", 2*c, "<", 1)
check("geometric_exponential_majorant", 1 / (1 - 2*c), "=", Q(32, 17))
check("exponential_ratio_cap", 1 / (1 - 2*c), "<", 2)
check("homogeneous_boundary_loss", 1 - inner_scale**9, "<=", Q(9, 1000))
check("initial_ratio_floor_value", initial_ratio_floor, "=", Q(47484119, 50000000))
check("initial_mass_threshold", initial_ratio_floor, ">", initial_threshold)
check("capacity_ratio_value", capacity_ratio_ceiling, "=", Q(768, 835))
check("capacity_threshold", capacity_ratio_ceiling, "<", capacity_threshold)
check("threshold_separation", initial_threshold - capacity_threshold, "=", Q(1, 50))
check("strict_separation", initial_ratio_floor - capacity_ratio_ceiling, ">", 0)
check("positive_measure_time_interval", horizon / 2, ">", 0)

failures = [item["name"] for item in checks if not item["passed"]]
certificate = {
    "step_id": "2026-11-15-actual-h-chart-exhaustion-mass-deficit-1009",
    "lemma": "lemmas/C467d-actual-h-chart-exhaustion-mass-deficit.md",
    "scope": "Exact finite rational inequalities only; no analytic or independent proof audit.",
    "analytic_premises_not_verified_by_script": [
        "Audited actual background bound and radial contraction on original survivors.",
        "Full real exterior-growth estimate, singular-force inequality and complex determinant comparison.",
        "Full survivor phase cone and complete time-dependent representative balance.",
        "Initial domination, homogeneity, and the elementary exponential/cosine inequalities used in the proof.",
        "All-survivor integration and per-test almost-everywhere raw identification.",
    ],
    "parameters": {"a": rational(a), "T0": rational(horizon), "k0": k0,
                   "inner_scale": rational(inner_scale), "phase_budget": rational(c)},
    "bounds": {
        "decay_rate_actual_lower": rational(decay),
        "decay_rate_used": rational(335),
        "initial_mass_ratio_lower": rational(initial_ratio_floor),
        "initial_mass_ratio_required": rational(initial_threshold),
        "capacity_ratio_upper": rational(capacity_ratio_ceiling),
        "capacity_ratio_required": rational(capacity_threshold),
        "threshold_gap": rational(initial_threshold - capacity_threshold),
    },
    "checks": checks,
    "failures": failures,
    "all_passed": not failures,
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
print(f"Rational checks: {len(checks) - len(failures)}/{len(checks)} passed; failures: {failures}")
print(f"Decay: {decay} > 335; k0: {k0}")
print(f"Initial/W > {initial_ratio_floor} > {initial_threshold}; capacity/W <= {capacity_ratio_ceiling} < {capacity_threshold}")
print(f"Required threshold gap: {initial_threshold - capacity_threshold}")
print(f"Full certificate: {path.relative_to(Path.cwd())}")
if failures:
    raise SystemExit(1)
