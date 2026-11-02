# Three-wave stationary bulk: source comparison

TARGET: Test whether S3(u)=sqrt(2/3) sum_{i=1}^3 cos(U_i u+B_i), with independent uniform U_i in [-1/2,1/2] and independent uniform B_i in [0,2pi], has paired jet covariance L473 (6), bounded stationary derivatives and E(S3(0)S3''(0)-S3'(0)^2)_+>=1/288.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded searches of finite random-phase sums, Laguerre expressions, clipped quadratic expectations and exact three-step densities found no inspected theorem deciding the specified derivative-weighted threshold; scoped local duplicate/failure checks found L576 and this nomination, not a completed three-wave test. Search details and unread leads are recorded below; no novelty inference follows.
SOURCE_EVIDENCE: Reuse Rahimi--Recht (2007), Section 3, Theorem 1, equation (2) and random-phase formula, PDF pp. 2--4, from the preceding assessment; newly inspect Csordas--Escassut (2005), Definitions 1.1/1.2 and Theorems 2.1/2.2, pp. 331--334 including the Theorem 2.1 proof; Borwein--Straub--Wan--Zudilin author-posted 32-page manuscript, Sections 1--3, (5),(7),(17)--(20), PDF pp. 1--4,7--8, at the relevant definitions/formulas and Example 2 verification discussion.
COMPARISON: Known random-phase covariance is reusable, but the inspected Laguerre sign theorem requires an unverified L-P premise and short-walk radial densities omit the joint frequency-weighted derivatives. None supplies the required clipped threshold. L576 remains a two-wave obstruction only; the three-wave outcome is unproved.
GAP: Determine full K, bounded stationary derivative support and the exact three-wave clipped expectation versus 1/288. Full fourth constraints, rare paths, derivative-preserving correction and actual-Hardy boundary/tail transfer remain independent gaps.
REASON: Essential elementary spectral and sign-theorem coverage is sufficient for the explicit bounded test without importing a realization theorem or a special-function density. Investigate only the stated missing nonlinear comparison; no three-wave calculation or new lemma was made in this literature-only turn.
LITERATURE_REASON: The target changed from two to three equal-amplitude waves and arrived REVIEW_REQUIRED; the two-wave assessment did not cover the changed nonlinear statistic. This is its first theorem-level comparison, not extra browsing on a ready target.
SCOPE: Exactly the TARGET's six mutually independent variables, ordinary u derivatives, Euclidean paired jet norm and every entry of L473 (6); include coincident/zero frequencies and zeros of S3. No fourth-moment, actual-Hardy stationarity, Gaussian replacement, RH or real-zero premise is authorized.

## Preserved nomination

The paragraphs below retain the pre-review nomination and its required
test. Its request for a source turn is fulfilled by the completed review
below; it is not a second pending action.

This is one proposed bounded intermediate, not a creative central-gap
mechanism or a complete stationary feasibility target. Essential input
IDs are L473 (6), for the full paired covariance comparison, and L576,
for the exact obstruction motivating the change. L471 supplies the
negative-mass motivation, not a premise of this proposed construction.
No cross-notebook input is needed.

The review must inspect primary hypotheses for known finite-wave
Laguerre-form sign results or exact clipped moments, search stronger
results and local duplicates/failures, and distinguish an inspected
theorem from discovery snippets. Reuse the preceding spectral source
where applicable. Do not perform a three-wave calculation in that
literature-only turn or treat covariance as the nonlinear conclusion.

The later bounded test, if approved, must compare the complete clipped
expectation with exactly 1/288, together with the whole matrix K and
bounded stationary derivative support. A certified upper bound below
the threshold rejects this choice; a passing value supplies a bulk
only; a straddling interval remains exploration. No lower threshold
substitutes for this one. The full 126 fourth constraints, rare paths,
derivative-preserving correction and actual-Hardy boundary/tail
transfer stay open regardless. Matching Mathlib coverage is unchecked.

## Completed source review, 2026-10-31

### Known results and applicability

Reuse the inspected spectral material in
`drafts/literature/2026-10-31-stationary-hardy-path-feasibility.md`:
Ali Rahimi and Benjamin Recht, *Random Features for Large-Scale Kernel
Machines*, Advances in NIPS 20 (2007), Section 3, Theorem 1, equation (2),
the subsequent real random-phase formula and Algorithm 1, PDF pp. 2--4,
[author PDF](https://people.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips.pdf).
Its hypotheses are a continuous positive definite translation-invariant
kernel and its normalized probability spectral measure. Independent
uniform phases give the real cosine feature comparison. The source
permits finite independent sampling; the local spectral law is uniform
on [-1/2,1/2]. Its theorem does not prescribe the clipped observable.
The later calculation must verify the normalization sqrt(2/3),
derivatives through order two at both heights, all cross entries,
stationarity in joint law and the deterministic norm after scaling.
These are necessary applicability checks, not a reproof of an arithmetic
moment theorem. No assertion that S3 passes them is made here.

George Csordas and Alain Escassut, *The Laguerre inequality and the
distribution of zeros of entire functions*, Ann. Math. Blaise Pascal
12 (2005), 331--345,
[primary PDF](https://www.numdam.org/item/AMBP_2005__12_2_331_0.pdf),
Definitions 1.1/1.2 and Theorems 2.1/2.2, pp. 331--334, were read.
Their S(A) has canonical factor exp(-az^2+bz), a>=0, b real,
zeros in |Im z|<=A and summable reciprocal squared moduli; L-P requires
real zeros. Theorem 2.1 gives (f')^2-ff''>=0 for f in L-P; its proof
handles the exponential case and identifies multiple-zero equality.
Theorem 2.2 requires every generalized Laguerre inequality at every
real point. No L-P membership or such hierarchy is supplied for S3.
These results therefore do not decide its clipped expectation; imposing
their premise would change the target. No reproof or import is made.

Jonathan M. Borwein, Armin Straub, James Wan and Wadim Zudilin,
*Densities of short uniform random walks* (with an appendix by Don
Zagier), Canad. J. Math. 64 (2012), 961--990,
[DOI](https://doi.org/10.4153/CJM-2011-079-2),
[author-posted 32-page manuscript](https://arminstraub.com/downloads/pub/walks-densities.pdf),
retrieved 2026-10-31: read the model definition in Section 1,
Section 2 (5),(7), and Section 3 (17)--(20), Example 2 and its
verification discussion (PDF pp. 1--4,7--8). The observable is the
radial distance of independent uniform unit steps. Equation (7)
specifies the independent phase integral; (20) supplies its three-step
density in hypergeometric form. Example 2 points to the differential
equation verification. This is an exact finite-size comparison, not
a large-wave Gaussian limit. It is not the joint law with random
frequency weights in first and second derivatives. No sufficiency
for the local clipped form is established; no special-function formula
or proof from this paper is imported or needed by the planned test.

### Discovery evidence, inaccessible leads and duplicate checks

Queries included `random trigonometric sums Laguerre inequality log
concavity random phases finite waves`; `"random trigonometric"
"positive part" derivative`; `Laguerre inequality trigonometric
polynomial real zeros cosine sums`; `"random trigonometric"
"Laguerre"`; `"random phase" "log concavity" cosine`;
`"trigonometric sums" "positive part" expectation`;
`"random phase" cosine sum exact probability distribution finite Bessel`;
`"random trigonometric" "Laguerre expression"`;
`"random trigonometric" "logarithmic derivative" expectation`;
`"three" "cosines" "Laguerre inequality"`; and the exact Blevins
title and Borwein--Straub--Wan--Zudilin density title below/above.
Additional discovery queries were `"three" "random waves"
"derivatives" probability`; `"random trigonometric" "fixed"
"phases" distribution derivatives`; `"Laguerre inequality"
"exponential" "polynomial" cosine`; `"S S" "Laguerre" "random"
trigonometric`; and `"random trigonometric sums" finite non Gaussian
expectation quadratic form`.
These searches supplied leads, not a certified exhaustive search.

B. Bojanov, *Turan's Inequalities for Trigonometric Polynomials*,
J. London Math. Soc. 53 (1996), 539--550,
[publisher record](https://doi.org/10.1112/jlms/53.3.539): the PDF URL
redirected to the abstract. Its abstract describes real-zero
trigonometric polynomials and convex increasing functions of absolute
derivatives. Full theorem hypotheses/proofs remain unread, so this
is not a theorem-level exclusion or input.

R. D. Blevins, *Probability density of finite Fourier series with random
phases*, J. Sound Vibration 208 (1997), 617--652,
[DOI](https://doi.org/10.1006/jsvi.1997.1207): publisher search text
describes scalar, peak and envelope distributions for finite sine sums.
The article request returned HTTP 403; no theorem or proof was read.
Its possible wider joint-distribution coverage remains unassessed.
Do not claim the paper lacks a matching theorem. It is an unread lead,
not an essential input to a direct compact phase/frequency integration.
No source access retry or theorem import is the continuation.

Read L473 through Sections 1--4, in particular all 21 second and 126
fourth tolerances (2), the full K integral (6) and its marginal block
(7); read the complete L576 proof, including degenerate frequencies
and zeros. The nominated target uses only K from L473, not its
arithmetic asymptotics or constructed fourth moments. Read the scoped
import and two-wave stop records in
`ATTEMPTS/2026-10-31-stationary-hardy-process-import-stop.md` and
`ATTEMPTS/2026-10-31-two-wave-stationary-bulk-stop.md`.
A scoped search in lemmas/, ATTEMPTS/ and drafts/literature/ for
three-wave/S3, its normalization and clipped trigonometric terms found
no completed matching test. Other clipped stationary-square or
Poisson-transform hits concern different observables. No claim of
novelty follows. Earlier Gaussian/transport source stops remain in
force at their stated scope; no retry of a blocked realization theorem
is necessary for this independent explicit model.

### Authorized scope of a later calculation

DECISION EXPLORE covers exactly TARGET, pending the supervisor's separate
approval of this changed assessment. It licenses an ordinary bounded
calculation, not deriving and approving mathematics in this source turn.
The missing clipped comparison has no established matching source in
this review. Covariance, normalization and stationarity may be verified
directly as elementary source specialization; the nonlinear statistic
requires its own complete analytic argument or certified integration.
No Gaussian approximation, independence of the lag-one jets, or
inference from a positive numerical preview is permitted.

For this particular bulk, continue only if all three checks pass:
the complete K comparison, exact stationary bounded derivatives and
clipped expectation at least 1/288. A certified upper bound strictly
below 1/288 abandons this choice. A certified interval straddling it
is EXPLORATION. A positive lower bound below 1/288 is insufficient.
If numerical certification is chosen, its full errors, complete
load-bearing evidence and actual/required bounds must be retained;
a preview is not verification. No integration was performed here.

A passing bulk would still leave L473's full fourth tensor, rare paths
and derivative-preserving corrections unresolved; actual-Hardy
finite-interval boundaries/tails and Xi realization are separate.
No central-gap creative mechanism is justified by this source screen:
the nonlinear actual law and its transfer remain missing. The next
bounded specialization is not to be labeled creative to meet a routing
preference. Full matching Mathlib coverage is unchecked; no absence
claim or new lemma is recorded. PROOF.md and DAG.md need no change.
