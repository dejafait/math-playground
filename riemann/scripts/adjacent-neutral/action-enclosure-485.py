#!/usr/bin/env python3
"""Exact rational certificate for C744k's analytic approximation errors.

This is NOT a certificate of either full finite Schur matrix. It records
all Taylor coefficients, exact remainder operands and perturbation bounds.
No floating-point inequality is used. Run from the active notebook root.
"""
from decimal import Context, Decimal, ROUND_CEILING
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def exponential_upper(x, degree):
    x = F(x)
    prefix = sum((x**k / factorial(k) for k in range(degree + 1)), F(0))
    tail = x**(degree + 1) / factorial(degree + 1)
    return prefix + tail / (1 - x / (degree + 2))


def quotient_coefficients(c, degree):
    # S(t) A(t)=exp(c t), S(t)=sinh(t)/t. All coefficients are exact.
    coefficients = []
    for n in range(degree + 1):
        value = c**n / factorial(n)
        value -= sum((coefficients[n - 2*j] / factorial(2*j + 1)
                      for j in range(1, n//2 + 1)), F(0))
        coefficients.append(value)
    return coefficients


def quotient_residual(coefficients, c):
    return [sum((coefficients[n-2*j] / factorial(2*j+1)
                 for j in range(n//2 + 1)), F(0)) - c**n / factorial(n)
            for n in range(len(coefficients))]


def rational(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def upper_decimal(value):
    return str(Context(prec=12, rounding=ROUND_CEILING).divide(
        Decimal(value.numerator), Decimal(value.denominator)))


def main():
    degree = 96
    # On |z|<=2: |S(z)-1| <= sum_{j>=1} 4^j/(2j+1)! < 5/6.
    last = 12
    s_prefix = sum((F(4**j, factorial(2*j+1)) for j in range(1, last+1)), F(0))
    s_first_tail = F(4**(last+1), factorial(2*last+3))
    s_ratio = F(4, (2*last+4)*(2*last+5))
    s_upper = s_prefix + s_first_tail / (1-s_ratio)
    exp1_upper = exponential_upper(1, 20)
    exp3_upper = exponential_upper(3, 32)
    a_plus = quotient_coefficients(F(1, 2), degree+1)
    a_minus = quotient_coefficients(F(-3, 2), degree+1)
    q = a_plus[1:]
    h = [x/2 for x in a_minus[1:]]
    residual_plus = quotient_residual(a_plus, F(1, 2))
    residual_minus = quotient_residual(a_minus, F(-3, 2))

    delta_q = F(400,29) * F(11,40)**(degree+1)
    delta_h = F(640,9) * F(11,20)**(degree+1)
    operator_error = F(11,20) * (delta_q/2 + 2*delta_h)
    head_error = F(51,50) * operator_error
    eta_squared_upper = F(8,245)
    tail_squared_upper = F(72*515, 7**512)
    tail_norm_upper = F(1, 10**100)
    full_action_upper = F(51,50) * (7 + 3 + F(3,2)*257 + 5)
    covariance_map_error = head_error + 500*tail_norm_upper
    covariance_error = 1003*covariance_map_error
    schur_error = 2*head_error + F(250,171)*covariance_error

    checks = {
        "S_minus_one_disk_bound": s_upper < F(5,6),
        "exp_one_below_three": exp1_upper < 3,
        "exp_three_below_twenty_one": exp3_upper < 21,
        "q_disk_max_below_ten": F(6*3+1,2) < 10,
        "h_disk_max_below_thirty_two": F(6*21+1,4) < 32,
        "q_quotient_all_98_coefficients": all(x == 0 for x in residual_plus),
        "h_quotient_all_98_coefficients": all(x == 0 for x in residual_minus),
        "q_initial_coefficients": q[:3] == [F(1,2), F(-1,24), F(-1,16)],
        "h_initial_coefficients": h[:3] == [F(-3,4), F(23,48), F(-5,32)],
        "neutral_graph_eta_squared_below_one_over_twenty_five": eta_squared_upper < F(1,25),
        "neutral_graph_norm_below_51_over_50": 1+F(1,25) < F(51,50)**2,
        "tail_moment_norm_below_1e_minus_100": tail_squared_upper < tail_norm_upper**2,
        "full_action_norm_below_500": full_action_upper < 500,
        "head_action_error_below_5_22e_minus_24": head_error < F(522,10**26),
        "head_action_error_below_1e_minus_22": head_error < F(1,10**22),
        "covariance_map_error_below_one": covariance_map_error < 1,
        "schur_perturbation_below_1e_minus_19": schur_error < F(1,10**19),
        "conditional_finite_margin_reserves_9_over_250": F(1,25)-F(1,10**19) > F(9,250),
        "conditional_L2_margin_exceeds_one_over_thirty": F(9,250)/F(26,25) > F(1,30),
    }
    operands = {
        "S_minus_one_upper": s_upper,
        "exp_one_upper": exp1_upper, "exp_three_upper": exp3_upper,
        "delta_q": delta_q, "delta_h": delta_h,
        "operator_error": operator_error, "head_action_error": head_error,
        "eta_squared_upper": eta_squared_upper,
        "tail_moment_squared_upper": tail_squared_upper,
        "tail_moment_norm_upper": tail_norm_upper,
        "full_action_norm_upper": full_action_upper,
        "covariance_map_error": covariance_map_error,
        "covariance_error": covariance_error,
        "schur_error": schur_error,
    }
    output = Path(__file__).with_suffix(".json")
    data = {
        "analytic_error_checks_pass": all(checks.values()),
        "full_two_sign_margin_certified": False,
        "degree": degree,
        "method": "Exact Fraction arithmetic; Cauchy and operator estimates proved in C744k.",
        "scope": "Analytic kernel replacement and exact-neutral covariance perturbation only.",
        "checks": checks,
        "bounds": {key:rational(value) for key,value in operands.items()},
        "q_coefficients": [rational(value) for value in q],
        "h_coefficients": [rational(value) for value in h],
        "quotient_residuals": {
            "plus": [rational(value) for value in residual_plus],
            "minus": [rational(value) for value in residual_minus],
        },
        "failures": [name for name, passed in checks.items() if not passed],
        "unresolved": [
            "Exact finite polynomial-log action scalar products have not been enclosed.",
            "Finite moments, covariance subtraction and matrix lower bounds remain unpaid.",
            "No both-sign positive Schur certificate, beta_1 bound or RH conclusion.",
        ],
    }
    output.write_text(json.dumps(data, indent=2)+"\n")
    print(f"Exact analytic checks: {sum(checks.values())}/{len(checks)} passed")
    print(f"Head action error <= {upper_decimal(head_error)}; required < 1e-22")
    print(f"Schur perturbation <= {upper_decimal(schur_error)}; required < 1e-19")
    print(f"Failures: {data['failures']}")
    print("Full matrix certificate: NOT ESTABLISHED; polynomial-log integrals and finite signs unpaid")
    print(f"Full certificate: {output}")
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
