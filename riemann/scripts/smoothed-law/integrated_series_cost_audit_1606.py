"""Independent exact replay of the restricted C032z preflight1586 audit.

Analytic implications are proved in C032z; this checks their rational
constants and the saved evidence without modifying the original files.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json

root = Path(__file__).resolve().parents[2]
original_path = root / "scripts/smoothed-law/integrated_spectral_cost_1586.json"
original_bytes = original_path.read_bytes()
original = json.loads(original_bytes)
checks = []


def check(name, actual, required, relation):
    passed = {"==": actual == required, ">": actual > required}[relation]
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       relation=relation, passed=passed))


# Integer common denominator, independent of the producer's recurrence.
d = 32**24 * factorial(24)
n = sum(121**j * 32**(24-j) * (factorial(24)//factorial(j))
        for j in range(25))
c_lower = Q(8*d + 704*n, d)
evidence = original["exact_evidence"]
check("Taylor_lower_matches_saved_full_rational", c_lower,
      Q(evidence["C_Taylor_lower"]), "==")
check("Taylor_lower_strict_margin", c_lower - 30000, Q(0), ">")
check("logarithmic_implication_margin_45000_minus_3pow9",
      Q(45000 - 3**9), Q(0), ">")
barrier = Q(4) * Q(21, 8) * Q(1, 8) * 30000**2
check("product_coefficient", barrier, Q(1181250000), "==")

cases = []
for eps in (Q(1), Q(1, 8)):
    row = next(r for r in evidence["cost_bounds"]
               if Q(r["requested_E_allowance_strict_upper"]) == eps)
    r_lower = Q(45000) / eps
    k_lower = barrier / eps**2
    minimum_integer_k = k_lower.numerator // k_lower.denominator + 1
    check(f"epsilon_{eps}_R", r_lower,
          Q(row["necessary_R_strict_lower"]), "==")
    check(f"epsilon_{eps}_K", k_lower,
          Q(row["necessary_K_strict_lower"]), "==")
    check(f"epsilon_{eps}_integer_rounding", minimum_integer_k,
          row["minimum_integer_K"], "==")
    check(f"epsilon_{eps}_ceiling_margin", k_lower - 10000000, Q(0), ">")
    cases.append(dict(epsilon=str(eps), R_strict_lower=str(r_lower),
                      K_strict_lower=str(k_lower),
                      minimum_integer_K=minimum_integer_k))

cap = original["finite_work_decision"]["literal_digamma_series_term_cap"]
check("original_work_ceiling", cap, 10000000, "==")
check("large_R_squared_allowance_bound", barrier / cap, Q(945, 8), "==")
check("large_R_squared_bound_exceeds_100", barrier / cap, Q(100), ">")
check("small_R_endpoint_45000_over_R", Q(45000, 45000), Q(1), "==")
check("original_arithmetic_failures_empty", len(original["arithmetic_failures"]), 0, "==")
failures = [c["name"] for c in checks if not c["passed"]]
certificate = dict(
    canonical_proof="lemmas/C032z-direct-integrated-spectral-explicit-formula.md#independent-cost-audit1606",
    original_certificate=str(original_path.relative_to(root)),
    scope="C032z(8)-(9), R>=1, integer K>=1, epsilon in {1,1/8}; chosen allowances only",
    exact_C_lower=str(c_lower), exact_C_lower_margin=str(c_lower-30000),
    cases=cases, work_ceiling=cap,
    small_R_case="1<=R<=45000 implies A>45000/R>=1, including equality R=45000",
    large_R_case="R>45000 and K<=10000000 imply (A+B)^2>945/8>100, hence A+B>10",
    caching="K counts one literal partial sum; no multiplier across nodes or parameters",
    limitations=["Analytic implications require the canonical proof, not this arithmetic alone",
                 "No actual-error, coefficient-size or actual-dictionary lower bound",
                 "No quadrature, finite evaluator or nonzero residual certificate",
                 "Sharper remainders and nonliteral digamma evaluation remain outside scope"],
    checks=checks, failures=failures,
    original_certificate_unchanged=original_path.read_bytes() == original_bytes)
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Restricted cost audit: {len(checks)} checks, {len(failures)} failures.")
for row in cases:
    print(f"epsilon={row['epsilon']}: R>{row['R_strict_lower']}, "
          f"K>{row['K_strict_lower']}; integer K>={row['minimum_integer_K']}.")
print("Ceiling=10000000; small R: allowance>1; large R: squared allowance>945/8>100.")
print("Failures: " + (", ".join(failures) if failures else "none"))
print(f"Certificate: {path.relative_to(root)}")
raise SystemExit(bool(failures) or not certificate["original_certificate_unchanged"])
