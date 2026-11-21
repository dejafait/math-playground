# Real-zero boxes and the coefficient torus — completed source comparison

TARGET: Assess whether, at r=2 and k=1, the original coefficient torus can be replaced by a finite oriented sum of L845 separated real-zero boxes in relative homology, with equality of the full holomorphic-form integrals.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Targeted contour/box records contain no relative-class test; reused the joint-angular-contour assessment and its automatic-sign stop. Searched relative de Rham, singular-divisor integration, semialgebraic-chain comparison and exact Xi/Katkova terminology; inspected the primary statements and relevant proof cases listed below. No exact replacement theorem was located; this is not a novelty claim.
SOURCE_EVIDENCE: Hatcher, Algebraic Topology (2002), Section 2.1 pp115–117, relative-chain definition/Theorem 2.16; Shartser–Valette arXiv:1002.4143v1 (22 February 2010), Definitions 2.2/2.10/2.14, Proposition 2.13, Theorem 3.6 pp12–14; Edmundo–Woerheide institutional manuscript revised 4 September 2006, Theorems 1.1/1.2 and real-field comparison paragraph pp2–3, Section7 pp30–31. Exact links, hypotheses and reading scope below.
COMPARISON: Known finite relative-chain and stratified-integration frameworks cover the proposed test after explicit compact semialgebraic reduction. They do not identify the actual torus class with box classes, compute their periods or supply signs. Normal-crossing and global semialgebraicity assumptions must not be silently imposed on Z.
GAP: The local application remains to be proved: finite-support reduction, relative closed-form restriction on every divisor branch, periods with orientations, and the full-form pairing. No invariant, integral value, class obstruction or replacement has been derived this turn.
REASON: Essential source coverage now supports a bounded relative-period test of participation. A separating period would stop finite-box replacement only; failure to separate would not establish replacement. The new covered continuation requires separate next-turn approval before mathematics.
LITERATURE_REASON: The invocation-start assessment was REVIEW_REQUIRED: relative-chain comparison and integration across singular divisor intersections were essential unread inputs. Existing contour coverage did not supply them.
SCOPE: Ordinary finite singular chains with integer coefficients in the specified pair; compact semialgebraic comparison and bounded smooth ambient forms, real and imaginary parts separately. No infinite-chain, thimble, growing-order, phase-sum or positivity theorem is covered. This turn is literature-only.
COVERED_TARGET: Test the r=2,k=1 finite real-zero-box replacement by a relative period invariant, retaining the full holomorphic form and proving the finite-support and integration-pairing qualifications.

## Original nomination: specified objects and limitations

Use the actual G and R_1 from L775 and exactly F_2 from L845 (4).
Let X=(C minus zero)^2 and let Z be the zero set in X of
G(z_1)G(z_2)(z_1-z_2). The candidate coefficient cycle is the product
of the two positively oriented circles |z_j|=R_1. The candidate box
chains are the images of the ordered, separated real-zero boxes of
L845 under (t_1,t_2) -> (-4t_1^2,-4t_2^2), with their induced real
orientations. Their boundaries lie in Z by construction. The full
form to retain is F_2 dz_1/(i z_1) wedge dz_2/(i z_2). This merely
specifies the proposed objects using the existing coordinate
identity; no integral over a box has been evaluated.

Review ordinary finite singular relative chains with integer
coefficients in (X,Z), not an unstated infinite or locally finite
sum. The future bounded test asks whether the image of the torus
class can equal a finite integer combination of these box classes
and whether such a relation is sufficient for equality of the full
form integrals. The source review must check well-definedness of
both classes and the integration pairing, regularity at the
intersections of zero divisors, the noncompact ambient space, and
the infinite but locally finite actual zero set. Do not remove zeros
as poles or discard the volume-form factors. If a general theorem
already decides the test, import it with its hypotheses rather than
reprove it. Search the notebook's relevant contour/topology records
for duplicates and failures before approving a calculation.

Continue only to a precise theorem application or independently
testable finite-cycle obstruction/construction under complete source
coverage. A contradiction from a valid relative invariant would stop
this **finite-box replacement**, not all contours or infinite-chain
representations. If a class relation is obtained, its integral
applicability must still be checked; a sign does not follow from
stationarity. If essential sources remain blocked, park this test.

Plausible downstream use: a positive result could supply a genuine
participation interface for the smallest interacting determinant; a
negative result could rule out finite real-box replacement before
spending effort on all-r saddle estimates. Growing-r control, sums
of phases, signed remainders, other shifts and the main
L030–L032/C032a mixed-positivity gap would remain unresolved.

The original nomination requested a new topological participation
mechanism. Its missing-source status is superseded by the comparison
below; its mathematical question remains unanswered. No cross-notebook
input; Mathlib matching coverage remains unchecked.

## Inspected primary inputs

[Allen Hatcher, *Algebraic Topology*, Section 2.1,
pp115–117](https://pi.math.cornell.edu/~hatcher/AT/ATch2.pdf#page=19),
defines relative singular chains for arbitrary pairs by the quotient
of chain complexes. A null relative cycle is a boundary plus a chain
in the subspace. No compactness, smoothness or good-pair hypothesis is
required for this definition or the pair exact sequence obtained from
Theorem 2.16. Read that definition, the algebraic exactness argument and
the pair-sequence application. Good-pair quotient-space formulas are
not needed. Thus meeting the diagonal does not invalidate a torus
cycle in (X,Z); this is not a cycle in X minus Z.

[Leonid Shartser and Guillaume Valette, *De Rham Theorem for
L-infinity forms and homology on singular spaces*,
arXiv:1002.4143v1](https://arxiv.org/pdf/1002.4143v1#page=7),
Definitions 2.2/2.10/2.14, Proposition 2.13 and
[Theorem 3.6, pp12–14](https://arxiv.org/pdf/1002.4143v1#page=12):
compact semialgebraic sets, continuous semialgebraic simplices,
bounded smooth stratified forms with bounded exterior derivative and
matching tangential restrictions. Differential forms need not be
semialgebraic (p2). Integration is independent of stratification and
satisfies Stokes. Read the definitions, integration proof, and the
complete Stokes proof, including its regular boundary and lower
dimensional exceptional-set cases. Only this chain-level input is
needed; the full de Rham isomorphism proof is not imported.

[Mário J. Edmundo and Arthur Woerheide, *Comparison theorems for
o-minimal singular (co)homology*, institutional manuscript revised
4 September 2006](https://repositorioaberto.uab.pt/bitstreams/e3125e0f-316c-403f-b987-e0d9aecc5aca/download#page=3),
Theorems 1.1/1.2, pp2–3, and the real-field comparison paragraph
immediately after Theorem 1.2 identify definable and ordinary
homology naturally over the real field, for pairs and coefficient
modules. Read Section7, pp30–31: triangulation compatible with the
subspace, compact subcomplex reduction, the pair exact sequence and
naturality. Use the semialgebraic structure over R with parameters;
integer coefficients are allowed. The inclusion comparison must
retain the represented torus and box classes, not merely an abstract
group isomorphism. Published citation: *Trans. Amer. Math. Soc.*
360 (2008), 4889–4912, DOI10.1090/S0002-9947-08-04403-6.
The inspected theorem/page numbering is the institutional manuscript's,
not asserted to be the publisher's pagination.

## Applicability and remaining mathematical work

The source interface is adequate for a **finite** test, with the
following local specializations to be written out in the research
attempt. These are proof obligations, not completed new results.

* Place the torus, finitely many boxes and every chain witnessing a
  proposed relative equality in a compact product of annuli avoiding
  zero. Justify this for ordinary continuous singular chains. Do not
  assume a global finite list of G zeros or replace ordinary chains
  by locally finite chains.
* For that compact setting, use L775's nonzero entire G and the
  isolated-zero input already cited in L845 to identify the finite
  coordinate-zero divisors and diagonal. Check that the resulting
  compact pair is semialgebraic with parameters, even though G itself
  is transcendental. Include all relevant complex G zeros, not only
  the negative-real ones. The reduction must work for an arbitrary
  hypothetical finite relation, not one fixed cutoff.
* Use compatible strata at all intersections, including points where
  vertical, horizontal and diagonal branches meet. No assertion that
  this is a simple normal-crossing divisor is needed or approved.
  Verify bounded ambient forms and their tangential restrictions;
  multiplicities of zeros do not license removing those points.
* Apply the comparison to the actual relative representatives, using
  real or complex cochains as appropriate. An obstruction over real
  coefficients suffices to obstruct an integer relation; no converse
  or torsion claim is authorized. Verify the integration functional
  descends to relative chains using the cited Stokes input and the
  restriction on Z. This finite-chain application replaces the need
  for a general singular holomorphic de Rham isomorphism.
* Retain omega=F_2 dz_1/(i z_1) wedge dz_2/(i z_2), with F_2 exactly
  as in L845 (4), and the induced orientations under t -> -4t^2.
  A proposed class relation must justify equality of omega integrals.
  An auxiliary invariant must not be substituted for this full form.

There is no source theorem here specifically asserting or refuting the
finite L845-box replacement. Necessary applications to this pair and
period evaluations are deliberately deferred. Citations suffice for
the general topology/integration inputs; reproof of those theorems is
unnecessary. L845's stationarity is geometric context, not an assumption
implying the relative relation. The source review permits independent
gaps to remain: nondegeneracy, saddle participation beyond finite boxes,
phase sums, uniform signed remainders, other shifts, and all-degree
mixed positivity in L030–L032/C032a.

## Bounded test and route

After separate approval, try to construct one closed ambient 2-form
whose relative pairing distinguishes the coefficient torus from the
entire finite span of the specified boxes. The logarithmic form
dz_1/z_1 wedge dz_2/z_2 is a candidate to test, not an evaluated or
accepted invariant. Require complete branch restrictions, period
calculations and the compact comparison above. This investigates a
participation obstruction instead of repeating stationary-point
existence or an absolute-complement estimate.

Decisive continuation/abandonment test: a valid separating period stops
finite-box replacement; a valid class construction must also pass the
full-form pairing. If the candidate form fails a restriction or fails
to separate, record that failure without inferring a class relation.
Do not escalate to infinite sums or another automatic sign argument.
No class equality, inequality of periods, integral identity or sign
has been derived in this literature turn. The next task is a bounded
proof attempt, contingent on separate approval of this changed coverage.

## Search, reuse and unused leads

Reused `2026-11-06-joint-angular-contour-signed-remainder.md` and
`ATTEMPTS/2026-11-06-joint-contour-automatic-sign-transfer-source-stop.md`.
Read L845's exact density and boundary construction and L775's G/radius
definitions. Targeted searches in contour/box assessments and failures
for relative homology, relative cycles, logarithmic forms and the new
authors found no completed duplicate test. No sibling notebook was read.

Queries included `relative de Rham theorem singular divisor integration
smooth singular chains analytic subset triangulation`, `subanalytic
chains smooth singular homology integration Stokes triangulation theorem
relative differential forms`, `Edmundo Woerheide comparison semialgebraic
singular homology classical theorem pdf`, `Riemann xi relative homology`,
`Katkova homology determinant`, and `holomorphic real boxes relative torus
integral`. No exact match from the last queries is evidence of novelty.

Bloom–Herrera was a lead only; its theorem was not inspected.
Brasselet–Pflaum's Annals PDF was opened for scope but supplies no input
here. A relative-Stokes publisher PDF and the AMS comparison URLs failed
access; the institutional manuscript resolved the essential comparison,
so no essential source blocker remains. The theorem statements and
relevant proof cases, rather than snippets, support the decision.
Full matching Mathlib coverage is unchecked; a search hit about a
Hatcher formalization was not used as Mathlib evidence.

No lemma, mathematical script, DAG or PROOF argument was changed.
This is local source-coverage progress, not a new topological result
or an advance on RH beyond the sources checked.
