#!/usr/bin/env python3
"""Exact determinant and monomial checks supporting L042's local calculation."""

import importlib.util
from itertools import permutations
from pathlib import Path


source = Path(__file__).resolve().parents[1] / "rm-cubic" / "check_correspondence.py"
spec = importlib.util.spec_from_file_location("rm_cubic_arithmetic", source)
arithmetic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(arithmetic)
add, scale, multiply = arithmetic.add, arithmetic.scale, arithmetic.multiply
reduce = arithmetic.cyclotomic_reduce
ONE = arithmetic.ONE


def zeta(exponent):
    return {(0, 0, exponent % 7): 1}


def subtract(left, right):
    return add(left, scale(right, -1))


def product(*factors):
    result = ONE
    for factor in factors:
        result = multiply(result, factor)
    return reduce(result)


def determinant(weights, monomials):
    """Coefficient after factoring out the product of the row monomials."""
    rows = []
    for u_degree, v_degree in monomials:
        exponent = weights[0] * u_degree + weights[1] * v_degree
        rows.append((ONE, zeta(exponent), zeta(-exponent)))
    terms = []
    for perm in permutations(range(3)):
        inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
        terms.append(scale(product(*(rows[row][perm[row]] for row in range(3))), (-1) ** inversions))
    return reduce(add(*terms))


def divides(left, right):
    return all(a <= b for a, b in zip(left, right))


def main():
    for weights in ((6, 2), (3, 5), (6, 2)):
        r, s = weights
        mixed = determinant(weights, ((0, 0), (1, 0), (0, 1)))
        pure_u = determinant(weights, ((0, 0), (1, 0), (2, 0)))
        pure_v = determinant(weights, ((0, 0), (0, 1), (0, 2)))
        expected_mixed = product(
            subtract(zeta(r), ONE), subtract(zeta(s), ONE),
            subtract(zeta(s), zeta(r)), zeta(-r - s),
        )
        expected_u = product(
            subtract(zeta(r), ONE), subtract(zeta(-r), ONE),
            subtract(zeta(-r), zeta(r)),
        )
        expected_v = product(
            subtract(zeta(s), ONE), subtract(zeta(-s), ONE),
            subtract(zeta(-s), zeta(s)),
        )
        assert mixed == expected_mixed and mixed
        assert pure_u == expected_u and pure_u
        assert pure_v == expected_v and pure_v

    generators = {(1, 1), (3, 0), (0, 3)}
    square = {(a + c, b + d) for a, b in generators for c, d in generators}
    minimal = {exponent for exponent in square
               if not any(other != exponent and divides(other, exponent) for other in square)}
    assert minimal == {(2, 2), (4, 1), (1, 4), (6, 0), (0, 6)}
    assert (6, 0) in minimal and (0, 6) in minimal and (0, 0) not in minimal
    assert len(minimal) == 5
    print("PASS: uv, u^3 and v^3 determinant coefficients are nonzero for all three fixed points.")
    print("PASS: their square has exactly the five stated minimal monomial generators.")
    print("Regularity, the full-ideal equality and the no-lift implication require L042's proof.")


if __name__ == "__main__":
    main()
