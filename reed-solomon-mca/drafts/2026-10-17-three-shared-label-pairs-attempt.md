# Simultaneous three-shared-label pair join

STEP_ID: 2026-10-17-mca-277-three-shared-label-pairs-join

The pre-existing EXPLORE assessment is
`literature/2026-10-17-three-shared-label-pairs-feasibility.md`; its
exact target is retained. The main gap is the uniform triangle twelve
bound and L010's sixteen-count equality. The intermediate target is
six full isolated additional recoveries, two through each named shared
label, in one gated L057 triangle pencil, with all nine supports linear.
An obstruction could constrain equality's shared-label incidences; a
full witness stops only this stronger exclusion. Completion of the other
seven additional errors, arbitrary-family coverage and challenge
definition qualifications remain independent gaps.

## Saved before calculation

Reused the ready source assessment, read L057's complete criterion and
load-bearing proof, L041's local converse, audited L101 and
ATTEMPTS/036–037/039. No source refresh is needed. The stopped disjoint-P
eliminations and refuted single-tag exclusion are not repeated.

For each actual triangle assignment, enumerate every four-support
containing exactly one named shared label and meeting each base support
at most once. Apply L057 (5)–(11) without changing roles. A row through
a fixes q,r; one through b fixes p,r; one through c fixes p,q. Group
two rows at a tag only if those two fixed weights match, their scalars
are distinct and their outside triples are disjoint. Join the three
tag pairs at one p,q,r, then check all cross intersections, all six
distinct scalars, full numerator weights and eight moments. A successful
join receives a separately chosen allowed finite chart, direct Gaussian
recovery and same-support failure checks. No original chart is presumed
rational; prime-field choices suffice only for an existence witness.

Bound: at most 250,000 actual assignments, starting with L101's actual
assignment, then a deterministic prefix of the existing pair-search
label traversal. Every processed assignment is fully searched for this
six-row join; no label symmetry or exhaustive coverage of all assignments
is inferred. Preserve counters and best partial configurations on disk.
Continue on a fully verified witness or a uniform contradiction; abandon
any impossibility inference from an unsuccessful prefix. An unsuccessful
bounded search is EXPLORATION, not an exclusion or a count improvement.

Full matching Mathlib coverage has not been checked; no new general
recurrence, distance or shortening result will be reproved.

## Completed bounded attempt

Outcome EXPLORATION. The corrected deterministic run processed 250,000
distinct actual triangle assignments and 57,750,000 admissible support
tests (231 per assignment). It included the L101 seed once, then the
first 249,999 nonseed assignments from the existing lexicographic
traversal with A<B; this is an explicitly chosen subfamily, not a
symmetry reduction. Here A={b,y1,y2}, B={c,z1,z2}. The outer shared
label remained a=1 throughout this prefix; the last actual assignment
is recorded in the certificate. There is no coverage of all H-labelings.

The three role-specific gated isolated-row totals were
215,431, 218,473 and 229,744. There were 2, 0 and 123 within-tag
compatible pairs, respectively, occurring at 2, 0 and 123 assignments.
No assignment had pairs at two tags, even before comparing cross-tag
weights. Thus there were zero two-tag weight joins and zero three-tag
weight joins, against the positive-witness threshold one. No six-row
fullness, finite-chart or eight-moment check was reached. The producer's
zero moment-failure counter is therefore vacuous for six-row witnesses;
it is not 48 checked moment equations or evidence of exclusion.

The complete prefix counters and endpoint are in
`scripts/triangle-recovery/three-shared-pairs-prefix.json`; every
pair-bearing assignment is in
`scripts/triangle-recovery/three-shared-pairs-partials.jsonl` (125 rows).
The saved seed and best partial coincide: the seed already has one
pair, and no processed assignment improves the number of pair-bearing
tags or the pair-product score. They are one distinct assignment,
not two independent examples.

Independent replay enumerates all 1820 four-subsets of H at the seed,
tests every eligible one (231), eliminates the two recurrence columns
directly, and compares complete gated row and pair sets with the
producer. All 12 rows and the sole a-tag pair agree; there are no b-
or c-tag pairs at any weight for these fixed base labels. All six
eligible rows through a, two through b and four through c are retained
in the full replay certificate, including their fixed weights. A
Gaussian first-four recovery followed by all eight moments reconstructs
the existing L101 pair at p,q,r=(2,14,75), gamma=(0,1,2). It also
checks its five distinct finite parameters and all five same-support
input failures. This is a regression of an already audited local
witness, not a new result or separate new audit of L101. Full load-bearing
seed rows, pair sets, positive replay and empty failures were inspected.
The certificate is
`scripts/triangle-recovery/three-shared-pairs-selected-verification.json`.
The remainder of the prefix has not received independent complete
replay; none of its negative counters is used as a theorem.

An initial output-instrumentation defect omitted the best-file copy
when the seed remained best; it was repaired before the corrected run.
The seed's second occurrence in the original traversal was also removed
before that run. The first failed verifier invocation and these fixes
provide no mathematical evidence. The final selected replay passes.

Reproduce the bounded run and selected verification with

    clang++ -std=c++17 -O3 scripts/triangle-recovery/three_shared_pairs_join.cpp -o /private/tmp/mca-three-shared-pairs-join
    /private/tmp/mca-three-shared-pairs-join
    python3 scripts/triangle-recovery/verify_three_shared_pairs_join.py

No canonical lemma, bound, DAG edge or main-argument change is warranted.
This is one mathematical exploration on the approved simultaneous target,
with no advance beyond the inspected sources and no impossibility claim.
Arbitrary labels, extension-field choices, original charts and completion
remain open. The 11/q–16/q interval is unchanged.

The exact target and pre-existing assessment remain usable. A second
bounded attempt could distribute actual assignments across the label
space rather than extend this highly concentrated prefix: use a saved
deterministic seed 277 to select at most 250,000 distinct ordered
nine-label assignments, sort only within each singleton pair, retain
all named roles and save the actual selections. Apply the same complete
join and independently replay any positive witness. This proposes no
new mathematical criterion or H-label symmetry. A second unproductive
attempt requires reassessing this search mechanism, rather than merely
extending its prefix. A full witness would stop only the simultaneous
exclusion; a failed bounded sample would still leave feasibility open.
