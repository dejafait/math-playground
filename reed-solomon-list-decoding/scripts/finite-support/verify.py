#!/usr/bin/env python3
"""Exact small-field audit for L001; no external dependencies.

Enumerate prime-field polynomial tuples, then quotient centers by code
translation. Checking that every length-k prefix occurs once makes the
zero-prefix centers a complete set of representatives. The enumeration is
only a sanity check; L001 contains the general informal proof.
"""

from fractions import Fraction
from itertools import product
from math import comb, prod
import json


def audit(p, domain, k, m, epsilon):
    n = len(domain)
    assert p > 1 and all(p % d for d in range(2, int(p**0.5) + 1))
    assert len(set(domain)) == n and all(0 <= x < p for x in domain)
    assert 1 <= k <= n and m >= 1 and 0 < epsilon < 1

    def symbol(values):
        return sum(value * p**row for row, value in enumerate(values))

    def evaluate(coefficients):
        return tuple(
            symbol(
                sum(coefficients[row * k + j] * pow(x, j, p) for j in range(k)) % p
                for row in range(m)
            )
            for x in domain
        )

    code = [evaluate(coefficients) for coefficients in product(range(p), repeat=k * m)]
    code_set = set(code)
    assert len(code_set) == p ** (k * m)
    assert len({word[:k] for word in code}) == p ** (k * m)

    maxima = [0] * (n + 1)
    center_count = 0
    for suffix in product(range(p**m), repeat=n - k):
        center = (0,) * k + suffix
        histogram = [0] * (n + 1)
        for word in code:
            distance = sum(a != b for a, b in zip(center, word))
            histogram[distance] += 1
        running = 0
        for t, count in enumerate(histogram):
            running += count
            maxima[t] = max(maxima[t], running)
        center_count += 1

    support_upper = [comb(n, k) // comb(n - t, k) for t in range(n - k + 1)]
    for t in range(n - k + 1):
        assert maxima[t] * comb(n - t, k) <= comb(n, k)

    roots = domain[: k - 1]
    h_values = [prod((x - a) % p for a in roots) % p for x in domain]
    witness = {
        tuple(symbol(b * value % p for b in multipliers) for value in h_values)
        for multipliers in product(range(p), repeat=m)
    }
    assert len(witness) == p**m and witness <= code_set
    witness_distances = sorted({sum(value != 0 for value in word) for word in witness})
    assert witness_distances == [0, n - k + 1]
    assert maxima[n - k + 1] >= p**m > epsilon * p

    threshold = epsilon * p
    safe_indices = [t for t, size in enumerate(maxima) if size <= threshold]
    assert bool(safe_indices) == (threshold >= 1)
    t_star = max(safe_indices) if safe_indices else None
    if t_star is not None:
        assert t_star <= n - k
        assert safe_indices == list(range(t_star + 1))
    sufficient_condition = threshold >= comb(n, k)
    if sufficient_condition:
        assert t_star == n - k

    return {
        "p": p,
        "domain": domain,
        "k": k,
        "m": m,
        "epsilon": str(epsilon),
        "threshold": str(threshold),
        "codewords": len(code),
        "center_representatives": center_count,
        "max_list_by_integer_radius": maxima,
        "support_upper_through_n_minus_k": support_upper,
        "explicit_next_grid_witness_size": len(witness),
        "largest_safe_error_index": t_star,
        "sufficient_large_field_condition": sufficient_condition,
    }


def main():
    cases = [
        (3, [1, 2], 1, 1, Fraction(2, 3)),
        (3, [1, 2], 1, 2, Fraction(2, 3)),
        (5, [1, 2, 3, 4], 2, 1, Fraction(4, 5)),
        (5, [1, 2, 3, 4], 2, 2, Fraction(4, 5)),
        (13, [1, 5, 12, 8], 2, 1, Fraction(1, 2)),
        (5, [1, 2, 3, 4], 4, 1, Fraction(1, 2)),
        (3, [1, 2], 1, 1, Fraction(1, 4)),
    ]
    results = [audit(*case) for case in cases]
    print(json.dumps({"all_checks_passed": True, "cases": results}, indent=2))


if __name__ == "__main__":
    main()
