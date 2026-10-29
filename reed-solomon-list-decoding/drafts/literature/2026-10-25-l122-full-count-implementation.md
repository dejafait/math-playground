# Full-H count implementation — completed scope review

TARGET: Implement and certify the full-H ordered disjoint-pair collinearity count using L122, retaining every star, vertical and antipodal case and checking both unexcluded incidence moments.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed queries, primary-source reads and duplicate/failure comparison in 2026-10-24-labeled-collinear-pair-triple-count.md and the approved reduction assessment; targeted local searches of L122, its check script, the working draft and histories 466–467 found reduction/small-field evidence only, not a completed actual-field count.
SOURCE_EVIDENCE: Read L122 in full and L020's predicate/examples, C001a, foundations/02 and ATTEMPTS/010; reuse Murphy–Petridis https://arxiv.org/pdf/1601.03981v3 Lemma 1, printed p.2 and full Section 2 proof p.5, and the inspected comparisons https://arxiv.org/pdf/1701.06192v2 Definition 1.1/Theorem 1.2/Lemma 2.4 and https://arxiv.org/pdf/2003.03493v1 Section 3/Theorem 5.2, as recorded in the count assessment.
COMPARISON: L122 already proves the exact fixed-field reduction and resource bounds; the new work is its reproducible integer implementation and complete actual-field certificate, not a new incidence theorem. Murphy–Petridis supplies only the unexcluded second-moment check; the Cartesian-product bounds still do not match the labeled point set.
GAP: Implement and independently check the actual-field occupancies and exact weighted count; no source supplies that saved numerical certificate, and this review performs no computation or new derivation.
REASON: Existing coverage suffices for this bounded implementation of L122; no changed mathematical hypothesis requires fresh external discovery, and no core/link or threshold transfer is licensed.
SCOPE: Exactly TARGET, using L122's proved formula, endpoint exclusions, orbit multiplicities and arithmetic bounds; implement its finite algorithm and certificate checks without new mathematical reductions or extremal estimates. The next research classification is REPRODUCTION.
LITERATURE_REASON: The newly saved actual-count implementation was REVIEW_REQUIRED and required a separate scope comparison; this turn reuses adequate inspected sources rather than repeating discovery on an already ready target.

The proposal below was saved before this separate literature-only review.
It was not ready at proposal time. The completed review below now approves
its unchanged target and stated scope; no absence of a matching exact-count
source is evidence of novelty.

Main gap: arbitrary-center 67/68 safety. The proposed intermediate target is
the exact whole-H count T defined in L122. Plausible downstream use is a
certified density diagnostic for L020. A total density does not imply a
uniform bound after deleting a 61-point core, a bound on selected support
families, supersaturation, threshold saving or an RS list realization.

Essential inputs: L122's full proof, L020's determinant predicate, C001a's
unchanged 955–957 bracket and foundations/02's pinned list convention.
Retain the genuine antipodal examples in ATTEMPTS/010 and all prior
transfer stops. No cross-notebook input or current L121 certificate is used.
Mathlib matching count/implementation coverage remains not checked.

If separately approved, the implementation should save complete actual-field
histograms for every representative and the vertical/horizontal passes,
the subgroup/coset partition and exact per-line-class subtotals. Verify the
exceptional star occupancies, eligible matching bounds, the two known
contributions in L122 (2), widened integer arithmetic and both unexcluded
incidence moments. An independently expressed pair-generation or histogram
check should make the certificate stronger than an unexamined printout.
The continuation test is an exact reproducible count with no failures and
transparent multiplicities; a failed moment, omitted degeneracy or resource
failure must be preserved and repaired or must stop this implementation.
No actual numerical value, extremal estimate or new lemma is approved here.

## Completed source and scope comparison, 2026-10-25

The prior count assessment records the exact queries and inspected primary
theorem/proof cases. Reuse those reads: no new external search or theorem
extraction was needed. Murphy and Petridis, *A Point-Line Incidence Identity
in Finite Fields, and Applications*, arXiv:1601.03981v3, 20 February 2016,
Lemma 1 (printed p.2; complete Section 2 proof p.5), applies to any subset
of the affine plane over F_q and sums over all affine lines. Its diagonal
and distinct-point cases include vertical lines. L122's injective pair image
is such a subset, with q=65537 and N=523776; its orbit weighting applies to
the unexcluded sums as well. Import that known second-moment identity by
citation. The first-moment diagnostic and exact third-count expression are
already specified in L122; no general incidence identity needs reproof.

The versioned 2017 and 2020 Cartesian-product comparisons in the reused
assessment retain their coordinate-set and nonzero restrictions and their
unspecified asymptotic constants. They do not replace L122's endpoint-labeled
count or certify its numerical value. Their essential cases were already
inspected; no additional passage is essential to this implementation scope.
Unread leads remain noninputs. Matching Mathlib implementation/count coverage
and supporting incidence coverage remain **not checked**.

The narrow duplicate check confirms that the existing L122 script explicitly
does not compute full-H histograms. The reduction working draft and session
467 also reserve that computation. L020 supplies both singular antipodal
examples and nonsingular examples; ATTEMPTS/010 therefore still refutes
universal exclusion. The prior global/core transfer assessments retain the
missing labeled supersaturation/cardinality step; the inspected 2026-10-06
comparison also records an unavailable parameter interval for its proposed
pair-supersaturation input. This count neither repairs nor assumes those
steps. L031 remains a nearby realizability criterion, not a count input.

Implementation acceptance requires complete representative, vertical and
horizontal occupancy arrays saved on disk, not just summaries. Retain the
unexcluded star bins for both moment checks, but omit their third-count
contributions exactly as L122 prescribes. Check every histogram mass, the
subgroup/coset partition, exceptional occupancies, eligible matching bound,
the two explicit contributions in L122 (2), and widened integer arithmetic.
An independently expressed pair-generation or histogram replay must compare
complete relevant data, with all failures saved. These are checks of the
existing formula, not additional unproved mathematics. The packed main-array
bound in L122 does not bound interpreter objects or saved certificate size;
record actual storage choices without claiming a measured bound in advance.

Continue only with an exact reproducible count and all checks passing. A
failed moment, omitted degeneracy, independent-replay mismatch or resource
failure must be preserved and repaired before accepting a count, or stop
this implementation. No small-field preview substitutes for the actual-field
certificate. A count may be recorded canonically in a later research turn;
this review writes no lemma or mathematical script and derives no new result.
Independent audit, core uniformity and threshold transfer remain outside scope.
