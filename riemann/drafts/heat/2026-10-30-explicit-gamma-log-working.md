# Explicit gamma-log linearization working record

2026-10-30. One approved calculation under the existing SPECIALIZE
assessment `drafts/literature/2026-10-30-explicit-gamma-log-linearization.md`.
No contour count or real/simple cutoff is being attempted.

Main gap: actual-Xi all-degree positivity, and finite positive-time
collision exclusion on this route. Intermediate test: the exact
assessment's closed-disk gamma-log error at most 1/100. Success could
supply one input to a later strict contour comparison with L490;
failure must identify its term and domain. Exhaustion, reflected
residual bounds, collision exclusion and zero-time control stay open.

The supplied assessment was read without rereading it from disk.
Duplicate/failure coverage was reused and checked against the narrow
source note and ATTEMPTS/2026-10-30-direct-numerical-tail-extraction.md.
The latter stops extracting an unspecified cutoff, not this explicit
component. Primary formulas (7),(9),(10),(42),(100) were retrieved from
Polymath arXiv:1904.12438v2. Need to keep the formula-(7) branch, not an
argument modulo 2*pi. No saddle approximation is used.

Plan saved before the longer calculation: expand the explicit logarithm
at s=(1+iX)/2 around iX/2, with Log(1-i/X) on its analytic small branch;
separate its center imaginary part from its real leading correction.
Then bound the exact derivative alpha+(t/2)alpha alpha' on the disk.
Conjugation of the principal logarithms away from the cut must justify
the negative-imaginary terms. All bounds must be uniform in X and t,
including the closed endpoints. No sample computation will certify this.

Unfinished at checkpoint: explicit rational constants and a complete
branch-aware proof have not yet been written or checked.

## Calculation completed; preliminary source-based constant withdrawn

The preliminary use of source (76) would have given (L/2+10)/X and
2505/10^12. These particular bounds are NOT established: the source's
printed coefficient fails already at sigma=0, x=200 when compared
with exact formula (9). This was caught before completing the step.
The full rational discrepancy and replacement estimates are preserved
in L491. The repaired calculation uses the explicit formulas and
elementary logarithm estimates, giving (L+20)/X < 5010/10^12 < 1/100
on the full prescribed domain. This changes no target or tolerance.

Canonical proof: [L491](../../lemmas/L491-explicit-gamma-log-linearization.md).
It handles the fixed branch at the center, both conjugate half-planes,
the entire closed disk, the closed time interval and unbounded X by
analytic inequalities. No finite samples or saddle imports certify it.
The result is a reproduction/specialization of the source's qualitative
model, with a corrected auxiliary bound, and awaits separate audit.
The original center/disk plan above is retained as the saved checkpoint.
