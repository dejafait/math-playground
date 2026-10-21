#!/usr/bin/env python3
"""Exact degree-four algebra check for L398; no analytic moment verification."""

from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json


def s_power(k, coefficient):
    return {(j, k - j): coefficient * comb(k, j) for j in range(k + 1)}


def add(target, source):
    for key, value in source.items():
        target[key] = target.get(key, F(0)) + value


def multiply(left, right):
    result = {}
    for (i, j), a in left.items():
        for (k, l), b in right.items():
            if i + j + k + l <= 4:
                key = (i + k, j + l)
                result[key] = result.get(key, F(0)) + a * b
    return result


vartheta = F(1, 100)
exponential = {}
for degree in range(5):
    add(exponential, s_power(degree, F(1, 2**degree * factorial(degree))))
j_series = {(0, 0): F(1)}
add(j_series, s_power(2, F(1, 24)))
add(j_series, s_power(4, F(1, 1920)))
factor = {(0, 0): F(4, 3) / vartheta, (1, 0): -F(1, 2),
          (0, 1): -F(1, 2), (1, 1): vartheta / 5}
polynomial = exponential.copy()
add(polynomial, multiply(factor, j_series))
orders = [(0, 0), (1, 1), (0, 2), (2, 2)]
jet_coefficients = {}
for i, j in orders:
    assert (i + j) % 2 == 0
    # i^i (-i)^j = (-1)^((i+j)/2+j) for the four even-total orders.
    sign = (-1) ** ((i + j) // 2 + j)
    jet_coefficients[(i, j)] = sign * factorial(i) * factorial(j) * polynomial[(i, j)]
expected = {
    (0, 0): 1 + F(4, 3) / vartheta,
    (1, 1): F(1, 4) + F(1, 9) / vartheta + vartheta / 5,
    (0, 2): -F(1, 4) - F(1, 9) / vartheta,
    (2, 2): F(1, 16) + F(1, 60) / vartheta + vartheta / 15,
}
actual = (jet_coefficients[(2, 2)] + F(3, 2) * jet_coefficients[(0, 2)]
          + jet_coefficients[(0, 0)] / 16 - jet_coefficients[(1, 1)]) / 2
required = -F(1, 4) - F(4, 45) / vartheta - vartheta / 15
failures = [f"jet {order}" for order in orders if jet_coefficients[order] != expected[order]]
if actual != required or actual != -F(10282, 1125):
    failures.append("signed combination")
if actual >= 0:
    failures.append("negative coefficient")
certificate = {
    "scope": "Exact rational degree-four generating-polynomial algebra only; no analytic error or limit verification.",
    "vartheta": str(vartheta),
    "generating_polynomial": {f"{i},{j}": str(value) for (i, j), value in sorted(polynomial.items())},
    "ordinary_jet_coefficients": {f"{i},{j}": str(value) for (i, j), value in jet_coefficients.items()},
    "expected_jet_coefficients": {f"{i},{j}": str(value) for (i, j), value in expected.items()},
    "balanced_scalar_coefficient": str(actual),
    "required_closed_expression": str(required),
    "sign_threshold": "0",
    "failures": failures,
}
path = Path(__file__).with_name("mollified_balanced_coeff_certificate.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Exact scalar coefficient: {actual}; required expression: {required}; sign threshold: 0")
print(f"Failures: {len(failures)}; full algebra certificate: {path}")
raise SystemExit(bool(failures))
