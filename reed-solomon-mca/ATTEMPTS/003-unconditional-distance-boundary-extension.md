# Extending the r+1 count unconditionally to distance 3r

Tested 2026-09-25. L006 proves the exact count r+1 when minimum distance
exceeds 3r. The boundary test asked whether the same count survives at
distance exactly 3r, first encountered for three omissions at length 16
and dimension 8.

WHY IT FAILS: At equality, a nonzero codeword can be the affine discrepancy
of three disjoint sparse errors. The full
[boundary proof and construction](../lemmas/L007-minimum-distance-boundary-sharp-error.md)
give exactly five bad parameters, rather than four, on F_17^* over every
extension F_{17^s}. The construction uses five disjoint split fibers of a
cubic polynomial pencil and verifies failure on the same thirteen-coordinate
supports. This refutes the unconditional formula, not the challenge or
every boundary extension: the new dichotomy still proves the r+1 count
when floor(n/r)<=r+1. No claim is made that F_17 itself meets the
prescribed security budget; the exact threshold here is q>=5*2^128.
