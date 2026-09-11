"""Exact finite regression for L162; no asymptotic certificate."""
from collections import defaultdict
from itertools import product
from math import comb


def diagonal(indices, weights, degree):
    buckets = defaultdict(int)
    for factors in product(indices, repeat=degree):
        key = mass = 1
        for n in factors:
            key *= n
            mass *= weights[n]
        buckets[key] += mass
    return sum(v * v for v in buckets.values())


cases = [[], [1], [1, 2], [1, 2, 3], [1, 2, 4],
         [2, 3, 4, 6], [1, 2, 3, 4, 6]]
checks = 0
for indices in cases:
    for weights in ({n: 1 for n in indices},
                    {n: n % 3 for n in indices},
                    {n: n + 1 for n in indices}):
        s = sum(v * v for v in weights.values())
        d2 = diagonal(indices, weights, 2)
        d3 = diagonal(indices, weights, 3)
        w = 0
        for a, b, r, s2, m, n in product(indices, repeat=6):
            if a != b and r != s2 and m != n and a*r*m == b*s2*n:
                w += weights[a]*weights[b]*weights[r]*weights[s2]*weights[m]*weights[n]
        assert w == d3 - 3*s*d2 + 2*s**3
        assert 0 <= w <= d3
        checks += 1
for e in range(101):
    assert comb(e + 2, 2)**2 <= comb(e + 8, 8)
print(f'PASS: {checks} exact weighted cases; 101 local divisor checks')
