#!/usr/bin/env python3
"""Exact finite checks of L351's collisions and two Gram expansions.

Frequencies are formal prime-log vectors and sample locations are integers.
This does not test actual a_n, infinite estimates, or any sampled sign.
"""

from collections import defaultdict
from fractions import Fraction as F
from math import gcd


def exponent_vector(value, primes):
    result = []
    for prime in primes:
        count = 0
        while value % prime == 0:
            value //= prime
            count += 1
        result.append(count)
    assert value == 1
    return tuple(result)


def squared_modulus(poly):
    result = defaultdict(F)
    for left, a in poly.items():
        for right, b in poly.items():
            difference = tuple(x - y for x, y in zip(left, right))
            result[difference] += a * b
    return dict(result)


def main():
    cases = 0
    repeated_cases = 0
    for cutoff in range(2, 8):
        primes = [p for p in (2, 3, 5, 7) if p <= cutoff]
        zero = (0,) * len(primes)
        vectors = {n: exponent_vector(n, primes)
                   for n in range(1, cutoff + 1)}
        for samples in ((0, 1), (-2, 0, 3), (0, 1, 4, 9), (0, 2, 2, 5)):
            weights = {(p, q): F((3 * p + 5 * q + len(samples)) % 11, 7)
                       for p in vectors for q in vectors
                       if p != q and gcd(p, q) == 1}
            weights = {pair: w for pair, w in weights.items() if w}
            frequencies = {
                pair: tuple(y - x for x, y in zip(vectors[pair[0]],
                                                  vectors[pair[1]]))
                for pair in weights
            }
            total = sum(weights.values())
            diagonal = sum(w * w for w in weights.values())
            size = len(samples)
            normalization = size ** 2 * total ** 2

            # Group raw products first, without reducing k/l.
            collisions = defaultdict(F)
            for (p, q), w in weights.items():
                for (u, v), other in weights.items():
                    collisions[q * u, p * v] += w * other
            assert sum(c for (k, l), c in collisions.items() if k == l) == diagonal
            assert sum(collisions.values()) == total ** 2

            # Sample-side squared Gram entries as formal Fourier polynomials.
            gram = defaultdict(F)
            for left in samples:
                for right in samples:
                    entry = defaultdict(F)
                    for pair, w in weights.items():
                        key = tuple((left - right) * x for x in frequencies[pair])
                        entry[key] += w
                    for key, value in squared_modulus(entry).items():
                        gram[key] += value / normalization

            # Frequency-side squared empirical correlations, independently.
            correlations = defaultdict(F)
            for pair, w in weights.items():
                for other, v in weights.items():
                    difference = tuple(x - y for x, y in
                                       zip(frequencies[pair], frequencies[other]))
                    empirical = defaultdict(F)
                    for sample in samples:
                        empirical[tuple(sample * x for x in difference)] += F(1, size)
                    for key, value in squared_modulus(empirical).items():
                        correlations[key] += w * v * value / total ** 2
            assert gram == correlations
            assert sum(gram.values()) == 1  # All phases zero: H(0)=1.

            equal_samples = sum(left == right for left in samples for right in samples)
            expected = (F(equal_samples, size ** 2)
                        + F(size ** 2 - equal_samples, size ** 2) * diagonal / total ** 2)
            assert gram[zero] == expected
            repeated_cases += int(equal_samples != size)
            cases += 1

    print(f"OK: {cases} exact collision, Gram/correlation, and constant-term checks; "
          f"{repeated_cases} include repeated samples to check the diagonal count.")
    print("Finite algebra only; no infinite bounds, actual-height estimates, or signs tested.")


if __name__ == "__main__":
    main()
