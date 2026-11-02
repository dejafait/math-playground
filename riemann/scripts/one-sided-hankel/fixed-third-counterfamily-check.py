#!/usr/bin/env python3
"""Exact rational inequalities for the fixed-third Hankel counterfamily.

Run from the active notebook:
  python3 scripts/one-sided-hankel/fixed-third-counterfamily-check.py
The JSON stores every grid entry and comparison; no floating point is
used in a mathematical check. Analytic uniformity is proved separately.
"""

from fractions import Fraction as F
import json
from pathlib import Path


def rational(q):
    return {"numerator": q.numerator, "denominator": q.denominator}


R, d, u = F(11, 8), F(5, 4), F(523, 400)
r, s, eta = F(23, 400), F(67, 1000), F(1, 100)
den = (u - s) * (R * R - s)
gamma = s * (R * R - F(1, 3)) / den
K = s / (2 * den)
gamma_cap, K_cap = F(7, 150), F(1, 50)
grid_count, rounding_scale = 64, 10000
rows = []
for k in range(1, grid_count + 1):
    t = F(k, grid_count)
    value = u / (u * u + t * t) - u * t * t / (R**4 + u * u * t * t)
    scaled = value * rounding_scale
    lower_integer = scaled.numerator // scaled.denominator
    lower = F(lower_integer, rounding_scale)
    difference = value - lower
    rows.append({
        "k": k, "t": rational(t), "value": rational(value),
        "lower_integer": lower_integer, "rounding_scale": rounding_scale,
        "difference": rational(difference), "passed": difference >= 0,
    })

lower_sum = F(sum(row["lower_integer"] for row in rows),
              grid_count * rounding_scale)
mean_required = F(11, 20)
beta, target_rate = r * mean_required, F(1, 32)
error_rate = (1 - r / s) / 3 - gamma_cap
checks = {
    "anchor": u - r == d,
    "clearance": u + r == R - eta,
    "auxiliary_radii": 0 < r < s < R - u,
    "left_half_plane": u - s > 0,
    "factor_denominators": R * R - s > 0,
    "derivative_monotonicity_rectangle": d > 1 and R * R > u,
    "gamma_bound": gamma < gamma_cap,
    "constant_bound": K < K_cap,
    "all_64_lower_entries": all(row["passed"] for row in rows),
    "mean_gain": lower_sum > mean_required,
    "product_rate": beta > target_rate,
    "error_rate": error_rate == F(1, 1675) and error_rate > 0,
    "geometric_denominator_for_m_ge_8": 8 * (1 - r / s) > 1,
    "boundary_kernel_constant": 1 / (R - u - s) == 2000,
    "full_boundary_prefactor": 1 / (R - u) + 8000 < 8100,
}
certificate = {
    "purpose": "Rational arithmetic only; analytic proof is separate.",
    "parameters": {name: rational(value) for name, value in
                   [("R", R), ("d", d), ("u", u), ("r", r),
                    ("s", s), ("eta", eta)]},
    "bounds": {
        "gamma": rational(gamma), "gamma_required_upper": rational(gamma_cap),
        "K": rational(K), "K_required_upper": rational(K_cap),
        "right_sum_lower": rational(lower_sum),
        "mean_required_lower": rational(mean_required),
        "beta": rational(beta), "target_rate": rational(target_rate),
        "rate_margin": rational(beta - target_rate),
        "quadrature_error_rate": rational(error_rate),
        "lower_integer_sum": sum(row["lower_integer"] for row in rows),
    },
    "grid_count": grid_count, "rounding_scale": rounding_scale,
    "lower_integers": [row["lower_integer"] for row in rows],
    "derivative_lower_table": rows, "checks": checks,
    "failures": [name for name, passed in checks.items() if not passed],
    "passed": all(checks.values()),
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
print(f"Passed: {certificate['passed']}; failures: {certificate['failures']}")
print(f"Mean lower bound: {lower_sum}; required > {mean_required}")
print(f"Grid growth gamma: {gamma}; required < {gamma_cap}; K: {K} < {K_cap}")
print(f"Decay rate: {beta}; required > {target_rate}; margin: {beta-target_rate}")
print(f"Quadrature error decay: {error_rate} > 0")
print(f"Certificate: {output}")
raise SystemExit(0 if certificate["passed"] else 1)
