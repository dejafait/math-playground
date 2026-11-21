#!/usr/bin/env python3
"""Exact scalar arithmetic for L960; does not verify analytic/model premises."""
from fractions import Fraction as F
from pathlib import Path
import json


def rational(value):
    return {"numerator": value.numerator, "denominator": value.denominator}


p = F(101, 200000000)
q = F(142, 10000000) + F(1, 250000000000)
m = F(1, 790)
linear = 25 * p + q
constant = F(81, 2) * p + p * q
reserve = 13 * m * m - linear * m - constant
derivative = 26 * m - linear
claimed_reserve = F(107199260708819659, 312050000000000000000000)
claimed_derivative = F(649470206171, 19750000000000)
threshold = F(3, 10000000)
checks = {
    "q_includes_companion_error": q == 2 * F(71, 10000000) + F(1, 250000000000),
    "p_is_half_remainder": p == F(101, 100000000) / 2,
    "reserve_matches_source": reserve == claimed_reserve,
    "derivative_matches_source": derivative == claimed_derivative,
    "reserve_exceeds_required_threshold": reserve > threshold,
    "derivative_at_modulus_floor_positive": derivative > 0,
    "second_derivative_positive": F(26) > 0,
}
values = {
    "p": p, "q": q, "modulus_floor": m,
    "positive_base": 13 * m * m,
    "error_p_times_25m": 25 * p * m,
    "error_q_times_m": q * m,
    "error_p_times_81_over_2": F(81, 2) * p,
    "error_product_pq": p * q,
    "linear_coefficient": linear, "constant_charge": constant,
    "reserve": reserve, "required_reserve": threshold,
    "reserve_minus_required": reserve - threshold,
    "derivative_at_modulus_floor": derivative, "second_derivative": F(26),
}
certificate = {
    "scope": "Exact scalar reserve only; proof and conditional premises are in L960.",
    "values": {key: rational(value) for key, value in values.items()},
    "checks": checks,
    "failures": [key for key, passed in checks.items() if not passed],
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {certificate['failures']}")
print(f"Reserve: {reserve}; required: > {threshold}; excess: {reserve - threshold}")
print(f"Derivative at modulus floor: {derivative}; required: > 0; Q'' = 26")
print(f"Certificate: {output.relative_to(Path.cwd())}")
raise SystemExit(bool(certificate["failures"]))
