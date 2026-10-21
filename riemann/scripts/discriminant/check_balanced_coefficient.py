#!/usr/bin/env python3
"""Exact finite six-term algebra; analytic applicability is proved in L393."""
from fractions import Fraction as F
from itertools import combinations
from math import factorial
from pathlib import Path
import json

ZERO = (0, 0, 0, 0)

def add(a, b):
    c = dict(a)
    for m, x in b.items():
        c[m] = c.get(m, F(0)) + x
        if not c[m]:
            del c[m]
    return c

def scale(a, x):
    return {m: v*x for m, v in a.items() if v*x}

def mul(a, b):
    c = {}
    for m, x in a.items():
        for n, y in b.items():
            k = tuple(i+j for i, j in zip(m, n))
            c[k] = c.get(k, F(0)) + x*y
    return {m: x for m, x in c.items() if x}

def power(a, n):
    b = {ZERO: F(1)}
    for _ in range(n):
        b = mul(b, a)
    return b

def divide_exact(a, b):
    r, q = dict(a), {}
    n = max(b)
    while r:
        m = max(r)
        if any(i < j for i, j in zip(m, n)):
            raise AssertionError(f"Nonzero polynomial remainder at {m}")
        k = tuple(i-j for i, j in zip(m, n))
        v = r[m]/b[n]
        q[k] = q.get(k, F(0)) + v
        r = add(r, scale(mul({k: F(1)}, b), -v))
    assert mul(q, b) == a
    return q

variables = [{tuple(int(i == j) for i in range(4)): F(1)} for j in range(4)]
vandermonde = {ZERO: F(1)}
for i, j in combinations(range(4), 2):
    vandermonde = mul(vandermonde, add(variables[i], scale(variables[j], -1)))

terms = []
for chosen in combinations(range(4), 2):
    other = tuple(i for i in range(4) if i not in chosen)
    cross = {ZERO: F(1)}
    for i in chosen:
        for j in other:
            cross = mul(cross, add(variables[i], scale(variables[j], -1)))
    within = divide_exact(vandermonde, cross)
    centered = {}
    for i in range(4):
        centered = add(centered, scale(variables[i], F(1, 2) if i in chosen else F(-1, 2)))
    terms.append((within, centered))

kernel = {}
certificates = []
for n in range(13):
    numerator = {}
    for within, centered in terms:
        numerator = add(numerator, mul(within, power(centered, n)))
    quotient = divide_exact(numerator, vandermonde) if numerator else {}
    if n < 4 or n % 2:
        assert not quotient, (n, quotient)
    else:
        # i^n is real for even n; cross products contain i^4=1.
        homogeneous = scale(quotient, F((-1)**(n//2), factorial(n)))
        kernel.update(homogeneous)
        certificates.append({
            "exponential_degree": n,
            "kernel_degree": n-4,
            "division_identity_checked": mul(quotient, vandermonde) == numerator,
            "coefficients": {','.join(map(str, m)): str(v) for m, v in sorted(homogeneous.items())},
        })

# P(x,y,z) in four-variable polynomial storage, unused last coordinate.
x, y, z = variables[:3]
M = scale(add(add(add(power(z, 2), scale(mul(x, z), F(3, 2))),
                  scale(power(x, 2), F(1, 16))), scale(power(y, 2), -1)), F(1, 2))
P = add(power(M, 2), scale(power(add(power(add(z, scale(x, F(-1, 4))), 2), power(y, 2)), 2), F(1, 8)))
table, q = [], F(0)
for monomial, coefficient in sorted(P.items(), reverse=True):
    a, b, c, unused = monomial
    assert a+b+c == 4 and unused == 0
    orders = (0,)*a + (1,)*b + (2,)*c
    moment = kernel.get(orders, F(0))
    for j in orders:
        moment *= factorial(j)
    contribution = coefficient*moment
    q += contribution
    table.append({"powers_xyz": [a, b, c], "P_coefficient": str(coefficient),
                  "jet_orders": list(orders), "kernel_derivative": str(moment),
                  "contribution": str(contribution)})

# Symmetry is required to assign monomial factors to any two orientations.
from itertools import permutations
for m, value in kernel.items():
    for permuted in set(permutations(m)):
        assert kernel.get(permuted, F(0)) == value
assert kernel[ZERO] == F(1, 12)
assert q > 0
report = {
    "kind": "exact_finite_algebra_only",
    "analytic_claim_verified_by_script": False,
    "failures": [],
    "checks": {"all_divisions_exact": True, "low_and_odd_cancellations": True,
               "permutation_symmetry": True, "kernel_at_zero": "1/12"},
    "moment_table": table,
    "quartic_coefficient": str(q),
    "required_bound": "quartic_coefficient > 0",
    "actual_bound": str(q),
    "homogeneous_certificates": certificates,
}
destination = Path(__file__).with_name("balanced-coefficient-certificate.json")
destination.write_text(json.dumps(report, indent=2) + "\n")
print(f"RESULT: exact finite algebra passed; failures=0; q={q}; required q>0")
print(f"TABLE: {len(table)} quartic monomials; kernel(0)=1/12; symmetric coefficients")
print(f"CERTIFICATE: {destination}")
print("LIMITATION: no analytic moment, tail, or endpoint proof is performed by this script")
