#!/usr/bin/env python3
"""Certify the failed cubic/cofactor sieve comparison, using exact arithmetic.

The large-domain calculation certifies an upper estimate and a limitation
of its absolute-sum allowance. It does not compute any actual large list.
Small-domain group-ring and cyclotomic calculations check normalization
and the cofactor norm identity without floating-point character sums.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial, prod
import json


def cycle_lengths(permutation):
    visited = set()
    lengths = []
    for start in range(len(permutation)):
        if start in visited:
            continue
        current, length = start, 0
        while current not in visited:
            visited.add(current)
            length += 1
            current = permutation[current]
        lengths.append(length)
    return lengths


def moments(values, p):
    return tuple(sum(pow(x, j, p) for x in values) % p for j in (1, 2, 3))


def convolve(left, right, p):
    answer = Counter()
    for u, left_count in left.items():
        for v, right_count in right.items():
            answer[tuple((x + y) % p for x, y in zip(u, v))] += left_count * right_count
    return answer


def positive_part(counter):
    assert all(count >= 0 for count in counter.values())
    return Counter({key: count for key, count in counter.items() if count})


def small_domain_audit():
    p, n, a = 17, 8, 4
    domain = tuple(sorted(pow(2, j, p) for j in range(n)))
    assert len(set(domain)) == n
    subsets = Counter(moments(subset, p) for subset in combinations(domain, a))
    direct_ordered = Counter(moments(values, p) for values in permutations(domain, a))
    assert direct_ordered == Counter({v: factorial(a) * count
                                      for v, count in subsets.items()})

    cycle_distributions = {
        length: Counter(tuple(length * value % p for value in moments((x,), p))
                        for x in domain)
        for length in range(1, a + 1)
    }
    signed_sieve = Counter()
    cycle_polynomial = 0
    for permutation in permutations(range(a)):
        lengths = cycle_lengths(permutation)
        sign = (-1) ** (a - len(lengths))
        distribution = Counter({(0, 0, 0): 1})
        for length in lengths:
            distribution = convolve(distribution, cycle_distributions[length], p)
        for v, count in distribution.items():
            signed_sieve[v] += sign * count
        cycle_polynomial += 770 ** len(lengths)
    assert positive_part(signed_sieve) == direct_ordered
    assert cycle_polynomial == prod(range(770, 770 + a))
    assert cycle_polynomial == factorial(a) * comb(770 + a - 1, a)

    curve = Counter(moments((z,), p) for z in range(p))
    incidence = Counter(moments(subset + (z,), p)
                        for subset in combinations(domain, a) for z in range(p))
    ordered_incidence = convolve(positive_part(signed_sieve), curve, p)
    assert ordered_incidence == Counter({v: factorial(a) * count
                                         for v, count in incidence.items()})
    fully_split = Counter(moments(subset, p) for subset in combinations(domain, a + 1))
    corrected_lists = Counter({v: count - a * fully_split[v]
                               for v, count in incidence.items()})
    assert all(count >= 0 for count in corrected_lists.values())
    assert sum(corrected_lists.values()) == p * comb(n, a) - a * comb(n, a + 1)

    # R(u) is represented exactly by its coefficient vector in Z[zeta_p].
    # Its squared modulus is a cyclic correlation. Modulo Phi_p, a vector
    # represents an integer N if coefficient[0]-coefficient[j]=N for j>0.
    cubic_norm_coefficients = [0] * p
    cubic_phases = 0
    for u1, u2, u3 in product(range(p), range(p), range(1, p)):
        phase_counts = Counter((u1 * z + u2 * z * z + u3 * z**3) % p
                               for z in range(p))
        for left, left_count in phase_counts.items():
            for right, right_count in phase_counts.items():
                cubic_norm_coefficients[(left - right) % p] += left_count * right_count
        cubic_phases += 1
    expected_norm = p**3 * (p - 1)
    assert all(cubic_norm_coefficients[0] - coefficient == expected_norm
               for coefficient in cubic_norm_coefficients[1:])
    assert cubic_phases == p**2 * (p - 1)
    for u1 in range(1, p):
        assert Counter(u1 * z % p for z in range(p)) == Counter(range(p))

    return {
        "source_field_cardinality": p,
        "domain_order": n,
        "subset_size": a,
        "subsets_enumerated": sum(subsets.values()),
        "distinct_ordered_tuples_enumerated": sum(direct_ordered.values()),
        "signed_three_moment_sieve_agrees": True,
        "factorial_and_cofactor_convolution_agree": True,
        "incidences_enumerated": sum(incidence.values()),
        "corrected_list_sum": sum(corrected_lists.values()),
        "cubic_cofactor_phases_audited_exactly": cubic_phases,
        "exact_cubic_cofactor_squared_norm_sum": expected_norm,
        "cyclotomic_norm_identity_passed": True,
        "linear_cofactor_cancellation_passed": True,
    }


def fixed_instance_certificate():
    q, n, a = 65537, 1024, 66
    index = (q - 1) // n
    assert index == 64 and index * n == q - 1
    assert (index + 1)**2 <= q and 4 <= q
    assert q > a and all(j % q for j in range(1, a + 1))
    assert all(r % q for r in (1, 2, 3))
    assert 4 * q < 513**2 and 9 * q < 769**2

    total = comb(n, a)
    d2, d3 = comb(579, a), comb(835, a)
    assert 2**292 < d2 < 2**293 and 2**328 < d3 < 2**329
    quadratic_phases, cubic_phases = q * (q - 1), q**2 * (q - 1)
    assert 1 + (q - 1) + quadratic_phases + cubic_phases == q**3
    mean_incidence = Fraction(total, q**2)
    upper = mean_incidence + Fraction(513 * (q - 1), q**2) * d2 \
        + Fraction(769 * (q - 1), q) * d3
    threshold = Fraction(q**28, 2**128)
    cubic_allowance_lower = Fraction(q - 1, 769) * d3
    assert 2**320 < threshold < 2**321
    assert 2**338 < upper < 2**339
    assert 320297 < upper / threshold < 320298
    assert 416 < d3 / threshold < 417
    assert 35496 < cubic_allowance_lower / threshold < 35497

    # Compare with the existing unconditional support bound (L001).
    # The failed sieve cap is not an improvement on that older bound.
    support_upper = Fraction(comb(n, 64), comb(a, 64))
    assert support_upper == Fraction(total, comb(n - 64, a - 64))
    support_floor = support_upper.numerator // support_upper.denominator
    assert 1050 < Fraction(support_floor, 1) / threshold <= support_upper / threshold < 1051
    assert threshold < support_upper < upper

    # Remove integer rounding as a possible cause of the failed estimate.
    root_upper = Fraction(256) + Fraction(1, 512)
    assert root_upper**2 > q
    rational_d2 = prod(2 * root_upper + 1 + j for j in range(a)) / factorial(a)
    rational_d3 = prod(3 * root_upper + 1 + j for j in range(a)) / factorial(a)
    rational_upper = mean_incidence + Fraction(q - 1, q**2) * 2 * root_upper * rational_d2 \
        + Fraction(q - 1, q) * 3 * root_upper * rational_d3
    rational_allowance_lower = Fraction(q - 1) * rational_d3 / (3 * root_upper)
    assert threshold < support_upper < rational_upper < upper
    assert 294741 < rational_upper / threshold < 294742
    assert 32749 < rational_allowance_lower / threshold < 32750

    return {
        "source_field_cardinality": q,
        "ambient_extension_degree": 28,
        "domain_order": n,
        "domain_index": index,
        "message_degree_bound_strict": 64,
        "center_degree": 67,
        "agreement_count": a,
        "tested_error_index": n - a,
        "cycle_weights_by_phase_degree": {"quadratic": 514, "cubic": 770},
        "complete_cofactor_caps": {"linear": 0, "quadratic": 513, "cubic": 769},
        "total_subsets": str(total),
        "quadratic_sieve_binomial": str(d2),
        "cubic_sieve_binomial": str(d3),
        "certified_uniform_upper": str(upper),
        "certified_integer_upper": str(upper.numerator // upper.denominator),
        "upper_power_of_two_bracket": [338, 339],
        "upper_threshold_ratio_integer_bracket": [320297, 320298],
        "rationally_refined_upper_threshold_ratio_integer_bracket": [294741, 294742],
        "existing_support_upper_threshold_ratio_integer_bracket": [1050, 1051],
        "new_sieve_cap_improves_existing_support_upper": False,
        "threshold": str(threshold),
        "threshold_power_of_two_bracket": [320, 321],
        "cubic_cofactor_squared_norm_sum": str(q**3 * (q - 1)),
        "constant_weight_absolute_error_allowance_lower": str(cubic_allowance_lower),
        "allowance_lower_threshold_ratio_integer_bracket": [35496, 35497],
        "rationally_refined_allowance_lower_ratio_integer_bracket": [32749, 32750],
        "uniform_cap_below_threshold": False,
        "absolute_sum_method_can_certify_threshold_with_this_cycle_cap": False,
        "allowance_lower_is_an_actual_list_or_error_lower_bound": False,
        "actual_fixed_instance_fibers": "not enumerated",
        "family_safety_or_unsafety": "not established",
        "interleaving_scope": "every m>=1 via L015; no exponent m",
        "full_code_grid_bound_changed": False,
    }


def main():
    result = {
        "all_checks_passed": True,
        "fixed_instance": fixed_instance_certificate(),
        "independent_small_domain_normalization": small_domain_audit(),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
