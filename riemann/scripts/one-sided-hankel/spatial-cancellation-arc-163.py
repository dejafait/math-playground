"""Exact auxiliary margins for L708; not a verification of its analytic proof."""
from fractions import Fraction as F
from pathlib import Path
import json


def encode(q):
    q = F(q)
    return {"numerator": q.numerator, "denominator": q.denominator,
            "decimal_preview": float(q)}


d, R, U, A = F(5, 4), F(11, 8), F(121, 64), F(27, 10)
g, w_upper = F(1, 1000), F(3, 81920)
frequency_lower = A * (d*d-U/2) * (U-1) / (
    8 * (d+1) * (d+F(1, 2)) * (U+d) * (U/2+d))
omega_lower = A * (U-1) / (2*(d+F(1, 2))*(U/2+d))
omega_upper = A/d
rows = [
    ("frequency_separation", frequency_lower, ">", F(1, 200)),
    ("bump_width_using_pi_lt_4", 8*w_upper, "<", F(1, 3000)),
    ("off_bump_margin", frequency_lower-g-8*w_upper, ">", 0),
    ("frequency_interval_lower", omega_lower-g, ">", 0),
    ("frequency_interval_upper_using_pi_gt_3", omega_upper+g, "<", F(9, 4)),
    ("positive_radial_derivative_factor", d-R/2, ">", 0),
    ("node_radius_squared", F(2824, 3025), "<", 1),
    ("spatial_pole_distance_squared", F(6481, 2824), ">", F(151, 100)**2),
    ("spatial_denominator_margin", d*(F(151, 100)-F(301, 200)), "=", F(1, 160)),
    ("resolvent_variation", F(27, 4)/F(67, 36), "<", 6),
    ("second_moment_majorant_n_ge_15", (A/d)**2*F(288, 225), "<", 16),
    ("centered_exponential_moment", F(25, 16), "<", 2),
    ("comb_tilt_log_majorant", F(27, 223), "<", F(1, 8)),
    ("two_endpoint_tail_constant", F(19200, 9)/(A*A), "<", 300),
    ("first_omitted_ordinate_n_ge_15", F(9, 20)-A/(8*15), ">", F(2, 5)),
]
checks = {}
for name, actual, relation, required in rows:
    actual, required = F(actual), F(required)
    ok = {">": actual > required, "<": actual < required,
          "=": actual == required}[relation]
    checks[name] = {"actual": encode(actual), "relation": relation,
                    "required": encode(required), "pass": ok}

certificate = {
    "purpose": "Exact auxiliary inequalities in L708, step 163",
    "qualification": "No numerical profile approximation, asymptotic test, or analytic proof verification.",
    "assumptions_not_certified_by_arithmetic": [
        "L703's actual construction and Fourier identity",
        "The elementary inequalities 3 < pi < 4",
        "Reused primary analytic theorems and their applicability",
        "Uniform complex convolution, Fourier, endpoint, and spatial continuation arguments",
        "Existential neighborhood, arc, exponential rate, and onset",
    ],
    "checks": checks,
    "failures": [name for name, row in checks.items() if not row["pass"]],
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(certificate, indent=2)+"\n")
for name in ("frequency_separation", "bump_width_using_pi_lt_4",
             "off_bump_margin", "spatial_pole_distance_squared"):
    row = checks[name]
    a, b = row["actual"], row["required"]
    print(f"{name}: {a['numerator']}/{a['denominator']} {row['relation']} "
          f"{b['numerator']}/{b['denominator']}; pass={row['pass']}")
print(f"Checks: {len(checks)}; failures: {certificate['failures']}; certificate: {out}")
if certificate["failures"]:
    raise SystemExit(1)
