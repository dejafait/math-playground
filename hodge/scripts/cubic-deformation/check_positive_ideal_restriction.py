#!/usr/bin/env python3
"""Check L020's coefficient ranks in characteristic 43.

This checks the displayed Laurent-polynomial calculation in finite cases.
The lemma proves the complex ranks for all parameters and degrees; this
script does not check geometric poles, cohomology, or descent.
"""

from functools import lru_cache


PRIME = 43
ZETA = next(z for z in range(2, PRIME) if pow(z, 7, PRIME) == 1)
assert ZETA != 1


def multiply(left, right):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            result[i + j] = (result.get(i + j, 0) + a * b) % PRIME
    return {i: a for i, a in result.items() if a}


@lru_cache(None)
def power(which, degree):
    base = {1: 1, -1: 1} if which == "t" else {
        1: ZETA, -1: pow(ZETA, -1, PRIME)
    }
    result = {0: 1}
    for _ in range(degree):
        result = multiply(result, base)
    return result


@lru_cache(None)
def rectangle(a, b):
    return tuple(
        multiply(power("t", i), power("s", j))
        for i in range(a + 1) for j in range(b + 1)
    )


def rank(vectors, bound):
    pivots = {}
    for polynomial in vectors:
        row = [polynomial.get(i, 0) for i in range(-bound, bound + 1)]
        for column in range(len(row)):
            if not row[column]:
                continue
            if column in pivots:
                scale = row[column]
                row = [(x - scale * y) % PRIME
                       for x, y in zip(row, pivots[column])]
            else:
                inverse = pow(row[column], -1, PRIME)
                pivots[column] = [x * inverse % PRIME for x in row]
                break
    return len(pivots)


def coefficient_rank(b, r, k, odd):
    pairs = [(i, k - i) for i in range(r + 1)
             if 0 <= k - i <= r
             and (not odd or max(i, k - i) >= 2)]
    vectors = []
    for i, j in pairs:
        a, c = r * b - 2 * i, r * b - 2 * j
        assert min(a, c) >= 1
        vectors.extend(rectangle(a, c))
    return rank(vectors, 2 * r * b - 2 * k)


def main():
    for a, b in [(1, 1), (1, 5), (2, 3), (7, 7), (8, 2)]:
        vectors = rectangle(a, b)
        bound = a + b
        factor = pow(ZETA, -2 * b, PRIME)
        assert all((v.get(-bound, 0) - factor * v.get(bound, 0))
                   % PRIME == 0 for v in vectors)
        assert rank(vectors, bound) == 2 * bound

    for b, r in [(3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (7, 1), (7, 2)]:
        total = 0
        for k in range(2 * r + 1):
            actual = coefficient_rank(b, r, k, odd=False)
            expected = 2 * (2 * r * b - 2 * k) + 1
            if k in (0, 2 * r):
                expected -= 1
            assert actual == expected, (b, r, k, "even", actual, expected)
            total += actual
        if r >= 2:
            for k in range(2, 2 * r + 1):
                actual = coefficient_rank(b, r, k, odd=True)
                expected = 2 * (2 * r * b - 2 * k) + 1 - (k == 2 * r)
                assert actual == expected, (b, r, k, "odd", actual, expected)
                total += actual
        square = 4 * b - 4
        target = 1 + 4 * r * r * square - 4 * r
        cokernel = target - total
        assert cokernel == (square - 4 if r == 1 else 0)
        print(f"b={b}, r={r}: image={total}, target={target}, cokernel={cokernel}")
    print(f"PASS: coefficient checks over F_{PRIME}, zeta={ZETA}; geometric claims require the proof.")


if __name__ == "__main__":
    main()
