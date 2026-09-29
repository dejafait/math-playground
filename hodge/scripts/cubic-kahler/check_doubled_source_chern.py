#!/usr/bin/env python3
"""Exact checks for L029; no maps, bundle existence or stability are tested."""

from collections import Counter
from fractions import Fraction as Q
from itertools import permutations

from check_eigenvector_certificate import (
    identity, linear_combination, matrix, multiply, transpose,
)


def polynomial_product(left, right):
    result = [Q(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def characteristic_polynomial(operator):
    size = len(operator)
    result = [Q(0)] * (size + 1)
    for permutation in permutations(range(size)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(size) for j in range(i + 1, size))
        term = [Q((-1) ** inversions)]
        for i, j in enumerate(permutation):
            term = polynomial_product(term, [-operator[i][j], Q(i == j)])
        result = [a + b for a, b in zip(result, term)]
    return result


def main():
    gram = matrix([[0, 1, 0, 1], [1, -2, 0, 0],
                   [0, 0, -2, 1], [1, 0, 1, -2]])
    a0 = matrix([[1, 2, -2, 5], [Q(1, 2), 0, -1, Q(3, 2)],
                 [Q(1, 2), 0, -2, 2], [0, 0, 0, 0]])
    pi_k = matrix([[0, 0, 0, -2], [0, 0, 0, -1],
                   [0, 0, 0, Q(1, 2)], [0, 0, 0, 1]])
    pi_w = linear_combination((1, identity(4)), (-1, pi_k))
    tensor = matrix([[0, -2, 2, 0], [-2, 1, 1, 0],
                     [2, 1, 4, 0], [0, 0, 0, 0]])
    assert multiply(pi_k, pi_k) == pi_k
    assert multiply(transpose(pi_k), gram) == multiply(gram, pi_k)
    assert multiply(tensor, gram) == multiply(
        linear_combination((2, a0), (-4, identity(4))), pi_w)
    operator = linear_combination((4, identity(4)), (1, multiply(tensor, gram)))
    assert operator == linear_combination((2, a0), (4, pi_k))
    assert operator == matrix([[2, 4, -4, 2], [1, 0, -2, -1],
                               [1, 0, -4, 6], [0, 0, 0, 4]])
    assert all(entry.denominator == 1 for row in operator for entry in row)
    assert multiply(transpose(operator), gram) == multiply(gram, operator)
    doubled_cubic = [-8, -8, 2, 1]
    assert characteristic_polynomial(operator) == polynomial_product(doubled_cubic, [-4, 1])
    reduced = [[int(entry) % 2 for entry in row] for row in operator]
    assert reduced == [[0, 0, 0, 0], [1, 0, 0, 1],
                       [1, 0, 0, 0], [0, 0, 0, 0]]
    assert all(int(entry) % 2 == 0 for row in multiply(reduced, reduced) for entry in row)
    assert [int(x) % 2 for x in characteristic_polynomial(operator)] == [0, 0, 0, 0, 1]
    assert [int(x) % 2 for x in polynomial_product(doubled_cubic, [-1, 1])] == [0, 0, 0, 1, 1]

    # Aggregate all signed actual product-line classes in (8). The source
    # -2[I_C] has rank -2, c_1=0, and contributes +2[C] to ch_2.
    rank = 4  # Only an example of the formal rank, not a rank-four bundle.
    zero = (0, 0, 0, 0)
    basis = [tuple(int(i == j) for i in range(4)) for j in range(3)]
    lines = Counter({(zero, zero): rank + 2})
    for i, x in enumerate(basis):
        for j, y in enumerate(basis):
            coefficient = int(tensor[i][j])
            for pair, sign in [((x, y), 1), ((x, zero), -1),
                               ((zero, y), -1), ((zero, zero), 1)]:
                lines[pair] += coefficient * sign
    assert sum(lines.values()) - 2 == rank
    assert all(sum(coefficient * x[i] for (x, _), coefficient in lines.items()) == 0
               for i in range(4))
    assert all(sum(coefficient * y[i] for (_, y), coefficient in lines.items()) == 0
               for i in range(4))
    moments = [[sum(coefficient * x[i] * y[j] for (x, y), coefficient in lines.items())
                for j in range(4)] for i in range(4)]
    assert moments == tensor
    for factor in (0, 1):
        pure = Q(0)
        for pair, coefficient in lines.items():
            vector = pair[factor]
            square = sum(vector[i] * gram[i][j] * vector[j]
                         for i in range(4) for j in range(4))
            pure += coefficient * square / 2
        assert pure == 0

    print("PASS: integral doubled correction tensor and self-adjoint pre-chamber operator.")
    print("PASS: doubled cubic, even gamma example, and square-zero reduction modulo 2.")
    print("PASS: signed product-line class has the stated rank, zero first moments and mixed tensor.")
    print("No final-chamber integrality, exact presentation or stable bundle is certified.")


if __name__ == "__main__":
    main()
