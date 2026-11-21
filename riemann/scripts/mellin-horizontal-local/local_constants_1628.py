#!/usr/bin/env python3
"""Exact rational checks for C048c; no numerical quadrature or sector grid."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json


def rational(q):
    q = F(q)
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


checks = []


def compare(name, actual, relation, required):
    actual, required = F(actual), F(required)
    passed = actual < required if relation == "<" else actual > required
    checks.append({"name": name, "actual": rational(actual),
                   "relation": relation, "required": rational(required),
                   "passed": passed})


compare("small_V_cos_clearance", F(1, 9), ">", F(1, 12))
compare("arcsine_clearance_squared", F(1, 16) / (1-F(1, 2304)),
        "<", F(13, 50)**2)
compare("large_V_delta_coefficient", F(4, 3)-F(4, 729)-F(13, 50),
        ">", F(16, 15))
compare("sine_clearance_coefficient", F(16, 15)*(1-F(4, 45)**2/6),
        ">", 1)
compare("segment_modulus", F(161, 36), ">", F(40, 9))
compare("segment_modulus_over_L", F(3, 8)-F(1, 432), ">", F(1, 3))
compare("curvature_upper", F(160, 27), "<", 6)
compare("amplitude_modulus", F(8, 7)*F(162, 161), "<", F(29, 25))
compare("linear_amplitude", F(85, 18), "<", F(19, 4))
compare("quadratic_amplitude", F(29, 50)*(F(81, 4)+F(81, 40)+F(81, 800)),
        "<", 13)
compare("cubic_phase", F(2656, 729), "<", F(73, 20))
compare("quartic_phase", F(3, 128)+F(32, 17), "<", 2)
compare("Z_coefficient", F(73, 20)+F(1, 18), "<", F(371, 100))
compare("quartic_residual", F(46, 9)*F(73, 20)+F(58, 25), "<", 22)
compare("sextic_residual", F(29, 50)*F(371, 100)**2, "<", 8)
assert F(39, 10)-F(371, 300) == F(799, 300)


def square_root_enclosure(q):
    q = F(q)
    scale = 10**15
    k = isqrt(q.numerator*scale**2 // q.denominator)
    lo, hi = F(k, scale), F(k+1, scale)
    assert lo**2 <= q < hi**2
    return lo, hi


x, y = F(39, 10), F(799, 300)
roots = {"sqrt6": (F(6), square_root_enclosure(6)),
         "sqrt39_over10": (x, square_root_enclosure(x)),
         "sqrt799_over300": (y, square_root_enclosure(y))}
s6lo, s6hi = roots["sqrt6"][1]
sxlo, sxhi = roots["sqrt39_over10"][1]
sylo, syhi = roots["sqrt799_over300"][1]
upper = s6hi*(F(13)/(2*x*sxlo*144)+F(33)/(2*x*x*sxlo*12)
              +F(15)/(y**3*sylo))
lower = s6lo*(F(13)/(2*x*sxhi*144)+F(33)/(2*x*x*sxhi*12)
              +F(15)/(y**3*syhi))
threshold = F(659107, 500000)
compare("A_loc_upper", upper, "<", threshold)

certificate = {
    "scope": "Exact coefficient comparisons only; analytic uniform proof is C048c.",
    "roots": {name: {"radicand": rational(q), "lower": rational(bounds[0]),
                      "upper": rational(bounds[1]),
                      "lower_square_le_radicand": bounds[0]**2 <= q,
                      "upper_square_gt_radicand": bounds[1]**2 > q}
              for name, (q, bounds) in roots.items()},
    "checks": checks,
    "A_loc": {"lower": rational(lower), "upper": rational(upper),
              "required_strict_upper": rational(threshold),
              "upper_slack": rational(threshold-upper)},
    "absorbed_curvature_coefficient": rational(F(799, 300)),
    "failures": [item["name"] for item in checks if not item["passed"]],
}
destination = Path(__file__).with_name("local_constants_1628.json")
destination.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"Exact rational checks: {len(checks)}, failures: {certificate['failures']}")
print(f"A_loc enclosure (decimal display only): {float(lower):.15f} .. {float(upper):.15f}")
print(f"Required strict upper: {float(threshold):.6f}; certified slack > {float(threshold-upper):.9g}")
print(f"Certificate: {destination.relative_to(Path.cwd())}")
if certificate["failures"]:
    raise SystemExit(1)
