"""Exact C033z input-constructor checks; no profile or transform evaluation.

The certificate checks every seed/refined root interval and constructs the
25 reference weights. Elementary-function accuracy and cost are rational
preflight bounds; the 48 Gaussian factors and 780 q inputs are not evaluated.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def evaluate(coefficients, x):
    result = coefficients[-1]
    for coefficient in reversed(coefficients[:-1]):
        result = result*x + coefficient
    return result


def legendre_polynomials():
    polynomials = [[F(1)], [F(0), F(1)]]
    for n in range(1, 13):
        a, b = polynomials[-1], polynomials[-2]
        polynomials.append([
            ((2*n+1)*(a[k-1] if 1 <= k <= len(a) else 0)
             - n*(b[k] if k < len(b) else 0))/(n+1)
            for k in range(n+2)
        ])
    return polynomials


def cardinal_weight(nodes, index):
    polynomial = [F(1)]
    denominator = F(1)
    for k, node in enumerate(nodes):
        if k == index:
            continue
        polynomial = [-node*polynomial[0]] + [
            polynomial[j-1]-node*polynomial[j]
            for j in range(1, len(polynomial))
        ] + [polynomial[-1]]
        denominator *= nodes[index]-node
    integral = sum((2*polynomial[j]/(j+1)
                    for j in range(0, len(polynomial), 2)), F(0))
    return integral/denominator


def main():
    polynomials = legendre_polynomials()
    rules = []
    root_checks = []
    for n in (12, 13):
        coefficients = polynomials[n]
        grid = [F(j, 128) for j in range(129)]
        values = [evaluate(coefficients, x) for x in grid]
        seeds = [(grid[j], grid[j+1]) for j in range(128)
                 if values[j]*values[j+1] < 0]
        positive_intervals = []
        for left, right in seeds:
            lo, hi = left, right
            sign_lo = evaluate(coefficients, lo) > 0
            for _ in range(160):
                mid = (lo+hi)/2
                value = evaluate(coefficients, mid)
                if value == 0:
                    lo = hi = mid
                elif (value > 0) == sign_lo:
                    lo = mid
                else:
                    hi = mid
            positive_intervals.append((lo, hi))
        intervals = [(-hi, -lo) for lo, hi in reversed(positive_intervals)]
        seed_intervals = [(-hi, -lo) for lo, hi in reversed(seeds)]
        if n % 2:
            intervals.append((F(0), F(0)))
            seed_intervals.append((F(0), F(0)))
        intervals += positive_intervals
        seed_intervals += seeds
        nodes = [(lo+hi)/2 for lo, hi in intervals]
        weights = [cardinal_weight(nodes, i) for i in range(n)]
        moment_checks = [sum((weights[i]*nodes[i]**k for i in range(n)), F(0))
                         == (F(2, k+1) if k % 2 == 0 else 0)
                         for k in range(n)]
        checks = {
            "degree_and_parity": len(coefficients) == n+1
                and coefficients[-1] != 0
                and all(c == 0 for k, c in enumerate(coefficients) if (k-n) % 2),
            "exactly_six_positive_sign_change_cells": len(seeds) == 6,
            "grid_zeros_only_the_odd_center":
                [j for j, value in enumerate(values) if value == 0] == ([0] if n % 2 else []),
            "full_n_distinct_root_intervals": len(intervals) == n,
            "all_seed_intervals_inside_open_unit_interval":
                all(-1 < lo <= hi < 1 for lo, hi in seed_intervals),
            "all_seed_gaps_above_1_over_32":
                all(seed_intervals[j+1][0]-seed_intervals[j][1] > F(1, 32)
                    for j in range(n-1)),
            "every_refined_interval_inside_its_seed":
                all(a <= lo <= hi <= b for (a, b), (lo, hi)
                    in zip(seed_intervals, intervals)),
            "every_refined_interval_certifies_a_root":
                all((lo == hi and evaluate(coefficients, lo) == 0)
                    or evaluate(coefficients, lo)*evaluate(coefficients, hi) < 0
                    for lo, hi in intervals),
            "every_midpoint_radius_at_most_2_pow_minus_168":
                all((hi-lo)/2 <= F(1, 2**168) for lo, hi in intervals),
            "all_cardinal_weight_moments_exact_through_n_minus_1": all(moment_checks),
        }
        root_checks.append(checks)
        rules.append({
            "degree": n,
            "coefficients_ascending": [str(c) for c in coefficients],
            "positive_seed_numerators_over_128": [[int(a*128), int(b*128)] for a, b in seeds],
            "roots": [{"left": str(lo), "right": str(hi), "midpoint": str(node),
                       "left_value": str(evaluate(coefficients, lo)),
                       "right_value": str(evaluate(coefficients, hi)),
                       "cardinal_weight": str(weight)}
                      for (lo, hi), node, weight in zip(intervals, nodes, weights)],
            "exact_moment_checks": moment_checks,
            "checks": checks,
        })

    root_radius = F(1, 2**168)
    log_tail = F(9, 4*129*3**129)
    outer_argument_error = 30*log_tail+F(7, 10)*root_radius
    outer_exp_taylor_error = F(96*3**21, factorial(41))
    outer_exp_input_error = 3**21*outer_argument_error
    outer_exp_error = outer_exp_taylor_error+outer_exp_input_error
    gaussian_error = F(48, factorial(41))+4*root_radius
    q_error = F(1, 2**65)+outer_exp_error/8
    bounds = {
        "root_radius": str(root_radius),
        "reference_weight_error_bound": str(2**99*root_radius),
        "unit_weight_error_bound": str(2**98*root_radius),
        "log2_tail_bound": str(log_tail),
        "outer_argument_error_bound": str(outer_argument_error),
        "outer_exp_taylor_error_bound": str(outer_exp_taylor_error),
        "outer_exp_input_error_bound": str(outer_exp_input_error),
        "outer_exp_total_error_bound": str(outer_exp_error),
        "gaussian_error_bound": str(gaussian_error),
        "q_error_bound": str(q_error),
        "required_input_radius": str(F(1, 2**60)),
    }
    cost = {
        "legendre_coefficients": 500,
        "two_reference_grid_scans": 129*(28+30),
        "twelve_positive_root_refinements": 6*160*(28+30),
        "root_midpoints_mirrors": 100,
        "seed_gap_and_range_checks": 100,
        "twenty_five_cardinal_weights": 4439,
        "inner_node_and_weight_affine_maps": 156,
        "taylor_coefficients_to_40": 81,
        "forty_eight_gaussian_factors": 48*88,
        "log2_series": 400,
        "outer_arguments_and_clamps": 260*12,
        "outer_exponentials": 260*86,
        "three_widths_at_each_outer_node": 260*4,
        "inverse_square_root_bisections_and_midpoints": 780*322,
    }
    generation = sum(cost.values())
    combined = generation+374518
    checks = {
        "all_twenty_root_rule_checks_pass": all(all(c.values()) for c in root_checks),
        "cardinal_derivative_ri_below_2_pow_94": 2**84*64*12 < 2**94,
        "cardinal_derivative_rk_below_2_pow_91": 2**83+2**90 < 2**91,
        "integrated_gradient_sum_below_2_pow_99": 13*2**95 < 2**99,
        "unit_weight_error_below_2_pow_minus_60": 2**98*root_radius < F(1, 2**60),
        "log2_error_below_2_pow_minus_200": log_tail < F(1, 2**200),
        "outer_argument_error_below_2_pow_minus_160": outer_argument_error < F(1, 2**160),
        "outer_exp_taylor_error_below_2_pow_minus_124": outer_exp_taylor_error < F(1, 2**124),
        "outer_exp_total_error_below_2_pow_minus_120": outer_exp_error < F(1, 2**120),
        "gaussian_error_below_2_pow_minus_150": gaussian_error < F(1, 2**150),
        "q_error_below_2_pow_minus_64": q_error < F(1, 2**64),
        "q_error_below_required_input_radius": q_error < F(1, 2**60),
        "legendre_coefficient_count_within_500": sum(4*(n+2)+3 for n in range(1, 13)) <= 500,
        "cardinal_weight_count_4439": sum(n*((n-1)**2+2*(n-1)+3*((n+1)//2)+1)
                                             for n in (12, 13))+25 == 4439,
        "inner_affine_count_156": 48*3+12 == 156,
        "generation_count_350842": generation == 350842,
        "combined_count_725360": combined == 725360,
        "remaining_budget_274640": 10**6-combined == 274640,
    }
    failures = [f"P{n}:{key}" for n, c in zip((12, 13), root_checks)
                for key, value in c.items() if not value]
    failures += [key for key, value in checks.items() if not value]
    result = {
        "status": "COSTED_CORE_INPUT_CONSTRUCTOR_PASS_AGGREGATE_INCOMPLETE" if not failures else "FAIL",
        "transforms_evaluated": False,
        "profile_callbacks_evaluated": False,
        "all_core_inputs_evaluated": False,
        "evaluated_data": "P12/P13 reference root brackets and rational cardinal weights only",
        "rules": rules,
        "bounds": bounds,
        "cost": {"unit": "exact rational +,-,*,/ or comparison; no bit-complexity bound",
                 "generation_breakdown": cost, "generation_upper": generation,
                 "existing_core_upper": 374518, "combined_upper": combined,
                 "aggregate_cap": 10**6, "remaining_budget": 10**6-combined},
        "checks": checks,
        "failures": failures,
        "aggregate": {"full_preflight_passed": False,
                      "complete_exponent_arithmetic_allowance_paid": False,
                      "final_exponential_allowance_paid": False,
                      "full_count": None},
        "unresolved": ["Constants and I(1)", "Prime and remaining profile terms",
                       "Outer weight/factor arithmetic and propagation", "Final exponentials",
                       "Application audits and qualified external/zero-data inputs"],
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Root intervals: 25/25; exact moment identities: 25/25; root checks: {sum(map(len, root_checks))}")
    print("Input bounds: x<=2^-169, unit weights<2^-70, Gaussian<2^-150, q<2^-64; required <=2^-60")
    print(f"Operations: generation <={generation}; with core <={combined}; cap {10**6}; remaining {10**6-combined}")
    print(f"Checks: {len(checks)} aggregate comparisons; failures: {failures}")
    print("Full preflight INCOMPLETE; profile callbacks and transforms not evaluated")
    print(f"Certificate: {path}")
    assert not failures, failures


if __name__ == "__main__":
    main()
