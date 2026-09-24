#!/usr/bin/env python3
"""Exact finite algebra checks for L335; no infinite/asymptotic certification."""

from fractions import Fraction as F
from math import comb, isqrt


def add(left, right):
    result = dict(left)
    for degree, value in right.items():
        result[degree] = result.get(degree, F(0)) + value
    return {degree: value for degree, value in result.items() if value}


def multiply(left, right):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            result[i + j] = result.get(i + j, F(0)) + a * b
    return {degree: value for degree, value in result.items() if value}


def scale(polynomial, factor):
    return {degree: factor * value for degree, value in polynomial.items()
            if factor * value}


def liouville(number):
    sign, divisor = 1, 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            number //= divisor
            sign = -sign
        divisor += 1
    return -sign if number > 1 else sign


def main():
    # Formal u=1/r; inversion sends z^k to 2^(-k) prod(1-j*u).
    expected = [{0: F(1)}, {}, {1: -F(1, 4)},
                {2: F(1, 4)}, {2: F(3, 16), 3: -F(3, 8)}]
    raw = []
    for k in range(5):
        polynomial = {0: F(1, 2 ** k)}
        for j in range(k):
            polynomial = multiply(polynomial, {0: F(1), 1: -F(j)})
        raw.append(polynomial)
        centered = {}
        for j in range(k + 1):
            centered = add(centered, scale(raw[j], comb(k, j) * (-F(1, 2)) ** (k-j)))
        assert centered == expected[k], (k, centered)

    # Independent divisor grouping of both Dirichlet products.
    count = 1024
    signs = [0] + [liouville(n) for n in range(1, count + 1)]
    for n in range(1, count + 1):
        divisors = [d for d in range(1, n + 1) if n % d == 0]
        assert sum(signs[d] for d in divisors) == int(isqrt(n) ** 2 == n)
        assert sum(signs[d] * signs[n // d] for d in divisors) == len(divisors) * signs[n]

    # Constant term of each finite phase-localizing polynomial.
    factor = {-1: -F(1, 4), 0: F(1, 2), 1: -F(1, 4)}
    polynomial = {0: F(1)}
    for m in range(1, 17):
        polynomial = multiply(polynomial, factor)
        constant = polynomial.get(0, F(0))
        assert constant == F(comb(2 * m, m), 4 ** m)
        assert constant >= F(1, 2 * m + 1)

    print("OK: 5 exact centered Mellin moments, 2048 divisor identities, "
          "and 16 phase-polynomial constant terms.")
    print("These finite checks do not certify analytic tails, asymptotics, "
          "phase-return heights, or any Laguerre sign.")


if __name__ == "__main__":
    main()
