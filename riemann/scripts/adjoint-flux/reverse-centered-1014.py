#!/usr/bin/env python3
"""Exact arithmetic in C467f; does not verify its analytic arguments."""

from fractions import Fraction as F
from pathlib import Path
import json


checks = []


def check(name, actual, required, relation="<"):
    actual, required = F(actual), F(required)
    passed = actual < required if relation == "<" else actual == required
    checks.append({
        "name": name,
        "actual": str(actual),
        "required": str(required),
        "relation": relation,
        "passed": passed,
    })


check("centroid_squared_comparison", 600**2, 48**2 * 160)
check("centered_radius_squared", F(1, 80), F(9, 80)**2)
check("interpolated_real_part", F(1, 600) + F(9, 1280) + F(1, 320), F(1, 80))
check("interpolated_modulus_squared", F(1, 6400) + F(3, 160), F(3, 20)**2)
check("interpolated_derivative_squared", 1 + F(19, 160)**2, F(101, 100)**2)
check("background_second_derivative", 40 * F(101, 100)**2 + 3, 44)
check("background_third_derivative", 400 * F(101, 100)**3 + 60 * F(101, 100), 475)
check("arctangent_argument", F(1, 16) + F(9, 80) * F(1, 4), F(1, 10))
check("singular_b_derivative", F(1, 40) + F(9, 160) * F(1, 16), F(1, 32))
u_bound = 44 + F(9, 160) * 475 + 3 + F(1, 32)
v_bound = F(475, 2) + F(1, 32)
check("U_derivative_identity", u_bound, F(295, 4), "=")
check("U_derivative", u_bound, 75)
check("V_derivative_identity", v_bound, F(7601, 32), "=")
check("V_derivative", v_bound, 238)
u_horizon, v_horizon = F(75, 1920), F(238, 1920)
check("U_bootstrap", u_horizon, F(1, 16))
check("V_bootstrap", v_horizon, F(1, 4))
secant = u_horizon + F(9, 80) * v_horizon
check("secant_identity", secant, F(4071, 76800), "=")
check("secant_cone", secant, F(1, 16))
frob = F(1, 3) + F(6, 5) + F(6, 5)**2 / 6
check("scaled_coordinate_frobenius", frob, F(133, 75), "=")
offset = u_horizon + 2 * F(9, 80) * v_horizon
check("graph_hessian_offset", offset, F(857, 12800), "=")
conditional_phase = F(15, 64) + 3 * (offset + frob / 5)
check("conditional_phase_identity", conditional_phase, F(95951, 64000), "=")
check("conditional_phase_threshold", conditional_phase, F(3, 2))

failures = [item["name"] for item in checks if not item["passed"]]
certificate = {
    "step": "1014",
    "scope": "Exact rational arithmetic only; C467e and all analytic arguments require proof review.",
    "unresolved": ["Coefficient projection invertibility", "Scaled momentum-graph derivative norm <= 1/5"],
    "checks": checks,
    "failures": failures,
    "passed": not failures,
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
print(f"Arithmetic: {len(checks)} checks; failures={failures}")
print(f"Secant bound={secant}; required <1/16")
print(f"Conditional phase bound={conditional_phase}; required <3/2")
print("Condition unverified: projection invertible and graph derivative norm <=1/5")
print(f"Certificate: {path.relative_to(Path.cwd())}")
raise SystemExit(bool(failures))
