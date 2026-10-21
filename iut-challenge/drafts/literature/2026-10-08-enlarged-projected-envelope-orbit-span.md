# Enlarged projected shell-envelope orbit span — completed source comparison

TARGET: Determine the Z_3-span of the finite-word Gamma orbit of q((pi J_L/6) intersect V), including its scalar level relative to q(M) and dependence on the admitted presentation.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared the exact target with L026's finite-sum proof, L031's complete basis, L033's exact quotient action, L034's full trace intersections, L035's same-space method and ATTEMPTS/020,022–024. Six focused external queries for residual-irreducible orbit lattices, exact enlarged-field logarithms and quotient factors found general stable-lattice literature but no inspected matching input-scale theorem; queries and source distinctions are recorded below.
SOURCE_EVIDENCE: Freshly read Brinon–Conrad, June 24 2009 preliminary notes, Definition 1.2.5/Lemma 1.2.6 and complete proof p. 7, https://math.stanford.edu/~conrad/papers/notes.pdf; Stacks Lemma 10.31.4(2), tag 00FM, and Lemma 10.20.1(2),(4), tag 00DV, statements and relevant proofs; Sehanobish (2019) section 3.1 setup/Corollary 3.1.9 and full sketch pp. 26–28. Reuse previously inspected Kondo even-degree actions, complete-logarithm inputs and Bürgisser–Kulkarni–Lerario intersection/quotient/interlacing coverage with locators below.
COMPARISON: Known bounded orbit-sum and same-space residual-irreducibility methods apply over Q_3 in arbitrary finite rank; audited L033/L035 provide precisely the free rank-106 quotient and action. Known full-intersection/quotient and relative-factor tools cover the changed input's lattice obligations. They do not compute its embedded scalar level or prove that one admitted presentation has the same level as another; L026's odd-degree scale and L035's container escape cannot be transferred.
GAP: In a separate research turn, form the full integral trace intersection of pi J_L/6, prove fullness and bounded finite generation of its projected finite-word span, apply the existing same-space method, and determine the scalar level or its rigorously justified dependence on the actual fixed line. No input-scale, presentation-independence, radius or orbit-escape verdict is established here.
REASON: The changed target now has sufficient essential coverage for a bounded specialization of known lattice methods. The needed field-specific difference is independently testable from the genuine basis and trace functional without freely assigning reciprocal coordinates; further source browsing is unnecessary before that test.
LITERATURE_REASON: The saved changed-input assessment was REVIEW_REQUIRED; essential orbit-span coverage and its actual-line applicability had not yet been compared. This completes that comparison rather than reopening the ready L035 target.
SCOPE: Exactly TARGET for L031's genuine enlarged J_L, L033's admitted finite-word reference subgroup and actual primitive line; full integral trace-intersection and relative-factor calculations, projected finite-sum span obligations, known same-space homothety, scalar-level and presentation-dependence tests. No new group-image theorem, prescribed coordinates, field valuation on the quotient, numerical enclosure or original-IUT realization.

## Scope of the proposal retained from the audit turn

Use L=Q_3(zeta_20,pi), pi^27=3, the genuine J_L=log(O_L^times),
V=ker(Tr_(L/Q_3)), M=J_L intersect V, and exactly L033's admitted
reference subgroup Gamma. Use its actual y_1, W=Q_3 y_1 and q:V->V/W.
The proposed orbit span consists of ordinary finite Z_3-linear sums of
finite-word images of q((pi J_L/6) intersect V); no compact closure
is part of the definition. Whether that span is a full lattice, is
scalar-homothetic to q(M), and has a presentation-independent scale
are obligations to assess and then prove, not assumptions or conclusions
of this proposal.

Essential local inputs for assessment are L031's complete genuine
logarithm lattice, L033's exact integral quotient action, L034's full
trace lattices and L035's audited method. Compare L026 only as an
odd-degree methodological precedent, not as an enlarged-field theorem.
Any detailed reads should be limited to the corresponding proof cases.
The already recorded original-input source blocker does not prevent
this strictly auxiliary local test; it remains parked.

The plausible downstream use is an input-specific projected span that
can later be compared with a stated scaled integral container. This
would still require a separate finite-sum-to-orbit attainment argument
for any claimed escape and an independently justified numerical target.
No radius-81 prescription is imported into this enlarged field here.

Continue if assessed methods allow an exact scale, or a sharp uniform
range sufficient to distinguish containment in a later specified
container. If the scale depends on unprovided presentation coordinates,
record precisely that dependence and test whether invariant bounds
resolve it; do not choose reciprocal coordinates arbitrarily or iterate
the unchanged qualitative nonpreservation proof. A proved obstruction
to uniformity is an informative outcome, not an IUT counterexample.

ATTEMPTS/020's prescribed-coordinate stop, ATTEMPTS/022's unchanged
packet exclusion, ATTEMPTS/023's scalar-transport failure and
ATTEMPTS/024's whole-kernel reducibility remain valid. No O_U-linearity,
extra shear, exponent twist, larger group or descended field valuation
is permitted. Actual/native membership and actions, fixed-line numerical
control, packet/global realization, pilot transport, essentiality and
the original finite B>=A remain unresolved. This new target is not
derived or approved in the completed L035 audit turn.

## Completed theorem-level comparison, 2026-10-08

**Orbit sums.** Brinon–Conrad, *CMI Summer School Notes on p-adic
Hodge Theory*, preliminary version June 24, 2009, Definition 1.2.5
and Lemma 1.2.6, printed p. 7 ([primary notes](https://math.stanford.edu/~conrad/papers/notes.pdf)),
assume a continuous profinite action on a finite-dimensional Q_p-space.
Their complete proof takes a finite sum of images of a starting lattice
using its open stabilizer and compactness. It establishes stable-lattice
existence, not a field-specific scale or set-orbit equality. The stabilizer
display's Lambda denotes the starting Lambda_0. Here the scalar field is
Q_3, and the representation is the actual rank-106 quotient. Compact
closure is optional: prefer L026's bounded algebraic finite-sum method,
checking its hypotheses afresh for the changed input.

**Finiteness and scalar homothety.** [Stacks Lemma 10.31.4(2)](https://stacks.math.columbia.edu/tag/00FM),
with its proof via finite presentation of the quotient, requires a
Noetherian ring and an ambient finite module. It covers finite generation
of a bounded orbit submodule over Z_3. Boundedness must first be proved;
this citation does not provide it. [Stacks Lemma 10.20.1(2)/(4)](https://stacks.math.columbia.edu/tag/00DV)
requires finite generation and an ideal in the Jacobson radical. Its
determinant argument and quotient proof were inspected. These hypotheses
support the existing normalized-inclusion argument over the local DVR
Z_3; an unbounded or merely dense span would not suffice.

Sehanobish, *Universal Deformations and p-adic L-functions*, Maryland
PhD dissertation (2019), section 3.1, printed pp. 26–28
([primary dissertation](https://api.drum.lib.umd.edu/server/api/core/bitstreams/9c358dab-b72f-47fa-924c-da55d0ae1ea6/content)),
sets up continuous compact/profinite representations. Corollary 3.1.9
states uniqueness of a stable lattice up to homothety under residual
irreducibility. The freshly inspected sketch ends with a GL_2 matrix
and abstract isomorphism; that ending alone is insufficient for same-space
equality in rank 106. Reuse L035's audited normalized-inclusion/Nakayama
argument as the justified general-rank reproduction. Serre's referenced
Exercise 4 remains unread and is not an essential input. Neither this
source nor Nakayama computes the input's scalar level.

**Integral intersections and projections.** Reuse the primary inspection
record in `drafts/2026-10-08-enlarged-projected-container-source-review.md`:
Bürgisser–Kulkarni–Lerario, *Nonarchimedean integral geometry*, Selecta
Mathematica 32:10 (2026), version of record January 5, 2026, section 2.2
pp. 13–14, Lemmas 3.1.4(1–3)/3.1.5 pp. 21–23 and Proposition 4.1.2
pp. 35–36 ([primary publication](https://doi.org/10.1007/s00029-025-01120-y),
[primary PDF](https://d-nb.info/1395945926/34)). Over a local scalar field,
intersections with rational subspaces and images in rational quotients
are full lattices. Quotienting a linear map's target by dimension d
gives sigma_i >= sigma''_i >= sigma_(i+d). Both minimax cases and the
duality proof were previously read; Lemma 3.1.4 leaves its proof to the
reader, and Lemma 3.1.5 gives the Smith-form proof. Retain the recorded
minimax cross-reference numbering qualification. Use only the
target-quotient assertion, not the simultaneous-deletion corollary.

For a future relative-factor test the domain lattice must be the full
T=(pi J_L/6) intersect V, with target lattice M in a second copy of V;
the linear map is the identity followed by q, with target lattice q(M).
It may have negative factors; the sources impose no nesting. Its
nonzero factors describe the full image q(T), rather than inventing a
field valuation on V/W. Voight, *Quaternion Algebras*, GTM 288 (2021),
Theorem 9.3.9 supplies simultaneous relative factors over a DVR
([primary chapter](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_9));
reuse the same prior inspection. Comparing the first surviving factors
under a one-dimensional quotient is an assessed uniformity test, not a
calculation performed here. Necessary bounds alone cannot establish
realizability of a chosen line or presentation.

**Exact action and field input reuse.** Kondo, arXiv:2512.09231v2,
December 12, 2025, section 1, Theorem 1.3 and the even-degree proof,
printed pp. 9–11 ([versioned primary text](https://arxiv.org/html/2512.09231v2#S1)),
is already assessed in the quotient-action review. Its odd-p, even-degree
paired/adjacent cases cover p=3,d=108 and all 53 pairs. L033 supplies
integral quotient reduction and audited irreducibility for precisely
those finite-word actions. L035 supplies M intersect W=Z_3 y_1 and the
full projected lattice. No fresh action extraction or larger image is
needed. L031 supplies the genuine complete basis and deep ideal; L034
supplies the full trace functional 27(4,-1,-1,-1,0,...,0) and complete
M. Their proofs/citations remain canonical. Only the coordinate-model,
complete-table, integral-intersection and action/method passages needed
for comparison were read; no certificate was rerun or preview used as
verification. L026's odd-degree bound and separator are method evidence,
not enlarged-field inputs.

## Discovery, decision and next-step boundaries

Queries actually submitted: `"p-adic" "orbit" "lattice" "residually
irreducible"`; `"logarithm" "lattice" "zeta" "27" "Q_3"`;
`"stable lattices" "irreducible" "homothety"`; `"Q_3(zeta_20"
logarithm orbit lattice`; `"lattice" "quotient" "elementary divisors"
"interlacing" p-adic`; `"lattice generated" "orbit" "irreducible"
p-adic`. Results included the already known Sehanobish criterion and
rank-two Garcia/Warwick notes, plus unrelated root-lattice and geometric
orbit material. Garcia and the Warwick notes were not inspected as
primary theorem evidence and are not imported. Reuse the earlier
Ophir–Weiss Proposition 2.5 comparison from the L026 assessment:
boundedness of invariant homothety classes does not determine an embedded
input scale. Its later maximal-lattice results remain unread. No exact
matching enlarged-field theorem was inspected; failed searches do not
establish novelty.

L026 decides a different field without a fixed-line quotient. L035
decides container nonpreservation from an unspecified container input.
Neither duplicates this target. ATTEMPTS/020,022–024 were read narrowly
and remain preserved. The actual/native source blocker remains parked;
it is not essential to this strictly auxiliary lattice question.

Decision **SPECIALIZE** approves only the unchanged TARGET for a later
mathematical invocation, subject to the supervisor's separate approval.
Recommended mathematical classification: **REPRODUCTION** of known
lattice methods with an exact local calculation, not a claim beyond
the literature checked. No lemma or mathematical script was modified
and no new span, scale or uniformity theorem was derived this turn.
Continue if the complete intersection and projected-factor tests give
an exact level or a useful uniform range; if coordinates still matter,
record the precise dependence and do not assert that arbitrary lines
are admitted presentations. A failed necessary method is not an IUT
counterexample. Fixed-line numerical control, actual/native membership
and action compatibility, packet/global realization, pilot transport,
essentiality and finite B>=A remain open. Matching/supporting Mathlib
coverage for this target is **not checked**, not asserted absent.
