# Optimized subset obstruction draft — 2026-09-11

Candidate: U_k=2^(4k²), d_k=sqrt(U_k), prescribe suffix indices
[U_k,U_k+d_k), plus 1, with x_s=s^(3/4); use the previous gap
interpolation. These packets retain divergent suffix weights.

Needed bound (UNPROVED at checkpoint): every nonempty subset F of an
integer interval of length d has c(F)/|F| at least const log(d)/d.
For m small use c≥1. For m≥sqrt(d), sum crowding at the m selected
points; rank-q distances have total at most q(d−1), so Cauchy gives
sum inverse shifted distances ≥(m−q)²/[q(d−1)+(m−q)]. Sum q≤m/2.
This should force every optimized block ratio to grow like log d,
with summable inverses on the sparse dyadic packet starts.

Resume by auditing the uniform bound including small m and clipped
blocks, then write a canonical lemma only if all bounds hold.

Completed: the uniform bound and construction are proved in Lemma 98.
The bound obtained is c(F)/|F|≥log(d)/(32d), for d≥256.
The draft's unproved candidate has been resolved; current work is recorded
only in PROGRESS.md.
