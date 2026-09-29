#!/usr/bin/env python3
"""Finite arithmetic check for L028; the integral Chern argument is in the proof."""

from itertools import permutations


GRAM = [
    [0, 1, 0, 1],
    [1, -2, 0, 0],
    [0, 0, -2, 1],
    [1, 0, 1, -2],
]


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def multiply(left, right):
    return [[sum(a * b for a, b in zip(row, column)) % 2
             for column in zip(*right)] for row in left]


def identity(size):
    return [[int(i == j) for j in range(size)] for i in range(size)]


def inverse_mod_two(matrix):
    size = len(matrix)
    rows = [[entry % 2 for entry in row] + identity(size)[i]
            for i, row in enumerate(matrix)]
    for column in range(size):
        pivot = next(i for i in range(column, size) if rows[i][column])
        rows[column], rows[pivot] = rows[pivot], rows[column]
        for i in range(size):
            if i != column and rows[i][column]:
                rows[i] = [a ^ b for a, b in zip(rows[i], rows[column])]
    assert [row[:size] for row in rows] == identity(size)
    return [row[size:] for row in rows]


def polynomial_product(left, right):
    """Bit i stores the coefficient of z^i over F_2."""
    result = 0
    while right:
        if right & 1:
            result ^= left
        left <<= 1
        right >>= 1
    return result


def characteristic_polynomial(matrix):
    size = len(matrix)
    determinant = 0
    for permutation in permutations(range(size)):
        term = 1
        for i, j in enumerate(permutation):
            term = polynomial_product(term, matrix[i][j] ^ (2 if i == j else 0))
        determinant ^= term  # Signs coincide in characteristic two.
    return determinant


def integer_determinant(matrix):
    result = 0
    for permutation in permutations(range(len(matrix))):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(len(matrix))
                         for j in range(i + 1, len(matrix)))
        term = (-1) ** inversions
        for i, j in enumerate(permutation):
            term *= matrix[i][j]
        result += term
    return result


def main():
    assert integer_determinant(GRAM) == -7
    gram = [[entry % 2 for entry in row] for row in GRAM]
    assert gram == transpose(gram)
    assert all(gram[i][i] == 0 for i in range(4))
    gram_inverse = inverse_mod_two(gram)
    assert multiply(gram, gram_inverse) == identity(4)

    # The cubic z^3+z^2+1 has neither possible root, hence is irreducible.
    cubic = 0b1101
    assert (cubic & 1) == 1
    assert cubic.bit_count() % 2 == 1
    forbidden = {polynomial_product(cubic, 0b10 | beta) for beta in (0, 1)}
    assert forbidden == {0b11010, 0b10111}

    # G B is symmetric exactly when B is self-adjoint. Enumerating all
    # symmetric 4 x 4 matrices therefore exhausts the 2^10 possible B.
    positions = [(i, j) for i in range(4) for j in range(i, 4)]
    attained = set()
    for mask in range(1 << len(positions)):
        symmetric = [[0] * 4 for _ in range(4)]
        for bit, (i, j) in enumerate(positions):
            symmetric[i][j] = symmetric[j][i] = (mask >> bit) & 1
        operator = multiply(gram_inverse, symmetric)
        assert multiply(transpose(operator), gram) == multiply(gram, operator)
        polynomial = characteristic_polynomial(operator)
        attained.add(polynomial)
        assert polynomial & 0b01010 == 0  # No odd-degree terms.
        assert polynomial not in forbidden

    assert attained == {0b10000, 0b10001, 0b10100, 0b10101}
    print("PASS: determinant -7 and nondegenerate alternating divisor pairing modulo 2.")
    print("PASS: irreducible cubic; both possible linear-factor products excluded.")
    print("PASS: all 1024 self-adjoint operators have square characteristic polynomials.")
    print("Integral Chern classes, divisor preservation and the forced spectrum use L028's proof.")


if __name__ == "__main__":
    main()
