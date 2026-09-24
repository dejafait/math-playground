#!/usr/bin/env python3
"""Exact finite checks for L340; not an actual phase-return calculation."""

from fractions import Fraction as F
from itertools import product
from math import comb


def convolve(left, right):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            result[i + j] = result.get(i + j, F(0)) + a * b
    return result


def primes_through(limit):
    primes = []
    for candidate in range(2, limit + 1):
        if all(candidate % p for p in primes if p * p <= candidate):
            primes.append(candidate)
    return primes


def main():
    # Independent finite convolution of the absolute Fourier coefficients.
    factor = {-1: F(1, 4), 0: F(1, 2), 1: F(1, 4)}
    polynomial = {0: F(1)}
    coefficient_checks = 0
    for m in range(1, 25):
        polynomial = convolve(polynomial, factor)
        for k, value in polynomial.items():
            assert value == F(comb(2 * m, m + k), 4**m)
            coefficient_checks += 1
        assert sum(polynomial.values()) == 1
        assert sum(k * value for k, value in polynomial.items()) == 0
        assert sum(k * k * value for k, value in polynomial.items()) == F(m, 2)
        assert polynomial[0] ** 2 <= F(1, 3 * m + 1)

    # Expand all coefficients of the quadratic frequency polynomial.
    # This checks cross-term cancellation without numerical logarithms.
    moment_checks = 0
    for d in (2, 3):
        for m in range(1, 5):
            weights = {k: F(comb(2 * m, m + k), 4**m)
                       for k in range(-m, m + 1)}
            moments = {(i, j): F(0) for i in range(d) for j in range(d)}
            mass = F(0)
            for vector in product(weights, repeat=d):
                weight = F(1)
                for k in vector:
                    weight *= weights[k]
                mass += weight
                for i, j in moments:
                    moments[i, j] += weight * vector[i] * vector[j]
            assert mass == 1
            for (i, j), value in moments.items():
                assert value == (F(m, 2) if i == j else 0)
                moment_checks += 1

    # These are finite audits of the algebra used for the all-degree proof.
    degree_checks = 0
    for m in range(101):
        assert 4 * (m + 1) ** 2 * (3 * m + 1) - (2 * m + 1) ** 2 * (3 * m + 4) == m
        if m:
            for d in range(2, 9):
                assert (3 * m + 1) ** d >= m * 4**d
                assert 3 * (d - 1) * m - 1 > 0
                degree_checks += 1

    # Check exact central-binomial prime exponents and the integer bounds
    # from which the logarithmic prime-count estimate is proved.
    valuation_checks = 0
    prime_count_checks = 0
    for n in range(1, 129):
        central = comb(2 * n, n)
        reconstructed = 1
        primes = primes_through(2 * n)
        for p in primes:
            exponent = 0
            power = p
            while power <= 2 * n:
                digit = (2 * n) // power - 2 * (n // power)
                assert digit in (0, 1)
                exponent += digit
                power *= p
            assert p**exponent <= 2 * n
            reconstructed *= p**exponent
            valuation_checks += 1
        assert reconstructed == central
        assert 4**n <= (2 * n + 1) * central
        assert central <= (2 * n) ** len(primes)
        prime_count_checks += 1

    print(f"OK: {coefficient_checks} Fourier coefficients, "
          f"{moment_checks} quadratic frequency coefficients, "
          f"{degree_checks} degree comparisons, {valuation_checks} prime "
          f"valuations, and {prime_count_checks} central-binomial bounds.")
    print("These exact finite checks do not certify an actual Fourier "
          "discrepancy, phase return, arithmetic sign, or RH conclusion.")


if __name__ == "__main__":
    main()
