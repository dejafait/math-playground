#!/usr/bin/env python3
"""Exact finite checks of L352's fourth-moment grouping and sample counts.

Formal prime-log vectors and integer toy samples are used. These checks
do not estimate the actual a_n, infinite tails, or the fourth moment there.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd

from check_endpoint_gram_collisions import exponent_vector, squared_modulus


def fourth_correlation(frequency, samples):
    empirical = defaultdict(F)
    for sample in samples:
        empirical[tuple(sample * x for x in frequency)] += F(1, len(samples))
    return squared_modulus(squared_modulus(empirical))


def main():
    cases = 0
    for cutoff in (2, 3, 5):
        primes = [p for p in (2, 3, 5) if p <= cutoff]
        vectors = {n: exponent_vector(n, primes)
                   for n in range(1, cutoff + 1)}
        weights = {(p, q): F((3 * p + 5 * q) % 11 + 1, 7)
                   for p in vectors for q in vectors
                   if p != q and gcd(p, q) == 1}
        frequencies = {pair: tuple(y - x for x, y in
                                  zip(vectors[pair[0]], vectors[pair[1]]))
                       for pair in weights}
        total = sum(weights.values())
        diagonal = sum(w * w for w in weights.values())
        collisions = defaultdict(F)
        for (p, q), w in weights.items():
            for (u, v), other in weights.items():
                collisions[q * u, p * v] += w * other

        for samples in ((0, 1), (0, 1, 4), (-1, 2, 2, 5)):
            direct = defaultdict(F)
            for pair, w in weights.items():
                for other, v in weights.items():
                    difference = tuple(x - y for x, y in
                                       zip(frequencies[pair], frequencies[other]))
                    for key, coefficient in fourth_correlation(difference, samples).items():
                        direct[key] += w * v * coefficient / total ** 2

            grouped = defaultdict(F)
            for (k, l), coefficient in collisions.items():
                difference = tuple(x - y for x, y in
                                   zip(exponent_vector(k, primes),
                                       exponent_vector(l, primes)))
                for key, value in fourth_correlation(difference, samples).items():
                    grouped[key] += coefficient * value / total ** 2
            assert direct == grouped

            # Independent expansion in four sample indices.
            sample_expansion = defaultdict(F)
            matching_tuples = 0
            for a, b, c, d in product(samples, repeat=4):
                delta = a + b - c - d
                matching_tuples += delta == 0
                entry = defaultdict(F)
                for pair, w in weights.items():
                    entry[tuple(delta * x for x in frequencies[pair])] += w
                for key, value in squared_modulus(entry).items():
                    sample_expansion[key] += value / (len(samples) ** 4 * total ** 2)
            assert direct == sample_expansion
            energy_fraction = F(matching_tuples, len(samples) ** 4)
            expected = energy_fraction + (1 - energy_fraction) * diagonal / total ** 2
            assert direct[(0,) * len(primes)] == expected
            assert sum(direct.values()) == 1
            cases += 1

    subset_cases = 0
    superincreasing = tuple(5 ** j for j in range(1, 7))
    for size in range(1, len(superincreasing) + 1):
        for samples in combinations(superincreasing, size):
            energy = sum(abs(a + b - c - d) <= 1
                         for a, b, c, d in product(samples, repeat=4))
            assert energy == 2 * size ** 2 - size
            subset_cases += 1
    print(f"OK: {cases} exact fourth-moment collision, sample-expansion, and constant-term checks.")
    print(f"OK: tolerance-one energy count on {subset_cases} superincreasing toy subsets.")
    print("Finite algebra only; actual samples, infinite bounds, and sampled signs are not tested.")


if __name__ == "__main__":
    main()
