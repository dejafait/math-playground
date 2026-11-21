#!/usr/bin/env python3
"""Exact scalar checks for C997c; the all-n proof is in the lemma."""

from fractions import Fraction as F
import json
from pathlib import Path


def encoded(value):
    return f"{value.numerator}/{value.denominator}"


checks = {}


def check(name, actual, relation, required):
    passed = {"<": actual < required, ">": actual > required,
              "=": actual == required}[relation]
    checks[name] = {"actual": encoded(actual), "relation": relation,
                    "required": encoded(required), "passed": passed}


radius = F(29, 112)
check("left_angle_radius", F(11, 7) - F(21, 16), "=", radius)
check("right_angle_radius", F(225, 128) - F(3, 2), "<", radius)
check("upper_angle_n48", F(27, 16) + F(27, 8 * 48), "=", F(225, 128))
sine_floor = 1 - radius**2 / 2
check("sine_floor", sine_floor, ">", F(24, 25))
check("sine_floor_value", sine_floor, "=", F(24247, 25088))

s, r, scale = F(24, 25), F(1, 49), F(2401, 2500)
check("polynomial_gap_endpoint", (1250 * s**2 - 1201) / 49, "=", F(-1))
check("polynomial_unit_endpoint", F(1250 - 1201, 49), "=", F(1))
check("factor_constant", scale * (1 - 2 * r * F(1201, 49) + r**2), "=", F(0))
check("factor_quadratic_coefficient", scale * 2 * r * F(1250, 49), "=", F(1))
check("root_discriminant_square", F(1201, 49)**2 - 1, "=", F(1200, 49)**2)
check("maximum_root_modulus", F(1201 + 1200, 49), "=", F(49))
check("sign_tail_constant", F(50, 49) / (1 - r), "=", F(25, 24))
check("upper_error_constant", F(25, 24) * 18 * 7, "=", F(525, 4))

log7_lower = 2 * sum((F(3, 4)**(2 * j + 1) / (2 * j + 1) for j in range(3)), F(0))
check("log7_series_lower", log7_lower, "=", F(4803, 2560))
rho_lower = log7_lower / 6 - F(9, 32)
check("rho_lower_value", rho_lower, "=", F(161, 5120))
check("rho_vs_required", rho_lower, ">", F(1, 32))
check("remaining_margin", rho_lower - F(1, 32), "=", F(1, 5120))
check("norm_bound_n48_margin", F(48**2) - (F(1, 2) + F(25, 784) * 48**2), ">", F(0))

failures = [name for name, item in checks.items() if not item["passed"]]
certificate = {
    "result": "PASS" if not failures else "FAIL",
    "scope": "Exact scalar arithmetic only; no sampling or independent proof audit.",
    "canonical_proof": "lemmas/C997c-local-positive-branch-recovery.md",
    "checks": checks,
    "failures": failures,
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"{certificate['result']}: {len(checks)} exact checks; failures={failures}")
print(f"sine lower={sine_floor}; required>{s}")
print(f"rho lower={rho_lower}; required>1/32; margin={rho_lower - F(1, 32)}")
print(f"certificate: {output}")
raise SystemExit(bool(failures))
