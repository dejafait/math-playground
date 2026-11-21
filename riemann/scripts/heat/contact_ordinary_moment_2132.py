#!/usr/bin/env python3
"""Exact degree-seven witnesses for the two C874b contacts; stdlib only."""

from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json


DEGREE = 7
OUTPUT = Path(__file__).with_name("contact-ordinary-moment-2132.json")


def multiply(a, b):
    return [sum((a[j] * b[n-j] for j in range(n+1)), Q(0))
            for n in range(DEGREE+1)]


def determinant(matrix):
    """Exact Gaussian elimination with row swaps, without a sign assumption."""
    a = [list(row) for row in matrix]
    result = Q(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        value = a[j][j]
        result *= value
        for i in range(j+1, len(a)):
            scale = a[i][j] / value
            for k in range(j+1, len(a)):
                a[i][k] -= scale * a[j][k]
            a[i][j] = Q(0)
    return result


def permutation_determinant(a):
    """Independent Leibniz determinant for the corners of size at most four."""
    from itertools import permutations
    total = Q(0)
    for p in permutations(range(len(a))):
        inversions = sum(p[i] > p[j]
                         for i in range(len(a)) for j in range(i+1, len(a)))
        term = Q((-1)**inversions)
        for i, j in enumerate(p):
            term *= a[i][j]
        total += term
    return total


def strings(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, list):
        return [strings(x) for x in value]
    if isinstance(value, dict):
        return {k: strings(v) for k, v in value.items()}
    return value


def main():
    failures = []
    cases = []
    for name, second in (("rank_one", 2), ("rank_two", 3)):
        s = [Q(0), Q(16), Q(second)] + [Q(2)] * 5
        # a_n=[x^n]exp(-sum S_k x^k/k), x=z^2.
        # The differentiated series gives n*a_n=-sum S_k*a_(n-k).
        a = [Q(1)]
        for n in range(1, DEGREE+1):
            a.append(-sum((s[k]*a[n-k] for k in range(1, n+1)), Q(0))/n)
        product = [Q(1)] + [Q(0)] * DEGREE
        for k in range(1, DEGREE+1):
            factor = [Q(0)] * (DEGREE+1)
            for r in range(DEGREE//k+1):
                factor[k*r] = (-s[k]/k)**r / factorial(r)
            product = multiply(product, factor)
        if a != product:
            failures.append(name + ": coefficient methods disagree")

        m = [(-1)**n * factorial(2*n) * a[n] for n in range(DEGREE+1)]
        # Recover S from moments by a triangular logarithmic recurrence.
        recovered = [Q(0)]
        normalized = [(-1)**n * m[n] / factorial(2*n)
                      for n in range(DEGREE+1)]
        for n in range(1, DEGREE+1):
            recovered.append(-n*normalized[n] - sum(
                (recovered[k]*normalized[n-k] for k in range(1, n)), Q(0)))
        if recovered != s:
            failures.append(name + ": reconstructed logarithmic prefix mismatch")
        if m[0] != 1 or s[1] <= 0:
            failures.append(name + ": normalization or S_1 fails")

        matrices = {}
        for label, shift in (("A_3", 0), ("B_3", 1)):
            matrix = [[m[i+j+shift] for j in range(4)] for i in range(4)]
            minors = []
            for size in range(1, 5):
                corner = [row[:size] for row in matrix[:size]]
                value = determinant(corner)
                independent = permutation_determinant(corner)
                if value != independent:
                    failures.append(f"{name}/{label}/{size}: determinant mismatch")
                if value <= 0:
                    failures.append(f"{name}/{label}/{size}: minor {value} <= 0")
                minors.append(value)
            matrices[label] = {"matrix": matrix, "leading_minors": minors,
                               "required_strict_lower_bound": "0",
                               "all_strictly_positive": all(v > 0 for v in minors),
                               "leibniz_crosscheck": all(
                                   determinant([row[:n] for row in matrix[:n]]) ==
                                   permutation_determinant([row[:n] for row in matrix[:n]])
                                   for n in range(1, 5))}
        cases.append({"name": name, "S_1_through_S_7": s[1:],
                      "coefficients_a_0_through_a_7": a,
                      "factor_product_coefficients": product,
                      "moments_m_0_through_m_7": m,
                      "recovered_S_1_through_S_7": recovered[1:],
                      "matrices": matrices})

    report = {"step": "2132", "arithmetic": "fractions.Fraction, exact",
              "degree": DEGREE, "normalization": "m_0=1; x=u^2",
              "formula": "m_j=(-1)^j(2j)![z^(2j)]exp(-sum_(k=1)^7 S_k*z^(2k)/k)",
              "tested_S_1": "16", "cases": cases,
              "required_each_leading_minor": ">0",
              "all_witnesses_pass": not failures, "failures": failures,
              "scope": "finite ordinary Stieltjes compatibility only; not actual theta or all-order realization"}
    OUTPUT.write_text(json.dumps(strings(report), indent=2) + "\n")
    for case in cases:
        print(f"{case['name']}: S_1=16; m_0=1")
        for label, evidence in case["matrices"].items():
            print(f"  {label} leading minors={list(map(str, evidence['leading_minors']))}; required >0")
    print(f"failures={len(failures)}; all_witnesses_pass={not failures}; certificate={OUTPUT}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
