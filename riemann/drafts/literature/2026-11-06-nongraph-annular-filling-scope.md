# Non-graph prescribed-collar filling — completed source comparison

TARGET: Assess whether L856's prescribed collars admit, for arbitrarily small r, a smooth embedded annular filling in the same primitive chart with real nonnegative full density and positive original angular projection, allowing the w projection to fold and leave the original annulus.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed bounded external searches for prescribed-boundary Lagrangian immersions, special-Lagrangian Plateau fillings, positive holomorphic forms and angular projection; inspected Haskins-Pacini Definition4.2, Theorem4.6/Remark4.8 and Theorem5.4/proof, and Lebl manifold Stokes. Scoped local comparisons retain L855/L856 and the fixed-cutoff and scalar-flux stops. No inspected theorem settles this exact class; search failure establishes neither novelty nor nonexistence.
SOURCE_EVIDENCE: Haskins-Pacini, Geometry & Topology10(2006)1453-1521, arXiv:math/0609352v4 (22April2009 typesetting corrections), Definition4.2 p1487, Theorem4.6/Remark4.8 p1489, Theorem5.4/proof p1501, https://arxiv.org/pdf/math/0609352v4 ; Lebl SCV v4.4 (31May2026) TheoremC.6/displayed-domain proof p224 and Theorem1.2.1/proof pp20-21, https://www.jirka.org/scv/scv.pdf ; reused Lebl Basic Analysis I v6.3 Theorem7.5.6 p290/Lemma4.2.2 pp162-163 and Basic Analysis II Theorem8.3.7 p38 from the local stationarity assessment; supporting OpenStax Calculus3 Theorem4.16 inspected directly.
COMPARISON: Relative Lagrangian h-principles supply conditional exact immersions in a nondegenerate standard symplectic space, without the requested embedding, real-full-density sign, angular inequality or divisor-crossing conclusion. General manifold Stokes applies without a w-graph hypothesis. Together with extrema and positive-integration inputs it supports a finite angular-observable test, whose primitives, boundary integrals and strict separation remain unproved.
GAP: Determine whether one tangent-normalized linear observable of the fixed angle lifts separates the collar periods from all permitted fillings. Interior extrema, ambient primitives on the entire fixed chart, boundary signs and small-radius errors require a separate mathematical attempt; this review establishes no separator or filling.
REASON: The generic immersion lead cannot be imported as a filling theorem. Essential standard-tool coverage for a narrower angular test is available; its ready continuation awaits separate supervisor approval and was not executed in this literature-only turn.
LITERATURE_REASON: The non-graph class was outside the approved graph audit and lacked an inspected prescribed-boundary comparison; this completes missing coverage rather than repeating ready-target browsing.
SCOPE: Exactly TARGET for the fixed actual-G pair, fixed finite n>=1, fixed primitive chart B and the two exact L856 collars; no higher-moment sequence, full-torus construction or all-degree positivity claim.

## Precise proposed class and relevance

Keep L855's hypotheses zeta eta!=0, G(zeta)=0 of finite multiplicity
n>=1, G(eta)(zeta-eta)!=0, the fixed chart B and omega=w^n dw wedge dv.
For each proposed radius r use exactly L856's two collar surfaces,
including their given orientations, not just their periods. Ask for a
smooth embedded compact oriented annulus in B agreeing with relative
open portions of both collars. Its original angular two-form
dTheta_1 wedge dTheta_2 must be strictly positive, and the restriction
of omega must be real nonnegative in that orientation.

The surface need not be a graph over w, and its w image need not lie
in r/2<=|w|<=r. It must remain in the same fixed B and in its fixed
logarithm branches; it is not allowed to leave the coordinate domain.
Zeros of w and of the restricted full form are retained. Existence
for arbitrarily small r, with the fixed pair and n, is the proposed
question, not an established fact. Boundary agreement only in periods,
an immersed surface, or positivity after deleting a divisor would not
answer it. No mathematical implication for this class was derived in
the preceding audit.

Such a filling, if justified, would identify a possible geometric escape
from the one-chart graph obstruction, a component relevant to later
contour assembly. A valid obstruction would close that specific escape.
Actual exterior Xi data, global homology and matching, exchange symmetry,
other orders and L030-L032/C032a all-degree mixed positivity remain
independent unresolved obligations.

## Source-review discriminator and stopping rule

Inspect primary theorem hypotheses and essential proof cases before
importing any relative surface or filling statement. Existing
[planar Stokes](https://www.jirka.org/scv/scv.pdf#page=205) and
[positive-measure necessity](https://arxiv.org/pdf/1809.00584v1#page=12)
are supporting tools, not a filling theorem. L847's inspected
[manifold Stokes input](https://www.jirka.org/scv/scv.pdf#page=224)
is a lead for a general boundary calculation; it does not settle this
existence question. Full matching Mathlib coverage is unchecked.

Continue only if source review supplies an applicable theorem with
checkable hypotheses or one bounded independently testable construction
or obstruction target for this exact surface class. Otherwise park
this extension and record the missing essential input. Do not approve
a broad gluing claim from an h-principle search snippet, claim novelty
from unsuccessful searches, or escalate through higher moments.

This nomination compares repeating the completed graph audit, reopening
the stopped fixed-cutoff equation, and changing the projection class;
only the last is proposed for assessment. No central creative proof
attempt is yet justified: actual exterior matching data and a tested
mechanism linking such a surface to the all-degree signs remain absent.
The separate source review must decide whether this proposal yields a
real discriminator before any creative routing. Prior stops and
exploration counts are preserved.

## Completed source review — 6 November 2026

The nomination above is retained as specification and history. No filling
or obstruction for the enlarged class is derived in this review.

### Closest relative theorem

Inspected Mark Haskins and Tommaso Pacini, *Obstructions to special
Lagrangian desingularizations and the Lagrangian prescribed boundary
problem*, Geometry & Topology 10 (2006), 1453-1521,
DOI 10.2140/gt.2006.10.1453, in the
[author arXiv PDF, v4](https://arxiv.org/pdf/math/0609352v4).
The [version record](https://arxiv.org/abs/math/0609352v4) identifies v4
as 22 April 2009 typesetting corrections to the published version.
References below use printed journal pages, not upload dates.

Definition 4.2 (p1487) requires compact connected oriented L, trivial
complexified tangent bundle, and exact Lagrangian collar data. Theorem
4.6 (p1489) assumes an extending Lagrangian monomorphism holonomic near
the boundary, and returns an exact immersion fixed there. Remark 4.8
explains the Legendrian-lift proof and the collar exactness requirement.
Theorem 5.4(2) and proof (p1501) require the boundary Maslov class to
extend from the surface; the connected-boundary shortcut does not apply
to an annulus. Its proof removes the second obstruction in dimension two.

These theorems do not ensure embedding or the additional positivity and
angular constraints. Their nondegenerate ambient setting gives no passage
through our retained divisor. Conversion of these collars into their
exact initial data has not been established. Thus no filling is imported.
The referenced Eliashberg-Mishachev sections remain unread leads.

### Inspected and reused tools for a finite discriminator

Reopened Jiří Lebl, *Tasty Bits of Several Complex Variables*, v4.4,
31 May 2026, [Theorem C.6 and displayed-domain proof, p224](https://www.jirka.org/scv/scv.pdf#page=224).
Stokes applies to compact smooth oriented embedded manifolds with
boundary and smooth forms, using induced orientation. The proof case
uses the fundamental theorem of calculus and checks its boundary sign.
No coordinate-projection injectivity is required; complex forms are
handled componentwise. Smooth ambient primitives remain to be verified.

Also reopened [Theorem1.2.1/proof, pp20-21](https://www.jirka.org/scv/scv.pdf#page=20):
joint holomorphic power series converge absolutely uniformly on compact
subpolydiscs, with the converse. Reuse L855's parameter-dependent primitive
method on the original product neighborhood. Primitives needed for a
future test must cover all of the unchanged B, not a smaller replacement
chart; no such new weighted primitive is derived here.

Reuse the inspected extrema and chain-rule coverage in
`2026-11-06-actual-g-real-zero-interval-stationarity.md`:
[Lebl Basic Analysis I v6.3, Theorem7.5.6 p290](https://www.jirka.org/ra/realanal.pdf#page=290),
[Lemma4.2.2 pp162-163](https://www.jirka.org/ra/realanal.pdf#page=162), and
[Basic Analysis II Theorem8.3.7 p38](https://www.jirka.org/ra/realanal2.pdf#page=38).
These supply compact extrema, coordinatewise Fermat and chain rule.
The directly inspected [OpenStax Calculus3 Theorem4.16](https://openstax.org/books/calculus-volume-3/pages/4-7-maxima-minima-problems)
confirms the multivariable statement. Reuse L856's positive-integration
coverage. Their application to the fixed angular observable is unproved.

### Searches, duplicates and the selected discriminator

Queries actually submitted included:

- `special Lagrangian surfaces prescribed boundary holomorphic volume form Lagrangian Plateau problem annulus`;
- `positive holomorphic volume form surfaces boundary symplectic rotated complex structure hyperkahler`;
- `"Lagrangian" "prescribed boundary" "h-principle" surfaces`;
- `"holomorphic" "two-form" "nonnegative" "surfaces" Lagrangian boundary`;
- `"special totally real" "boundary" filling`;
- `"positive" "angular projection" "holomorphic" annulus filling`;
- `"prescribed boundary" "holomorphic volume" "nonnegative"`;
- `"Lagrangian" "boundary" "convex hull" volume form`.

Additional degree/winding and holomorphic-Poincare searches supplied no
essential input. Petersen's manifold notes were opened only as a lead;
no theorem from them is imported. Plateau, calibration, split-special-
Lagrangian and boundary-rigidity search hits remain unread leads.
Search snippets and abstracts do not approve their applicability.

Read L856 in full, L855's joint-chart/model/angle proof, L847's full-form
statement and audit, the positive-annular assessment, the scalar-flux
stop and its decision history. Scoped searches of the 6 November collar
literature, stops and histories found no prior tangent-normalized
angular-separator calculation. The stationarity assessment covers Fermat,
not this surface test. No novelty inference follows from these searches.

Compare three mechanisms: the relative immersion theorem does not cover
the constraints; the planar w-support test repeats L856 under a removed
hypothesis; the still-required angular transversality offers a distinct
finite necessary-condition test. Select only the last. Fix one observable
from L855's already computed angular tangent, without a higher-moment
sequence. Its exact target and application obligations are saved in
`2026-11-06-nongraph-angular-observable-test.md` for separate approval.
No separation estimate, new primitive identity, existence or nonexistence
is established today. If that single test fails, park it.

## Mathlib and relevance limits

Inspected official [LocalExtr.Basic documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/LocalExtr/Basic.html#IsLocalMax.hasFDerivAt_eq_zero):
`IsLocalMax.hasFDerivAt_eq_zero` assumes a real normed space, an actual
Fréchet derivative and a local maximum, and concludes the derivative
vanishes. This is coordinate-level support, not a matching annular
theorem. Full matching coverage and other formal ingredients are unchecked.

Main gap remains L030-L032/C032a actual-Xi all-degree mixed positivity.
A local obstruction could close only this particular escape from L856;
actual exterior data, matching, global homology, exchange and other orders
remain independent. No central creative RH mechanism is justified without
those data and a tested link to signs. No cross-notebook input was used.
