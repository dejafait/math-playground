"""Exact arithmetic for C467b; does not verify its analytic arguments."""

from fractions import Fraction as F
import json
from pathlib import Path


def fraction_record(value):
    return {"numerator": value.numerator, "denominator": value.denominator}


def strict_less(name, actual, required):
    margin = required - actual
    return {
        "name": name,
        "actual": fraction_record(actual),
        "required_upper_bound": fraction_record(required),
        "positive_margin": fraction_record(margin),
        "passed": margin > 0,
    }


a, time, initial_r = F(1, 16), F(1, 1920), F(31, 1000)
k = F(1, 47)
contraction = F(1137, 200)
image_speed = F(1, 5)
lower_q = initial_r - image_speed * time
upper_q_squared = a * a - contraction * time
raw_derivative_bound = -6 + 4 * k * k + 80 * a * a
normal_speed_bound = k * k * (F(13, 2) * 40 + 40 * a) + 40 * a * k

checks = [
    strict_less("positive_bump_start", 32 * initial_r, F(1)),
    strict_less("tangent_envelope", F(96, 4607), k),
    strict_less("raw_norm_barrier", 80 * 2 * a * a, F(12)),
    strict_less("raw_squared_contraction", raw_derivative_bound, -contraction),
    strict_less("characteristic_image_speed", normal_speed_bound, image_speed),
    strict_less("no_collision_barrier", F(1, 40), lower_q),
    strict_less("endpoint_incompatibility", upper_q_squared, lower_q * lower_q),
]
certificate = {
    "step_id": "2026-11-15-actual-h-compact-adjoint-symmetric-escape-1000",
    "scope": "Exact rational arithmetic only; analytic proof and continuation are in C467b and await independent conceptual audit.",
    "parameters": {
        "a": fraction_record(a),
        "T_0": fraction_record(time),
        "r_0": fraction_record(initial_r),
        "contraction": fraction_record(contraction),
        "image_speed": fraction_record(image_speed),
    },
    "lower_q": fraction_record(lower_q),
    "upper_q_squared": fraction_record(upper_q_squared),
    "final_gap": fraction_record(lower_q * lower_q - upper_q_squared),
    "checks": checks,
    "failures": [check["name"] for check in checks if not check["passed"]],
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
for check in checks:
    left = F(**check["actual"])
    right = F(**check["required_upper_bound"])
    print(f"{check['name']}: actual {left}; required < {right}; {'PASS' if check['passed'] else 'FAIL'}")
print(f"Final strict gap: {lower_q * lower_q - upper_q_squared}; required > 0")
print(f"Failures: {certificate['failures']}")
print(f"Certificate: {path.relative_to(Path.cwd())}")
raise SystemExit(bool(certificate["failures"]))
