#!/usr/bin/env python3
"""Exact checks of the sparse-product formulas; not an infinite-product certificate."""
from fractions import Fraction as Q

for n in range(1, 101):
    b = 1 - Q(1, 2**n)
    c = 1 - Q(1, 2**(n+1))
    assert 0 < b < c < 1
    delta = c - b
    assert 2 * delta / delta**2 == 2**(n+2)
    # Sum of the geometric tail in the four-factor growth bound.
    tail = Q(4, 3) * Q(1, 4**n)
    assert tail * (2**n)**2 == Q(4, 3)
    assert tail * (2**(n+1))**2 == Q(16, 3)
print('OK: 100 exact height/contribution and geometric-tail checks.')
