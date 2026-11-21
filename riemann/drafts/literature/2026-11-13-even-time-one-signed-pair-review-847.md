# Single time-one signed pairing — nomination847, source review848

TARGET: Assess source coverage for a certified sign test of B_1=<u,exp(-A_e)v> at time one for exactly C759i's fixed even quartic pair and C759a's complete operator, retaining both poles and all five masked shifts.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step848 inspected primary Jacob-Zwart2010-11 Lemma10.1.2 and its full proof, Jawecki-Auzinger-Koch2020 Section2/Theorem1 and proof, and Colbrook2110.06350v1 Section3/Theorem3.1 and its three proof steps; exact queries, limits and local failure comparisons are below. No actual time-one sign theorem was found in the sources checked; no novelty inference is made.
SOURCE_EVIDENCE: Jacob-Zwart, 14th Internet Seminar2010-11, Definition10.1.1/Lemma10.1.2/(10.3), printed p120, give the needed classical-solution defect identity. Reuse C759h Proof1-2 for the floor/domain/full action, C759a/k for the closed realization, C759i for the fixed pair, and L515/C759m audit847 for their separate unsigned scopes.
COMPARISON: Direct complete-L2 defect certification is covered by the known variation-of-constants method; applying it and bounding one full residual remain work. Matrix-only Krylov bounds leave compression error unpaid; Colbrook's stronger algorithm additionally needs an operator core and certified action inner products. C759i and the stopped parameter-16 witness do not determine B_1.
GAP: Construct one exact finite evolution candidate and rigorously bound its complete spatial defect, Fourier tail, time integration and arithmetic errors against its signed pairing. No enclosure or sign has been computed; successful discrimination is not promised. Ground-state sign/simplicity, parity and Xi realization remain open.
REASON: Essential general certification coverage is now available for a known-method scalar calculation. Prefer the direct defect identity over building the additional core/oracle infrastructure of a general contour solver; do not repeat unsigned smoothing or the old triangle-residual estimate as a sign certificate.
LITERATURE_REASON: The saved REVIEW_REQUIRED target concerns a prescribed-time signed observable, outside the ready unsigned smoothing import and all-times order test; the full evolution-error theorem was the missing essential source input.
SCOPE: One fixed t=1, C759i's exact u,v and C759a's complete even half-width1 realization; one space W=span{v,(1-x^2)P_0,(1-x^2)P_2,...,(1-x^2)P_508}, with P_j(1)=1. Only a REPRODUCTION calculation via the full L2 defect is covered. No time/pair/support/basis sweep or extrapolation from t=0 is covered.
COVERED_TARGET: Attempt one certified enclosure of B_1=<u,exp(-A_e)v> for C759i's fixed quartic pair using a single declared 256-dimensional Galerkin evolution and its complete L2 defect, retaining both poles and all five masked shifts.

## Preserved nomination847 (historical)

The paragraphs below record the original uncovered nomination. Their
REVIEW_REQUIRED/unread wording describes847, superseded only by the
completed source comparison848 below. They are not current instructions.

This is an uncovered continuation, not approval to do mathematics in847.
No primary theorem is asserted to cover it. It must receive a separate
literature-only turn, with precise hypotheses and essential proof cases
inspected before any mathematical attempt. Reuse adequate L515/C759m
coverage for unsigned bounds; the missing issue is a signed certificate.

The main gap remains actual-Xi all-degree mixed positivity. The proposed
intermediate mechanism is positivity improvement at one specified time
as a possible route to a signed simple lowest-even eigenvector. This
nomination tests only one necessary pairing, not positivity improvement
itself. Any later spectral consequence requires its own exact theorem
hypotheses; no compactness, isolation or positive eigenvector is assumed
as an input here.

The prospective bounded test seeks a rigorous interval enclosing B_1
whose upper endpoint is strictly negative. Such evidence would rule out
positivity preservation at time1. A nonnegative value would be
inconclusive for positivity improvement or ground-state sign. An
enclosure crossing zero is also inconclusive. Do not expand to a time
or pair sweep to rescue an inconclusive test. The source review should
park the proposed calculation if it cannot identify an effective full
remainder bound that could discriminate its sign; an absolute smoothing
bound alone is insufficient.

Essential inputs for assessment are C759i(1)-(3), C759m(1)-(5) and
audit847, L515(7)-(10), and C759a/k's unchanged closed realization.
C759j's arbitrary-domain residual obstruction and the parameter-16
resolvent stops must be compared, not silently bypassed. Historical
instructions against substituting eventual positivity within those
attempts remain preserved; this proposes a new fixed-time diagnostic
after a distinct smoothing input, not a continuation of those attempts.
Do not assume any large-time positivity or use numerical signs as proof.

If the assessment finds a concrete genuinely new signed mechanism,
nominate the subsequent proof attempt as creative with a precise
bounded test and escalation. If only a routine certified obstruction
calculation is justified, route it as calculation. Do not label the
current unsigned audit or this uncovered nomination creative.
Sign, simplicity, parity ordering and Xi realization remain unresolved.
No cross-notebook input is proposed. Full matching Mathlib coverage
has not been checked.

## Completed source review848 — 13 November2026

This is one literature-only comparison, with no new lemma, mathematical
script, spectral bound or signed enclosure. The local outcome is source
coverage for a subsequent known-method calculation, not progress beyond
the inspected sources and not a proof that the proposed sign is negative.
The main gap remains L030-L032/C032a actual-Xi all-degree mixed positivity.
The diagnostic's possible downstream use is to exclude time-one cone
preservation as a proposed ground-state sign mechanism. Even positivity
improvement at this time would still need a separate spectral argument;
one nonnegative pairing cannot establish it.

### Primary theorem and inspected proof

[Jacob-Zwart, *14th Internet Seminar: Infinite-dimensional Linear Systems
Theory*,2010-11](https://www.math.tecnico.ulisboa.pt/~czaja/ISEM/14internetseminar201011.pdf),
Definition10.1.1 and Lemma10.1.2, printed p120 (PDF p128), assume a
C0-semigroup T with generator H on a complex Hilbert space, continuous
f on [0,tau], and a classical solution x: C1 into the space, taking
values in D(H), satisfying x'=Hx+f. The conclusion is continuity of Hx
and x(t)=T(t)x(0)+integral_0^t T(t-s)f(s)ds, equation(10.3).
The full proof was inspected: domain membership handles the generator
difference quotient; compact-time boundedness and strong continuity
handle the moving vector; differentiation of T(t-s)x(s) and integration
give(10.3). This is an import, not a new general error theorem.
For the proposed application H=-A_e (or its fixed scalar shift), the
candidate must satisfy those domain/regularity hypotheses; deriving and
evaluating its error certificate is deferred to research.

### Stronger results and why they do not themselves decide the test

[Jawecki-Auzinger-Koch, *Computable upper error bounds for Krylov
approximations to matrix exponentials and associated phi-functions*,
BIT60 (2020),157-197](https://doi.org/10.1007/s10543-019-00771-6),
version of record11September2019: inspected Section2,(2.1)-(2.9),
Section3, Proposition2 and Theorem1 including their proofs. The setting
is a finite matrix, normalized initial vector, |sigma|=1, an exact
Arnoldi identity and nonexpansive numerical range. Theorem1 bounds its
Krylov error by tau_(m+1,m) gamma_m t^m/m!. Its proof uses the defect
integral and divided differences. This controls matrix-exponential
error, not compression of A_e. It cannot certify the proposed pairing
without a complete operator residual. Shift-and-invert is expressly
outside that theorem's immediate scope (Remark3). No infinite-dimensional
extension of the theorem is imported.

[Colbrook, *Computing semigroups with error control*,
arXiv:2110.06350v1,12October2021](https://arxiv.org/pdf/2110.06350v1),
Section3, Theorem3.1 and Algorithm3.1, PDF pp6-9: read the input
definition and all three proof steps. It gives arbitrary Hilbert-norm
accuracy for a generator represented in an orthonormal basis whose
span is a core for the operator and adjoint. Inputs include certified
matrix elements, action Gram elements, vector coefficients/norm and
semigroup growth constants. The proof uses regularization, controlled
contour tails/quadrature and full-residual resolvent solves, invoking
Appendix PropositionA.2. The HTML calls these Theorem7/Algorithm1 and
Proposition11. An actual-Q implementation of its operator core and
action-Gram evaluations is not in hand; a form core is not automatically
that operator core. This stronger result is a comparison, not an imported
ready solver. Its Appendix proof and Section5 optimized contour theorem
were not inspected; neither is used for the selected continuation.

### Exact local comparison and prospective specialization

The essential local statements were read in C759h Proof1-3, C759i,
C759a Proof1, C759k(2)-(9), C759m(1)-(5)/audit847 and L515(7)-(10).
Use the existing A_e>=-10I and H1_0 operator-domain/full-action
statements of C759h, with their qualifications; do not establish a new
floor or assume actual positivity. W above consists of its admissible
even polynomials and the prescribed quartic v. Including v fixes the
initial datum exactly, rather than hiding an initial projection error.
The source lemma does not require W to be an operator core or invariant.
The later calculation must explicitly check C1 regularity and continuity
of the complete action of its chosen finite path. Working with A_e+10I
is an allowed fixed scalar normalization, not a time/parameter search;
the spectral-theorem scalar factor must be restored in reporting B_1.

L515's factorial remainder bounds bounded-perturbation order, but does
not evaluate the killed reference evolution. Replacing the killed Levy
kernel by a subordinated killed Brownian kernel or commuting compressed
convolutions would not be covered. The direct defect method avoids this
unpaid reference-kernel computation. C759m is supporting context, not a
signed remainder theorem or an essential substitute for a full residual.

C759h/stop823 used parameter-16 and a static witness; its conservative
residual1.3555 missed the required0.00038969 threshold. It is preserved.
The new method must enclose the combined residual BEFORE taking its norm,
including cancellation, not recycle ||forcing||+||w'||+35||w||. C759j
and stop831 obstruct unrestricted L2-to-interior-sup conversion; this
observable remains in L2 throughout. Stop829's eigenvector isolation and
weighted sign requirements are not assumed. Stops838/843 closed repeated
source-approval sequences after successful unsigned bounds, not the
present time-one scalar calculation. C759i's negative infinitesimal
pairing does not settle t=1. No existing time-one sign certificate was
located in the narrowly searched November13 even-family assessments.

The calculation must bound the ENTIRE defect w'+A_e w in L2(I), using
C759h(2)'s full-line multiplier before restriction, rho=r(|x|)/2 when
using the split, all ten masked translations and both poles. Certified
finite quadrature alone is insufficient without its Fourier/spatial
tail and roundoff bounds. C759h(1) and its exact piecewise-polynomial
data give a covered starting envelope for those tails; sharper estimates
must be proved in the subsequent reproduction, not assumed from a sample.
An unvalidated norm sample or projected defect is diagnostic only.
No positivity, spectral isolation, ground-state eigenvector or Xi
realization is used as an input. No full residual bound is derived here.

One declared finite evolution in this W is authorized after separate
approval. Exact candidate data, all error terms and complete certificate
must be saved. Precision/quadrature refinement may certify that same
candidate; changing W, t, u or v to rescue a failure is outside scope.
The decisive threshold is a rigorous upper endpoint for B_1 strictly
below0. A certified nonnegative value does not establish cone preservation;
an enclosure crossing0 or an unresolved tail is inconclusive. Either
ends this fixed test; preserve its evidence and reassess before another
attempt. No claim that the method will meet the threshold is made.

### Search record, access and routing

Queries included `unbounded operator semigroup exponential a posteriori
error residual variation of constants Galerkin defect bound`,
`Jawecki Auzinger Koch computable upper error bounds Krylov approximations
matrix exponentials residual 2020`, `"Weil" "semigroup" "time" "positivity"`,
`"variation of constants" "Proposition" "classical solution" Engel Nagel
pdf semigroups`, `"Computing semigroups with error control" "Theorem" 3.1`,
and targeted classical/inhomogeneous Cauchy-problem searches. Local
searches were limited to the November13 even-family assessments/stops
and the named earlier coverage. A guessed review filename was absent;
the existing scoped assessment paths were used instead. No global
checkpoint, sibling-proof or cross-notebook search was performed.

Engel-Nagel author PDF retrieval timed out; its previous bounded-
perturbation coverage was reused only for that established scope.
Jacob-Zwart's accessible complete proof pays the different missing
identity, so this is not a persistent essential source blocker.
Colbrook's Cambridge PDF timed out; arXiv v1 was accessible. Daners-
Koch Medina's 2014 reissue and splitting/parabolic-estimator results
were discovery leads only, not theorem coverage used here. Screenshot
retrieval was not used as proof evidence; the complete
Jacob-Zwart lemma text and proof were read from the primary PDF text.
No Mathlib declaration was inspected; matching and supporting coverage
remain unchecked, with no absence or formal-verification claim.

Recommend calculation/standard/high, REPRODUCTION, for the exact
COVERED_TARGET. This is a routine certification mechanism, not a creative
central-gap proof attempt. The creative-route blocker is the absence of
a new signed mechanism connecting a single pairing to all-degree actual-Xi
positivity; do not label this known defect formula creative. The newly
ready continuation requires separate source-gate approval next turn;
that deferral does not undo this completed comparison. No further
browsing is needed unless a specific source/hypothesis defect emerges.
