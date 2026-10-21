# Exact elliptic rank test — working record

2026-10-21. Target: Determine whether L111's elliptic quotient has Mordell–Weil rank zero over Q.
Prior assessment: literature/2026-10-21-marked-elliptic-rank-zero.md (SPECIALIZE).

Main gap: positive primitive integer exclusion for residual Beal signatures,
here ordered (3,5,11)'s rational-factor/minus-three branch. Intermediate
target: rank zero of L111's exact quartic with origin (2,165). A rank-zero
certificate could enable a finite torsion/lifting analysis; an exact
non-torsion witness stops that route. Use the assessment's covariant
images first, its fixed box only if needed, and at most sixteen multiples
or two complete good-prime counts <=101. No witness leaves rank unknown;
no enlargement, backend probing or analytic rank inference is authorized.

Inputs are audited L109/L110/L111 and the cited Fisher, Milne and Cremona
results in the assessment. ATTEMPTS/050's different genus-two detector
is exhausted and preserved; L108 remains unfinished. No exact-instance
rank result or duplicate rank proof was found in the saved coverage.
All existing notebook changes are preserved. Unresolved independent
steps: marked lifting h²=3(4−T²), degree-nine root recovery, remaining
factors, both L095 integer systems and minus-eleven.

Checkpoint before calculation: exact model, covariant evaluation and
non-torsion certificate still pending. Formula extraction from the already
assessed primary source is implementation support, not a fresh literature
assessment or a changed target.

## Completed bounded attempt

The rank-zero target is answered negatively: rank is at least one.
Canonical full proof and citations are in
[L112](../lemmas/L112-marked-elliptic-positive-rank.md).
`python3 scripts/pair-genus-two/elliptic_rank_witness.py` passes all
23 checks without failures and writes the complete certificate to
`scripts/pair-genus-two/elliptic-rank-witness-certificate.json`.
The known boundary point suffices; only the first two multiples are
used, within the cap sixteen, and the fallback box is not invoked.
All covariant coefficients and thirteen zero syzygy coefficients,
both images, exact tangent and double were inspected in full. The
remaining exact invariant/scaling/check fields were also inspected in
full before closing this step. No finite-field counts, complete descent, exact
rank, generator list or integer exclusion is claimed.

Record this as RESEARCH / ADVANCE / REPRODUCTION, actual type
calculation: it establishes a relevant exact-instance input by known
methods and stops the rank-zero route, not a general discovery.
ATTEMPTS/051 preserves that stop. Separate critical audit is the sole
next action; its newly written assessment is REVIEW_REQUIRED for
approval next turn. All independent gaps above remain unresolved.

Documentation validation initially flagged PROOF.md at 102 lines after
the two added overview/trap lines. Integrating those sentences into the
existing overview/trap paragraphs restores the 100-line limit without
removing mathematical content. This is a documentation issue, not a
failed mathematical certificate.
