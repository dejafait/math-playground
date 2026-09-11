"""Exact rational regression checks for L191; no asymptotic inference."""
from fractions import Fraction as F
from math import ceil, floor, gcd


def mu(n):
    sign = 1
    p = 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def inverted(u, b, t, alpha, beta):
    value = F(0)
    for d in range(1, u+1):
        if u % d:
            continue
        lo, hi = ceil(F(b, d)), floor(F(t, d))
        if lo > hi:
            continue
        count = hi-lo+1-int(lo <= 0 <= hi)
        moment = F((lo+hi)*(hi-lo+1), 2)
        value += mu(d)*(alpha*count+beta*d*moment)
    return value


intervals = endpoints = 0
flags = set()
for n in (2, 3):
    rho = F(1, 2)
    R = F(4*n*n)+F(1, 3)
    for amin, amax in [(F(n*n), F(4*n*n)),
                        (F(2*n*n)+F(1, 2), F(2*n*n)+F(3, 2)),
                        (F(n*n+2), F(n*n))]:
        for u in range(n*n, 4*n*n+1):
            for m in range(1, 4*n*n+3):
                if not amin-rho <= m <= amax+rho or gcd(m, u) != 1:
                    continue
                for v in range(n*n, 4*n*n+1):
                    b = max(ceil(-R), ceil(amin**2-m*m),
                            ceil(-2*m*rho+rho**2), u*n*n-m*m, u*v-m*m)
                    t = min(floor(R), floor(amax**2-m*m),
                            floor(2*m*rho+rho**2), 4*u*n*n-m*m,
                            u*(v+1)-m*m-1)
                    original = []
                    for r in range(ceil(-R), floor(R)+1):
                        k = m*m+r
                        valid = (amin**2 <= k <= amax**2
                                 and u*n*n <= k <= 4*u*n*n
                                 and abs(r-rho**2) <= 2*m*rho)
                        if valid and k == u*(v+1):
                            flags.add('strict')
                        if valid and u*v <= k < u*(v+1):
                            original.append(r)
                            if k == 4*u*n*n:
                                flags.add('closed')
                    assert original == list(range(b, t+1))
                    if b > t:
                        flags.add('empty')
                    alpha, beta = F((-1)**m, 3), F(m+1, u+1)
                    direct = sum((alpha+beta*r for r in original
                                  if r and gcd(r, u) == 1), F(0))
                    assert direct == inverted(u, b, t, alpha, beta)
                    intervals += 1
# Exhaust zero-crossing, singleton and reversed intervals, including modulus 1.
for u in range(1, 25):
    for b in range(-12, 13):
        for t in range(-12, 13):
            direct = sum((F(2, 3)-F(5, 7)*r for r in range(b, t+1)
                          if r and gcd(r, u) == 1), F(0))
            assert direct == inverted(u, b, t, F(2, 3), -F(5, 7))
            endpoints += 1
assert flags == {'strict', 'closed', 'empty'}, flags
print(f'Passed {intervals} exact interval checks and {endpoints} signed Möbius checks; {sorted(flags)}.')
