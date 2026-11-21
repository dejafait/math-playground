# Reverse top spatial pullback — nomination1017 / source review1018

TARGET: Establish or refute a time-uniform L1 majorant and the t=0 L1 trace for the unnormalized reverse pullback F(Y(t,u)) det_C(D_uY(t,u)/i) on I.
CHECKED: 2026-11-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1018 searched reverse/gradient Vandermonde Jacobian integrability, singular Lefschetz pullbacks, polynomial-root/Calogero coefficient flows and stronger domination results; inspected the primary statements below and scoped duplicates/stops948/1009. Reuse reviews992/994/1012/1016 for ODE, integration, flow and interpolation tools. No full matching actual-flow majorant theorem was located; this does not establish novelty.
SOURCE_EVIDENCE: Reuse Teschl April2012 Lemma2.14/Corollary2.15 pp52-53, Theorem3.9 p81, Lemma3.11(3.91) p83 and Theorem6.1 pp189-190; Hunter Measure Theory Theorem4.24/Section4.6 pp49-50 (also freshly inspected); de Boor2005 Sections8-9 via review1016. Fresh primary comparisons: Athreya-Bufetov-Eskin-Mirzakhani author version 17September2011 AppendixA (A.5) p40; Hall-Ho2025 Proposition3.1 (3.1)-(3.5) and its proof. Links and limits below.
COMPARISON: Smooth local ODE dependence and dominated convergence cover the nonsingular trace framework; coefficient Jacobians and the audited C467e-g bounds offer supporting tools. None imports the missing time-uniform bound for the original complex top pullback. Heat-polynomial root flow has different dynamics; forward current damping and phase containment do not supply reverse amplitude control.
GAP: Supply the actual gap-uniform modulus estimate for A(t,u), including the complete fixed-time complex determinant, then check measurability and the initial limit before applying the standard integration theorem. No bound, trace or diagonal extension is proved in review1018.
REASON: Essential source comparison is complete for one bounded specialization attempt using the audited coefficient chart; no source-access blocker remains. The additional work is the actual determinant/weight estimate, not a reproof of ODE or integration theory. Separate next-turn approval of this changed assessment remains due.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED concerns the changed amplitude/trace scope, absent from the phase assessment; this review adds only its essential domination and singular-coordinate comparison.
SCOPE: Actual B,H,H_0,F and raw reverse Y of C467e-g/audit1017; n=3,R=1/4,a=1/16,T_0=1/1920,I=(-a,a)^3; original physical time and flat metric. Only the unnormalized top spatial pullback is in scope, not normalized K_-, spacetime current minors, interfaces, mass payment, all degrees or Xi transfer.

## Original nomination1017 — proposed bounded test, not a result

Let A(t,u)=F(Y(t,u)) det_C(D_uY(t,u)/i) for distinct u in I
and 0<=t<=T_0. Seek a measurable G in L1(I), independent of t,
with |A(t,u)|<=G(u) throughout that domain, and establish
||A(t,.)-F(i.)||_L1(I)->0 as t decreases to zero. Values on the
initial diagonals may be assigned arbitrarily for these Lebesgue
statements; no smooth diagonal extension is proposed. The actual
flow, original F and full spatial determinant must be retained.

Essential local inputs are C466z/audit988 for normalization,
C466/audit993 for the complex-disk bound, and C467e-g/audit1017
for survival, noncollision for each distinct u, imaginary ordering,
centered variables, bounded Hessians and tangent reconstruction.
Their bounds may provide a coordinate route, but no new estimate
is derived here. C466y and the forward balance results are at most
comparison leads; their directional integrability conclusions do not
automatically transfer. Keep C466a's external density qualifications.

The next source review should check duplicates and recorded failures,
and compare the exact target with standard dominated convergence,
finite-dimensional variational estimates and any applicable singular
flow/change-of-coordinate theorem. Reuse already inspected local ODE
and interpolation coverage. Identify any genuinely additional source
obligation before deriving a new bound; no generic phase search is
needed. Full matching Mathlib coverage is not checked.

Continuation test: a valid time-uniform majorant covering arbitrarily
small unequal initial gaps, together with the stated L1 limit, would
provide one initial top-form trace input. A failure of a convenient
majorant alone is inconclusive; a negative result requires a rigorous
actual-flow obstruction to this target. Even success leaves spacetime
current integrability, payment, interfaces, global assembly, all
degrees and actual-Xi transfer unproved. Those independent tasks
are not hidden in this nomination.

Next turn is literature_comparison, standard/high, because this changed
amplitude/trace scope is uncovered. No mathematical attempt or source
approval for it was performed in audit1017.

## Completed source review1018 — 15 November 2026

The original nomination above is retained as history. The fields at the
top record the completed comparison. This turn is literature-only:
no new estimate, lemma, mathematical script or proof audit is performed.

### Discovery and local comparisons

Queries included `"Lefschetz" "Vandermonde" "Jacobian" singular flow`,
`"reverse" "gradient flow" "Vandermonde" integrability`,
`"root coordinates" "Vandermonde" "Jacobian" symmetric polynomials flow`,
`Lefschetz thimble logarithmic singularities flow Jacobian integrability
Vandermonde`, `Calogero complex gradient flow polynomial coefficients
Jacobian Vandermonde`, `"Vandermonde" "flow" "dominated convergence"`,
`"Vandermonde" "gradient flow" Jacobian integrable`,
`"Calogero" "polynomial" "zeros" "first order" flow`, and
`"symmetric polynomials" "Jacobian" "Vandermonde" lecture notes`.
Some exact searches had no adequate matches; broader results supplied
the specific primary comparisons below. Neither a failed search nor a
search snippet is evidence of novelty or of a theorem's hypotheses.

Read C467e-g's exact hypotheses, C467g(22)-(24) and its linear
reconstruction, and C467f(18)-(19) and its determinant reconstruction.
Their audited conclusions are available inputs, not new results here.
They leave amplitude control explicitly open. Read the relevant complete
coefficient and domination passages of C466y/audit983: their damping
estimate concerns the forward field. Reversing the field does not import
that estimate. Review994 in nomination993 already assessed DCT and
local initial-point flow tools; reuse them without another trace-theory
search. No general Sobolev trace or stopped-current theorem is needed
for this narrower spatial L1 target.

Reuse nomination988/review989 and nomination1011/completion1012's exact
comparison of product contours, free germs and changing-flow results.
Freshly read stop948: it rejects smooth collision-divided extension as
a necessary screen, rather than proving failure of weighted
integrability. Lebesgue domination on distinct initial points does not
require such an extension. Freshly read stop1009 including audit1011:
the capacity contradiction is for its prescribed forward flow/cap/initial
family. It neither proves nor refutes the reverse spatial target.
These stops remain in force with their original hypotheses. The inspected
local records contain no duplicate majorant/trace for this exact Y.

### Primary inputs and exact limits of import

1. **ODE and interpolation tools, reused.** Teschl,
   [*Ordinary Differential Equations and Dynamical Systems*, author-hosted
   April2012 version](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf),
   Lemma2.14/Corollary2.15 pp52-53, Theorem3.9 p81,
   Lemma3.11(3.91)/proof p83, Theorem6.1/proof pp189-190.
   Reviews992/994 inspected the local smooth-flow, compact-continuation,
   continuous-coefficient linear-system and Abel-Liouville statements.
   Use them on the original smooth punctured domain for fixed distinct
   initial data, or on the already justified local coefficient charts.
   They supply neither a common initial distance from the divisor nor
   a uniform physical-root Jacobian bound. Review1016's de Boor,
   *Divided Differences*, Surveys in Approximation Theory 1(2005),
   [Sections8-9 pp60-64, (41),(44),(49)-(52)](https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf),
   remains supporting coverage for the audited coefficient Hessians.
   No general ODE or interpolation theorem needs reproof.

2. **Dominated convergence, reused and checked at the primary locator.**
   John K. Hunter, *Measure Theory*,
   [Chapter4, Theorem4.24 and Section4.6, printed pp49-50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf#page=11).
   Read the statement, Fatou proof and complex/a.e. qualifications.
   Measurable functions converging a.e. under one integrable absolute
   bound have convergent integrals; on a noncomplete space the limit's
   measurability needs attention. The intended measure is completed
   Lebesgue measure on I. For L1 convergence the future application is
   to the nonnegative absolute difference, along arbitrary time sequences
   tending to zero. That application must first verify convergence,
   measurability and domination; DCT does not construct the majorant.
   This is the undated author-hosted chapter version also inspected in
   review994, not a newly inferred edition. An additional MIT Lecture12
   PDF (Casey Rodriguez, 1April2021, printed p63) was inspected for its
   complex extension, but adds no essential input. A Driver PDF timed out;
   it is not used and creates no essential blocker.

3. **Root/coefficient Jacobian, supporting identity only.**
   Jayadev Athreya, Alexander Bufetov, Alex Eskin and Maryam Mirzakhani,
   [*Lattice Point Asymptotics and Volume Growth on Teichmüller Space*,
   author-hosted version dated 17September2011](https://www.math.uchicago.edu/~eskin/final_final.pdf#page=40),
   AppendixA, printed p40, monic-polynomial setup, (A.5) and its
   antisymmetry/degree justification. This records the root-to-coefficient
   Vandermonde Jacobian. Only this algebraic identity is a supporting
   input; their Teichmüller measure theorem is not an import here.
   Any use in the centered/scaled coordinates must retain local
   distinct-root charts and check coordinate order, sign and scaling
   against C467f's existing exact formula. It does not make the root
   inverse smooth across the discriminant or bound this pullback.

4. **Stronger-looking root-flow comparison, not an import.**
   Brian C. Hall and Ching-Wei Ho,
   [*The heat flow conjecture for polynomials and random matrices*,
   Letters in Mathematical Physics 115,60 (2025)](https://doi.org/10.1007/s11005-025-01946-9),
   published 26May2025, Section3.1 Proposition3.1, (3.1)-(3.5)
   and its proof through the antisymmetric cancellation. Its hypothesis
   is polynomial heat evolution with distinct roots at a given complex
   time; it gives local holomorphic root paths satisfying
   dz_j/dtau=-(1/N)sum_{k!=j}(z_j-z_k)^(-1).
   The proof uses simple-root implicit differentiation and the polynomial
   heat equation. Our raw field depends on conjugate differences and
   the actual nonpolynomial background g. No identification with this
   heat evolution is justified. The paper's large-N transport assertions
   are labeled conjectures; they are not a time-uniform L1 theorem here.
   The Csordas-Smith-Varga and Choodnovsky references cited there are
   unread historical leads and unnecessary for the stated comparison.

The previously inspected TNV2017 AppendixB and FM2020 local variational
and Gram identities retain review1012's scope. No new thimble theorem,
deformation invariance or integral conservation is imported. Their
general formulation is not the missing prescribed-flow majorant.

### Authorized specialization and discriminating test

SPECIALIZE covers exactly the saved TARGET, with no new broader
subtarget. Retain C466z/audit988 normalization, C466/audit993 analytic
bound and C467e-g/audit1017. A bounded attempt may use their centered
coefficient variation and full reconstruction to test whether the
Vandermonde weight compensates the root-coordinate determinant.
It must exhibit a measurable G in L1(I), independent of every
0<=t<=T_0 and of arbitrarily small unequal initial gaps, for the
original A(t,u). Every determinant factor and any inverse-gap
cancellation must be justified; bounding factors separately by
nonintegrable expressions is not a negative result. Only after this
may the initial fixed-point flow dependence and cited DCT be applied.
No compensation identity or bound is established in this review.

Continue if the complete target holds. Retire it only on a rigorous
actual-flow obstruction to its asserted domination or trace. Failure
of one sufficient estimate is inconclusive; preserve that obstruction
and require a refined mechanism before repetition. Success would add
one initial spatial top-form trace, while spacetime minors/current,
payment, interfaces, global assembly, all degrees and Xi transfer
remain independent unpaid obligations. No smooth diagonal extension
or control of normalized K_- is required or supplied.

This is established-route development rather than a newly proposed
central mechanism: prospective classification REPRODUCTION and routing
proof_attempt/development, deep_research/xhigh for the singular
determinant cancellation. The creative priority does not justify
renaming this specialization creative. This necessary amplitude test
is the present blocker to advancing the signed reverse-deformation
mechanism; no independently assessed new central creative target is
selected in this narrowly gated review. The changed ready assessment
requires separate next-turn approval before mathematics.

Mathlib: reuse review994's inspected supporting names
`MeasureTheory.tendsto_integral_of_dominated_convergence` and
`MeasureTheory.tendsto_integral_filter_of_dominated_convergence`,
with a.e. strong measurability, integrable norm majorant and a.e.
convergence (plus the filter version's countable-generation hypothesis).
Full matching coverage for this singular reverse pullback is not
checked; unknown coverage is not absence. No Lean verification.
