"""C033z exact inner-core preflight; no quadrature callbacks or transforms."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def main():
    delta = F(1, 2**60)
    d_e = F(8 * 2**15, factorial(17))
    d_s = F(4**22, factorial(23)) / (1 - F(16, 24*25))
    d_t = d_s / 4
    d_r = (d_e + d_t) / 2 + 2*d_s
    c = []
    a = []
    for n in range(29):
        an = F(1, 2**(n+1) * factorial(n+1))
        if n % 2:
            an -= F(1, factorial(n+2))
        a.append(an)
        cn = an/2 - sum((c[n-2*j]/factorial(2*j+1)
                        for j in range(1, n//2+1)), F(0))
        c.append(cn)
    identities = []
    for n in range(29):
        product_coefficient = 2*sum((c[n-2*j]/factorial(2*j+1)
                                    for j in range(n//2+1)), F(0))
        identities.append(product_coefficient == a[n])

    coefficient_cost = {
        "factorials_to_30": 30,
        "factorial_reciprocals": 30,
        "powers_of_two_to_29": 29,
        "E_coefficients": 29,
        "odd_coefficient_subtractions": 14,
        "halvings": 29,
        "recurrence_multiply_subtract": 2*sum(n//2 for n in range(29)),
    }
    cost = {
        "coefficient_formation": sum(coefficient_cost.values()),
        "clamp_48_input_triples": 48*3*2,
        "48_products_and_scaled_nodes": 48*2,
        "29_shared_moments": 48*(28+29+29),
        "29_moment_coefficients": 29,
        "clamp_780_inverse_square_roots": 780*2,
        "663_high_width_horner_rules": 663*(1+2*28+1),
        "117_remaining_and_one_fixed_rule": 118*(48*58+1),
        "780_final_differences": 780,
    }
    total = sum(cost.values())
    high_perturbation_factor = 48 + F(1, 4)*4*12*F(17, 4) + F(1, 4)*12*96
    low_perturbation_factor = 8 + 4*35*5 + 2*96
    high_error = F(6, 2**28) + 512*delta
    low_error = 4*d_r + 1024*delta
    difference_bound = F(1, 2**25) + F(1, 2**26) + 2048*delta
    checks = {
        "disk_S_upper_below_15_over_8": (F(121, 16)-F(16, 121))/4 < F(15, 8),
        "disk_R_upper_below_6": F(21, 4) < 6,
        "all_29_coefficient_identities": all(identities),
        "all_29_coefficients_obey_cauchy_bound": all(abs(c[k]) <= F(6, 2**k) for k in range(29)),
        "c0_is_one_quarter": c[0] == F(1, 4),
        "c1_is_minus_one_over_48": c[1] == F(-1, 48),
        "first_17_panel_width_exponent_above_4": F(28)-F(7*17, 5) > 4,
        "geometric_tail_ratio_below_1": F(16, 24*25) < 1,
        "quotient_remainder_below_2_pow_minus_28": d_r < F(1, 2**28),
        "polynomial_remainder_below_2_pow_minus_25": F(6, 2**28) < F(1, 2**25),
        "quotient_derivative_below_35": F(1+4, 2)+F(4*16, 2) < 35,
        "high_input_factor_below_512": high_perturbation_factor == 387 < 512,
        "low_input_factor_below_1024": low_perturbation_factor == 900 < 1024,
        "high_plus_fixed_error_below_difference_bound": high_error+low_error < difference_bound,
        "low_plus_fixed_error_below_difference_bound": 2*low_error < difference_bound,
        "difference_error_below_2_pow_minus_24": difference_bound < F(1, 2**24),
        "propagated_error_below_2_pow_minus_22": F(13, 6*2**24) < F(1, 2**22),
        "coefficient_cost_553": sum(coefficient_cost.values()) == 553,
        "core_operation_total_374518": total == 374518,
        "core_operation_bound_below_380000": total < 380000,
        "profile_count_780": 663+117 == 780,
    }
    assert all(checks.values()), [k for k, v in checks.items() if not v]
    result = {
        "status": "CONDITIONAL_INNER_CORE_PASS_AGGREGATE_PREFLIGHT_INCOMPLETE",
        "scope": "C033y exact-node Jhat differences; qualified inputs and separate application audit remain",
        "transforms_evaluated": False,
        "gauss_callbacks_evaluated": False,
        "input_contract": {
            "absolute_radius": str(delta),
            "families": ["48 x", "48 omega", "48 exp(-x^2)", "780 w^(-1/2)"],
            "data_generated": False,
            "generation_cost_certified": False,
        },
        "coefficients": [{"k": k, "c_k": str(c[k]), "identity_verified": identities[k]}
                         for k in range(29)],
        "bounds": {
            "E16_remainder": str(d_e), "S10_remainder": str(d_s),
            "T10_remainder": str(d_t), "quotient_remainder": str(d_r),
            "quotient_required": str(F(1, 2**28)),
            "polynomial_remainder": str(F(6, 2**28)),
            "high_input_factor": str(high_perturbation_factor),
            "low_input_factor": str(low_perturbation_factor),
            "high_J_error": str(high_error), "low_J_error": str(low_error),
            "difference_error_bound": str(difference_bound),
            "difference_required": str(F(1, 2**24)),
            "exponent_core_error_bound": str(F(13, 6*2**24)),
            "exponent_core_required": str(F(1, 2**22)),
        },
        "coefficient_cost": coefficient_cost,
        "core_cost": {"unit": "rational +,-,*,/ or clamp comparison; no bit-cost claim",
                      "breakdown": cost, "total_upper": total, "required_core_bound": 380000},
        "aggregate": {"required_cap": 10**6, "full_operation_count": None,
                      "full_exponent_arithmetic_radius_certified": False,
                      "final_exponential_radius_certified": False,
                      "preflight_passed": False},
        "checks": checks,
        "unresolved": [
            "Certified node/weight, exp(-x^2), q input generation and complete cost",
            "Constants, I(1), prime enumeration/evaluation and remaining profile arithmetic",
            "Outer constants and arithmetic, final exponentials and full error/cost ledger",
            "C033y/C033z application audits and qualified external inputs",
        ],
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Quotient error bound: {d_r} < 1/268435456: PASS")
    print(f"Conditional J-difference bound: {difference_bound} < 1/16777216: PASS")
    print("Conditional propagated core error: 13/100663296 < 1/4194304: PASS")
    print(f"Core operations: {total} < 380000; aggregate UNKNOWN, required <=1000000")
    print(f"Checks: {len(checks)} PASS; input data/callbacks/scalars not evaluated")
    print("Aggregate preflight: INCOMPLETE; input generation and remaining error/cost unpaid")
    print(f"Certificate: {path}")


if __name__ == "__main__":
    main()
