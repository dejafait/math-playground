"""Exact finite algebra checks; no evidence about RH is inferred."""
from fractions import Fraction as F
from collections import defaultdict

freq = [F(0), F(1, 101), F(1)]
raw, sym = defaultdict(F), defaultdict(F)
for r in range(3):
    for s in range(3):
        if r == s:
            continue
        for m in range(3):
            for n in range(3):
                if m == n:
                    continue
                x, y = freq[r] - freq[s], freq[m] - freq[n]
                key = (tuple(sorted((r, m))), tuple(sorted((s, n))))
                raw[key] += x / y
                sym[key] += (x / y + y / x) / 2
                assert (x / y + y / x) / 2 == (x + y)**2 / (2*x*y) - 1
assert raw == sym
assert raw[((0, 0), (1, 2))] == F(101) + F(1, 101)
print('Exact quartic symmetrization and monomial coefficient checks passed.')
