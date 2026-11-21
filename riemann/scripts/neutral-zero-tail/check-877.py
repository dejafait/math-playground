#!/usr/bin/env python3
"""Exact scalar checks for the analytic proof in C750d; no zero sampling."""
from fractions import Fraction as Q
from pathlib import Path
import json

H = 3 * 10**12
checks = []


def encode(value):
    value = Q(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def less(name, actual, required):
    actual, required = Q(actual), Q(required)
    checks.append({"name": name, "actual": encode(actual),
                   "required_strict_upper": encode(required),
                   "pass": actual < required})


# These only verify scalar consequences; analytic hypotheses are in C750d.
less("exp_5_over_4_series_exceeds_3", 3, 1 + Q(5, 4) + Q(25, 32))
less("sin_pi_over_4_exceeds_2_over_3_squared", Q(4, 9), Q(1, 2))
less("twice_sqrt3_exceeds_10_over_3_squared", Q(100, 9), 12)
less("mu2_lower_exceeds_1", 1, Q(5 * 4, 18))
less("log_H_less_30_via_e_gt_8_over_3", H * 3**30, 8**30)
less("H_above_2pi_e_using_pi_lt4_e_lt3", 24, H)
less("sqrt10_less_4_squared", 10, 16)

gram_loss = Q(1, 2) - 3 * Q(1, 10)
assert gram_loss == Q(1, 5)
phi_second_sup = 352 * 10**2 + 2 * (5 * 10) * 12 + 12**2
less("phi_second_derivative_sup", phi_second_sup, 37000)
less("phi_L1_plus_second_L1", 5 * (1 + 37000), 200000)
mode_l1 = 1 + 16
projection_l1_bound = mode_l1 * 4
coordinate_l1_bound = mode_l1 * (1 + projection_l1_bound)
assert coordinate_l1_bound == 1173
less("all_ten_coordinate_L1_plus_second_L1", 4 * 1173 * 200000, 10**9)

positive_tail = Q(91, 54 * H**3) + Q(1687, 100 * H**4)
both_tail = 2 * positive_tail
assert both_tail == Q(91, 27 * H**3) + Q(1687, 50 * H**4)
A = 36 * 10**9
epsilon = A**2 * both_tail
required = Q(2, 10**16)
less("epsilon", epsilon, required)

certificate = {
    "scope": "C750d analytic U12 tail specialization; exact scalar arithmetic only",
    "H": H,
    "analytic_qualifications": [
        "L750(11) cutoff derivative bounds are mathematical inputs, not replayed here",
        "C750d proves exact moment and original-L2 projection bounds analytically",
        "BPT Lemma 1 is imported with multiplicity and half endpoint weights",
        "L753(10) bounds the holomorphic product on the full zero strip",
        "No finite Gram sign, zero ordinate data, RH or global positivity is verified",
    ],
    "constants": {
        "gram_lower_factor_times_T": encode(gram_loss),
        "phi_second_sup": phi_second_sup,
        "b_sine_l1_upper": mode_l1,
        "projection_coefficient_l1_upper": projection_l1_bound,
        "e_sine_l1_upper": coordinate_l1_bound,
        "all_coordinates_L1_plus_second_L1_upper": 10**9,
        "strip_A_per_coefficient_norm": A,
    },
    "positive_height_power_tail_upper": encode(positive_tail),
    "both_height_power_tail_upper": encode(both_tail),
    "epsilon": encode(epsilon),
    "required_upper": encode(required),
    "strict_slack": encode(required - epsilon),
    "checks": checks,
    "failures": [entry["name"] for entry in checks if not entry["pass"]],
}
path = Path(__file__).with_name("certificate-877.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"{len(checks)} exact scalar checks; failures={len(certificate['failures'])}")
print(f"actual epsilon upper: {epsilon}; required strict upper: {required}")
print("required for later positivity: a separately certified Gram margin > epsilon + finite errors (unknown)")
print(f"certificate: {path}")
if certificate["failures"]:
    raise SystemExit(1)
