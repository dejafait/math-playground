# Finite signed cancellation of smoothed laws — source comparison1299

TARGET: Assess whether a finite signed combination of distinct positive-width Gaussian-smoothed one-sided reciprocal probability laws can remain a probability measure and acquire a finite positive exponential moment.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1299 screened the exact signed-law question, finite signed mixtures, exponential moments, analytic cancellation and finite-mixture identifiability; local duplicates/failures and external queries are recorded below. No matching theorem was located in this bounded search; no novelty inference.
SOURCE_EVIDENCE: Sra2611.00345v1 Theorem4.1/p9, PropositionA.8/p17, LemmaA.4/p13, Proposition3.1/pp5-6 and proof/p21; Sra2610.00584v1 Corollary2.5/p6; Boyer2015 Definition2.1/Lemma2.2/p6; DLMF1.14.47/49. Essential statements and proof cases inspected as specified below.
COMPARISON: Individual-law divergence cannot be imported as signed-combination divergence. Existing signed-convolution and Gaussian-mixture results concern different operations. Standard analytic tools cover a necessary-feature test, while finite signed cancellation and positivity remain unproved.
GAP: No inspected result settles the exact finite-law question. A bounded transform obstruction attempt is now source-covered; any higher expansion, continuation across the cut, linear-independence claim or positivity certificate must still be proved. Cancellation of a leading term alone does not settle the target.
REASON: Accessible primary analytic inputs permit one test of the proposed compensation operation without subtracting divergent moments. This approves exploration, not a theorem, a representation of the unsmoothed law or a new central signing mechanism.

## Original nomination1298 (historical)

Proposed bounded object, not an asserted result: for finite r≥2,
distinct σ_j>0 and real a_j with Σa_j=1, consider the signed measure
ν=Σa_j ν_(σ_j), with νσ defined canonically in C032j. Ask whether ν
can be nonnegative and have ∫exp(cu)dν(u)<∞ for some c>0.
The measure must be nonzero; an identically zero signed combination
is excluded by its mass. Cancellation cannot be tested by subtracting
infinite expectations. Any later proof must use complete tail or
transform evidence, with positivity treated separately.

This is a proposed necessary-feature test, not a nominated exact
representation of the unsmoothed law. Continue only if source review
identifies exact coverage or an independently testable uncovered claim
with access to the required complete asymptotics/analytic hypotheses.
Stop this finite-mixture mechanism if an inspected theorem rules it
out, or park it if its essential source evidence remains unavailable;
do not retry individual-law Gaussian positivity or change route names.

Inputs for any continuation: C032j and its two cited preprints;
L018/L024 fix the divisor. L030-L032/C032a remain the downstream gap,
not mathematical positivity inputs. The source Corollary2.5 comparison
uses only the existence of some positive exponential-moment interval,
not its optimization. No cross-notebook theorem is needed.

The completed1298 step did not test this claim mathematically, approve
it as ready, perform a new literature assessment or assert novelty.
The next turn must be literature-only. An eventual proof-purpose route
must depend on that review; no creative proof attempt is approved now.

## Saved interim source review1299

The current invocation is literature-only. Direct fixed-v1 source
retrieval succeeded. Inspected the smoothing paper Theorem4.1 and
its proof (printed p9), PropositionA.8 and its complete proof
(printed p17), and Proposition3.1/(3.2)-(3.3) (printed pp5-6).
Theorem4.1 is an individual-law theorem, whereas PropositionA.8
records a leading square-root singularity only. Neither is cited as
a signed-cancellation theorem. Boyer, The speed of convergence in
the renewal theorem, 19June2015, Definition2.1/Lemma2.2 and full
proof (printed p6), supplies the exponential-moment-to-holomorphy
necessity for a probability measure. Applicability and a bounded
continuation remain under review; no new mathematical conclusion,
lemma or mathematical script has been produced.

## Completed source comparison1299

This completes the originally required literature-only step. The
REVIEW_REQUIRED nomination above records the state at the end of1298;
it is preserved as history, not as a competing current decision.
Readiness proposed here receives the supervisor's separate approval
next turn. No mathematical attempt was performed during this review.

### Exact object and local comparison

Retain the finite r, distinct positive widths, real coefficients of
sum one and C032j definitions in the nomination. The question concerns
a sum of measures, not convolution of measures, smoothing a density,
or a sum of Bernstein exponents. Positivity must hold as a measure;
no density assumption or infinite-divisibility assumption is supplied
for the combination. Its positive exponential moment is the threshold.
L030-L032/C032a remains the downstream all-degree actual-Xi sign gap.
This necessary-feature test could rule out this proposed surrogate
or identify a candidate deserving separate positivity and transfer work.
It supplies no initial signs, singular-block control or realization.

The local screen used `rg` in drafts/literature and ATTEMPTS for
`finite signed.*smooth`, `signed.*smooth.*law`, `smoothed.*cancel`,
`cancel.*smoothed`, and `Sra.*tail`, then the specific17November
Gaussian/reciprocal assessments. C032j and assessment1297 were read
in full. Stop1297 was read and remains in force for its individual-law
surrogate. The finite-reference atom assessment1246 concerns a
finite-polynomial multiplier and signed convolution, not this operation;
no sibling notebook or cross-notebook theorem was read. No exact
local duplicate of the signed-law question was identified. This is a
bounded search statement, not proof of originality.

### Primary inputs inspected

- [Sra smoothing, fixed v1,11November2026](https://hexagonmath.org/pdf/2611.00345v1):
  Theorem4.1/full proof p9 is individual-law only. PropositionA.8/full
  proof p17 gives B_sigma(s)=2*pi*p_sigma(0)*sqrt(s)+O(s), s down to0.
  LemmaA.4/full proof p13 gives an even entire profile and logarithmic
  real-axis growth. Proposition3.1/(3.2)-(3.3), pp5-6, with complete
  Gaussian-integral proof p21, gives the exact heat-time transform.
  The Stieltjes formula for B_sigma' in the A.8 proof is absolutely
  convergent. The proof's small-r and large-r estimates were read;
  they do not establish a convergent all-order expansion.
- [Sra original, fixed v1,20October2026](https://hexagonmath.org/pdf/2610.00584v1):
  Corollary2.5/(2.9), p6, and its proof through p7 give the unsmoothed
  transform on Re(s)>-gamma_1^2. Section2.4 states its density mass
  is1/c0; use its probability normalization when comparing laws.
  Earlier applicability and finite-zero coverage are reused from C032j.
- [Boyer,19June2015 manuscript](https://maths.jbboyer.fr/documents/articles/renewal.pdf),
  Definition2.1/Lemma2.2 and complete proof p6: a Borel probability
  measure on R with an exponential absolute moment of order eta>0
  has a holomorphic Fourier-Laplace transform on |Re(z)|<eta, with
  derivative bounds on smaller strips. The proof uses domination and
  differentiation under the integral. Its renewal/drift assumptions
  are not hypotheses of Lemma2.2. For the proposed nonnegative law
  supported on [0,infinity), the positive moment is exactly the
  absolute moment. This matches the lemma only conditional on the
  proposed combination being a probability measure.
- [NIST DLMF,Section1.14(vi)](https://dlmf.nist.gov/1.14#vi),
  equations1.14.47/49 and their hypothesis paragraphs: the Stieltjes
  boundary-jump formula assumes local absolute integrability on every
  finite interval and convergence of the transform, at positive
  arguments having the stated one-sided limits. It does not require
  a positive density. Endpoint0 is not a positive interior argument.
  A later use must verify convergence and local limits for its chosen
  integrand; this review supplies no endpoint continuation theorem.

Supplementary inspected input: [Remling, Distributions](https://math.ou.edu/~cremling/teaching/lecturenotes/ln-dist.pdf),
Theorem3.3 and complete proof p15, is the distributional
Sokhotski-Plemelj formula; both imaginary approximate-identity and
real principal-value cases were read. This is not itself pointwise
boundary regularity at0. No use of this supplementary theorem is
required if the DLMF form suffices. These are source tools, not a
new locally proved cancellation result. No manuscript-wide audit,
certificate replay, or source-independent verification is claimed.
Mathlib matching coverage is unchecked and unknown.

### External search and exclusions

Queries actually used include:

- `"Gaussian" "signed" "mixtures" "exponential moments" reciprocal Xi`
- `"Sra" "smoothing" "Riemann" "signed"`
- `"signed mixtures" "exponential" tails Laplace analytic`
- `"finite linear combinations" "Laplace transforms" "branch" probability`
- `"Gaussian-smoothed" "reciprocal" "signed"`
- `"Gaussian smoothing" "Xi" "signed combination"`
- `"reciprocal laws" "finite" "mixture"`
- `"2611.00345" "cancellation"`
- `"finite linear combinations" "Laplace" "exponential moments"`
- `"finite" "mixtures" "analytic" "stable" identifiability Teicher`

The smoothing PDF was also searched for `signed`, `combination`,
`cancellation`, `mixture`, and `asymptotic`. Hits on signed profiles,
translated kernels and strip budgets concern other objects. Search
results on finite-mixture identifiability (Teicher/Yakowitz-Spragins),
stable mixtures and signed exponentials are unread leads, not imports:
no theorem from them is asserted here. Merely identifying a law from
its mixture parameters would not by itself answer membership in the
class with a positive exponential moment. No source blocker persists.

### Bounded continuation and stopping test

SCOPE: One analytic obstruction attempt for the exact finite signed-law
question. Begin with the first square-root term, then test the
cancellation case using the source Stieltjes representation and a
justified boundary or higher-order argument. Any claimed exclusion
must include coefficient choices cancelling the first term; a
noncancelling-coefficient statement alone is a partial result. Finite
sums of bounded positive-s Laplace integrals may be considered; sums
of divergent moment integrals may not.

The sought discriminator is an uncancellable nonanalytic feature for
every allowed nonnegative combination, or an explicit combination
with proved positivity and a positive exponential moment. A rigorous
necessary cancellation identity may be useful partial progress, but
is not the discriminator itself. Continue only with a new informative
constraint beyond the imported leading cusp. If this bounded attempt
only restates the cusp or cannot distinguish cancellation from
noncancellation, retain the unresolved case and reassess the mechanism;
do not call it an impossibility result or repeat the same test.
A proof of impossibility stops this finite-combination route only.
A positive example still needs independent identification, PF signs
and transfer to the main gap. No parameter optimization or unbounded
search is preapproved.

The next mathematical work is development of this analytic obstruction,
not a creative sign-producing construction. The central creative-route
blocker is still the absence of a paid positive-measure compensator
and actual-Xi transfer. Do not label a necessary cusp calculation as
a new signing mechanism. Completed step classification is
NOVELTY_UNCHECKED; subsequent EXPLORE work may use REPRODUCTION or
POTENTIALLY_NEW as its actual outcome warrants, without originality
claims. No new mathematics has been derived and approved together.
