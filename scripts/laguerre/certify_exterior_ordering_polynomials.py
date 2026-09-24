"""Retain height-polynomial cancellation in the finite ordering test.

Fourier quadrature inputs come from certify_exterior_ordering.py.
All sums, product remainders and height-cell evaluations are enclosed.
"""

import hashlib
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import sys

from certify_averaged_ordering import I, evaluate

ROOT = Path(__file__).resolve().parents[2]
SOURCE = "scripts/laguerre/exterior-ordering-fourier-inputs.json"
LOCAL_ORDER = 8


def convolution(a, b):
    result = [I(0) for _ in range(len(a)+len(b)-1)]
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            result[j+k] = result[j+k]+x*y
    return result


def differentiated(poly, order):
    return [comb(k, order)*poly[k] for k in range(order, len(poly))]


def enclose(derivatives, center, local, radius):
    coefficients = [evaluate(poly, center) for poly in derivatives[:LOCAL_ORDER]]
    bound = evaluate(derivatives[LOCAL_ORDER], center+local).magnitude()
    error = I(bound)*radius**LOCAL_ORDER
    return evaluate(coefficients, local)+I(error.hi.copy_negate(), error.hi)


def certify():
    source_bytes = (ROOT/SOURCE).read_bytes()
    source = json.loads(source_bytes)
    assert source["arithmetic_contract"] == "L037"
    moment_bytes = (ROOT/source["source_moments"]).read_bytes()
    assert hashlib.sha256(moment_bytes).hexdigest() == source["source_sha256"]
    moment_data = json.loads(moment_bytes)
    moments = {int(j): I(v["lower"], v["upper"])
               for j, v in moment_data["half_line_moments"].items()}
    for j in range(1, 35, 2):
        # u^j <= (u^(j-1)+u^(j+1))/2; only an upper bound is used.
        moments[j] = (moments[j-1]+moments[j+1])/2
    masses = {int(n): I(v["lower"], v["upper"])
              for n, v in source["mass_denominators"].items()}
    errors = [I(v["lower"], v["upper"]) for v in source["height_taylor_remainder_bounds"]]
    product_errors = {}
    for n, mass in masses.items():
        terms = I(0)
        for j in range(2*n+1):
            k = 2*n-j
            terms += comb(2*n, j)*(moments[j]*errors[k]
                                  + moments[k]*errors[j]+errors[j]*errors[k])
        product_errors[n] = terms/mass
    cells_per_band = source["height_cells_per_band"]
    radius = I.rational(Fraction(5, cells_per_band))
    local = I(radius.hi.copy_negate(), radius.hi)
    bands, rows, minima, unresolved = [], [], {}, []
    for anchor in source["anchors"]:
        center = anchor["center"]
        ds = [I(v["lower"], v["upper"]) for v in anchor["transform_derivatives"]]
        polys = [[ds[j+ell]/factorial(ell) for ell in range(len(ds)-j)]
                 for j in range(35)]
        ratios = {}
        for n, mass in masses.items():
            numerator = [I(0) for _ in range(2*len(ds)-2*n-1)]
            for j in range(n+1):
                factor = comb(2*n, j)*(1 if j == n else 2*(-1)**(n+j))
                term = convolution(polys[j], polys[2*n-j])
                numerator = [x+factor*y for x, y in zip(numerator, term)]
            ratios[n] = [x/mass for x in numerator]
        comparisons = {"R_1": ratios[1]}
        comparison_errors = {"R_1": product_errors[1]}
        for n in range(1, 17):
            a, b = ratios[n+1], ratios[n]
            a = a+[I(0) for _ in range(len(b)-len(a))]
            name = str(n)
            comparisons[name] = [x-y for x, y in zip(a, b)]
            comparison_errors[name] = product_errors[n+1]+product_errors[n]
        derivative_polys = {name: [differentiated(poly, j) for j in range(LOCAL_ORDER+1)]
                            for name, poly in comparisons.items()}
        bands.append({"center": center,
                      "comparison_polynomials": {name: [v.data() for v in poly]
                                                 for name, poly in comparisons.items()}})
        print(f"Comparison polynomials formed at {center}", file=sys.stderr, flush=True)
        for cell in range(cells_per_band):
            left = Fraction(center-5)+Fraction(10*cell, cells_per_band)
            right = Fraction(center-5)+Fraction(10*(cell+1), cells_per_band)
            midpoint = I.rational((left+right)/2-center)
            enclosed = {}
            for name, polys_j in derivative_polys.items():
                error = comparison_errors[name]
                value = enclose(polys_j, midpoint, local, radius)
                value += I(error.hi.copy_negate(), error.hi)
                enclosed[name] = value.data()
                if name not in minima or value.lo < minima[name]["value"]:
                    minima[name] = {"value": value.lo, "cell": len(rows)}
                if value.lo <= 0:
                    unresolved.append({"comparison": name, "cell": len(rows),
                                       "enclosure": value.data()})
            rows.append({"a_interval": [str(left), str(right)], "comparisons": enclosed})
        print(f"Band [{center-5},{center+5}]: {len(unresolved)} unresolved so far",
              file=sys.stderr, flush=True)
    return {
        "scope": "finite adjacent comparisons n=1..16 and R_1 on 20<=|a|<=40 only",
        "arithmetic_contract": "L037", "source_fourier_inputs": SOURCE,
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "local_taylor_order": LOCAL_ORDER, "height_cells": len(rows),
        "mass_denominators": source["mass_denominators"],
        "normalized_product_error_bounds": {str(n): v.data() for n, v in product_errors.items()},
        "bands": bands, "cells": rows,
        "minimum_lower_endpoints": {name: {"value": str(v["value"]), "cell": v["cell"]}
                                    for name, v in minima.items()},
        "unresolved_comparisons": unresolved, "finite_ordering_certified": not unresolved,
    }


if __name__ == "__main__":
    result = certify()
    print(json.dumps(result, indent=2))
    if not result["finite_ordering_certified"]:
        sys.exit(1)
