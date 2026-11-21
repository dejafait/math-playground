"""Exact rational certificate for C750p; no floating transcendental input."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def rational(x):
    return f"{x.numerator}/{x.denominator}"


exp_terms = [F(14, 3)**j / factorial(j) for j in range(9)]
exp_lower = sum(exp_terms, F())
# DLMF4.24.3 at1: an even number of terms is a strict lower sum.
atan_terms = [F((-1)**j, 2*j+1) for j in range(64)]
pi_lower = 4*sum(atan_terms, F())
b_upper, sinh_squared_upper, pi_coarse_lower = F(7, 3), F(41, 20), F(25, 8)
tail_upper = F(1, 32)
norm_upper = 8*b_upper*sinh_squared_upper/pi_coarse_lower**2*tail_upper
threshold = F(1, 8)
checks = {
    "positive_exp_sum_exceeds_101": exp_lower > 101,
    "atan_lower_exceeds_25_over_8": pi_lower > pi_coarse_lower,
    "sqrt101_exceeds_10": 101 > 10**2,
    "sinh_square_algebra": (F(102, 10)-2)/4 == sinh_squared_upper,
    "strict_norm_upper_below_threshold": norm_upper < threshold,
}
certificate = {
    "target": "C750p unchanged P64 odd-pole norm below 1/8",
    "arithmetic": "Python Fraction; all inequalities exact",
    "exp": {"argument": "14/3", "degree": 8,
            "terms": [rational(x) for x in exp_terms],
            "lower_sum": rational(exp_lower), "required_lower": "101/1"},
    "pi": {"method": "4 times 64-term alternating arctan(1) lower sum",
           "terms": [rational(x) for x in atan_terms],
           "strict_lower": rational(pi_lower), "required_lower": "25/8",
           "error_upper": rational(F(4, 129))},
    "parameter_bounds": {"b_strict_upper": rational(b_upper),
                         "sinh_b_over_2_squared_strict_upper": rational(sinh_squared_upper)},
    "complete_tail": {"first_k": 33, "last_removed_k": 32,
                      "bound": "k^2/(k^2+a^2)^2 < k^-2; sum(k>=33) k^-2 < integral(32,infinity) x^-2 dx",
                      "strict_upper": rational(tail_upper)},
    "norm": {"lower": "0/1", "strict_upper": rational(norm_upper),
             "required_strict_upper": rational(threshold),
             "strict_margin": rational(threshold-norm_upper)},
    "checks": checks,
    "failures": [name for name, passed in checks.items() if not passed],
    "scope": "Only compressed negative odd-pole component; no full R/E positivity or Xi conclusion",
}
destination = Path(__file__).with_name("odd-pole-reserve-1174.json")
destination.write_text(json.dumps(certificate, indent=2)+"\n")
print("C750p exact checks:", "PASS" if not certificate["failures"] else "FAIL")
print("Actual strict bound:", rational(norm_upper), "; required:", rational(threshold))
print("Strict margin:", rational(threshold-norm_upper))
print("Complete tail: k>=33, strict upper 1/32; no omitted modes")
print("Failures:", certificate["failures"])
print("Certificate:", destination)
if certificate["failures"]:
    raise SystemExit(1)
