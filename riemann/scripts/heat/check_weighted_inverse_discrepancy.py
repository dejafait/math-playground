#!/usr/bin/env python3
"""Exact finite algebra checks; no asymptotic distribution claim."""
from fractions import Fraction as F
from math import gcd


def mu(n):
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def ratio(n):
    return F(sum(gcd(j, n) == 1 for j in range(1, n + 1)), n)


checks = occupied = 0
for a in range(2, 7):
    for v in range(3, 8):
        for m in range(2, 16):
            left, right, R = F(2), F(7), F(3)
            A, B = -R, R

            def f(x):
                return max(min(B, a * (v + 1) * x - m*m - 1)
                           - max(A, a * v * x - m*m), 0) / R

            # All envelope switches and all potential zero crossings.
            lines = [(F(0), A), (F(a*v), F(-m*m)),
                     (F(0), B), (F(a*(v+1)), F(-m*m-1))]
            knots = {left, right}
            for s, t in lines:
                for u, w in lines:
                    if s != u:
                        x = (w-t)/(s-u)
                        if left < x < right:
                            knots.add(x)
            knots = sorted(knots)
            integral = sum((y-x)*(f(x)+f(y))/2
                           for x, y in zip(knots, knots[1:]))
            values = {b: f(F(b)) for b in range(2, 8)}
            direct = sum(ratio(a*b)*z for b, z in values.items()
                         if gcd(m, a*b) == 1)
            main = error = F(0)
            if gcd(a, m) == 1:
                divisors = [j for j in range(1, m+1) if m % j == 0]
                sk = sum(F(mu(k), k*k) for k in range(1, 8)
                         if gcd(k, a*m) == 1)
                assert F(1, 4) <= sk <= F(7, 4)
                main = ratio(a)*ratio(m)*sk*integral
                for k in range(1, 8):
                    if gcd(k, a*m) != 1:
                        continue
                    for j in divisors:
                        delta = sum(z for b, z in values.items()
                                    if b % (j*k) == 0) - integral/(j*k)
                        assert abs(delta) <= 8
                        error += ratio(a)*F(mu(k)*mu(j), k)*delta
            assert direct == main + error, (a, v, m)
            checks += 1
            occupied += direct > 0
print(f'Passed {checks} exact weighted identities ({occupied} positive sums).')
