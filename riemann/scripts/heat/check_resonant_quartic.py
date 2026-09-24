"""Exact finite regression for L159; no numerical zeta claims."""
from collections import defaultdict
from itertools import product

for indices in ([], [2], list(range(1, 9)), list(range(4, 13))):
    amplitudes = {n: n * n + 1 for n in indices}
    products = defaultdict(int)
    for r, m in product(indices, repeat=2):
        products[r * m] += amplitudes[r] * amplitudes[m]
    full = sum(v * v for v in products.values())
    diagonal = sum(v * v for v in amplitudes.values()) ** 2
    resonant = 0
    for r, s, m, n in product(indices, repeat=4):
        if r * m == s * n:
            assert (r == s) == (m == n)
            if r != s and m != n:
                resonant += amplitudes[r] * amplitudes[s] * amplitudes[m] * amplitudes[n]
    assert resonant == full - diagonal
    assert resonant >= 0
print('PASS: exact resonant regrouping, exclusions, and positivity (4 windows)')
