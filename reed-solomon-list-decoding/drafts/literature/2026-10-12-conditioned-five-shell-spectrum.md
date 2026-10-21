# Full conditioned distance-five shell — proposed strength test

TARGET: Test L053's unchanged trial on the full singleton-conditioned half-distance-five shell, including the anchor and the exact (5,5,3,2) incidence override, by a complete stabilizer spectral certificate.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 172 searched Johnson scheme tensor product distance shell eigenvalues Eberlein constant weight Schrijver; Johnson subconstituent product scheme; constant-weight triple product semidefinite Schrijver; Johnson singleton moment distance five; and the Bannai–Zhu shell-paper title. Scoped ATTEMPTS/012–015,018,033–035 and the two global-triple assessments retain distinct prior stops; no exact fixed-trial certificate was located and no novelty is inferred.
SOURCE_EVIDENCE: Reused foundations/04,12 for the union program; freshly inspected Brouwer–Haemers author preprint Section 1.4.7 p. 19 and Section 11.2 pp. 162–163, Schrijver Theorem 1 (51) and III.A (52)–(59) pp. 6–7 including the full restriction proof, and Brouwer–Cioaba–Ihringer–McGinnis arXiv:1709.09011v2 Sections 1.2,3,3.4 pp. 3,10,12; Theorem 2.7.1(i) p. 36 covers the anchor. Canonical source additions: foundations/09-global-pair-johnson-source.md.
COMPARISON: Known tensor/block and Johnson spectral inputs cover a complete exact strength test on this one shell and its anchor; L053 certifies only small principal matrices, while L023/L024 test a different unmodified assignment. None of the inspected sources supplies PSD signs for L053's incidence-zero trial or a useful uniform bound.
GAP: Research must verify the shell-to-product relation dictionary and normalization, reconstruct every coefficient including Boolean repetitions and the override, evaluate every spectral mode and the anchor Schur coordinate, and justify the resulting fixed-trial implication; no shell calculation is performed in this review.
REASON: Separate approval of the unchanged target is complete: known primary spectral inputs suffice and only the finite trial specialization remains. Import those results without reproof; a citation alone cannot determine this trial's exact signs.
SCOPE: Only the fixed rational L053 trial and one full half-distance-five shell plus its singleton anchor; no optimization over pairs, averaging of labeled feasible points, other shells or full-SDP feasibility.

The main gap remains arbitrary-center safety at 68 agreements, with
67 agreements independently open. The intermediate target is a reliable
strength diagnostic for one full conditioned matrix. A negative exact
spectral coordinate would exclude L053's fixed trial from a necessary
larger relaxation and motivate a separately reviewed repair or bound.
A complete nonnegative spectrum with the anchor condition would park
this shell as an exclusion test. Neither outcome alone proves safety,
unsafety or a uniform bound for arbitrary moment assignments.

Fix any 68-support A and use the union-matrix indices {A} and {A,B}
for every 68-support B satisfying |A\B|=5. The proposed entries are
exactly L053's moments of the unions of these index sets. Do not replace
the repeated B=C values by the distinct-triple formula, omit the anchor,
or restore the pre-L053 value at (i,j,t,s)=(5,5,3,2). The trial has a
stronger all-incidence zero prescription; its label-independent definition
does not license stabilizer averaging of the actual labeled relaxation.
The review must distinguish a symmetry of this specified matrix from
a symmetry of the general feasible set.

## Recovery comparison and bounded decision

Three mechanisms were considered without calculating any of them:

1. The entire distance-five conditioned shell: selected because it checks
   simultaneous PSD beyond every retained three-index test and contains
   the changed incidence orbit. A primary spectral reduction would make
   it independently testable with exact arithmetic. The old (0,0) and
   (0,1) stops apply to a different trial; they do not settle this test.
2. Anchor-free three-index conditioned matrices: distinct omitted
   constraints, but requiring a new four-support incidence coverage and
   repetition analysis. Defer in favor of the more explicitly specified
   single-shell matrix. No failure or feasibility is asserted.
3. A uniform optimization with free pairs and labeled triple moments:
   directly useful for the main gap, but currently missing a justified
   finite reduction or concrete dual search. L051/L052's failed fixed
   pair prescriptions cannot replace such an optimization. Defer.

The small-principal exclusion route is exhausted by audited L053 and
preserved in ATTEMPTS/035. Its source approval is complete, so another
approval of that same target is not a recovery action. The blocked ABF
definition comparison remains parked; the selected finite-shell test is
independent of it. No source access is retried in this research turn.

The original step-171 proposal required a separate literature invocation.
Step 172 supplies that comparison below and approves the unchanged target
for a subsequent research invocation. No mathematics was invoked while
its coverage was REVIEW_REQUIRED.

Essential inputs are L001, C001a, L020–L023 and audited L053, with
foundations/04,09,12 and the existing global-triple certificates.
Continue to a bounded exact calculation only after separate coverage
approval. A failing coordinate needs a reconstructible exact witness;
a passing claim needs every shell eigenspace and the singular anchor
case. General pair choices, other conditioned matrices, representing
measures, a useful uniform list bound and RS realization remain open.
Mathlib full matching and supporting coverage have not been checked.

## Separate primary comparison — step 172

LITERATURE_REASON: The full conditioned shell is outside the ready small-principal audit scope; the essential product decomposition and anchor case required separate theorem comparison before calculation.

This is a literature-only source import and comparison, not a proof of
shell feasibility or infeasibility. The trial in L053 was read to delimit
the changed orbit and repetitions; its certificates were not recalculated.
The mathematical overview and DAG are unchanged.

The precise known inputs, hypotheses, inspected cases and citations are
recorded in foundations/09, with union-program coverage in foundations/12
and the orbit qualifications in foundations/04. Brouwer–Haemers gives
the tensor eigenvectors and full product spectrum in Section 1.4.7,
and the complete common factor eigenspaces and constant projector in
Section 11.2. Schrijver's (53)–(58) supplies the tensor change of basis
and restriction to equal head/tail weights; its extension/reset argument
through (59) verifies completeness of the restriction. Thus the proposed
fixed-layer computation has primary coverage for nontrivial modes as
well as the constant mode. No hierarchy or spectral theorem needs a
local reproof. The source's averaging application and qualified
complement prefactor are unnecessary for this fixed-matrix test.

For applicability, the candidate shell indices are exactly the ordered
pairs of five-subsets (A\\B,B\\A) in the 68-point head and 956-point
tail, as in Schrijver's identification preceding (60). Consequently
the factor parameters to use are (68,5) and (956,5), both satisfying
n>=2d. The assessed sources cover all factor eigenspace indices 0–5
and all relation indices 0–5, including the identity relation. Research
must justify the concrete entry dictionary against L053's eight-region
description, rather than assuming a new equality based only on total
distance. In particular (5,5,3,2) is one product relation, not every
triple with three half-distances equal to five.

The union program is reused at order three with singleton anchor A.
The source allows all {A,B} indices; selecting a whole shell together
with {A} is a principal restriction of its conditioned matrix. For this
trial the anchor leading entry is the positive singleton moment rho,
and the anchor/shell entries are L053's prescribed pair moments.
Brouwer–Haemers Theorem 2.7.1(i) applies after division by rho and
inverts only the leading scalar 1. It requires no nonsingular shell
block and retains zero spectral coordinates. Research must include
that congruence and the constant-mode correction, not infer anchored
PSD from the anchor-free spectrum. Boolean repetition B=C uses the
pair moment; it cannot use the distinct-triple product recipe.

The specified trial's symmetry can be checked directly from its
incidence/half-distance recipe. It is not the group average of a
general labeled feasible point. Full L020-incidence zeros, including
realizable incidences, remain a trial choice. Actual-label restrictions
cannot be averaged using the full head/tail permutation group merely
because this particular trial is invariant. Polak's separate
constraint-preserving averaging hypothesis remains unchanged.

## Discovery and duplicate comparison

The queries in SEARCH_EVIDENCE returned established tensor/Johnson and
Terwilliger methods, not a checked certificate for these rational
coordinates. Bannai–Zhu, *Tight t-designs on one shell of Johnson
association schemes*, European J. Combin. 80 (2019), 23–36,
DOI 10.1016/j.ejc.2018.02.024, is a relevant product-shell lead.
Only its indexed abstract was accessible; a direct publisher open
failed. Yan Zhu's author presentation, *Relative t-designs on one shell
of Johnson association schemes*, JCCA 2018, 21 May 2018,
[primary slides](https://infoshako.sk.tsukuba.ac.jp/jcca/JCCA18/slides/2_YanZhu.pdf),
was inspected for the shell definition and theorem statements on
displayed slides 2 and 7. Those design theorems are not imported:
L053 has no relative-design hypothesis. The full journal proof and
its Martin/Dunkl/Tanaka references remain unread and nonessential,
since Schrijver's inspected tensor restriction already provides coverage.
The Kyoto RIMS report search extract was not readable as a primary PDF
through the repository endpoint and is not evidence used for approval.

ATTEMPTS/012–015 retain the old selected-block, zero-block, mixed-block
and scalar passes. ATTEMPTS/018 concerns an occupancy inequality with
fixed shortening coefficients, not this conditioned union matrix.
ATTEMPTS/033–034 exclude other prescribed pair extensions; L053 uses
L021/L022's different pairs. ATTEMPTS/035 stops only the audited
small-principal batch and explicitly leaves larger matrices unresolved.
None decides this changed full-shell test. No stronger applicable
theorem determining this fixed trial was found in the sources inspected;
that does not establish originality or rule out further literature.

## Approved calculation and decision test

The next turn is RESEARCH / REPRODUCTION under this SPECIALIZE scope.
Import the known spectral inputs and justify only the finite
specialization. Reconstruct the complete shell coefficient table from
L053's Boolean union recipe, including the repeated diagonal, all
forbidden distances and the unique incidence override. Retain all
36 product eigenspace pairs and their source multiplicities, check
that their dimensions exhaust the shell, and check the anchored
constant coordinate. Either Johnson eigenvalues or Schrijver's exact
normalized tensor coefficients can implement the reduction; an
independent reconstruction must verify their normalization and entries.
Write full exact evidence to disk and report signs and required bounds,
not approximate eigenvalues or an unverified preview.

A negative exact coordinate excludes only the fixed L053 trial from
this necessary larger relaxation. A full nonnegative spectrum plus
the anchor condition parks this shell only. Stop this bounded test
after either complete verdict; do not tune pairs, triple coordinates
or shell indices in the same step. Any implementation failure stays
unfinished, with no mathematical sign conclusion. Essential local
input IDs are L001, C001a, L020–L023 and audited L053; sources are
foundations/04,09,12. The main gap is still safety at 68 agreements,
with 67 agreements independently unresolved. General pair choices,
other conditioned matrices, representing measures, uniform bounds,
cross-core consistency and RS realization remain open. Required safety
is an upper bound strictly below T=floor(65537^28/2^128)+1; rejecting
one trial does not meet it. Full matching and supporting Mathlib
coverage remain not checked.
