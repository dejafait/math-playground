#!/usr/bin/env python3
"""Exact checks of L003's factor algebra and controls, not a Beal search."""

import json
from math import gcd, isqrt
from pathlib import Path


def valuation(number, prime):
    assert number > 0
    exponent = 0
    while number % prime == 0:
        number //= prime
        exponent += 1
    return exponent


def prime_factors(number):
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            yield divisor
            while number % divisor == 0:
                number //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if number > 1:
        yield number


def exact_root(number, exponent):
    low, high = 0, 1 << ((number.bit_length() + exponent - 1) // exponent)
    while low <= high:
        middle = (low + high) // 2
        power = middle**exponent
        if power == number:
            return middle
        if power < number:
            low = middle + 1
        else:
            high = middle - 1
    return None


def factors(a, b):
    return a + b, a * a - a * b + b * b


def reconstruct(branch, n, u, v):
    assert gcd(u, v) == 1
    if branch == 1:
        assert (u * v) % 3 != 0
        s, q, c = u**n, v**n, u * v
    else:
        assert branch == 3 and v % 3 != 0
        s, q, c = 3 ** (n - 1) * u**n, 3 * v**n, 3 * u * v
    numerator = 4 * q - s * s
    assert numerator % 3 == 0
    discriminant = numerator // 3
    if discriminant < 0 or isqrt(discriminant) ** 2 != discriminant:
        return None, discriminant
    d = isqrt(discriminant)
    if d >= s:
        return None, discriminant
    assert (s + d) % 2 == 0
    a, b = (s + d) // 2, (s - d) // 2
    assert a > 0 and b > 0 and gcd(a, b) == 1
    assert factors(a, b) == (s, q)
    assert a**3 + b**3 == c**n
    return (a, b, c), discriminant


def main():
    limit = 256
    counts = {1: 0, 3: 0}
    largest_sum_valuation = 0
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            if gcd(a, b) != 1:
                continue
            s, q = factors(a, b)
            branch = gcd(s, 3)
            counts[branch] += 1
            assert gcd(s, q) == branch
            assert s * q == a**3 + b**3
            assert 4 * q == s * s + 3 * (a - b) ** 2
            assert s * s <= 4 * q and q < s * s
            assert valuation(q, 3) == (1 if branch == 3 else 0)
            assert all(ell == 3 or ell % 3 == 1 for ell in prime_factors(q))
            largest_sum_valuation = max(largest_sum_valuation, valuation(s, 3))

    # Genuine n=2 solutions exercise both converses without presuming a Beal solution.
    square_controls = []
    for a, b, c in [(56, 65, 671), (1, 2, 3), (11, 37, 228)]:
        n = 2
        assert a**3 + b**3 == c**n and gcd(a, b) == 1
        s, q = factors(a, b)
        branch = gcd(s, 3)
        if branch == 1:
            u, v = exact_root(s, n), exact_root(q, n)
        else:
            u, v = exact_root(s // 3 ** (n - 1), n), exact_root(q // 3, n)
        assert u is not None and v is not None
        reconstructed, discriminant = reconstruct(branch, n, u, v)
        assert reconstructed == (max(a, b), min(a, b), c)
        square_controls.append({"a": a, "b": b, "c": c, "n": n,
                                "branch_gcd": branch, "u": u, "v": v,
                                "discriminant": discriminant})

    # Formal factor data test valuation allocation, including 3 dividing u.
    # No claim is made that these data arise from integer a,b.
    ramified_allocation_checks = 0
    for n in (2, 5, 7, 11):
        for k in (1, 2, 3):
            u, v = 2 * 3 ** (k - 1), 7
            s, q, c = 3 ** (n - 1) * u**n, 3 * v**n, 3 * u * v
            assert gcd(s, q) == 3 and gcd(u, v) == 1
            assert s * q == c**n
            assert valuation(q, 3) == 1
            assert valuation(s, 3) == n * valuation(c, 3) - 1 == n * k - 1
            ramified_allocation_checks += 1

    single_factor_controls = []
    for a, b, branch in [(62, 149, 1), (211, 236, 3)]:
        s, q = factors(a, b)
        assert gcd(a, b) == 1 and gcd(s, q) == branch
        assert q == branch * 7**5
        if branch == 1:
            assert exact_root(s, 5) is None
        else:
            assert valuation(s, 3) == 1 and s % 3**4 != 0
        single_factor_controls.append({"a": a, "b": b, "sum": s,
                                       "quadratic_factor": q, "branch_gcd": branch})

    nonsquare_controls = []
    for branch, u, v in [(1, 4, 13), (3, 3, 37)]:
        reconstructed, discriminant = reconstruct(branch, 5, u, v)
        assert reconstructed is None and discriminant > 0
        s = u**5 if branch == 1 else 3**4 * u**5
        assert discriminant < s * s
        assert all(ell % 3 == 1 for ell in prime_factors(v))
        nonsquare_controls.append({"branch_gcd": branch, "n": 5, "u": u, "v": v,
                                   "discriminant": discriminant,
                                   "floor_square_root": isqrt(discriminant)})

    result = {
        "purpose": "Check L003 identities, exceptional valuations, and exact controls; no global exclusion is inferred.",
        "coprime_pair_range": "1 <= a <= b <= 256",
        "coprime_pairs": sum(counts.values()),
        "factor_gcd_one_pairs": counts[1],
        "factor_gcd_three_pairs": counts[3],
        "largest_sum_3_adic_valuation": largest_sum_valuation,
        "square_exponent_controls_outside_beal": square_controls,
        "formal_ramified_allocation_checks": ramified_allocation_checks,
        "single_quadratic_factor_controls_not_beal_solutions": single_factor_controls,
        "factor_data_rejected_by_square_condition": nonsquare_controls,
        "status": "passed",
    }
    output = Path(__file__).with_name("results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
