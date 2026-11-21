#!/usr/bin/env python3
"""Exact rational scalar certificate for C048g, without parameter sampling."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json


def rational(x):
    x = F(x)
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def exp_bounds(x, n):
    x = F(x)
    assert 0 < x < n + 2
    term = total = F(1)
    for k in range(1, n + 1):
        term *= x / k
        total += term
    omitted = term * x / (n + 1)
    ratio = x / (n + 2)
    upper = total + omitted / (1 - ratio)
    return total, upper, {
        "argument": rational(x), "degree": n,
        "lower": rational(total), "first_omitted": rational(omitted),
        "tail_ratio_upper": rational(ratio), "upper": rational(upper),
    }


def atan_bounds(x, n):
    x = F(x)
    assert 0 < x < 1 and n % 2 == 0
    lower = sum(((-1)**k * x**(2*k+1) / (2*k+1)
                 for k in range(n)), F(0))
    upper = lower + x**(2*n+1)/(2*n+1)
    return lower, upper, {"argument": rational(x), "terms": n,
                          "lower": rational(lower), "upper": rational(upper)}


def root_bounds(x):
    x = F(x)
    scale = 10**18
    k = isqrt(x.numerator * scale**2 // x.denominator)
    lower, upper = F(k, scale), F(k+1, scale)
    assert lower**2 <= x < upper**2
    return lower, upper


checks = []


def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    assert relation in ("<", ">")
    passed = actual < required if relation == "<" else actual > required
    checks.append({"name": name, "actual": rational(actual),
                   "relation": relation, "required": rational(required),
                   "passed": passed})


e3_lower, _, exp3 = exp_bounds(3, 8)
check("exp3_partial_sum_above_20", e3_lower, ">", 20)
check("exp12_floor_pays_rate", F(20**4, 12**3), ">", F(675, 8))
check("theta_amplitude", 1 + F(1, 14) + F(20, 343), "<", F(3, 2))
check("mode_ratio", F(81, 16*98), "<", F(1, 10))

e_lower, e_upper, exp12 = exp_bounds(12, 120)
e_lo = F(1627547914190039, 10**10)
e_hi = F(1627547914190040, 10**10)
check("exp12_lower", e_lower, ">", e_lo)
check("exp12_upper", e_upper, "<", e_hi)
a_lo, a_hi, atan5 = atan_bounds(F(1, 5), 24)
b_lo, b_hi, atan239 = atan_bounds(F(1, 239), 8)
pi_lower, pi_upper = 16*a_lo - 4*b_hi, 16*a_hi - 4*b_lo
pi_lo = F(3141592653589793, 10**15)
pi_hi = F(3141592653589794, 10**15)
check("pi_lower", pi_lower, ">", pi_lo)
check("pi_upper", pi_upper, "<", pi_hi)

y_lo, y_hi = e_lo / 12**4, e_hi / 12**4
c = F(19, 45)
check("y0_monotonicity_threshold", y_lo, ">", F(45, 38))
rad_lo, rad_hi = 6*y_lo/pi_hi, 6*y_hi/pi_lo
root_lo = root_bounds(rad_lo)[0]
root_hi = root_bounds(rad_hi)[1]
ex_lo, ex_hi, exp_eighth = exp_bounds(F(1, 8), 30)
den_lo, _, exp_den_lo = exp_bounds(c*y_lo, 80)
_, den_hi, exp_den_hi = exp_bounds(c*y_hi, 80)
prefactor = F(3, 2) / F(62, 25)
lower = prefactor * ex_lo * root_lo / den_hi
upper = prefactor * ex_hi * root_hi / den_lo
threshold = F(48257, 500000)
check("A_plus_upper", upper, "<", threshold)

scale = 10**15
rounded_lo = F((lower.numerator*scale)//lower.denominator, scale)
rounded_hi = F((upper.numerator*scale)//upper.denominator+1, scale)
check("A_plus_rounded_lower", lower, ">", rounded_lo)
check("A_plus_rounded_upper", upper, "<", rounded_hi)
slack_floor = F(1, 10**9)
check("A_plus_slack", threshold-upper, ">", slack_floor)

certificate = {
    "scope": "C048g fixed scalar comparisons; full-sector analytic proof is canonical.",
    "exp3": exp3,
    "exp12": exp12,
    "pi_machin": {"identity": "pi=16 atan(1/5)-4 atan(1/239)",
                  "atan5": atan5, "atan239": atan239},
    "scalar_intervals": {"exp12": [rational(e_lo), rational(e_hi)],
                         "pi": [rational(pi_lo), rational(pi_hi)],
                         "y0": [rational(y_lo), rational(y_hi)]},
    "root": {"lower_radicand": rational(rad_lo),
             "upper_radicand": rational(rad_hi),
             "lower": rational(root_lo), "upper": rational(root_hi),
             "lower_square_le_lower_radicand": root_lo**2 <= rad_lo,
             "upper_square_gt_upper_radicand": root_hi**2 > rad_hi},
    "exp_eighth": exp_eighth,
    "denominator_lower": exp_den_lo,
    "denominator_upper": exp_den_hi,
    "A_plus": {"lower": rational(lower), "upper": rational(upper),
               "required_strict_upper": rational(threshold),
               "upper_slack": rational(threshold-upper)},
    "A_plus_rounded": {"lower": rational(rounded_lo), "upper": rational(rounded_hi),
                       "required_strict_upper": rational(threshold),
                       "certified_slack_lower": rational(slack_floor)},
    "checks": checks,
    "failures": [check["name"] for check in checks if not check["passed"]],
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Exact scalar comparisons: {len(checks)}; failures: {certificate['failures']}")
print(f"A_+ display: {float(rounded_lo):.15f} .. {float(rounded_hi):.15f}")
print(f"Required < {float(threshold):.6f}; certified slack > {float(slack_floor):.1g}")
print(f"Certificate: {destination.relative_to(Path.cwd())}")
if certificate["failures"]:
    raise SystemExit(1)
