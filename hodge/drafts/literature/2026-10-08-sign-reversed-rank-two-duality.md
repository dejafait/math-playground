# Changed-sign rank-two transform duality — source assessment

TARGET: Test whether determinant-duality and rank-two simplicity exclude the changed-sign L074 survivors b=-11 and b=-13.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped duplicate/failure comparison of L059/L061, ATTEMPTS/043/045/051 and the saved six-charge assessments; five exact-statement/standard-terminology queries recorded below; primary Stacks duality/sign proofs and Huybrechts's real-Kahler stability/simplicity passage inspected, with reusable Perego coverage retained.
SOURCE_EVIDENCE: Stacks 48.19(2),(9), 0AU3; Lemmas 48.3.6, 0A9Q and 48.15.7, 0BRT with proofs; Section 15.59, 0GWN commutativity differential check, live versions accessed 2026-10-08; Huybrechts, Lectures on K3 Surfaces, author-hosted prepublication draft, Chapter 9 Section 3.1(iii),(iv), printed pp. 175--176, and Theorem 4.9, printed p. 182; reused Perego (2021), Propositions 3.9--3.12 and 3.15, pp. 36--38, from the inspected 2026-10-05 assessment.
COMPARISON: Known proper-smooth coefficient duality and graded signs cover the projection independently of the mixed-character sign; the inspected simplicity statement explicitly covers a complex K3 with a real Kahler class. L059 contains the related stable rank-two form comparison, but its rank-seven residual conclusion and L061's rank-three lifting conclusion are not changed-sign inputs.
GAP: Apply these known tools to the actual L073 image: justify integral determinant trivializations, relative canonical coefficient, trace, both interchange signs and fibrewise perfectness, then compare the resulting duality morphism with rank-two simplicity using L074's exact-h alternatives. No such application or exclusion is established in this source-only step.
REASON: Essential changed-target coverage is now complete for one separate bounded reproduction; only the actual-image specialization remains. No reproof of duality, stability-to-simplicity or connection-morphism theorems is warranted.
SCOPE: L071/L073/L074 with a=-10, b=-11 or -13, full integral -tau_D, identical marked metrics, rank-two locally free product-polystable F and c_1(F)=0; actual G, allowing its initially polystable category. No kernel existence, opposite-projection stability, inverse, spin lift or transverse transport is assumed.

## Test and relevance

The universal primitive-Hodge algebraicity gap and holomorphic product-kernel
existence remain unresolved. This proposed target concerns only two nonflat
numerical survivors. An applicable pairing obstruction could remove them
before any reconstruction or gluing attempt. Compatibility would supply
neither a product kernel nor a cycle. The flat b=-17 case is outside this test;
no assertion about it follows from a negative answer for the nonflat cases.

Essential established inputs for a later attempt are L071, audited L073 and
audited L074, with the exact metric and line lattice inherited through L071.
L059 supplies a coefficient-duality and stable-summand comparison to check,
not a changed-sign theorem that can be directly invoked. L061 and its source
assessment are further source leads only. There is no cross-notebook input.

The source comparison below licenses a later mathematical application. Retain the possible relative
canonical/coefficient line, integral determinant, both interchange signs,
all-fibre perfection and the distinction between a holomorphic pairing and
a compatible connection. Determine what is actually required to test the
stable rank-two alternative; do not impose a projective lifting problem if
ordinary duality already addresses it. No claim of a symmetric pairing on
this G, exclusion, splitting or new lemma is established in this proposal.

The discriminating mathematical test, after source approval, is whether the
actual duality structure is incompatible with the stable rank-two branch
required by the audited exact-h filter. If it is compatible or an essential
hypothesis fails, record the precise obstruction to this argument and stop
this bounded mechanism rather than repeat the character inequalities.

The rank-seven parity/index stop in ATTEMPTS/043 and the nonspin rank-three
lifting stop in ATTEMPTS/045 are preserved. The new object has rank two and
the test compares its own duality with simplicity, rather than repeating
those residual indices or lifting constraints. ATTEMPTS/051's directional
filter remains exhausted. Historical stops are evidence, not global bans.

## Primary sources and hypothesis comparison

**Coefficient duality.** Freshly read [Stacks 48.19(2),(9),
0AU3](https://stacks.math.columbia.edu/tag/0AU3). The setting is finite-type
separated schemes over a fixed Noetherian base. For a proper morphism,
bounded-above coherent A and bounded-below quasicoherent B, it identifies
Rf_* RHom(A,f^!B) with RHom(Rf_*A,B). For smooth proper relative dimension
d, f^!B is Lf^*B tensor Omega^d[d]. Here p_2 is smooth projective of
relative dimension two over a Noetherian complex K3, F is locally free,
and the coefficient B is O_S. The shift and canonical coefficient must
remain in the later application. Neither the mixed Chern character nor
stability enters these hypotheses.

Also read [Lemma 48.3.6, 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q),
including its qualification that the map becomes an isomorphism after
DQ, and its proof via adjunction and the projection formula. Use the
proper coherent formulation above. [Lemma 48.15.7,
0BRT](https://stacks.math.columbia.edu/tag/0BRT) identifies the right
adjoint's value on O_S with Omega^d[d]; its proof uses the smooth
diagonal's conormal bundle and invertibility, retaining the dimension
shift. These are supporting proofs, not extra existence assumptions.

**Pairing convention.** Freshly read [Stacks 15.59,
0GWN](https://stacks.math.columbia.edu/tag/0GWN), through the differential
check of the commutativity map. Swapping degrees p,q contributes
(-1)^(pq). This fixes the cohomological convention; coefficient wedge
has its own interchange rule. A later proof must construct cup/wedge/
trace on the actual bundle, keep both rules, and check perfectness at
every fibre using L073's base change. Self-duality alone does not specify
the bilinear symmetry. Determinant wedge and the exponential exact
sequence are named standard inputs already used in L059; integral
c_1(F)=0 and H^1(X,O_X)=0 must be verified before trivializing det(F).
The fibre's holomorphic two-form, not an unmentioned coefficient twist,
must account for the relative canonical line.

**Exact-metric simplicity.** Freshly read Huybrechts,
*Lectures on K3 Surfaces*, [author-hosted draft, Chapter 9 Section
3.1](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175),
printed pp. 175--176 (zero-based PDF pages 174--175). The introductory
scope explicitly includes a complex K3 with a Kahler class, alongside
the algebraic ample-line case. Item (iii) states that every slope-stable
sheaf is simple; its proof compares the image of a nonscalar
endomorphism both as quotient and subsheaf. Item (iv) covers dual
stability. This removes a possible rational-polarization scope problem
at the retained h. The preceding algebraically closed-field convention
identifies simplicity with scalar endomorphisms. Also inspected
[Theorem 4.9, printed p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182),
which gives the compact-Kahler Hermite--Einstein/polystability
correspondence. These general results supply no transformed pairing.

**Connection compatibility, reusable and optional for the obstruction.**
Reuse [the saved primary-source assessment](2026-10-05-flat-transform-orthogonal-residual.md),
its coefficient and connection paragraphs, and [the subsequent scope
comparison](2026-10-06-nonflat-rank-three-projective-lift.md),
its reused-coverage paragraph. They inspected Arvid Perego,
*Kobayashi--Hitchin corrispondence for twisted vector bundles*, Complex
Manifolds 8 (2021), 1--95, [Propositions 3.9--3.12 and 3.15,
pp. 36--38](https://unige.iris.cineca.it/retrieve/e268c4cd-97f6-a6b7-e053-3a05fe0adea1/10.1515_coma-2020-0107.pdf#page=36).
On a compact Hermitian manifold the stated weak Hermite--Einstein
morphisms are parallel when the target function is at most the source
function; the dual and tensor results specify those functions. For an
untwisted application use cocycle one and B-field zero and verify both
functions are zero from L073's connection. The metric is identical;
mixed-character sign does not appear in the morphism theorem's scope.
Fresh PDF opening returned document metadata, but proposition searches
and page screenshots errored; no fresh page inspection is claimed.
This is not an essential source blocker: adequate prior inspected
coverage exists, and the holomorphic simplicity comparison needs no
parallelness conclusion or real reduction.

## Search, duplicates and limits

Queries on 2026-10-08 were `stable rank two symmetric symplectic bundle
simple`, `Nahm transform symplectic orthogonal K3 rank two Serre duality`,
`site.math.uni-bonn.de/people/huybrech/K3Global.pdf stable simple`,
`stable orthogonal rank two bundle simple`, and `Nahm transform symplectic
K3`. No returned search result was imported as an exact changed-sign
theorem. Curve/parabolic orthogonal results and torus Nahm-transform
leads were not followed as inputs: their hypotheses do not supply this
ordinary K3 product projection. No originality follows from the search.

Read L059's determinant/duality/sign passage and its full stable-block
comparison through the rank-two form test; read L061's initial duality
passage and saved general-source reuse. Read L073's hypotheses and
conclusion and L074's hypotheses, conclusion and complete stable/split
filter. Their existing audits remain the mathematical inputs. The
general rank-two comparison is already present locally, so a later
changed-image test is a REPRODUCTION, not a new theorem claim. Do not
apply either older lemma's conclusion to this G without the new
applicability argument. The full stated b=-11,-13 test is covered;
b=-9,-17 and broader slices remain outside this assessment's target.

ATTEMPTS/043's compatible rank-seven branch, ATTEMPTS/045's compatible
nonspin rank-three lifting cases and ATTEMPTS/051's exhausted directional
filter were read. None tests a stable ordinary rank-two image against
its own coefficient-duality morphism. Preserve those stops; do not
repeat their parity, index or lifting calculations here.

The separate attempt must first determine the actual pairing's
coefficient, symmetry and perfectness, then compare it with the
determinant wedge using the inspected simplicity theorem. Stop if
the comparison is compatible or a necessary hypothesis fails. A
conclusive contradiction would exclude only the specified conditional
F cases, with no kernel construction, cycle, reconstruction or
transport. No changed-sign result is proved by this assessment.

Full matching Mathlib coverage has not been checked. Reuse known
theorems by the citations above; local determinant, trace, sign and
actual-image checks are necessary specializations because the sources
do not state this conditional bundle test.
