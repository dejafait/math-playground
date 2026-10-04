#!/usr/bin/env python3
"""Check the residual-linear-factor dictionary, not large-domain fibers.

The small-domain audit compares cofactor incidences with independently
exhausted scalar messages at every center. Fixed-instance comparisons
use exact integers/rationals and certify only the averaging lower bound.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb
import json


def elementary(subset, p):
    return tuple(sum(prod_mod(group, p) for group in combinations(subset, j)) % p
                 for j in (1, 2, 3))


def prod_mod(values, p):
    result = 1
    for value in values:
        result = result * value % p
    return result


def multiply_by_root(coefficients, root, p):
    result = [0] * (len(coefficients) + 1)
    for j, coefficient in enumerate(coefficients):
        result[j] = (result[j] - root * coefficient) % p
        result[j + 1] = (result[j + 1] + coefficient) % p
    return result


def evaluate(coefficients, x, p):
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * x + coefficient) % p
    return value


def center_word(domain, triple, p):
    # The audited instance has k=2, degree k+3=5, A=k+2=4.
    b, c, d = triple
    return tuple((pow(x, 5, p) - b * pow(x, 4, p)
                  + c * pow(x, 3, p) - d * pow(x, 2, p)) % p
                 for x in domain)


def small_domain_audit():
    p, n, k, a = 17, 8, 2, 4
    domain = tuple(sorted(pow(2, j, p) for j in range(n)))
    assert len(set(domain)) == n and pow(2, n // 2, p) == p - 1
    incidence = Counter()
    full_roots = Counter()
    representations = defaultdict(Counter)
    representatives = {}
    case_counts = Counter()

    for subset in combinations(domain, a):
        e1, e2, e3 = elementary(subset, p)
        moments = tuple(sum(pow(x, j, p) for x in subset) % p for j in (1, 2, 3))
        assert moments == (e1, (e1 * e1 - 2 * e2) % p,
                           (e1**3 - 3 * e1 * e2 + 3 * e3) % p)
        root_product = [1]
        for root in subset:
            root_product = multiply_by_root(root_product, root, p)
        for z in range(p):
            triple = ((e1 + z) % p, (e2 + z * e1) % p,
                      (e3 + z * e2) % p)
            b, c, d = triple
            v = (b, (b * b - 2 * c) % p, (b**3 - 3 * b * c + 3 * d) % p)
            assert moments == tuple((v[j - 1] - pow(z, j, p)) % p
                                    for j in (1, 2, 3))
            difference = multiply_by_root(root_product, z, p)
            assert difference[k:] == [(-d) % p, c, (-b) % p, 1]
            message = tuple((-coefficient) % p for coefficient in difference[:k])
            received = center_word(domain, triple, p)
            word = tuple(evaluate(message, x, p) for x in domain)
            agreement_set = tuple(x for x, y, value in zip(domain, received, word)
                                  if y == value)
            expected = tuple(sorted(set(subset) | ({z} if z in domain else set())))
            assert agreement_set == expected
            incidence[triple] += 1
            representations[triple][message] += 1
            if z not in domain:
                case = "residual_outside_domain"
            elif z in subset:
                case = "repeated_agreement_root"
            else:
                case = "extra_agreement_root"
            case_counts[case] += 1
            if all(triple) and case not in representatives:
                representatives[case] = (triple, message, subset, z)

    for subset in combinations(domain, a + 1):
        triple = elementary(subset, p)
        full_roots[triple] += 1

    # Exhaust every degree-less-than-2 prime-field message independently
    # of root products; compare all 17^3 centers, including empty lists.
    message_words = {message: tuple(evaluate(message, x, p) for x in domain)
                     for message in product(range(p), repeat=k)}
    exact = Counter()
    for triple in product(range(p), repeat=3):
        received = center_word(domain, triple, p)
        direct = {message for message, word in message_words.items()
                  if sum(y == value for y, value in zip(received, word)) >= a}
        represented = representations.get(triple, {})
        assert direct == set(represented)
        assert len(direct) == incidence[triple] - a * full_roots[triple]
        extra_count = 0
        for message in direct:
            agreements = sum(y == value for y, value in zip(received, message_words[message]))
            assert agreements in (a, a + 1)
            assert represented[message] == (a + 1 if agreements == a + 1 else 1)
            extra_count += agreements == a + 1
        assert extra_count == full_roots[triple]
        exact[triple] = len(direct)

    assert sum(incidence.values()) == p * comb(n, a)
    assert sum(full_roots.values()) == comb(n, a + 1)
    assert sum(exact.values()) == p * comb(n, a) - a * comb(n, a + 1)
    assert set(representatives) == {"residual_outside_domain",
                                   "repeated_agreement_root", "extra_agreement_root"}

    # F_17(alpha), alpha^2=3 is a field since 3 is a nonsquare. At base
    # domain points, an affine message has coordinates a0+a1*x and
    # b0+b1*x. Exhausting them also exhausts width-two base-field messages.
    assert pow(3, (p - 1) // 2, p) == p - 1
    extension_checks = []
    for case, (triple, representative, subset, z) in sorted(representatives.items()):
        received = center_word(domain, triple, p)
        extension_messages = set()
        for a0, a1, b0, b1 in product(range(p), repeat=4):
            agreements = sum((a0 + a1 * x) % p == y and (b0 + b1 * x) % p == 0
                             for x, y in zip(domain, received))
            if agreements >= a:
                assert b0 == b1 == 0
                extension_messages.add((a0, a1))
        assert extension_messages == set(representations[triple])
        assert representative in extension_messages

        # A nonzero scale and nonzero low-degree translate of this center.
        scale, translation = 3, (5, 7)
        received_affine = tuple((scale * y + evaluate(translation, x, p)) % p
                                for x, y in zip(domain, received))
        predicted_affine = {tuple((scale * coefficient + offset) % p
                                  for coefficient, offset in zip(message, translation))
                            for message in extension_messages}
        direct_affine = {message for message, word in message_words.items()
                         if sum(y == value for y, value in zip(received_affine, word)) >= a}
        assert predicted_affine == direct_affine
        for m in (1, 3):
            center_tuple = tuple((y,) + (0,) * (m - 1) for y in received_affine)
            for message in direct_affine:
                candidate_tuple = tuple((value,) + (0,) * (m - 1)
                                        for value in message_words[message])
                assert sum(y == value for y, value in zip(center_tuple, candidate_tuple)) >= a
        extension_checks.append({
            "residual_case": case,
            "coefficient_triple": triple,
            "chosen_subset": subset,
            "residual_root": z,
            "exact_scalar_and_extension_list_size": len(extension_messages),
            "extension_messages_exhausted": p**(2 * k),
            "width_two_messages_exhausted_via_components": p**(2 * k),
            "all_extension_candidates_in_prime_field": True,
            "nonmonic_translated_center_check_passed": True,
            "additional_constructed_widths": [1, 3],
        })
    return {
        "base_field_cardinality": p,
        "domain_order": n,
        "message_degree_bound_strict": k,
        "agreement_count": a,
        "center_degree": k + 3,
        "centers_exhausted": p**3,
        "scalar_messages_exhausted_per_center": p**k,
        "total_root_subset_cofactor_incidences": sum(incidence.values()),
        "total_fully_split_root_subsets": sum(full_roots.values()),
        "sum_of_distinct_center_list_sizes": sum(exact.values()),
        "nonempty_center_lists": sum(bool(count) for count in exact.values()),
        "largest_small_domain_list": max(exact.values()),
        "residual_case_incidence_counts": dict(case_counts),
        "all_center_lists_and_multiplicities_agree": True,
        "three_moment_signs_agree": True,
        "representative_extension_and_normalization_checks": extension_checks,
    }


def fixed_instance_certificate():
    q, n, a = 65537, 1024, 66
    total66, total67 = comb(n, a), comb(n, a + 1)
    numerator = q * total66 - a * total67
    denominator = q**3
    mean = Fraction(numerator, denominator)
    lower = (numerator + denominator - 1) // denominator
    threshold = Fraction(q**28, 2**128)
    assert (lower - 1) * denominator < numerator <= lower * denominator
    assert 2**316 < mean <= lower < 2**317 < 2**320 < threshold < 2**321
    assert Fraction(11094, 100000) < mean / threshold < Fraction(11095, 100000)
    assert mean / Fraction(total66, q**2) == Fraction(4327751, 4390979)
    assert mean / Fraction(total66, q**2) == 1 - Fraction(a * (n - a), (a + 1) * q)
    return {
        "source_field_cardinality": q,
        "ambient_extension_degree": 28,
        "domain_order": n,
        "message_degree_bound_strict": 64,
        "center_degree": 67,
        "agreement_count": a,
        "tested_error_index": n - a,
        "incidence_to_list_correction": "I_66 - 66 Z_67",
        "exact_mean": str(mean),
        "averaging_lower_certificate": str(lower),
        "lower_power_of_two_bracket": [316, 317],
        "threshold_power_of_two_bracket": [320, 321],
        "mean_threshold_ratio_bracket": ["11094/100000", "11095/100000"],
        "deduplication_mean_factor": "4327751/4390979",
        "averaging_certifies_unsafety": False,
        "maximum_fixed_instance_fiber": "not computed",
        "uniform_family_upper_below_threshold": "not established",
        "interleaving_scope": "every m>=1 by the factor/root argument",
        "full_code_safety": "not established",
    }


def main():
    result = {
        "all_checks_passed": True,
        "fixed_instance": fixed_instance_certificate(),
        "independent_small_domain_dictionary": small_domain_audit(),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
