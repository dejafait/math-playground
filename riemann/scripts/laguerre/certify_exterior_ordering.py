"""Enclose adjacent normalized levels 1--16 on [20,40], under L037.

This tests a possible level-transfer mechanism on a finite rectangle only.
It supplies no all-height or all-level implication and no RH conclusion.
"""

import argparse
from fractions import Fraction
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import sys

from certify_averaged_ordering import I, PRECISION, evaluate, pi_bounds, self_check, sin_cos, translate

ROOT = Path(__file__).resolve().parents[2]
SOURCE = "scripts/laguerre/variance-cutoff-certificate.json"
ORDER = 16
DEGREE = 80
LAST_LEVEL = 17
CENTERS = (25, 35)


def product(a, b):
    return [sum((a[j] * b[n-j] for j in range(n+1)), I(0))
            for n in range(ORDER+1)]


def exponential(a):
    b = [a[0].exp()]
    for n in range(1, ORDER+1):
        b.append(sum((j*a[j]*b[n-j] for j in range(1, n+1)), I(0))/n)
    return b


def kernel_jet(u, pi):
    e2u = [I(2)*u, I(2)] + [I(0) for _ in range(ORDER-1)]
    e2u = exponential(e2u)
    ehalf = exponential([u/2, I.rational(Fraction(1, 2))]
                        + [I(0) for _ in range(ORDER-1)])
    total = [I(0) for _ in range(ORDER+1)]
    for m in range(1, 5):
        v = [x*pi*m*m for x in e2u]
        v2 = product(v, v)
        polynomial = [8*x-12*y for x, y in zip(v2, v)]
        term = product(polynomial, exponential([-x for x in v]))
        total = [x+y for x, y in zip(total, term)]
    return product(ehalf, total)


def integrand_jets(u, pi, center):
    kernel = kernel_jet(u, pi)
    sine, cosine = sin_cos(center*u, pi)
    cycle = (cosine, -sine, -cosine, sine)
    trig = [[cycle[(phase+ell) % 4]
             * I.rational(Fraction(center**ell, factorial(ell)))
             for ell in range(ORDER+1)] for phase in range(4)]
    # Share the kernel/trigonometric product before multiplying by u^j.
    weighted = [product(kernel, t) for t in trig]
    upowers = [I(1)]
    for _ in range(DEGREE):
        upowers.append(upowers[-1]*u)
    result = []
    for j in range(DEGREE+1):
        power = [comb(j, ell)*upowers[j-ell] if ell <= j else I(0)
                 for ell in range(ORDER+1)]
        result.append(product(power, weighted[j % 4]))
    return result


def derivative_integrals(panels, pi, tail, center):
    h = I.rational(Fraction(1, panels))
    weights = {ell: 2*h**(ell+1)/(ell+1) for ell in range(0, ORDER, 2)}
    remainder_weight = 2*h**(ORDER+1)/(ORDER+1)
    totals = [I(0) for _ in range(DEGREE+1)]
    errors = [I(0) for _ in totals]
    for panel in range(panels):
        midpoint = I.rational(Fraction(2*panel+1, panels))
        domain = I(I.rational(Fraction(2*panel, panels)).lo,
                   I.rational(Fraction(2*panel+2, panels)).hi)
        mid = integrand_jets(midpoint, pi, center)
        full = integrand_jets(domain, pi, center)
        for j in range(DEGREE+1):
            value = sum((mid[j][ell]*w for ell, w in weights.items()), I(0))
            error = I(full[j][ORDER].magnitude())*remainder_weight
            totals[j] = totals[j]+value+I(error.hi.copy_negate(), error.hi)
            errors[j] = errors[j]+error
    return [v+I(tail.hi.copy_negate(), tail.hi) for v in totals], errors


def certify(panels, cells_per_band):
    if panels < 1 or cells_per_band < 1:
        raise ValueError("Positive spatial and height panel counts required")
    source_bytes = (ROOT/SOURCE).read_bytes()
    source = json.loads(source_bytes)
    if source["arithmetic_contract"] != "L037" or not source["variance_threshold_certified"]:
        raise ValueError("Unexpected source moment certificate")
    moments = {int(j): I(v["lower"], v["upper"])
               for j, v in source["half_line_moments"].items()}
    tail = I(source["common_tail_bound"]["lower"], source["common_tail_bound"]["upper"])
    moment_bound = (moments[80]+moments[82])/2
    remainders = [moment_bound*5**(DEGREE+1-j)/factorial(DEGREE+1-j)
                  for j in range(2*LAST_LEVEL+1)]
    masses = {n: sum((comb(2*n, j)*moments[j]*moments[2*n-j]
                      for j in range(0, 2*n+1, 2)), I(0))
              for n in range(1, LAST_LEVEL+1)}
    if any(mass.lo <= 0 for mass in masses.values()):
        raise ArithmeticError("Nonpositive denominator enclosure")
    pi = pi_bounds()
    local_radius = I.rational(Fraction(5, cells_per_band))
    local = I(local_radius.hi.copy_negate(), local_radius.hi)
    rows, anchors, minima, unresolved = [], [], {}, []
    for center in CENTERS:
        derivatives, errors = derivative_integrals(panels, pi, tail, center)
        print(f"Fourier derivatives enclosed at {center}", file=sys.stderr, flush=True)
        powers = [derivatives[j]/factorial(j) for j in range(DEGREE+1)]
        anchors.append({"center": center,
                        "transform_derivatives": [v.data() for v in derivatives],
                        "quadrature_error_bounds": [v.data() for v in errors]})
        for cell in range(cells_per_band):
            left = Fraction(center-5)+Fraction(10*cell, cells_per_band)
            right = Fraction(center-5)+Fraction(10*(cell+1), cells_per_band)
            translated = translate(powers, I.rational((left+right)/2-center))
            values = []
            for j, remainder in enumerate(remainders):
                coeffs = [translated[j+ell]*(factorial(j+ell)//factorial(ell))
                          for ell in range(DEGREE-j+1)]
                values.append(evaluate(coeffs, local)
                              + I(remainder.hi.copy_negate(), remainder.hi))
            ratios = {}
            for n, mass in masses.items():
                numerator = sum(((-1)**(n+j)*comb(2*n, j)*values[j]*values[2*n-j]
                                 for j in range(2*n+1)), I(0))
                ratios[n] = numerator/mass
            differences = {n: ratios[n+1]-ratios[n] for n in range(1, LAST_LEVEL)}
            for n, value in differences.items():
                if n not in minima or value.lo < minima[n]["value"]:
                    minima[n] = {"value": value.lo, "cell": len(rows)}
                if value.lo <= 0:
                    unresolved.append({"cell": len(rows), "level": n,
                                       "difference": value.data()})
            rows.append({"a_interval": [str(left), str(right)],
                         "transform_derivatives": [v.data() for v in values],
                         "normalized_Laguerre_coefficients": {str(n): v.data() for n, v in ratios.items()},
                         "adjacent_differences": {str(n): v.data() for n, v in differences.items()}})
        print(f"Height band [{center-5},{center+5}] enclosed; "
              f"{len(unresolved)} unresolved comparisons so far", file=sys.stderr, flush=True)
    return {
        "scope": "R_(n+1)>R_n for 1<=n<=16 on 20<=|a|<=40 only; no global ordering or RH claim",
        "arithmetic_contract": "L037", "precision": PRECISION,
        "source_moments": SOURCE, "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "pi": pi.data(), "theta_terms": 4, "u_cutoff": 2,
        "quadrature_panels": panels, "quadrature_taylor_order": ORDER,
        "height_taylor_degree": DEGREE, "common_integral_tail_bound": tail.data(),
        "absolute_81st_moment_upper_bound": str(moment_bound.hi),
        "height_taylor_remainder_bounds": [v.data() for v in remainders],
        "anchors": anchors, "mass_denominators": {str(n): v.data() for n, v in masses.items()},
        "height_cells_per_band": cells_per_band, "height_cells": len(rows),
        "comparison_levels": [1, 16],
        "minimum_difference_lower_endpoints": {str(n): {"value": str(v["value"]), "cell": v["cell"]}
                                               for n, v in minima.items()},
        "cells": rows, "unresolved_comparisons": unresolved,
        "finite_ordering_certified": not unresolved,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--panels", type=int, default=128)
    parser.add_argument("--cells-per-band", type=int, default=512)
    parser.add_argument("--fourier-only", action="store_true",
                        help="save Fourier inputs and the inconclusive derivative-box assessment")
    args = parser.parse_args()
    self_check()
    result = certify(args.panels, args.cells_per_band)
    if args.fourier_only:
        result["initial_derivative_box_test"] = {
            "comparisons": result["height_cells"]*16,
            "unresolved": len(result["unresolved_comparisons"]),
            "minimum_difference_lower_endpoints": result["minimum_difference_lower_endpoints"],
            "first_unresolved": next(iter(result["unresolved_comparisons"]), None),
            "interpretation": "inconclusive enclosures, not negative signs",
        }
        for key in ("cells", "unresolved_comparisons", "minimum_difference_lower_endpoints", "finite_ordering_certified"):
            del result[key]
    print(json.dumps(result, indent=2))
    if not args.fourier_only and not result["finite_ordering_certified"]:
        sys.exit(1)
