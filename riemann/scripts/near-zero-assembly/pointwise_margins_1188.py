"""Exact scalar comparisons for C030f; no special-function sampling."""

from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path


checks = {}


def rational(value):
    return {"numerator": value.numerator, "denominator": value.denominator}


def check(name, actual, relation, required):
    passed = actual < required if relation == "<" else actual > required
    checks[name] = {
        "actual": rational(actual),
        "relation": relation,
        "required": rational(required),
        "positive_gap": rational(required - actual if relation == "<" else actual - required),
        "passed": passed,
    }
    print(f"{name}: {actual} {relation} {required}: {'PASS' if passed else 'FAIL'}")


def taylor(x, n):
    return sum((x**k / factorial(k) for k in range(n + 1)), F(0))


pi_lower = 16 * (F(1, 5) - F(1, 3 * 5**3) + F(1, 5 * 5**5) - F(1, 7 * 5**7)) - F(4, 239)
pi_upper = 16 * (F(1, 5) - F(1, 3 * 5**3) + F(1, 5 * 5**5)) - 4 * (F(1, 239) - F(1, 3 * 239**3))
check("pi_lower", pi_lower, ">", F(3))
check("pi_upper", pi_upper, "<", F(22, 7))
check("exp_log2_upper", taylor(F(7, 10), 3), ">", F(2))
check("exp_logpi_upper", taylor(F(6, 5), 4), ">", F(22, 7))
check("exp3_lower", taylor(F(3), 8), ">", F(20))
check("exp_log_endpoint_upper", taylor(F(3, 2), 2), ">", F(10, 3))
check("global_floor", -(F(1) + F(11, 7) + F(21, 10) + F(6, 5)), ">", F(-6))
check("head_denominator", F(3 * 20**2 - 1, 16), ">", F(74))
check("tail_budget", F(31, 90 * (20**10 - 1)), "<", F(1, 10**11))
check("total_binet_budget", F(1, 3200) + F(2, 1601) + F(1, 888) + F(1, 10**11), "<", F(3, 1000))
check("endpoint_log_argument", F(35, 11), ">", F(3))
check("endpoint_lower", F(13, 12) - F(3, 1000), ">", F(1))
check("endpoint_upper", F(3, 2) + F(3, 1000), "<", F(2))

failures = [name for name, result in checks.items() if not result["passed"]]
certificate = {
    "step_id": "2026-11-16-archimedean-pointwise-audit-1188",
    "scope": "Exact rational comparisons in C030f. Analytic identities, convergence and universal quantifiers are justified in the canonical proof, not by this script.",
    "checks": checks,
    "failures": failures,
    "all_passed": not failures,
}
path = Path(__file__).with_name("pointwise-margins-1188.json")
path.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
print(f"Checks: {len(checks)}; failures: {failures}; certificate: {path}")
raise SystemExit(bool(failures))
