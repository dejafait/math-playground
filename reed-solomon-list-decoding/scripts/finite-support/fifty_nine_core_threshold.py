"""Exact arithmetic for L041; does not compute labeled family maxima."""

import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path


def rational(value):
    return {"numerator": value.numerator, "denominator": value.denominator}


def factorial_binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def main():
    q = 65537**28
    threshold_denominator = 2**128
    T = Fraction(q, threshold_denominator)
    M, threshold_remainder = divmod(q, threshold_denominator)
    N = comb(1024, 59)
    D = comb(68, 59)
    endpoint = D * (M + 1)
    b, cap_remainder = divmod(endpoint - 1, N)
    ordinary_numerator = comb(965, 5)
    ordinary_denominator = comb(9, 5)
    ordinary_cap, ordinary_remainder = divmod(
        ordinary_numerator, ordinary_denominator
    )

    # Proposition 1.1.4: strength five, innermost floor first.
    nested = 1
    stages = []
    for i in range(4, -1, -1):
        numerator = (965 - i) * nested
        denominator = 9 - i
        quotient, remainder = divmod(numerator, denominator)
        stages.append({
            "i": i, "input": nested, "multiplier": 965 - i,
            "denominator": denominator, "numerator": numerator,
            "quotient": quotient, "remainder": remainder,
        })
        nested = quotient

    global_values = {}
    for name, cap in (("benchmark", b), ("adjacent", b + 1),
                      ("ordinary", ordinary_cap), ("nested", nested)):
        numerator = N * cap
        quotient, remainder = divmod(numerator, D)
        global_values[name] = {
            "local_cap": cap, "numerator": numerator,
            "quotient": quotient, "remainder": remainder,
            "threshold_integer_slack": M - quotient,
            "strict_endpoint_slack": endpoint - numerator,
            "safe_certificate": quotient * threshold_denominator <= q,
            "unfloored_ratio_to_threshold": rational(Fraction(numerator, D) / T),
        }

    support_ratio = Fraction(comb(1024, 64), comb(68, 64))
    ordinary_ratio = Fraction(N * ordinary_numerator, D * ordinary_denominator)
    nested_ratio = Fraction(N * nested, D) / T
    checks = {
        "N_factorial": N == factorial_binomial(1024, 59),
        "D_factorial": D == factorial_binomial(68, 59),
        "ordinary_numerator_factorial": ordinary_numerator == factorial_binomial(965, 5),
        "ordinary_denominator_factorial": ordinary_denominator == factorial_binomial(9, 5),
        "threshold_division": q == M * threshold_denominator + threshold_remainder,
        "threshold_fractional_part": 0 < threshold_remainder < threshold_denominator,
        "threshold_bracket": 2**320 < T < 2**321,
        "cap_division": endpoint - 1 == N * b + cap_remainder and 0 <= cap_remainder < N,
        "greatest_cap_lower": N * b < endpoint,
        "greatest_cap_upper": N * (b + 1) >= endpoint,
        "benchmark_pass": global_values["benchmark"]["safe_certificate"],
        "adjacent_fail": not global_values["adjacent"]["safe_certificate"],
        "nonuniform_last_pass": (endpoint - 1) // D == M,
        "nonuniform_first_fail": endpoint // D == M + 1,
        "ordinary_division": ordinary_numerator == ordinary_denominator * ordinary_cap + ordinary_remainder,
        "nested_divisions": all(
            s["numerator"] == s["denominator"] * s["quotient"] + s["remainder"]
            and 0 <= s["remainder"] < s["denominator"] for s in stages
        ),
        "nested_expanded_formula": nested == (965 * ((964 * ((963 * ((962 * (961 // 5)) // 6)) // 7)) // 8)) // 9,
        "nested_improves_ordinary": nested <= ordinary_cap,
        "ordinary_fail": not global_values["ordinary"]["safe_certificate"],
        "nested_fail": not global_values["nested"]["safe_certificate"],
        "ambient_marked_subset_identity": N * ordinary_numerator == comb(1024, 64) * comb(64, 59),
        "support_marked_subset_identity": D * ordinary_denominator == comb(68, 64) * comb(64, 59),
        "support_ratio_reproduced": ordinary_ratio == support_ratio,
        "nested_ratio_interval": Fraction(2763, 1000) < nested_ratio < Fraction(2764, 1000),
        "real_endpoint_exceeds_conservative": Fraction(D * (M + 1), N) > T * D / N,
    }
    for name, entry in global_values.items():
        checks[name + "_global_division"] = (
            entry["numerator"] == D * entry["quotient"] + entry["remainder"]
            and 0 <= entry["remainder"] < D
        )
        checks[name + "_floor_endpoint_equivalence"] = (
            entry["safe_certificate"] == (entry["strict_endpoint_slack"] > 0)
        )
    failures = [name for name, passed in checks.items() if not passed]
    certificate = {
        "scope": "Arithmetic only; no admissible-family maximum, label symmetry or RS safety asserted.",
        "parameters": {"n": 1024, "k": 64, "agreement": 68, "core": 59,
                       "residual_ground": 965, "block": 9, "strength": 5},
        "counts": {"N": N, "D": D, "ordinary_numerator": ordinary_numerator,
                   "ordinary_denominator": ordinary_denominator},
        "threshold": {"q": q, "T": rational(T), "M": M,
                      "remainder": threshold_remainder},
        "local_caps": {"benchmark": b, "adjacent": b + 1,
                       "benchmark_division_remainder": cap_remainder,
                       "ordinary": ordinary_cap, "ordinary_remainder": ordinary_remainder,
                       "nested": nested, "nested_stages": stages,
                       "real_strict_endpoint": rational(Fraction(endpoint, N)),
                       "real_conservative_endpoint": rational(T * D / N)},
        "nonuniform_endpoint": {"first_failing_sum": endpoint,
                               "last_passing_sum": endpoint - 1,
                               "last_passing_quotient": (endpoint - 1) // D,
                               "first_failing_quotient": endpoint // D},
        "global_transfer": global_values,
        "unfloored_ordinary_ratio": rational(ordinary_ratio),
        "original_support_ratio": rational(support_ratio),
        "checks": checks, "failures": failures,
    }
    output = Path(__file__).with_name("fifty-nine-core-threshold-results.json")
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Benchmark {b}; adjacent {b + 1}; ordinary {ordinary_cap}; nested {nested}")
    print(f"Required sum < D*(floor(T)+1); benchmark slack {endpoint - N*b}; adjacent slack {endpoint - N*(b+1)}")
    print(f"Nested ratio to threshold is in (2.763,2.764): {checks['nested_ratio_interval']}")
    print(f"Checks {len(checks) - len(failures)}/{len(checks)}; failures: {failures}")
    print(f"Certificate: {output.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
