"""Exact cost preflight for the approved dictionary1570 calculation.

This checks consequences of C032w's stated *bounds*, not actual kernel
errors, numerical complexity lower bounds for other methods, or RH.
No optimizer solve or unprovided zero-coordinate input is used.
"""
from fractions import Fraction as Q
from pathlib import Path
import json


def exp_lower(x, degree):
    term = Q(1)
    total = term
    for n in range(1, degree + 1):
        term *= x / n
        total += term
    return total


checks = []


def check(name, actual, required, relation):
    passed = actual > required if relation == ">" else actual < required
    checks.append(dict(name=name, actual_exact=str(actual),
                       required_exact=str(required), relation=relation,
                       passed=passed))


# C032w(4), at M=2: all omitted positive Taylor terms are positive.
P2_lower = (exp_lower(Q(25, 16), 32)
            + 6 * exp_lower(Q(2), 32) + Q(7, 2)
            + exp_lower(Q(81, 16), 32))
check("P2_lower_exceeds_210", P2_lower, Q(210), ">")
check("e_cubed_exceeds_10_using_retained_e_bound", Q(8, 3)**3, Q(10), ">")

# Delta_E >= 8*tau_2(T) > (32/3)*210/T = 2240/T.
T_barrier = 2240
costs = []
for tolerance in [Q(1), Q(1, 8)]:
    strict_T_lower = Q(T_barrier) / tolerance
    assert strict_T_lower.denominator == 1
    t0 = int(strict_T_lower)
    k_lower = Q(t0**4, 2)
    # J > exp(2*T^2)*T^3/(8*tolerance) > exp(2*T^2).
    # Since e^3>10 and T>t0, J>10^floor(2*t0^2/3).
    j_exponent = 2*t0**2 // 3
    check(f"T_prefactor_exceeds_one_tolerance_{tolerance}",
          Q(t0**3, 8)/tolerance, Q(1), ">")
    costs.append(dict(
        requested_primitive_error_strict_upper=str(tolerance),
        necessary_spatial_cutoff_strict_lower=str(strict_T_lower),
        integer_spatial_cutoff_at_least=t0+1,
        necessary_Taylor_degree_strict_lower=str(k_lower),
        necessary_midpoint_cell_count_strict_lower=f"10^{j_exponent}",
        decimal_power_exponent=j_exponent,
        arithmetic_rounding_allowance="0; exact rational inequalities",
        omitted_allowances="prime/small/large/profile-Taylor/coefficient errors are nonnegative"))

preflight_rows = []
for t in [5, 128, 512, 1024, 2048, 4096]:
    preflight_rows.append(dict(
        integer_T=t, E_tail_allowance_strict_lower=str(Q(T_barrier, t)),
        necessary_K_if_full_E_error_below_one_strict_lower=str(Q(t**4, 2)),
        necessary_J_if_full_E_error_below_one_strict_lower=
            f"exp({2*t*t})*{t**3}/8",
        required_E_error_strict_upper="1"))

# The box-model minimax calculation is in the associated complete draft.
box_lower = Q(3, 5)
check("independent_E_radius_one_box_barrier_exceeds_half", box_lower, Q(1, 2), ">")

# Preserve an actual, exactly valid candidate rather than pretend the cost
# preflight returned optimizer data.  It supplies only the trivial bound1.
names = []
for axis in ["real", "imaginary"]:
    for w in ["1/4", "1/2", "1", "2"]:
        for component in ["Re", "Im"]:
            names.append(f"{component}_kappa_{axis}_{w}")
for s in ["1/16", "1/4", "1", "4"]:
    names.append(f"L_{s}")
coefficients = {name: "0" for name in names}
cells = [dict(left="1", right="2", endpoints_included=True,
              candidate="q=0", exact_residual="1",
              tail_and_rounding_allowance="0: no evaluated kernel is used")]

certificate = dict(
    target_assessment="drafts/literature/2026-11-18-bounded-variation-continuum-dual-test-1570.md",
    complete_analytic_record="lemmas/C032x-common-disk-effective-evaluator-cost-stop.md",
    working_record="drafts/2026-11-18-bounded-variation-effective-cost-1576.md",
    canonical_evaluator="lemmas/C032w-effective-shifted-gaussian-primitive-evaluation.md",
    canonical_cost_result="lemmas/C032x-common-disk-effective-evaluator-cost-stop.md",
    scope="Literal common-M=2 implementation of C032w(6)-(13), raw independent symmetric E errors; no actual-dictionary obstruction",
    assumptions=[
        "C032j/m/q qualified actual divisor, multiplicities, zero-ordinate exclusion, strip/counting, finite-zero, heat and fixed-v1 inputs",
        "C032w audited explicit-formula normalization and uniform bounds",
        "M=2, T>=5, D=sqrt(T^2+1), R=T^2+1, r=T^2/R, H=P_D+d",
        "0<a<=1, A>=2D, N>=2, integer J>=1 and K>=1",
        "primitive radius Delta_E=8*(T*(d+d_K)+tau_2(T)), plus nonnegative arithmetic allowances"],
    exact_values=dict(P2_lower=str(P2_lower), P2_simplified_lower="210",
                      P2_Taylor_lower_degree=32,
                      E_tail_radius_strict_lower="2240/T",
                      polynomial_degree_necessary_strict_lower="T^4/2",
                      midpoint_cells_necessary_strict_lower="exp(2*T^2)*T^3/8",
                      independent_error_box_residual_lower=str(box_lower)),
    cost_bounds=costs, preflight_rows=preflight_rows,
    candidate=dict(coefficients=coefficients, exact_uniform_residual="1"),
    validation=dict(subinterval_count=1, maximum_allowed=4096, cells=cells,
                    coefficient_amplification="All coefficients0; kernel uncertainties contribute0 for this trivial candidate"),
    execution=dict(initial_optimizer_solves=0, refinement_optimizer_solves=0,
                   reason="Cost preflight stopped numerical data generation; no fictitious sampled-kernel solve is reported",
                   prime_powers_enumerated=0, finite_zero_coordinates_used=0,
                   large_sums_allocated=False),
    results=dict(required_strict_uniform_residual="1/2",
                 certified_uniform_residual_upper="1",
                 uniform_target_certified=False,
                 actual_dictionary_lower_bound_certified=False,
                 independent_box_lower_bound_scope="Only when raw common E radius>=1 in the selected independent interval model",
                 dominant_error="C032w common expanding-disk E tail, then its midpoint constant and Taylor degree",
                 decision="Stop this bounded implementation inconclusively; park literal expanding-disk/midpoint evaluation",
                 evidence="New exact cost barrier for a specific evaluator; no lower bound on actual residual or on better evaluators"),
    failures=[dict(name="requested_strict_uniform_residual",
                   actual="1", required="<1/2"),
              dict(name="executable_common_disk_E_enclosure",
                   actual=f"Delta_E<1 requires K>{costs[0]['necessary_Taylor_degree_strict_lower']} and J>{costs[0]['necessary_midpoint_cell_count_strict_lower']}",
                   required="Finite sums explicitly evaluated with full errors before a nontrivial kernel certificate")],
    arithmetic_checks=checks,
    arithmetic_failures=[c["name"] for c in checks if not c["passed"]])

path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2)+"\n")
print("certified uniform residual upper=1; required <1/2; no actual-dictionary lower bound")
print(f"common E radius<1 requires T>{T_barrier}, K>{costs[0]['necessary_Taylor_degree_strict_lower']}, J>{costs[0]['necessary_midpoint_cell_count_strict_lower']}")
print("dominant error: expanding-disk primitive tail and midpoint/Taylor constants; optimizer solves=0; closed cells=1")
print(f"failed obligations={len(certificate['failures'])}; arithmetic failures={len(certificate['arithmetic_failures'])}")
print(f"certificate={path}; full reasoning={certificate['complete_analytic_record']}")
raise SystemExit(bool(certificate["arithmetic_failures"]))
