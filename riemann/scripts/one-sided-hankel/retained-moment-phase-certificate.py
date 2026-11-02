"""Exact arithmetic for L660; analytic angle minimization is in the proof."""

import json
from fractions import Fraction as F
from pathlib import Path


def encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, list):
        return [encode(item) for item in value]
    return value


def log_lower(z):
    terms = [2 * z ** (2 * j + 1) / (2 * j + 1) for j in range(3)]
    return {"atanh_parameter": z, "terms": terms, "lower_bound": sum(terms)}


first = log_lower(F(2, 7))
second = log_lower(F(40, 161))
d = F(5, 4)
lower = first["lower_bound"] + F(121, 100) * second["lower_bound"] - F(4, 5)
threshold = F(2, 5)
max_moment_subtraction = F(1, 3) / d
remainder_bound = F(2, 3) * (16 + 4 + F(1, 3) / d**2)
checks = {
    "lambda_lower_above_two_fifths": lower > threshold,
    "phase_gap_is_two_fifteenths": threshold - max_moment_subtraction == F(2, 15),
    "neutral_degree_threshold_is_one_half": d * threshold == F(1, 2),
    "cutoff_degree_deficit_is_one_sixth": d * threshold - F(1, 3) == F(1, 6),
    "log_remainder_below_fourteen": remainder_bound < 14,
}
failures = [name for name, passed in checks.items() if not passed]
certificate = {
    "status": "EXACT_RATIONAL_ARITHMETIC_ONLY",
    "logarithm_lower_bounds": {"log_9_over_5": first, "log_201_over_121": second},
    "lambda_plus": {
        "exact_lower_bound": lower,
        "required_lower_bound": threshold,
        "positive_margin": lower - threshold,
    },
    "phase_gap": {
        "maximum_normalized_moment_subtraction": max_moment_subtraction,
        "strict_normalized_lower_bound": threshold - max_moment_subtraction,
        "required_for_neutrality": F(0),
        "normalized_neutral_degree_lower_bound": d * threshold,
        "normalized_available_degree_ceiling": F(1, 3),
        "strict_degree_deficit": d * threshold - F(1, 3),
    },
    "log_remainder": {"rational_bound": remainder_bound, "stated_bound": 14},
    "checks": checks,
    "failures": failures,
    "limitations": [
        "Does not verify analytic differentiation or angular minimization; those are proved in L660.",
        "Does not bound H, D, an arc mean, or a sum of spatial moments.",
        "No numerical approximation or finite-family screen is used.",
    ],
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(encode(certificate), indent=2) + "\n")
print(f"lambda_plus > {lower} > required {threshold}; margin {lower - threshold}")
print(f"retained phase slope / n > {threshold - max_moment_subtraction}; neutrality requires 0")
print("neutralizing degree / n > 1/2; available degree / n < 1/3")
print(f"log remainder bound {remainder_bound} < 14")
print(f"failures: {failures}; certificate: {path}")
if failures:
    raise SystemExit(1)
