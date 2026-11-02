#!/usr/bin/env python3
"""Exact rational margins for C645l; the analytic argument is in the lemma.

Run from the active notebook:
  python3 scripts/one-sided-hankel/anchor-line-chebyshev-check.py
No floating-point comparisons or finite spectral screens are used.
"""

from fractions import Fraction as F
import json
from pathlib import Path


def rational(value):
    return {"numerator": value.numerator, "denominator": value.denominator}


d, R, eta = F(5, 4), F(11, 8), F(1, 100)
r, s = F(1, 2), F(1, 10)
D, U = d*d, R*R
u = d-s
p, H = D/U, u*u/U
coefficient_margins = [
    p+2-1/p-2*H,
    1+2*p-2*H/p-H*H,
    p-H*H/p,
]

vertex = (U-D)/r


def K(t):
    return r*(U+t*t)-2*t*(U-D)


lower_entries = [F(11, 100), F(9, 100), F(13, 200), F(7, 200)]
rows = []
for k, claimed in enumerate(lower_entries):
    left, right = F(k, 4), F(k+1, 4)
    minimizer = min(right, max(left, vertex))
    k_min = K(minimizer)
    numerator_lower = r*(U-right*right)*k_min
    denominator_upper = (
        D+max((r-left)**2, (r-right)**2)
    )*(U*U+D*right*right)
    actual_lower = numerator_lower/denominator_upper
    margin = actual_lower-claimed
    rows.append({
        "interval": [rational(left), rational(right)],
        "quadratic_minimizer": rational(minimizer),
        "quadratic_minimum": rational(k_min),
        "numerator_lower": rational(numerator_lower),
        "denominator_upper": rational(denominator_upper),
        "actual_lower": rational(actual_lower),
        "required_lower": rational(claimed),
        "margin": rational(margin),
        "passed": k_min > 0 and margin > 0,
    })

circle_radius_squared = D+r*r
ellipse_radius_squared = D+r*r+s*s+D*s*s/(r*r)
ellipse_squared_margin = U-ellipse_radius_squared
circle_distance_lower = (U-circle_radius_squared)/(2*R)
ellipse_distance_lower = ellipse_squared_margin/(2*R)
sum_lower = sum(lower_entries, F(0))
continuous_rate = sum_lower/8
finite_grid_constant = sum_lower/2
rho_log_lower = F(5, 26)
ellipse_growth_upper = F(2, 23)
quadrature_rate = 2*rho_log_lower/3-ellipse_growth_upper
required_rate = F(1, 32)

checks = {
    "node_clearance_squared": circle_radius_squared < (R-eta)**2,
    "ellipse_vertex_is_in_range": -1 < -d*s/(r*r) < 1,
    "ellipse_maximum": ellipse_radius_squared == F(377, 200),
    "ellipse_inside_boundary": ellipse_squared_margin == F(9, 1600) > 0,
    "circle_distance": circle_distance_lower == F(5, 176),
    "ellipse_distance": ellipse_distance_lower == F(9, 4400),
    "normalized_parameters": 0 < H < p < 1,
    "all_three_factor_coefficients": all(c > 0 for c in coefficient_margins),
    "quadratic_vertex": vertex == F(21, 32),
    "all_four_gain_entries": all(row["passed"] for row in rows),
    "gain_sum": sum_lower == F(3, 10),
    "continuous_rate": continuous_rate == F(3, 80) > required_rate,
    "finite_grid_constant": finite_grid_constant == F(3, 20),
    "exponential_constant_below_two": 1/(1-finite_grid_constant) < 2,
    "sqrt26_comparison": F(26) < F(26, 5)**2,
    "ellipse_growth_log_bound": d/u == F(25, 23) and d/u-1 == ellipse_growth_upper,
    "geometric_denominator_for_m_ge_three": 6*rho_log_lower > 1,
    "quadrature_rate": quadrature_rate == F(37, 897) > continuous_rate,
    "continuous_prefactor": 4/circle_distance_lower < 144,
    "ellipse_prefactor": 1/ellipse_distance_lower < 500,
    "total_prefactor": F(144+2000, 3) < 720,
    "final_rate_margin": continuous_rate-required_rate == F(1, 160),
}

certificate = {
    "purpose": "Exact arithmetic only; not an independent analytic audit or Xi certificate.",
    "family": "m odd >=3, n=3m, a_k=-5/4+(i/2)cos((2k-1)pi/(2m)), residues 1",
    "parameters": {name: rational(value) for name, value in [
        ("d", d), ("R", R), ("eta", eta), ("r", r), ("s", s),
        ("u", u), ("p", p), ("H", H),
    ]},
    "geometry": {
        "circle_radius_squared": rational(circle_radius_squared),
        "node_clearance_squared_margin": rational((R-eta)**2-circle_radius_squared),
        "ellipse_radius_squared": rational(ellipse_radius_squared),
        "ellipse_squared_margin": rational(ellipse_squared_margin),
        "circle_distance_lower": rational(circle_distance_lower),
        "ellipse_distance_lower": rational(ellipse_distance_lower),
    },
    "factor_polynomial_coefficient_margins": [rational(c) for c in coefficient_margins],
    "gain_table": rows,
    "bounds": {
        "quarter_lower_sum": rational(sum_lower),
        "continuous_decay": rational(continuous_rate),
        "finite_grid_log_constant": rational(finite_grid_constant),
        "rho_log_lower": rational(rho_log_lower),
        "ellipse_growth_upper": rational(ellipse_growth_upper),
        "quadrature_decay": rational(quadrature_rate),
        "quadrature_margin_over_continuous": rational(quadrature_rate-continuous_rate),
        "actual_full_boundary_decay": rational(continuous_rate),
        "required_decay": rational(required_rate),
        "final_decay_margin": rational(continuous_rate-required_rate),
        "full_boundary_prefactor": 720,
    },
    "checks": checks,
    "failures": [key for key, passed in checks.items() if not passed],
    "passed": all(checks.values()),
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2)+"\n", encoding="utf-8")
print(f"Passed: {certificate['passed']}; failures: {certificate['failures']}")
print(f"Full-boundary decay: {continuous_rate}; required > {required_rate}; margin {continuous_rate-required_rate}")
print(f"Quadrature decay: {quadrature_rate}; required >= {continuous_rate}")
print(f"Four gain margins: {', '.join(str(F(row['margin']['numerator'], row['margin']['denominator'])) for row in rows)}")
print(f"Three factor margins: {', '.join(map(str, coefficient_margins))}")
print(f"Boundary prefactor: 720*n; certificate: {output}")
raise SystemExit(0 if certificate['passed'] else 1)
