# Opposite multiple collision — completed curvature source comparison

TARGET: Assess a pointwise Gauss-curvature obstruction to three quaternionically dependent branches of L118's opposite image.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched hyperkahler curvature/Sym4, quaternionic totally geodesic curvature invariance, three-branch and nonorthogonal rigidity, and exact references below; compared L118/L121, the saved point-separation assessment and ATTEMPTS/047/070. Found explicit general curvature and Gauss-Codazzi inputs, but no inspected theorem deciding the prescribed three-line compatibility problem; no novelty inference follows.
SOURCE_EVIDENCE: Kramer--Semmelmann--Weingart dg-ga/9703021v1, Section 3, especially Lemmas 3.3--3.5 and their complete proofs, PDF pp. 7--11; Semmelmann--Weingart math/0001061v1, Section 2 and Lemma 2.3, PDF pp. 5--9; Rozansky--Witten hep-th/9612216v1, Sections 2.1--2.2, PDF pp. 9--11; Chen Riemannian Submanifolds, Sections 3.1--3.3 and 11.1--11.2, PDF pp. 14--16 and 127--128; Hitchin--Sawon math/9908114v1, Section 2, PDF pp. 3--4.
COMPARISON: Known algebraic curvature descriptions and the combined Gauss-Codazzi identity cover the framework; the remaining specialization is simultaneous compatibility, including vanishing normal curvature components, arbitrary actual angles, quaternionic reality and the retained common scale. No inspected source supplies that joint answer or a collision exclusion.
GAP: The three-line linear compatibility space and its restriction range have not been computed. Actual K3 curvature values and collision angles are unknown; algebraic compatibility would not establish a hyperkahler germ, F, or an actual collision.
REASON: Approve only a bounded pointwise algebraic test using these imported tools. Do not reprove curvature classification, retry gluing sources, infer pointwise nonzero curvature from global nonflatness, or promote a formal tensor to geometric existence.
SCOPE: Conditional L118 opposite map with L120 normalization and L121 distinct quaternionic tangent lines; only three distinct preimages of one stable image point whose tangent lines span a quaternionic two-plane, with the original source metric and common scale 2lambda retained.
COVERED_TARGET: Compute the real pointwise Gauss-Codazzi compatibility space for three distinct quaternionic tangent lines spanning a two-plane in L118's opposite image.
LITERATURE_REASON: Essential primary curvature coverage was absent for this changed target at invocation start; this completes that coverage without a mathematical attempt.

## Review result and precise remaining work

The main gap remains universal primitive rational Hodge realization. The
intermediate target is a necessary condition on a conditional triple
collision, potentially useful for image separation or later gluing analysis.
It leaves F existence, double collisions, other tangent spans, actual image
defects, reconstruction and transverse transport unresolved. This turn
is EXPLORATION / LITERATURE / NOVELTY_UNCHECKED: it completes source
comparison and specifies a test, but proves no new compatibility result.

Import [Kramer--Semmelmann--Weingart, *Eigenvalue Estimates for the Dirac
Operator on Quaternionic Kaehler Manifolds*, dg-ga/9703021v1, 27 March
1997, Section 3](https://arxiv.org/pdf/dg-ga/9703021v1#page=7), especially
Lemma 3.5, equations (3.10)--(3.13), PDF pp. 10--11. Its proof handles
the H-symmetric, E-symmetric and mixed sectors, using Lemma 3.3's
dimension-dependent injectivity and Lemma 3.4's five Bianchi equations;
all those proof cases, PDF pp. 7--11, were read. The resulting curvature
is a scalar-curvature term plus the fourth-symmetric-power part. The
ambient quaternionic dimension here is 39, within its n>=2 hypothesis.
Do not use the quaternionic-Kahler Einstein argument to justify the
four-dimensional source case. For hyperkahler curvature in all dimensions
use the directly inspected [Rozansky--Witten, hep-th/9612216v1,
Section 2.1, equation (2.4)](https://arxiv.org/pdf/hep-th/9612216v1#page=9),
PDF pp. 9--10: holonomy, pair interchange and algebraic Bianchi give
the symmetric four-tensor. Section 2.2, p. 11, separately treats
differential Bianchi; no covariant-derivative condition is silently
replaced by an algebraic identity.

Use [Semmelmann--Weingart, *Vanishing Theorems for Quaternionic Kaehler
Manifolds*, math/0001061v1, Section 2 and Lemma 2.3,
equations (13)--(15)](https://arxiv.org/pdf/math/0001061v1#page=5), PDF
pp. 5--9, for positive quaternionic reality, symplectic raising and
lowering, the explicit curvature action and its Ricci trace. A complex
symmetric four-tensor alone is not a real Riemannian tensor; retain the
real form induced by the positive quaternionic structure. The theorem
is imported; no local reproof is needed. The algebraic model supplies
no prescribed metric germ. [Hitchin--Sawon, math/9908114v1,
Section 2](https://arxiv.org/pdf/math/9908114v1#page=3), PDF pp. 3--4,
independently describes symplectic lowering and the fourth-symmetric-power
interpretation; no characteristic-number theorem from that paper is needed.
The cited arXiv identifiers fix the versions; some PDFs have later internal
TeX compilation dates, which are not treated as new source versions.

Import the named Gauss and Codazzi equations, with their combined identity
in [Chen, *Riemannian Submanifolds*, Section 3.1, equations (3.1)--(3.7),
PDF pp. 14--15](https://www.math.stonybrook.edu/~bishop/classes/math638.F20/Chen_Riemann_Submanifolds.pdf#page=14).
The integrability computation in (3.4) retains both tangent and normal
components. Thus the intended test must retain the complete vector-valued
curvature matching of a totally geodesic isometric immersion, not only
four-tangent scalar contractions. Equation (3.6) has a missing ambient
tilde in this PDF; (3.4) unambiguously fixes the meaning. Sections 3.2--3.3
were checked too: the printed existence theorem concerns space forms,
and cannot realize our hyperkahler data. Apply the isometric statement
to L118's source metric 2lambda g, with its actual differential. A
unit-frame computation must account for this scaling explicitly.

For the stronger rigidity comparison, Chen's named Cartan theorem in
Section 11.1, PDF p. 127, tests parallel-translated curvature along every
short tangent geodesic, not just curvature at its center. Section 11.2,
pp. 127--128, concerns locally symmetric spaces and retains that
hypothesis. These statements do not give the sought pointwise collision
exclusion. Their existence/rigidity conclusions are not invoked. The
saved Verbitsky/Soldatenkov comparison already controls separate local
branches and normalization without separation; its adequate coverage is
reused rather than browsed again.

## Approved specialization and stopping test

The exact covered continuation above is one algebraic attempt. Take the
three actual scaled quaternionic derivatives at a hypothetical collision
in the single common L118 chart. At fixed embeddings, use the real
hyperkahler algebraic curvature space from the cited formulas and impose,
for each branch, its intrinsic curvature matching together with the
normal-component equations from Gauss-Codazzi. Determine the allowable
triples of source curvature tensors. These are unknown input values,
not three independently selected tensors subsequently attributed to B.

The ambient tangent is quaternionic dimension 39; only the line span has
dimension two. Before reducing the algebra to that span, justify any
orthogonal compression and extension being used. Do not assume that
the span itself is an ambient curvature-invariant subspace. Retain
positive quaternionic reality and arbitrary line configurations; a
nonunitary change to coordinate/diagonal lines changes the metric and
is not an allowed angle normalization. Do not assume the three source
curvatures agree in chosen frames. These are applicability checks for
the future attempt, not results derived in this review.

Continue if this calculation yields a necessary restriction on actual
curvature triples beyond the existing tangent and metric information.
For a universal pointwise exclusion based merely on nonzero source
curvature, the discriminating test is whether an admissible configuration
supports nonzero induced curvature on all three lines. If it does, park
that universal exclusion; this would not settle compatibility with the
actual three unknown K3 tensors. If only a vanishing condition results,
it still cannot exclude collisions without a separate pointwise curvature
input. Algebraic feasibility is never a hyperkahler-germ or F-existence
theorem. No such feasibility test, rank, witness or obstruction has been
computed this turn.

## Search scope, access and duplicates

Queries included `hyperkahler curvature tensor Sym4 E Salamon curvature
module totally geodesic`, `hyperkahler totally geodesic submanifolds
curvature invariant quaternionic lines Gauss equation`, `hyperkahler
curvature symmetric fourth power`, `hyperkahler curvature invariant
three`, `quaternionic totally geodesic nonorthogonal curvature`, and
the exact titles of the primary papers above. Search-only results on
Grassmannian/symmetric-space classifications were not imported. No
novelty claim follows from a missing match.

Tsukada's 1996 publisher metadata was accessible, but substantive PDF
retrieval and screenshots timed out. Salamon's 1982 full text was also
inaccessible. Both remain unread leads, not inspected stronger theorems.
The accessible complete Kramer--Semmelmann--Weingart proof and direct
hyperkahler formula remove any essential dependence on those retrievals
for this algebraic attempt; do not schedule another access retry. No old
gluing-source blocker was reopened. Full matching Mathlib coverage is
not checked, and no absence claim is made.

L122 and ATTEMPTS/070 stop only the flat-data minimal-defect inference;
ATTEMPTS/047 stops the selected compatible index mechanism. This test
adds curved source data but presumes none of their missing conclusions.
L118, L120 and L121 are the essential local inputs; L119 is a comparison
only. No lemmas, mathematical scripts, DAG or PROOF.md were changed.

## Initial proposal retained (superseded by the completed review)

The following proposal was REVIEW_REQUIRED at invocation start. It is
preserved as the original scope; the comparison and bounded approval
above supersede its missing-source status.

## Exact prospective test and its limits

Essential local inputs are L118, L120 and L121. Retain their conditional
rank-two locally free Omega-polystable F on the identical marked K3
product, integral c_1(F)=0 and ch_2(F)=-14e_1-21e_2-tau_D. In one actual
smooth harmonic-moduli chart take a hypothetical triple x_1,x_2,x_3 of
distinct preimages of m. Write P_i=df_(x_i)(T_(x_i)B). Only the case
of three distinct P_i spanning quaternionic dimension two is proposed.
No orthogonality, equal angles, diagonal normal form, or equality of
the three source curvature tensors is assumed. L118 fixes the metric
scale 2lambda for every derivative, with 1<lambda<5/4.

Review primary Gauss-equation and hyperkahler curvature results with
their exact algebraic symmetries and essential proof cases. Determine
whether they give an independently testable condition for one ambient
curvature tensor to restrict on these three totally geodesic branches
to the three actual source curvature tensors, using the actual scaled
derivatives. Compare any stronger local rigidity theorem, and record
whether it needs local symmetry, completeness, special angles, or
nonzero curvature assumptions not available here. Do not infer an
applicable theorem from a name or a search snippet.

The main gap is universal primitive Hodge realization. A possible
downstream use is an additional necessary condition on multiple
collisions of this conditional image, where the flat quotient test
cannot decide actual gluing. This would still leave F existence,
double collisions, other tangent configurations, normalization defect,
reconstruction and transverse transport unresolved.

Continue only if the source comparison supplies a precise restricted
curvature compatibility test not already implied by the retained
quaternionic/metric data, or an exact explicit compatibility test whose
outcome can park the mechanism. Abandon a universal pointwise exclusion
if inspected coverage admits the required nonzero curvature restrictions
under the retained hypotheses. Distinguish arbitrary algebraic curvature
compatibility from realization by a hyperkahler germ or by this actual
F. Global K3 nonflatness gives no assumed nonzero curvature at each of
the three points, and no values of the actual tensors are presently
computed. Missing numerical or geometric source data must be recorded,
not replaced by freely chosen tensors and then attributed to B.

## Recovery comparison

Three directions were compared without undertaking additional mathematics:
(1) actual-image coherent cohomology through its normalization quotient
still depends on unknown simultaneous gluing, so ATTEMPTS/070 parks the
automatic minimal-defect input; (2) for numerical normal-bundle indices
from L119, no new mechanism beyond the type tested in ATTEMPTS/047 was
identified in this comparison; no L119 index calculation was performed,
and a rank substitution alone does not justify reopening that mechanism;
(3) the pointwise Gauss test retains the curved source
data discarded by L122 and is independently assessable before any
gluing formula. Select (3), subject to separate literature review.
No inaccessible source from the old gluing comparison is retried.
