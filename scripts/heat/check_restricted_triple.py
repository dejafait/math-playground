"""Exact finite regression for the margin surjection in L163."""
from itertools import product
from collections import defaultdict
from math import prod


def factors(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def matrix(rows, cols):
    rf, cf = [factors(n) for n in rows], [factors(n) for n in cols]
    x = [[1] * 3 for _ in range(3)]
    for p in factors(prod(rows)):
        r = [f.get(p, 0) for f in rf]
        c = [f.get(p, 0) for f in cf]
        for i in range(3):
            for j in range(3):
                v = min(r[i], c[j])
                x[i][j] *= p ** v
                r[i] -= v
                c[j] -= v
        assert r == c == [0, 0, 0]
    return x


checked = 0
for lo, hi in [(1, 1), (1, 6), (2, 9), (5, 12)]:
    groups = defaultdict(list)
    for triple in product(range(lo, hi + 1), repeat=3):
        groups[prod(triple)].append(triple)
    for triples in groups.values():
        for rows, cols in product(triples, repeat=2):
            x = matrix(rows, cols)
            assert tuple(map(prod, x)) == rows
            assert tuple(prod(x[i][j] for i in range(3)) for j in range(3)) == cols
            e = [[v.bit_length() - 1 for v in row] for row in x]
            assert 2 ** sum(map(sum, e)) <= hi ** 3
            checked += 1
print(f'Passed {checked} equal-product margin constructions.')
