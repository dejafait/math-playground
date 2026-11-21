#!/usr/bin/env python3
"""Exact bound preflight for C033t; never evaluates an observable or quadrature."""
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import json


def encoded(value):
    if isinstance(value, F):
        return {"numerator": str(value.numerator),
                "denominator": str(value.denominator)}
    if isinstance(value, dict):
        return {key: encoded(item) for key, item in value.items()}
    return value


def least_cells(tolerance):
    square = F(1021, 384) / tolerance
    candidate = isqrt(square.numerator // square.denominator)
    if candidate * candidate * square.denominator < square.numerator:
        candidate += 1
    assert F(1021, 384 * candidate**2) <= tolerance
    assert candidate == 1 or F(1021, 384 * (candidate - 1)**2) > tolerance
    return candidate


epsilon = F(1, 2**112)
quad_allowance = epsilon / 2
term_budget = 10**7
coefficient_bound = F(2048, 255)
input_error = coefficient_bound * (2**73 + 2**82) * epsilon
input_reserve = F(1, 2**25)
arithmetic_reserve = F(1, 2**25)
cut = 60 * 3**48 * F(1, 2**128)
series = F(3**24 * 24**129 * 130, factorial(129) * 106)
lambda_tail = F(3**21 * 21**129 * 130, factorial(129) * 109)
omitted = lambda_tail + 2 * (cut + series)
conditional_total = omitted + input_error + arithmetic_reserve
required_total = F(1, 2**20)
curvature = 2 * (F(21, 4) + F(200, 2) + F(2400, 16))
at_budget = F(1021, 384 * term_budget**2)
minimum = least_cells(quad_allowance)
relaxed_minimum = least_cells(32 * quad_allowance)

checks = {
    "coefficient_bound_below_9": coefficient_bound < 9,
    "exp50_integer_majorant": 3**50 < 2**80,
    "exp44_integer_majorant": 3**45 < 2**72,
    "input_error_below_reserve": input_error < input_reserve,
    "omitted_below_2^-44": omitted < F(1, 2**44),
    "conditional_combined_error_passes": conditional_total < required_total,
    "curvature_identity": curvature == F(1021, 2),
    "certificate_fails_at_term_budget": at_budget > quad_allowance,
    "least_accepted_cells_exceeds_10^17": minimum > 10**17,
    "factor32_relaxation_still_exceeds_10^16": relaxed_minimum > 10**16,
}
assert all(checks.values()), checks

certificate = {
    "step": "2026-11-19-paired-scalar-preflight-1781",
    "scope": "Conditional scalar error allocation; explicit midpoint-bound failure only.",
    "analytic_inputs": "C033j/m/r/s; all external and unaudited-C033s qualifications retained.",
    "checks": checks,
    "error": {
        "uniform_scalar_tolerance": epsilon,
        "m_quadrature_allocation": quad_allowance,
        "coefficient_sum_upper_bound": coefficient_bound,
        "scalar_propagation_upper_bound": input_error,
        "final_arithmetic_allocation_unimplemented": arithmetic_reserve,
        "omitted_part_upper_bound": omitted,
        "conditional_combined_upper_bound": conditional_total,
        "required_combined_upper_bound": required_total,
    },
    "midpoint_branch": {
        "second_derivative_upper_bound": curvature,
        "error_bound_at_budget": at_budget,
        "error_bound_over_allocation_at_budget": at_budget / quad_allowance,
        "least_accepted_cells": minimum,
        "least_accepted_cells_factor32_relaxation": relaxed_minimum,
        "aggregate_term_budget": term_budget,
        "normalization_counted_once": True,
        "nested_costs_omitted_only_because_outer_branch_already_fails": True,
        "actual_error_lower_bound_claimed": False,
        "universal_algorithmic_lower_bound_claimed": False,
    },
    "precision": {"declared_bit_ceiling": 512, "numerical_implementation_verified": False},
    "observable_evaluated": False,
    "failures": {
        "midpoint_bound_exceeds_allocated_error_with_10^7_nodes": True,
        "overall_cost_precision_preflight_passed": False,
    },
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(encoded(certificate), indent=2) + "\n")
print("PASS: exact scalar propagation and conditional total-error allocation.")
print(f"Conditional error bound {float(conditional_total):.8g}; required {float(required_total):.8g}.")
print(f"FAIL: midpoint certificate at {term_budget} nodes = {float(at_budget):.8g}; allocated {float(quad_allowance):.8g}.")
print(f"Least nodes accepted by that certificate: {minimum}; budget {term_budget}.")
print("512-bit evaluation unverified; no observable or quadrature evaluated.")
print(f"Certificate: {output.relative_to(Path.cwd())}")
