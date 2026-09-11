# Restricted triple diagonal checkpoint — 2026-09-13

L162 is complete; no interrupted proof needs recovery. Proposed improvement:
every equal-product pair of triples is the row/column product margins of a
positive integer 3-by-3 matrix, by primewise exponent transportation.
Keeping every margin in [aN,bN], dyadic exponents have all row/column sums
in an interval of bounded width about log2 N. Choose the top-left four
exponents freely (O(log N)^4 choices); the other five have boundedly many
choices. Each box has at most C N^3 integer matrices, since the total
exponent sum is at most 3 log2(bN). This should give D3=O(log N)^4.

Resume: verify the surjection and five constrained exponents, state explicit
counting constants and small-N assumptions, then check finite examples.
The improvement and any tail consequence are unproved at this checkpoint.

Completed as L163: the finite matrix count proves the fourth-power bound.
The regression passed 9,647 margin constructions. Sharpness and uniform
cutoff control remain unproved.
