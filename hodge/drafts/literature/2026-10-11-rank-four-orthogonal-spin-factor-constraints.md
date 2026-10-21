# Rank-four orthogonal image: source comparison

TARGET: Assess the Spin(4) lifting and rank-two factor constraints for L079's stable orthogonal rank-four charge-eight branch at the exact metric.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped L079, L052, L061 and ATTEMPTS/053; searched Spin(4) rank-four tensor factors, SO(4)/SO(3) characteristic relations and twisted rank-two lifting; primary passages and scope distinctions below.
SOURCE_EVIDENCE: Choe--Hitching 2203.06645v2, introduction, Section 2.3 and Theorem 4.2 with complete proof, pp. 1,5,11; Grove--Ziller 0801.0767v1, Proposition 1.8 with both proof cases and equations (1.10)--(1.11), pp. 7--8, Proposition 3.3, p. 11; reused Yoshioka math/0411538v2 coverage, rechecked Lemmas 1.2--1.4 and Proposition 3.6 with trace-obstruction paragraph, pp. 2,8.
COMPARISON: General group and projective-factor tools cover a necessary test; the curve tensor theorem cannot supply ordinary K3 factors without its isotropic-subbundle hypothesis. Separate half-adjoint constraints were not tested by L079's total adjoint index or L086's projector stop.
GAP: Justify the actual parallel holomorphic half-adjoints and simplicity of their local rank-two lifts; compute and compare their individual necessary constraints, retaining every spin, ordinary-nonspin and Brauer-twisted case. No exact-h realization theorem or common kernel is supplied.
REASON: Approve one bounded specialization of known tools, rather than reprove lifting theory or import curve nonemptiness at the saved real metric.
SCOPE: L079's conditional t=1 stable symmetric acyclic K_4, c_1=0 integrally and c_2=8, at L052's exact h; necessary two-factor characteristic, simple-index and spin stable-factor tests only. No existence, inverse transform, transport or exclusion of other L079 alternatives.
COVERED_TARGET: Test the two half-adjoint lifting and index constraints for L079's stable K_4 at the exact metric, retaining spin, ordinary-nonspin and Brauer-twisted cases.

## Main gap and bounded use

The main unresolved claim remains algebraicity of every primitive rational
(2,2)-class, already unresolved for arbitrary fourfolds. Locally no
common holomorphic F with the full negative mixed tensor at (-13,-14),
or transverse transport, is constructed. The intermediate target is a
necessary factor-sensitive test on K_4. It could eliminate or narrow
one image alternative before attempting a common kernel; the repeated
E_4 branch and all t=2 branches remain independent.

Continue for one mathematical attempt only if the actual half-adjoint
bundles and lift hypotheses are justified. Compare their individual
constraints, not just their sum. A contradiction in the spin case is
useful but does not exclude nonspin K_4. If ordinary-nonspin or twisted
cases remain numerically compatible, record the exact survivors and
stop this bounded mechanism without an existence assertion. No
characteristic specialization or new lemma is performed in this review.

## Inspected primary results

Choe and Hitching, *Low rank orthogonal bundles and quadric fibrations*,
[2203.06645v2, 23 September 2023](https://arxiv.org/pdf/2203.06645v2),
pp. 1,5,11: Spin(4,C) is SL2(C) x SL2(C); Section 2.3 gives the central
cover obstruction criterion. Theorem 4.2 is explicitly over a smooth
projective curve: a rank-four line-valued orthogonal bundle is a tensor
of rank-two bundles with the indicated determinant relation exactly
when it admits a rank-two isotropic subbundle. Its proof constructs a
rank-two extension of line bundles from the orthogonal extension class,
and matches that class after tensoring. This does not establish the
required isotropic subbundle on a K3 surface. Import the group
representation, not the curve structure or moduli existence conclusion.

Grove and Ziller, *Lifting Group Actions and Nonnegative Curvature*,
[0801.0767v1, 5 January 2008](https://arxiv.org/pdf/0801.0767v1),
Proposition 1.8, pp. 7--8: for compact simply connected M, the two
associated SO3 bundles determine its SO4 bundle and have the same w_2;
conversely a pair with equal w_2 comes from SO4. Both proof cases were
read: separate spin covers when the class vanishes, and a double cover
of the fibre product when it does not. Equation (1.10) gives
p_1(P_±)=p_1(P)±2e(P), using the two ideals of Lambda^2 R^4;
(1.11) records the usual U2 special case. Proposition 3.3, p. 11,
keeps Euler class as an independent invariant on simply connected
four-manifolds. These are topological statements, not holomorphic
realization at h. S meets the compactness, simple connectivity and
real dimension hypotheses; no cohomogeneity-one assumption is used.

Yoshioka, *Moduli spaces of twisted sheaves on a projective variety*,
[math/0411538v2, 8 May 2006](https://arxiv.org/pdf/math/0411538v2),
Lemmas 1.2--1.4, p. 2, identify the SL_r obstruction of an ordinary
projectivization with c_1 modulo r, and ordinary liftability with its
lying in NS modulo r. Proposition 3.6, p. 8, requires a simple Y-sheaf;
its Mukai square is at least -2. The preceding paragraph identifies
the trace-free Ext2 obstruction. Reuse the inspected discriminant and
twisted conventions from the [rank-three assessment](2026-10-06-nonflat-rank-three-projective-lift.md).
Its general-polarization nonemptiness statements are not exact-h
locally free slope existence. This review imports necessary tools only.

## Applicability obligations for the next attempt

L079 supplies K_4's actual compatible connection and parallel symmetric
form, not an assumed tensor decomposition. First trivialize and normalize
its orientation and form compatibly, then construct the two exterior
half-adjoints and check that they are global, parallel and holomorphic.
Their induced connections must stay at the identical h. Use the
complex group representation locally to identify the projective
rank-two torsors; compare their central lifting cocycles, rather than
assuming that a topological pair of factors is holomorphically realized.
For a nonspin lift use local SL2 transitions and the common central
cocycle; the descending End bundles are legitimate ordinary bundles
although the rank-two factors may be twisted. Verify cancellation and
identify the actual coefficient representation before any tensor formula.

Prove simplicity of each local/twisted rank-two factor from the actual
K_4 stability and parallel connection; it is not implied by the word
“twisted”. Show how a nonscalar descending endomorphism would act on
the rank-four coefficient. In a spin branch establish exact-h factor
polystability and rule out reducibility before applying L052's stable
rank-two bound. In an ordinary nonspin branch determinants are arbitrary
Picard classes, not necessarily in Zk: L052 describes only zero-slope
line classes. Do not apply untwisted RR to a nonexistent ordinary
factor, or infer spin liftability from c_1(K_4)=0 or base spin.

Retain the real rank-four Euler invariant; it is not the complex
rank-four top Chern class. Use p_1 of the compact real reduction with
the correct complexification convention. Keep both obstruction w and
its Brauer image alpha. The future calculation must distinguish
formal numerical survivors from actual exact-h bundles. These local
identifications and characteristic specializations are why a bounded
reproduction is needed instead of citation alone.

## Duplicates, failures and source limits

L079 and ATTEMPTS/053 stop the total-character/cohomology/adjoint-index
mechanism; its branch table is the input, not an exclusion of K_4.
L061 stops a different rank-three lifting/index test and permits
nonzero obstructions. L086 stops natural endomorphism-projector lifting,
which does not imply nonexistence of F. Reuse their covered RR,
connection and twisting tools; do not repeat those stops as new evidence.
The independent test here resolves the two half-adjoint constraints,
which L079 recorded only in aggregate.

Queries included “Spin(4) SO(4) rank four orthogonal bundle tensor product
rank two bundles obstruction twisted” and “SO(4) bundle two SO(3)
bundles w2 p1 Euler spin lifting”. The author-hosted Grove--Ziller PDF
failed to open, but arXiv v1 supplied the essential proof cases. An
initial arXiv identifier math/0007198 was found to be a different
Grove--Ziller paper and was not used. Fulton--Harris Lectures 18--20
and the Dold--Whitney reference remain unread leads; no essential
claim rests on them. No novelty follows from the searches.

Mathlib: full holomorphic Spin(4), twisted-factor and exact-h coverage
not checked; no absence claimed. No lemma, script, DAG or proof assembly
changed. This approves only the stated necessary test, with all local
specialization obligations still unresolved.
