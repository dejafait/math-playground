#!/usr/bin/env python3
"""Exact pigeonhole certificate and independent small pole-center checks.

The large-domain fibers and ambient extension are not enumerated. Small
messages are reconstructed by interpolation, with separate root-product
cancellation and exhaustive-list checks. Full output stays in this directory.
"""

from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial, prod
from pathlib import Path
import json

from verify import evaluate, interpolate


def parameter(subset, p):
    return sum(subset) % p, ((-1) ** len(subset) * prod(subset)) % p


def received(x, k, pair, p):
    b, d = pair
    return (pow(x, k + 1, p) - b * pow(x, k, p) + d * pow(x, -1, p)) % p


def root_polynomial(subset, p):
    coefficients = [1]
    for a in subset:
        grown = [0] * (len(coefficients) + 1)
        for j, c in enumerate(coefficients):
            grown[j] = (grown[j] - a * c) % p
            grown[j + 1] = (grown[j + 1] + c) % p
        coefficients = grown
    return coefficients


def check_center(domain, subsets, k, pair, p):
    center = tuple(received(x, k, pair, p) for x in domain)
    words = set()
    for subset in subsets:
        coefficients = interpolate(subset[:k], [received(x, k, pair, p) for x in subset[:k]], p)
        root = root_polynomial(subset, p)
        numerator = [(-c) % p for c in root]
        b, d = pair
        numerator[0] = (numerator[0] + d) % p
        numerator[k + 1] = (numerator[k + 1] - b) % p
        numerator[k + 2] = (numerator[k + 2] + 1) % p
        assert numerator[0] == numerator[k + 1] == numerator[k + 2] == 0
        assert tuple(numerator[1:k + 1]) == coefficients
        word = tuple(evaluate(coefficients, x, p) for x in domain)
        agreements = tuple(x for x, y, w in zip(domain, center, word) if y == w)
        assert agreements == subset
        assert word not in words
        words.add(word)
    for m in (1, 3):
        array = tuple((y,) + (0,) * (m - 1) for y in center)
        candidate_arrays = {tuple((w,) + (0,) * (m - 1) for w in word) for word in words}
        assert len(candidate_arrays) == len(subsets)
        assert all(sum(y == w for y, w in zip(array, candidate)) == k + 2
                   for candidate in candidate_arrays)
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
    return {"pair": pair, "exact_list": len(subsets), "widths": [1, 3],
            "exhaustive_scalar_count": exhaustive_scalar_count,
            "exhaustive_width_two_count": exhaustive_width_two_count}


def small_domain_checks():
    cases = []
    for p, generator, n, dimensions in ((97, 8, 16, (8, 4, 2, 1)),
                                          (31, 2, 5, (2, 1))):
        domain = sorted(pow(generator, j, p) for j in range(n))
        assert len(set(domain)) == n and pow(generator, n, p) == 1
        assert n < p - 1
        for k in dimensions:
            s = k + 2
            ending_coset = {((-1) ** s * x) % p for x in domain}
            fibers = {}
            for subset in combinations(domain, s):
                pair = parameter(subset, p)
                assert pair[1] in ending_coset and pair[1] != 0
                fibers.setdefault(pair, []).append(subset)
            assert sum(map(len, fibers.values())) == comb(n, s)
            assert len(fibers) <= p * n
            largest = max(fibers, key=lambda pair: (len(fibers[pair]), pair))
            nonzero_sum = max((pair for pair in fibers if pair[0]),
                              key=lambda pair: (len(fibers[pair]), pair))
            lower = (comb(n, s) + p * n - 1) // (p * n)
            assert lower <= len(fibers[largest])
            cases.append({"p": p, "n": n, "k": k,
                          "largest_fiber": len(fibers[largest]),
                          "nonempty_fibers": len(fibers),
                          "ending_coset_equals_subgroup": ending_coset == set(domain),
                          "selected_centers": [check_center(domain, fibers[pair], k, pair, p)
                                               for pair in sorted({largest, nonzero_sum})]})
    return cases


def fixed_instance():
    Q, n, k, s = 65537, 1024, 64, 66
    total = comb(n, s)
    numerator_product = prod(range(n - s + 1, n + 1))
    assert numerator_product == total * factorial(s)
    assert 2**348 * factorial(s) < numerator_product < 2**349 * factorial(s)
    classes = Q * n
    lower = (total + classes - 1) // classes
    assert (lower - 1) * classes < total <= lower * classes
    assert 2**322 < lower < 2**323
    threshold = Fraction(Q**28, 2**128)
    assert 2**320 < threshold < 2**321
    assert lower * 2**128 > Q**28
    ratio = Fraction(lower, 1) / threshold
    assert Fraction(7204, 1000) < ratio < Fraction(7205, 1000)
    return {"Q": Q, "n": n, "k": k, "agreements": s,
            "total_subsets": str(total), "parameter_classes": classes,
            "certified_list_lower": str(lower), "ambient_q": str(Q**28),
            "actual_threshold": str(threshold), "lower_over_threshold": str(ratio),
            "strict_unsafe_comparison": True, "unsafe_error_index": n - s,
            "t_star_upper": n - s - 1,
            "maximizing_pair": "not computed", "actual_maximum_fiber": "not computed"}


def main():
    result = {"fixed_instance": fixed_instance(), "small_domain_checks": small_domain_checks(),
              "all_checks_passed": True}
    artifact = Path(__file__).with_name("pole-at-zero-results.json")
    artifact.write_text(json.dumps(result, indent=2) + "\n")
    print("All exact checks passed; cancellation, injectivity and simultaneous agreement checked.")
    print("Certified list: 2^322 < lower < 2^323; required threshold: 2^320 < epsilon*q < 2^321.")
    print("7.204 < lower/threshold < 7.205; error index 958 unsafe, t_star <= 957.")
    print("Large-domain maximizing pair, exact fiber and sharp boundary remain uncomputed.")
    print("Artifact: scripts/coefficient-fibers/pole-at-zero-results.json")


if __name__ == "__main__":
    main()
