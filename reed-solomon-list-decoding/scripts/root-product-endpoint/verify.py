#!/usr/bin/env python3
"""Independent interpolation and exhaustive endpoint checks for L011.

The smooth-domain check reconstructs candidates by Lagrange interpolation,
without subtracting root products. The exhaustive check reuses the existing
enumerator, which scans every center modulo code translation. These finite
checks corroborate the symbolic proof and do not locate other boundaries.
"""

from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
import json
import runpy


def evaluate(coefficients, x, p):
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * x + coefficient) % p
    return value


def interpolate(subset, k, p):
    """Interpolate x^k on the subset using a degree-less-than-k polynomial."""
    coefficients = [0] * k
    for a in subset:
        basis = [1]
        denominator = 1
        for b in subset:
            if b == a:
                continue
            grown = [0] * (len(basis) + 1)
            for j, coefficient in enumerate(basis):
                grown[j] = (grown[j] - b * coefficient) % p
                grown[j + 1] = (grown[j + 1] + coefficient) % p
            basis = grown
            denominator = denominator * (a - b) % p
        scale = pow(a, k, p) * pow(denominator, -1, p) % p
        for j, coefficient in enumerate(basis):
            coefficients[j] = (coefficients[j] + scale * coefficient) % p
    return tuple(coefficients)


def smooth_domain_audit():
    p, n = 97, 16
    assert all(p % d for d in range(2, int(p**0.5) + 1))
    root = next(a for a in range(1, p) if pow(a, n, p) == 1 and pow(a, n // 2, p) != 1)
    subgroup = {pow(root, j, p) for j in range(n)}
    multiplier = next(a for a in range(1, p) if a not in subgroup)
    domain = sorted(multiplier * a % p for a in subgroup)
    assert len(subgroup) == len(set(domain)) == n
    assert set(domain).isdisjoint(subgroup)
    cases = []
    for k in (n // 2, n // 4, n // 8, n // 16):
        center = tuple(pow(x, k, p) for x in domain)
        scalar_words = set()
        for subset in combinations(domain, k):
            coefficients = interpolate(subset, k, p)
            assert len(coefficients) == k
            word = tuple(evaluate(coefficients, x, p) for x in domain)
            agreements = tuple(x for x, y, value in zip(domain, center, word) if y == value)
            assert agreements == subset
            assert word not in scalar_words
            scalar_words.add(word)
        assert len(scalar_words) == comb(n, k)
        interleaved = []
        for m in (1, 3):
            received = tuple((value,) + (0,) * (m - 1) for value in center)
            words = {tuple((value,) + (0,) * (m - 1) for value in word) for word in scalar_words}
            assert len(words) == comb(n, k)
            assert all(sum(a == b for a, b in zip(received, word)) == k for word in words)
            interleaved.append({"m": m, "distinct_candidates": len(words), "agreement_columns": k})
        cases.append({"k": k, "rate": str(Fraction(k, n)), "expected_endpoint": comb(n, k), "interleaved": interleaved})
    return {"p": p, "n": n, "subgroup_generator": root, "coset_multiplier": multiplier, "domain": domain, "cases": cases}


def exhaustive_audit():
    path = Path(__file__).resolve().parents[1] / "finite-support" / "verify.py"
    audit = runpy.run_path(str(path))["audit"]
    cases = [
        (3, [1, 2], 1, 2, Fraction(2, 3)),
        (5, [1, 2, 3, 4], 2, 2, Fraction(4, 5)),
        (13, [1, 5, 12, 8], 2, 1, Fraction(1, 2)),
    ]
    results = []
    for p, domain, k, m, epsilon in cases:
        result = audit(p, domain, k, m, epsilon)
        n = len(domain)
        endpoint = result["max_list_by_integer_radius"][n - k]
        assert endpoint == comb(n, k)
        endpoint_safe = endpoint <= epsilon * p
        assert endpoint_safe == (result["largest_safe_error_index"] == n - k)
        results.append({"p": p, "n": n, "k": k, "m": m, "threshold": str(epsilon * p), "exact_endpoint": endpoint, "endpoint_safe": endpoint_safe})
    return results


def main():
    result = {"all_checks_passed": True, "smooth_domain": smooth_domain_audit(), "exhaustive_toy_cases": exhaustive_audit()}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
