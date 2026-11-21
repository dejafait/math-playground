"""Exact arithmetic for the actual-theta crossing obstruction in L915.

No contact search, floating-point sampling, or replacement measure is used.
Analytic source imports, convergence, and the crossing argument are in L915.
"""

from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def add(a, b):
    size = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else F(0))
                 + (b[i] if i < len(b) else F(0)) for i in range(size)])


def scale(p, c):
    return trim([c * x for x in p])


def derivative(p):
    return trim([i * p[i] for i in range(1, len(p))])


def evaluate(p, x):
    answer = F(0)
    for c in reversed(p):
        answer = answer * x + c
    return answer


def spatial_derivative(p):
    # d/du [exp(u/2-v) p(v)], with v=pi*n^2*exp(2u).
    return add(add([F(0)] + scale(derivative(p), F(2)), scale(p, F(1, 2))),
               [F(0)] + scale(p, F(-2)))


checks = []


def equality(name, actual, required):
    checks.append({"name": name, "passed": actual == required,
                   "actual": actual, "required": required})


def inequality(name, actual, relation, required):
    passed = actual < required if relation == "<" else actual > required
    checks.append({"name": name, "passed": passed,
                   "actual": actual, "relation": relation, "required": required})


kernel_polynomial = [F(0), F(-12), F(8)]
first_derivative = spatial_derivative(kernel_polynomial)
second_derivative = spatial_derivative(first_derivative)
origin_polynomial = add(second_derivative, scale(kernel_polynomial, F(2)))
equality("second_derivative_coefficients", second_derivative,
         list(map(F, [0, -75, 330, -224, 32])))
equality("K_second_plus_two_K_coefficients", origin_polynomial,
         list(map(F, [0, -99, 346, -224, 32])))
cubic = origin_polynomial[1:]
cubic_second = derivative(derivative(cubic))
equality("cubic_second_derivative", cubic_second, list(map(F, [-448, 192])))
equality("cubic_at_three", evaluate(cubic, F(3)), F(-213))
equality("cubic_at_four", evaluate(cubic, F(4)), F(-251))
inequality("cubic_convexity_lower_bound", evaluate(cubic_second, F(3)), ">", F(0))

exp_three_partial = sum((F(3**j, factorial(j)) for j in range(9)), F(0))
inequality("exp_three_positive_series_through_degree_eight", exp_three_partial, ">", F(20))
tail_factor = F(32 * 3**4 * 2**8 + 346 * 3**2 * 2**4)
equality("tail_n_two_coefficient", tail_factor, F(713376))
geometric_ratio_upper = F(3, 2)**8 / 20**5
inequality("geometric_ratio", geometric_ratio_upper, "<", F(1, 10))
tail_upper = tail_factor / (20**4 * F(9, 10))
inequality("entire_theta_tail", tail_upper, "<", F(5))
head_upper = F(-639, 81)
total_upper = head_upper + 5
equality("coarse_total_upper", total_upper, F(-26, 9))
inequality("origin_curvature_sign", total_upper, "<", F(0))
tilted_slope_upper = F(1, 20) - 1
equality("tilted_log_slope_upper", tilted_slope_upper, F(-19, 20))
equality("dilation_score_derivative_upper", 2 * tilted_slope_upper, F(-19, 10))
equality("support_leading_sign_full_degree", F(-6, factorial(12)), F(-1, 79833600))

failures = [c["name"] for c in checks if not c["passed"]]
certificate = {
    "scope": "Exact derivative and rational bounds for L915; no actual contact or flux sign is certified.",
    "variables": "Coefficient arrays are in increasing powers of v=pi*n^2 at u=0.",
    "source_input_not_checked_by_script": "Csordas arXiv:1309.0055v2, (4.2), Theorems4.1 and4.2(b), pp10-11.",
    "analytic_inputs_not_checked_by_script": [
        "3<pi<4; exp(1)<3; local uniform termwise differentiation.",
        "Evenness at zero; log-concavity in the square variable.",
        "Whole theta-series geometric majorization; L874 endpoint and integrability bounds.",
        "Zero mean and zero dilation expectation; the conditional strict-crossing contradiction."],
    "kernel_polynomial": kernel_polynomial,
    "first_derivative_polynomial": first_derivative,
    "second_derivative_polynomial": second_derivative,
    "origin_polynomial": origin_polynomial,
    "checks": checks,
    "bounds": {
        "first_term_upper": head_upper,
        "tail_upper": tail_upper,
        "tail_required": F(5),
        "origin_total_upper": total_upper,
        "origin_required": F(0),
        "tilted_log_slope_upper": tilted_slope_upper,
        "score_derivative_upper": 2 * tilted_slope_upper,
        "conditional_minimum_strict_crossings": 2,
        "proposed_crossings": 1},
    "summary": {"checks": len(checks), "passed": len(checks) - len(failures),
                "failures": failures, "actual_contact_established": False,
                "contact_flux_sign_established": False,
                "source_and_analytic_proof_audited_by_script": False}}

output = Path(__file__).with_name("contact-one-crossing-obstruction-184.json")
output.write_text(json.dumps(certificate, default=str, indent=2) + "\n")
print(f"Exact checks: {len(checks) - len(failures)}/{len(checks)}; failures: {failures}")
print(f"Whole tail upper {tail_upper} < required 5; origin upper {total_upper} < required 0.")
print("Conditional crossing lower bound in analytic proof: 2; proposed count: 1. No contact or flux sign certified.")
print(f"Certificate: {output}")
raise SystemExit(bool(failures))
