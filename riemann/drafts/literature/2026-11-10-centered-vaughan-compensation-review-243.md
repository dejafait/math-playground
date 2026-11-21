# Center before absolute Vaughan estimates — completed source review

TARGET: Assess a signed centered Vaughan decomposition for B_n, seeking a residual correlation estimate that avoids L985's absolute-value loss.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step244 searched centered Vaughan identities, main-term Type II estimates, smooth centered Mangoldt sums and exact Laguerre combinations; reused review240/review231 and the step224/233/235/240/243 stops. No inspected theorem supplies the required signed residual; no novelty or impossibility inference.
SOURCE_EVIDENCE: Inspected Tao arXiv1201.6656v4 (3 July2012), Lemma4.11/(4.18)-(4.19), printed pp23-24, including the pre-inequality identity and coefficient alignment; Lemma4.3/(4.4), pp16-17; Proposition7.2/(7.2)-(7.4), pp34-36, including both low-zero and high-zero proof cases. Reuse review240 for Theorem1.3 and its rational-separation case. Exact contracts below.
COMPARISON: The source's subtraction of log(w)/2 improves a coefficient sup bound by a factor two; it does not assert a centered correlation estimate. The Type I c_d depend on F and arise after absolute values. Genuine centered major-arc estimates retain a linear-in-x term at fixed verified height and have smooth nonnegative-weight hypotheses absent here. Neither source pays L985's required gain.
GAP: The signed arithmetic residual for actual Lambda and the continuum compensator is still unpaid. No applicable estimate removes the fixed positive exponential rate in L985; both logarithmic complements also remain open.
REASON: New theorem-level comparison parks this refinement: coefficient recentering is already present, whereas continuum compensation requires additional arithmetic input. EXPLORE records bounded coverage, not permission to repeat this stopped payment attempt. A separate proper-prime-power target is nominated below, without deriving it.
LITERATURE_REASON: The start-of-turn REVIEW_REQUIRED target changed from absolute derivative bounds to signed compensation; essential pre-inequality and centered main-term contracts had not been compared.

## Exact observable, bounded question and relevance

Use actual Lambda, integers n>=2, all prime powers and full right
endpoints, with K_n and B_n exactly as in L985. The desired upper
bound remains B_n<=C_epsilon*exp(epsilon*n) for every epsilon>0
and all n>=2. The exact degree identity includes -1/(n-1).
No RH, simplicity, new zero-free region or cross-notebook input.

L981/L982 fix the remote-tail/normalization interface, and L984
provides only conditional sufficiency for the entire common-cutoff
average. The low and high logarithmic complements are independent
gaps; even a successful B_n estimate would not pay them. L985's
phase formulas and loss comparison are a completed but unaudited
local specialization, not a centered residual theorem.

The source review should first check known centered versions and
obstructions, then compare exact signed identities and the strongest
applicable arithmetic estimates. Retrieve primary hypotheses and
load-bearing cases before larger extracts. Inspect only the named
local records as needed; do not reopen parked inaccessible sources
without a new essential reason. Keep the proposed calculation as a
target while assessing it. No new identity or estimate is derived
in this nomination.

Continue only if a concrete independently testable signed residual
estimate or informative obstruction can be specified. If the source
comparison yields only a decomposition whose residual is the original
unpaid discrepancy, park this refinement and select a different
mechanism; do not repeat the uncentered derivative test, criterion
approval, automatic-average argument, or universal lobe rule.

A later creative attempt would require an actual proposed gain
surviving compensation, a bounded discriminating test, and separate
coverage approval. None is justified yet. Full matching Mathlib
coverage for this changed target is unchecked and unknown.

## Completed comparison — step244, 10 November2026

The preceding nomination is historical; this section supersedes its
missing-coverage language. This turn is literature-only: no new
identity, bound, lemma or mathematical script is derived. L985 was
read for the required gain and its stopping scope; L981/L982 were
read only for definitions and cutoff normalization.

### Signed identity versus a centered bound

T. Tao, *Every odd number greater than1 is the sum of at most five
primes*, [arXiv1201.6656v4](https://arxiv.org/pdf/1201.6656v4#page=23),
Lemma4.11, printed pp23-24, assumes U,V>1 and arbitrary complex F
supported strictly in (V,UV^2). Its proof's (4.18) is the exact
Dirichlet-convolution identity

    Lambda = mu_(<=U)*log - mu_(<=U)*Lambda_(<=V)*1
                       +mu_(>U)*Lambda_(>V)*1+Lambda_(<=V).

Here * is Dirichlet convolution and 1 is the constant arithmetic
function. This is an imported identity, not a new centered identity
for B_n. The short final term vanishes only under the support condition.
The proof moves the log(w)/2 portion of the bilinear coefficient
into Type I using w>V and dw<UV^2. Equation(4.19) bounds
g(w)=sum_(b|w,b>V)Lambda(b)-log(w)/2 in absolute value by log(w)/2.
It asserts no zero mean or signed correlation bound. The coefficients
c_d in the resulting inequality depend on F: the proof aligns complex
inner sums after taking absolute values. They are not fixed signed
arithmetic coefficients from (4.18). This source distinction rules out
using that inequality itself as the proposed signed decomposition.

### Genuine continuum compensation has a separate cost

The same primary source, Proposition7.2, printed pp34-36,
assumes smooth nonnegative eta supported in [c,c'], c>0,
cx>10^3 and |alpha|<=T0/(4*pi*c'*x), with T0=3.29*10^9 from
Theorem1.5. Put S=sum_m Lambda(m)*eta(m/x)*exp(2*pi*i*alpha*m).
It bounds |S-x*integral_R eta(y)*exp(2*pi*i*alpha*x*y)dy| by

    A*x*log(T0)/(3*T0)
              +2.01*c^(-1/2)*sqrt(x)*N(T0)*||eta||_1,
    A=60||eta||_1+32*c'*||eta'||_1+4*c'^2*||eta''||_1.

Here N(T0) counts zeros in 0<=Re(s)<=1, 0<=Im(s)<=T0,
with multiplicity; both conjugate halves are included in the proof.

The proof uses verified critical-line zeros up to T0; for higher zeros
it uses 0<Re(rho)<1, two integrations by parts and an absolute inverse
square zero-tail bound. These are the essential two cases, both read.
The first error term remains linear in x at fixed T0. Compare with
L985's already-recorded near-sqrt(x) saving requirement, not just a
small relative constant. Also B_n has a sign-changing polynomial and
sharp endpoints; the stated eta hypotheses do not cover it directly.
No smoothing extension or n-dependent norm bound is asserted here.
Raising T0 with n would require new verified-zero information, not a
consequence of this proposition. Lemma4.3/(4.4), printed pp16-17,
likewise has a derivative-norm error of order x/log(cx), not the
required power saving. Theorem1.3's fixed additive-frequency bounds
remain covered by review240; no logarithmic-phase transfer is imported.

Thus the sources provide exact algebra and some centered estimates,
but no adequate residual estimate for this target. This is a bounded
source exclusion, not a lower bound for B_n, a refutation of RH, or a
proof that all centered methods fail. No mathematical theorem is
added to the notebook by this source review.

### Search, reuse and continuation

Queries included `Vaughan identity centered von Mangoldt function
minus 1 bilinear sums cancellation smooth weights`, `"centered"
"Vaughan" "identity" primes`, `"Vaughan" "main term" "Type II"
"prime number theorem"`, and `"von Mangoldt" "minus" "1" "smooth"
"Mellin" prime number theorem`. Primary Tao contracts were inspected,
not inferred from search snippets. Additive-shift correlation hits
(including arXiv1707.01315) remain unread leads and are not imported.
Reuse review231's primary short-interval variance comparison: it has
averaging/covariance and coarse-term gaps, not a ready residual theorem.
Preserve the separate lobe-sign, automatic-average, criterion-only and
absolute-derivative stops. No cross-notebook input is used.

PDF screenshot tools returned no inspectable image and a direct shell
download failed DNS resolution. Text extraction supplied the complete
load-bearing statements and proof cases above; no essential source
blocker is being claimed or scheduled for retry. Full matching Mathlib
coverage is unchecked; nothing is inferred about absence.

Park this refinement unless a specific new signed arithmetic estimate
survives compensation. Creative preparation is blocked by that missing
gain. Instead nominate the independent proper-prime-power component
at the existing common cutoff, using the global DLMF18.14.8 bound.
The separate [assessment](2026-11-10-proper-prime-power-laguerre-review-244.md)
prepares one routine specialization, with approval deferred to the next
turn. It would remove one component of the actual arithmetic head;
prime terms, compensator and all signed bounds remain unpaid. This is
not a substitute name for the stopped B_n cancellation attempt.
