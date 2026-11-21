#!/usr/bin/env python3
"""Exact scalar certificate for C048d; no parameter sampling/quadrature."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json


def rational(q):
    q = F(q)
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def exp_bounds(x, n):
    """For x>0, S_n < exp(x) < S_n+t_(n+1)/(1-x/(n+2))."""
    x = F(x)
    assert x > 0 and x < n+2
    term = F(1)
    total = term
    for k in range(1, n+1):
        term *= x/k
        total += term
    first_omitted = term*x/(n+1)
    ratio = x/(n+2)
    upper = total+first_omitted/(1-ratio)
    return total, upper, {"argument": rational(x), "degree": n,
                         "partial_sum": rational(total),
                         "first_omitted": rational(first_omitted),
                         "tail_ratio_upper": rational(ratio),
                         "upper": rational(upper)}


def atan_bounds(x, n):
    """Alternating atan sum through k=n-1, with next-term remainder."""
    x = F(x)
    assert 0 < x < 1 and n % 2 == 0
    total = sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(n)), F(0))
    upper = total+x**(2*n+1)/F(2*n+1)
    return total, upper, {"argument": rational(x), "terms": n,
                         "lower": rational(total), "upper": rational(upper)}


def root_bounds(q):
    q = F(q)
    scale = 10**18
    k = isqrt(q.numerator*scale**2 // q.denominator)
    lo, hi = F(k, scale), F(k+1, scale)
    assert lo**2 <= q < hi**2
    return lo, hi


checks = []


def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    ok = actual < required if relation == "<" else actual > required
    checks.append({"name": name, "actual": rational(actual),
                   "relation": relation, "required": rational(required),
                   "passed": ok})


e_lo_raw, e_hi_raw, exp12 = exp_bounds(12, 120)
e_lo = F(1627547914190039, 10**10)
e_hi = F(1627547914190040, 10**10)
check("exp12_lower", e_lo_raw, ">", e_lo)
check("exp12_upper", e_hi_raw, "<", e_hi)
a_lo, a_hi, atan5 = atan_bounds(F(1, 5), 24)
b_lo, b_hi, atan239 = atan_bounds(F(1, 239), 8)
pi_lo_raw, pi_hi_raw = 16*a_lo-4*b_hi, 16*a_hi-4*b_lo
pi_lo = F(3141592653589793, 10**15)
pi_hi = F(3141592653589794, 10**15)
check("pi_lower", pi_lo_raw, ">", pi_lo)
check("pi_upper", pi_hi_raw, "<", pi_hi)

y_lo, y_hi = e_lo/12**4, e_hi/12**4
c = F(13, 30)
check("y0_above_monotonicity_threshold", y_lo, ">", F(15, 13))
# Each replacement below is monotone separately; no dependency assumption.
rad_lo, rad_hi = 6*y_lo/pi_hi, 6*y_hi/pi_lo
root_lo = root_bounds(rad_lo)[0]
root_hi = root_bounds(rad_hi)[1]
den_lo, _, exp_lower = exp_bounds(c*y_lo, 80)
_, den_hi, exp_upper = exp_bounds(c*y_hi, 80)
lower = F(10, 13)*root_lo/den_hi
upper = F(10, 13)*root_hi/den_lo
threshold = F(24819, 250000)
check("A_g_upper", upper, "<", threshold)
check("A_g_slack", threshold-upper, ">", F(1, 10**7))
rounded_lower = F(99275864521823, 10**15)
rounded_upper = F(99275864521825, 10**15)
check("A_g_rounded_lower", lower, ">", rounded_lower)
check("A_g_rounded_upper", upper, "<", rounded_upper)

certificate = {
    "scope": "Fixed scalar comparisons for C048d; uniform analytic proof is canonical.",
    "exp12_series": exp12,
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
    "denominator_lower_series": exp_lower,
    "denominator_upper_series": exp_upper,
    "A_g": {"lower": rational(lower), "upper": rational(upper),
            "required_strict_upper": rational(threshold),
            "upper_slack": rational(threshold-upper)},
    "A_g_rounded": {"lower": rational(rounded_lower),
                    "upper": rational(rounded_upper),
                    "required_strict_upper": rational(threshold),
                    "certified_slack_lower": rational(F(1, 10**7))},
    "checks": checks,
    "failures": [item["name"] for item in checks if not item["passed"]],
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"Exact scalar comparisons: {len(checks)}; failures: {certificate['failures']}")
print(f"A_g decimal display: {float(lower):.15f} .. {float(upper):.15f}")
print(f"Required < {float(threshold):.6f}; certified slack > {float(threshold-upper):.10g}")
print(f"Certificate: {destination.relative_to(Path.cwd())}")
if certificate["failures"]:
    raise SystemExit(1)
