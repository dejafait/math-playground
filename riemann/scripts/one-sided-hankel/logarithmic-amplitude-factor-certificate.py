#!/usr/bin/env python3
"""Exact rational certificate for the single-factor bounds used in L659."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return out


def scale(a, factor):
    return [factor * value for value in a]


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[i + j] += av * bv
    return out


def bernstein(a, left, right):
    degree = len(a) - 1
    width = right - left
    power = [sum((a[j] * comb(j, k) * left ** (j-k) * width ** k
                  for j in range(k, degree + 1)), F(0))
             for k in range(degree + 1)]
    return [sum((power[j] * F(comb(k, j), comb(degree, j))
                 for j in range(k + 1)), F(0))
            for k in range(degree + 1)]


def positive_cover(poly):
    pending = [(F(-1), F(1), 0)]
    cells = []
    failures = []
    while pending:
        left, right, depth = pending.pop()
        coefficients = bernstein(poly, left, right)
        if min(coefficients) > 0:
            cells.append({"left": str(left), "right": str(right),
                          "bernstein_coefficients": list(map(str, coefficients)),
                          "minimum": str(min(coefficients))})
        elif depth < 16:
            middle = (left + right) / 2
            pending.extend([(middle, right, depth + 1), (left, middle, depth + 1)])
        else:
            failures.append({"left": str(left), "right": str(right),
                             "coefficients": list(map(str, coefficients))})
    cells.sort(key=lambda cell: F(cell["left"]))
    covered = (not failures and cells[0]["left"] == "-1"
               and cells[-1]["right"] == "1"
               and all(cells[j]["right"] == cells[j+1]["left"]
                       for j in range(len(cells)-1)))
    return cells, failures, covered


def main():
    d, u2 = F(5, 4), F(121, 64)
    parameters = [(F(1, 2), F(101, 100)), (F(3, 4), F(21, 20)),
                  (F(9, 10), F(113, 100)), (F(1), F(129, 100))]
    checks, failures = [], []
    rate, additive, previous = F(0), F(0), F(0)
    for t, bound in parameters:
        n0 = [d*d+t*t, 2*d*t]
        d0 = [u2*u2+t*t*d*d, 2*u2*d*t]
        a = add(scale(d0, bound), scale(n0, -t*t))
        c = scale(mul(d0, n0), bound-1)
        middle = add(scale(d0, bound), scale(n0, -u2))
        determinant = add(mul(a, c), scale(mul([F(1), F(0), F(-1)],
                                               mul(middle, middle)), -t*t))
        cells, bad, covered = positive_cover(determinant)
        failures.extend(bad)
        if not covered:
            failures.append({"t": str(t), "failure": "incomplete interval cover"})
        e = bound-1
        half_log_upper = (e-e*e/2+e*e*e/3)/2
        rate += (t-previous)*half_log_upper
        additive += half_log_upper
        previous = t
        checks.append({"t": str(t), "squared_factor_bound": str(bound),
                       "determinant_power_coefficients": list(map(str, determinant)),
                       "cells": cells, "full_interval_covered": covered,
                       "minimum_bernstein_coefficient": str(min(F(v["minimum"]) for v in cells)),
                       "half_log_upper": str(half_log_upper)})
    comparisons = {
        "rate_actual": str(rate), "rate_required_strict_upper": "31/1000",
        "rate_margin": str(F(31,1000)-rate),
        "additive_actual": str(additive), "additive_required_strict_upper": "1",
        "additive_margin": str(1-additive),
        "required_target_rate": "1/32",
        "target_rate_margin": str(F(1,32)-F(31,1000))}
    riemann_terms = [1/(d-F(j,32))+F(j,32)/(u2-d*F(j,32)) for j in range(32)]
    lambda_lower = sum(riemann_terms, F(0))/32
    geometry_margin = F(273,200)**2-d*d-F(11,21)**2
    resonance_checks = {
        "lambda_lower_riemann_terms": list(map(str, riemann_terms)),
        "lambda_lower_riemann_mean": str(lambda_lower),
        "lambda_required_strict_lower": "2", "lambda_margin": str(lambda_lower-2),
        "ordinate_bound_using_pi_less_than_22_over_7": "11/21",
        "pole_radius_squared_margin": str(geometry_margin),
        "half_ratio_margin_U_minus_9d2_over_8": str(u2-9*d*d/8)}
    if not rate < F(31,1000) < F(1,32) or not additive < 1:
        failures.append({"failure": "rate or additive bound failed"})
    if not lambda_lower > 2 or not geometry_margin > 0 or not u2 > 9*d*d/8:
        failures.append({"failure": "resonance parameter bound failed"})
    output = Path(__file__).with_suffix(".json")
    certificate = {"kind": "EXACT_RATIONAL_CERTIFICATE", "checks": checks,
                   "comparisons": comparisons, "resonance_checks": resonance_checks,
                   "failures": failures,
                   "scope": "Four quartic determinant inequalities on all c in [-1,1]; logarithm and grid-count constants only. The analytic maximum principle and resonant-lattice asymptotics require the written proof."}
    output.write_text(json.dumps(certificate, indent=2)+"\n")
    print(f"Exact interval covers: {sum(c['full_interval_covered'] for c in checks)}/4; cells: {sum(len(c['cells']) for c in checks)}; failures: {len(failures)}")
    print(f"Rate actual {rate} ({float(rate):.12g}) < required 31/1000 < target 1/32; additive {additive} < 1")
    print(f"Lambda lower bound {float(lambda_lower):.12g} > required 2; pole-radius squared margin {geometry_margin} > 0")
    print(f"Full certificate: {output}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
