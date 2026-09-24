#!/usr/bin/env python3
"""Exact finite checks for L336; no asymptotic or return-height certificate."""

from fractions import Fraction as F
from itertools import product
from math import comb, prod


def multiply(left, right):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            result[i + j] = result.get(i + j, F(0)) + a * b
    return {degree: value for degree, value in result.items() if value}


def main():
    # Independently multiply the finite Fourier factor and check every
    # signed coefficient, its l1 norm, and the constant-term lower bound.
    factor = {-1: -F(1, 4), 0: F(1, 2), 1: -F(1, 4)}
    polynomial = {0: F(1)}
    coefficient_checks = 0
    for degree in range(1, 17):
        polynomial = multiply(polynomial, factor)
        for k in range(-degree, degree + 1):
            sign = -1 if k % 2 else 1
            expected = sign * F(comb(2 * degree, degree + k), 4 ** degree)
            assert polynomial[k] == expected
            coefficient_checks += 1
        assert sum(abs(value) for value in polynomial.values()) == 1
        assert polynomial[0] >= F(1, 2 * degree + 1)

    # Check the integer separation underlying |log(u/v)| >= P^(-M).
    # The logarithmic inequality itself is proved by integration in L336.
    primes = (2, 3, 5)
    prime_product = prod(primes)
    frequency_checks = 0
    for degree in range(1, 5):
        for exponents in product(range(-degree, degree + 1), repeat=3):
            if not any(exponents):
                continue
            numerator = prod(p ** max(k, 0) for p, k in zip(primes, exponents))
            denominator = prod(p ** max(-k, 0) for p, k in zip(primes, exponents))
            assert numerator != denominator
            assert max(numerator, denominator) <= prime_product ** degree
            assert F(abs(numerator - denominator), max(numerator, denominator)) >= F(1, prime_product ** degree)
            frequency_checks += 1

    # The Gaussian tail primitive has derivative minus its integrand:
    # d/dU [2(1+U^2+8r)e^(-U^2/(8r))]
    #   = -(1+U^2)U/(2r) e^(-U^2/(8r)).
    primitive_checks = 0
    for r in (F(1), F(7, 3), F(16), F(100)):
        for u in (F(0), F(1, 3), F(5), F(17)):
            derivative_factor = 4 * u - 2 * (1 + u * u + 8 * r) * u / (4 * r)
            assert derivative_factor == -(1 + u * u) * u / (2 * r)
            primitive_checks += 1

    assert F(22, 4096) < F(1, 128)
    assert F(3, 128) < F(1, 16)
    print(f"OK: {coefficient_checks} signed Fourier coefficients, "
          f"{frequency_checks} integer frequency separations, "
          f"{primitive_checks} Gaussian primitive checks, and 2 margin inequalities.")
    print("These finite checks do not certify analytic tails, asymptotics, "
          "actual first returns, or any Laguerre sign.")


if __name__ == "__main__":
    main()
