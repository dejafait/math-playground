"""Remaining C033z arithmetic preflight. No profiles or scalars evaluated."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

from direct_positive_real_inputs_1802 import (
    evaluate, legendre_polynomials, cardinal_weight,
)


def main():
    polys = legendre_polynomials()
    n = 13
    a, b = polys[-1], polys[-2]
    coefficients = [((2*n+1)*(a[k-1] if 1 <= k <= len(a) else 0)
                     - n*(b[k] if k < len(b) else 0))/(n+1)
                    for k in range(n+2)]
    grid = [F(j, 128) for j in range(129)]
    values = [evaluate(coefficients, x) for x in grid]
    seeds = [(grid[j], grid[j+1]) for j in range(128)
             if values[j]*values[j+1] < 0]
    positive = []
    for lo, hi in seeds:
        sign = evaluate(coefficients, lo) > 0
        for _ in range(160):
            mid = (lo+hi)/2
            v = evaluate(coefficients, mid)
            if v == 0:
                lo = hi = mid
            elif (v > 0) == sign:
                lo = mid
            else:
                hi = mid
        positive.append((lo, hi))
    intervals = [(-hi, -lo) for lo, hi in reversed(positive)] + positive
    full_seeds = [(-hi, -lo) for lo, hi in reversed(seeds)] + seeds
    nodes = [(lo+hi)/2 for lo, hi in intervals]
    weights = [cardinal_weight(nodes, i) for i in range(14)]
    moments = [sum((weights[i]*nodes[i]**k for i in range(14)), F(0))
               == (F(2, k+1) if k % 2 == 0 else 0) for k in range(14)]
    root_checks = {
        "degree14_even": len(coefficients) == 15 and coefficients[-1] != 0
            and all(c == 0 for k, c in enumerate(coefficients) if k % 2),
        "seven_positive_sign_change_cells": len(seeds) == 7,
        "no_grid_zeros": all(values),
        "fourteen_disjoint_seeds": len(full_seeds) == 14 and all(
            full_seeds[j+1][0]-full_seeds[j][1] > F(1, 32) for j in range(13)),
        "seed_extrema_within_127_over_128": all(-F(127, 128) <= lo <= hi <= F(127, 128)
            for lo, hi in full_seeds),
        "refined_containment": all(a <= lo <= hi <= b
            for (a, b), (lo, hi) in zip(full_seeds, intervals)),
        "all_refined_root_signs": all((lo == hi and evaluate(coefficients, lo) == 0)
            or evaluate(coefficients, lo)*evaluate(coefficients, hi) < 0 for lo, hi in intervals),
        "all_midpoint_radii": all((hi-lo)/2 <= F(1, 2**168) for lo, hi in intervals),
        "fourteen_cardinal_moments": all(moments),
    }

    ell = 2*sum((F(1, 3**(2*j+1)*(2*j+1)) for j in range(64)), F(0))
    log2_error = F(9, 4*129*3**129)
    primes = [p for p in range(2, 33) if all(p % d for d in range(2, p))]
    powers = {}
    for p in primes:
        v = p
        while v <= 32:
            powers[v] = p
            v *= p
    log_values = {}
    for v in sorted(powers):
        k = v.bit_length()-1
        z = F(v-2**k, v+2**k)
        lower = k*ell + 2*sum((z**(2*j+1)/(2*j+1) for j in range(32)), F(0))
        log_values[v] = lower
    prime_log_error = 5*log2_error + F(9, 4*65*3**65)
    schedule = []
    for j in range(1, 21):
        exponent = (F(28)-F(7*j, 5)).__floor__()
        for sigma in (F(1), F(3, 2), F(2)):
            lower_width = sigma + 2**exponent
            kept = [v for v in powers if lower_width*log_values[v]**2 < 32]
            omitted = [v for v in powers if v not in kept]
            schedule.append({"panel": j, "sigma": str(sigma),
                "lower_width": str(lower_width), "keep": sorted(kept),
                "omit": sorted(omitted),
                "omitted_lower_exponents": {str(v): str(lower_width*log_values[v]**2)
                                             for v in omitted}})
    slots = 13*sum(len(row["keep"]) for row in schedule)

    eta = F(1, 2**169)
    taylor = F(3, factorial(21))
    h_A_error = 256*taylor + 32*eta
    h_u_error = 8*taylor + eta/2
    h_error = 512*h_A_error + 2**21*h_u_error
    I_error = 16*h_error + F(224*7, 2**63)
    pi_error = F(16, 65*5**65)+F(4, 65*239**65)
    gamma_error = F(1, 8*4096**2)+12*log2_error
    log4pi_error = F(49, 24*33*7**33)+4*log2_error+pi_error
    K_error = (gamma_error+log4pi_error+2*I_error)/12+32*pi_error
    logw_error = F(1, 99*2**30)+F(8, 2**120)+F(1, 2**160)+2*log2_error
    pole_error = F(2, 2**60)+F(2, 16**11*factorial(11))+F(4, 2**64)
    prime_argument_error = F(16, 2**120)+2**30*8*prime_log_error
    prime_exp_error = 32*taylor+prime_argument_error
    prime_error = 18*(F(1, 2**60)+4*(prime_exp_error+F(1, 2**44)))
    profile_error = K_error + pole_error + logw_error/24 + F(1, 6*2**24) + prime_error/6 + 128*pi_error
    r_error = F(96*3**11, factorial(21))+F(3**11, 2**161)
    outer_exp_error = taylor+F(2, 2**120)
    g_error = 2*r_error + 2*2**16*outer_exp_error + F(2**16, 2**64)
    outer_weight_error = F(1, 2**68)
    arithmetic_error = 13*profile_error + 7*(20*g_error+260*4*outer_weight_error)
    final_exp_error = 128*taylor
    bounds = {
        "Ihat_arithmetic_error": I_error, "Ihat_required": F(1, 2**30),
        "pi_error": pi_error, "pi_required": F(1, 2**140),
        "gamma_error": gamma_error, "gamma_required": F(1, 2**26),
        "log4pi_error": log4pi_error, "K_error": K_error,
        "prime_log_error": prime_log_error,
        "prime_argument_error": prime_argument_error,
        "prime_sum_error": prime_error,
        "logw_error": logw_error, "pole_error": pole_error,
        "profile_error": profile_error, "profile_required": F(1, 2**22),
        "outer_r_error": r_error, "outer_g_error": g_error,
        "outer_weight_error": outer_weight_error,
        "exponent_arithmetic_error": arithmetic_error, "exponent_required": F(1, 2**10),
        "final_exp_error": final_exp_error, "final_exp_required": F(1, 2**10),
        "final_scalar_radius": F(25, 16384)+arithmetic_error+final_exp_error,
        "final_scalar_required": F(1, 256),
    }
    cost = {
        "P14_coefficients": 63,
        "P14_grid_scan": 129*32,
        "P14_root_refinements": 7*160*32,
        "P14_midpoints_reflections_and_seed_checks": 120,
        "P14_cardinal_weights": 14*(13**2+2*13+3*7+1)+14,
        "Ihat_unit_nodes_weights_clamps": 224*3+14+224*2,
        "Ihat_224_values_and_accumulation": 224*108,
        "gamma_harmonic_sum_and_assembly": 8200,
        "pi_sqrtpi_log4pi_constants_and_coefficient_tables": 1500,
        "prime_enumeration": 2000,
        "18_prime_logs_roots_coefficients_squares": 18*(70+322+2),
        "60_panel_prime_schedules": 60+60*18*2,
        "selected_prime_slots": slots*53,
        "260_reciprocals_and_clamps": 260*3,
        "780_logw_values_and_260_bases": 780*36+260,
        "780_pole_terms": 780*24,
        "780_profile_assemblies": 780*7,
        "260_outer_square_root_exponentials": 260*46,
        "520_outer_Laplace_factors": 520*45,
        "outer_sqrtpi_products_and_g": 260+520,
        "outer_weight_generation_and_clamps": 60,
        "520_weighted_g_and1560_accumulations": 520+1560*2,
        "eight_final_clamps_exponentials": 8*53,
    }
    additional = sum(cost.values())
    total = 725360+additional
    checks = {
        "all_root_checks": all(root_checks.values()),
        "reference_weight_gradient_bound": 14*2**102 < 2**106,
        "Ihat_error_below_2_pow_minus30": I_error < F(1, 2**30),
        "Ihat_denominator_survives_perturbation": 4*h_u_error < F(1, 2**9),
        "pi_error_below_2_pow_minus140": pi_error < F(1, 2**140),
        "gamma_error_below_2_pow_minus26": gamma_error < F(1, 2**26),
        "log4pi_error_below_2_pow_minus60": log4pi_error < F(1, 2**60),
        "prime_logs_below_2_pow_minus100": prime_log_error < F(1, 2**100),
        "eighteen_prime_powers": len(powers) == 18,
        "all_suppressed_panel_bounds": all(F(v) >= 32 for row in schedule
            for v in row["omitted_lower_exponents"].values()),
        "selected_slots1534": slots == 1534,
        "prime_argument_error_below_2_pow_minus66": prime_argument_error < F(1, 2**66),
        "threshold_exp_bound": 2*F(3, 8)**32 < F(1, 2**44),
        "prime_sum_error_below_2_pow_minus37": prime_error < F(1, 2**37),
        "logw_error_below_2_pow_minus35": logw_error < F(1, 2**35),
        "pole_error_below_2_pow_minus55": pole_error < F(1, 2**55),
        "profile_error_below_2_pow_minus22": profile_error < F(1, 2**22),
        "outer_r_error_below_2_pow_minus40": r_error < F(1, 2**40),
        "outer_g_error_below_2_pow_minus35": g_error < F(1, 2**35),
        "arithmetic_error_below_2_pow_minus17": arithmetic_error < F(1, 2**17),
        "exponent_allowance_paid": arithmetic_error < F(1, 2**10),
        "final_exp_allowance_paid": final_exp_error < F(1, 2**10),
        "final_radius_passes": bounds["final_scalar_radius"] < F(1, 256),
        "additional_count_fits": additional <= 274640,
        "full_count_fits": total <= 10**6,
    }
    failures = ["roots:"+k for k, ok in root_checks.items() if not ok]
    failures += [k for k, ok in checks.items() if not ok]
    result = {
        "status": "PREFLIGHT_PASS_PENDING_APPLICATION_AUDIT" if not failures else "PREFLIGHT_FAIL",
        "transforms_evaluated": False, "profile_callbacks_evaluated": False,
        "evaluated_data": "P14 reference rule and finite prime-log/suppression table only",
        "root_rule": {
            "coefficients_ascending": list(map(str, coefficients)),
            "positive_seed_numerators_over128": [[int(lo*128), int(hi*128)] for lo, hi in seeds],
            "roots": [{"left": str(lo), "right": str(hi), "midpoint": str(node),
                       "left_value": str(evaluate(coefficients, lo)),
                       "right_value": str(evaluate(coefficients, hi)), "weight": str(weight)}
                      for (lo, hi), node, weight in zip(intervals, nodes, weights)],
            "moments": moments, "checks": root_checks,
        },
        "prime_logs": {str(n): {"prime_base": p, "lower_log": str(log_values[n])}
                       for n, p in sorted(powers.items())},
        "prime_schedule": schedule,
        "bounds": {k: str(v) for k, v in bounds.items()},
        "cost": {"unit": "exact rational +,-,*,/ or comparison; no bit-complexity claim",
                 "prior_upper": 725360, "additional_breakdown": cost,
                 "additional_upper": additional, "full_upper": total,
                 "required_cap": 10**6, "remaining": 10**6-total},
        "checks": checks, "failures": failures,
        "unresolved": ["Independent C033y/z application and complete ledger audit",
                       "Qualified external source and finite-zero assumptions",
                       "No evaluated scalar data, interpolation, conditioning or TV certificate",
                       "Actual-Xi positivity, cancellation, signed height and realization"],
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(f"P14: {len(intervals)} root intervals, {sum(moments)}/14 moments; {len(root_checks)} checks")
    print(f"Prime work: {slots} slots; 14040 naive slots; suppression errors included")
    print(f"Exponent arithmetic {float(arithmetic_error):.9g} < required {2**-10:.9g}")
    print(f"Final exponential {float(final_exp_error):.9g} < required {2**-10:.9g}")
    print(f"Final scalar radius {float(bounds['final_scalar_radius']):.9g} < required {2**-8:.9g}")
    print(f"Cost {total} <= {10**6}; additional {additional} <= 274640; remaining {10**6-total}")
    print(f"Checks: {len(checks)}; failures: {failures}; no callbacks/scalars evaluated")
    print(f"Certificate: {path}")
    assert not failures, failures


if __name__ == "__main__":
    main()
