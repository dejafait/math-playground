# Paired Hardy-jet feasibility attempt, 28 October 2026

Approved target: the exact Next action in the saved SPECIALIZE assessment
`literature/2026-10-28-two-height-hardy-jet-feasibility-test.md`.
Main gap: actual-Xi initial signs and actual clipped mass remain uncontrolled.
Test: a positive six-coordinate law satisfying all 21 second and 126 fourth
constraints and E Q>=ell/288, or a rigorous uniform separator.

## Checkpoint before source specialization

The candidate mechanism retains the actual six-jet quartics by a positive
spherical pushforward at radius ell^2, without any reflection. Its second
matrix R is positive semidefinite and O(1). The leading second matrix should
be the derivative Gram matrix of sinc((r-s)/2) at r,s in {0,1}. Strict
positive definiteness would permit exact subtraction of R from ell K in
the bulk; thus all four tight odd second entries could be exactly zero
without altering a cross-height fourth moment.

Extend L472's twelve-state first-jet bulk to a six-coordinate law with
second matrix K using the Schur complement and independent centered finite
noise. Then transport by
K^(1/2)(I-ell^(-1)K^(-1/2)R K^(-1/2))^(1/2)K^(-1/2).
For fixed positive definite K this is I+O(ell^(-1)). A mass-normalized bulk
should retain E Q=ell/144+O(1), above the required ell/288 eventually,
and add only O(ell^2) to quartics. These assertions are not yet certified.

Remaining work: justify the complete Hardy-phase second/fourth generators,
strict Gram positivity, the six-coordinate extension and exact covariance
correction; check uniform errors and one common onset. No numerical search
is evidence for these claims. Existing L471 ordinary-moment and frozen-jet
stops are preserved. The arithmetic moment theorems are imports, including
the unaudited omitted proof of Bui--Hall Proposition 3.

## Completed attempt

The construction is written in full in
[L473](../lemmas/L473-paired-hardy-jet-moment-feasibility.md).
The source specializations give the sinc-derivative covariance and all
126 quartic coefficients with the required errors. The Gram matrix is
strictly positive definite by exponential-polynomial independence.
Exact covariance correction replaces the unavailable reflection; all
four odd second entries are zero. The law satisfies every quartic
reference entry with error O(ell^2), within the allowed O(ell^3), and
E Q=ell/144+O(1)>=ell/288 eventually. The source proofs are imported;
the new application still requires separate critical audit.

This is an informative negative result for this finite-moment
discriminator, not a negative actual-Xi value or a resolution of RH.
No mathematical script or numerical feasibility certificate was needed.
