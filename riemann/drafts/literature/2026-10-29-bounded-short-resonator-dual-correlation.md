# Bounded short-resonator correlation: completed source comparison

TARGET: Assess whether the bounded weight phi_{A,T}=|F_T|^6/((log T)^A+|F_T|^6), with L481's F_T and some fixed A>=0, can certify a positive T(log T)^3 correlation with the complete L477 residual along an unbounded sequence.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded searches for bounded/nonlinear resonator correlations, rational weights and finite-height Dirichlet-polynomial distributions; inspected the primary statements and proof cases below. Reused the L481 comparison, Hardy-space review, interpolation stop and fixed-witness clipped-source mismatch; no matching signed saturation theorem was located and no novelty is inferred.
SOURCE_EVIDENCE: Heap--Soundararajan 2007.13154v1 Section 5 Lemmas 1--2/(12)--(16); Heap--Radziwill--Soundararajan 1901.08423v1 Theorem 1, Propositions 1--3 and good/exceptional-set proof; Trefethen Chapter 8 Theorems 8.1--8.2; Shadrin Section 1.1/(1.1); Kraus--Vassilevski--Zikatanov 1002.1859v3 Theorem 2.1, degree-zero case and Appendix A. Exact URLs, versions and scopes are below; Gonek's scalar input is reused through audited L481 only.
COMPARISON: Prime-block exponential approximation controls absolute zeta moments with carefully limited product lengths, not the proposed complete signed saturation. Analytic approximation supplies error bounds only after specifying an interval and analytic neighborhood. Markov's classical derivative inequality supplies a concrete test of a global-range polynomial implementation. Neither source gives the desired correlation, a negligible weighted tail or an actual-height Haar transfer.
GAP: No fixed A, positive correlation constant, full signed approximation error or large-value remainder has been established. The separate continuation tests only uniform polynomial approximation on the deterministic full amplitude envelope against an explicitly stated length budget; its feasibility is unresolved and it does not authorize a direct lower-bound proof from the moment citations.
REASON: Source discovery for the exact target is complete for this bounded step. Park direct saturation evaluation from the inspected moment theorems; instead prepare one source-supported deterministic approximation feasibility test, separately assessed below. This is EXPLORATION, not a negative theorem or proof of the correlation. No lemma or mathematical script was written.
LITERATURE_REASON: Essential finite-height nonlinear or controlled-approximation coverage was missing at invocation start; the saved target was REVIEW_REQUIRED. The inspected approximation/exceptional-set passages address that gap and do not repeat literature solely for scheduling balance.
SCOPE: L477's exact R_T and theta on [T,2T]; L481's F_T=sum_{n<=floor(T^(1/24))} n^(-1/2-it); fixed real A>=0; no RH, independent phases, conjectural moment, Haar replacement or weighted transfer of an unbounded test through L477's error.

## Original nomination

The following paragraphs preserve the nomination's original unread-source
status. The completed review below supersedes that status.

The main gap remains actual-Xi all-degree mixed positivity. The intermediate
target proposed for source review is a bounded dual test of the first-sign
square defect, not a new sign theorem. A positive correlation at the stated
scale would lower-bound the actual L1 residual and, using L477, reject this
particular square as a little-o approximation. It would not supply the
negative-mass saving, other degrees, individual-height signs or RH.

The new input motivating this nomination is the now audited complete
signed decomposition in L481, not merely a large moment of one component.
Its positive correlation uses an unbounded weight; its Holder consequence
stops the exact second/fourth-moment certificate. This proposal replaces
that weight by an explicitly bounded rational function. No inference from
the unbounded correlation to the bounded one is authorized: signed mass
may change under saturation, and a large-value tail cannot be discarded.

Three options were compared only for routing. The unchanged moment
interpolation is now stopped by L481. Automatic multiplicative Hardy-space
transfer retains the finite-height and chirped-cancellation mismatch in
`2026-10-29-fixed-square-residual-hardy-l1-coverage.md`. The bounded actual-time
test above is independently specified, but has no source coverage yet.
It is selected for one source review, not approved as a creative proof.
The absence of a covered sign-sensitive joint input still blocks such a
proof nomination; this source review must determine whether one exists.

L472 and L473 are used here only as contrasts: their abstract moment laws
do not evaluate an actual-height nonlinear statistic. The stopped fixed
prime witness in `2026-10-19-finite-witness-oriented-clipped-mean.md` concerned
a different sign-clipped jet observable. Its obstruction warns against
repeating ordinary moment citations as if they controlled a clipped mean.
The present proposal uses a growing short polynomial and retains the
entire L477 residual. This difference defines a test, not a proof that the
earlier source limitation has been overcome.

Continue only if an inspected primary result, or a source-supported
approximation with explicit degree, product length and signed-tail error
obligations, yields a concrete test at c T(log T)^3 for fixed c>0 on an
unbounded sequence. Preserve the exact numerator, denominator and both
phases throughout. If the available result concerns only Haar averages,
unweighted finite moments or a scalar large-value tail, record that exact
mismatch and park this certificate without asserting its inequality false.
Do not spend a dependent mathematical turn on missing coverage. No new
lemma, expansion or script has been derived for this continuation.

## Completed source review, 29 October 2026

The main gap, intermediate target and downstream use remain those in the
nomination: all-degree actual-Xi positivity; the exact bounded correlation;
and a possible obstruction to this particular square's little-o defect.
The exact TARGET has not been replaced by a scalar or independent-phase
statistic. No mathematical specialization is performed in this source turn.

### Primary theorem and proof-case comparison

**Heap--Soundararajan, _Lower bounds for moments of zeta and L-functions
revisited_, arXiv:2007.13154v1, 26 July 2020.**
[Primary version](https://arxiv.org/pdf/2007.13154v1).
Theorem 1, p. 1, concerns absolute zeta moments, uniformly for
(log T)^(-1/2)<=k<=(log T)^(1/2-delta), fixed delta>0.
Read Section 2's prime-block/truncated-exponential setup and Section 5,
pp. 8--11: Lemma 1's small/large block cases (12)--(13), Lemma 2's
nonnegative exceptional majorant and finite mean square (14), and (16).
The last factorization requires pairwise coprime block supports and a
bound on every product length. Those hypotheses are not supplied for
the present rational weight. Its exceptional majorant does not estimate
the signed residual-weighted saturation error. Retain (14) as the known
finite-polynomial interface already used in L481; do not import the
absolute-moment conclusion for R_T or infer saturation from L481's S(T).

**Heap--Radziwill--Soundararajan, _Sharp upper bounds for fractional
moments of the Riemann zeta function_, arXiv:1901.08423v1,
24 January 2019.** [Primary version](https://arxiv.org/pdf/1901.08423v1).
Theorem 1, pp. 1--2, gives I_k(T)<<T(log T)^(k^2) for 0<=k<=2,
T>=10. Read Section 2's definitions and Propositions 1--3, Section 3's
Lemma 1 and both cases, and Section 4's length check. Lemma 1 assumes
real |alpha|<=2 and |P_j(s)|<=50P_j. The exceptional case takes the
first bad prime block and retains a high-power penalty; products are
kept within T^(1/10). These are nonnegative upper comparisons with
twisted absolute fourth moments. They supply neither a two-sided
approximation to the specified saturation nor its correlation with
U+Re(exp(2i theta)V). Small exceptional-set measure alone is not a
bound for its R_T-weighted error. Their exact cutoffs and penalties
cannot be transferred to the all-integer F_T by terminology alone.

**Trefethen, _Approximation Theory and Approximation Practice_,
Chapter 8, Theorems 8.1--8.2.**
[Author text in the ETH mirror, PDF pp. 56--57](https://people.math.ethz.ch/~hiptmair/Seminars/RAP_22/TRE13.pdf#page=56).
The accessible chapter-format text has no edition/date in the inspected
chapter header; theorem numbers and PDF pages identify the text actually
read, rather than claiming a checked 2019 edition. For f analytic on
[-1,1], continuable and bounded by B in the open Bernstein ellipse
E_rho, rho>1, degree-d projection/interpolation errors are at most
2B rho^(-d)/(rho-1) and 4B rho^(-d)/(rho-1), respectively.
Read the coefficient contour argument, its open-annulus limiting case
and Theorem 8.2's proof. This gives quantitative approximation with
specified hypotheses; no uniform rho, B or usable degree for our
T-dependent amplitude interval is supplied. An approximation theorem
alone does not control either signed finite-height correlation.

**Classical Markov inequality.**
[Shadrin, _Twelve Proofs of the Markov Inequality_, author-hosted
undated draft, Section 1.1/(1.1), PDF pp. 1--2](https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf#page=1).
Read the complete statement and norm/degree definitions: every real
polynomial p of degree at most d satisfies
||p'||_[-1,1]<=d^2 ||p||_[-1,1]. The theorem includes endpoints and
does not assume coefficient positivity. Import this standard named
inequality without reproof. It allows a deterministic degree test for
a uniformly bounded approximation across a long interval. No degree
bound specialized to our weight is derived in this literature turn.

**Stronger known reciprocal approximation.** A subsequent exact search
located [Kraus--Vassilevski--Zikatanov v3, Theorem 2.1, p. 3](https://arxiv.org/pdf/1002.1859v3#page=3),
23 May 2012. For a>1 and integer m>=1, the best uniform degree-m
error for 1/(t+a) on [-1,1] is delta^m/(a^2-1), with
delta=a-sqrt(a^2-1). Read Section 2's interval transformations,
the degree-zero case on p. 4 and Appendix A's reduction to Meinardus's
classical formula. This is more directly relevant than a generic
analytic upper bound. Its saturation scaling and compatibility with
the product-length budget are left to a separate mathematical turn;
the approximation theorem should be imported rather than rediscovered.
Neither it nor Markov evaluates a residual-weighted tail.

### Search and local failure comparison

Queries included `Dirichlet polynomial bounded rational weight nonlinear
correlation short resonator moments`, `zeta function truncated resonator
bounded weight signed moment saturation`, `Dirichlet polynomials bounded
test functions`, `Dirichlet polynomial saturation`, `zeta rational weight
moments`, and the exact approximation theorem names. Several hits
concerned unrelated Dirichlet processes or only abstract/random norms;
they were excluded. No search snippet or abstract is theorem coverage.

The invocation-start assessment of L481's fourth-moment construction
was reused, including its primary Gonek scope. Narrow reads of L481
Sections 1--2, 4 and 6 retain finite lengths, coefficient masses and
both summed endpoint errors. L477 (1)--(5) retains both phases and its
unweighted L1 transfer. The Hardy-space and fixed-witness source
comparisons remain obstructions to automatic transfer, not bans on a
new finite calculation. A targeted Markov/global-range/uniform-polynomial
search in the residual/resonator assessments and residual ATTEMPTS
found no completed duplicate of the proposed implementation test.
L472/L473 remain contrasts only; no abstract law is identified with zeta.

### Decision and concrete continuation

No inspected theorem establishes the exact correlation or a full
signed-tail approximation at c T(log T)^3. Do not invoke a mathematical
attempt that simply saturates the known unbounded correlation or drops
the chirped part. Park that direct import route. This is a bounded
search outcome, not evidence that the target inequality is false.

The approximation sources support a smaller, independently testable
obligation: can a real polynomial uniformly approximate the stated
rational function over the entire deterministic amplitude envelope
while satisfying the finite-product length budget? A global uniform
test has no exceptional set to discard. Its exact proposed tolerance,
interval and budget are specified, without a feasibility conclusion,
in [the separate assessment](2026-10-29-saturation-global-polynomial-feasibility.md).
This is a necessary implementation check only. Success would still
require complete signed polynomial correlations, coefficient-dependent
errors and an error margin using L477's absolute bound; failure would
stop that global-range implementation, leaving measured-range and
direct nonlinear methods unresolved. The new assessment needs separate
next-turn approval before research. No central creative sign mechanism
is justified merely by these approximation results.

Mathlib: full matching saturation, finite-height correlation and
specialized approximation coverage were not checked. Unknown coverage
is not absence. The cited results are not claimed as new discoveries.
