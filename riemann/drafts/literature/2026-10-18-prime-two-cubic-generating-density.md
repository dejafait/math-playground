# Coverage: analytic sign test instead of further finite minors

TARGET: Assess an analytic generating-function sign test for the full fixed log-2 cubic moment sequence, using L432's valuation-sum template without increasing the finite Toeplitz cutoff.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 226 checked the local step-221/213 source comparisons, step-222 attempt, relevant step-222/225 histories, L431's valuation reduction and L432's coefficient/tail/moment sections; searched exact arithmetic and circle-density terminology externally; inspected the primary statements and relevant proofs below. No matching theorem deciding this arithmetic density was found in the sources inspected; no novelty claim follows.
SOURCE_EVIDENCE: Reuse the inspected fixed-rational source hypotheses in steps 213/221 and audited L406--L409/L430--L432; newly inspect Helton--Putinar (2007), section 3.1 Theorem 3.3(a)--(d) and proof, pp. 245--246, especially analytic clause (c); Zhou--Siadat, arXiv:2206.05105v1 (8 June 2022), Theorem 3.5 and proof p. 14 and section 7 absolute-Fourier-series paragraph. Direct links and qualifications below.
COMPARISON: The fixed positive rational source domain includes each separately fixed 2^(+/-j) character, while Herglotz supplies a whole-disk real-part criterion and Fourier uniqueness supplies identification of a summable density. None establishes this sequence's all-fixed-j physical limits, harmonic summability, rational generating expression or sign. L432 remains a finite-prefix theorem.
GAP: In a later research turn establish each fixed-j coefficient with the complete physical/tail errors, prove the candidate sequence summable and justify any valuation/harmonic rearrangement, then determine the whole-circle density sign with exact analytic bounds. These are unproved specialization obligations, not missing primary-source hypotheses.
REASON: Essential source scope is ready for one bounded analytic sign attempt after separate supervisor approval; import the general theorems and derive only the arithmetic specialization. No new coefficients, convergence result, generating function or sign is derived in this literature turn.
LITERATURE_REASON: Changed scope from a finite audited prefix to an infinite-sequence analytic generating-density test; the essential analytic and Fourier-uniqueness coverage was missing at turn start and is supplied by this review.
SCOPE: One prime, all separately fixed integer harmonics before the height limit, symmetric cosine-moment compatibility only; no growing-frequency uniformity, new law or actual conditional distribution.
COVERED_TARGET: Establish the full fixed log-2 cubic coefficient sequence from L432's valuation template, justify its circle-density generating function, and decide its sign analytically without increasing the Toeplitz cutoff.

The main gap is global mixed positivity. The proposed intermediate
target is an exact analytic decision about whether this single-prime
cubic moment sequence can be represented by a positive measure. Its
plausible downstream use is to decide whether the entire single-prime
cosine family can obstruct a nonnegative intermediate mass, instead
of collecting additional compatible finite prefixes. Even a positive
measure would not give an actual critical-function law, preserve other
constraints automatically, or resolve clipping or a regulator margin.

The new idea to assess is a generating function from the valuation
weights already used in L432, followed by an analytic sign test over
the whole circle. No such function or sign is asserted here. The
canonical result proves only the saved finite range; extension to
each fixed j, absolute summability of the normalized sequence, and any
exchange of harmonic and valuation sums require justified coverage and
then proof. Constants depending on j are not uniform growing-frequency
estimates. A source proving general Herglotz equivalence alone cannot
settle the arithmetic sign.

Continuation test: approve only a concrete analytic density/sign target
with sufficient primary coverage and a discriminating sign criterion.
If the needed representation or analytic sign mechanism is not supported,
record that obstruction and select independent work; do not resume the
finite-minor cutoff search. A negative density region, if rigorously
derived under valid convergence hypotheses, would obstruct a positive
measure; a nonnegative density would close only this moment-compatibility
question and stop its use as a single-prime obstruction. These are
prospective decision tests, not established conclusions.

Essential local inputs are L406--L409 for physical and rational-frequency
interfaces, L430 for fixed-character full tails and signed bulk,
L431 for the valuation factorization, and audited L432 for the finite
prefix. L421/L429 matter only for the existing high/bulk interpretation.
L427's fixed-mixture, L428's uniformly bounded bulk and L430's unchanged-law
stops remain valid; L431 already repairs the first-harmonic mismatch.
The harmonic-4 search and C426c/core-tail route remain parked. No law
redesign is authorized by this proposed source review. Actual/global
realization, actual clipping, capped nondegeneracy, L413's full-error
regulator margin and global mixed positivity remain unproved.

The preceding proposal records the scope left unapproved in step 225.
The completed review below supersedes its pending source-coverage
language; all mathematical obligations remain for a separate turn.

## Completed source comparison — 2026-10-18, step 226

Outcome EXPLORATION, LITERATURE / NOVELTY_UNCHECKED /
literature_comparison. This adds source-scope coverage and a concrete
test, not a mathematical result or progress beyond the sources checked.
No lemma, mathematical script, PROOF.md or DAG.md is changed.

### Discovery, duplicates and retained failures

Local searches in the specific October-17--18 literature, failures and
prime-power histories used generating function/density, summability,
Herglotz, Wiener algebra and harmonic terms. Read L431's prime-2
reduction and L432 through its analytic transfer, valuation and moment
sections; reuse its separately audited finite scope. Read the step-222
attempt and step-225 decision, the step-221 assessment and the
step-213 fixed-rational comparison. No earlier completed full-density
calculation was located in these paths. No sibling notebook is used.

External queries included `absolutely summable positive definite
sequence Fourier series nonnegative density Herglotz theorem`,
`"1161" "1786" "Toeplitz"`, `"valuation" "gcd" "cubic" "zeta"
"Fourier"`, and `"A_u" "gcd" "Toeplitz"`. Searches for rational
nonnegative Fourier symbols and absolute Fourier series located
general tools, not a theorem deciding this physical cubic sequence.
Unrelated hits and search snippets are not imported. This bounded
search establishes no originality or global absence claim.

The step-221 comparison and the canonical L427 failure record preserve
the unchanged-mixture stop. L428's bounded-bulk obstruction and L430's
unchanged-law mismatch do not forbid a different nonnegative
intermediate mass; L431 already repairs the first harmonic. L432's
positive finite section neither proves nor obstructs the full sequence.
No further finite section, core/tail calculation or law redesign is
authorized by this assessment.

### Primary theorems to import

J. W. Helton and M. Putinar, *Positive Polynomials in Scalar and Matrix
Variables, the Spectral Theorem, and Optimization* (2007),
[section 3.1, Theorem 3.3 and proof, pp. 245--246](https://mathweb.ucsd.edu/~toal/READ07/hpSurvey07.pdf#page=17).
Read all four clauses and the proof. For c_0>0 and conjugate symmetry,
positive-measure representability and positivity of every Toeplitz
section are equivalent to an analytic function with positive real part
in the disk and expansion c_0+2 sum_(k>=1)c_(-k)z^k. Uniqueness uses
compactness and Stone--Weierstrass; the analytic correspondence invokes
their Riesz--Herglotz Theorem 2.3. Import this equivalence, not a new
general proof. Its disk condition supplies no arithmetic sign and no
boundary regularity without additional convergence.

K. Zhou and M. Vali Siadat, *Notes on Harmonic Analysis Part II: the
Fourier Series*, [arXiv:2206.05105v1, 8 June 2022, Theorem 3.5,
p. 14](https://arxiv.org/html/2206.05105v1#S3), with
[PDF pagination](https://arxiv.org/pdf/2206.05105v1#page=14).
Read the statement and full convolution proof: a finite complex Borel
measure with all Fourier--Stieltjes coefficients zero is zero. Finiteness
is explicit in the proof's total-variation bound and must be retained.
Section 7's paragraph beginning `Define A` also records absolute
Fourier convergence implying uniform convergence; use the named
Weierstrass M-test for an explicitly proved coefficient majorant.
Import uniqueness to identify a prospective density with any finite
representing measure. Its negative Fourier convention is harmless for
the real symmetric sequence, but normalization remains necessary.

The Loyola-hosted copy and two Katznelson PDF locations failed to open;
Wilf's author-hosted PDF returned 403. These are unused leads, not
source evidence or essential blockers: the accessible arXiv text gives
the needed uniqueness proof, Helton--Putinar gives the analytic
criterion, and only elementary geometric resummation is proposed below.
The arXiv PDF screenshot timed out; its readable HTML proof, not that
screenshot, is the evidence. No inaccessible theorem is assumed.

### Exact mathematical obligations approved for a later attempt

Use the candidate coefficient expression already displayed in L432
(2), with its B_j valuation template (10)--(12), now as a target for
every separately fixed integer j>=0. Those expressions are not
established actual coefficients beyond j=4 by this review. Reuse the
step-213/221 assessments of Milinovich--Ng Lemma 6.1, Gonek Lemma 2,
Fazzari (3.5), and the DLMF Hurwitz poles. Their hypotheses permit each
positive fixed rational 2^(+/-j)mn/k; no new uniform-in-j theorem is
being imported. The later proof must retain both sharp endpoints,
every denominator-2^j zero-carrier resonance, complete response sums
and L406's absolute physical replacement. Take H first at fixed j
and fixed head, then remove the head; do not sum physical asymptotics
over infinitely many j or interchange that series with H's limit.

After identifying the candidate coefficients c_j=g_j/beta, set
c_(-j)=c_j. The proposed objects to justify are

    F(z)=1+2 sum_(j>=1)c_j z^j,
    w(theta)=1+2 sum_(j>=1)c_j cos(j theta).

No convergence, formula or sign for these objects is asserted here.
Prove an absolute harmonic majorant directly from the valuation sums;
any exchange with those sums needs a joint absolute majorant, or a
clearly stated nonnegative Tonelli step before complex summation.
Polynomial/geometric resummation is justified to avoid an infinite
list of arithmetic evaluations, not to reprove a general moment
theorem. Verify any rational expression on its convergence domain,
including transition indices; reproduce c_0 and the audited prefix
as checks, not as proof of the infinite identity.

For the prospective specialization use normalized Haar measure
dtheta/(2pi), mass one and a real even density. Reflection of an
arbitrary measure preserves cosine moments, so no actual sine-weighted
limit or evenness of the physical distribution is assumed. Once
absolute convergence is proved, justify termwise integration and
apply the cited finite-measure uniqueness theorem. The required sign
test is the entire circle, including possible zeros and endpoints.
If rational resummation succeeds, proving the denominator has no
circle zero and clearing its positive modulus square reduces the
remaining question to a finite real polynomial sign test on
cos(theta) in [-1,1]. This is a proposed method, not a derived numerator,
degree, denominator or sign. A sampled plot or truncated Fourier
polynomial does not meet it.

A proved negative region would obstruct the positive intermediate-mass
mechanism with L421's unchanged high and L430's lower-order complete
signed bulk. A proved nonnegative density would settle only this
single-prime cosine compatibility question and end its use as that
obstruction. If the analytic identity or sign cannot be controlled,
record the exact failed bound and reassess the mechanism; do not
increase the Toeplitz cutoff. No new law construction follows either
way. Full matching Mathlib coverage remains unchecked. Essential
inputs and all independent unresolved assumptions are those recorded
above; mathematical exploration usage remains 0 of 3.
