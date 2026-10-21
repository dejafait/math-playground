#!/usr/bin/env python3
"""Exact finite algebra for L400; no analytic or RH verification."""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import factorial
from pathlib import Path
import json


def add(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, F(0)) + value
    return {key: value for key, value in out.items() if value}


def scale(a, value):
    return {key: coefficient * value for key, coefficient in a.items()
            if coefficient * value}


def mul(a, b):
    out = {}
    for m, x in a.items():
        for n, y in b.items():
            key = tuple(i + j for i, j in zip(m, n))
            out[key] = out.get(key, F(0)) + x * y
    return {key: value for key, value in out.items() if value}


def power(a, n):
    assert a
    out = {(0,) * len(next(iter(a))): F(1)}
    for _ in range(n):
        out = mul(out, a)
    return out


def variables(count):
    return [{tuple(int(i == j) for i in range(count)): F(1)}
            for j in range(count)]


def divide(a, b):
    remainder, quotient = dict(a), {}
    leading = max(b)
    while remainder:
        term = max(remainder)
        assert all(i >= j for i, j in zip(term, leading))
        exponent = tuple(i - j for i, j in zip(term, leading))
        value = remainder[term] / b[leading]
        quotient[exponent] = quotient.get(exponent, F(0)) + value
        remainder = add(remainder, scale(mul({exponent: value}, b), -1))
    assert mul(quotient, b) == a
    return quotient


def cmul(a, b):
    return (add(mul(a[0], b[0]), scale(mul(a[1], b[1]), -1)),
            add(mul(a[0], b[1]), mul(a[1], b[0])))


def real_product(a, b):
    return add(mul(a[0], b[0]), scale(mul(a[1], b[1]), -1))


def serialized(poly):
    return [{"powers": list(key), "coefficient": str(value)}
            for key, value in sorted(poly.items(), reverse=True)]


u = variables(4)
vandermonde = {(0, 0, 0, 0): F(1)}
for i, j in combinations(range(4), 2):
    vandermonde = mul(vandermonde, add(u[i], scale(u[j], -1)))
terms = []
for chosen in combinations(range(4), 2):
    cross = {(0, 0, 0, 0): F(1)}
    centered = {}
    for i in range(4):
        centered = add(centered, scale(u[i], F(1, 2) if i in chosen else F(-1, 2)))
    for i in chosen:
        for j in range(4):
            if j not in chosen:
                cross = mul(cross, add(u[i], scale(u[j], -1)))
    terms.append((divide(vandermonde, cross), centered))
kernel, divisions = {}, []
for n in range(13):
    numerator = {}
    for within, centered in terms:
        numerator = add(numerator, mul(within, power(centered, n)))
    quotient = divide(numerator, vandermonde) if numerator else {}
    if n < 4 or n % 2:
        assert not quotient
    else:
        kernel.update(scale(quotient, F((-1) ** (n // 2), factorial(n))))
    divisions.append({"exponential_degree": n, "exact_division": True,
                      "zero_quotient": not quotient})
for orders, value in kernel.items():
    for permuted in set(permutations(orders)):
        assert kernel.get(permuted, F(0)) == value

x, y, z, a, h = variables(5)
M = add(add(scale(power(z, 2), F(1, 2)), scale(mul(x, z), F(3, 4))),
        add(scale(power(x, 2), F(1, 32)), scale(power(y, 2), F(-1, 2))))
aa = add(z, scale(x, F(-1, 4)))
K = (scale(add(power(aa, 2), scale(power(y, 2), -1)), F(1, 2)),
     scale(mul(aa, y), -1))
V = scale(add(power(y, 2), scale(power(x, 2), F(1, 4))), F(1, 2))
J = (scale(add(power(y, 2), scale(power(x, 2), F(-1, 4))), F(1, 2)),
     scale(mul(x, y), F(-1, 2)))
P = add(mul(M, V), scale(add(mul(K[0], J[0]), mul(K[1], J[1])), F(1, 2)))
P1 = (add(mul(M, J[0]), mul(V, K[0])),
      add(mul(M, J[1]), mul(V, K[1])))
P2 = tuple(scale(part, F(1, 2)) for part in cmul(K, J))
r = add(power(a, 2), power(h, 2))
q = (add(power(a, 2), scale(power(h, 2), -1)), scale(mul(a, h), 2))
q2 = cmul(q, q)
weight_direct = power(add(mul(y, a), scale(mul(x, h), F(1, 2))), 2)
weight_harmonics = add(mul(V, r), real_product(J, q))
discriminant_leading = add(mul(M, r), real_product(K, q))
product_direct = mul(discriminant_leading, weight_direct)
product_harmonics = add(mul(P, power(r, 2)),
                        add(mul(real_product(P1, q), r), real_product(P2, q2)))
residual_weight = add(weight_direct, scale(weight_harmonics, -1))
residual_product = add(product_direct, scale(product_harmonics, -1))
assert not residual_weight and not residual_product

table, coefficient = [], F(0)
for exponents, factor in sorted(P.items(), reverse=True):
    nx, ny, nz, na, nh = exponents
    assert nx + ny + nz == 4 and na == nh == 0
    orders = (0,) * nx + (1,) * ny + (2,) * nz
    moment = kernel.get(orders, F(0))
    for j in orders:
        moment *= factorial(j)
    contribution = factor * moment
    coefficient += contribution
    table.append({"powers_xyz": list(exponents[:3]), "factor": str(factor),
                  "orders": list(orders), "moment": str(moment),
                  "contribution": str(contribution)})
assert coefficient < 0
report = {
    "kind": "exact_finite_algebra_only", "analytic_claim_verified": False,
    "failures": [], "variables": ["x", "y", "z", "a", "h"],
    "weight_residual": serialized(residual_weight),
    "product_residual": serialized(residual_product),
    "balanced_polynomial": serialized(P),
    "k1_polynomial": {"real": serialized(P1[0]), "imaginary": serialized(P1[1])},
    "k2_polynomial_including_half": {"real": serialized(P2[0]), "imaginary": serialized(P2[1])},
    "moment_table": table, "balanced_coefficient": str(coefficient),
    "division_checks": divisions, "permutation_symmetry": True,
    "kernel_coefficients": serialized(kernel),
    "required_bound": "gamma_W > 0 with complete error o(log^4 H)",
    "actual_bound": f"balanced q_W={coefficient}<0; analytic obligations in L400",
}
destination = Path(__file__).with_name("wronskian-weight-certificate.json")
destination.write_text(json.dumps(report, indent=2) + "\n")
print("RESULT: both polynomial identities exact; arithmetic failures=0")
print(f"ACTUAL: balanced q_W={coefficient}<0; REQUIRED: positive complete coefficient")
print(f"CERTIFICATE: {destination}")
print("LIMITATION: finite algebra only; analytic asymptotic and RH not verified")
