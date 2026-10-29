# Residual-state domination — step 540 working record

Invocation-start gate: `drafts/literature/2026-10-28-residual-domination-offline-test-review.md`
(SPECIALIZE), reused unchanged. Main gap: pair-free uniform twelve-row
exclusion. Intermediate target: completion-preserving same-span domination
among the frozen complete histories; possible use: compression of a later
cover. Continue only with a sound criterion and an independently verified
relation between distinct histories. No new block-rank tests, resumed
traversal, symmetry or coding converse is authorized.

## Soundness argument saved before the finite test

For an increasing feasible history T let W(T) be its whole-block row span,
d(T) its sixteen integer degrees, and B(T) its complete saved candidate
set, including the strict last-label cutoff. A completion X is an
increasing list disjoint from T such that T followed by X is increasing,
pairwise linear, degree at most four and has deficient whole-block span.
The empty completion is allowed. All its prefixes satisfy these conditions.

Assume W(T)=W(U), |T|=|U|, d(T)=d(U), and B(U) subset B(T).
For every completion X of U, each a in X belongs to B(U): its single
block extension is contained in the deficient final span; its order,
individual compatibility and unsaturated-coordinate tests follow from the
completion. Thus X subset B(T). In particular its labels exceed T's last
label, are unselected in T and are individually linear with every member
of T. Internal conflicts within X are unchanged. At every coordinate h,
d_h(T)+d_h(X)=d_h(U)+d_h(X)<=4. Moreover
W(T)+sum_(a in X) row(N_a)=W(U)+sum_(a in X) row(N_a),
so the final span and each prefix span are deficient. T followed by the
same X is consequently a completion of the same cardinality. Optional
zero-increment blocks and the empty completion require no extra condition.
This works over every extension of F_97: equality of base-field spans
extends, and ranks of these base-field matrices are unchanged by extension.
It asserts preservation of existence/cardinality, not coding gates or a
bijection between labeled complete families.

This specializes semantic state dominance from Kuroiwa–Beck,
arXiv:2401.13883v5, section 3.3.1, Definitions 14–15 and Theorem 5
(pp.12–13); it supplies the notebook-specific completion argument rather
than assuming the generic theorem identifies our state. Range 17/2013,
sections 3–4.1, Dominance 1–2 (pp.4–6), explains why future availability
must be retained. Direct primary URLs and essential cases are in the
unchanged invocation-start assessment. This is reproduction/specialization,
not a claim beyond the checked literature. Full matching Mathlib coverage
has not been checked.

Safe deletion additionally needs an acyclic representative policy. For
equal B sets retain the smaller node ID. For strict inclusion permit only
arrows toward the larger B set. Every arrow then strictly decreases the
lexicographic potential (-|B|,node ID), so finite chains end at a retained
representative. Every removed state's completions transport along that
chain. Each retained representative's entire search obligation must still
be discharged; a saved capacity node has its certified bound, whereas a
branch retains every unresolved descendant obligation. This offline test
does not delete states, discharge frontier records or construct a cover.

## Planned exact finite test

Group complete nodes by (exact canonical whole-span kernel, cardinality,
sixteen residual degrees). Inspect unordered node-ID pairs in global
lexicographic order, at most 100000, and test both B inclusions. Recompute
every complete B from saved complete extension increments and original
incidence data, without matrix operations. Exclude frontier and partial
scans. Independently reconstruct incidence by pair constraints and verify
all groups, tested pairs, both directions and representative arrows.
Retain full input hashes and evidence under `scripts/residual-domination/`.
No smaller complete cover or capacity bound follows from comparison counts.

## Completed result

The completion argument and all qualifications are now canonical in
`lemmas/L170-same-span-residual-completion-domination.md`.
Both finite implementations pass with zero failures. Of 360214 eligible
pairs, the approved prefix of 100000 has 29124 strict and 26205 equal-B
pairs; 31 acyclic arrows join branch nodes. Every complete B list and
both inclusion directions were independently checked. The original
cover and verification bytes remain unchanged; zero new rank tests were
used, and all 1665 frontier obligations remain. This is useful local
specialization, not a mathematical discovery beyond the checked sources.

The continuation threshold is met. Further traversal is not authorized
by this offline result or the exhausted cumulative block-test budget.
Separate critical review of L170 is pending. A different source-first
target is prepared at saved span 274, retaining exact-rank-one gates
that this rank-only comparison does not address. No geometry of that
kernel was calculated or asserted this step.
