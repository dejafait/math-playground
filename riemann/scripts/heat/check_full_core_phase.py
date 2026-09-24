#!/usr/bin/env python3
"""Exact finite checks of L201; no asymptotic counting inference."""
from fractions import Fraction as F
from math import isqrt
from random import Random

rng = Random(201)
occupied = expansions = 0
for _ in range(10000):
    j = rng.randint(4, 25)
    n = j*j
    u = rng.randint(n*n, 4*n*n)
    v = 2*n*n + rng.randint(-j**3, j**3)
    w = rng.randint(1, j**3)
    rho = F(1, j)
    candidate = isqrt(u*v) + 1
    amin = F(candidate + rng.randint(-2, 2), 1) + F(rng.randint(0, 2), 3)
    amax = amin + rng.randint(0, 5)

    def original(m):
        # Unrounded endpoint inequalities for b <= -W and t >= W;
        # take R=W. Check both rho inequalities independently.
        return (amin**2-m*m <= -w and -2*m*rho+rho*rho <= -w
                and u*n*n-m*m <= -w and u*v-m*m <= -w
                and amax**2-m*m >= w and 2*m*rho+rho*rho >= w
                and 4*u*n*n-m*m >= w and u*(v+1)-m*m-1 >= w)

    actual = [m for m in range(isqrt(u*v), isqrt(u*(v+1)-1)+1)
              if original(m)]
    m = candidate
    delta = m*m-u*v  # exactly 2*x*g+g*g
    criterion = (w <= delta <= u-1-w
                 and amin**2+w <= m*m <= amax**2-w
                 and u*n*n+w <= m*m <= 4*u*n*n-w
                 and 2*m*rho-rho*rho >= w)
    assert actual == ([candidate] if criterion else [])
    occupied += bool(actual)

    s, k = u+v, u-v
    if 2*k*k <= s*s:
        q = F(s, 2)-F(k*k, 4*s)-F(k**4, 16*s**3)
        bound = F(k**6, s**5)
        assert q >= 0 and q*q >= u*v
        # q-bound <= sqrt(uv) <= q, checked without floating point.
        assert q-bound <= 0 or (q-bound)**2 <= u*v
        expansions += 1
print(f'Passed 10000 exact candidate checks ({occupied} occupied), '
      f'{expansions} rational Taylor bounds.')
