"""Exact arithmetic for the frozen, source-covered cubic diagnostic2217.

The analytic bounds are proved in C919k; this program checks their
rational constants, not the zeta zero computations imported there.
Run from the active notebook. No third-party packages or network.
"""

from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path
import json


def record(value):
    value = F(value)
    with localcontext() as context:
        context.prec = 35
        display = str(Decimal(value.numerator) / Decimal(value.denominator))
    return {"numerator": str(value.numerator),
            "denominator": str(value.denominator), "display_only": display}


def product(values):
    result = F(1)
    for value in values:
        result *= value
    return result


lower = [F(14), F(41, 2), F(49, 2)]
upper = [F(29, 2), F(43, 2), F(51, 2)]
band_upper, band_lower, cutoff, onset = 200, 100, 1000, 4
error_per_endpoint = F("0.10076") * 6 + F("0.24460") * 2 + F("8.08344")
main_count_lower = F(350, 11)
count_lower_strict = main_count_lower - 2 * error_per_endpoint
integer_count_lower = count_lower_strict.numerator // count_lower_strict.denominator + 1
gaps = [x**-2 - F(1, band_lower**2) for x in upper]
exterior_factors = [x**-2 + F(1, cutoff**2) for x in lower]
gap_product = product(gaps)
exterior_product = product(exterior_factors)
head = F(1, band_upper**(4*onset + 4)) * gap_product**2
shell_series_bound = F(1, cutoff**19) + F(1, 18 * cutoff**18)
tail = 18 * exterior_product**2 * shell_series_bound
margin = head - tail
cross_product = head.numerator * tail.denominator - tail.numerator * head.denominator
head_shift = F(1, band_upper**4)
tail_shift = F(1, cutoff**4)
relative_shift = tail_shift / head_shift

checks = {
    "exp6_lower_exceeds_200": F(8, 3)**6 > 200,
    "exp2_lower_exceeds_6": F(8, 3)**2 > 6,
    "exp2_upper_below_log_argument_lower": F(3)**2 < F(100) / F(44, 7),
    "error_per_endpoint_is_9_17720": error_per_endpoint == F("9.17720"),
    "strict_count_exceeds_13": count_lower_strict > 13,
    "integer_count_lower_is_14": integer_count_lower == 14,
    "cancelled_boxes_disjoint_below_surviving_band":
        all(lower[i] < upper[i] for i in range(3))
        and upper[0] < lower[1] and upper[1] < lower[2]
        and upper[-1] < band_lower,
    "all_survivor_gaps_positive": all(gap > 0 for gap in gaps),
    "head_positive": head > 0,
    "tail_positive": tail > 0,
    "strict_head_tail_margin": margin > 0 and cross_product > 0,
    "head_tail_ratio_exceeds_ten_million": head / tail > 10_000_000,
    "relative_shift_is_1_over_625": relative_shift == F(1, 625),
    "relative_shift_strictly_between_zero_and_one": 0 < relative_shift < 1,
}
failures = [name for name, passed in checks.items() if not passed]
certificate = {
    "step": "2217", "classification": "REPRODUCTION",
    "frozen_parameters": {"onset": onset, "surviving_band": "(100,200]",
                          "complete_real_head_cutoff": cutoff,
                          "boxes": [[record(a), record(b)] for a, b in zip(lower, upper)]},
    "count": {"strict_main_lower": record(main_count_lower),
              "strict_error_upper_per_endpoint": record(error_per_endpoint),
              "strict_count_lower": record(count_lower_strict),
              "required_count": 1, "integer_count_lower": integer_count_lower},
    "bounds": {"survivor_gaps": [record(x) for x in gaps],
               "gap_product": record(gap_product),
               "exterior_factors": [record(x) for x in exterior_factors],
               "exterior_product": record(exterior_product),
               "complete_shell_series_upper": record(shell_series_bound),
               "head_lower_at_4": record(head), "tail_upper_at_4": record(tail),
               "strict_margin_at_4": record(margin),
               "head_tail_ratio": record(head / tail),
               "comparison_cross_product": str(cross_product)},
    "all_r": {"head_extra_shift_lower": record(head_shift),
              "tail_extra_shift_upper": record(tail_shift),
              "relative_extra_shift_upper": record(relative_shift),
              "statement": "Q(X^(4+k) P_3) >= 200^(-4k)*(h4-t4*(1/625)^k) > 0, integer k>=0"},
    "checks": checks, "failures": failures,
    "qualifications": ["The complete analytic proof is C919k.",
                       "Platt/Bellotti-Wong computations and C919f backend remain imported.",
                       "Decimal output is explanatory only; proof values are exact fractions.",
                       "No arbitrary-degree, unshifted, heat-time or RH conclusion."],
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"count: >= {integer_count_lower}; required >= 1")
print(f"head lower: {record(head)['display_only']}; tail upper: {record(tail)['display_only']}")
print(f"margin: {record(margin)['display_only']}; required > 0")
print(f"head/tail: {record(head/tail)['display_only']}; required > 1")
print(f"all-r relative factor: {relative_shift}; required < 1")
print(f"checks: {sum(checks.values())}/{len(checks)}; failures: {failures}")
print(f"certificate: {output}")
raise SystemExit(bool(failures))
