# Completed coverage — simultaneous formal collision linearization

TARGET: Determine whether all branches at a finite opposite-image collision admit simultaneous formal holomorphic linearization under L118/L120/L121.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Jentsch Weingart Kähler normal coordinates totally geodesic submanifolds Theorem 4.6 Corollary 4.9, Higashijima Itou Nitta 0203081 Kähler normal coordinates submanifold totally geodesic, and Kähler normal coordinates totally geodesic formal; compared scoped history/376--383, the prior four-branch assessments and ATTEMPTS/070--072.
SOURCE_EVIDENCE: Read Jentsch--Weingart, Asian J. Math. 24 (2020), Theorem 4.6 statement p. 388 and complete proof pp. 389--391, Definition 4.8 and Corollary 4.9 pp. 391--392; Higashijima--Itou--Nitta hep-th/0203081v3 Section 3.1 equations (3.1)--(3.3), (3.7)--(3.8), PDF pp. 7--9; Stacks 0C0S and 07N9 statements and proofs.
COMPARISON: Published anchored-coordinate compatibility already covers each totally geodesic complex submanifold in a fixed ambient chart; the inspected degreewise construction supplies the formal scope needed here. The remaining work is specialization to all actual completed algebraic branch maps, not a new general linearization theorem.
GAP: Write the common-chart applicability and completed-pullback comparison under L118/L120/L121; retain source reparametrizations and distinguish a formal coordinate automorphism from a convergent chart. No actual-image all-orders result is proved in this review.
REASON: Essential coverage is ready for one separate mathematical specialization; neither a reproof of the general coordinate theorem nor a new mathematical mechanism is needed.
SCOPE: Finite opposite-image collisions under the unchanged conditional L118/L120/L121 setting, without limiting the number of branches or their tangent-span dimension; no F existence, global defect bound or collision exclusion is included.
COVERED_TARGET: Determine whether all branches at a finite opposite-image collision admit simultaneous formal holomorphic linearization under L118/L120/L121.
LITERATURE_REASON: The startup gate requires coverage of the enlarged all-orders target; the newly essential submanifold-compatibility corollary and its formal existence construction were not assessed for that scope by the second-jet review.

## Proposed intermediate target and relevance

The universal primitive rational Hodge-realization gap remains open.
The proposed target asks for one formal ambient holomorphic coordinate
system in which each completed branch image is its tangent plane;
independent formal source reparametrizations are permitted. This would
allow later normalization-defect calculations to use the full tangent
arrangement rather than new higher normal-jet data at each branch count.
It does not itself compute those arrangements or give a global bound.

Essential inputs are L118 (the actual common connection and parametrized
geodesy), L120 (finite normalization) and L121 (distinct quaternionic
lines). L126 and audited L127 supply comparisons and the already-settled
four-branch result; they do not prove the new target. Retain rank-two
locally free Omega-polystable F, integral c_1=0 and
ch_2=-14e_1-21e_2-tau_D on the identical marked K3 factors, normalized
pullback scale 2lambda and ambient quaternionic dimension 39. F and
collision occurrence remain unproved. A finite collision is assumed;
no global completeness or real-analytic metric premise is added.

## Primary theorem and proof cases inspected

Jentsch--Weingart, [*Riemannian and Kählerian normal coordinates*,
Asian J. Math. **24** (2020), 369--416,
doi:10.4310/AJM.2020.v24.n3.a1](https://archive.intlpress.com/site/pub/files/_fulltext/journals/ajm/2020/0024/0003/AJM-2020-0024-0003-a001.pdf#page=20):
Corollary 4.9 concerns every totally geodesic complex submanifold of a
Kähler manifold and restricts the ambient anchored coordinates to its
tangent subspace. Its proof is left to the reader. Theorem 4.6 gives
universal composition polynomials in the complex structure, curvature
and its covariant derivatives. Its complete induction, equations
(26)--(29), includes the quadratic base, partial inversion of the
formal Laplacian and removal of the holomorphic ambiguity by the
potential normalization. The final paragraph on p. 391 constructs
successive anchored approximations by homogeneous holomorphic flows.
Definition 4.8 uses a smooth torsion-free connection, parallel complex
structure and curvature of type (1,1). These are the relevant formal
proof cases, not a convergence estimate. The claim on p. 372 that all
Kähler metrics are real analytic is not imported.

Higashijima--Itou--Nitta, [*Normal Coordinates in Kähler Manifolds
and the Background Field Method*, hep-th/0203081v3,
17 June 2002](https://arxiv.org/pdf/hep-th/0203081v3#page=7), Section 3.1,
equations (3.1)--(3.3) and (3.7)--(3.8), supplies an independent
all-degree formal coordinate formula with identity linear part and
the pure holomorphic connection-derivative normalization. The
coefficients are evaluated at the centre. This reading does not
establish convergence for arbitrary smooth metric jets. Section 2.2's
nonholomorphic real-exponential terms prevent replacing holomorphic
coordinates by real Riemannian exponential coordinates.

The exact theorem and stronger standard terminology were searched;
secondary results and search snippets were discovery leads only.
The alternate publisher URL initially failed, but the archive publisher
PDF was accessible and its complete relevant proof was read. There is
no essential source-access blocker. The arXiv preprint 1707.06379 was
located but is not an additional inspected proof version.

## Application boundaries for the separate mathematical turn

L118 conclusions (3)--(4) supply the actual holomorphic immersion and
one common smooth hyperkähler connection germ. The finite collection
of locally embedded images must be treated as separate submanifold
germs through the same point; the singular whole image is not the
submanifold in Corollary 4.9. The source metric induced on each branch
is 2lambda g. No completeness, compact ambient metric, real-analytic
metric premise or global embedding is available. The next proof must
check the theorem's applicability with these exact data, including
the source connection, and use one fixed ambient anchored construction.
It must not choose a different ambient coordinate change per branch.

The required formal comparison is the identity
`k_M^{-1} o f_i o k_i = df_i`, where k_M is the single formal ambient
anchored chart and the k_i are formal source charts. This is the test
to establish next, not an identity derived by this literature turn.
Its pullbacks must describe the actual completed branch ideals.
No arrangement interpolation, defect length or global consequence is
part of the approved target.

[Stacks Lemma 10.160.10(2), 0C0S](https://stacks.math.columbia.edu/tag/0C0S)
requires a complete Noetherian regular local ring with a coefficient
field inducing its residue field; its proof uses any cotangent basis
as power-series parameters. Apply only to the smooth source and
ambient local rings, not to the singular image ring.
[Stacks Lemma 10.97.8, 07N9](https://stacks.math.columbia.edu/tag/07N9)
requires a finite ring map over a Noetherian ring and identifies the
completed finite algebra with the product of its local completions
over the selected prime. L120 supplies the finiteness input. These
sources do not themselves assert compatibility with analytic branch
maps: the next proof must compare Taylor series in algebraic regular
parameters, including the invertible linear part and the same actual
map. Formal changes need not be algebraic or convergent. The earlier
completion coverage is otherwise reused without a new source search.

## Duplicate/failure comparison and decision test

The targeted history/376--383 search and the prior normal-jet
assessments found only a proposed all-orders continuation. L127 is
the completed second-jet result, not this target. Its arbitrary-branch
comparisons in L126 omit common geodesy and are not counterexamples
with the retained hypotheses. The earlier inaccessible all-orders
gluing lead recorded in the four-branch assessment is a different
source; this coordinate target does not depend on it.

ATTEMPTS/070 stops minimal defect from pairwise data, and
ATTEMPTS/071--072 stop the specified curvature tests. Formal
linearization would not imply pairwise-minimal normalization defect.
Those stop decisions remain intact. No prior result or unfinished
work is withdrawn. Full matching Mathlib coverage remains not checked;
unknown coverage is not absence.

Continue with exactly the saved target by importing the cited
compatibility theorem and writing its formal application. A valid
common-chart identity for every actual completed branch is the success
test. A surviving formal normal component, failure of a required
connection hypothesis or failure to match actual pullbacks blocks
that import and must be recorded explicitly. Do not repair such a
failure by assuming convergence, analyticity or independent ambient
charts. F existence, collision occurrence, tangent-arrangement defect
computations, global exclusion and universal Hodge realization remain
independent unresolved problems.

This completed step is LITERATURE / REPRODUCTION / EXPLORATION:
coverage has changed from REVIEW_REQUIRED to SPECIALIZE, but no new
lemma or actual-image linearization has been established. Any later
successful application is a specialization of known mathematics,
without a claim of progress beyond the inspected sources.
