#!/usr/bin/env python3
"""Exact Laurent-polynomial checks supporting L006; no geometric claims tested."""

from collections import defaultdict


def add(*polynomials):
    result = defaultdict(int)
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            result[monomial] += coefficient
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def scale(polynomial, coefficient):
    return {monomial: coefficient * value for monomial, value in polynomial.items() if coefficient * value}


def multiply(left, right):
    result = defaultdict(int)
    for (a, v, z), x in left.items():
        for (b, w, u), y in right.items():
            result[(a + b, v + w, (z + u) % 7)] += x * y
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


ONE = {(0, 0, 0): 1}


def power(polynomial, exponent):
    result = ONE
    for _ in range(exponent):
        result = multiply(result, polynomial)
    return result


def cyclotomic_reduce(polynomial):
    """Further reduce by Phi_7(z)=1+z+...+z^6, not just z^7=1."""
    result = defaultdict(int)
    for (a, v, z), coefficient in polynomial.items():
        if z == 6:
            for u in range(6):
                result[(a, v, u)] -= coefficient
        else:
            result[(a, v, z)] += coefficient
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def main():
    # Monomials are a^i v^j zeta^k, with integer coefficients.
    a = {(1, 0, 0): 1}
    t = {(0, 1, 0): 1, (1, -1, 0): 1}
    dickson = add(
        power(t, 7),
        scale(multiply(a, power(t, 5)), -7),
        scale(multiply(power(a, 2), power(t, 3)), 14),
        scale(multiply(power(a, 3), t), -7),
    )
    assert dickson == {(0, 7, 0): 1, (7, -7, 0): 1}

    theta = {(0, 0, 1): 1, (0, 0, 6): 1}
    alpha = {(0, 0, 0): 1, (1, -2, 0): -1}
    for j in (1, -1):
        # kappa_j(v)=a*zeta^(-2j)/v, including its differential.
        kappa_alpha = {(0, 0, (2 * j) % 7): 1, (1, -2, (-2 * j) % 7): -1}
        beta = {(0, 0, j % 7): 1, (1, -2, (-j) % 7): -1}
        assert cyclotomic_reduce(add(alpha, kappa_alpha, scale(multiply(theta, beta), -1))) == {}

    relation = add(power(theta, 3), power(theta, 2), scale(theta, -2), scale(ONE, -1))
    assert cyclotomic_reduce(relation) == {}
    # A monic cubic with constant term -1 can have only rational roots +/-1.
    assert all(r**3 + r**2 - 2*r - 1 != 0 for r in (-1, 1))
    assert 4**2 + 2 + 3 == 21
    assert 4**2 + 3 == 19
    print("PASS: Dickson identity; both graph trace identities; irreducible cubic relation; dimensions 19 < 21.")
    print("The unnormalized two-graph sum acts by 2*theta; its half acts by theta.")


if __name__ == "__main__":
    main()
