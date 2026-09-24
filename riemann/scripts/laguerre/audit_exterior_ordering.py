"""Exact-rational audit of the saved finite comparison polynomials.

Uses a different, coarser height partition and independently evaluates
the polynomial Taylor enclosures. This checks the saved polynomial
bounds, not the Fourier quadrature or the Decimal implementation.
"""

from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path
import sys

from audit_finite_witness_band import interval, plus, scale, square, times

ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = ROOT/"scripts/laguerre/exterior-ordering-certificate.json"
CELLS_PER_BAND = 128


def horner(poly, x):
    result = (Q(0), Q(0))
    for coefficient in reversed(poly):
        result = plus(scale(result, x), coefficient)
    return result


def magnitude(value):
    return max(abs(value[0]), abs(value[1]))


def main():
    certificate_bytes = CERTIFICATE.read_bytes()
    certificate = json.loads(certificate_bytes)
    source_bytes = (ROOT/certificate["source_fourier_inputs"]).read_bytes()
    assert hashlib.sha256(source_bytes).hexdigest() == certificate["source_sha256"]
    source = json.loads(source_bytes)
    moment_bytes = (ROOT/source["source_moments"]).read_bytes()
    assert hashlib.sha256(moment_bytes).hexdigest() == source["source_sha256"]
    moments = {int(j): interval(v) for j, v in json.loads(moment_bytes)["half_line_moments"].items()}
    denominators = {}
    for n in range(1, 18):
        value = (Q(0), Q(0))
        for j in range(0, 2*n+1, 2):
            value = plus(value, scale(times(moments[j], moments[2*n-j]), comb(2*n, j)))
        stored = interval(certificate["mass_denominators"][str(n)])
        assert 0 < stored[0] <= value[0] <= value[1] <= stored[1]
        denominators[n] = value
    errors = {int(n): Q(v["upper"]) for n, v in certificate["normalized_product_error_bounds"].items()}
    previous = Q(20)
    for row in certificate["cells"]:
        left, right = map(Q, row["a_interval"])
        assert left == previous < right
        previous = right
        for name, value in row["comparisons"].items():
            assert Q(value["lower"]) > (Q(5, 10**20) if name == "R_1" else Q(7, 10**19))
    assert previous == 40
    half_width = Q(5, CELLS_PER_BAND)
    minima = {}
    for band, anchor in zip(certificate["bands"], source["anchors"]):
        assert band["center"] == anchor["center"]
        # Unpaired exact-rational extraction of the constant coefficient.
        ds = [interval(v) for v in anchor["transform_derivatives"]]
        point_ratios = {}
        for n in range(1, 18):
            total = (Q(0), Q(0))
            for j in range(2*n+1):
                term = square(ds[j]) if j == n else times(ds[j], ds[2*n-j])
                total = plus(total, scale(term, (-1)**(n+j)*comb(2*n, j)))
            mass = denominators[n]
            point_ratios[n] = times(total, (1/mass[1], 1/mass[0]))
        for name, values in band["comparison_polynomials"].items():
            poly = [interval(v) for v in values]
            if name == "R_1":
                point = point_ratios[1]
                product_error = errors[1]
            else:
                n = int(name)
                point = plus(point_ratios[n+1], scale(point_ratios[n], -1))
                product_error = errors[n+1]+errors[n]
            assert poly[0][0] <= point[0] <= point[1] <= poly[0][1]
            derivs = [[scale(poly[k], comb(k, j)) for k in range(j, len(poly))]
                      for j in range(9)]
            for cell in range(CELLS_PER_BAND):
                midpoint = -Q(5)+(2*cell+1)*half_width
                # Constant term retained with its sign; remaining terms bounded
                # in absolute value, avoiding the certificate's interval Horner.
                constant = horner(poly, midpoint)
                variation = product_error
                for j in range(1, 8):
                    variation += magnitude(horner(derivs[j], midpoint))*half_width**j
                radius = abs(midpoint)+half_width
                # A coefficient absolute sum bounds the entire eighth derivative.
                bound = Q(0)
                for coefficient in reversed(derivs[8]):
                    bound = bound*radius+magnitude(coefficient)
                variation += bound*half_width**8
                lower = constant[0]-variation
                assert lower > 0, (band["center"], name, cell, str(lower))
                minima[name] = min(minima.get(name, lower), lower)
        print(f"Exact rational audit passed band centered at {band['center']}",
              file=sys.stderr, flush=True)
    print(json.dumps({
        "certificate_sha256": hashlib.sha256(certificate_bytes).hexdigest(),
        "checks_passed": True, "height_band": [20, 40],
        "independent_height_cells": 2*CELLS_PER_BAND,
        "positive_polynomial_enclosures": 2*CELLS_PER_BAND*17,
        "anchor_constant_coefficients_checked": 34,
        "method": "exact rational midpoint derivatives and absolute coefficient remainder on a coarser partition",
        "minimum_lower_bounds": {name: str(value) for name, value in minima.items()},
        "qualification": "checks saved polynomials; does not independently verify all coefficient construction, Fourier quadrature or Decimal implementation",
    }, indent=2))


if __name__ == "__main__":
    main()
