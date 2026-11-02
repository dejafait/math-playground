# Coupled four-state flux: completed source comparison

TARGET: Assess source coverage for a bounded centered full-K law with clipped mean at least 1/288 that annihilates every globally C1 positively degree-two homogeneous four-state storage derivative.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact-class, homogeneous-storage, prescribed-covariance and occupation/closed-measure searches completed; queries and read/unread distinctions below. Reused ready one-height sufficient-method and converse comparisons. No inspected theorem supplies this fixed K and clipping threshold; failed searches imply no novelty.
SOURCE_EVIDENCE: Reused Chernyavsky et al., arXiv:2110.03079v1, Lemma 2.1/(2.4)--(2.11). Reopened Fantuzzi, arXiv:2201.00362v1, Sections 3.1--3.2, Lemmas 5/8 and Proposition 9, PDF p.3, including necessary-constraint proofs. Newly compared Fantuzzi--Tobasco, arXiv:2207.13570v3, (5.1), Theorem 5.1/(H1)--(H2), Corollary 5.6 and its convexification/coercivity proof, printed pp.12--14; Henrion--Korda--Kruzik--Rios-Zertuche, arXiv:2303.02434v1, Definition 2.7/(8), Theorem 3.1 and its disintegration/Jensen/trace proof, pp.4--7.
COMPARISON: Known C1 divergence/weak-bound methods permit vector-valued states, but do not construct the prescribed universal comparison law. Inspected sharpness results require additional integrand, boundary or convexity hypotheses not verified here. L592 supplies all one-height and quadratic four-state cancellation only; Schur covariance completion does not establish the enlarged full-state quantifier. Necessary occupation constraints are distinguished from path realization.
GAP: One common bounded centered law must still meet exact full K, clipping >=1/288 and every allowed coupled storage identity. No inspected result proves its existence or impossibility. A narrower completion test preserving L592's ellipse marginal is covered below; its universal drift condition remains wholly unproved.
REASON: Essential coverage is ready for one separate bounded specialization of the sufficient method, without assuming sharpness, full occupation-measure feasibility or Xi transfer. This turn performs source comparison only; the newly ready continuation requires separate approval before mathematical work.
SCOPE: v=(x_0,y_0,z_0,x_1,y_1,z_1), w=(x_0,y_0,x_1,y_1), dot_w=(y_0,z_0,y_1,z_1), exact L592 K and Q=max(0,x_0 z_0-y_0^2). Seek one bounded centered positive probability law, independent of V, with E vv^T=K, E Q>=1/288 and E[gradient V(w) dot dot_w]=0 for every globally C1 V:R^4->R satisfying V(a w)=a^2 V(w) for a>0. Retain the origin and global R^6 certificate domain; no evenness, convexity, path realization or dual attainment is assumed.
COVERED_TARGET: Test whether L592's elliptical first marginal admits a bounded centered full-K completion that annihilates every globally C1 positively degree-two homogeneous four-state storage derivative while retaining clipped mean 1/(36pi).
LITERATURE_REASON: The changed full-state functional quantifier was explicitly REVIEW_REQUIRED at invocation start. Prior one-height coverage did not assess its occupation constraints or stronger sharpness results; this review fills that scope, without repeating the completed L592 audit or browsing for a quota.

## Main gap, intermediate target and scope of the decision

Actual-Xi all-degree signs at unbounded heights remain the main gap.
The intermediate question is existence of the comparison law in SCOPE.
Such a law would obstruct global sub-1/288 certificates using genuinely
coupled nonlinear storage, beyond the stopped W+U class. It would not
decide general periodic feasibility, generate lag-one jets, or transfer
a sign to Xi. An unsuccessful completion would not establish a cheap
certificate or disprove existence of other comparison laws.

The invocation-start nomination is preserved as the exact TARGET and
SCOPE. This review resolves its source gate only. No law, coupled drift
formula, regularity lemma, new obstruction or mathematical script was
produced. The changed difficulty is one common measure's full-state
functional quantifier, not a new divergence theorem.

## Primary results and their exact comparison

Reuse `2026-10-31-general-homogeneous-storage-scope.md` and
`2026-10-31-general-periodic-clipping-dual-scope.md` for the sufficient
method in Chernyavsky--Bramburger--Fantuzzi--Goluskin,
[*Convex relaxations of integral variational problems*, v1](https://arxiv.org/pdf/2110.03079v1),
Lemma 2.1/(2.4)--(2.11), printed pp.8--10. The assessed bounded
Lipschitz-domain, W^(1,p), C1-field and integrable-divergence conditions
remain applicable hypotheses to check. No reproof or sharpness import
is proposed. The vector-state formulation is already in the source;
the change from two to four storage coordinates is a specialization
obligation, not a claim of a new general theorem.

Fantuzzi, [*Verification of some functional inequalities via polynomial
optimization*, arXiv:2201.00362v1](https://arxiv.org/pdf/2201.00362v1),
Sections 3.1--3.2, PDF p.3: Lemma 5 gives the divergence identity for
generated W^(1,p) occupation/boundary measures and admissible C1 fields
with integrable chain-rule derivative. Reopened (7)--(10), Lemma 8's
entire proof and Proposition 9: (12a) retains boundary flux, (12b,c)
fix spatial marginals, and (12d,e) retain differential/boundary
constraints. The relaxation includes generated measures; the stated
direction is sufficient, not a realization converse. Only this identity
and direction support our later vector-state application. The polynomial
functional-optimization conclusion is not imported for nonpolynomial Q.

Fantuzzi--Tobasco, [*Sharpness and non-sharpness of occupation measure
bounds for integral variational problems*, arXiv:2207.13570v3,
22 April 2024](https://arxiv.org/pdf/2207.13570v3),
(5.1), Theorem 5.1 and Corollary 5.6, printed pp.12--14: the stated
problem has zero Dirichlet data and separated integrand
f_0(x,gradient u)+f_1(x,u). Theorem 5.1 assumes p>1, continuity,
convexity and two-sided p-growth/coercivity (H1)--(H2). Corollary 5.6
allows nonconvex f_0 when n=1 or m=1, retaining convex f_1 and (H2).
Read its convexification proof and growth estimates (5.4)--(5.5);
Remarks 5.3--5.5/5.7 retain their stated extensions. These hypotheses
are not furnished for our periodic paired-jet clipping and prescribed
quadratic moment equalities. One-dimensional time alone does not make
this a matching theorem. No sharpness or optimizer is imported;
the full Theorem 5.1 proof was not read or audited.

Henrion--Korda--Kruzik--Rios-Zertuche, [*Occupation measure relaxations
in variational problems: the role of convexity*, arXiv:2303.02434v1,
4 March 2023](https://arxiv.org/pdf/2303.02434v1),
Definition 2.7/(8), Theorem 3.1/Corollary 3.2, printed pp.4--7:
the test fields in (8) are smooth, with the specified p-growth.
Theorem 3.1 requires closed convex Y,Z, jointly convex objective and
inequality data, affine equality data, and the corresponding boundary
conditions. Read its complete disintegration, weak-derivative,
Jensen/support and trace cases. It recovers a feasible centroid under
those hypotheses; it does not reproduce an arbitrary occupation law's
moments. The hypotheses have not been verified for the fixed full-K
equalities and clipping target. This is a stronger-result comparison,
not a realization input. Its smooth test class also does not silently
replace the target's global C1 class.

Reuse the general-periodic assessment's inspected
Tobasco--Goluskin--Doering, arXiv:1705.07096v2, (1)--(8), (15)/(23):
sharp duality there uses a prescribed well-posed C1 autonomous flow
and compact forward-invariant state set. Neither is specified here.
Reuse the bounded-periodic-occupation assessment's Bernard,
arXiv:math/0701451v2, Definition 28/Lemmas 29--30/Theorem 31,
printed pp.17--19: closed tangent-measure approximation on a compact
connected manifold does not supply our higher-jet support or lag
coupling. The prior switched-system converse comparison also remains
outside scope. None of these theorems supplies the requested K or cost.

## Necessary identities versus the proposed test

The source weak-divergence identity is the template, not a newly proved
full-state reduction. The later specialization must use n=1, m=4,
state w and velocity dot_w as in SCOPE; retain endpoint terms until
periodicity has been checked. The comparison measure need only test
the global certificate inequalities. It is not required to satisfy
every other occupation constraint in Fantuzzi's relaxation.

In particular the target quantifies only over degree-two homogeneous
C1 storage. Requiring cancellation for every C1 storage would be a
stronger sufficient construction goal, not an equivalence imported
from these sources. A failure of an inadmissible test function would
not refute the target. No distributional-divergence characterization,
conditional-drift formula, homogeneous angular reduction, finite-basis
completeness or dual-attainment theorem is assumed here. Any such
local reduction must be proved in the later mathematical attempt.

## One bounded continuation, pending separate approval

The sole mathematical continuation is COVERED_TARGET. Use L592
Sections 2--4's fixed marginal exactly:

    theta uniform on [0,2pi], independent of k;
    P(k=1/12)=1/6, P(k=-7/60)=5/6;
    (x_0,y_0,z_0)=(sqrt(2)cos(theta),sin(theta)/sqrt(6),k x_0).

Its audited centering, K_0, one-height cancellation and
E Q=1/(36pi)>1/288 are reused, not recalculated. Seek a bounded
conditional completion for the second triple, fixed independently of
V. It may change L592's Schur extension, which is only a covariance
template. No claim about that old extension's coupled flux is made.
The test is to meet exact full K and prove the universal full-state
identity in SCOPE. One-height identities and quadratic tests alone
would repeat the completed route and cannot pass.

Essential local inputs: L592's marginal and class; L473 Sections 3--4's
positive K and Schur template; L586's six-coordinate periodic interface;
L588 Section 1's necessary finite-cone implication; L589 Section 2's
quadratic cancellation. The later argument must check global C1
origin/growth and integrability for the enlarged class, centering,
bounded probability support, every cross-lag moment, and one law for
all V. Neither a finite angular sample nor a separate law chosen for
each V proves the target. Ordinary chain rule and finite-dimensional
spectral diagonalization are standard inputs; no source reproof is
needed. No cross-notebook result is used. Matching Mathlib coverage
for the proposed completion is unchecked.

Continue only with an exact common-law construction, a rigorous
informative incompatibility, or a specific refined completion supported
by exact intermediate evidence. An exact obstruction to completions
of this fixed marginal would abandon this narrower mechanism only.
Failure of one completion or a solver run is EXPLORATION, not a
whole-class stop. Save partial reasoning and return after one attempt;
do not also start a certificate optimization or assert periodic/Xi
realization. General periodic feasibility, finite-C_I reserve,
fourth/probability assembly and nonlinear Xi transfer remain open.

## Discovery, duplicates and retained failures

Queries on 2026-10-31: `occupation measures homogeneous auxiliary
functions invariant measures differential constraints convex relaxation
Fantuzzi`; `"holonomic measures" "homogeneous" Lagrangian`;
`"occupation measures" "homogeneous" "degree two"`;
`"stationary" "positive part" "derivatives" "inequality" periodic`;
`"closed measures" "homogeneous" "sphere" dynamics`;
`"homogeneous" "occupation measure" "storage" nonlinear`;
`"positive part" "periodic" "h h" derivative inequality`;
`"homogeneous degree" "invariant measure" "covariance" auxiliary`;
and named-author/title searches for Chernyavsky et al. and
Fantuzzi--Tobasco. No inspected exact match supplies the law.
Search snippets and unrelated results are not theorem evidence.
Fantuzzi's 1906.12136 bounded-domain strong-duality paper was a search
lead only; it was not read or imported and is not essential to this
sufficient-method test. No other unread lead is treated as coverage.

Local failure comparison reuses the quadratic/rational/Gaussian stops
recorded in the general-homogeneous assessment. Read the one-height
storage stop and corrected-law stationary-extension stop records:
L592's W+U obstruction remains valid, while L580/L581 concern other
fixed marginals and stronger path-stationarity requirements. They do
not decide this changed universal homogeneous four-state law. No route
is reopened by discarding its old obstruction. This is literature
EXPLORATION/source readiness, not a new mathematical result.

No justified central-Xi creative mechanism follows from the present
surrogate obstruction: a controlled nonlinear transfer remains missing.
The next task is development of the changed completion test, not a
protected creative central-gap attempt or another audit of L592.
