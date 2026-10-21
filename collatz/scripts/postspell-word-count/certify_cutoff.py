#!/usr/bin/env python3
"""Exact certificate for the fixed L041/Corollary 2 scalar cutoff.

Run from the active notebook: python3 scripts/postspell-word-count/certify_cutoff.py
No floating-point value is used. The certificate tests scalar inequalities;
it does not construct an actual Collatz word or cycle.
"""

from fractions import Fraction as F
import json
from pathlib import Path


def rational(value):
    value = F(value)
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def log_bounds(integer, terms=64):
    # log t = 2 sum_{j>=0} x^(2j+1)/(2j+1), x=(t-1)/(t+1).
    # The omitted positive tail is strictly below the displayed geometric bound.
    x = F(integer - 1, integer + 1)
    lower = 2 * sum((x ** (2*j + 1) / (2*j + 1) for j in range(terms)), F(0))
    tail = 2 * x ** (2*terms + 1) / ((2*terms + 1) * (1 - x*x))
    return lower, lower + tail


def q(r):
    return sum((F(23, 8)**j for j in range(r)), F(0))


def main():
    threshold = 225640000
    c = 3 * threshold // 2
    q12, q13 = q(12), q(13)
    a12, a13 = F(399, 5)*q12, F(399, 5)*q13
    rhs12 = F(8334, 5)*q12 + F(828, 1034)
    margin12 = F(c) - rhs12
    k, length = 225640001, 357630941
    even = length-k
    js = [4] + [2]*12
    hs = [225639881] + [3]*12
    tails = [131990888] + [2]*12
    lo2, hi2 = log_bounds(2)
    lo3, hi3 = log_bounds(3)
    decimal_lo2, decimal_hi2 = F(6931471805599453, 10**16), F(6931471805599454, 10**16)
    decimal_lo3, decimal_hi3 = F(10986122886681096, 10**16), F(10986122886681097, 10**16)
    lambda_lower = length*decimal_lo2-k*decimal_hi3
    lambda_upper = length*decimal_hi2-k*decimal_lo3
    lambda_cap = F(23*13, 517)
    margin13 = 17*a13-length

    checks = {
        "exp_series_5_gt_27_over_10": F(163, 60) > F(27, 10),
        "exp20_gt_C": 27**20 > c*10**20,
        "exp3_gt_12": 27**3 > 12*10**3,
        "A12_lt_C": a12 < c,
        "r12_margin_gt_54971760": margin12 > 54971760,
        "log_ratio_gt_3_over_2": 3**2 > 2**3,
        "K13_gt_imported_threshold": k > threshold,
        "J13_guards": len(js) == 13 and all(j >= 2 for j in js),
        "H13_guards": len(hs) == 13 and all(h >= 3 for h in hs),
        "tail13_guards": len(tails) == 13 and all(a >= 0 and a % 18 == 2 for a in tails),
        "K13_matches_word_counts": sum(3*j+h for j, h in zip(js, hs)) == k,
        "L13_matches_word_counts": sum(j+a for j, a in zip(js, tails)) == even,
        "N13_matches_word_counts": sum(4*j+h+a for j, h, a in zip(js, hs, tails)) == length,
        "N13_gt_13r": length > 13*13,
        "log_N13_gt_17_via_e_lt_3": length > 3**17,
        "r13_rhs_margin_positive": margin13 > 0,
        "log2_decimal_lower_certified": decimal_lo2 < lo2,
        "log2_decimal_upper_certified": hi2 < decimal_hi2,
        "log3_decimal_lower_certified": decimal_lo3 < lo3,
        "log3_decimal_upper_certified": hi3 < decimal_hi3,
        "lambda13_gt_1_over_2": lambda_lower > F(1, 2),
        "lambda13_lt_53_over_100": lambda_upper < F(53, 100),
        "53_over_100_lt_lambda_cap": F(53, 100) < lambda_cap,
    }
    failures = [name for name, passed in checks.items() if not passed]
    certificate = {
        "scope": "Fixed L041 length inequality plus exact total word counts, primitive scaling, imported K0 threshold and L041 positive linear-form upper bound; scalar feasibility is not an orbit.",
        "r12": {
            "threshold": threshold, "C": c, "Q": rational(q12), "A": rational(a12),
            "conservative_rhs": rational(rhs12), "margin": rational(margin12),
            "exp20_integer_lhs": str(27**20), "exp20_integer_rhs": str(c*10**20),
        },
        "r13": {
            "r": 13, "K": k, "L": even, "N": length, "d": 1, "K0": k, "L0": even,
            "J": js, "H": hs, "a": tails, "Q": rational(q13), "A": rational(a13),
            "lower_rhs_margin": rational(margin13),
            "lambda_lower": rational(lambda_lower), "lambda_upper": rational(lambda_upper),
            "lambda_cap": rational(lambda_cap),
        },
        "log_enclosures": {
            "method": "positive atanh series with geometric tail", "terms": 64,
            "log2_lower": rational(lo2), "log2_upper": rational(hi2),
            "log3_lower": rational(lo3), "log3_upper": rational(hi3),
            "decimal_log2_lower": rational(decimal_lo2), "decimal_log2_upper": rational(decimal_hi2),
            "decimal_log3_lower": rational(decimal_lo3), "decimal_log3_upper": rational(decimal_hi3),
        },
        "checks": checks, "failures": failures,
    }
    path = Path(__file__).with_name("cutoff-certificate.json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"cutoff: r=3..12 excluded; scalar feasible at r=13")
    print(f"r12: exact margin > {margin12.numerator // margin12.denominator}; required > 0")
    print(f"r13: 17*A(13)-N > {margin13.numerator // margin13.denominator}; required > 0")
    print("r13: certified 1/2 < Lambda < 53/100 < 299/517; required 0 < Lambda < 23r/517")
    print(f"checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}")
    print(f"certificate: {path.as_posix()}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
