# Twisted harmonic metric — curvature source comparison

TARGET: Test uniform boundedness of the Chern curvature of L148's actual twisted harmonic L2 metric near each split parameter.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the October 16 derivative discovery and October 23 twisted comparison coverage; performed changed-coefficient cohomology-jump/L2/quotient-curvature searches; inspected Verbitsky Section 4 operator hypotheses/proof, Naumann Section 2/Theorem 2.1 and Yoshikawa arXiv:1007.2836v1 introduction/Theorem 1.1; compared L148, L146's actual complement construction, L113 and ATTEMPTS/060/063/066/067.
SOURCE_EVIDENCE: Reuse inspected Demailly CADG (21 June 2012), V.12 (12.2)-(12.3)/Theorem 12.4, pp. 268-269, and V.14 Theorems 14.3/14.5, pp. 273-275; BGS III Section 1(b)-(c), Theorem 3.5/Lemmas 3.6-3.8 and Stacks 064B through L148's ready assessment; primary coefficient/positivity comparisons and precise references are recorded below.
COMPARISON: Chern differentiation and smooth quotient formulas apply to the given twisted metric on the puncture; no inspected theorem supplies its bounded curvature. Verbitsky's parallel-real hyperholomorphic coefficient hypothesis is not supplied for this twist with its arbitrary fixed line metric, and L146's corrected complement is not asserted Hermitian orthogonal. L113's cancellation therefore remains unavailable as an imported conclusion.
GAP: Test the actual central cross block and complete quotient derivatives under the unchanged metric; either a uniform finite curvature bound or a rigorously identified failure is still required. No central cancellation, divergence, extension or F nonexistence is proved by this review.
REASON: Separate source-scope comparison is complete for one later REPRODUCTION specialization of ready Chern/quotient tools; retain the original target and all hypotheses, and do not reprove general source formulas or substitute another metric. No essential unread source blocks this bounded calculation.
LITERATURE_REASON: The saved gate requires separate coverage of the changed twisted coefficient and curvature derivatives; the ready norm-bound assessment does not cover them, and the adjoint curvature assessment needs this exact hypothesis comparison.
SCOPE: Hypothetical locally free Omega-polystable equality F on identical marked K3 factors/common metric, integral c_1=0, ch_2=-14e_1-21e_2-tau_D, fixed k=(-4,-2,1,2), the same fixed smooth positive line metric, and finite possibly empty Z.

The main gap remains universal primitive rational Hodge realization.
The intermediate target is a bound on the Chern curvature of the
given metric on L147's actual locally free rank-24 M, using its
holomorphic structure and the unchanged smooth base metric. A bound
would provide an analytic input for later extension work. No applicable
extension theorem, image positivity or polystability, useful split-set
bound, F or nonempty Z, reconstruction or transport is supplied.

Essential inputs for the proposed attempt are audited L148's natural
comparison and exact quotient identity, L146's actual full Koszul
splitting and L147's actual ordinary middle image. Their retained
L071/L094/L095/L096/L134/L145 hypotheses remain unchanged. No cross-
notebook input is proposed. L112/L113 concern the adjoint coefficient;
they are comparison material, not a premise establishing this result.
The existing `drafts/literature/2026-10-16-split-harmonic-metric-curvature-energy.md`
supplies reusable general derivative coverage, as qualified in the
separate source-scope comparison below. Its adjoint-specific conclusion
is not an input for the twisted estimate.

The precise test is a finite constant bounding the norm of the actual
Chern curvature everywhere on one full punctured ball, uniformly in
direction and including both coordinate axes. A later covered attempt
must retain the actual central Hermitian cross block between P and J
in L148, all higher coefficients and all derivative terms in the
quotient. The arbitrary fixed smooth positive line metric in SCOPE
must not silently be replaced by a preferred connection metric.
Neither scalar self-duality of G nor the adjoint-coefficient Serre
complement is available. Two-sided norm bounds alone do not control
these derivatives.

Continue the bounded-curvature route only if a valid estimate supplies
that constant for the stated actual metric. A demonstrated failure
requires parking or narrowing this estimate, without inferring F
nonexistence. An abstract smooth finite-complex example would test only
an inference from the stated local algebra, unless all necessary
actual-family constraints are retained; it is not automatically a
counterexample for the conditional geometric family. Empty Z is
vacuous. No metric limit or extension may be inferred automatically.

ATTEMPTS/060/063/066/067 and the IT/effectivity stops remain in their
recorded scopes. This proposes an independently testable analytic
estimate, not a repetition of strict Euler or automatic extension.
Full matching Mathlib coverage is not checked. The original proposal
did not execute or approve the curvature test. The separate source
comparison below approves its scope for a later mathematical attempt,
without executing that attempt.

## Separate source-scope comparison, step 476

This LITERATURE-only step preserves the exact TARGET. It supplies source
coverage, not a curvature result. Its outcome is EXPLORATION: no new
estimate or actual-family obstruction is established. The universal
primitive rational Hodge realization gap is unchanged. A successful
estimate could support later extension work, with the extension theorem
and its hypotheses still to be reviewed independently.

**Reusable formulas.** The
[October 16 assessment](2026-10-16-split-harmonic-metric-curvature-energy.md)
records inspection of J.-P. Demailly, *Complex Analytic and Differential
Geometry*, version 21 June 2012, Chapter V, sections 12 and 14,
[university mirror](https://www.ime.usp.br/~cordaro/wp-content/uploads/2022/03/Jean-Pierre-Demailly-Complex-Analytic-and-Differential-Geometry-1.pdf#page=269).
Reuse its coordinate derivation of (12.2)-(12.3)/Theorem 12.4,
pp. 268-269, and block-connection proof of Theorems 14.3/14.5 and
(14.6)-(14.7), pp. 273-275. A smooth positive Hermitian matrix H in a
holomorphic frame has Chern curvature bar-partial(H^{-1} partial H).
The quotient statements concern a constant-rank exact sequence of
holomorphic bundles on the open set where it is used. Here that is the
puncture. They are not a theorem extending a quotient across a vanishing
column. The new fetch of this large PDF timed out; the recorded complete
proof-case inspection is reused, not claimed as a fresh retrieval.

The
[twisted norm assessment](2026-10-23-twisted-harmonic-metric-two-sided-bounds.md)
already checks the arbitrary Hermitian coefficient scope of Bismut,
Gillet and Soulé, *Analytic torsion and holomorphic determinant bundles
III*, Comm. Math. Phys. 115 (1988), 301-351, DOI
[10.1007/BF01466774](https://www.imo.universite-paris-saclay.fr/~bismut/Bismut/1988b.pdf),
Section 1(b)-(c), pp. 304-305, Theorem 3.5/Lemmas 3.6-3.8,
pp. 342-345, and the projective-complex comparison
[Stacks Lemma 13.19.8, 064B](https://stacks.math.columbia.edu/tag/064B).
Reuse this coverage and audited L148's natural comparison and exact
least-norm identity (8). These inputs require smooth positive metrics,
not coefficient curvature positivity or scalar self-duality. They do
not bound derivatives of the resulting ordinary cohomology metric.

**The changed coefficient matters.** Directly read M. Verbitsky,
*Hyperholomorphic bundles over a hyperkähler manifold*,
[alg-geom/9307008v1, 29 July 1993](https://arxiv.org/pdf/alg-geom/9307008v1#page=13),
Section 4, printed pp. 12-15: the operator setup, Proposition 4.2 proof,
Theorem 4.1 proof and Corollary 4.3. Its construction uses a parallel
real structure; the proof of Proposition 4.2 uses the given connection
being Hermitian holomorphic for I,J,K. The Laplacian identities then
preserve harmonic representatives and give the stated real SU(2)
action, quaternionic in degree one. This is adequate for L113's adjoint
comparison as assessed there. The present hypotheses do not furnish
these structures for G with its arbitrary fixed line metric. Positivity
of a Hermitian norm is not the missing connection hypothesis. No choice
of a preferred line metric, nor transfer of derivative bounds between
different harmonic metrics, is approved.

The local comparison is also different before metric differentiation.
L146, equations (9)-(12), corrects a free complement by subtracting
vectors in P to kill the actual outgoing row. L148 uses that complement
J and pulls back the given central harmonic product. Neither statement
identifies J with the Hermitian orthogonal complement of P. L113's
Serre/Hermitian identity concerns End_0(F), not this coefficient.
Thus central cross-block cancellation is a mathematical obligation for
the attempt, not an additional assumption or a conclusion of this review.
Changing an extending holomorphic frame must respect the actual ordinary
sections and cannot be used to replace their harmonic metric.

**Stronger-looking estimates do not match.** Directly read P. Naumann,
*Curvature of higher direct images*, Ann. Fac. Sci. Toulouse 30 (2021),
171-201, [DOI 10.5802/afst.1670, primary PDF](https://www.numdam.org/item/AFST_2021_6_30_1_171_0.pdf#page=3),
Section 2 and Theorem 2.1, pp. 172-174. The relatively positive
Hermitian line curvature defines the fibre Kähler metrics; the setup
assumes local freeness/base change for the specified form-valued higher
image and supplies the spectral-resolvent conditions. This does not
supply a theorem for G or a uniform estimate at its cohomology jump.
No proof of its formula is imported. The earlier Mourougane--Takayama
screening is reused: Nakano semipositivity and identification with its
Hodge metric have not been furnished here.

Also read K.-I. Yoshikawa,
[*On the boundary behavior of the curvature of L2-metrics*,
arXiv:1007.2836v1, 16 July 2010](https://arxiv.org/pdf/1007.2836v1#page=1),
introduction and Theorem 1.1, pp. 1-2. It assumes a one-parameter
degeneration and a Nakano semipositive coefficient twisted by the
relative canonical bundle; it gives Poincaré-growth curvature control
and a first-Chern-form asymptotic. Those hypotheses and conclusion do
not provide the requested uniform full-ball bound for this smooth
product projection with its arbitrary twisted coefficient metric.
Only the statement/setup comparison is used; no later proof is claimed
read or needed for this rejection.

## Discovery, limits and approved mathematical attempt

Changed-scope queries included `"higher direct images" "L2" metric
"jumping" curvature`, `"cohomology" "quotient metric" "curvature"
harmonic`, `"harmonic" "metric" "change of metric" higher direct image
curvature`, `"cohomology jump" "harmonic" "metric" curvature`, and
`"quotient metric" "Chern" "singular" curvature cohomology`; followed
the exact Naumann and Yoshikawa titles to primary statements. General
Riemannian harmonic-curvature hits and flat-local-system jump-locus
results were not used as metric theorems. A search lead in Ark. Mat.
55 (2017), pp. 131-153, on singular quotient metrics timed out at the
[PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/116/8947-ARKIV-2017-55-1-a06.pdf).
Its theorem and example were not inspected and supply no premise; it is
not essential to differentiating the already established local formula.
This bounded search establishes neither novelty nor exhaustive absence.

Duplicates and failures were checked in the actual L148 and L113 proofs,
L146's complement construction, the two ready assessments, and the
named ATTEMPTS files. No other notebook was read. L148's norm estimate
is not repeated as a derivative result. ATTEMPTS/060's strict-Euler
stop, /063's missing singular metric bridge, /066's automatic surface
extension failure and /067's duality-only bound remain in their scopes.
Their stopped inferences do not prohibit this direct, independently
testable estimate.

SPECIALIZE now covers exactly TARGET for a later RESEARCH /
REPRODUCTION attempt. Import the general formulas by citation. Retain
L148's full natural spectral comparison and exact quotient, L146's
full Koszul splitting, L147's actual ordinary image, and their retained
L071/L094/L095/L096/L134/L145 hypotheses. Inspect the central Hermitian
cross block using the actual twisted harmonic product; do not impose
its vanishing or reuse adjoint scalar self-duality. Differentiate the
complete quotient, including every inverse denominator and higher
coefficient, and test the actual Chern curvature in the fixed base and
actual endomorphism norms. No matrix calculation, asymptotic rate or
central identity has been derived in this literature step.

Continue this route only upon a finite uniform bound on one full
punctured ball, including both axes. A genuine unbounded actual-family
term would park the proposed bound. An unresolved central comparison
must be reported as a gap; a smooth finite-complex model can refute only
an inference from local algebra unless it retains the actual geometric
constraints. Neither such a model nor failure of this estimate proves
F nonexistence. The arbitrary fixed line metric and possibly empty Z
remain unchanged. Extension, positivity, a useful split-set bound,
F existence and universal primitive realization remain separate gaps.
Full matching Mathlib coverage is not checked. No new lemma, mathematical
script, DAG edge or overview argument is introduced.
