#!/usr/bin/env python3
"""Supplementary rational checks; the all-index proof is in Lemma 73."""
from fractions import Fraction as Q


def cluster(n):
    x = Q(2**n)
    b = 1 - Q(1, 2**n)
    eps = Q(1, 2 * 8**n)
    d = Q(1, 2 * 4**n)
    return x, b, eps, d, d*d


checks = 0
for n in range(1, 31):
    x, b, eps, d, delta = cluster(n)
    eta = Q(5, 12) * eps
    c = b + delta
    best = c - eta*(x+d)**2
    assert best - (b-eta*x*x) == d*d*(1-Q(5, 12)*(2+eps)) > 0
    s = Q(0)
    e = Q(0)
    checks += 1
    for k in range(1, 46):
        u, h, _, gap, rise = cluster(k)
        for a, v in ((u, h), (u+gap, h+rise)):
            for sx in (-1, 1):
                for sy in (-1, 1):
                    score = sy*v - eta*a*a
                    is_max = k == n and a == u+gap and sy == 1
                    assert (score == best) if is_max else (score < best)
                    checks += 1
                    if sy*v > c:
                        assert k > n
                        horizontal = abs(sx*a-(x+d))
                        assert horizontal >= u/3
                        inverse = 1/(horizontal**2+(sy*v-c)**2)
                        s += inverse
                        e += 2*(sy*v-c)*inverse
                        checks += 2
    assert s <= 12*Q(1, 4**n)
    assert e <= 2*(1-c)*s <= 24*Q(1, 8**n)
    checks += 2
print(f'OK: {checks} exact satellite score and interaction checks.')
