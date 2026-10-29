# Fixed-pair closure/capacity attempt — step 533 working record

Invocation-start assessment:
`drafts/literature/2026-10-28-block-closure-capacity-pilot-review.md`
(EXPLORE). Only its fixed-pair target is being attempted. Existing
uncommitted files are preserved. No cross-notebook input is used.

Main gap: uniform twelve-row exclusion. Intermediate target: at most
eleven pairwise-linear, degree-at-most-four selected supports in every
deficient complete-block closure containing L167 rows 2 and 3. Success
would give a numerical-pair exclusion, with all-pair transfer, coding
realization and challenge identification still independent gaps.

## Proposed invariant, before calculation

Let B_a be the entire row space of L109's original six-by-21 block,
W a span of selected whole blocks, and C(W)={a:B_a subset W}. Its
closure properties are the specialization of the finite closure/
representable-polymatroid machinery assessed in step 532. No new
enumeration theorem is proposed.

Use the larger *deficient-extension envelope*
E(W)={a:dim(W+B_a)<21}. If W is contained in a deficient span W',
every selected block of W' belongs to E(W), by dimension monotonicity.
Thus a capacity upper bound on E(W), with the already selected rows
and their integer degrees, bounds **all** deficient descendants of W.
Capacity on C(W) alone would not do so. This is the proposed coupling,
not yet a numerical bound. One may intersect E(W) with literal
compatibility with the selected rows and residual positive capacities.

A selection-history search may branch in increasing added-support
order, keeping histories separately even when their spans coincide.
The invariant is that every as-yet-unexcluded deficient twelve-support
family containing the pilot has a branch whose selected history is a
subset and whose candidate envelope contains its remaining supports.
Rank 21, an exact integer capacity bound below twelve, or exhaustion
can close a branch; a capacity failure cannot. All 756 original blocks
remain available for closure reconstruction, and ranks below 21 remain.

Weak-duality weights, if used, will be exact nonnegative rationals for
the incidence matrix with residual capacities 4-d_h, as covered by
Boyd–Vandenberghe (2004), sections 5.1.3 and 5.2.1–5.2.3 pp. 216,
224–227. No LP integrality or matroid exchange will be assumed.

Stop at an exact twelve-support deficient witness, 10,000 distinct
generated spans, or 1,000,000 block-containment/extension tests. Save
the entire unresolved frontier and actual counters on a cap. A capped
run is not exclusion. A successful conclusion needs full exact evidence
and independent reconstruction. Mathematical scripts will live under
`scripts/block-closure-capacity/`.

## Inputs and retained limits

L109 formula (1) and its rank-21 necessary obstruction; L167's actual
table fixes rows {8,12,70,75} and {18,22,79,85}. L153 is optional
rank-twelve evidence only. Relevant source and duplicate comparison
is already complete in the prior assessment. ATTEMPTS/041,043,048,055
and the L125/L151/L154/L162/L168 comparison prohibit rank extrapolation,
kernel identification, or coding-dependent exclusions on relaxed sets.

All original S/J labels, pivots, block order and characteristic 97 are
retained. Every selected support is optional until selected. Rank
statements extend by minors; no extension-field sample is used.
Decomposability, exact projection ranks, weights, original charts,
sixteen-event completion, arbitrary representation and identification
with the grand challenge remain unproved. Any coding application retains
L104/L086/L010 and their full finite-field qualifications.

## State

The producer completed its bounded run: 300 distinct proper spans,
226,800 whole-block tests, 12,508 retained selection histories, 91 branch
nodes and 12,417 capacity leaves. Every leaf bound is at most eleven;
the frontier is empty. Full independent reconstruction of all original
blocks, complete kernels, extension ranks, capacity inequalities and
tree coverage passes with zero failures. This establishes the fixed-pair
partial result, not a challenge solution. Full reasoning is now canonical
in L169; full evidence is `scripts/block-closure-capacity/pilot.json` and
`scripts/block-closure-capacity/verification.json`. Separate critical
audit remains pending, with the new source-scope intake recorded in
PROGRESS.md. Do not use these working notes as a second proof or status
record; the canonical lemma and checkpoint supersede their proposal.
