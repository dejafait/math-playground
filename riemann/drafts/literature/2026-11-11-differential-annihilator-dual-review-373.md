# Complete-kernel differential-annihilator dual densities — source gate

TARGET: Assess source coverage for compactly supported differential-annihilator dual densities at the complete-kernel threshold and original TV cap.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step374 checked the complete C997c/C997s kernel and stops371/372, searched the exact Laguerre/annihilator/compact-support/TV terminology and stronger exponential-polynomial and Ehrenpreis-cutoff results; inspected primary statements and relevant proof cases below. No matching normalized growing-n rate was found; this bounded search establishes no novelty.
SOURCE_EVIDENCE: Aldaz–Kounchev–Render arXiv:0805.1618v1 §1(1),(3), §2 p3 repeated-root basis; Boman Ark. Mat.5(1964) Lemma1 pp272-273, (2.1),(2.2') and proof; Melrose Chapter3 p44(1.4), p53(2.13)-(2.15); Behm–Wennman arXiv:1404.3127v2 §3.1 Lemma3.1/Proposition3.2 pp8-11. Direct URLs and qualifications below; C997c/C997s and review369's support-function assessment are reused.
COMPARISON: Finite ODE annihilation and compact-support adjoint pairing are standard. Boman supplies order-dependent cutoffs with paid finite-order derivative bounds, avoiding reliance on an unspecified fixed bump. These inputs do not estimate the complete-kernel normalized target action; finite atomic stops and exact endpoint homogeneity do not decide this different density mechanism.
GAP: Specialize the known inputs to all complete endpoint columns, then control actual L1 normalization and target action jointly at exp(-n/64). No kernel-specific operator, density, nonzero denominator, rate or obstruction is established in this literature-only step.
REASON: The essential formal and quantitative derivative background has now been inspected; the remaining ratio is the proposed research question, not an unread theorem being assumed. Nominate one bounded creative test with separate approval next turn; no more numerical iterations or literature searches are justified merely by balance targets.
SCOPE: Same integer n>=2, I=[7/4,9/4], z_star=1+i/8, gamma_j=15/8+j/(4n), j=0,...,n, complete C997c kernel and coefficient cap exp(sqrt(n)); proposed complex densities have compact support in the interior of I and are normalized by their actual L1 norm.

## Step373 nomination, preserved; not an established construction

The main gap remains L030-L032/C032a actual-Xi positivity, L966/L968
signed forcing and unpaid L984(H). A negative answer to the fixed-grid
complete-kernel threshold would rule out this particular point-bridge
budget; a positive answer could supply one resource for signed slope
selection. Neither outcome resolves the independent transfer gaps.

The candidate is to seek a constant-coefficient differential operator
P_n(partial_c) annihilating every COMPLETE band column k_n(c,gamma_j),
and a smooth complex function phi_n compactly supported in (7/4,9/4).
Its proposed test density is

    w_n(c)=P_n(-partial_c)phi_n(c)/||P_n(-partial_c)phi_n||_L1(I).

Nonzero denominator, exact annihilation, valid adjoint integration by
parts, and a quantitative target action are all requirements to check;
none is assumed proved. The operator must also retain the lower-window
term, both beta terms and K's -1. No cancellation of only a leading
asymptotic component suffices, and no division by g_n is proposed.

The discriminating quantitative target is an explicit family for which

    exp(n/64)*|integral_I w_n(c) k_n(c,z_star) dc|

is unbounded on an unbounded integer subsequence, with all band actions
zero (or, if exact cancellation fails, with their full exp(sqrt(n))
charge retained). This tests the same actual target direction as C997s.
The L1 normalization, derivative order, support boundary terms and any
target cancellation must be paid explicitly. A bare annihilator formula,
an unnormalized nonzero response, fixed-degree solvability or an
uncertified oscillatory calculation is not the desired result.

The source turn should first inspect precise primary hypotheses for
exponential-polynomial annihilators/adjoint test functions and relevant
growing-order compact-support derivative bounds. Determine whether a
known theorem covers this ratio, a specialization is justified, or the
candidate has an informative norm-cost obstruction. No source is yet
represented as supplying those estimates. A particular bump/operator
family with a proved inadequate normalized action should be abandoned
on that scope, not promoted to a universal dual impossibility. If no
concrete cost estimate can be nominated, record that limitation rather
than approving formal annihilation as a mathematical advance.

## Why this nomination follows the audit

Three possibilities were compared without a second mathematical attempt:

1. More iterations or degrees of the two existing numerical generators:
   parked by stop372; no quantitative input supports reopening.
2. Reusing centered Taylor, exact endpoint homogeneity or scalar/spectral
   damping: review369 retains their scoped stops or unpaid tails; this
   audit supplies no new estimate for them.
3. An explicit differential operator acting on a compactly supported
   density: select for source comparison because its derivative L1 cost
   and normalized target action can be tested independently of numerical
   conditioning, a Taylor coefficient rule or packet asymptotics.

This is a proposed analytic realization of exact cancellation, not a
claim that exact cancellation is new or successful. Step371's near-null
test remains negative evidence for its own equispaced atomic construction.
No stopped construction is silently restarted, and no mathematical
exploration counter is reset by this nomination. Creative work is blocked
by essential source coverage and the missing quantitative derivative-cost
mechanism; the immediate next task is literature comparison, not a proof.

Essential inputs: audited C997c(1),(4)-(6) and C997s(1) with its step373
finite audit. C997q is notation only. C997a(8), selected/both-sign
transfer, assay/reconstruction, complements/regulators, L993, L984(H),
L966/L968 forcing and actual-Xi signs remain open. No Haar, zero
simplicity or nonvanishing assumption is available. Mathlib matching
coverage is unknown. No cross-notebook theorem or RH candidate.

Step373 only nominates this target with REVIEW_REQUIRED. It performs
no new differential construction, theorem application or source approval.

## Step374 source comparison, 11 November 2026

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. The preceding
nomination describes what was missing at step373; the fields above and
this section record the completed comparison. No lemma or mathematical
script is written, and no proposed operator or response is evaluated.

### Inspected primary contracts

1. J. M. Aldaz, O. Kounchev and H. Render, *Bernstein operators for
   exponential polynomials*, arXiv:0805.1618v1, 12 May 2008,
   [primary PDF](https://arxiv.org/pdf/0805.1618v1), pp1-3, §1(1),(3)
   and §2's repeated-root paragraph. For arbitrary complex roots, the
   constant-coefficient operator product(D-lambda_j) has the solution
   basis c^s exp(lambda*c), 0<=s<m_lambda, where m_lambda is the root's
   multiplicity. This algebraic contract needs neither a Haar premise nor
   conjugation closure. The stronger positive Bernstein results require
   additional interval/conjugacy/real-root conditions; those are not
   imported. Future specialization must identify every endpoint exponent,
   polynomial degree and the separate lower-window contribution in the
   COMPLETE kernel. No actual annihilator or minimal order is asserted.

2. J. Boman, *On the propagation of analyticity of solutions of
   differential equations with constant coefficients*, Arkiv för
   Matematik **5** (1964), 271-279, DOI10.1007/BF02591127,
   [primary paper](https://archive.ymsc.tsinghua.edu.cn/pacm_download/116/7017-11512_2007_Article_BF02591127.pdf),
   Lemma1, pp272-273, (2.1),(2.2'), proof. Given compact K inside an
   open Omega, take smooth 0<=Psi<=1, compactly supported in Omega and
   equal to one near K; a nonnegative smooth unit-mass mollifier has
   sufficiently small fixed support. Convolve Psi with k copies of its
   k-rescaled mollifier. The resulting chi_k has support in Omega, equals
   one on K, and satisfies

       ||D^alpha chi_k||_infinity <= (C*k)^|alpha|, |alpha|<=k,

   where C>=1 bounds the first-derivative L1 norms of that fixed mollifier
   and is independent of k. Read the proof's support sum, unit mass,
   allocation of at most one derivative per factor and L1 convolution
   estimate (2.3)-(2.4). These are finite-order bounds, not an analytic
   compactly supported function or control beyond order k. Choosing
   compact K and support margins inside I is compatible with these
   hypotheses. The paper supplies no bound for our normalized response.

3. R. Melrose, *Chapter 3: Distributions*, MIT18.155 Fall2016 course
   [author notes](https://math.mit.edu/~rbm/18.155-F16/Chapter3.pdf),
   printed p44(1.4), p53(2.13)-(2.15). The pairing is complex-linear,
   with no conjugation, and differentiation transfers with a minus sign
   by integration by parts. The displayed D uses the author's 1/i
   convention; our proposed partial_c is the ordinary derivative. A
   future finite-order application must preserve that distinction and
   all coefficients without Hermitian conjugation. Compact support
   strictly inside I, not merely vanishing at its two endpoints, removes
   all boundary traces. No growing-order norm estimate follows from this
   identity alone.

4. G. Behm and A. Wennman, *Carleman-Sobolev classes for small exponents*,
   [arXiv:1404.3127v2](https://arxiv.org/pdf/1404.3127v2), 17 April2014,
   §3.1 pp8-11, (7)-(8), Lemma3.1 and Proposition3.2 including its
   proof. For decreasing positive summable a_j satisfying
   sum_(j>k) a_j <= (1-delta)*a_k with fixed 0<delta<1, their infinite
   box convolution u is smooth, supported on [0,sum a_j], and
   ||u^(r)||_infinity=1/(a_0*...*a_r). The proof uses separated translated
   supports, a surviving plateau and uniform derivative limits; its
   rectangle estimate gives the displayed Lp bound. The paper's ambient
   range is 0<p<1: no L1 assertion is imported by setting p=1.
   Neither the finite-spline smoothness wording nor a norm of a sum of
   derivatives is used here. This is an alternative benchmark, not a
   license to impose geometric widths on Boman's different construction.

These are source statements, not new local lemmas. Boman resolves the
essential finite-order cutoff lead through an inspected construction.
Hörmander's *Analysis of Linear Partial Differential Operators I*,
Theorem1.3.5 p19, was identified through secondary leads, but Springer
exposed only subscription/preview pages; the theorem was not inspected
in that book and is NOT imported. The separately accessible *Lectures on
Harmonic Analysis* had no matching infinite-convolution/Gevrey statement
in targeted searches. Abramczuk, J. Austral. Math. Soc.A39(1985),
Lemma1 proof p314, was inspected only to follow its reference[4] to
Boman; its unrelated continuation theorem is not an input. Browser
extraction of Boman's (2.2') and proof succeeded; direct shell retrieval
failed DNS and the screenshot request timed out. No inaccessible
formula is being treated as evidence. Boman's displayed finite-order
estimate, rather than the degraded OCR of general (2.2), is the contract
used for coverage.

### What the comparison permits and leaves open

The newly inspected quantitative resource is a cutoff family with an
order parameter, rather than merely the existence of a fixed smooth
bump. Its role in a later attempt is to pay derivatives through the
chosen operator order. It does not pay cancellations among those
derivatives, guarantee a nonzero normalization, or lower-bound the target
integral. A large upper estimate for a denominator is not a lower
estimate for its actual size and cannot prove that a family fails.

The later research test must first justify the complete kernel's
exponential-polynomial specialization using C997s(2) and its exact
antiderivative, then explicitly check the ordinary-derivative adjoint.
Both time endpoints for each beta term, the lower time window and K's
constant subtraction remain. It must bound the actual L1 norm from
above for a successful lower certificate, or use sufficient two-sided
control to establish a genuine upper bound for a failed family's
normalized action. A kernel-specific response estimate is indispensable.
Generic disconjugacy, annihilation, density of test functions, numerical
conditioning and nonzero fixed-n action do not supply the threshold.

Stops371/372 remain atomic-generator evidence, not optimal E_n bounds.
C997q's exact homogeneity obstruction concerns primal band transforms,
not a test density in c. No repetition of those attempts is proposed.
The prior two mathematical EXPLORATION outcomes remain recorded; this
source turn spends no mathematical exploration turn and resets nothing.

The exact statement/stronger-result queries included `Laguerre
differential annihilator compact`, `exponential polynomial annihilator
L1 norm compact`, `Ehrenpreis annihilator total variation`, `Laguerre
moving window approximation complex`, `compactly supported smooth
function derivative bounds infinite convolution`, and `Ehrenpreis cutoff
Lemma derivatives`. Most exact-target hits were irrelevant; no theorem
matching the complete-kernel rate was identified. Secondary answers and
generated-looking mathematics sites were not accepted as theorem
evidence. Primary references were followed from exponential-polynomial
and cutoff terminology, not inferred from search snippets. Local checks
read C997s's hypotheses, (1)-(2), C997c's complete-window representation,
and the two specific attempt records. No cross-notebook result was used.

### Continuation and approval boundary

Nominate one kernel-specific differential-density attempt with the exact
threshold already stated above. Its research component is the joint
choice/control of cutoff and annihilator in the actual target direction;
reproducing the ODE basis or Boman's theorem is not the intended outcome.
The continuation assessment is
[review374](2026-11-11-differential-density-cost-test-review-374.md).
It requires a separate approval turn before mathematical invocation.

No source promises success. Continue only with an explicit paid
normalized-action estimate or informative family-specific obstruction;
otherwise preserve the partial reasoning and change the mechanism rather
than repeat formal cancellation. Actual-Xi positivity, L966/L968 forcing,
L984(H), selected/both-sign transfer, reconstruction and regulator gaps
remain open. Mathlib: full matching theorem and cutoff-cost coverage not
checked; no absence claim. No RH candidate or new result beyond sources.
