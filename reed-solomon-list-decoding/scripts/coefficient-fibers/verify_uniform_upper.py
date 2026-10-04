#!/usr/bin/env python3
"""Certify the rate-1/16 uniform two-moment upper comparison.

The fixed-instance certificate uses exact integers and rational numbers,
not enumeration or numerical character sums. A small-domain group-algebra
audit independently checks the imported sieve's signs and the ordered to
unordered conversion against direct subset and distinct-tuple enumeration.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial, prod
import json


def cycle_lengths(permutation):
    visited = set()
    lengths = []
    for start in range(len(permutation)):
        if start in visited:
            continue
        current = start
        length = 0
        while current not in visited:
            visited.add(current)
            length += 1
            current = permutation[current]
        lengths.append(length)
    return lengths


def convolve(left, right, p):
    answer = Counter()
    for (u, v), left_count in left.items():
        for (x, y), right_count in right.items():
            answer[((u + x) % p, (v + y) % p)] += left_count * right_count
    return answer


def normalization_audit():
    p, n, a = 17, 8, 4
    domain = sorted(pow(2, j, p) for j in range(n))
    assert len(set(domain)) == n and pow(2, n // 2, p) == p - 1
    subsets = Counter()
    elementary = Counter()
    for subset in combinations(domain, a):
        first = sum(subset) % p
        second = sum(x * x for x in subset) % p
        pairwise = sum(x * y for x, y in combinations(subset, 2)) % p
        assert second == (first * first - 2 * pairwise) % p
        subsets[(first, second)] += 1
        elementary[(first, pairwise)] += 1

    direct_ordered = Counter(
        (sum(tuple_) % p, sum(x * x for x in tuple_) % p)
        for tuple_ in permutations(domain, a)
    )
    assert direct_ordered == Counter({pair: factorial(a) * count
                                      for pair, count in subsets.items()})
    assert sum(direct_ordered.values()) == prod(range(n - a + 1, n + 1))
    assert sum(subsets.values()) == comb(n, a)
    assert {((b, (b * b - 2 * c) % p), count)
            for (b, c), count in elementary.items()} == set(subsets.items())

    # Each permutation imposes equality within its cycles. Convolve the
    # resulting moment-residue counts before applying the sieve's sign.
    cycle_distributions = {
        j: Counter(((j * x) % p, (j * x * x) % p) for x in domain)
        for j in range(1, a + 1)
    }
    signed_sieve = Counter()
    cycle_weight_sum = 0
    for permutation in permutations(range(a)):
        lengths = cycle_lengths(permutation)
        sign = (-1) ** (a - len(lengths))
        distribution = Counter({(0, 0): 1})
        for length in lengths:
            distribution = convolve(distribution, cycle_distributions[length], p)
        for pair, count in distribution.items():
            signed_sieve[pair] += sign * count
        cycle_weight_sum += 514 ** len(lengths)
    assert all(count >= 0 for count in signed_sieve.values())
    assert Counter({pair: count for pair, count in signed_sieve.items() if count}) == direct_ordered
    assert cycle_weight_sum == prod(range(514, 514 + a))
    assert cycle_weight_sum == factorial(a) * comb(514 + a - 1, a)
    return {
        "source_field_cardinality": p,
        "domain_order": n,
        "subset_size": a,
        "subsets_enumerated": sum(subsets.values()),
        "distinct_ordered_tuples_enumerated": sum(direct_ordered.values()),
        "permutations_in_signed_sieve": factorial(a),
        "moment_pairs_attained": len(subsets),
        "sieve_and_ordered_unordered_normalization_agree": True,
        "elementary_to_power_sum_signs_agree": True,
    }


def fixed_instance_certificate():
    source_q, n, a, extension_degree = 65537, 1024, 66, 28
    characteristic = source_q
    index = (source_q - 1) // n
    assert index == 64 and index * n == source_q - 1
    assert (index + 1) ** 2 <= source_q
    assert characteristic > a and characteristic % 2 != 0
    assert all(j % characteristic != 0 for j in range(1, a + 1))

    # This square comparison proves 2 sqrt(Q)+1 < 514 without floats.
    assert 4 * source_q < 513 ** 2
    character_bound = 514
    total = comb(n, a)
    error = comb(character_bound + a - 1, a)
    numerator = total + (source_q ** 2 - 1) * error
    denominator = source_q ** 2
    upper = Fraction(numerator, denominator)
    upper_floor = numerator // denominator
    threshold = Fraction(source_q ** extension_degree, 2 ** 128)
    mean = Fraction(total, denominator)
    assert total < 2 ** 349 and error < 2 ** 293
    assert upper < 2 ** 318  # Coarse proof from the preceding two brackets.
    assert 2 ** 316 < upper < 2 ** 317
    assert upper_floor <= upper < 2 ** 317 < 2 ** 320 < threshold < 2 ** 321
    assert numerator * 2 ** 128 < source_q ** 30
    assert Fraction(11256, 100000) < upper / threshold < Fraction(11257, 100000)

    # A rational bound supplies an independent, slightly tighter check of
    # the same imported character estimate and cycle specialization.
    root_upper = Fraction(256) + Fraction(1, 512)
    assert root_upper ** 2 > source_q
    rational_character_bound = 2 * root_upper + 1
    assert rational_character_bound < character_bound
    rising = prod(rational_character_bound + j for j in range(a))
    rational_error = rising / factorial(a)
    tighter_upper = mean + Fraction(denominator - 1, denominator) * rational_error
    assert tighter_upper < upper < threshold
    return {
        "source_field_cardinality": source_q,
        "ambient_extension_degree": extension_degree,
        "domain_order": n,
        "domain_index": index,
        "message_degree_bound_strict": 64,
        "agreement_count": a,
        "tested_error_index": n - a,
        "integer_one_coordinate_character_bound": character_bound,
        "total_subsets": str(total),
        "nontrivial_character_error_binomial": str(error),
        "uniform_upper_numerator": str(numerator),
        "uniform_upper_denominator": denominator,
        "certified_integer_list_upper": str(upper_floor),
        "upper_power_of_two_bracket": [316, 317],
        "threshold": str(threshold),
        "threshold_power_of_two_bracket": [320, 321],
        "upper_threshold_ratio_rational_bracket": ["11256/100000", "11257/100000"],
        "strict_threshold_comparison_passed": True,
        "rational_character_bound_check_passed": True,
        "actual_subgroup_fibers": "not enumerated",
        "interleaving_scope": "every m>=1 via L013; no exponent m",
        "full_code_safety": "not established",
    }


def main():
    result = {
        "all_checks_passed": True,
        "fixed_instance": fixed_instance_certificate(),
        "independent_small_domain_normalization": normalization_audit(),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
