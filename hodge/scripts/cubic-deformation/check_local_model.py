#!/usr/bin/env python3
"""Exact supporting checks for L007; no global deformation claim is tested."""

from fractions import Fraction


def cyclotomic_reduce(terms):
    coefficients = [0] * 7
    for exponent, coefficient in terms:
        coefficients[exponent % 7] += coefficient
    return tuple(c - coefficients[6] for c in coefficients[:6])


def basis(degree):
    if degree == 0:
        return [(0, 0, 0, 0)]
    return [
        (i, degree - i, 0, 0) for i in range(degree + 1)
    ] + [(0, 0, i, degree - i) for i in range(degree + 1)]


def multiply_variable(monomial, variable):
    result = list(monomial)
    result[variable] += 1
    if any(result[:2]) and any(result[2:]):
        return None  # r_i s_j = 0 in the two-plane local ring
    return tuple(result)


def rank(matrix):
    rows = [[Fraction(entry) for entry in row] for row in matrix]
    pivot = 0
    for column in range(len(rows[0])):
        index = next((i for i in range(pivot, len(rows)) if rows[i][column]), None)
        if index is None:
            continue
        rows[pivot], rows[index] = rows[index], rows[pivot]
        lead = rows[pivot][column]
        rows[pivot] = [entry / lead for entry in rows[pivot]]
        for i in range(pivot + 1, len(rows)):
            if rows[i][column]:
                multiple = rows[i][column]
                rows[i] = [a - multiple * b for a, b in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def normal_image_dimension(degree):
    source, target = basis(degree), basis(degree + 1)
    target_index = {monomial: i for i, monomial in enumerate(target)}
    # e_ij denotes the ideal generator r_i s_j, ordered 11, 12, 21, 22.
    # Syzygies: r_2 e_1j - r_1 e_2j; s_2 e_i1 - s_1 e_i2.
    syzygies = [
        [(0, 1, 1), (2, 0, -1)],
        [(1, 1, 1), (3, 0, -1)],
        [(0, 3, 1), (1, 2, -1)],
        [(2, 3, 1), (3, 2, -1)],
    ]
    matrix = [[0] * (4 * len(source)) for _ in range(4 * len(target))]
    for equation, syzygy in enumerate(syzygies):
        for generator, variable, coefficient in syzygy:
            for j, monomial in enumerate(source):
                product = multiply_variable(monomial, variable)
                if product is not None:
                    row = equation * len(target) + target_index[product]
                    matrix[row][generator * len(source) + j] += coefficient
    return 4 * len(source) - rank(matrix)


def main():
    # (zeta^-1-zeta)(zeta^2-zeta^-2), exactly modulo Phi_7.
    determinant = cyclotomic_reduce([(1, 1), (4, -1), (3, -1), (6, 1)])
    assert determinant == (-1, 0, -1, -2, -2, -1)
    assert any(determinant)

    # The four distinct quadratic generators remain independent modulo m I.
    quadratics = {(1, 0, 1, 0), (1, 0, 0, 1), (0, 1, 1, 0), (0, 1, 0, 1)}
    assert len(quadratics) == 4 and all(sum(m) == 2 for m in quadratics)

    dimensions = [normal_image_dimension(d) for d in range(6)]
    assert dimensions == [0, 4, 8, 12, 16, 20]
    print("PASS: exact nonzero branch determinant; four minimal quadratics.")
    print("PASS: normal-module image degrees 0..5 have dimensions", dimensions)
    print("These support the local proof; the global RM obstruction is not computed.")


if __name__ == "__main__":
    main()
