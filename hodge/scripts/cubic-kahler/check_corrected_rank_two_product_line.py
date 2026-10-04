#!/usr/bin/env python3
"""Exact cup-product check of L049's product-line indices.

The forced fourth character includes the full mixed square from L048.
Only the divisor projection is needed in the remaining products:
the transcendental tensor pairs trivially with every line class.
The geometric inputs are not re-proved, and no bundle is certified.
"""

from fractions import Fraction as Q

from check_eigenvector_certificate import (
    linear_combination, matrix, multiply, transpose,
)
from check_rank_two_third_chern import (
    GRAM, ZERO, apply, inverse, pairing,
)


# Surface basis: unit=0, four divisor classes=1,...,4, point class=5.
def surface_product(i, j):
    if i == 0:
        return j, Q(1)
    if j == 0:
        return i, Q(1)
    if 1 <= i <= 4 and 1 <= j <= 4:
        return 5, GRAM[i - 1][j - 1]
    return 5, Q(0)


def cup(left, right):
    result = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            first, c = surface_product(i, k)
            second, d = surface_product(j, ell)
            key = first, second
            result[key] = result.get(key, Q(0)) + a * b * c * d
    return {key: value for key, value in result.items() if value}


def product_line_character(x, y):
    # The exponential on a surface terminates after its square term.
    first = {0: Q(1), 5: pairing(x, x) / 2}
    second = {0: Q(1), 5: pairing(y, y) / 2}
    first.update({i + 1: value for i, value in enumerate(x)})
    second.update({i + 1: value for i, value in enumerate(y)})
    return {(i, j): a * b for i, a in first.items()
            for j, b in second.items() if a * b}


def formal_character(p, t, mixed):
    result = {(0, 0): Q(2), (5, 0): Q(p), (0, 5): Q(t),
              (5, 5): Q(p * t + 78, 6)}
    result.update({(i + 1, j + 1): mixed[i][j]
                   for i in range(4) for j in range(4) if mixed[i][j]})
    return result


def main():
    chamber = matrix([[1, 1, -2, 2], [0, 1, 0, 0],
                      [0, -1, 1, -1], [0, 0, 0, 1]])
    b0 = matrix([[0, -2, 2, 0], [-2, 1, 1, 0],
                 [2, 1, 4, 0], [0, 0, 0, 0]])
    final_b = multiply(multiply(chamber, b0), transpose(chamber))
    mixed = linear_combination((4, inverse(GRAM)), (1, final_b))
    d_n = multiply(mixed, GRAM)
    bilinear = multiply(GRAM, d_n)
    assert multiply(transpose(d_n), GRAM) == bilinear
    assert bilinear == linear_combination(
        (4, GRAM), (1, multiply(multiply(GRAM, final_b), GRAM)))
    assert all(entry.denominator == 1 for row in bilinear for entry in row)
    assert all(GRAM[i][i] % 2 == 0 for i in range(4))

    basis = [tuple(Q(i == j) for i in range(4)) for j in range(4)]
    vectors = [ZERO, *basis,
               tuple(map(Q, [-4, -2, 1, 2])),
               tuple(map(Q, [2, -1, 3, 1])),
               tuple(map(Q, [-1, 2, 0, 3]))]
    todd = {(0, 0): Q(1), (5, 0): Q(2), (0, 5): Q(2),
            (5, 5): Q(4)}
    checked = 0
    passing_residues = 0
    for p in range(6):
        for t in range(6):
            character_todd = cup(formal_character(p, t, mixed), todd)
            untwisted = character_todd[(5, 5)]
            assert untwisted == 8 + 2 * (p + t) + Q(p * t + 78, 6)
            passing_residues += int(p * t % 6 == 0)
            for x in vectors:
                for y in vectors:
                    m, n = pairing(x, x) / 2, pairing(y, y) / 2
                    k = pairing(apply(d_n, x), y)
                    assert all(value.denominator == 1 for value in (m, n, k))
                    expanded = cup(character_todd, product_line_character(x, y))
                    index = expanded.get((5, 5), Q(0))
                    assert index == (2 * (m + 2) * (n + 2)
                                     + p * (n + 2) + t * (m + 2)
                                     + k + Q(p * t + 78, 6))
                    shift = (t + 4) * m + (p + 4) * n + 2 * m * n + k
                    assert index - untwisted == shift
                    assert shift.denominator == 1
                    assert (index.denominator == 1) == (p * t % 6 == 0)
                    checked += 1
    assert (passing_residues, checked) == (15, 2304)

    # Actual Bogomolov-region examples, rather than just residue representatives.
    x, y = basis[0], basis[1]  # fibre and zero-section divisors
    assert (pairing(x, x) / 2, pairing(y, y) / 2,
            pairing(apply(d_n, x), y)) == (0, -1, -1)
    for a, b, expected in [(-13, 0, Q(9)), (-10, -10, Q(4)),
                            (-7, -7, Q(17, 2))]:
        p, t = a + 4, b + 4
        index = cup(cup(formal_character(p, t, mixed), todd),
                    product_line_character(x, y))[(5, 5)]
        assert index == expected
        assert (index.denominator == 1) == (p * t % 6 == 0)

    print("PASS: fixed mixed divisor pairing is integral on the full rank-four lattice.")
    print("PASS: independent truncated cup products match the product-line HRR formula.")
    print(f"PASS: {checked} indices checked across all 36 residue pairs and 64 twist pairs.")
    print("PASS: all shifts are integral; exactly the same 15 residue pairs survive.")
    print("PASS: fibre/section twists give 9, 4, 17/2 for the three stated examples.")
    print("Product-line indices add no restriction; no finite-rank bundle is certified.")


if __name__ == "__main__":
    main()
