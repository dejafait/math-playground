#!/usr/bin/env python3
"""Audit C033t's saved rational certificate; no observable is evaluated."""
from fractions import Fraction as F
from pathlib import Path
import json


def encode(value):
    if isinstance(value, F):
        return {"numerator": str(value.numerator), "denominator": str(value.denominator)}
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    return value


def decode(value):
    return F(int(value["numerator"]), int(value["denominator"]))


def term129(base):
    term = F(1)
    for j in range(1, 130):
        term *= F(base, j)
    return term


def least_by_bisection(tolerance, curvature_coefficient):
    def accepts(n):
        return curvature_coefficient <= tolerance * n * n

    lo, hi = 0, 1
    while not accepts(hi):
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if accepts(mid):
            hi = mid
        else:
            lo = mid
    return hi


source = Path(__file__).with_name("paired_scalar_preflight_1781.json")
saved = json.loads(source.read_text())
checks = {}


def check(name, value):
    checks[name] = bool(value)


epsilon = F(1, 2**112)
quadrature = epsilon / 2
budget = 10**7
# Sum four absolute coefficients using log(2)<1, independently of 2048/255.
coefficient = 4 * (F(16, 15) + F(16, 17))
scalar = coefficient * (2**73 + 2 * 2**81) * epsilon
reserve = F(1, 2**25)
cut = 2 * 30 * F(1, 2**128) * 3**48
series = 3**24 * term129(24) / (1 - F(24, 130))
lambda_tail = 3**21 * term129(21) / (1 - F(21, 130))
omitted = lambda_tail + 2 * (cut + series)
total = omitted + scalar + reserve
statement_total = omitted + 2 * reserve
required = F(1, 2**20)
curvature = 2 * (F(21, 4) + 2 * F(1, 4) * 200 + F(1, 16) * 2400)
midpoint_coefficient = F(1, 2)**3 * curvature / 24
at_budget = midpoint_coefficient / budget**2
minimum = least_by_bisection(quadrature, midpoint_coefficient)
relaxed = least_by_bisection(32 * quadrature, midpoint_coefficient)

expected_error = {
    "uniform_scalar_tolerance": epsilon,
    "m_quadrature_allocation": quadrature,
    "coefficient_sum_upper_bound": coefficient,
    "scalar_propagation_upper_bound": scalar,
    "final_arithmetic_allocation_unimplemented": reserve,
    "omitted_part_upper_bound": omitted,
    "conditional_combined_upper_bound": total,
    "required_combined_upper_bound": required,
}
check("complete_saved_error_key_set", set(saved["error"]) == set(expected_error))
for key, expected in expected_error.items():
    check("saved_error_" + key, decode(saved["error"][key]) == expected)

expected_midpoint = {
    "second_derivative_upper_bound": curvature,
    "error_bound_at_budget": at_budget,
    "error_bound_over_allocation_at_budget": at_budget / quadrature,
    "least_accepted_cells": minimum,
    "least_accepted_cells_factor32_relaxation": relaxed,
    "aggregate_term_budget": budget,
    "normalization_counted_once": True,
    "nested_costs_omitted_only_because_outer_branch_already_fails": True,
    "actual_error_lower_bound_claimed": False,
    "universal_algorithmic_lower_bound_claimed": False,
}
check("complete_saved_midpoint_key_set", set(saved["midpoint_branch"]) == set(expected_midpoint))
for key, expected in expected_midpoint.items():
    found = saved["midpoint_branch"][key]
    if isinstance(expected, F):
        found = decode(found)
    check("saved_midpoint_" + key, found == expected)

original_assertions = {
    "coefficient_bound_below_9": coefficient < 9,
    "exp50_integer_majorant": 3**50 < 2**80,
    "exp44_integer_majorant": 3**45 < 2**72,
    "input_error_below_reserve": scalar < reserve,
    "omitted_below_2^-44": omitted < F(1, 2**44),
    "conditional_combined_error_passes": total < required,
    "curvature_identity": curvature == F(1021, 2),
    "certificate_fails_at_term_budget": at_budget > quadrature,
    "least_accepted_cells_exceeds_10^17": minimum > 10**17,
    "factor32_relaxation_still_exceeds_10^16": relaxed > 10**16,
}
check("complete_saved_check_key_set", set(saved["checks"]) == set(original_assertions))
for key, result in original_assertions.items():
    check("recomputed_" + key, result)
    check("saved_assertion_" + key, saved["checks"][key] == result)

check("loose_coefficient_scalar_bound", 9 * (2**73 + 2**82) < 2**87)
check("statement_total_below_2^-23", statement_total < F(1, 2**23))
check("statement_total_below_required", statement_total < required)
check("midpoint_coefficient", midpoint_coefficient == F(1021, 384))

threshold = 1021 * 2**113
bracket = {
    "least_accepted_cells": minimum,
    "previous_integer_deficit": threshold - 384 * (minimum - 1)**2,
    "accepted_integer_surplus": 384 * minimum**2 - threshold,
    "deficit_at_10^17": threshold - 384 * (10**17)**2,
    "budget_deficit": threshold - 384 * budget**2,
}
check("previous_integer_fails", bracket["previous_integer_deficit"] > 0)
check("accepted_integer_passes", bracket["accepted_integer_surplus"] >= 0)
check("10^17_integer_fails", bracket["deficit_at_10^17"] > 0)
check("budget_integer_fails", bracket["budget_deficit"] > 0)
check("relaxed_previous_fails", midpoint_coefficient > 32 * quadrature * (relaxed - 1)**2)
check("relaxed_accepted_passes", midpoint_coefficient <= 32 * quadrature * relaxed**2)
check("saved_precision_scope", saved["precision"] == {
    "declared_bit_ceiling": 512, "numerical_implementation_verified": False})
check("saved_no_evaluation", saved["observable_evaluated"] is False)
check("saved_failure_scope", saved["failures"] == {
    "midpoint_bound_exceeds_allocated_error_with_10^7_nodes": True,
    "overall_cost_precision_preflight_passed": False})

failures = [name for name, result in checks.items() if not result]
certificate = {
    "step": "2026-11-19-paired-scalar-critical-audit-1789",
    "scope": "Exact arithmetic audit only; analytic proof and source qualifications remain canonical in C033t.",
    "source_certificate": str(source.relative_to(Path.cwd())),
    "checks": checks,
    "audit_failures": failures,
    "reconstructed_error": expected_error,
    "statement_total": statement_total,
    "midpoint": expected_midpoint,
    "integer_bracket": bracket,
    "claimed_numeric_failure": "The specified sufficient midpoint allowance fails the declared term budget.",
    "observable_evaluated": False,
    "precision_verified": False,
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(encode(certificate), indent=2) + "\n")
print(f"Audit checks: {len(checks) - len(failures)}/{len(checks)} passed; failures: {failures}.")
print(f"Conditional statement allowance: {float(statement_total):.12g}; required: {float(required):.12g}.")
print(f"Scheme FAIL: midpoint allowance at {budget} nodes: {float(at_budget):.12g}; required: {float(quadrature):.12g}.")
print(f"Least accepted cells: {minimum}; term budget: {budget}; relaxed-by-32: {relaxed}.")
print("No observable evaluation, actual-error lower bound or512-bit implementation verified.")
print(f"Full audit certificate: {output.relative_to(Path.cwd())}")
if failures:
    raise SystemExit(1)
