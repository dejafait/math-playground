"""Exact finite checks supporting the general identities proved in L127."""
from fractions import Fraction
from math import factorial


def polynomial(n):
    return {n - 2*j: Fraction(factorial(n)*(-1)**j,
                            factorial(j)*factorial(n-2*j))
            for j in range(n//2+1)}


for m in range(2, 31):
    p, prev, nxt = polynomial(m), polynomial(m-1), polynomial(m+1)
    derivative = {k-1: k*v for k, v in p.items() if k}
    assert derivative == {k: m*v for k, v in prev.items()}
    # P_(m+1) + 2 P_m' = v P_m: root evaluation gives beta=2A.
    for k in range(m+2):
        assert nxt.get(k, 0) + 2*derivative.get(k, 0) == p.get(k-1, 0)
print('Exact multiple-zero coefficient identities passed for m=2,...,30.')
