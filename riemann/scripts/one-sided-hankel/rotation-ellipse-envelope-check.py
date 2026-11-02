#!/usr/bin/env python3
"""C645m rational margins, plus explicitly uncertified exploratory screens."""
import cmath
from fractions import Fraction as F
import json
import math
from pathlib import Path


def rational(v):
    return {"numerator": v.numerator, "denominator": v.denominator}


d, R, r = F(5, 4), F(11, 8), F(1, 2)
log_lower = 2*(F(2, 3)+F(2, 3)**3/3)
riemann_loss = 1/(d-1)-1/d
checks = {
    "log5_lower_above_three_halves": log_lower > F(3, 2),
    "riemann_loss": riemann_loss == F(16, 5),
    "onset_margin": F(39, 12)-riemann_loss > 0,
    "growth_rate_gap": F(17, 12)-F(4, 3) == F(1, 12) > 0,
    "ellipse_inside_disk": F(377, 200) < R*R,
    "ellipse_grid_clearance": d-F(1, 10) > 1,
    "rightmost_factor_positive": d-F(1, 10)-1 > 0,
    "grid_denominator_positive": R*R-d > 0,
}

# Record the exploratory computations in full. They are not interval
# estimates and are not used in any certified inequality.
xf, Rf, rf = -float(d), float(R), float(r)
endpoint_rows = []
for k in range(17):
    theta = 2*math.pi*k/16
    gains = []
    for y in [-rf, rf]:
        a = xf+1j*y
        gain = 0.0
        for j in range(2000):
            b = 1j*cmath.exp(1j*theta)*(j+.5)/2000
            ratio = (a-b)/(Rf*Rf-b.conjugate()*a)
            ratio /= (xf-b)/(Rf*Rf-b.conjugate()*xf)
            gain += math.log(abs(ratio))
        gains.append(gain/2000)
    endpoint_rows.append({"theta_over_pi": 2*k/16, "endpoint_gains": gains})

ellipse_rows = []
for s in [.025, .05, .075, .1]:
    worst, location = -math.inf, None
    for k in range(64):
        theta = 2*math.pi*k/64
        zeros = [1j*cmath.exp(1j*theta)*(j+.5)/400 for j in range(400)]
        for h in range(80):
            phi = 2*math.pi*h/80
            v = xf+s*math.cos(phi)+1j*math.sqrt(rf*rf+s*s)*math.sin(phi)
            cost = sum(math.log(abs((xf-b)/(Rf*Rf-b.conjugate()*xf)
                           *(Rf*Rf-b.conjugate()*v)/(v-b))) for b in zeros)/400
            if cost > worst:
                worst, location = cost, [k, h]
    quadrature_rate = 2/3*math.asinh(s/rf)
    ellipse_rows.append({"s": s, "screened_max_cost": worst,
                         "grid_location": location,
                         "quadrature_decay_rate": quadrature_rate,
                         "screened_net_decay": quadrature_rate-worst})

certificate = {
    "purpose": "Exact constant checks for C645m; no proof of the angular target or its negation.",
    "hypotheses": "n=3m>=39, m odd; 0<s<=1/10; theta=pi/2; C645l common poles",
    "exact_values": {key: rational(value) for key, value in {
        "log5_strict_lower": log_lower,
        "log5_margin_above_three_halves": log_lower-F(3, 2),
        "riemann_loss": riemann_loss,
        "onset_margin_at_39": F(39, 12)-riemann_loss,
        "inverse_weight_growth_coefficient": F(17, 12),
        "quadrature_decay_coefficient_upper": F(4, 3),
        "majorant_growth_coefficient_lower": F(1, 12),
        "majorant_prefactor_lower": 1/R,
        "target_decay_coefficient": F(1, 32),
    }.items()},
    "checks": checks,
    "failures": [name for name, passed in checks.items() if not passed],
    "passed": all(checks.values()),
    "exploratory_only": {
        "certified": False,
        "role": "Motivation only, not a bound; finite screens cannot verify the angular mean.",
        "endpoint_midpoint_t_count": 2000,
        "endpoint_rows": endpoint_rows,
        "ellipse_grid_counts": {"theta": 64, "phi": 80, "midpoint_t": 400},
        "ellipse_rows": ellipse_rows,
    },
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2)+"\n", encoding="utf-8")
print(f"Exact margins passed: {certificate['passed']}; failures: {certificate['failures']}")
print("Majorant lower bound: (8/11)*exp(s*n/12); required: error O(exp(-n/32)); no actual-error lower bound.")
print(f"Exact onset margin: {F(39, 12)-riemann_loss}; growth gap: {F(1, 12)}")
print(f"Uncertified screens saved, not used as proof; certificate: {output}")
raise SystemExit(0 if certificate["passed"] else 1)
