#!/usr/bin/env python3
"""Replay the pulse certificate using a separate product rule and finite sums."""

import itertools
import json
import math
from collections import defaultdict
from pathlib import Path

DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / "pulse-rank-certificate.json"
OUTPUT = DIRECTORY / "pulse-rank-verification.json"


def direct_euler(m, coordinates):
    result = defaultdict(int)
    occurrences = [tuple(coord) for coord, count in zip(coordinates, m)
                   for _ in range(count)]
    for removed in range(4):
        r, j = occurrences[removed]
        remaining = [a for i, a in enumerate(occurrences) if i != removed]
        for allocation in itertools.product(range(j + 1), repeat=3):
            if sum(allocation) != j:
                continue
            coefficient = (-1) ** j * math.factorial(j)
            for amount in allocation:
                coefficient //= math.factorial(amount)
            factors = tuple(sorted((rr - r, jj + amount)
                                   for (rr, jj), amount in zip(remaining, allocation)))
            result[factors] += coefficient
    return {factors: value for factors, value in result.items() if value}


def inverse_and_check(matrix, p):
    n = len(matrix)
    augmented = [[value % p for value in row]
                 + [int(i == j) for j in range(n)]
                 for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = next(i for i in range(column, n) if augmented[i][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = pow(augmented[column][column], -1, p)
        augmented[column] = [value * scale % p for value in augmented[column]]
        for i in range(n):
            if i != column:
                factor = augmented[i][column]
                augmented[i] = [(a - factor * b) % p
                                for a, b in zip(augmented[i], augmented[column])]
    inverse = [row[n:] for row in augmented]
    assert all(augmented[i][j] == int(i == j)
               for i in range(n) for j in range(n))
    assert all(sum(matrix[i][k] * inverse[k][j] for k in range(n)) % p == int(i == j)
               for i in range(n) for j in range(n))
    return inverse


def main():
    data = json.loads(SOURCE.read_text())
    p = data["prime"]
    assert p == 1000003 and all(p % d for d in range(2, math.isqrt(p) + 1))
    order = data["series_order"]
    assert 2 * order + 3 < p
    monomials, coordinates = data["monomials"], data["coordinate_order"]
    assert len(monomials) == len({tuple(m) for m in monomials}) == 126
    assert all(len(m) == 6 and min(m) >= 0 and sum(m) == 4 for m in monomials)
    assert coordinates == [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]]
    euler = [direct_euler(m, coordinates) for m in monomials]
    for actual, recorded in zip(euler, data["euler_columns"]):
        assert actual == {tuple(tuple(f) for f in term["factors"]): term["coefficient"]
                          for term in recorded}

    # Rebuild all 50 universal rows without importing the generator.
    index = {tuple(m): i for i, m in enumerate(monomials)}
    relations = []
    for m in monomials:
        if m[2] == m[5] == 0:
            row = [0] * 126
            for a in (0, 1, 3, 4):
                if m[a]:
                    v = list(m)
                    v[a] -= 1
                    v[a + 1] += 1
                    row[index[tuple(v)]] += m[a]
            relations.append(row)
    for m in monomials:
        if sum(m[3:]) == 0:
            row = [0] * 126
            row[index[tuple(m)]] = 1
            row[index[(0, 0, 0) + tuple(m[:3])]] = -1
            relations.append(row)
    assert relations == data["universal_relations"]
    assert len(relations) == 50
    for row in relations:
        polynomial = defaultdict(int)
        for c, column in zip(row, euler):
            for factors, value in column.items():
                polynomial[factors] += c * value
        assert not any(polynomial.values())

    # Coefficients of a triple product, summed directly over n1+n2+n3=N.
    # Differentiate t^(2n) by its integer falling factorial; divide by
    # (2n+1)!, independently of the generator's simplified denominator.
    jet_cache, triple_cache = {}, {}

    def jet(n, derivative, t):
        key = (n, derivative, t)
        if key not in jet_cache:
            if 2 * n < derivative:
                value = 0
            else:
                falling = math.prod(range(2 * n - derivative + 1, 2 * n + 1))
                value = ((-1) ** n * falling * pow(t, 2 * n - derivative, p)
                         * pow(math.factorial(2 * n + 1) % p, -1, p)) % p
            jet_cache[key] = value
        return jet_cache[key]

    def triple(factors, s, total):
        key = (factors, s, total)
        if key not in triple_cache:
            (r1, j1), (r2, j2), (r3, j3) = factors
            value = 0
            for n1 in range(total + 1):
                for n2 in range(total - n1 + 1):
                    n3 = total - n1 - n2
                    value += (jet(n1, j1, s + r1) * jet(n2, j2, s + r2)
                              * jet(n3, j3, s + r3))
            triple_cache[key] = value % p
        return triple_cache[key]

    pc = data["pulse_certificate"]
    rebuilt = []
    for selection in pc["selected_rows"]:
        s, total = selection["s"], selection["b_squared_order"]
        rebuilt.append([
            sum(c * triple(factors, s, total) for factors, c in column.items()) % p
            for column in euler
        ])
    assert rebuilt == pc["full_selected_rows_mod_prime"]
    pulse_minor = [[row[j] for j in pc["selected_columns"]] for row in rebuilt]
    assert pulse_minor == pc["minor"]
    assert len(pulse_minor) == 81 and all(len(row) == 81 for row in pulse_minor)
    pulse_inverse = inverse_and_check(pulse_minor, p)
    rc = data["relation_certificate"]
    relation_minor = [[relations[i][j] for j in rc["selected_columns"]]
                      for i in rc["selected_rows"]]
    assert relation_minor == rc["minor"]
    assert len(relation_minor) == 45 and all(len(row) == 45 for row in relation_minor)
    relation_inverse = inverse_and_check(relation_minor, p)
    result = {
        "passed": True, "prime": p,
        "regenerated_euler_columns": len(euler),
        "exact_universal_relations": len(relations),
        "regenerated_pulse_entries": len(rebuilt) * len(monomials),
        "required_pulse_entries": 81 * 126,
        "pulse_minor_size": 81, "required_pulse_minor_size": 81,
        "relation_minor_size": 45, "required_relation_minor_size": 45,
        "pulse_inverse_mod_prime": pulse_inverse,
        "relation_inverse_mod_prime": relation_inverse,
        "both_inverse_products_checked_entrywise": True, "failures": [],
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items()
                      if key not in ("pulse_inverse_mod_prime", "relation_inverse_mod_prime")}
                     | {"certificate": str(OUTPUT)}))


if __name__ == "__main__":
    main()
