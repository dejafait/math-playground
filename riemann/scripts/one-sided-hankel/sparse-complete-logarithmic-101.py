"""Exact arithmetic support for L692; not an analytic-proof audit."""
from fractions import Fraction as F
import json
from pathlib import Path


def main():
    checks = []

    def check(name, actual, relation, required):
        actual, required = F(actual), F(required)
        passed = {">": actual > required, "<": actual < required,
                  "<=": actual <= required, ">=": actual >= required}[relation]
        checks.append({"name": name, "actual": str(actual),
                       "relation": relation, "required": str(required),
                       "passed": passed})

    n0 = 10**6
    r = F(11, 8)
    check("anchor_product_constant", F(27, 80)/r, ">", F(1, 5))
    check("log_400000_below_14", F(8, 3)**14, ">", 400000)
    check("log_40000_below_11", F(8, 3)**11, ">", 40000)
    check("log_5_over_2_below_1", F(8, 3), ">", F(5, 2))
    check("log_n0_below_20", 2**20, ">", n0)
    check("log_2R_below_2", 4, ">", 2*r)
    check("available_binomial_increasing_range_at_onset",
          F(n0, 5000), "<", F(n0, 3)-1)
    check("range_comparison_slope", F(1, 5000), "<", F(1, 3))
    check("baseline_error_rate_margin",
          F(1, 500)-F(7, 5000), ">", F(1, 2000))
    check("twice_error_log_ratio_upper_at_onset",
          2+40+22-F(n0, 2000), "<", 0)
    check("error_envelope_log_derivative_at_onset",
          F(2, n0)-F(1, 2000), "<", 0)
    check("complete_mean_loss_rate", F(23, 10000), "<", F(1, 400))
    check("target_margin_above_constant_upper_at_onset",
          (F(1, 100)-F(1, 400))*n0, ">", 2)
    certificate = {
        "lemma": "L692",
        "scope": "Exact arithmetic support only; analytic and algebraic proof unaudited.",
        "required_conditions": {"n_at_least": n0, "n_congruence": "3 mod 12",
                                "L_at_most": "n/40000", "support_at_most": "2L"},
        "analytic_inputs_not_replayed": ["L690 (1)-(2)", "L657 integrability and charge identity"],
        "elementary_e_bounds_used_in_proof": "8/3 < exp(1) < 3, from its positive series",
        "checks": checks,
        "failures": [c["name"] for c in checks if not c["passed"]],
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"{len(checks)-len(certificate['failures'])}/{len(checks)} exact arithmetic checks passed")
    print("Actual mean-loss rate upper bound: 23/10000; reported: 1/400; target: 1/100")
    print("Actual baseline error-rate margin: 3/5000; required: >1/2000")
    print("Failures:", certificate["failures"])
    print("Certificate:", path)
    if certificate["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
