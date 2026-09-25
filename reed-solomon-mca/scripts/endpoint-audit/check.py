"""Exact auxiliary checks for C001a and L002, not a finite-field enumeration."""

from itertools import combinations
from math import comb


q = 5**56
budget_denominator = 2**128
assert budget_denominator < q < 6 * budget_denominator
assert (q - 1) % 16 == 0
assert q > 2 * (5**3 - 1)
assert 5**7 > 2**16
assert 5**8 < 6 * 2**16
assert 6**7 < 5**8

# Coefficients in 1, X, X^2 over F_5 for 0, 1, X, X^2.
xs = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))
assert len(set(xs)) == 4
pair_sums = {
    tuple((a + b) % 5 for a, b in zip(x, y))
    for x, y in combinations(xs, 2)
}
assert len(pair_sums) == 6

# L002: this sufficient bound makes every radius safe for the larger field.
q_larger = 5**60
assert comb(16, 2) == 120
assert q_larger > comb(16, 2) * budget_denominator
assert (q_larger - 1) % 16 == 0

print("PASS: 2^128 < 5^56 < 6*2^128; 16 divides 5^56-1.")
print("PASS: field size exceeds the quadratic-root union bound.")
print("PASS: four distinct polynomial vectors have six distinct pair sums over F_5.")
print("PASS: 120*2^128 < 5^60; 16 divides 5^60-1 (L002).")
