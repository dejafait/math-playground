"""Exact rational scalar checks for C030e; not a spectral computation."""

from fractions import Fraction as F
import json
from pathlib import Path


def rational(value):
    return {"numerator": value.numerator, "denominator": value.denominator}


checks = {}


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


pi_lower = 16 * (F(1, 5) - F(1, 3 * 5**3) + F(1, 5 * 5**5) - F(1, 7 * 5**7)) - F(4, 239)
pi_upper = 16 * (F(1, 5) - F(1, 3 * 5**3) + F(1, 5 * 5**5)) - 4 * (F(1, 239) - F(1, 3 * 239**3))
check("pi_lower", pi_lower, ">", F(3141, 1000))
check("pi_upper", pi_upper, "<", F(22, 7))
check("log2_lower", 2 * (F(1, 3) + F(1, 81) + F(1, 1215)), ">", F(693, 1000))
check("beta_lower", F(693, 1000)**2 / 24, ">", F(1, 50))
check("time_domain", F(1, 10**6), "<", F(693, 1000) / 180)
check("C3_squared", F(6**12 * 1000, 5**10 * 11 * 3141), "<", F(127, 50)**2)
check("uniform_polar", F(22, 7 * 250) * F(4000000, 3999999), "<", F(13, 1000))
check("uniform_prime", F(1, 12 * 80001), "<", F(1, 1000))
check("special_polar", 4 * F(22, 7) * F(127, 50) * F(1, 1000) * F(4000000, 3999989), "<", F(32, 1000))
check("special_prime", F(4, 3 * 20001), "<", F(1, 1000))
check("uniform_margin", 1 - F(28, 100) - F(13, 1000) - F(1, 1000), ">", F(7, 10))
check("special_margin", 1 - F(7112, 10000) - F(32, 1000) - F(1, 1000), ">", F(1, 4))

failures = [name for name, result in checks.items() if not result["passed"]]
certificate = {
    "step_id": "2026-11-16-near-zero-assembly-audit-1186",
    "scope": "Exact rational comparisons in C030e. Analytic identities and imported theorems are not certified by this script.",
    "checks": checks,
    "failures": failures,
    "all_passed": not failures,
}
path = Path(__file__).with_name("scalar-margins-1186.json")
path.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
print(f"Checks: {len(checks)}; failures: {failures}; certificate: {path}")
raise SystemExit(bool(failures))
