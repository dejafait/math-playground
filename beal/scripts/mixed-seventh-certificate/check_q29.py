#!/usr/bin/env python3
"""Reproduce the displayed q=29 arithmetic; no modular-list coverage is assumed.

Run from the beal notebook: python3 scripts/mixed-seventh-certificate/check_q29.py
Uses only the Python standard library. Coefficients in arrays are constant first.
"""

from collections import Counter
from fractions import Fraction
import json
from pathlib import Path


Q = 29
NR = 2
ELL = 7
SOURCE = "https://arxiv.org/html/2609.26996v1"
PARAMETERS = [(10, 14), (14, 10), (24, 25), (28, 15)]
EXPECTED_TRACES = [[6, 6, 1], [4, 6, 1], [4, 0, 1], [3, 2, 1]]
COMPARISON = [[0, 1], [0, 0, 1], [2, 5, 1], [4, 3, 1], [-2, 1], [-5, 1]]
EXPECTED_RESULTANTS = [[6, 1, 5, 1, 1, 5], [4, 2, 3, 1, 6, 3],
                       [4, 2, 6, 1, 1, 1], [3, 2, 6, 2, 4, 3]]


def trim(poly):
    poly = [c % Q for c in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def remainder(a, b):
    a, b = trim(a), trim(b)
    assert b != [0]
    while a != [0] and len(a) >= len(b):
        shift = len(a) - len(b)
        factor = a[-1] * pow(b[-1], -1, Q) % Q
        for i, value in enumerate(b):
            a[i + shift] = (a[i + shift] - factor * value) % Q
        a = trim(a)
    return a


def poly_gcd(a, b):
    a, b = trim(a), trim(b)
    while b != [0]:
        a, b = b, remainder(a, b)
    inv = pow(a[-1], -1, Q)
    return [(c * inv) % Q for c in a]


def mul_ext(x, y):
    a, b = x
    c, d = y
    return ((a * c + NR * b * d) % Q, (a * d + b * c) % Q)


def eval_base(poly, x):
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % Q
    return value


def eval_ext(poly, x):
    value = (0, 0)
    for coefficient in reversed(poly):
        a, b = mul_ext(value, x)
        value = ((a + coefficient) % Q, b)
    return value


def character_base(value):
    if value % Q == 0:
        return 0
    power = pow(value % Q, (Q - 1) // 2, Q)
    assert power in (1, Q - 1)
    return 1 if power == 1 else -1


def character_ext(value):
    a, b = value
    return character_base(a * a - NR * b * b)


def sylvester(p, h):
    p, h = list(reversed(p)), list(reversed(h))
    m, n = len(p) - 1, len(h) - 1
    size = m + n
    return ([([0] * i + p + [0] * (size - i - len(p))) for i in range(n)]
            + [([0] * i + h + [0] * (size - i - len(h))) for i in range(m)])


def det_mod(matrix):
    a = [[c % ELL for c in row] for row in matrix]
    result = 1
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result % ELL
        value = a[j][j]
        result = result * value % ELL
        inv = pow(value, -1, ELL)
        for i in range(j + 1, len(a)):
            factor = a[i][j] * inv % ELL
            for k in range(j, len(a)):
                a[i][k] = (a[i][k] - factor * a[j][k]) % ELL
    return result


def det_exact(matrix):
    a = [[Fraction(c) for c in row] for row in matrix]
    result = Fraction(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        value = a[j][j]
        result *= value
        for i in range(j + 1, len(a)):
            factor = a[i][j] / value
            for k in range(j, len(a)):
                a[i][k] -= factor * a[j][k]
    assert result.denominator == 1
    return int(result)


def main():
    assert character_base(NR) == -1
    base_elements = list(range(Q))
    extension_elements = [(a, b) for a in base_elements for b in base_elements]
    squares_base = Counter(y * y % Q for y in base_elements)
    squares_extension = Counter(mul_ext(y, y) for y in extension_elements)
    infinity_roots = [v for v in base_elements if v * v % Q == 5]
    assert infinity_roots == [11, 18]
    assert all(2 * v % Q != 0 for v in infinity_roots)
    assert sum(squares_base.values()) == Q
    assert sum(squares_extension.values()) == Q * Q
    # Check the two independent square predicates on every field element.
    assert all(squares_base[v] == 1 + character_base(v) for v in base_elements)
    assert all(squares_extension[v] == 1 + character_ext(v) for v in extension_elements)
    rows = []
    resultants = []
    all_match = True
    for index, (eta, t) in enumerate(PARAMETERS):
        f = [t * t, 0, 0, 10 * t, 0, -12, 5]
        derivative = [i * f[i] for i in range(1, len(f))]
        gcd = poly_gcd(f, derivative)
        assert gcd == [1], (t, gcd)
        values_base = [eval_base(f, x) for x in base_elements]
        values_extension = [eval_ext(f, x) for x in extension_elements]
        n1_affine = sum(squares_base[v] for v in values_base)
        n2_affine = sum(squares_extension[v] for v in values_extension)
        bins1 = Counter(character_base(v) for v in values_base)
        bins2 = Counter(character_ext(v) for v in values_extension)
        assert n1_affine == Q + bins1[1] - bins1[-1]
        assert n2_affine == Q * Q + bins2[1] - bins2[-1]
        n1, n2 = n1_affine + 2, n2_affine + 2
        a = Q + 1 - n1
        s2 = Q * Q + 1 - n2
        assert (a * a - s2) % 2 == 0
        b = (a * a - s2) // 2
        frobenius = [Q * Q, -Q * a, b, -a, 1]
        trace = [b - 2 * Q, -a, 1]
        trace_mod = [c % ELL for c in trace]
        actual = [det_mod(sylvester(trace_mod, h)) for h in COMPARISON]
        exact = [det_exact(sylvester(trace, h)) for h in COMPARISON]
        assert actual == [value % ELL for value in exact]
        trace_match = trace_mod == EXPECTED_TRACES[index]
        resultant_match = actual == EXPECTED_RESULTANTS[index]
        all_match = all_match and trace_match and resultant_match
        resultants.append(actual)
        rows.append({
            "eta_label": eta, "t": t, "smoothness_gcd_constant_first": gcd,
            "character_bins_F29": {str(k): bins1[k] for k in (-1, 0, 1)},
            "character_bins_F841": {str(k): bins2[k] for k in (-1, 0, 1)},
            "N1_affine": n1_affine, "N2_affine": n2_affine,
            "N1_projective": n1, "N2_projective": n2,
            "A": a, "B": b,
            "frobenius_polynomial_constant_first": frobenius,
            "two_trace_polynomial_constant_first": trace,
            "two_trace_polynomial_mod7_constant_first": trace_mod,
            "expected_two_trace_polynomial_mod7_constant_first": EXPECTED_TRACES[index],
            "trace_matches": trace_match, "exact_resultants": exact,
            "resultants_mod7": actual, "expected_resultants_mod7": EXPECTED_RESULTANTS[index],
            "resultants_match": resultant_match,
        })
        print(f"eta={eta}, t={t}: N1={n1}, N2={n2}, A={a}, B={b}, "
              f"trace(mod7)={trace_mod}, resultants={actual}")
    report = {
        "source_version": "arXiv:2609.26996v1, Section 6.2, equations (38)-(40)",
        "source_url": SOURCE, "q": Q, "extension_relation": "w^2=2",
        "coefficient_order": "constant first", "infinity_points_each_field": 2,
        "comparison_polynomials_constant_first": COMPARISON,
        "curves": rows, "resultant_matrix_mod7": resultants,
        "all_displayed_entries_match": all_match,
        "all_resultants_nonzero": all(value != 0 for row in resultants for value in row),
        "global_coverage_verified": False,
    }
    destination = Path(__file__).with_name("results.json")
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(f"All displayed entries match: {all_match}; all resultants nonzero: "
          f"{report['all_resultants_nonzero']}; global coverage is not verified.")
    return 0 if all_match and report["all_resultants_nonzero"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
