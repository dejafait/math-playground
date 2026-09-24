"""Exact arithmetic checks for L210; no population simulation."""
from fractions import Fraction

z = 65536
m = (z - 2) // 2
assert 2 * m + 1 == z - 1
# Squared lower bound for phi(D)/D exceeds (1/512)^2.
assert Fraction(1, 4 * (2 * m + 1)) > Fraction(1, 512**2)
assert Fraction(3, 128) * Fraction(1, 512) == Fraction(3, z)
assert Fraction(2, z) + Fraction(1, z) == Fraction(3, z)
# Each factor's squared comparison is equivalent to this exact identity.
for j in range(1, m + 1):
    assert 4 * j * j - (2 * j - 1) * (2 * j + 1) == 1
print("L210 rational constant and factor checks passed")
