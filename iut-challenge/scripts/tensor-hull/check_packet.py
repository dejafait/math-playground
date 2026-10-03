#!/usr/bin/env python3
"""Exact rational checks for the fixed Q_2(sqrt(2)) tensor packet.

The logarithm lattice and complete automorphism orbit require the proof in L007;
this checks its finite matrices and witness, without numerical log truncation.
"""

from fractions import Fraction as Q
import json
from pathlib import Path


def columns(vectors):
    return [list(row) for row in zip(*vectors)]


def matmul(left, right):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*right)] for row in left]


def matvec(matrix, vector):
    return [sum(x * y for x, y in zip(row, vector)) for row in matrix]


def inverse(matrix):
    n = len(matrix)
    rows = [[Q(x) for x in row] + [Q(i == j) for j in range(n)]
            for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        divisor = rows[j][j]
        rows[j] = [x / divisor for x in rows[j]]
        for i in range(n):
            if i != j:
                multiplier = rows[i][j]
                rows[i] = [x - multiplier * y
                           for x, y in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def field_mul(x, y):
    # (r + s*pi)(t + u*pi), pi^2 = 2.
    r, s = x
    t, u = y
    return [r * t + 2 * s * u, r * u + s * t]


def product_mul(x, y):
    return field_mul(x[:2], y[:2]) + field_mul(x[2:], y[2:])


def action(element):
    basis = [[Q(i == j) for i in range(4)] for j in range(4)]
    return columns([product_mul(element, vector) for vector in basis])


def v2(value):
    value = Q(value)
    if not value:
        return float("inf")
    result = 0
    num, den = abs(value.numerator), value.denominator
    while num % 2 == 0:
        num //= 2
        result += 1
    while den % 2 == 0:
        den //= 2
        result -= 1
    return result


def field_valuation(vector):
    return min(v2(vector[0]), v2(vector[1]) + Q(1, 2))


def minimum_entry_valuation(matrix):
    return min(v2(value) for row in matrix for value in row)


def integral(matrix):
    return minimum_entry_valuation(matrix) >= 0


def printable(matrix):
    return [[str(value) for value in row] for row in matrix]


def main():
    tensor_order = columns([
        [Q(1), Q(0), Q(1), Q(0)],
        [Q(0), Q(1), Q(0), Q(1)],
        [Q(0), Q(1), Q(0), Q(-1)],
        [Q(2), Q(0), Q(-2), Q(0)],
    ])
    shell = columns([
        [Q(1), Q(0), Q(1), Q(0)],
        [Q(0), Q(1, 4), Q(0), Q(1, 4)],
        [Q(0), Q(1, 4), Q(0), Q(-1, 4)],
        [Q(1, 8), Q(0), Q(-1, 8), Q(0)],
    ])
    shell_inverse = inverse(shell)
    order_inverse = inverse(tensor_order)
    a = [Q(0), Q(1), Q(0), Q(-1)]
    beta_last = [Q(0), Q(2), Q(0), Q(-2)]
    beta_first = [Q(0), Q(2), Q(0), Q(2)]
    gamma_last = [Q(1, 2), Q(0), Q(1, 2), Q(0)]
    gamma_first = [Q(1, 2), Q(0), Q(-1, 2), Q(0)]

    assert product_mul(beta_last, gamma_last) == a
    assert product_mul(beta_first, gamma_first) == a
    for beta in (beta_last, beta_first):
        assert field_valuation(beta[:2]) == Q(3, 2)
        assert field_valuation(beta[2:]) == Q(3, 2)
        # beta O_L is inside T, with O_L's canonical basis as the input.
        assert integral(matmul(order_inverse, action(beta)))
    assert integral(matmul(shell_inverse, tensor_order))
    for beta in (beta_last, beta_first):
        # The log tensor is J = 16 I; this verifies beta J inside I,
        # the second branch of (6.4) -> (6.5).
        log_tensor = [[16 * value for value in row] for row in shell]
        assert integral(matmul(shell_inverse,
                               matmul(action(beta), log_tensor)))

    last_matrix = matmul(shell_inverse, matmul(action(gamma_last), shell))
    first_matrix = matmul(shell_inverse, matmul(action(gamma_first), shell))
    expected_first = [
        [Q(0), Q(0), Q(0), Q(1, 16)],
        [Q(0), Q(0), Q(1, 2), Q(0)],
        [Q(0), Q(1, 2), Q(0), Q(0)],
        [Q(4), Q(0), Q(0), Q(0)],
    ]
    assert first_matrix == expected_first
    assert last_matrix == [[Q(i == j, 2) for j in range(4)]
                           for i in range(4)]
    assert minimum_entry_valuation(first_matrix) == -4
    assert minimum_entry_valuation(last_matrix) == -1
    swap = columns([
        [Q(0), Q(0), Q(0), Q(1)],
        [Q(0), Q(1), Q(0), Q(0)],
        [Q(0), Q(0), Q(1), Q(0)],
        [Q(1), Q(0), Q(0), Q(0)],
    ])
    witness_coefficients = matvec(swap, matvec(
        first_matrix, [Q(0), Q(0), Q(0), Q(1)]))
    witness = matvec(shell, witness_coefficients)
    assert witness == [Q(1, 128), Q(0), Q(-1, 128), Q(0)]
    assert field_valuation(witness[:2]) == -7
    assert field_valuation(witness[2:]) == -7
    component_minima = [min(field_valuation(vector[offset:offset + 2])
                            for vector in zip(*shell))
                       for offset in (0, 2)]
    assert component_minima == [-3, -3]
    report = {
        "arithmetic": "exact fractions; no logarithm truncation",
        "beta_component_valuations": ["3/2", "3/2"],
        "both_beta_maximal_order_inclusions": True,
        "both_6_4_to_6_5_inclusions": True,
        "shell_component_minimum_valuations": component_minima,
        "last_factor_gamma_matrix": printable(last_matrix),
        "first_factor_gamma_matrix": printable(first_matrix),
        "orbit_exponents_from_L007_proof": {"last_factor": -1,
                                            "first_factor": -4},
        "rounded_hull_radii": [16, 16],
        "first_factor_orbit_hull_radii": [128, 128],
        "basis_swap_witness": [str(value) for value in witness],
        "logarithm_lattice_and_orbit_completeness": "proved in L007",
    }
    destination = Path(__file__).with_name("result.json")
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
