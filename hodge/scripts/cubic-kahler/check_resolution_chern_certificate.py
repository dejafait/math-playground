#!/usr/bin/env python3
"""Exact algebra for L026; the geometric and SU(2) arguments are in its proof."""

from fractions import Fraction as Q
from itertools import permutations


SYMBOLS = ("r", "d", "c", "t", "z", "b") + tuple(
    f"{letter}{i}" for letter in ("u", "v") for i in range(4)
)
ZERO_EXPONENTS = (0,) * len(SYMBOLS)


def constant(value):
    return {ZERO_EXPONENTS: Q(value)} if value else {}


def variable(name, exponent=1):
    powers = list(ZERO_EXPONENTS)
    powers[SYMBOLS.index(name)] = exponent
    return {tuple(powers): Q(1)}


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for powers, coefficient in polynomial.items():
            result[powers] = result.get(powers, Q(0)) + coefficient
    return {powers: coefficient for powers, coefficient in result.items() if coefficient}


def scale(coefficient, polynomial):
    return {powers: Q(coefficient) * value for powers, value in polynomial.items()
            if coefficient * value}


def multiply(left, right):
    result = {}
    for a, x in left.items():
        for b, y in right.items():
            powers = tuple(i + j for i, j in zip(a, b))
            result[powers] = result.get(powers, Q(0)) + x * y
    return {powers: coefficient for powers, coefficient in result.items() if coefficient}


def power(polynomial, exponent):
    result = constant(1)
    for _ in range(exponent):
        result = multiply(result, polynomial)
    return result


def main():
    # Chern classes commute here; Laurent powers allow the formal inverse of rank.
    r, d, c, t, z, b = (variable(name) for name in SYMBOLS[:6])
    inverse_rank = variable("r", -1)
    twisted_c1 = add(d, multiply(r, t))
    twisted_ch2 = add(c, multiply(d, t), scale(Q(1, 2), multiply(r, power(t, 2))))
    normalized = add(c, scale(Q(-1, 2), multiply(inverse_rank, power(d, 2))))
    twisted_normalized = add(
        twisted_ch2, scale(Q(-1, 2), multiply(inverse_rank, power(twisted_c1, 2)))
    )
    assert twisted_normalized == normalized

    # The universal rank-one matrix, with independent entries u_i and v_j.
    # L026 specializes u=ell and v=q(ell,-); no sample polarization is used.
    u = [variable(f"u{i}") for i in range(4)]
    v = [variable(f"v{i}") for i in range(4)]
    z_minus_two = add(z, constant(-2))
    matrix = [[add(z_minus_two if i == j else {},
                   scale(-1, multiply(b, multiply(u[i], v[j]))))
               for j in range(4)] for i in range(4)]
    determinant = {}
    for permutation in permutations(range(4)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(4) for j in range(i + 1, 4))
        term = constant((-1) ** inversions)
        for i, j in enumerate(permutation):
            term = multiply(term, matrix[i][j])
        determinant = add(determinant, term)
    pairing = add(*(multiply(u[i], v[i]) for i in range(4)))
    expected = multiply(power(z_minus_two, 3),
                        add(z_minus_two, scale(-1, multiply(b, pairing))))
    assert determinant == expected

    # Successive kernels in the formal basis (P_0,P_1,P_2,I_C).
    kernel = (0, 0, 0, 1)
    for i in range(3):
        kernel = tuple(int(i == j) - kernel[j] for j in range(4))
    assert kernel == (1, -1, 1, -1)
    assert all(x**3 + x**2 - 2*x - 1 != 0 for x in (-1, 1))
    print("PASS: universal line-twist cancellation and rank-one characteristic polynomial.")
    print("PASS: three-presentation K-class signs and cubic rational-root test.")
    print("The divisor action and common-metric eigenvalue condition use L026's proof.")


if __name__ == "__main__":
    main()
