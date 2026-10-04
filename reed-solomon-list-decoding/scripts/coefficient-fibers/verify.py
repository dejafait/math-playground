#!/usr/bin/env python3
"""Independent subset enumeration/interpolation checks for the A=k+1 lists.

The candidate polynomials are recovered from k received values by Lagrange
interpolation, without constructing or subtracting any root product. Only
prime-field domains are enumerated; the ambient extension threshold is an
exact cardinality calculation, not an enumeration of that extension field.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb, isqrt
import json


def evaluate(coefficients, x, p):
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * x + coefficient) % p
    return value


def pivot_value(x, k, b, p):
    return (pow(x, k + 1, p) - b * pow(x, k, p)) % p


def interpolate(points, values, p):
    """Return the degree-less-than-len(points) interpolant."""
    coefficients = [0] * len(points)
    for a, value in zip(points, values):
        basis = [1]
        denominator = 1
        for x in points:
            if x == a:
                continue
            grown = [0] * (len(basis) + 1)
            for j, coefficient in enumerate(basis):
                grown[j] = (grown[j] - x * coefficient) % p
                grown[j + 1] = (grown[j + 1] + coefficient) % p
            basis = grown
            denominator = denominator * (a - x) % p
        scale = value * pow(denominator, -1, p) % p
        for j, coefficient in enumerate(basis):
            coefficients[j] = (coefficients[j] + scale * coefficient) % p
    return tuple(coefficients)


def subset_counts(domain, s, p):
    return Counter(sum(subset) % p for subset in combinations(domain, s))


def li_wan_full_nonzero_count(q, p, s, b):
    j = s // p
    eta = (-1) ** (s + j)
    v = q - 1 if b == 0 else -1
    numerator = comb(q - 1, s) + eta * v * comb(q // p - 1, j)
    assert numerator % q == 0
    return numerator // q


def check_center(domain, k, b, p, expected):
    center = tuple(pivot_value(x, k, b, p) for x in domain)
    words = set()
    for subset in combinations(domain, k + 1):
        if sum(subset) % p != b:
            continue
        interpolation_points = subset[:k]
        interpolation_values = [pivot_value(x, k, b, p) for x in interpolation_points]
        coefficients = interpolate(interpolation_points, interpolation_values, p)
        word = tuple(evaluate(coefficients, x, p) for x in domain)
        agreements = tuple(x for x, y, value in zip(domain, center, word) if y == value)
        assert agreements == subset
        assert word not in words
        words.add(word)
    assert len(words) == expected
    interleaved_checks = []
    for m in (1, 3):
        received = tuple((value,) + (0,) * (m - 1) for value in center)
        candidates = {tuple((value,) + (0,) * (m - 1) for value in word) for word in words}
        assert len(candidates) == expected
        assert all(sum(a == b_col for a, b_col in zip(received, word)) == k + 1 for word in candidates)
        interleaved_checks.append({"m": m, "distinct_candidates": expected, "agreement_columns": k + 1})

    # A distinct check of completeness for the two smallest message dimensions.
    exhaustive_scalar_count = None
    if k <= 2:
        exhaustive_scalar_count = sum(
            sum(evaluate(coefficients, x, p) == y for x, y in zip(domain, center)) >= k + 1
            for coefficients in product(range(p), repeat=k)
        )
        assert exhaustive_scalar_count == expected
    return {"interleaved": interleaved_checks, "exhaustive_scalar_count": exhaustive_scalar_count}


def audit_domain(p, subgroup, multiplier, full_nonzero):
    assert all(p % d for d in range(2, isqrt(p) + 1))
    n = len(subgroup)
    assert n >= 16 and n & (n - 1) == 0
    assert len(set(subgroup)) == n and 0 not in subgroup
    assert {a * b % p for a in subgroup for b in subgroup} == set(subgroup)
    domain = sorted(multiplier * a % p for a in subgroup)
    assert len(set(domain)) == n
    if full_nonzero:
        assert set(subgroup) == set(range(1, p))
    cases = []
    for k in (n // 2, n // 4, n // 8, n // 16):
        s = k + 1
        counts = subset_counts(domain, s, p)
        base_counts = subset_counts(sorted(subgroup), s, p)
        inverse = pow(multiplier, -1, p)
        assert sum(counts.values()) == comb(n, s)
        assert all(counts[b] == base_counts[b * inverse % p] for b in range(p))
        if full_nonzero:
            assert all(counts[b] == li_wan_full_nonzero_count(p, p, s, b) for b in range(p))
        b = max(range(p), key=lambda c: (counts[c], -c))
        largest = counts[b]
        support_upper = comb(n, k) // (k + 1)
        assert largest <= support_upper
        checks = check_center(domain, k, b, p, largest)
        cases.append({
            "k": k,
            "rate": str(Fraction(k, n)),
            "s": s,
            "center_parameter": b,
            "largest_fiber": largest,
            "zero_sum_fiber": counts[0],
            "fiber_histogram": dict(sorted(Counter(counts[b] for b in range(p)).items())),
            "support_upper": support_upper,
            **checks,
        })
    return {"p": p, "n": n, "coset_multiplier": multiplier, "domain": domain, "cases": cases}


def threshold_audit(full_domain):
    epsilon = Fraction(1, 2**128)
    q = 17**32
    threshold = epsilon * q
    assert 1 < threshold < 8
    expected = {8: 673, 4: 257, 2: 33, 1: 8}
    cases = []
    for case in full_domain["cases"]:
        k = case["k"]
        count = case["largest_fiber"]
        assert count == expected[k]
        assert count > threshold
        cases.append({
            "k": k,
            "attained_list": count,
            "unsafe_error_index": 16 - k - 1,
            "largest_safe_index_upper": 16 - k - 2,
            "unsafe": True,
        })
    return {
        "domain_subfield_cardinality": 17,
        "ambient_extension_degree": 32,
        "ambient_field_cardinality": q,
        "epsilon": str(epsilon),
        "threshold": str(threshold),
        "threshold_is_between_1_and_8": True,
        "cases": cases,
    }


def main():
    full_domain = audit_domain(17, list(range(1, 17)), 1, True)
    subgroup = sorted(pow(8, j, 97) for j in range(16))
    assert pow(8, 16, 97) == 1 and pow(8, 8, 97) != 1
    assert 2 not in subgroup
    coset = audit_domain(97, subgroup, 2, False)
    result = {
        "all_checks_passed": True,
        "full_nonzero_subfield_domain": full_domain,
        "nontrivial_smooth_coset": coset,
        "cryptographic_threshold": threshold_audit(full_domain),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
