# Frozen third moment audit — 2026-09-13

The L171 step is complete; earlier changes are preserved. Scope here:
test interpolation as a route to the requested uniform third moment.
For Y=|Z_j|, Cauchy–Schwarz gives E Y³ ≤ (E Y² E Y⁴)^(1/2),
so the available upper bound grows as T^(1/8)sqrt(log T).
Candidate sharpness model: with B=T^(1/4)log T, take Y=sqrt(B)
with probability 1/B and zero otherwise. Then its second, third,
and fourth moments are 1, sqrt(B), B. This is an abstract model only.
A complementary Cauchy–Schwarz inequality gives
E Y³ ≥ (E Y²)²/E Y. A vanishing first absolute moment along any
actual block sequence would therefore refute the uniform third-moment
proposal, and would also refute uniform integrability of Y².

Resume by auditing both inequalities, proving the last integrability
implication using truncation, and recording the distinction between
this obstruction criterion and an unproved assertion about actual sums.

Completed: the inequalities and conditional tail obstruction were audited
and stored in L172. The actual first and third moment questions remain open.
