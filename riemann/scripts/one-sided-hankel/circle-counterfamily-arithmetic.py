#!/usr/bin/env python3
"""Exact rational checks for the one-sided circle counterfamily.

This certifies finite arithmetic only. The analytic inequalities and the
uniform Hankel estimate require the complete canonical proof.
Run from the active notebook:
  python3 scripts/one-sided-hankel/circle-counterfamily-arithmetic.py
"""

import json
from fractions import Fraction as F
from pathlib import Path


def exact(value):
    return {"numerator": value.numerator, "denominator": value.denominator}


delta, eta = F(2, 5), F(1, 100)
d, radius = F(11, 10), F(13, 10)
u, pole_radius, taylor_radius = F(239, 200), F(19, 200), F(1, 10)
terms = []
lower_sum = F(0)
for k in range(1, 9):
    t = F(k, 8)
    derivative = u / (u*u+t*t) - u*t*t / (radius**4+u*u*t*t)
    lower_thousandths = (derivative.numerator*1000)//derivative.denominator
    lower = F(lower_thousandths, 1000)
    lower_sum += lower
    terms.append({"k": k, "t": exact(t), "derivative": exact(derivative),
                  "lower_thousandths": lower_thousandths,
                  "cross_product_margin": derivative.numerator*1000
                  -lower_thousandths*derivative.denominator})
average = sum((F(v["derivative"]["numerator"], v["derivative"]["denominator"])
               for v in terms), F(0)) / 8
threshold = F(27, 50)
gain = (u-d)*threshold
required = delta/8
factor_constant = 1/(radius**2) + 1/(u-taylor_radius)
checks = {
    "parameter_range": 0 < eta < delta/2 and 0 < delta < F(1, 2),
    "anchor": -u+pole_radius == -d,
    "clearance": u+pole_radius == radius-eta,
    "taylor_boundary_clearance": radius-u-taylor_radius == F(1, 200),
    "monotone_v_first_term": d > 1,
    "monotone_v_second_term": radius**4 > u*u,
    "factor_constant_below_two": factor_constant < 2,
    "eight_rectangle_threshold": average > threshold,
    "all_table_cross_products_positive": all(v["cross_product_margin"] > 0 for v in terms),
    "table_lower_average": lower_sum/8 > threshold,
    "product_exponent": gain == F(513, 10000) and gain > required,
    "strict_exponent_gap": gain-required == F(13, 10000),
    "geometric_denominator_at_n5": (pole_radius/taylor_radius)**50 < F(1, 2),
    "final_prefactor": 10*(1/(radius-u)+400) < 4100,
}
failures = [name for name, passed in checks.items() if not passed]
certificate = {
    "scope": "Exact rational arithmetic; analytic proof is separate.",
    "parameters": {name: exact(value) for name, value in {
        "delta": delta, "eta": eta, "d": d, "R": radius,
        "u": u, "r": pole_radius, "s": taylor_radius, "C": F(10)
    }.items()},
    "derivative_rectangle_terms": terms,
    "rectangle_average": exact(average),
    "required_rectangle_threshold": exact(threshold),
    "rectangle_margin": exact(average-threshold),
    "table_lower_average": exact(lower_sum/8),
    "factor_constant": exact(factor_constant),
    "product_exponent_lower_bound": exact(gain),
    "required_exponent": exact(required),
    "strict_exponent_gap": exact(gain-required),
    "checks": checks,
    "failures": failures,
}
path = Path(__file__).with_name("circle-counterfamily-arithmetic.json")
path.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
print(f"Checks: {len(checks)-len(failures)}/{len(checks)} passed; failures: {failures}")
print(f"Rectangle average: {float(average):.12f}; required: {threshold}")
print(f"Table lower numerators /1000: {[v['lower_thousandths'] for v in terms]}")
print(f"Table lower average: {lower_sum/8}; required: {threshold}")
print(f"Product exponent: >= {gain}; required: {required}; gap: {gain-required}")
print(f"Factor constant: {factor_constant}; required: < 2")
print(f"Certificate: {path.as_posix()}")
raise SystemExit(bool(failures))
