#!/usr/bin/env python3
"""Exact finite factor tables for the conditional exceptional-field bridge.

Run from beal: python3 scripts/mixed-seventh-certificate/check_parameters.py
Uses only the standard library. Polynomial coefficients are constant first.
This checks residue arithmetic, not transport from an integer solution.
"""

from collections import Counter
from itertools import product
import json
from pathlib import Path

Q = 29
PHI = [0, 0, 0, 0, 0, 21, -35, 15]
EXCEPTIONAL = [-3945, 3955, -483, 0, 0, 0, 0, 1]
TARGET_TYPE = [1, 3, 3]


def trim(f):
    f = [a % Q for a in f]
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    return f


def subtract(f, g):
    return trim([(f[i] if i < len(f) else 0)
                 - (g[i] if i < len(g) else 0)
                 for i in range(max(len(f), len(g)))])


def multiply(f, g):
    result = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            result[i + j] += a * b
    return trim(result)


def divide(f, g):
    f, g = trim(f), trim(g)
    assert g != [0]
    quotient = [0] * max(1, len(f) - len(g) + 1)
    while f != [0] and len(f) >= len(g):
        shift = len(f) - len(g)
        a = f[-1] * pow(g[-1], -1, Q) % Q
        quotient[shift] = a
        f = subtract(f, [0] * shift + [a * b for b in g])
    return trim(quotient), f


def monic(f):
    f = trim(f)
    assert f != [0]
    inverse = pow(f[-1], -1, Q)
    return trim([inverse * a for a in f])


def gcd(f, g):
    f, g = trim(f), trim(g)
    while g != [0]:
        f, g = g, divide(f, g)[1]
    return monic(f)


def power_mod(f, n, modulus):
    result = [1]
    while n:
        if n & 1:
            result = divide(multiply(result, f), modulus)[1]
        f = divide(multiply(f, f), modulus)[1]
        n //= 2
    return result


def factor_record(f):
    f = trim(f)
    degree = len(f) - 1
    derivative = [i * f[i] for i in range(1, len(f))]
    squarefree_gcd = gcd(f, derivative)
    assert squarefree_gcd == [1], (f, squarefree_gcd)
    # X^(q^d)-X contains each monic irreducible of degree dividing d once.
    frobenius = [0, 1]
    gcd_degrees = []
    factor_counts = {}
    for d in range(1, degree + 1):
        frobenius = power_mod(frobenius, Q, f)
        total = len(gcd(f, subtract(frobenius, [0, 1]))) - 1
        lower = sum(e * factor_counts[e] for e in factor_counts if d % e == 0)
        assert (total - lower) >= 0 and (total - lower) % d == 0
        factor_counts[d] = (total - lower) // d
        gcd_degrees.append(total)
    factor_type = [d for d, count in factor_counts.items() for _ in range(count)]
    assert sum(factor_type) == degree
    return {"polynomial": f, "squarefree_gcd": squarefree_gcd,
            "frobenius_gcd_degrees": gcd_degrees, "factor_type": factor_type}


def explicit_133(f):
    """Independently certify each matching polynomial by exact division."""
    original = monic(f)
    f = original
    factors = []
    for r in range(Q):
        quotient, remainder = divide(f, [-r, 1])
        if remainder == [0]:
            factors.append(trim([-r, 1]))
            f = quotient
    assert len(factors) == 1 and len(f) == 7
    for coefficients in product(range(Q), repeat=3):
        cubic = list(coefficients) + [1]
        quotient, remainder = divide(f, cubic)
        if remainder == [0]:
            assert len(quotient) == 4
            factors.extend([cubic, quotient])
            break
    assert len(factors) == 3
    # A cubic over a field is irreducible exactly when it has no field root.
    for cubic in factors[1:]:
        assert all(divide(cubic, [-r, 1])[1] != [0] for r in range(Q))
    reconstructed = [1]
    for factor in factors:
        reconstructed = multiply(reconstructed, factor)
    assert reconstructed == original
    return factors


def binomial(n, coefficient, u):
    return [-u] + [0] * (n - 1) + [coefficient]


def main():
    exceptional = factor_record(EXCEPTIONAL)
    assert exceptional["factor_type"] == TARGET_TYPE
    exceptional["explicit_factors"] = explicit_133(EXCEPTIONAL)
    ordinary = []
    for eta in range(2, Q):
        f = list(PHI)
        f[0] = -eta
        record = factor_record(f)
        record["eta"] = eta
        record["t0"] = eta * pow(eta - 1, -1, Q) % Q
        if record["factor_type"] == TARGET_TYPE:
            record["explicit_factors"] = explicit_133(f)
        ordinary.append(record)
    survivors = [r["eta"] for r in ordinary if r["factor_type"] == TARGET_TYPE]
    assert survivors == [10, 14, 24, 28]
    assert [r["t0"] for r in ordinary if r["eta"] in survivors] == [14, 10, 25, 15]

    fixed_x = factor_record([21, -35, 15])
    fixed_y = factor_record([35, 105, 126, 70, 15])
    assert fixed_x["factor_type"] == [1, 1]
    assert fixed_y["factor_type"] == [1, 1, 2]
    branches = {}
    for name, n, coefficient, fixed in [
            ("29_divides_X", 5, 21, fixed_x["factor_type"]),
            ("29_divides_Y", 3, 35, fixed_y["factor_type"]),
            ("29_divides_Z", 7, 15, [])]:
        rows = []
        for u in range(1, Q):
            record = factor_record(binomial(n, coefficient, u))
            record["unit"] = u
            record["combined_factor_type"] = sorted(fixed + record["factor_type"])
            assert record["combined_factor_type"] != TARGET_TYPE
            rows.append(record)
        branches[name] = rows
    assert all(r["combined_factor_type"] == [1, 1, 1, 2, 2]
               for name in ("29_divides_X", "29_divides_Y") for r in branches[name])
    z_types = Counter(tuple(r["combined_factor_type"]) for r in branches["29_divides_Z"])
    assert z_types == Counter({(1,) * 7: 4, (7,): 24})
    split_units = [r["unit"] for r in branches["29_divides_Z"]
                   if r["combined_factor_type"] == [1] * 7]
    assert split_units == sorted({15 * pow(a, 7, Q) % Q for a in range(1, Q)})

    report = {"q": Q, "coefficient_order": "constant first",
              "scope": "Finite-field arithmetic only; no local-algebra transport assumed.",
              "exceptional": exceptional, "ordinary": ordinary,
              "ordinary_survivors": survivors, "fixed_X": fixed_x, "fixed_Y": fixed_y,
              "branches": branches, "Z_branch_split_units": split_units,
              "all_source_tables_match": True}
    output = Path(__file__).with_name("parameter-results.json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print("Exceptional polynomial factors:", exceptional["explicit_factors"])
    print("Ordinary factor types:", {r["eta"]: r["factor_type"] for r in ordinary})
    print("Survivors eta -> t0:", [(r["eta"], r["t0"]) for r in ordinary
                                     if r["eta"] in survivors])
    print("X and Y branch types: [1,1,1,2,2] for all 28 unit residues each.")
    print("Z branch: seven linear factors for units", split_units, "; [7] otherwise.")
    print("All 111 variable residue cases and three fixed polynomials checked.")


if __name__ == "__main__":
    main()
