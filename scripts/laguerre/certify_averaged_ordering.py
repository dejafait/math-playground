"""Enclose the first averaged level comparison on [10,20], under L037.

L313 proves the Fourier identities, tails and height Taylor remainder.
This covers levels one and two only, with no all-level or RH claim.
"""

import argparse
from fractions import Fraction
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "hankel"))
from certify_hankel import (  # noqa: E402
    I, ORDER, PRECISION, moment_jet, multiply, pi_bounds, self_check,
    theta_kernel_jet,
)
from certify_conditional_cosine import sin_cos  # noqa: E402

SOURCE = "scripts/laguerre/variance-cutoff-certificate.json"
CENTER = 15
DEGREE = 32
DIFFERENCE_MARGIN = Fraction(4, 10**7)
FIRST_MARGIN = Fraction(1, 10**7)


def integrand_jets(u, pi):
    kernel = theta_kernel_jet(u, pi)
    sine, cosine = sin_cos(CENTER * u, pi)
    cycle = (cosine, -sine, -cosine, sine)
    trig = [
        [cycle[(phase + ell) % 4] * I.rational(Fraction(CENTER**ell, factorial(ell)))
         for ell in range(ORDER + 1)]
        for phase in range(4)
    ]
    return [multiply(moment_jet(u, j, kernel), trig[j % 4])
            for j in range(DEGREE + 1)]


def derivative_integrals(panels, pi, tail):
    if panels < 1:
        raise ValueError("Positive panel count required")
    h = I.rational(Fraction(1, panels))
    weights = {ell: 2 * h**(ell+1) / (ell+1) for ell in (0, 2, 4, 6)}
    remainder_weight = 2 * h**9 / 9
    totals = [I(0) for _ in range(DEGREE + 1)]
    errors = [I(0) for _ in totals]
    for panel in range(panels):
        center = I.rational(Fraction(2*panel + 1, panels))
        domain = I(I.rational(Fraction(2*panel, panels)).lo,
                   I.rational(Fraction(2*panel+2, panels)).hi)
        midpoint = integrand_jets(center, pi)
        full_panel = integrand_jets(domain, pi)
        for j in range(DEGREE + 1):
            value = sum((midpoint[j][ell] * weight for ell, weight in weights.items()), I(0))
            error = I(full_panel[j][ORDER].magnitude()) * remainder_weight
            totals[j] = totals[j] + value + I(error.hi.copy_negate(), error.hi)
            errors[j] = errors[j] + error
    return [v + I(tail.hi.copy_negate(), tail.hi) for v in totals], errors


def translate(powers, center):
    # Coefficients of p(center+x), obtained by the exact binomial identity.
    degree = len(powers) - 1
    center_powers = [I(1)]
    for _ in range(degree):
        center_powers.append(center_powers[-1] * center)
    return [sum((comb(k, ell) * powers[k] * center_powers[k-ell]
                 for k in range(ell, degree+1)), I(0))
            for ell in range(degree+1)]


def evaluate(powers, x):
    result = I(0)
    for value in reversed(powers):
        result = result * x + value
    return result


def certify(panels, cells):
    if cells < 1:
        raise ValueError("Positive height cell count required")
    source_bytes = (ROOT / SOURCE).read_bytes()
    source = json.loads(source_bytes)
    if source["arithmetic_contract"] != "L037" or not source["variance_threshold_certified"]:
        raise ValueError("Unexpected source certificate")
    moments = {int(j): I(v["lower"], v["upper"])
               for j, v in source["half_line_moments"].items()}
    tail = I(source["common_tail_bound"]["lower"], source["common_tail_bound"]["upper"])
    pi = pi_bounds()
    derivatives, errors = derivative_integrals(panels, pi, tail)
    # u^33 <= (u^32+u^34)/2 on the positive half-line.
    moment_bound = (moments[32] + moments[34]) / 2
    powers = [[derivatives[j+ell] / factorial(ell)
               for ell in range(DEGREE-j+1)] for j in range(5)]
    remainders = [moment_bound * 5**(DEGREE+1-j) / factorial(DEGREE+1-j)
                  for j in range(5)]
    mass1 = moments[0] * moments[2]
    mass2 = moments[0] * moments[4] + 3 * moments[2]**2
    if mass1.lo <= 0 or mass2.lo <= 0:
        raise ArithmeticError("Mass denominator not positive")
    half_width = I.rational(Fraction(5, cells))
    local = I(half_width.hi.copy_negate(), half_width.hi)
    rows = []
    minima = {"R_1": None, "R_2_minus_R_1": None}
    for cell in range(cells):
        left, right = Fraction(10) + Fraction(10*cell, cells), Fraction(10) + Fraction(10*(cell+1), cells)
        center = I.rational((left+right)/2 - CENTER)
        vals = []
        for poly, remainder in zip(powers, remainders):
            vals.append(evaluate(translate(poly, center), local)
                        + I(remainder.hi.copy_negate(), remainder.hi))
        f, fp, fpp, fppp, fpppp = vals
        r1 = (fp*fp - f*fpp) / mass1
        r2 = (f*fpppp - 4*fp*fppp + 3*fpp*fpp) / mass2
        difference = r2 - r1
        for name, value, margin in (("R_1", r1, FIRST_MARGIN),
                                    ("R_2_minus_R_1", difference, DIFFERENCE_MARGIN)):
            if Fraction(value.lo) <= margin:
                raise ArithmeticError(f"{name} unresolved on [{left},{right}]: {value.data()}")
            if minima[name] is None or value.lo < minima[name]["value"]:
                minima[name] = {"value": value.lo, "cell": cell}
        rows.append({"a_interval": [str(left), str(right)],
                     "transform_derivatives": [v.data() for v in vals],
                     "R_1": r1.data(), "R_2": r2.data(),
                     "R_2_minus_R_1": difference.data()})
    return {
        "scope": "R_2>R_1>0 on 10<=|a|<=20 only; no all-level or RH claim",
        "arithmetic_contract": "L037", "precision": PRECISION,
        "source_moments": SOURCE,
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "pi": pi.data(), "theta_terms": 4, "u_cutoff": 2,
        "quadrature_panels": panels, "quadrature_taylor_order": ORDER,
        "height_center": CENTER, "height_taylor_degree": DEGREE,
        "common_integral_tail_bound": tail.data(),
        "quadrature_error_bounds": [v.data() for v in errors],
        "transform_derivatives_at_center": [v.data() for v in derivatives],
        "absolute_33rd_moment_upper_bound": str(moment_bound.hi),
        "height_taylor_remainder_bounds": [v.data() for v in remainders],
        "mass1": mass1.data(), "mass2": mass2.data(),
        "height_cells": cells,
        "strict_margins": {"R_1": str(FIRST_MARGIN),
                           "R_2_minus_R_1": str(DIFFERENCE_MARGIN)},
        "minimum_lower_endpoints": {key: {"value": str(row["value"]), "cell": row["cell"]}
                                    for key, row in minima.items()},
        "cells": rows, "first_averaged_comparison_certified": True,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--panels", type=int, default=256)
    parser.add_argument("--cells", type=int, default=512)
    args = parser.parse_args()
    self_check()
    print(json.dumps(certify(args.panels, args.cells), indent=2))
