#!/usr/bin/env python3
"""Exact modular certificate for the paired quartic pulse first variation.

All underlying coefficients are rational.  Reduction is modulo the fixed
prime 1000003; factorial denominators here are strictly smaller than it.
No floating point, numerical differentiation or numerical quadrature is used.
Run from the notebook: python3 scripts/periodic-tensor/pulse_rank.py
"""

import itertools
import json
from collections import defaultdict
from pathlib import Path

PRIME = 1000003
ORDER = 48
OUT = Path(__file__).with_name("pulse-rank-certificate.json")
COORDS = [(r, j) for r in range(2) for j in range(3)]


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, length - 1):
                yield (first,) + rest


MONOMIALS = list(compositions(4, 6))
INDEX = {m: i for i, m in enumerate(MONOMIALS)}


def clean(poly):
    return {key: value for key, value in poly.items() if value}


def differentiate(poly):
    out = defaultdict(int)
    for factors, coefficient in poly.items():
        for i, (r, j) in enumerate(factors):
            altered = list(factors)
            altered[i] = (r, j + 1)
            out[tuple(sorted(altered))] += coefficient
    return clean(out)


def euler_column(m):
    """E_F(s)=sum_(r,j) (-D)^j partial_(r,j) F(J(s-r))."""
    out = defaultdict(int)
    for a, multiplicity in enumerate(m):
        if not multiplicity:
            continue
        r, j = COORDS[a]
        remaining = list(m)
        remaining[a] -= 1
        factors = tuple(sorted(
            (rr - r, jj)
            for count, (rr, jj) in zip(remaining, COORDS)
            for _ in range(count)
        ))
        poly = {factors: multiplicity * (-1) ** j}
        for _ in range(j):
            poly = differentiate(poly)
        for key, value in poly.items():
            out[key] += value
    return clean(out)


EULER = [euler_column(m) for m in MONOMIALS]


def universal_relations():
    rows = []
    # Total derivatives of degree-four polynomials in h,h',H,H'.
    base_coords = (0, 1, 3, 4)
    for powers in compositions(4, 4):
        m = [0] * 6
        for a, count in zip(base_coords, powers):
            m[a] = count
        row = [0] * len(MONOMIALS)
        for a in base_coords:
            if m[a]:
                shifted = m.copy()
                shifted[a] -= 1
                shifted[a + 1] += 1
                row[INDEX[tuple(shifted)]] += m[a]
        rows.append(row)
    # Translation invariance of each same-height degree-four monomial.
    for powers in compositions(4, 3):
        row = [0] * len(MONOMIALS)
        row[INDEX[powers + (0, 0, 0)]] += 1
        row[INDEX[(0, 0, 0) + powers]] -= 1
        rows.append(row)
    return rows


def add_row(basis, original):
    row = [x % PRIME for x in original]
    for pivot in sorted(basis):
        factor = row[pivot]
        if factor:
            row = [(a - factor * b) % PRIME
                   for a, b in zip(row, basis[pivot])]
    pivot = next((i for i, value in enumerate(row) if value), None)
    if pivot is None:
        return None
    inverse = pow(row[pivot], -1, PRIME)
    basis[pivot] = [(value * inverse) % PRIME for value in row]
    return pivot


def minor_determinant(matrix):
    """Independent square Gaussian elimination with explicit row swaps."""
    a = [[x % PRIME for x in row] for row in matrix]
    determinant = 1
    pivots = []
    swaps = []
    for k in range(len(a)):
        chosen = next((i for i in range(k, len(a)) if a[i][k]), None)
        if chosen is None:
            return 0, pivots, swaps
        if chosen != k:
            a[k], a[chosen] = a[chosen], a[k]
            determinant = -determinant
            swaps.append([k, chosen])
        pivot = a[k][k]
        pivots.append(pivot)
        determinant = determinant * pivot % PRIME
        inverse = pow(pivot, -1, PRIME)
        for i in range(k + 1, len(a)):
            factor = a[i][k] * inverse % PRIME
            if factor:
                for j in range(k, len(a)):
                    a[i][j] = (a[i][j] - factor * a[k][j]) % PRIME
    return determinant % PRIME, pivots, swaps


def convolution(left, right):
    out = [0] * (ORDER + 1)
    for i, a in enumerate(left):
        if a:
            for j in range(ORDER + 1 - i):
                out[i + j] += a * right[j]
    return [a % PRIME for a in out]


def sampled_euler_series(s):
    # f_b^(j)(t)/(2b) = sum_n (-1)^n t^(2n-j)
    #                         /((2n+1)(2n-j)!) (b^2)^n.
    factorials = [1]
    for n in range(1, 2 * ORDER + 2):
        factorials.append(factorials[-1] * n % PRIME)
    jets = {}
    terms = sorted(set(itertools.chain.from_iterable(EULER)))
    for r, j in set(itertools.chain.from_iterable(terms)):
        t = s + r
        coefficients = []
        for n in range(ORDER + 1):
            if 2 * n < j:
                coefficients.append(0)
            else:
                denominator = (2 * n + 1) * factorials[2 * n - j] % PRIME
                coefficients.append(
                    (-1) ** n * pow(t, 2 * n - j, PRIME)
                    * pow(denominator, -1, PRIME) % PRIME
                )
        jets[(r, j)] = coefficients
    pairs = {}
    triples = {}
    for factors in terms:
        pair = factors[:2]
        if pair not in pairs:
            pairs[pair] = convolution(jets[pair[0]], jets[pair[1]])
        triples[factors] = convolution(pairs[pair], jets[factors[2]])
    columns = []
    for poly in EULER:
        columns.append([
            sum(coefficient * triples[factors][n]
                for factors, coefficient in poly.items()) % PRIME
            for n in range(ORDER + 1)
        ])
    return [[column[n] for column in columns] for n in range(ORDER + 1)]


def main():
    assert len(MONOMIALS) == 126
    assert all(PRIME % d for d in range(2, 1001))  # sqrt(PRIME)<1001
    relations = universal_relations()
    relation_basis, relation_indices, relation_pivots = {}, [], []
    for index, row in enumerate(relations):
        # Exact integer Euler identity, not just a modular check.
        poly = defaultdict(int)
        for coefficient, column in zip(row, EULER):
            for factors, value in column.items():
                poly[factors] += coefficient * value
        assert not clean(poly), ("nonzero Euler relation", index)
        pivot = add_row(relation_basis, row)
        if pivot is not None:
            relation_indices.append(index)
            relation_pivots.append(pivot)
    relation_minor = [[relations[i][j] for j in relation_pivots]
                      for i in relation_indices]
    relation_det, relation_diag, relation_swaps = minor_determinant(relation_minor)
    required = len(MONOMIALS) - len(relation_basis)
    basis, selected, rows, pivots, samples = {}, [], [], [], []
    for s in range(9):
        for n, row in enumerate(sampled_euler_series(s)):
            assert all(sum(a * b for a, b in zip(row, rel)) % PRIME == 0
                       for rel in relations)
            pivot = add_row(basis, row)
            if pivot is not None:
                selected.append({"s": s, "b_squared_order": n})
                rows.append(row)
                pivots.append(pivot)
            if len(basis) == required:
                break
        samples.append({"s": s, "rank": len(basis)})
        if len(basis) == required:
            break
    minor = [[row[j] for j in pivots] for row in rows]
    determinant, diagonal, swaps = minor_determinant(minor)
    passed = (len(relation_basis) == 45 and relation_det != 0
              and len(basis) == 81 and determinant != 0)
    certificate = {
        "method": "rational Taylor coefficients reduced modulo a prime",
        "prime": PRIME, "series_order": ORDER,
        "monomials": MONOMIALS, "coordinate_order": COORDS,
        "euler_columns": [
            [{"factors": factors, "coefficient": coefficient}
             for factors, coefficient in sorted(poly.items())] for poly in EULER
        ],
        "universal_relations": relations,
        "relation_certificate": {
            "rank": len(relation_basis), "selected_rows": relation_indices,
            "selected_columns": relation_pivots, "minor": relation_minor,
            "determinant_mod_prime": relation_det,
            "elimination_pivots": relation_diag, "row_swaps": relation_swaps,
            "exact_integer_euler_relations_verified": len(relations),
        },
        "pulse_certificate": {
            "rank": len(basis), "required": required,
            "selected_rows": selected, "selected_columns": pivots,
            "full_selected_rows_mod_prime": rows, "minor": minor,
            "determinant_mod_prime": determinant,
            "elimination_pivots": diagonal, "row_swaps": swaps,
            "samples": samples,
        },
        "passed": passed,
        "scope": "rank only; no occupation representation follows without analytic argument",
    }
    OUT.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({
        "passed": passed, "relation_rank": len(relation_basis),
        "required_relation_rank": 45, "pulse_rank": len(basis),
        "required_pulse_rank": 81, "relation_minor_det": relation_det,
        "pulse_minor_det": determinant, "samples": samples,
        "failures": [] if passed else ["rank target not attained"],
        "certificate": str(OUT),
    }))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
