"""Exact rational checks for C033e; analytic hypotheses are proved in the lemma."""

import json
from fractions import Fraction as F
from pathlib import Path


def p2(k):
    return F(2**k) if k >= 0 else F(1, 2**(-k))


def encode(value):
    if isinstance(value, F):
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, list):
        return [encode(item) for item in value]
    return value


n, h, degree = 4096, F(1, 256), 2336
vmin, vmax = h / 2, (F(n) - F(1, 2)) * h
r, rho = 520, 1040
eps = p2(-256)
cauchy_bound = 2 * p2(2080) * F(r, rho)**(degree + 1)
denominator_lower = 2 * vmin**2 / 33
denominator_perturbation = 16 * eps
separated_lower = p2(-24)
numerator_bound, numerator_error = p2(65), p2(66) * eps
quotient_error = numerator_error / separated_lower + (
    numerator_bound * denominator_perturbation / (separated_lower * p2(-23))
)
quotient_majorant = p2(117) * eps
sum_error, sum_majorant = n * h * quotient_error, p2(-135)
required = F(1, 64)
checks = {
    "prescribed_node_count": n == 4096,
    "prescribed_panel_width": h == F(1, 256),
    "first_node": vmin == F(1, 512),
    "last_node_below_16": vmax == F(8191, 512) and vmax < 16,
    "total_weight_16": n * h == 16,
    "argument_radius": 2 * F(16)**2 + F(16, 2) == r,
    "strict_circle_nesting": 0 < r < rho,
    "cauchy_prefactor": F(rho, rho-r) == 2,
    "explicit_degree_error": cauchy_bound == eps,
    "exact_denominator_above_dyadic": denominator_lower > p2(-23),
    "perturbed_denominator_separated": (
        denominator_lower - denominator_perturbation > separated_lower
    ),
    "denominator_dyadic_slack": p2(-23) - denominator_perturbation > separated_lower,
    "numerator_product_error": (p2(65) + 2) * eps <= numerator_error,
    "quotient_error_majorant": quotient_error <= quotient_majorant,
    "sum_error_majorant": sum_error <= sum_majorant,
    "required_error": sum_majorant < required,
}
failures = [name for name, passed in checks.items() if not passed]
certificate = {
    "scope": "Exact arithmetic comparisons only; C033e supplies analytic proof, no parameter sampling.",
    "rule": {"nodes": n, "h": h, "v_j": "(2*j+1)/512, 0<=j<4096", "vmin": vmin, "vmax": vmax},
    "taylor": {"degree": degree, "r": r, "rho": rho, "exp_circle_upper": "2^2080", "error": cauchy_bound},
    "bounds": {
        "exact_denominator_lower": denominator_lower,
        "denominator_perturbation": denominator_perturbation,
        "perturbed_denominator_lower": separated_lower,
        "numerator_modulus": numerator_bound,
        "numerator_error": numerator_error,
        "quotient_error": quotient_error,
        "quotient_majorant": quotient_majorant,
        "sum_error": sum_error,
        "sum_majorant": sum_majorant,
        "required": required,
    },
    "checks": checks,
    "failures": failures,
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(encode(certificate), indent=2) + "\n")
print(f"Exact rational comparisons: {sum(checks.values())}/{len(checks)} passed")
print("Certified sum error <= 2^-135; required <= 1/64")
print("All perturbed node denominators > 2^-24; original lower = 1/(33*2^17)")
print(f"Failures: {failures}")
print(f"Certificate: {output.relative_to(Path.cwd())}")
if failures:
    raise SystemExit(1)
