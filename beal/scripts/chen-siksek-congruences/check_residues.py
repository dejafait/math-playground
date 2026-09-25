#!/usr/bin/env python3
"""Check the residue arithmetic of L011, not the cited Diophantine theorem.

Run from the active notebook:
    python3 scripts/chen-siksek-congruences/check_residues.py
"""

import json
from math import gcd, isqrt, lcm
from pathlib import Path


# Literal clause IV in Theorem 1, author manuscript p. 2.
CLAUSE_IV_1296 = {
    43, 49, 61, 79, 97, 151, 157, 169, 187, 205, 259, 265, 277, 295, 313,
    367, 373, 385, 403, 421, 475, 481, 493, 511, 529, 583, 589, 601, 619, 637,
    691, 697, 709, 727, 745, 799, 805, 817, 835, 853, 907, 913, 925, 943, 961,
    1015, 1021, 1033, 1051, 1069, 1123, 1129, 1141, 1159, 1177, 1231, 1237,
    1249, 1267, 1285,
}
CLAUSE_IV_108 = {43, 49, 61, 79, 97}
SURVIVING_108 = {1, 7, 13, 19, 25, 31, 37, 55, 67, 73, 85, 91, 103}
MODULUS = lcm(108, 5, 13, 53)


def source_clauses(d):
    """The displayed clauses, before simplification or prime assumptions."""
    return {
        "I": d % 5 in {2, 3},
        "II": d % 78 in {17, 61},
        "III": d % 106 in {51, 103, 105},
        "IV": d % 1296 in CLAUSE_IV_1296,
    }


def survives(r):
    return (
        r % 108 in SURVIVING_108
        and r % 5 in {1, 4}
        and r % 13 in set(range(1, 13)) - {9}
        and r % 53 in range(1, 50)
    )


def is_prime(n):
    """Exact trial division, used only for the two small exponent controls."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def main():
    lifted = {r + 108 * j for r in CLAUSE_IV_108 for j in range(12)}
    assert CLAUSE_IV_1296 == lifted
    assert len(lifted) == 60
    assert all(
        (r in CLAUSE_IV_1296) == (r % 108 in CLAUSE_IV_108)
        for r in range(1296)
    )
    assert not any(source_clauses(1).values())
    assert SURVIVING_108 == set(range(1, 108, 6)) - CLAUSE_IV_108
    assert MODULUS == 372060

    units = old_remaining = source_excluded = new_excluded = remaining = 0
    for r in range(MODULUS):
        if gcd(r, MODULUS) != 1:
            assert not survives(r)
            continue
        units += 1
        clauses = source_clauses(r)
        source_excluded += any(clauses.values())
        before = r % 3 == 1
        old_remaining += before
        after = before and not any(clauses.values())
        assert after == survives(r), r
        remaining += after
        new_excluded += before and any(clauses.values())
        if before:
            assert clauses["II"] == (r % 13 == 9), r
        assert clauses["III"] == (r % 53 in {50, 51, 52}), r

    assert (units, old_remaining, source_excluded, new_excluded, remaining) == (
        89856, 44928, 56438, 30914, 14014
    )
    assert remaining == 13 * 2 * 11 * 49
    # Cross-check the paper's section 10 count on its unreduced modulus.
    original_modulus = lcm(5, 78, 106, 1296)
    assert original_modulus == 12 * MODULUS == 4464720
    assert 12 * source_excluded == 677256

    controls = []
    for p, expected in ((1000000009, True), (1000000021, False)):
        assert p > 10**9 and p % 3 == 1 and is_prime(p)
        assert survives(p) == expected
        controls.append({
            "prime_exponent": p,
            "residues_mod_108_5_13_53": [p % m for m in (108, 5, 13, 53)],
            "theorem_1_clauses": [k for k, v in source_clauses(p).items() if v],
            "survives_exponent_tests": expected,
        })
    assert controls[1]["theorem_1_clauses"] == ["IV"]

    result = {
        "purpose": "Exact exponent-residue audit; no search for Beal solutions.",
        "modulus": MODULUS,
        "allowed_residues": {
            "108": sorted(SURVIVING_108),
            "5": [1, 4],
            "13": sorted(set(range(1, 13)) - {9}),
            "53": list(range(1, 50)),
        },
        "reduced_classes": units,
        "classes_before_theorem_1_with_p_1_mod_3": old_remaining,
        "newly_excluded_classes": new_excluded,
        "remaining_classes": remaining,
        "theorem_1_excluded_classes_before_freitas": source_excluded,
        "original_modulus": original_modulus,
        "original_theorem_1_class_count": 12 * source_excluded,
        "controls": controls,
        "qualification": "Theorem 1's proof and number-field computations were not rerun.",
    }
    Path(__file__).with_name("results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in (
        "modulus", "reduced_classes", "newly_excluded_classes", "remaining_classes", "controls"
    )}, indent=2))


if __name__ == "__main__":
    main()
