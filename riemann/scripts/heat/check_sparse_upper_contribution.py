"""Exact finite checks supplementing the analytic proof of Lemma 70."""
from fractions import Fraction as F

checks = 0
for n in range(1, 21):
    x, c = 2**n, 1 - F(1, 2**(n + 1))
    s = F(0)
    e = F(0)
    for m in range(1, n + 21):
        for h in (1 - F(1, 2**m), 1 - F(1, 2**(m + 1))):
            for a in (-2**m, 2**m):
                if h <= c:
                    continue
                assert m > n
                assert abs(x - a) >= F(2**m, 2)
                reciprocal = 1 / ((x - a)**2 + (c - h)**2)
                assert reciprocal <= 4 * F(1, 4**m)
                s += reciprocal
                e += 2 * (h - c) * reciprocal
                checks += 3
    assert 1 - F(1, 2**(n + 1)) == c  # b_(n+1) equals c_n
    assert s <= F(16, 3) / 4**n
    assert 0 <= e <= F(1, 2**n) * s <= F(16, 3) / 8**n
    checks += 3
print(f'Passed {checks} exact upper-cluster checks.')
