# Triangle twelve-count attempt: finite threshold reduction

STEP_ID: 2026-10-10-mca-137-triangle-finite-threshold-reduction

Approved target: determine whether L057's gated fixed-H triangle pencils
have at most twelve distinct additional relaxed recovery parameters,
retaining both-zero lifts and the original finite exclusions. Coverage
is the unchanged `literature/2026-10-10-triangle-twelve-recovery-bound.md`.

The main gap is arbitrary sixteen-count equality exclusion. The present
intermediate target is an exact, threshold-complete finite reduction
of this triangle count, with an explicit way to retain arbitrary original
charts. Its downstream use is a finite simultaneous count rather than
another conditional-descent argument. Other patterns, extraction and
challenge definitions remain open.

Test: define the prime-field scalar set by all L057 lifted equations,
including both-zero cases and zero recovered weights, before the E gate.
Prove that the original twelve bound is equivalent to its uniform twelve
bound over all rational gated weights and all labelings. Necessity must
construct an actual original chart preserving every retained scalar;
sufficiency must use L058 only at a genuine thirteen-parameter violation.
Stop or repair if the free chart introduces nonprime recoveries, loses a
base event, or invalidates same-support failure. A selected-label maximum
would not prove the target and is not the proposed output.

Reused the supplied source comparison and its duplicate/failure record.
Read L057's full symbolic criterion/proof, L058's full descent/audit,
L010's bound/equality proof and L041's local converse. The existing
L044 finite reduction concerns tau=1; the triangle requires all its
both-zero lifts and cannot import that candidate classification. No new
source retrieval or standard recurrence reproof is needed.

Saved initial reasoning: write the chart-free set as support-indexed affine
coordinate cylinders for isolated recoveries, and explicit scalar-indexed
points for both-zero recoveries. Deduplicate scalar values before any
count. The proposed chart choice is gamma=(0,1,rho) with rho outside
F_97, lambda=1; check E=(1+mu)rho-mu for every prime-field mu!=0,-1.
No maximum or exclusion has been computed or claimed.

## Completed attempt

The exact proof is canonical in
[L059](../lemmas/L059-triangle-finite-threshold-reduction.md).
For rational gated weights the full scalar set M loses exactly its
intersection with {rho/(1-rho)} in any original chart. Choosing nonprime
rho realizes the entire set in an allowed pencil, including all both-zero
lifts and lower-weight recoveries. L010 therefore bounds |M| by thirteen.
At thirteen, fullness and coordinate balance imply at least seven distinct
recoveries disjoint from P. Their complete restored equations generate
an explicit weight/scalar table: one scalar per isolated support and up
to 95 per both-zero support, with every gate retained and scalars
deduplicated. Only weight points with seven distinct such scalars can
violate twelve. L058 makes this finite test complete for arbitrary
extension-field weights; no given pencil's chart is changed.

The chart mechanism was already present in L044 for tau=1 and is openly
reproduced. The triangle table and its necessary seven-scalar filter are
the present local restriction. They are not a claim of originality, an
enumerated maximum or a complete solution. No selected-label sampling,
new mathematical script or finite certificate was used. The all-eight-
moment and same-support implications use audited L057, rather than a
four-moment numerical regression. Reviewed direct DAG uses are L010,
L041, L057 and L058; L044 is a comparison only.

Outcome: ADVANCE, POTENTIALLY_NEW under the unchanged approved EXPLORE
scope, meaning a relevant exact reduction rather than a twelve theorem.
The finite table may still have thirteen-scalar survivors. Preserve all
prior stopped routes and unfinished work. The new result requires a
separate critical audit; its proposed scope is REVIEW_REQUIRED, not
approved by this derivation. The global interval remains 11/q–16/q.
