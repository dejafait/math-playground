"""Finite exact checks for L200; no asymptotic inference."""
from math import isqrt

cases = 0
occupied = 0
for u in range(1, 101):
    for v in range(1, 101):
        s, k = u + v, u - v
        e = s % 2
        assert 4 * ((s // 2) ** 2 - u * v) == k * k - e * (2 * s - 1)
        for w in (1, 2, 5, 10, 25):
            lo, hi = u * v + w, u * (v + 1) - 1 - w
            first = isqrt(lo)
            if first * first < lo:
                first += 1
            if first * first <= hi:
                occupied += 1
                assert first <= s // 2
                assert k * k >= 4 * w + e * (2 * s - 1)
            cases += 1
assert occupied > 0
print(f'Passed {cases:,} exact cases; {occupied:,} occupied floor-cell windows.')
