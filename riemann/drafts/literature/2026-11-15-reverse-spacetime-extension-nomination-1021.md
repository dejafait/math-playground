# Original reverse spacetime extension — nomination1021 / review1022

TARGET: Establish or refute an L1 extension of the original reverse spacetime pullback across the initial diagonals, with zero interior collision-boundary defect and C467h's initial trace.
CHECKED: 2026-11-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1022 searched exact Vandermonde/gradient-flow pullbacks, closed L1 forms, removable PDE singularities, divergence-measure fields and Sobolev naturality; inspected the primary statements/proof cases below and scoped C467e-h, reviews1012/1018/1020 and stops948/1009. No full matching original-flow extension theorem was found in this bounded search; no novelty claim follows.
SOURCE_EVIDENCE: Fresh primary reads: Harvey–Polking1970 Theorem2.1/proof pp40–41 and Theorem5.2/Green formulas/Lemma5.3 pp49–50; Gol'dshtein–Troyanov arXiv0801.4295v1 §§2–7; Phuc–Torres2008 Theorem5.1/proof pp1593–1594 and Remark5.3 p1595; Martio–Miklyukov–Vuorinen2007 §1/Theorem1.1 and §2/Lemma2.1. Reuse the recorded ODE/DCT/coefficient sources; exact links and limits below.
COMPARISON: Standard weak-form and conditional removability tools cover the framework, not the missing actual-flow estimates. C467h supplies only the spatial coefficient/initial trace. L1 alone does not meet the inspected removal criteria; neither Sobolev stability, matching collision traces nor mixed-minor domination has been established. Stops948/1009 have different scopes.
GAP: Reconstruct and bound every original mixed minor, and prove the stated cutoff defect vanishes at single and simultaneous initial collisions, or give a rigorous actual-flow counterexample. Quantitative tubular decay is an optional sufficient route, not a necessary condition or a claimed estimate.
REASON: Essential theorem-level comparison is complete for the unchanged target; SPECIALIZE supports one bounded established-route attempt after separate approval of this changed assessment. No essential source blocker remains. Supporting definitions/theorems should be cited; the actual weighted cancellation and collision-flux estimates cannot be imported from the inspected results.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED newly concerns full spacetime minors and collision defects, outside the ready spatial/DCT assessment; review1022 supplies that missing coverage without refreshing unchanged sources.
SCOPE: n=3,R=1/4,a=1/16,T_0=1/1920,I=(-a,a)^3; actual B,H,H_0,F and raw reversed flat-metric Y of C467e-h, fixed physical time, arbitrary unequal distinct initial triples, completed Lebesgue measure and the original unnormalized full pullback. No divided K_-, smooth diagonal extension, modified current, outer-interface payment, global/all-degree signs or Xi transfer is assumed.

## Exact proposed test, not an established result

Use C467e-g/audit1017 and C467h/audit1021 with their unchanged
analytic hypotheses. C466z/audit988 and C466/audit993 supply the
normalization and analytic bound through those inputs; preserve
C466a's external qualifications for any density interpretation.

On (0,T_0) x I*, consider the original complex three-form

\[
 \Theta=Y^*\left(F(z)\,{dz_1\over i}\wedge{dz_2\over i}
                                      \wedge{dz_3\over i}\right).
\]

Its spatial coefficient is C467h's A. For each j, the mixed
coefficient M_j is F(Y) times the complex determinant with the jth
column D_{u_j}Y/i replaced by partial_t Y/i; wedge-order signs must
be retained when reconstructing the form. The proposed target asks
for integrability of all three M_j on (0,T_0) x I and for the
zero extension of the full form to have no distributional exterior
derivative in the interior, with the spatial initial trace already
established by C467h. These are assertions to test, not premises.

A concrete collision test uses
chi_epsilon(u)=product_{j<k} eta((u_k-u_j)^2/epsilon^2), where a
fixed smooth eta is zero on [0,1] and one on [4,infinity). After
the complete complex minors have been reconstructed, test whether
the cutoff boundary integral of phi dchi_epsilon wedge Theta tends
to zero for every smooth compactly supported scalar test phi in
(0,T_0) x I. Include both a single vanishing gap and simultaneous
triple collision, with no equal-gap assumption. Spatial compact
support excludes the outer box boundary from this particular test.

Continue only with a justified L1 estimate and zero collision defect,
or an explicit alternative extension theorem whose hypotheses are
verified. A rigorous nonintegrable coefficient or nonzero defect is
an informative obstruction to this exact extension claim. Failure of
one sufficient absolute estimate is not a counterexample to the
extension or to reverse deformation. Preserve partial reasoning if
the test remains unresolved. Payment on outer interfaces, any global
signed identity, all-degree positivity and actual-Xi transfer remain
independent even if this local test succeeds.

## Separate approval required

The next turn is literature_comparison, standard/high: compare the
exact statement and relevant current/removable-singularity results,
including their hypotheses at collision strata, against existing local
coverage and failures. Retrieve primary theorem statements and the
essential proof cases before approving any mathematical attempt.
Ready spatial/DCT coverage alone does not approve the mixed-minor
target. No new lemma or mathematical script was produced here.

This is an established-route extension problem; no genuinely new
central creative mechanism has been justified by the spatial audit.
Its missing source coverage is the concrete next bottleneck. Do not
label this continuation creative merely to meet scheduling guidance.
Mathlib coverage for the full extension has not been checked.

## Completed source comparison1022 — 15 November 2026

The nomination above is preserved as the proposed test and its original
gate status. This completion changes source coverage only. It proves no
estimate or extension and does not audit a new mathematical argument.

### Discovery and local comparison

The main gap remains L030–L032/C032a, actual-Xi all-degree
algebraic-square positivity. The intermediate target is exactly TARGET,
with the original three-form and all mixed coefficients specified above.
Its plausible downstream use is a local signed reverse-deformation
identity using the audited spatial trace. Outer-interface payment,
global signed assembly, all degrees and Xi transfer are independent.

Queries included `Harvey Polking removable singularities differential
forms Lp closed currents hypersurface theorem`, `singular gradient flow
Vandermonde differential form pullback mixed minors integrability Stokes`,
`removable singularities closed differential forms L1 hypersurface boundary
current flux`, `Harvey Polking Removable singularities 1970 pdf`,
`removable divergence L1 Hausdorff Phuc Torres`, `pullback differential
forms Sobolev minors weak exterior derivative`, `On the naturality of the
exterior differential pdf`, `Vandermonde pullback current gradient flow`,
`logarithmic Lefschetz Stokes singularities flow integrability`, and
`removable closed forms L1 cutoff boundary`. Search summaries were used
to locate primary texts, never as theorem evidence. No exact match was
located; the scope of this finding is the inspected material only.

Read C467h's hypotheses, complete determinant cancellation and initial
trace passage; C467f's hypotheses, conclusions and reconstruction
(18)–(19); C467g's hypotheses, conclusions and physical-time Hamiltonian
(3)–(7). Reuse their independent audits1017/1021 without repeating them.
Review1018 explicitly excludes spacetime current coverage, and review1020
covers only the spatial audit. These records contain no duplicate solution
to the present target. The coefficient chart offers already established
inputs for an attempt; its availability is not an extension theorem.

Read stops948/1009, including audit1011's retained scope, and the relevant
review1012 comparison of TNV2017, LY2021 and FM2020. Stop948 does not make
smooth divided extension necessary; stop1009 excludes its prescribed
forward cap and initial family. Neither refutes the reverse spacetime
target. Modified flows, conditional contour constructions and action-phase
identities in those already assessed sources do not settle its original
mixed coefficients or collision flux. No renewed generic thimble search
or reproof of local smooth ODE theory is needed.

### Primary theorem statements and essential cases inspected

**Harvey–Polking.** Reese Harvey and John Polking, *Removable singularities
of solutions of linear partial differential equations*, Acta Math.125
(1970),39–56, [journal scan, pp40–41 and49–50](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6102-11511_2008_Article_BF02838327.pdf).
The setup permits smooth matrix coefficients and exterior differentiation.
Theorem2.1: for an order-m operator P, relatively closed A, and
f in L1_loc solving Pf=0 off A, the condition
liminf(epsilon^(-m)||1_(K_epsilon)f||_1)=0 for every compact K in A
implies Pf=0 everywhere. K_epsilon is the epsilon-neighborhood of K.
Its proof uses derivative-controlled cutoffs and the formal adjoint.
This is a sufficient quantitative test, not a consequence of L1.
Theorem5.2 requires a smooth hypersurface, a smooth off-surface solution,
normal order m>=1, and equal two-sided weak distributional traces of
normal derivatives of orders0 through m−1. It yields a distributional
extension solving P; Green formulas(5.1)–(5.4) and Lemma5.3 control the
limit. No such traces are established here; a double-stratum theorem
does not by itself treat their triple intersection. Read also
Theorems4.1–4.2/proofs pp45–46 for comparison. No automatic import.

**Weak pullbacks.** Vladimir Gol'dshtein and Marc Troyanov,
[*On the naturality of the exterior differential*, arXiv:0801.4295v1,
28January2008](https://arxiv.org/html/0801.4295v1), §§2–7, particularly
Definition2.2, Lemma2.1/proof, Proposition5.1/proof, Theorem6.3/proof and
Corollaries6.4/7.2. Definition2.2 specifies weak closedness of an
L1_loc k-form by its pairing with derivatives of compact tests.
Lemma2.1 passes weak convergence of forms and their exterior derivatives
to the limit. Proposition5.1 covers closed smooth forms pulled back by
k-stable maps: smooth approximation in the topology combining W1,1
and weak convergence of all k-pullbacks. It proves closure by passing
test pairings to the limit. Corollary6.4 requires W1,k+1; Corollary7.2
requires W1,k and all k-minors in L^(k/(k−1)). For degree3 these demand
W1,4, or W1,3 with all real 3-minors in L^(3/2), respectively.
C467h proves none of those map conditions. A weighted complex minor
is not the full real minor array. Use Definition2.2's framework directly;
any Sobolev import would need its map, approximation and target-localization
hypotheses verified. The author PDF timed out; the primary arXiv text
was accessible, so this creates no essential blocker.

**Sharp divergence comparison.** Nguyen Cong Phuc and Monica Torres,
[*Characterizations of the Existence and Removable Singularities of
Divergence-measure Vector Fields*, Indiana Univ.Math.J.57(2008),1573–1597](https://www.math.purdue.edu/~torresm/pubs/Divergence-measure-fields.pdf),
author-hosted journal PDF: §2/Remark2.1, Theorem5.1 and both proof cases
pp1593–1594, Remark5.3 p1595. For compact E inside open U, a locally
finite signed Radon measure mu with mu(E)=0 and n/(n−1)<p<=infinity,
zero cap_(1,p')(E) ensures extension of div V=mu for V in Lp_loc(U).
The converse assumes a global solution exists and every punctured
solution extends. At p=infinity, zero capacity means H^(n−1)(E)=0.
The sufficiency proof controls cutoff-gradient pairings; the necessity
proof constructs a nonzero measure supported on E. Remark5.3 records
bounded counterexamples smooth off E when H^(n−1)(E)>0. Collision faces
are hypersurfaces in four real parameters; their Lebesgue nullity is
insufficient for that automatic-removal criterion. This comparison
neither constructs a defect in the prescribed Y nor supplies its minors;
the theorem's p-range excludes an L1-only import.

**Excluded nonlinear form theorem.** Olli Martio, Vladimir Miklyukov and
Matti Vuorinen, [*Removable Singularities of WT-Differential Forms and
Quasiregular Mappings*, Boundary Value Problems2007,Article61602](https://boundaryvalueproblems.springeropen.com/counter/pdf/10.1155/2007/61602.pdf),
§1(1.9)–(1.11)/Theorem1.1, pp2–3, §2/Lemma2.1 and §3 applications.
The theorem requires compact p-capacity-zero E, 1<=p<=n, simple forms
Z and theta of degrees k−1 and n−k, the stated integrability, a bounded
Z and the WT pair coercivity/size condition. None is provided by the
spatial phase cone alone. Lemma2.1 and its following observation tie
capacity zero to H^(n−1)-nullity. It is not a generic L1 closed-form
extension theorem; its nonlinear proof is unnecessary for this exclusion.

The standard smooth pullback/naturality identity and weak-form
definitions above are supporting imports only. Reuse Teschl, Hunter and
the coefficient Jacobian citation exactly as assessed in review1018.
No general removability, trace or Sobolev theorem should be reproved.
No known result from another notebook is used. Other search hits and
references within these papers remain unread leads, not premises.

### Scope of the ready mathematical attempt

SPECIALIZE covers exactly TARGET, with C467e-g/audit1017 and
C467h/audit1021 as essential inputs. C466z/audit988 and C466/audit993
enter through those inputs; preserve C466a's external density
qualifications. Retain n=3,R=1/4,a=1/16,T_0=1/1920, I=(-a,a)^3,
the actual F and the raw reversed flat-metric field at fixed physical
time, completed Lebesgue measure and arbitrary unequal initial gaps.

The next attempt must reconstruct the complete original complex mixed
minors with their wedge signs before estimating them. It must establish
their integrability on the whole open time slab, including behavior
approaching t=0; current closure is tested with compact interior scalar
tests. Retain the nominated product cutoff and test both a single
vanishing gap and the simultaneous triple collision, without an
equal-gap restriction. The spatial trace remains C467h's audited input.
Do not replace F, divide by a Vandermonde, change the current or time,
or presume a smooth root map across the initial diagonals.

Theorem2.1 offers one optional sufficient absolute-decay test. If used,
verify its full local hypotheses for the coefficient vector and operator;
no tubular estimate has been obtained here. Alternatively prove the
specific cutoff pairing tends to zero, using the cited weak-closure
definition and justified limits, or verify all hypotheses of another
already assessed extension theorem. An unsuccessful absolute estimate
does not refute the target. A negative conclusion requires a proved
nonintegrable original coefficient or nonzero actual cutoff defect.
If unresolved, preserve the mixed-minor reasoning and identify a refined
test before repeating it. Success still leaves outer payment, global
assembly, all-degree signs and Xi transfer open.

This is established-route development; prospective classification is
REPRODUCTION, with proof_attempt/development, deep_research/xhigh for
the singular weighted minors and collision strata. No new central
creative mechanism is justified by this narrowly scoped source review;
creative priority does not turn a current-extension specialization into
one. The present source gate is now complete, while mathematical
extension remains unresolved. A separate next-turn approval of this
changed assessment is required before its mathematical use.

Mathlib: retain review1018's supporting DCT coverage. Full matching
coverage for this spacetime extension, weak singular pullback and
collision cancellation has not been checked; no absence or Lean
verification is claimed. No lemma or mathematical script was written.

Completed step: LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. New source
comparison supplies precise sufficient conditions and exclusions, not
progress beyond the inspected theorems or a proved actual-flow result.
The main argument and DAG are unchanged.
