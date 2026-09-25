#!/usr/bin/env python3
"""Bounded exact-arithmetic checks of L001; no integer-solution search."""

import json
from itertools import combinations, product
from math import gcd


def valuation(n, p):
    exponent = 0
    while n % p == 0:
        n //= p
        exponent += 1
    return exponent


def check_finite_representatives():
    moduli = (1, 2, 3, 4, 8, 9, 16, 25, 27, 49, 64, 81, 125, 128, 243, 1009, 30030)
    signatures = ((3, 3, 3), (3, 4, 5), (4, 4, 4), (4, 7, 9), (11, 13, 17))
    count = 0
    for modulus, height, signature in product(moduli, (1, 10**6), signatures):
        t = modulus * (height + 1)
        a, b, c = t, t + 1, t * (t + 1) + 1
        assert min(a, b, c) > height
        assert all(gcd(u, v) == 1 for u, v in combinations((a, b, c), 2))
        x, y, z = signature
        assert (pow(a, x, modulus) + pow(b, y, modulus) - pow(c, z, modulus)) % modulus == 0
        count += 1
    return count


def check_lifts():
    primes = (2, 3, 5, 7, 11)
    left_exponents = (3, 4, 5, 8, 9)
    right_exponents = (3, 4, 5, 6, 7, 8, 9, 11, 12, 16, 25, 27, 49)
    precision = 20
    cases = ramified_cases = corrections = 0
    for p, x, y, z in product(primes, left_exponents, left_exponents, right_exponents):
        s = valuation(z, p)
        a = p ** (2 * s + 1)
        b = 1 + a
        u = a**x + b**y
        c, k = 1, s + 1
        assert (u - 1) % (p ** (2 * s + 1)) == 0
        while k + s < precision:
            modulus = p ** (k + s)
            next_modulus = modulus * p
            assert (pow(c, z, modulus) - u) % modulus == 0
            error = ((pow(c, z, next_modulus) - u) // modulus) % p
            slope = ((z // (p**s)) * pow(c, z - 1, p)) % p
            assert slope != 0
            digit = (-error * pow(slope, -1, p)) % p
            lifted = c + digit * p**k
            assert (lifted - c) % (p**k) == 0
            assert (lifted - 1) % (p ** (s + 1)) == 0
            assert pow(lifted, z, next_modulus) == u % next_modulus
            c, k = lifted, k + 1
            corrections += 1
        assert pow(c, z, p**precision) == u % (p**precision)
        assert a % p == 0 and b % p != 0 and c % p != 0
        cases += 1
        ramified_cases += s > 0
    return {
        "prime_list": list(primes),
        "left_exponents": list(left_exponents),
        "right_exponents": list(right_exponents),
        "precision_power": precision,
        "cases": cases,
        "cases_with_prime_dividing_z": ramified_cases,
        "digit_corrections": corrections,
    }


if __name__ == "__main__":
    result = {
        "finite_representative_cases": check_finite_representatives(),
        "lifts": check_lifts(),
        "result": "PASS",
        "scope": "Bounded construction checks only; neither a Beal proof nor a counterexample.",
    }
    print(json.dumps(result, indent=2))
