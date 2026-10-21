# Column-aware algebraic syndrome packing — source comparison

TARGET: Assess a column-aware algebraic syndrome partition for (3,2,2,2)-profile additions on nine F_107 columns that guarantees at least 5774752369 pairwise-compatible nine-sets.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded searches for algebraic constant-weight syndromes, unequal-weight generalized packings, power-sum constructions and mixed moments found no inspected theorem supplying this exact finite column-aware guarantee; reuse the completed product/asymptotic comparison.
SOURCE_EVIDENCE: Derksen arXiv:math/0311385v1 Definition 1, Proposition 2 and full proof, Corollary 4 and full proof, Theorem 5(a,b), printed pp. 2–3; reuse previously inspected Lemma 6/Theorem 7 and Xu–Chen v4 Proposition 2.2 through L043.
COMPARISON: The source separates fibers using a B_4 sequence on distinct point indices; its polynomial construction requires distinct field labels. No inspected theorem proves that mixed column/value moments retain this separation with a small finite image.
GAP: A specific mixed-moment map needs an exact conflict test before any fiber-size claim; no compatible fiber of the required size is established.
REASON: The changed column-aware mechanism is outside ready Gilbert coverage; this literature-only step completes a bounded comparison without deriving or approving a new mathematical result.
SCOPE: Nine-subsets of Omega={0,...,8} times F_107 with all placements of profile (3,2,2,2); the two embedding points are unused. Only a bounded test of the proposed mixed-moment map below is suggested.

## Inspected primary input

Harm Derksen, *Error correcting codes and B_h-sequences*,
[arXiv:math/0311385v1, 21 November 2003](https://arxiv.org/pdf/math/0311385v1),
printed pp. 2–3: Definition 1 requires distinct sums of h indexed
terms, allowing repetitions. Proposition 2 makes each fixed-weight
fiber of the sum map a distance-at-least-2h+2 code. Its proof cancels
common terms and pads equally to h terms, including distances below
2h. Corollary 4 uses pigeonhole over the group. Theorem 5(a) uses
distinct a_i in F_q, P(a_i) nonzero, and degree h; part (b) uses
degree h+1 and quotient by F_q units, adding the identity label.
Its proof is referred to Bose–Chowla rather than supplied. Importing
that theorem would not require an original reproof; the original
reference remains unaudited.

For distance ten the source parameter is h=4. The point indices
here are pairs (c,x), not x alone. The distinct-label hypothesis
must be checked on those pairs. Theorem 5 does not state a
column-compression theorem. Its general group-size guarantee does
not give the proposed restricted-universe image bound. No use of
Corollary 4 with a mixed-moment map is justified until its separation
hypothesis is independently established.

## Reuse, duplicates and failures

The unchanged product and asymptotic comparisons in
`2026-10-10-compatible-four-column-augmentation.md` are reused:
equal inner weights/constituent-code requirements and the ineffective
finite cutoff remain obstacles to citing them for this guarantee.
L043 imports the quartic graph baseline; L045 records the full
profile universe size 18244718624781348840. ATTEMPTS/027–029 and
history/132 retain the resource, prescribed Derksen and Gilbert stops.
Their lower-bound shortfalls are not upper bounds on possible fibers.
Targeted searches of these assessments and attempts found no completed
mixed-moment compatibility test. No cross-notebook input is used.

Queries actually submitted included `constant weight codes algebraic
construction elementary symmetric polynomials multisets columns syndrome
packing`, `multiply constant weight codes algebraic construction unequal
weights syndrome`, `constant weight codes syndrome Graham Sloane
algebraic`, `generalized packing algebraic construction unequal weights
finite fields`, and the quoted phrases `constant weight codes` with
`power sums`, `multiply constant-weight` with `algebraic` and `syndrome`,
and `constant weight` with `mixed moments`. Search hits were discovery
leads, not theorem evidence. The q-ary code hits concern a different
symbol model; they were not imported. The previously located
Graham–Sloane scan remains an unread lead, not an essential blocker
for a bounded test independent of its theorem. No novelty or
nonexistence conclusion follows from this search.

## One proposed discriminating mathematical test

On the auxiliary labeled columns c=0,...,8 in F_107, propose
Phi(B)=(sum x, sum x^2, sum x^3, sum c*x), summing over (c,x) in B.
This is a proposed map, not a proper coloring established here.
The next test must prove separation for every distinct same-syndrome
pair in the profile universe or exhibit a full conflicting pair.
Start with cyclic reassignments of three values among the three
size-two columns, retaining the size-three column and the other
points; this specifically tests information lost by the first three
coordinates and restored, if sufficient, by the last coordinate.
No equality, counterexample or size calculation is claimed this turn.

If a complete nine-set conflict is found, park this map only; do not
rename or vary its coefficients during that attempt. If separation
is proved, certify its finite image bound and the pigeonhole lower
certificate against 5774752369. A failure to find a collision in a
bounded search does not establish separation. Save complete evidence
and all profile/intersection checks in a later research step.

The main gap remains arbitrary-center 67/68 safety. A successful
packing would feed L041/L042's cap-route comparison, not supply an
RS list. Essential local inputs are L043's imported baseline and
L045's profile definition/count. Actual-label transfer, cross-core
consistency, common-center realization and ABF comparison remain
unresolved. Mathlib coverage is not checked. No lemma or mathematical
script was changed; no new mathematical theorem was derived.
