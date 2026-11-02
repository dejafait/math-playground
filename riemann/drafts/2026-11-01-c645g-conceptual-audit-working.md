# C645g conceptual audit — working record, 1 November 2026

Approved target: the unchanged half-grid-exponent norm test in
`drafts/literature/2026-11-01-positive-residue-hankel-exponent-test.md`.
This invocation audits the existing proof, without expanding its family.
The main gap is actual-Xi signs/all-degree mixed positivity. The proposed
use is a boundary detector after a principal-part application, an actual
sparse census and an independent smaller boundary upper bound.

## Saved before completing the audit

Read C645g completely, the parent full-pole source comparison, C645c's
unconditional rate proof and its audit, and C645f's exact factor/grid and
source conventions. Reused their inspected primary sources; no additional
literature search or mathematical script is needed. The recorded scalar
cancellation stop remains valid. No cross-notebook theorem is used.

Initial checks: q(z/R) has exactly the physical residues in (8), including
the 1/R cancellation. Multiplication by the product of distinct pole
factors gives a polynomial of degree at most m-1, irrespective of residue
sizes. Normalized Fourier orthogonality gives the displayed interior
evaluation factor. The lower bound uses H_q applied to 1, hence the full
operator norm, not a smallest singular value.

Still to complete: verify the finite improper integral and existence of
one admissible radius for all poles simultaneously; check all constants
on the full open delta interval; check the residue theorem's complete
pole list and the orientation; verify the census and exact-rate
comparison, including empty small-n cases. Acceptance requires each
quantified case to survive without hidden separation or phase positivity.
A failed proof step alone would not refute the approved norm target.

Only C645c's unconditional Lambda>delta/4 is a mathematical lemma input.
C645d/C645e/C645f remain comparisons/source conventions. Exact confluent
higher-order poles, nonpositive residues, actual-Xi realization and the
downstream principal-part application are outside the claim.

## Completed audit

All stated checks passed; no mathematical correction was needed. The
full verification is canonical in
[C645g](../lemmas/C645g-sparse-positive-residue-hankel-bound.md), under
its independent conceptual audit. The radius selection includes the
strict-average argument, every pole enters the denominator cost, and
the residue normalization retains both the complex multiplier and the
physical/unit-circle scaling. The verified exponent remains delta/8,
which is smaller than Lambda/2 by the already audited C645c input.

This is reproduction/verification of an existing local bound, not a new
bound or certified novelty. No mathematical script, fresh external
search, source-proof audit or actual-Xi application was performed.
The mathematical assembly and DAG inputs have not changed.
