"""C033y rational analytic preflight; no transforms or callbacks evaluated."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json


def main():
    e16 = F(3, 8) ** 16
    small = F(9, 32768) + F(13, 2**30)
    large = 202 * e16
    inner_j = F(600, 4**12) + F(3, 8) * e16
    inner_i = F(2400, 4**14) + 4 * e16
    profile = (inner_i + 2 * inner_j) / 6
    outer = F(12000, 4**13)
    prime = F(20, 3) * F(3, 8) ** 10
    actual_bounds = {
        "small_levy_tail": small,
        "large_levy_tail": large,
        "outer_quadrature": outer,
        "archimedean_propagated": 13 * profile,
        "prime_tail": prime,
    }
    required_bounds = {
        "small_levy_tail": F(1, 2**11),
        "large_levy_tail": F(1, 2**14),
        "outer_quadrature": F(1, 2**12),
        "archimedean_propagated": F(1, 2**12),
        "prime_tail": F(1, 2**11),
    }
    log_lo, log_hi = F(56, 81), F(25, 36)
    adaptive = []
    for w, exponent in [(128, 1), (32, 2), (8, 3), (4, 4)]:
        lower_exponent = w * (exponent * F(2, 3))**2 - F(3, 2)*exponent*F(7, 10)
        monotonic = exponent * F(2, 3) >= F(5, 4*w)
        assert lower_exponent > 20 and monotonic
        adaptive.append({"minimum_width": w, "cutoff": 2**exponent,
                         "decay_exponent_lower": str(lower_exponent),
                         "required_decay_exponent": 20,
                         "monotonicity_verified": monotonic})

    primes = [n for n in range(2, 33)
              if all(n % d for d in range(2, isqrt(n) + 1))]
    powers = {}
    for p in primes:
        n, exponent = p, 1
        while n <= 32:
            assert n not in powers
            powers[n] = [p, exponent]
            n *= p
            exponent += 1
    independently = []
    for n in range(2, 33):
        d = next((d for d in range(2, isqrt(n)+1) if n % d == 0), n)
        remainder = n
        while remainder % d == 0:
            remainder //= d
        if remainder == 1:
            independently.append(n)
    assert sorted(powers) == independently

    analytic_allowance = sum(required_bounds.values())
    analytic_bound = sum(actual_bounds.values())
    conditional_final = analytic_allowance + 2*F(1, 2**10)
    positions = {
        "outer_nodes_shared": 20*13,
        "profiles": 3*20*13,
        "variable_inner_samples": 3*20*13*4*12,
        "fixed_inner_samples": 16*14+4*12,
        "prime_summands_upper": 3*20*13*len(powers),
        "outer_weighted_summands": 6*20*13,
        "final_exponentials": 8,
    }
    named_positions = sum(positions[k] for k in (
        "variable_inner_samples", "fixed_inner_samples", "prime_summands_upper",
        "outer_weighted_summands", "final_exponentials"))
    checks = {name: actual_bounds[name] < required_bounds[name]
              for name in actual_bounds}
    checks.update({
        "profile_radius_below_2_pow_minus_16": profile < F(1, 2**16),
        "dyadic_analytic_sum": analytic_allowance == F(25, 16384),
        "analytic_allowance_below_2_pow_minus_9": analytic_allowance < F(1, 512),
        "conditional_final_sum": conditional_final == F(57, 16384),
        "conditional_final_below_2_pow_minus_8": conditional_final < F(1, 256),
        "outer_length_below_20": 28*log_hi < 20,
        "weight_quadrature_error_below_1": F(2000, 4**13) < 1,
        "log2_bounds_in_adaptive_range": F(2, 3) < log_lo < log_hi < F(7, 10),
        "cutoff32_decay_exponent_above_10": 25*log_lo**2-F(5, 2)*log_hi > 10,
        "prime_power_count_18": len(powers) == 18,
        "independent_prime_power_lists_agree": sorted(powers) == independently,
        "named_positions_53320": named_positions == 53320,
    })
    assert all(checks.values())
    missing = [
        "Certified finite Gauss nodes and weights, with propagated errors and cost.",
        "Constants and every elementary operation/exp/log/sqrt radius and cost.",
        "Cancellation-sensitive R(z) evaluation at enlarged widths.",
        "Arithmetic exponent error <=2^-10 and final exponential error <=2^-10.",
        "Full aggregate elementary-term count <=10^6; named positions are not that count.",
    ]
    result = {
        "scope": "Exact-node analytic allowances only, conditional on C033y's qualified inputs.",
        "status": "ANALYTIC_ALLOWANCES_PASS_AGGREGATE_PREFLIGHT_INCOMPLETE",
        "transforms_evaluated": False,
        "levy_cutoffs": {"small": "1/1073741824", "large": "1/4",
                         "residual_large_domain": "[1/4,infinity) minus [1,3/2]"},
        "allowances": {k: {"proved_upper_bound": str(actual_bounds[k]),
                            "required_strict_bound": str(required_bounds[k]),
                            "passes": checks[k]} for k in actual_bounds},
        "inner_errors": {"J_upper": str(inner_j), "I_upper": str(inner_i),
                         "profile_upper": str(profile), "profile_required": "1/65536"},
        "aggregate_analytic": {"proved_upper_bound": str(analytic_bound),
                               "dyadic_allowance": str(analytic_allowance),
                               "required_strict_bound": "1/512"},
        "conditional_final": {"allowance": str(conditional_final), "required": "1/256",
                              "unpaid_exponent_arithmetic_allowance": "1/1024",
                              "unpaid_final_exponential_allowance": "1/1024"},
        "adaptive_prime_thresholds": adaptive,
        "prime_powers": [[n, *powers[n]] for n in sorted(powers)],
        "positions": positions,
        "cost": {"named_positions_only": named_positions,
                 "full_elementary_term_count": None, "required_cap": 10**6,
                 "full_cost_certified": False},
        "checks": checks,
        "unresolved": missing,
        "not_verified": ["Analytic proof audit", "External preprints and zero data",
                         "Numerical scalar values", "Conditioning/interpolation/TV", "RH"],
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    for key in actual_bounds:
        print(f"{key}: {actual_bounds[key]} < {required_bounds[key]}: PASS")
    print(f"Analytic allowance: {analytic_allowance} < 1/512: PASS")
    print(f"Final radius conditional on unpaid arithmetic: {conditional_final} < 1/256")
    print(f"Named positions: {named_positions}; FULL cost: UNKNOWN; required <=1000000")
    print("Aggregate preflight: INCOMPLETE; no transforms evaluated")
    print("Unresolved: nodes/weights, constants, R cancellation, rounding/exponentials and full cost")
    print(f"Certificate: {path}")


if __name__ == "__main__":
    main()
