"""Exact rational arithmetic supporting C033g; not an analytic proof audit."""

from fractions import Fraction as F
import json
from pathlib import Path


def value(x):
    x = F(x)
    return {
        "numerator": str(x.numerator),
        "denominator": str(x.denominator),
        "decimal_preview": float(x),
    }


checks = []


def below(name, actual, required):
    actual, required = F(actual), F(required)
    checks.append({
        "name": name,
        "actual": value(actual),
        "required_strict_upper_bound": value(required),
        "passed": actual < required,
    })


q = F(3, 8)
delta = F(3, 64)
m = 3 * (q**18 + 504 * q**40)
t32 = q**6 + 147 * q**12
eps = F(16, 15) * F(8, 7) * F(441, 6) * q**20
eta = eps * F(484, 2)
j2 = F(16, 45) * F(101, 100) / (2 * 250) + F(32, 15) * F(4, 21)
j4 = F(16, 45) * F(101, 100) / (6 * 250) + F(128, 15) * F(40, 27 * 14**3)


def series(t):
    return (3 + t) / (1 - t)**3


near_m = 4 * delta * series(F(1, 64)) / 12
far_j = 4 * delta * series(F(1, 16))
total_m = near_m + F(4, 3) * far_j
epsilon_bound, eta_bound, m_bound = F(1, 10**6), F(1, 10**4), F(1, 10**6)
e_difference = F(7, 2000) + 2 * m_bound
pair_error = 2 * (eta_bound + 60 * epsilon_bound) / (1 - epsilon_bound)
final_bracket = -F(1, 192) + F(1, 3000) + F(1, 10**6) + F(1, 280)

below("count_simplification", 4, F(25, 6))
below("shell_T32_ratio", F(484, 441) * F(32, 73), F(1, 2))
below("other_shell_ratios", F(5, 4) / 16, F(1, 8))
below("T32", t32, F(1, 250))
below("M2", m, m_bound)
below("J2", j2, F(5, 12))
below("J4", j4, F(1, 200))
below("E_far_J4_coefficient", far_j, F(7, 10))
below("E_total_M_coefficient", total_m, 2)
below("E_difference", e_difference, F(1, 280))
below("R_near_coefficient", 1 / (3 * (1 - F(1, 64))), F(1, 2))
below("R_segment", m_bound / 2 + F(16, 15) * (F(5, 12) + m_bound), F(1, 2))
below("core_score_slope", -F(369, 184), -2)
below("core_log_derivative", F(1, 2) + F(61, 4)**2 / 4, 60)
below("relative_epsilon", eps, epsilon_bound)
below("relative_eta", eta, eta_bound)
below("relative_log_error_pair", pair_error, F(1, 3000))
below("full_log_derivative", (60 + eta_bound) / (1 - epsilon_bound), 61)
below("phase_upper", 2 * m_bound, F(1, 10**5))
below("sine_error_pair", F(122, 10**10), F(1, 10**6))
below("normalization_exp_upper", F(64, 61), 2)
below("signed_bracket", final_bracket, -F(1, 1000))
below("normalized_final_bound", -F(1, 2000), 0)

failures = [c["name"] for c in checks if not c["passed"]]
certificate = {
    "step_id": "2026-11-19-signed-first-zero-margin-1728",
    "scope": "Exact rational comparisons in C033g; all analytic and source hypotheses remain in the canonical proof.",
    "source_assessment": "drafts/literature/2026-11-19-signed-first-zero-comparison-1726.md",
    "canonical_proof": "lemmas/C033g-signed-first-zero-width-ratio-margin.md",
    "all_passed": not failures,
    "failures": failures,
    "checks": checks,
    "conclusion": {
        "conditional_on": "C033g's analytic argument and explicitly qualified source inputs; arithmetic alone does not establish the theorem.",
        "bracket_upper": value(final_bracket),
        "simplified_bracket_upper": value(-F(1, 1000)),
        "ratio_lower": value(F(1, 2)),
        "W_over_f_squared_upper": value(-F(1, 2000)),
        "required_strict_upper_threshold": value(0),
        "analytic_audit": "PENDING",
    },
}
output = Path(__file__).with_name("margin-1728.json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Rational checks: {len(checks) - len(failures)}/{len(checks)} passed; failures={failures}")
for c in checks:
    if c["name"] in {"M2", "T32", "J4", "relative_epsilon", "relative_eta", "E_difference", "signed_bracket", "normalized_final_bound"}:
        print(f"{c['name']}: actual={c['actual']['decimal_preview']:.12g}, required < {c['required_strict_upper_bound']['decimal_preview']:.12g}, passed={c['passed']}")
print(f"Full certificate: {output.relative_to(Path.cwd())}")
print("Analytic proof and external source correctness: not checked by this script.")
raise SystemExit(bool(failures))
