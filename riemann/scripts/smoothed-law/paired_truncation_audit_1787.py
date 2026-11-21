"""Independent rational audit of C033s; no profile or observable evaluation."""
import json
from fractions import Fraction as F
from pathlib import Path


def record(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def fraction(value):
    return F(int(value["numerator"]), int(value["denominator"]))


def omitted_order_bound(norm):
    # Recurrence, independent of the original factorial expression.
    first = F(1)
    for order in range(1, 130):
        first *= F(norm, order)
    return 3**norm * first / (1 - F(norm, 130))


source = Path(__file__).with_name("paired_truncation_1779.json")
old = json.loads(source.read_text())
epsilon = (24 + 6) * F(1, 2**128)
cut = 2 * epsilon * 3**(2 * 24)
r_orders = omitted_order_bound(24)
lambda_orders = omitted_order_bound(21)
combined = lambda_orders + 2 * (cut + r_orders)
required, threshold = F(1, 2**20), F(1, 2**44)
expected_bounds = {
    "jump_omission": epsilon,
    "R_spatial": cut,
    "R_orders": r_orders,
    "lambda_orders": lambda_orders,
}
expected_parameters = {
    "n": 1, "delta": "1/16", "max_order": 128,
    "lower_cut_power_of_two": -256, "upper_cut_power_of_two": 256,
    "width_TV_cap": 2, "Q_norm_upper": 24, "P_mass_upper": 21,
}
checks = {
    "source_result": old["canonical_result"] == "C033s",
    "parameters_match": old["parameters"] == expected_parameters,
    "constant_sum": F(69, 16) + F(9, 25) == F(1869, 400),
    "envelope_constant": F(1, 8) + F(1869, 800) + F(1, 16) == F(2019, 800),
    "envelope_constant_below_3": F(2019, 800) < 3,
    "q_tail_ratio": 0 < F(24, 130) < 1,
    "lambda_tail_ratio": 0 < F(21, 130) < 1,
    "profile_range": 1 <= F(7, 6) <= F(5, 4) <= 2,
    "paired_kernel_bound": F(8, 15) < 1,
    **{f"source_{name}_matches": fraction(old["bounds"][name]) == value
       for name, value in expected_bounds.items()},
    "source_combined_matches": fraction(old["combined"]["upper"]) == combined,
    "source_required_matches": fraction(old["combined"]["required"]) == required,
    "source_threshold_matches": fraction(old["combined"]["stronger_threshold"]) == threshold,
    "combined_below_2^-44": combined.numerator * 2**44 < combined.denominator,
    "combined_below_2^-20": combined.numerator * 2**20 < combined.denominator,
}
failures = [name for name, passed in checks.items() if not passed]
certificate = {
    "canonical_result": "C033s",
    "source_certificate": "scripts/smoothed-law/paired_truncation_1779.json",
    "method": "Exact Fraction recurrence through order129; full source-value comparisons.",
    "parameters": expected_parameters,
    "bounds": {name: record(value) for name, value in expected_bounds.items()},
    "combined": {"upper": record(combined), "required": record(required),
                 "threshold": record(threshold)},
    "integer_comparisons": {
        "denominator": str(combined.denominator),
        "numerator_times_2^44": str(combined.numerator * 2**44),
        "positive_gap_at_2^-44": str(combined.denominator - combined.numerator * 2**44),
        "positive_gap_at_2^-20": str(combined.denominator - combined.numerator * 2**20),
    },
    "verification": {"checks": checks, "failures": failures},
    "qualifications": [
        "Analytic hypotheses and measure arguments are audited in canonical C033s, not by this script.",
        "No source-wide or finite-zero certification; fixed-v1 qualifications retained.",
        "No new cutoff/order, compact quadrature, observable evaluation or RH assertion.",
    ],
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Reconstructed allowance {float(combined):.12g}; audit threshold 2^-44={float(threshold):.12g}; required 2^-20={float(required):.12g}")
print(f"Exact checks: {len(checks)}; failures: {failures}; certificate: {out}")
if failures:
    raise SystemExit(1)
