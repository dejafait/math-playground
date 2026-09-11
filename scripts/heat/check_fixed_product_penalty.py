#!/usr/bin/env python3
"""Supplementary exact checks; the infinite proof is in Lemma 72."""
from fractions import Fraction as Q


def cluster(n):
    x = Q(2**n)
    b = 1-Q(1, 2**n)
    eps = Q(1, 2*8**n)
    d = Q(1, 2*4**n)
    return x, b, eps, d, d*d


checks = 0
for n in range(1, 41):
    x, b, eps, d, delta = cluster(n)
    m = b-eps*x*x
    assert d == eps*x
    assert m == 1-Q(3, 2)*Q(1, 2**n)
    assert 0 < b < b+delta < 1-Q(3, 4)*Q(1, 2**n)
    assert x+d < 2*x
    assert delta-eps*(2*x*d+d*d) == -d*d*(1+eps)
    assert 2*delta/(d*d+delta*delta) == 2/(1+d*d) > 1
    checks += 6
    for k in range(1, 61):
        u, h, _, gap, rise = cluster(k)
        for a, v in ((u, h), (u+gap, h+rise)):
            for sx in (-1, 1):
                for sy in (-1, 1):
                    score = sy*v-eps*(sx*a)**2
                    expected_max = k == n and a == u and sy == 1
                    assert (score == m) if expected_max else (score < m)
                    checks += 1
print(f'OK: {checks} exact construction and score checks.')
