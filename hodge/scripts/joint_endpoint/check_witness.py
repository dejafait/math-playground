#!/usr/bin/env python3
"""Exact coefficient checks for L179; no sampling or geometric realization.

Run from the hodge notebook: python3 scripts/joint_endpoint/check_witness.py
The complete coefficient certificate is written beside this script.
"""

from fractions import Fraction
from itertools import permutations
from pathlib import Path
import json


class Poly:
    """Q[alpha, d, z, z^-1], with sparse exponent triples (alpha,z,d)."""

    def __init__(self, terms=None):
        self.terms = {k: Fraction(v) for k, v in (terms or {}).items() if v}

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Poly) else Poly({(0, 0, 0): value})

    def __add__(self, other):
        terms = self.terms.copy()
        for key, value in self.coerce(other).terms.items():
            terms[key] = terms.get(key, Fraction(0)) + value
        return Poly(terms)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        terms = {}
        for left, lv in self.terms.items():
            for right, rv in self.coerce(other).terms.items():
                key = tuple(a + b for a, b in zip(left, right))
                terms[key] = terms.get(key, Fraction(0)) + lv * rv
        return Poly(terms)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        if exponent < 0:
            if len(self.terms) != 1:
                raise ValueError("Only Laurent monomials can be inverted")
            (key, value), = self.terms.items()
            return Poly({tuple(e * exponent for e in key): value ** exponent})
        result = Poly.coerce(1)
        for _ in range(exponent):
            result *= self
        return result

    def __truediv__(self, scalar):
        return self * Fraction(1, scalar)

    def constant_z(self):
        return Poly({k: v for k, v in self.terms.items() if k[1] == 0})

    def z_support(self):
        return sorted({k[1] for k in self.terms})

    def encode(self):
        return [
            {"powers_alpha_z_d": list(k), "coefficient": str(v)}
            for k, v in sorted(self.terms.items())
        ]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def multiply(left, right):
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Poly())
         for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def subtract(left, right):
    return [[a - b for a, b in zip(lr, rr)] for lr, rr in zip(left, right)]


def determinant(matrix):
    value = Poly()
    for perm in permutations(range(len(matrix))):
        inversions = sum(perm[i] > perm[j]
                         for i in range(len(perm)) for j in range(i + 1, len(perm)))
        term = Poly.coerce((-1) ** inversions)
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        value += term
    return value


def encode_matrix(matrix):
    return [[Poly.coerce(entry).encode() for entry in row] for row in matrix]


tests = []


def zero_test(name, entries):
    values = [Poly.coerce(entry) for entry in entries]
    tests.append({"name": name, "passed": all(not v.terms for v in values),
                  "complete_residuals": [v.encode() for v in values]})


def flat(matrix):
    return [entry for row in matrix for entry in row]


s = 781
alpha = Poly({(1, 0, 0): 1})
z = Poly({(0, 1, 0): 1})
d = Poly({(0, 0, 1): 1})
epsilon = 1 - alpha ** 2
a = alpha + z + epsilon / 2 * z ** -1
b = z ** 4
c = (1 - a ** 2) * z ** -4
evaluation = [[(a + 1) * z ** -4, Poly.coerce(1)],
              [(a - 1) / 2, b / 2]]
omega = [[0, 1], [-1, 0]]
symmetric = [[0, 1], [1, 0]]
restricted = [[-c, a], [a, b]]
zero_test("split_involution", [a ** 2 + b * c - 1])
zero_test("evaluation_determinant_one", [determinant(evaluation) - 1])
zero_test("common_alternating_pullback",
          flat(subtract(multiply(multiply(transpose(evaluation), omega), evaluation), omega)))
zero_test("symmetric_pullback",
          flat(subtract(multiply(multiply(transpose(evaluation), symmetric), evaluation), restricted)))
zero_test("section_pair_symmetric_determinant_minus_one", [determinant(restricted) + 1])

polynomials = {"a": a, "b": b, "c": c,
               "a2": a * a, "b2": b * b, "c2": c * c,
               "ab": a * b, "ac": a * c, "bc": b * c}
expected_constants = {"a": alpha, "a2": Poly.coerce(1)}
for name, polynomial in polynomials.items():
    zero_test("constant_coefficient_" + name,
              [polynomial.constant_z() - expected_constants.get(name, Poly())])
support = sorted({power for polynomial in polynomials.values()
                  for power in polynomial.z_support()})
support_ok = all(power == 0 or power % s != 0 for power in support)
tests.append({"name": "root_sum_no_nonzero_multiple_of_781", "passed": support_ok,
              "actual_support": support, "required": "no nonzero exponent divisible by 781"})

# Coordinates are the three section quadrics X=sum x_i^2, T=sum x_i*y_i,
# Y=sum y_i^2. No section value is sampled.
coefficients = [-c, 2 * a, b]
first_moment = [s * value.constant_z() for value in coefficients]
second_moment = [[s * (left * right).constant_z() for right in coefficients]
                 for left in coefficients]
delta_endpoint = 14 * s * alpha ** 2
quartic_residual = [
    [delta_endpoint * second_moment[i][j] - 14 * first_moment[i] * first_moment[j]
     for j in range(3)] for i in range(3)
]
zero_test("full_quartic_coefficient_tensor", flat(quartic_residual))

# The KS block uses coordinates (e_+1,e_+2,e_-1,e_-2).
omega4 = [[0, 0, 1, 0], [0, 0, 0, 1], [-1, 0, 0, 0], [0, -1, 0, 0]]
sym4 = [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
action4 = [[2 if i == j and i < 2 else -2 if i == j else 0
            for j in range(4)] for i in range(4)]
ks = [[1, 0], [0, -d / 2], [0, d / 2], [1, 0]]
incoming = multiply(action4, ks)
ks_omega = multiply(multiply(transpose(ks), omega4), ks)
ks_b = multiply(multiply(transpose(ks), sym4), ks)
mixed_omega = multiply(multiply(transpose(ks), omega4), incoming)
incoming_omega = multiply(multiply(transpose(incoming), omega4), incoming)
zero_test("KS_alternating_normalization", flat(subtract(ks_omega, [[0, d], [-d, 0]])))
zero_test("KS_symmetric_isotropy", flat(ks_b))
zero_test("KS_incoming_alternating_orthogonality", flat(mixed_omega))
zero_test("incoming_alternating_normalization",
          flat(subtract(incoming_omega, [[0, -4 * d], [4 * d, 0]])))
ks_and_incoming = [ks[i] + incoming[i] for i in range(4)]
ks_det = determinant(ks_and_incoming)
zero_test("KS_and_incoming_direct_sum_determinant", [ks_det - 4 * d ** 2])

failures = [test["name"] for test in tests if not test["passed"]]
certificate = {
    "schema": "hodge-L179-joint-endpoint-exact-v1",
    "result": "PASS" if not failures else "FAIL",
    "scope": "Exact finite-data identities only; no geometric realization or independent proof audit",
    "parameters": {"s": s, "dim_H": 46, "dim_E_z": 52, "dim_normal_fibre": 48,
                   "dim_K_N": 15, "alpha_relation": "alpha^2=(d^2-16+14*s)/(14*s)",
                   "d": "twice the root of x^3+x^2-2*x-1 in (1,5/4)",
                   "z": "ranges over all 781st roots of unity",
                   "point_weight": "delta_B/d", "gamma": "delta_B/(2*pi*i)^2"},
    "coefficient_ring": "Q[alpha,d,z,z^-1]; exponent triples are (alpha,z,d)",
    "laurent_polynomials": {name: value.encode() for name, value in polynomials.items()},
    "root_sum_support": {"minimum": min(support), "maximum": max(support), "all": support,
                         "required_absolute_bound": s, "proved_by": "finite geometric series"},
    "evaluation_matrix": encode_matrix(evaluation),
    "restricted_symmetric_matrix": encode_matrix(restricted),
    "point_quadric_basis": ["X", "T", "Y"],
    "first_moment": [value.encode() for value in first_moment],
    "second_moment": encode_matrix(second_moment),
    "quartic_residual_tensor": encode_matrix(quartic_residual),
    "KS_matrix": encode_matrix(ks),
    "KS_plus_incoming_determinant": ks_det.encode(),
    "tests": tests,
    "failures": failures,
    "analytical_obligations": [
        "L179 proves d, gamma, alpha and Delta nonzero using the retained exact root intervals.",
        "L179 verifies every full-domain Atiyah Gram block, the k-line scalar factors and the radical kernel.",
        "L179 proves the rank statements and inventories the retained and omitted geometric conditions.",
        "The 46-dimensional blocks are 23 copies of the checked two-dimensional matrices."
    ]
}
output = Path(__file__).with_name("L179-exact-certificate.json")
output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
print(f"{certificate['result']}: {len(tests)} exact checks; failures={failures}")
print(f"Root-sum exponents: actual [{min(support)},{max(support)}]; required |m|<781 for m!=0.")
print("Dimensions: H=46, derived fibre=52, normal fibre=48, normal obstruction=15.")
print(f"Full certificate: {output.relative_to(Path.cwd())}")
raise SystemExit(bool(failures))
