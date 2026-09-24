"""Exact finite checks of L225; no distribution or asymptotic claim."""
from math import gcd, isqrt
from fractions import Fraction

checks = crossings = 0
# General integral squared endpoints exercise strict lower/upper boundaries.
for lower in range(1, 250):
    for upper in range(lower + 1, lower + 25):
        # sqrt(upper)-sqrt(lower)<1, tested without floating point.
        if upper - lower - 1 >= 0 and (upper - lower - 1)**2 >= 4*lower:
            continue
        k = isqrt(lower) + 1
        direct = [m for m in range(isqrt(lower), isqrt(upper)+2)
                  if lower < m*m < upper]
        assert direct == ([k] if k*k < upper else [])
        crossings += int(isqrt(lower)**2 == lower or isqrt(upper)**2 == upper)
        checks += 1

# Exact overlap and reindexing in short cells, with rounded integer cutoffs.
weighted = 0
for a in range(2, 9):
    for v in range(50, 61):
        for R in range(1, 5):
            for offset in range(3):
                bset = range(10, 21)
                j0, j1 = isqrt(a*v*10)-offset, isqrt(a*(v+1)*20)+offset
                def weight(m, b):
                    A, B = -R + m % 2, R - m % 3
                    return Fraction(max(0, min(B, a*(v+1)*b-m*m-1)
                                        - max(A, a*v*b-m*m)), R)
                direct = sum((weight(m,b) for m in range(j0,j1+1)
                              if gcd(a,m)==1 for b in bset), Fraction(0))
                candidate = Fraction(0)
                for b in bset:
                    lower, upper = a*v*b-R, a*(v+1)*b+R-1
                    assert (upper-lower-1)**2 < 4*lower
                    k = isqrt(lower)+1
                    delta = k*k-lower  # exactly 2 alpha theta + theta squared
                    if j0 <= k <= j1 and gcd(a,k)==1 and k*k < upper:
                        A, B = -R+k%2, R-k%3
                        candidate += Fraction(max(0,min(B,a*b+R-1-delta)
                                                   -max(A,R-delta)),R)
                assert direct == candidate, (a,v,R,offset,direct,candidate)
                weighted += 1
assert crossings > 0
print(f'Passed {checks} cell checks ({crossings} square-endpoint cases) '
      f'and {weighted} exact weighted reindexings.')
