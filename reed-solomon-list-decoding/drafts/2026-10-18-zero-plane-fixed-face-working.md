# Fixed-face test — work saved before exact calculation

Approved target: Determine whether L082's positive-weight modes yield a fixed exact face reduction of the full zero-plane joint affine-LMI system.

Reuse `literature/2026-10-18-zero-plane-fixed-face-reduction.md` (SPECIALIZE),
Permenter–Parrilo v3 Lemma 3 and Section 4.1 as recorded in foundations/10.
Main gap: arbitrary-center safety at 67/68 agreements; bracket 955–957.
One bounded REPRODUCTION calculation, with no new numerical solve, weight
change, point scan, domain restriction or minimal-face assumption.

Candidate: in each of L082's 28 positive-weight modes, use the Schur
kernel vector of the step-298 retained positive-diagonal base. First
check that its inverse action is constant on the entire t78=s plane.
Then weight its outer product by the unchanged canonical scalar weight.
Check all 49 affine trace coefficients (constant, three parameters,
45 moments), transport back through the saved rational congruence,
and require nonzero action on the retained blocks. If any essential
identity fails, preserve it and stop this prescription. If all pass,
compute full-rank kernel/complement bases and retain every mixed and
removed-coordinate equation with the compressed PSD conditions.
Check the coefficientwise invertible pullback to the original blocks.

Essential inputs: L021,L053,L073,L075,L076,L078,L079,L081–L084;
foundations/04,09,10,12; complete step-290/292/294, equality and step-298
certificates. Retain rho,p8, original pairs, seven RREF/completion,
85 domain rows, 90 weighted kernel equations, 500 types/3000
presentations, 36 forced/45 free entries, all 81 modes, full anchor,
singular/empty ranges and canonical weights. Ancestor PSD, uniqueness,
whole-kernel and source-normalization qualifications remain; L084's
separate critical review remains pending. A formal face equivalence
alone decides neither feasibility nor the RS gap. Scalar upper rows,
other anchors, global consistency and different moment choices remain open.

## Completed calculation

The prescription passes. [L085](../lemmas/L085-fixed-face-reduction-of-zero-plane-joint-system.md)
is canonical: it gives the multiplier, full kernel/complement bases,
all retained equations, original normalization and both equivalence
directions. The complete certificates are
`scripts/finite-support/zero-plane-fixed-face-results.json` and
`scripts/finite-support/zero-plane-fixed-face-verification.json`.
They pass 10999 and 491 exact checks respectively, with zero failures.
All 49 affine trace coefficients and 45 raw-moment coefficients equal
the required zero. The multiplier has rank 28 on the already retained
blocks; their summed sizes decrease from 140 to 112.

The 28 face equations are precisely the old selected equalities, with
constant/linear right sides on the plane. This is a reformulation, not
a new exclusion or feasibility verdict. No numerical solve was run.
The source method is imported without reproof; this is REPRODUCTION.
Independent verification here is arithmetic checking, not the separately
routed critical proof review. That review is the sole proposed next
target and requires separate approval of its new source-reuse assessment.
No failure or pre-existing unfinished work was removed.
