"""Enclose Laguerre levels 3--16 on [10,20], under L037.

L314 records the cutoff, Fourier identities, tails and height remainder.
Together with the existing low-level signs this excludes nonreal centers
through twenty. No unbounded-height or RH conclusion is claimed.
"""

import argparse
from fractions import Fraction
import hashlib
import json
from math import comb, factorial
from pathlib import Path

from certify_averaged_ordering import (
    I, ORDER, PRECISION, evaluate, moment_jet, multiply, pi_bounds,
    self_check, sin_cos, theta_kernel_jet, translate,
)

ROOT = Path(__file__).resolve().parents[2]
SOURCE = "scripts/laguerre/variance-cutoff-certificate.json"
CENTER = 15
DEGREE = 64
FIRST_LEVEL = 3
LAST_LEVEL = 16
MARGIN = Fraction(1, 10**6)


def cutoff_checks(pi):
    # The analytic argument in L314 reduces the cutoff to these rationals.
    e_upper = sum((Fraction(1, factorial(j)) for j in range(7)), Fraction(0))
    e_upper += Fraction(8, 7 * factorial(7))
    assert e_upper < Fraction(87, 32)
    assert Fraction(87, 32)**32 < 8 * 10**13
    assert Fraction(pi.lo) > Fraction(31, 10)
    assert Fraction(pi.hi) < Fraction(16, 5)
    assert Fraction(31, 10)**7 > 7**4
    assert Fraction(5 * 404 * 401, 16) > 50000
    ratio_bound = Fraction(8 * 8 * 10**13, 3 * 50000)
    assert ratio_bound < 4**LAST_LEVEL
    return {"M_strict_upper_bound": "1",
            "A_strict_lower_bound": "50000*exp(-32)",
            "exp_32_strict_upper_bound": str(8 * 10**13),
            "8M_over_3A_strict_upper_bound": str(ratio_bound),
            "uniform_witness_cutoff": LAST_LEVEL}


def integrand_jets(u, pi):
    kernel = theta_kernel_jet(u, pi)
    sine, cosine = sin_cos(CENTER * u, pi)
    cycle = (cosine, -sine, -cosine, sine)
    trig = [[cycle[(phase + ell) % 4]
             * I.rational(Fraction(CENTER**ell, factorial(ell)))
             for ell in range(ORDER + 1)] for phase in range(4)]
    return [multiply(moment_jet(u, j, kernel), trig[j % 4])
            for j in range(DEGREE + 1)]


def derivative_integrals(panels, pi, tail):
    if panels < 1:
        raise ValueError("Positive spatial panel count required")
    h = I.rational(Fraction(1, panels))
    weights = {ell: 2 * h**(ell + 1) / (ell + 1) for ell in (0, 2, 4, 6)}
    remainder_weight = 2 * h**9 / 9
    totals = [I(0) for _ in range(DEGREE + 1)]
    errors = [I(0) for _ in totals]
    for panel in range(panels):
        center = I.rational(Fraction(2 * panel + 1, panels))
        domain = I(I.rational(Fraction(2 * panel, panels)).lo,
                   I.rational(Fraction(2 * panel + 2, panels)).hi)
        midpoint = integrand_jets(center, pi)
        full_panel = integrand_jets(domain, pi)
        for j in range(DEGREE + 1):
            value = sum((midpoint[j][ell] * weight
                         for ell, weight in weights.items()), I(0))
            error = I(full_panel[j][ORDER].magnitude()) * remainder_weight
            totals[j] = totals[j] + value + I(error.hi.copy_negate(), error.hi)
            errors[j] = errors[j] + error
    return [v + I(tail.hi.copy_negate(), tail.hi) for v in totals], errors


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
    cutoff = cutoff_checks(pi)
    derivatives, errors = derivative_integrals(panels, pi, tail)
    # 2u^65 <= u^64 + u^66 on the positive half-line.
    moment_bound = (moments[64] + moments[66]) / 2
    powers = [derivatives[j] / factorial(j) for j in range(DEGREE + 1)]
    remainders = [moment_bound * 5**(DEGREE + 1 - j) / factorial(DEGREE + 1 - j)
                  for j in range(2 * LAST_LEVEL + 1)]
    masses = {n: sum((comb(2*n, j) * moments[j] * moments[2*n-j]
                      for j in range(0, 2*n + 1, 2)), I(0))
              for n in range(FIRST_LEVEL, LAST_LEVEL + 1)}
    if any(value.lo <= 0 for value in masses.values()):
        raise ArithmeticError("A mass denominator is not positive")
    half_width = I.rational(Fraction(5, cells))
    local = I(half_width.hi.copy_negate(), half_width.hi)
    rows, minima = [], {}
    for cell in range(cells):
        left = Fraction(10) + Fraction(10*cell, cells)
        right = Fraction(10) + Fraction(10*(cell+1), cells)
        center = I.rational((left + right)/2 - CENTER)
        translated = translate(powers, center)
        vals = []
        for j, remainder in enumerate(remainders):
            coeffs = [translated[j+ell] * (factorial(j+ell)//factorial(ell))
                      for ell in range(DEGREE-j+1)]
            vals.append(evaluate(coeffs, local)
                        + I(remainder.hi.copy_negate(), remainder.hi))
        ratios = {}
        for n, mass in masses.items():
            # Deliberately use the full, unpaired sum; all signs are enclosed.
            numerator = sum(((-1)**(n+j) * comb(2*n, j) * vals[j] * vals[2*n-j]
                             for j in range(2*n+1)), I(0))
            ratio = numerator / mass
            if Fraction(ratio.lo) <= MARGIN:
                raise ArithmeticError(f"R_{n} unresolved on [{left},{right}]: {ratio.data()}")
            if n not in minima or ratio.lo < minima[n]["value"]:
                minima[n] = {"value": ratio.lo, "cell": cell}
            ratios[str(n)] = ratio.data()
        rows.append({"a_interval": [str(left), str(right)],
                     "transform_derivatives": [v.data() for v in vals],
                     "normalized_Laguerre_coefficients": ratios})
    return {
        "scope": "levels 3--16 on 10<=|a|<=20; no unbounded-height or RH claim",
        "arithmetic_contract": "L037", "precision": PRECISION,
        "source_moments": SOURCE,
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "cutoff_bounds": cutoff, "pi": pi.data(),
        "theta_terms": 4, "u_cutoff": 2,
        "quadrature_panels": panels, "quadrature_taylor_order": ORDER,
        "height_center": CENTER, "height_taylor_degree": DEGREE,
        "common_integral_tail_bound": tail.data(),
        "quadrature_error_bounds": [v.data() for v in errors],
        "transform_derivatives_at_center": [v.data() for v in derivatives],
        "absolute_65th_moment_upper_bound": str(moment_bound.hi),
        "height_taylor_remainder_bounds": [v.data() for v in remainders],
        "mass_denominators": {str(n): value.data() for n, value in masses.items()},
        "height_cells": cells, "levels": [FIRST_LEVEL, LAST_LEVEL],
        "strict_normalized_margin": str(MARGIN),
        "minimum_lower_endpoints": {str(n): {"value": str(row["value"]), "cell": row["cell"]}
                                    for n, row in minima.items()},
        "cells": rows, "finite_witness_signs_certified": True,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--panels", type=int, default=256)
    parser.add_argument("--cells", type=int, default=512)
    args = parser.parse_args()
    self_check()
    print(json.dumps(certify(args.panels, args.cells), indent=2))
