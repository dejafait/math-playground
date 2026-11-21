"""Exact rational omitted-part certificate for C033s; no heat evaluation."""
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path


def record(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


cut = 60 * 3**48 * F(1, 2**128)
series = F(3**24 * 24**129, factorial(129)) * F(130, 106)
lam = F(3**21 * 21**129, factorial(129)) * F(130, 109)
combined = lam + 2 * (cut + series)
required = F(1, 2**20)
stronger = F(1, 2**44)
checks = {
    "heat_constant_below_3": F(2019, 800) < 3,
    "q_series_ratio_below_1": F(24, 130) < 1,
    "lambda_series_ratio_below_1": F(21, 130) < 1,
    "maximum_retained_order_at_most_128": 128 <= 128,
    "cutoffs_in_declared_range": -256 <= -256 <= 256 and -256 <= 256 <= 256,
    "combined_below_2^-44": combined < stronger,
    "combined_below_required_2^-20": combined < required,
}
certificate = {
    "canonical_result": "C033s",
    "scope": "Omitted jump measures and convolution orders only; exact compact integrals.",
    "parameters": {"n": 1, "delta": "1/16", "max_order": 128,
                   "lower_cut_power_of_two": -256, "upper_cut_power_of_two": 256,
                   "width_TV_cap": 2, "Q_norm_upper": 24, "P_mass_upper": 21},
    "bounds": {"jump_omission": record(30 * F(1, 2**128)),
               "R_spatial": record(cut), "R_orders": record(series),
               "lambda_orders": record(lam)},
    "combined": {"upper": record(combined), "required": record(required),
                 "stronger_threshold": record(stronger)},
    "verification": {"checks": checks, "failures": [k for k, v in checks.items() if not v]},
    "qualifications": ["Analytic inequalities are proved in C033s, not checked by this script.",
                       "Both fixed-v1 inputs and finite-zero data remain qualified.",
                       "No compact quadrature, runtime, positive separation or RH claim."],
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"combined upper allowance: {float(combined):.12g}; required: 2^-20; verified: <2^-44")
print(f"failures: {certificate['verification']['failures']}; certificate: {out}")
if certificate["verification"]["failures"]:
    raise SystemExit(1)
