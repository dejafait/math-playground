# Exact bulk square — completed deterministic source comparison

TARGET: Assess whether a deterministic short-shift reconstruction of B_n^2 using H=floor(sqrt(X)) on dyadic blocks can retain all long-shift, cross-block and continuum terms at subexponential cost.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step306 searched Gallagher/Fejer short-window inequalities, finite-sequence van der Corput correlation reconstruction, finite-measure variants, short-lag ambiguity and exact Laguerre combinations; inspected the primary contracts below and reused review304 and named stops. No matching exact centered reconstruction was identified; failed searches establish neither impossibility nor novelty.
SOURCE_EVIDENCE: Hugh L. Montgomery, Harmonic Analysis as found in Analytic Number Theory (2001), printed pp276–277/PDF6–7, full finite-sequence shift/Cauchy proof, https://www.nato-us.org/analysis2000/papers/montgomery.pdf ; Coppola–Laporta arXiv1411.1739v1 (21 October2014), unnumbered Lemma (**) on p2, Cesaro case p3 and its finite-window proof p5, https://arxiv.org/pdf/1411.1739v1 ; Tao Notes5 Proposition7 and proof, https://terrytao.wordpress.com/2015/02/07/254a-notes-5-bounding-exponential-sums-and-the-zeta-function/ . Reuse review304 for MRT and review241 for the exact observable.
COMPARISON: The finite-sequence source gives a costed upper bound via signed local energy, not equality with the global square. The weighted Gallagher source controls an L2 frequency integral, not its value at frequency zero or the continuum compensator. Neither supplies the required every-epsilon B_n bound. A separate exact-cell compensated majorant test is now source-covered, with no result asserted.
GAP: Exact long-pair reconstruction at subexponential cost is not supplied by the inspected theorems. A sufficient inequality remains possible, but its actual centered weighted energy, block-combination costs and degree uniformity must be established; no small residual or arithmetic saving is known.
REASON: New theorem-level evidence parks direct equality/reconstruction import while distinguishing a standard finite-window majorization test. Its separate assessment records the needed specialization rather than assuming the local energy is small. No mathematical identity, counterexample or new bound is derived in this literature-only step.
LITERATURE_REASON: The startup REVIEW_REQUIRED target changed from arithmetic correlation import to deterministic reconstruction; the essential finite-window and weighted Gallagher contracts had not been assessed. This turn completes that missing coverage without reopening the completed arithmetic review.
SCOPE: Completed source-only comparison for the stated exact K_n and B_n, dyadic terminal pieces and H=floor(sqrt(X)). Arbitrary finite complex sequences in Montgomery; absolutely convergent discrete-frequency sums in Coppola–Laporta. No automatic extension to signed measures, exact cell specialization, Laguerre rate calculation, lemma or mathematical script.

The original nomination below is preserved. The completed comparison at the end supersedes its missing-source language.

## Proposed question and relevance

Retain exactly review241's

    K_n(u)=(n-1)^(-1)*sum_(k=2)^n L_(k-1)^(1)(u),
    B_n=sum_(exp(n)<m<=exp(2n)) Lambda(m)*K_n(log m)/m
                                  -integral_n^(2n) K_n(u)du.

The source review must preserve the full upper endpoint and all prime
powers. The sufficient bulk threshold is B_n^2<=D_epsilon*exp(epsilon*n)
for every epsilon>0, with D_epsilon finite and independent of n.
Even a successful bulk reconstruction would leave L984(H)'s lower
and upper logarithmic complements, arithmetic estimates, and the
L030–L032/C032a and L966/L968 main gaps unresolved.

The candidate mechanism is to retain signed short-shift quadratic
information rather than individually bound weighted prime errors.
The first question is deterministic: what information is lost when
the global square is localized at the proposed H, and can the exact
Laguerre kernel suppress that loss? No localization identity,
positive majorant, stochastic model or small remainder is asserted.
Dyadic terminal pieces, pairs between pieces, the diagonal and the
prime-integral/integral-integral terms must remain explicit.

Retrieve primary hypotheses for finite-window/positive-kernel or
quadratic reconstruction results, checking stronger statements and
counterexamples. Specify the class of sequences or signed measures
to which any deterministic assertion would apply; do not silently
use an arbitrary-sequence theorem with arithmetic hypotheses, or
the reverse. Translate weights or variable scales only in a later
approved mathematical step. The current nomination is a question,
not an unproved identity to be promoted to an input.

A discriminating later test would either provide one exact
reconstruction with every residual and a credible route to the
stated cost, or exhibit a counterexample within its explicitly stated
class showing that the selected short-shift data leave an uncontrolled
global term. A bound for arbitrary sequences need not be possible;
failure there would only limit that contract, not actual primes.
If only the original B_n^2 survives as an unpaid remainder, abandon
this reconstruction and select a different mechanism. Do not replace
the task with an automatic averaging or absolute-norm calculation.

The next review may nominate at most one bounded mathematical test
after source coverage. A genuinely new signed kernel mechanism at
the central arithmetic gap could justify proof_attempt/creative,
with the reconstruction obstruction, a bounded test and decisive
evidence named in NEXT_ESCALATION. None is justified yet: the exact
kernel bridge and its source coverage are missing. Existing source
coverage is to be reused, not browsed again without changed scope.

Inputs and contrasts: L984(H); review241's B_n; L981/L982 full-endpoint
normalization; completed review304; review231 variance; review243
centered Vaughan; stops233/235/243/302; review200 only for the distinct
complex-zero Fejer obstruction. C999a supplies no arithmetic premise.
Signed covariance, exceptional-set costs, n-uniform weights, both
complementary ranges and infinite-zero/regulator control remain open.
Mathlib matching coverage is unchecked and unknown. No cross-notebook
input, new result, exploration-counter renewal or creative approval.

## Completed source comparison — step306, 10 November 2026

The main gap remains actual-Xi positivity in L030–L032/C032a and
L966/L968 signed forcing; L984(H) is unpaid. The intermediate question
is whether short-shift information can retain the complete compensated
bulk observable. Its sufficient downstream threshold remains
B_n^2<=D_epsilon exp(epsilon n), every epsilon>0, uniformly in integer
n>=2. Both complementary logarithmic ranges remain independent gaps.

### Primary contracts actually inspected

Hugh L. Montgomery, *Harmonic Analysis as found in Analytic Number
Theory*, in J. S. Byrnes (ed.), *Twentieth Century Harmonic Analysis —
A Celebration*, Kluwer (2001), pp271–293, specifically the unnumbered
van der Corput argument on [pp276–277/PDF6–7](https://www.nato-us.org/analysis2000/papers/montgomery.pdf#page=6).
For a complex sequence y supported on {1,...,N}, zero elsewhere,
and integer H>=1, its proof retains the signed intermediate bound

    |sum_j y_j|^2 <= (N+H)/(H+1) *
      [sum_j |y_j|^2 + 2 Re sum_(h=1)^H
          (1-h/(H+1))*sum_j y_(j+h)*conj(y_j)].

Read the complete zero-extension, shift-averaging, Cauchy and
correlation-counting argument, including the subsequent absolute-value
version. There is no arithmetic assumption or bounded-coefficient
hypothesis. This is a known upper bound, not reconstruction equality;
its displayed support/window cost must be retained. No reproof or
specialization is performed here. The [author's publication list](https://public.websites.umich.edu/~hlm/epubs.html)
and [publisher record](https://link.springer.com/book/10.1007/978-94-010-0662-0)
identify the version. PDF screenshots did not supply usable evidence;
the complete relevant extracted proof was read instead.

Giovanni Coppola and Maurizio Laporta, *A generalization of Gallagher's
lemma for exponential sums*, [arXiv1411.1739v1](https://arxiv.org/pdf/1411.1739v1),
21 October2014, unnumbered Lemma (**), p2, Cesaro specialization p3,
finite-window proof p5. For absolutely convergent S(t)=sum_nu s(nu)e(nu t),
strictly increasing real frequencies nu, delta,T>0 and a locally
integrable w, let w_delta=w on [-delta,delta] and zero otherwise.
The statement is

    m_(delta,T)*integral_(-T)^T |S(t)|^2 dt
      <= integral_R |sum_nu s(nu)w_delta(x-nu)|^2 dx,
    m_(delta,T)=min_(|t|<=T) |Fourier(w_delta)(t)|^2.

Read the infinite-right-side case and the Fourier/Plancherel proof.
A useful division requires m_(delta,T)>0; its odd-weight zero case
is explicit. The Cesaro choice has delta*T in (0,1). Only finite sums
and bounded compact windows are needed for comparison here. The source
controls a frequency integral, not point evaluation. No finite-measure
extension or prime-continuum compensation is imported. The general
untruncated-window extension and later arithmetic theorems are not inputs.

Tao's [Notes5 Proposition7 and its full proof](https://terrytao.wordpress.com/2015/02/07/254a-notes-5-bounding-exponential-sums-and-the-zeta-function/),
7 February2015, concern e(f(j)), real f on an interval of length N,
N>=H>=1. They provide a useful cross-check of the diagonal and
intersection-of-shifted-support cases. They are not an arbitrary-weight
prime theorem. Montgomery is the precise arbitrary-complex-sequence
input for the next test. Reuse completed review304 for MRT
Proposition3.1/Corollary3.2: its major/minor-arc premises remain premises.

### Exact comparison and decision

The first source changes the feasibility question: a sufficient global
upper bound need not reconstruct each long pair separately. Its proof
already supplies a costed inequality. This does not certify that its
right-hand side, or its specialization to B_n, has subexponential size.
The second source cannot by itself turn a Fourier mean square into
B_n^2, nor does it identify the compensator with a discrete main term.
These are theorem-scope findings, not new mathematical obstructions.

| Obligation | Status after review |
| --- | --- |
| Long shifts within one block | A standard costed majorant is available for finite sequences; equality or a small discarded-pair remainder is not supplied. |
| Cross-block pairs | Neither cited statement reconstructs them for B_n. Any later block-combination inequality must keep its entire cost. |
| Prime-integral and integral-integral terms | Not inputs to the discrete source theorem. Exact cellwise compensation is a proposed specialization to prove later; Lambda-1 at integer points alone is not justified. |
| Sharp terminal pieces and the full upper endpoint | Must be represented exactly in the finite sequence and integral accounting. No smoothing error is paid here. |
| Diagonal and exceptional shifts | Remain in the local energy. Review304 supplies no permission to discard them or assign a small signed contribution. |
| Degree-uniform weighted centered energy | Unpaid. No source estimate meets the every-epsilon bulk threshold as stated. |

Park direct exact-reconstruction import from these sources. Do not claim
that arbitrary-sequence reconstruction is impossible: no counterexample
has been proved in this turn. Do not claim that long shifts must be
estimated individually: Montgomery supplies a sufficient alternative.
The changed, bounded continuation tests that alternative with exact
compensation and a full cost comparison, rather than repeating the
uncentered absolute-norm calculation or assuming an energy estimate.

The named stop233 actual-prime lobe counterexample, stop235 automatic
averaging failure, stop243 uncentered derivative loss, stop302 formal
coefficient/arithmetic-norm mismatch and stop305 arithmetic direct-import
limit were checked and preserved. Review200's complex-zero Fejer failure
concerns another class; no complex zero law is used in the finite-sequence
source. The exact-term searches found no matching reconstruction theorem;
this is not evidence of originality. Nonessential finite-measure and
short-lag ambiguity search leads were not imported or inspected as theorems.

Only the next finite-window applicability/cost test is justified. It is
ordinary specialization, not a protected creative mechanism: there is no
source-covered new signed arithmetic cancellation input to justify that
label. Its newly saved assessment requires separate approval next turn.
No new identity, bound, lemma, mathematical script, DAG edge or PROOF.md
change was made. Full matching Mathlib coverage is unchecked and unknown.
