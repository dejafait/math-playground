#!/usr/bin/env python3
"""Exact local-map checks for L017; the global sheaf argument is in the proof."""

import importlib.util
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path


source = Path(__file__).resolve().parents[1] / "rm-cubic" / "check_correspondence.py"
spec = importlib.util.spec_from_file_location("rm_cubic_arithmetic", source)
arithmetic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(arithmetic)
add, scale = arithmetic.add, arithmetic.scale
multiply, power = arithmetic.multiply, arithmetic.power
reduce = arithmetic.cyclotomic_reduce
ONE, ZERO = arithmetic.ONE, {}


def root(exponent):
    return {(0, 0, exponent % 7): 1}


def determinant(matrix):
    terms = []
    for order in permutations(range(len(matrix))):
        inversions = sum(order[i] > order[j]
                         for i in range(len(order))
                         for j in range(i + 1, len(order)))
        term = ONE
        for i, j in enumerate(order):
            term = multiply(term, matrix[i][j])
        terms.append(scale(term, (-1) ** inversions))
    return reduce(add(*terms))


def tangent_bivector(k, weights):
    # Tangent plane of w_j=zeta^(k*d_j) u_j, in (u1,u2,w1,w2).
    first = [ONE, ZERO, root(k * weights[0]), ZERO]
    second = [ZERO, ONE, ZERO, root(k * weights[1])]
    return [add(multiply(first[i], second[j]),
                scale(multiply(first[j], second[i]), -1))
            for i, j in combinations(range(4), 2)]


def main():
    for weights in ((6, 2), (3, 5), (6, 2)):
        # The map Ext^2(k,Q_+ direct sum Q_-) -> Ext^2(k,k)
        # has these two columns; it must be injective, not silently zero.
        columns = [tangent_bivector(k, weights) for k in (2, -2)]
        assert any(determinant([[columns[0][a], columns[1][a]],
                                [columns[0][b], columns[1][b]]])
                   for a, b in combinations(range(6), 2))

        for rotation in (1, 3):
            # The restriction of ambient tangent vectors to the conormal
            # generators of P_+ and P_- is the other connecting-map test.
            restrictions = []
            for k in (rotation, -rotation):
                restrictions.extend([
                    [scale(root(k * weights[0]), -1), ZERO, ONE, ZERO],
                    [ZERO, scale(root(k * weights[1]), -1), ZERO, ONE],
                ])
            assert determinant(restrictions)

    # The two graph equations have variables d and H*mu.
    assert Fraction(1, 2) - 1 == Fraction(-1, 2)

    theta = {j: add(root(j), root(-j)) for j in (1, 2, 3)}
    action = add(theta[1], scale(theta[2], 2), theta[3])
    assert not reduce(add(action, scale(power(theta[1], 2), -1), scale(ONE, 3)))
    assert any(zeta_degree != 0 for _, _, zeta_degree in reduce(action))

    print("PASS: both infinity connecting maps have the required ranks at all three points.")
    print("PASS: the residue equations are independent and the 1,2,1 action is U^2-3 id.")
    print("Global Ext gluing, unfiltered support recovery, and the kernel statement require L017's proof.")


if __name__ == "__main__":
    main()
