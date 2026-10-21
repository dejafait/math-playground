#!/usr/bin/env python3
"""Exact weighted quartic algebra only; analytic application is in L394."""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import factorial
from pathlib import Path
import json

zero = (0, 0, 0, 0)

def add(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, F(0)) + value
    return {k: v for k, v in out.items() if v}

def scale(a, value):
    return {k: v * value for k, v in a.items() if v * value}

def mul(a, b):
    out = {}
    for m, x in a.items():
        for n, y in b.items():
            key = tuple(i + j for i, j in zip(m, n))
            out[key] = out.get(key, F(0)) + x * y
    return {k: v for k, v in out.items() if v}

def power(a, n):
    out = {zero: F(1)}
    for _ in range(n):
        out = mul(out, a)
    return out

def divide(a, b):
    remainder, quotient = dict(a), {}
    leading = max(b)
    while remainder:
        term = max(remainder)
        assert all(i >= j for i, j in zip(term, leading))
        exponent = tuple(i - j for i, j in zip(term, leading))
        value = remainder[term] / b[leading]
        quotient[exponent] = quotient.get(exponent, F(0)) + value
        remainder = add(remainder, scale(mul({exponent: F(1)}, b), -value))
    assert mul(quotient, b) == a
    return quotient

variables = [{tuple(int(i == j) for i in range(4)): F(1)} for j in range(4)]
vandermonde = {zero: F(1)}
for i, j in combinations(range(4), 2):
    vandermonde = mul(vandermonde, add(variables[i], scale(variables[j], -1)))
terms = []
for chosen in combinations(range(4), 2):
    cross = {zero: F(1)}
    for i in chosen:
        for j in range(4):
            if j not in chosen:
                cross = mul(cross, add(variables[i], scale(variables[j], -1)))
    centered = {}
    for i in range(4):
        centered = add(centered, scale(variables[i], F(1, 2) if i in chosen else F(-1, 2)))
    terms.append((divide(vandermonde, cross), centered))
kernel = {}
division_checks = []
for n in range(13):
    numerator = {}
    for within, centered in terms:
        numerator = add(numerator, mul(within, power(centered, n)))
    quotient = divide(numerator, vandermonde) if numerator else {}
    if n < 4 or n % 2:
        assert not quotient
    else:
        kernel.update(scale(quotient, F((-1) ** (n // 2), factorial(n))))
    division_checks.append({"exponential_degree": n, "exact_division": True,
                            "zero_quotient": not quotient})
for orders, value in kernel.items():
    for permuted in set(permutations(orders)):
        assert kernel.get(permuted, F(0)) == value

x, y, z = variables[:3]
M = add(add(scale(power(z, 2), F(1, 2)), scale(mul(x, z), F(3, 4))),
        add(scale(power(x, 2), F(1, 32)), scale(power(y, 2), F(-1, 2))))
def moment(exponents):
    a, b, c, unused = exponents
    assert a + b + c == 4 and unused == 0
    orders = (0,) * a + (1,) * b + (2,) * c
    value = kernel.get(orders, F(0))
    for j in orders:
        value *= factorial(j)
    return orders, value

matrix = [[F(0) for _ in range(3)] for _ in range(3)]
entries = []
for i in range(3):
    for j in range(i, 3):
        polynomial = mul(M, mul(variables[i], variables[j]))
        table = []
        for powers, coefficient in sorted(polynomial.items(), reverse=True):
            orders, value = moment(powers)
            contribution = coefficient * value
            matrix[i][j] += contribution
            table.append({"powers_xyz": list(powers[:3]), "coefficient": str(coefficient),
                          "orders": list(orders), "moment": str(value),
                          "contribution": str(contribution)})
        matrix[j][i] = matrix[i][j]
        entries.append({"entry": [i, j], "table": table, "value": str(matrix[i][j])})

assert matrix[0][1] == matrix[1][2] == 0
a, b, d, e = matrix[0][0], matrix[1][1], matrix[2][2], matrix[0][2]
block_determinant = a * d - e * e
principal_minors = [-a, a * b, -b * block_determinant]
assert all(value > 0 for value in principal_minors)
report = {"kind": "exact_finite_algebra_only", "analytic_claim_verified_by_script": False,
          "failures": [], "division_checks": division_checks,
          "permutation_symmetry": True, "entries": entries,
          "matrix": [[str(value) for value in row] for row in matrix],
          "xz_block_determinant": str(block_determinant),
          "negative_matrix_leading_principal_minors": [str(value) for value in principal_minors],
          "required_bound": "exists v with v^T C v > 0",
          "actual_bound": "C is strictly negative definite; no such nonzero v"}
destination = Path(__file__).with_name("weighted-coefficient-certificate.json")
destination.write_text(json.dumps(report, indent=2) + "\n")
print("RESULT: exact weighted matrix is strictly negative definite; failures=0")
print(f"MATRIX: {report['matrix']}")
print(f"NEGATIVE-MATRIX PRINCIPAL MINORS: {report['negative_matrix_leading_principal_minors']}")
print("REQUIRED: a positive quadratic direction; ACTUAL: none")
print(f"CERTIFICATE: {destination}")
print("LIMITATION: finite algebra only; no analytic moment or RH verification")
