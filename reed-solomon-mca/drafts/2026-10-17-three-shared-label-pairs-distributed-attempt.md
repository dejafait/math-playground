# Distributed simultaneous shared-label join

STEP_ID: 2026-10-17-mca-278-distributed-shared-label-join

Saved before calculation. Reuse the pre-existing EXPLORE assessment
`literature/2026-10-17-three-shared-label-pairs-feasibility.md` and its exact
TARGET. Main gap: uniform triangle twelve and sixteen-count equality.
Intermediate target: one gated L057 pencil with six distinct finite full
isolated recoveries, two through each shared label, all nine supports
pairwise linear. An obstruction could constrain equality; a witness would
stop only this stronger exclusion. Completion of the other seven errors,
uniform count and challenge-definition qualifications remain independent.

Read L057's complete criterion and proof mechanism, L041's local converse,
audited L101, the first simultaneous attempt and ATTEMPTS/036–037/039.
Existing recurrence and shortening source coverage is ready and unchanged;
no additional literature or new individual recovery lemma is needed.

Execute at most 250,000 distinct actual ordered nine-label assignments,
using deterministic seed 277 and sorting only inside Y,Z,W. Save all
selections. Reuse the complete common-weight join; six-row positives must
pass restored equations, full weights, all eight moments, distinct scalars,
all intersections and a chosen allowed original finite chart. Prime-field
choices serve existence only; no arbitrary weights or chart descend.
Independent recurrence-column replay will compare complete rows and pairs
at saved pair-bearing assignments and the best selection. Stop at a verified
witness or the bound. A failed sample is EXPLORATION, not an exclusion.
A second unproductive attempt requires reassessment of this join search,
not another extension or reseeding. Preserve all prior work.

No new lemma or main argument change is planned; Mathlib coverage of the
full simultaneous target remains unchecked, not absent.

## Completed attempt

Outcome: EXPLORATION, RESEARCH, POTENTIALLY_NEW (search classification,
not an originality claim). No advance beyond the inspected sources.
The seed-277 selection used the standard mt19937 engine, an explicitly
rejection-bounded Fisher–Yates shuffle, and only within-pair sorting.
250,059 draws produced 250,000 distinct ordered assignments after 59
exact duplicates were skipped. Every assignment has nine distinct labels
in H; named roles were never identified by a supposed label symmetry.
The selection file saves ordinal,a,b,c,y1,y2,z1,z2,w1,w2, without a header:
`scripts/triangle-recovery/three-shared-pairs-distributed-selections.csv`.
Its SHA256 is
`65bb12873d40e2b40ab439401e5f056e1bc087884ad1d2dbee635b6b3fd96cb3`.
Every H label occurs in each shared role; the complete per-role counts
are saved in `scripts/triangle-recovery/three-shared-pairs-distributed-role-counts.json`.
Distribution across roles is not exhaustive coverage of assignments.

The producer performed 57,750,000 support tests, 231 per assignment.
Role-specific gated isolated rows number 235,287, 235,089 and 233,607.
Compatible within-tag pairs number 64,73,87 at 64,73,87 assignments;
these are 224 distinct pair-bearing assignments in total. The maximum
number of pair-bearing tags at any assignment is one. Thus no assignment
reaches a two-tag or three-tag common-weight join, versus the required
positive threshold one full six-row join. There are zero distinct-scalar,
linear and full six-row joins. The zero six-row moment-failure counter is
vacuous: no six-row moment equations or original-chart checks were reached.
These are exact counters for this sample, not uniform exclusion evidence.
The full counters and endpoint are in
`scripts/triangle-recovery/three-shared-pairs-distributed-prefix.json`;
every reported pair-bearing assignment, with its complete candidate row
and pair sets, is in
`scripts/triangle-recovery/three-shared-pairs-distributed-partials.jsonl`.
The best assignment is ordinal 1162, with
(a,b,c)=(70,75,8), Y=(27,33), Z=(18,47), W=(22,89).
It has seven gated rows and one b-tag pair. It improves the first random
selection only; it does not improve step 277's maximum one pair-bearing tag.

## Independent replay and limits

The existing verifier now accepts an optional parsed saved assignment;
its previous file-based behavior is unchanged. The new verifier validates
every saved selection for exact ordinal, membership, distinctness,
within-pair ordering and global assignment uniqueness, and compares all
role frequencies. At every one of the 224 reported pair-bearing assignments
it enumerates all 1820 four-subsets of H, applies the complete eligibility
gates (231 supports), and eliminates recurrence columns independently of
the producer's G_J quotient. All 51,744 eligible support tests, 1,254
retained rows and 224 pair sets agree exactly. The saved best assignment
also receives complete replay; it is already among these 224, not an
additional independently selected case. All replayed three-tag joins are
empty. The producer reports no assignment with two pair-bearing tags.

For each of the 224 local pairs the verifier chooses an allowed free weight
and finite chart and recovers actual errors by first-four Gaussian solve,
then checks every one of the eight moments. It verifies the affine third
base, five distinct finite times, full errors and same-support input
failure for all five errors. Every local pair has such a witness; there
are no missing pair replays. This corroborates the existing local-pair
phenomenon, not a new canonical existence theorem or a six-row witness.
No unreported assignment received independent complete row replay;
selection validation alone does not certify those negative support tests.
No sampling result is used as a theorem over prime or extension weights.

The full certificate is
`scripts/triangle-recovery/three-shared-pairs-distributed-verification.json`.
Its aggregate, all relevant empty/failure sets, complete best rows/pairs,
and producer counters were inspected exactly. An initial inspector call
used the invalid pointer `/` for a root object; it returned an error and
provided no evidence. Correct selected pointers were used afterward.
Reproduce with:

    clang++ -std=c++17 -O3 scripts/triangle-recovery/three_shared_pairs_distributed.cpp -o /private/tmp/mca-three-shared-pairs-distributed
    /private/tmp/mca-three-shared-pairs-distributed
    python3 scripts/triangle-recovery/verify_three_shared_pairs_distributed.py

The new producer preserves the earlier prefix and certificate paths.
The independent replay imports the existing verifier's exact residue-field
helpers; it does not import producer recovery formulas. No external source,
new canonical lemma, DAG edge or main-argument change is warranted.

## Reassessment

This is the second mathematical EXPLORATION on the simultaneous join
mechanism. Stop further prefix extensions and reseeded sampling on this
mechanism; preserve the failure in ATTEMPTS/040. Neither feasibility nor
infeasibility is decided. No twelve bound or interval improvement follows;
11/q–16/q and the independent challenge-definition gaps remain.

The proposed next source review considers a different exact algebraic
mechanism: imposing the prescribed subgroup equations in L095's rational
cyclic reconstruction, before searching for a bounded nonvanishing test.
This is a proposed review, not an assertion that a subgroup elimination
works or differs sufficiently from ATTEMPTS/033–034. Those recorded failures
must be compared before approval. It addresses one possible equality family,
not arbitrary-family coverage or simultaneous shared-label feasibility.
The changed target has REVIEW_REQUIRED coverage and receives a separate
literature-only turn. No cyclic derivation, source comparison or calculation
was performed in this step.
