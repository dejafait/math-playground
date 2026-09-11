"""Finite exact-arithmetic checks; no distribution inference."""
from fractions import Fraction as F
from math import ceil, floor, gcd, isqrt
from random import Random


def endpoints(u, v, m, n, R):
    rho = F(1, isqrt(n))
    ap = 2*n*n-F(1, 4)
    am = ap-n*isqrt(n)
    lo = max(-R, ceil(am*am-m*m), ceil(-2*m*rho+rho*rho),
             u*n*n-m*m, u*v-m*m)
    hi = min(R, floor(ap*ap-m*m), floor(2*m*rho+rho*rho),
             4*u*n*n-m*m, u*(v+1)-m*m-1)
    return lo, hi, am, ap


def check(a, b, c, d, n):
    u, v = a*b, c*d
    R = n*isqrt(n)
    low = u*v-R
    k = isqrt(low)
    k += k*k < low
    # Enumerate a deliberately larger m interval independently of k.
    root = isqrt(u*v)
    possible = [m for m in range(root-3, root+5)
                if low <= m*m <= u*(v+1)+R-1]
    assert len(possible) <= 1
    assert not possible or possible == [k]
    total = 0
    for m in range(root-3, root+5):
        lo, hi, am, ap = endpoints(u, v, m, n, R)
        if am <= m <= ap and gcd(m, u) == 1:
            total += max(hi-lo, 0)
    lo, hi, am, ap = endpoints(u, v, k, n, R)
    single = max(hi-lo, 0) if am <= k <= ap and gcd(k, u) == 1 else 0
    assert total == single
    if root*root == u*v:
        assert k == root and gcd(k, u) > 1 and total == 0
    return total > 0, root*root == u*v


rng = Random(218)
occupied = squares = count = 0
for n in (100, 144, 400, 900):
    left, right = ceil(F(8*n, 5)), floor(F(17*n, 10))
    tuples = [(rng.randint(n, 2*n), rng.randint(n, 2*n),
               rng.randint(left, right), rng.randint(left, right))
              for _ in range(3000)]
    tuples += [(a, a, c, c) for a in range(n, 2*n+1, max(1, n//20))
               for c in range(left, right+1, max(1, n//100))]
    for factors in tuples:
        hit, square = check(*factors, n)
        occupied += hit
        squares += square
        count += 1
assert occupied and squares
print(f'Passed {count} exact checks; {occupied} occupied and {squares} square cases.')
