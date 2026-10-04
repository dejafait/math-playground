#!/usr/bin/env python3
"""Check the A=k+2 collision certificate and small-domain center lists.

Counts for the 1024-point instance are rigorous pigeonhole lower bounds,
not enumerated joint fibers. Small-domain candidates are independently
reconstructed by Lagrange interpolation from k received values.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial
import json

from verify import evaluate, interpolate


def coefficient_pair(subset, p):
    first = sum(subset) % p
    second = sum(x * y for x, y in combinations(subset, 2)) % p
    return first, second


def pivot_value(x, k, pair, p):
    b, c = pair
    return (pow(x, k + 2, p) - b * pow(x, k + 1, p) + c * pow(x, k, p)) % p


def check_center(domain, subsets, k, pair, p):
    center = tuple(pivot_value(x, k, pair, p) for x in domain)
    words = set()
    for subset in subsets:
        points = subset[:k]
        values = [pivot_value(x, k, pair, p) for x in points]
        coefficients = interpolate(points, values, p)
        assert len(coefficients) == k  # Leading zero coefficients are allowed.
        word = tuple(evaluate(coefficients, x, p) for x in domain)
        agreements = tuple(x for x, y, value in zip(domain, center, word) if y == value)
        assert agreements == subset
        assert word not in words
        words.add(word)
    assert len(words) == len(subsets)

    for m in (1, 3):
        received = tuple((value,) + (0,) * (m - 1) for value in center)
        candidates = {tuple((value,) + (0,) * (m - 1) for value in word) for word in words}
        assert len(candidates) == len(subsets)
        assert all(sum(a == b for a, b in zip(received, word)) == k + 2 for word in candidates)

    exhaustive_scalar_count = None
    if k <= 2:
        exhaustive_scalar_count = sum(
            sum(evaluate(coefficients, x, p) == y for x, y in zip(domain, center)) >= k + 2
            for coefficients in product(range(p), repeat=k)
        )
        assert exhaustive_scalar_count == len(subsets)

    exhaustive_width_two_count = None
    if k == 1:
        exhaustive_width_two_count = sum(
            sum((a, b) == (y, 0) for y in center) >= k + 2
            for a, b in product(range(p), repeat=2)
        )
        assert exhaustive_width_two_count == len(subsets)
    return {
        "coefficient_pair": pair,
        "exact_list": len(subsets),
        "interleaved_widths_checked": [1, 3],
        "exhaustive_scalar_count": exhaustive_scalar_count,
        "exhaustive_width_two_count": exhaustive_width_two_count,
    }


def small_domain_audit():
    p = 97
    domain = sorted(pow(8, j, p) for j in range(16))
    assert len(set(domain)) == 16 and pow(8, 8, p) == p - 1
    assert 16 < p - 1
    cases = []
    for k in (8, 4, 2, 1):
        fibers = {}
        for subset in combinations(domain, k + 2):
            pair = coefficient_pair(subset, p)
            fibers.setdefault(pair, []).append(subset)
        counts = Counter({pair: len(subsets) for pair, subsets in fibers.items()})
        assert sum(counts.values()) == comb(len(domain), k + 2)
        assert len(counts) <= p**2
        largest_pair = max(counts, key=lambda pair: (counts[pair], pair))
        largest = counts[largest_pair]
        lower = (comb(16, k + 2) + p**2 - 1) // p**2
        upper = comb(16, k) // comb(k + 2, k)
        assert lower <= largest <= upper
        nonzero_pair = max(
            (pair for pair in counts if all(pair)),
            key=lambda pair: (counts[pair], pair),
        )
        checks = [check_center(domain, fibers[pair], k, pair, p)
                  for pair in sorted({largest_pair, nonzero_pair})]
        cases.append({
            "k": k,
            "s": k + 2,
            "nonempty_fibers": len(counts),
            "largest_joint_fiber": largest,
            "collision_lower": lower,
            "support_upper": upper,
            "center_checks": checks,
        })
    return {"p": p, "domain": domain, "cases": cases}


def fixed_instance_audit():
    source_q = 65537
    ambient_q = source_q**28
    threshold = Fraction(ambient_q, 2**128)
    assert 2**320 < threshold < 2**321
    assert 2**16 < source_q < 2**17
    assert factorial(66) > 2**308
    assert comb(1024, 66) < Fraction(2**660, factorial(66)) < 2**352
    cases = []
    exponents = {512: 986, 256: 796, 128: 525, 64: 316}
    for k in (512, 256, 128, 64):
        s = k + 2
        total = comb(1024, s)
        divisor = source_q**2
        lower = (total + divisor - 1) // divisor
        assert (lower - 1) * divisor < total <= lower * divisor
        exponent = exponents[k]
        assert 2**exponent < lower < 2**(exponent + 1)
        support_upper = comb(1024, k) // comb(s, k)
        assert lower <= support_upper
        exceeds = lower * 2**128 > ambient_q
        assert exceeds == (k != 64)
        if k != 64:
            assert 128 <= min(s, 1024 - s) <= 512
            assert total >= comb(1024, 128) >= 8**128 == 2**384
            assert Fraction(total, divisor) > 2**350 > threshold
            new_t_star_upper = 1024 - k - 3
        else:
            assert Fraction(total, divisor) < 2**320
            assert lower <= 2**320 < threshold
            new_t_star_upper = None
        cases.append({
            "k": k,
            "rate": str(Fraction(k, 1024)),
            "s": s,
            "total_subsets": str(total),
            "certified_list_lower": str(lower),
            "lower_power_of_two_exponent": exponent,
            "support_upper": str(support_upper),
            "certificate_exceeds_threshold": exceeds,
            "tested_error_index": 1024 - s,
            "new_t_star_upper": new_t_star_upper,
            "actual_largest_joint_fiber": "not computed",
        })
    return {
        "source_field_cardinality": source_q,
        "ambient_extension_degree": 28,
        "ambient_field_cardinality": str(ambient_q),
        "threshold": str(threshold),
        "cases": cases,
    }


def main():
    result = {
        "all_checks_passed": True,
        "fixed_instance": fixed_instance_audit(),
        "independent_small_domain_checks": small_domain_audit(),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
