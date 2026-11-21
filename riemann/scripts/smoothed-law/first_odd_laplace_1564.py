"""Exact elementary inequalities for the qualified two-width test1564.

Analytic reductions and external assumptions are in the associated draft.
This checks rational bounds, not the external zero data or positivity.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

BASE = Q(3, 8)  # e > 8/3
EPS = Q(1, 10**100)
checks = []


def check(name, actual, required, relation="<"):
    passed = actual < required if relation == "<" else actual > required
    checks.append({"name": name, "actual_exact": str(actual),
                   "required_exact": str(required), "relation": relation,
                   "actual_decimal_preview": float(actual), "passed": passed})


check("universal_high_zero_tail", 4*Q(3, 25)*100**6*BASE**306, EPS)
check("P1_lower_tail_absorption", EPS, Q(1, 20)*Q(1, 3)**57)
check("P2_lower_tail_absorption", EPS, Q(1, 42)*Q(1, 3)**29)
check("P1_upper_tail_absorption", EPS, Q(1, 3)**49)
check("P2_upper_tail_absorption", EPS, Q(1, 3)**25)
check("width_ratio_r", 287*BASE**20, Q(1, 10**6))
check("T1_exceeds_48", 49*EPS, Q(1, 8)*Q(1, 3)**57)
check("T2_correction_to_24_75", 7000*BASE**21+182*EPS*3**29, Q(1, 4))
check("profile_second_derivative_on_0_1", 40*Q(32, 15)*196*BASE**21+EPS, Q(1, 1000))
check("profile_origin_uniform", 41*BASE**24, Q(1, 1000))
S2 = Q(40, 196)+Q(3, 25)
e_abs_bound = 2*(Q(1, 2000)+Q(1, 1000)+Q(16, 15)*(2*S2+40*BASE**6+EPS))
check("absolute_quadratic_exponent_coefficient", e_abs_bound, Q(2))
negative_high = Q(16, 15)*Q(4, 9)*Q(3, 25)*BASE**9+2*EPS
check("negative_high_zero_spatial_integral", negative_high, Q(1, 100000))
check("P1_for_spatial_lower_bound", 41*BASE**49, Q(1, 10**9))
R1_lower = Q(3, 8192)-Q(1, 100000)-Q(1, 10**9)-EPS/2
check("R1_lower_bound", R1_lower, Q(1, 4000), ">")
check("quadratic_output_negative_margin", Q(1, 2000)-Q(2, 10**6), Q(0), ">")
check("cubic_output_positive_bracket", Q(48-25, 6)+Q(1, 2000)-2, Q(11, 6), ">")

certificate = {
    "scope": "mass-one widths 1,2; first odd jet zero; Laplace derivatives 1 and 2 near positive zero",
    "assumptions": ["C032j/m/q/s/t/u qualified actual-zero and fixed-v1 inputs",
                    "zeros through 100 on the line; gamma>14; one gamma in (14,15)",
                    "N(100)<40 and sum_gamma_gt_100 gamma^-2<3/25"],
    "elementary_constants": ["3<pi<4", "8/3<e<3", "exp(1/16)<16/15"],
    "analytic_proof": "drafts/2026-11-18-first-odd-laplace-calculation-1564.md",
    "checks": checks,
    "failures": [c["name"] for c in checks if not c["passed"]],
    "conclusion": "Both necessary signs hold for sufficiently small positive s; output positivity unresolved.",
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2)+"\n")
for c in checks:
    print(f'{c["name"]}: {c["actual_decimal_preview"]:.12g} {c["relation"]} {c["required_exact"]}; {"PASS" if c["passed"] else "FAIL"}')
print(f'failures={len(certificate["failures"])}; certificate={path}')
raise SystemExit(bool(certificate["failures"]))
