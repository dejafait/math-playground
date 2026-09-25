"""Exact auxiliary checks for L009; no external packages or random search."""

from collections import defaultdict
from itertools import combinations, permutations
from math import comb


P = 97
H = tuple(pow(8, i, P) for i in range(16))


def nullspace(rows, columns):
    rows = [list(row) for row in rows]
    pivots = []
    height = 0
    for column in range(columns):
        pivot = next(
            (i for i in range(height, len(rows)) if rows[i][column]), None
        )
        if pivot is None:
            continue
        rows[height], rows[pivot] = rows[pivot], rows[height]
        scale = pow(rows[height][column], -1, P)
        rows[height] = [value * scale % P for value in rows[height]]
        for i in range(len(rows)):
            if i != height and rows[i][column]:
                scale = rows[i][column]
                rows[i] = [
                    (a - scale * b) % P for a, b in zip(rows[i], rows[height])
                ]
        pivots.append(column)
        height += 1
        if height == len(rows):
            break
    free = [j for j in range(columns) if j not in pivots]
    return [
        tuple(
            -rows[pivots.index(j)][f] % P
            if j in pivots else int(j == f)
            for j in range(columns)
        )
        for f in free
    ]


def determinant_polynomial(u, v):
    """Coefficients indexed by (X degree, c degree), over the integers."""
    result = defaultdict(int)
    for permutation in permutations(range(5)):
        if any(i + permutation[i] + 1 not in (u, v) for i in range(4)):
            continue
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(5) for j in range(i + 1, 5)
        )
        c_degree = sum(i + permutation[i] + 1 == v for i in range(4))
        result[permutation[4], c_degree] += (-1) ** inversions
    return {key: value for key, value in result.items() if value}


def check_determinants():
    expected = {
        (1, 5): {(4, 3): -1, (0, 4): 1},
        (2, 5): {(3, 3): -1, (0, 4): 1},
        (2, 6): {(4, 2): 1, (0, 3): -1},
        (3, 5): {(4, 2): 1, (2, 3): -1, (0, 4): 1},
        (3, 6): {},
        (3, 7): {(4, 1): -1, (0, 2): 1},
        (4, 5): {(4, 0): 1, (3, 1): -1, (2, 2): 1, (1, 3): -1, (0, 4): 1},
        (4, 6): {(4, 0): 1, (2, 1): -1, (0, 2): 1},
        (4, 7): {(4, 0): 1, (1, 1): -1},
        (4, 8): {(4, 0): 1, (0, 1): -1},
    }
    admissible = {
        (u, v) for u, v in combinations(range(1, 9), 2)
        if u <= 4 and v >= 5 and v - u <= 4
    }
    assert set(expected) == admissible
    for pair, coefficients in expected.items():
        assert determinant_polynomial(*pair) == coefficients, pair
    print("PASS: all ten locator determinant identities over the integers.")


def check_supports():
    assert len(set(H)) == 16 and pow(8, 16, P) == 1 and pow(8, 8, P) != 1
    fourth_roots = {x for x in H if pow(x, 4, P) == 1}
    cosets = {frozenset(a * x % P for x in fourth_roots) for a in H}
    assert len(fourth_roots) == len(cosets) == 4
    powers = {x: tuple(pow(x, j, P) for j in range(1, 9)) for x in H}
    total = 0
    for u, v in combinations(range(1, 9), 2):
        hits = set()
        for support in combinations(H, 4):
            rows = [
                [powers[x][j - 1] for x in support]
                for j in range(1, 9) if j not in (u, v)
            ]
            basis = nullspace(rows, 4)
            total += 1
            if not basis:
                continue
            assert len(basis) == 1
            weights = basis[0]
            assert all(weights)
            actual = tuple(
                sum(value * powers[x][j - 1] for x, value in zip(support, weights)) % P
                for j in range(1, 9)
            )
            assert {j for j, value in enumerate(actual, 1) if value} == {u, v}
            assert len({value * pow(x, u, P) % P for x, value in zip(support, weights)}) == 1
            directions = {
                actual[v - 1] * pow(t, v, P)
                * pow(actual[u - 1] * pow(t, u, P) % P, -1, P) % P
                for t in H
            }
            assert len(directions) == 4
            hits.add(frozenset(support))
        expected = cosets if v == u + 4 else set()
        assert hits == expected, ((u, v), hits)
        if hits:
            print(f"PASS: moments {(u, v)}: exactly four cosets; each orbit has four directions.")
    assert total == comb(8, 2) * comb(16, 4) == 50960
    print(f"PASS: {total} moment-pair/support systems; no other nonzero kernel.")


def main():
    check_determinants()
    check_supports()
    assert 15 * 2**128 <= 97**20 < 16 * 2**128
    assert 97**20 // 2**128 == 15
    assert comb(16, 9) // comb(11, 8) == 69
    print("PASS: q=97^20 permits fifteen bad challenges; the required witness has sixteen.")
    print("The orbit bound four leaves the general bounds 10/q and 69/q unchanged.")
    print("This finite check is not a maximization over affine lines or a challenge resolution.")


if __name__ == "__main__":
    main()
