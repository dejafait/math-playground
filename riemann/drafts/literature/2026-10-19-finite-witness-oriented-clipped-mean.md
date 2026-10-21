# Completed source comparison: fixed-witness oriented clipped mean

TARGET: Test whether L436's fixed polynomial gives a strictly positive liminf for E_H[Delta (Bcal_-)^2 P(t log 2,t log 3,t log 5)]/(log H)^4.
CHECKED: 2026-10-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 243 performed bounded exact-clipping, signed Hardy-jet and fixed-twist discovery; reused the step-99 and step-173 comparisons, read audited L411/L405/L436, and inspected the new Grover--Mezzadri--Simm 2604.03051v1 theorem and relevant proof cases. No matching signed clipped theorem was located; this is not an exhaustive absence or novelty claim.
SOURCE_EVIDENCE: Hughes--Young 0709.2345v2 Theorem 1.1/(16)--(17), pp. 4--5, and holomorphy remark https://arxiv.org/pdf/0709.2345v2#page=4; Bui--Hall 2304.05178v1 Theorem 3, defining asymptotic and Corollary 1 https://arxiv.org/html/2304.05178v1; Curran--Heycock 2403.00902v1 Theorem 1.1 and Section 4 https://arxiv.org/html/2403.00902v1; Grover--Mezzadri--Simm 2604.03051v1 Proposition 1.3, Theorems 1.2/1.4 and Lemma 3.3/(3.17)--(3.27) https://arxiv.org/html/2604.03051v1. Reuse audited L411, L405 and L436 without reproof.
COMPARISON: The fixed finite prime weight is compatible with fixed rational polynomial twists, but the inspected sources still do not evaluate the sign-restricted real-jet observable. The new unconditional derivative result takes the height limit at fixed sigma>1/2 before the line limit; its critical-line matrix analogue is not an actual-zeta clipping theorem. L411 is absolute transfer and L405 is unclipped evaluation.
GAP: No signed clipped leading coefficient, positive liminf, suitable joint-sign symmetry or controlled nonpolynomial approximation is established. Absolute transfer does not remove this evaluation gap. The complete physical response, sharp interval and quartic-scale error must remain in any reopening.
REASON: The bounded discovery is complete without an adequate matching input; park this source-based evaluation rather than repeat the step-99 blocker. Propose a materially different prescribed-response signed-intermediate feasibility test, separately REVIEW_REQUIRED, without attempting or approving its mathematics here.

## Exact proposed scope and relevance

Use the complete actual Delta and Bcal and the same normalization as
L435--L436, E_H=H^(-1) integral_[H,2H]. Set Bcal_-=max(-Bcal,0).
P is exactly L436's polynomial at degree 131071 in each coordinate,
fixed before any height limit. The requested threshold is a strictly
positive liminf after division by (log H)^4, not merely a nonnegative
unweighted moment or existence of an asymptotic expansion.

The main RH gap remains global mixed positivity. The proposed intermediate
target could supply sign-sensitive information in the region selected by
the finite witness. L436's negative cubic mean leaves both opposite-sign
orientations possible; neither that result nor L405's unclipped benchmark
evaluates this target. Even a successful positive liminf would leave
capped nondegeneracy and L413's full-error regulator scale, as well as
the main positivity assertion, unresolved. No complete route to RH is
claimed.

Essential inputs to assess are L436 and its step-242 audit, the actual
definitions and absolute transfer in L411, and the unclipped comparison
in L405. Inherited analytic inputs should be read only for a concrete
application question. Reuse their existing assessments where applicable;
do not reopen the entire chain or repeat the ready finite-witness review.
Search the specific clipped-statistic source and failure records for a
matching theorem or persistent blocker before external discovery.
The L431 calibration and positive one-/two-prime densities remain valid
contrasts; they do not approve a clipping theorem. No sine limit,
growing-character uniformity, joint distribution or law realization is
assumed.

The next invocation is literature-only. Seek primary hypotheses for a
signed clipped moment with the required ordinary jets and fixed rational
characters, distinguishing absolute transfer from evaluation. Approve a
mathematical attempt only if an exact import, justified specialization or
bounded adequately assessed test is available. If known restrictions or
a persistent essential source blocker prevent this target, record that
specific limitation and choose a materially different independently
testable target; do not repeat source searches indefinitely. Failure to
find a matching theorem is neither a negative value nor evidence of
novelty. No mathematical calculation has been performed for this proposal.

LITERATURE_REASON: The new fixed-polynomial nonlinear clipped statistic lies outside the ready L436 finite-kernel audit and requires its own essential source comparison.

Full matching Mathlib coverage is unchecked; no absence claim is made.

## Completed comparison — 2026-10-19, step 243

This section supersedes the retained proposal's pending-review language.
Outcome EXPLORATION / LITERATURE / NOVELTY_UNCHECKED: a bounded source
review, with no new mathematical input or negative value for the target.
The exact TARGET above is preserved. No lemma, mathematical script,
certificate, argument in PROOF.md or dependency in DAG.md was changed.
Mathematical exploration usage remains 0 of 3; this review does not
spend or reset that budget.

### Local comparison and duplicate/failure check

Read L411's complete transfer proof and the start of its separate audit,
L405's hypotheses and full-square specialization, and L436's statement
and separate audit conclusions. They distinguish three different scales
and tasks: absolute quartic transfer, unclipped quartic evaluation, and
the fixed P-weighted signed cubic with coefficient beta I<0. None states
the desired clipped quartic lower bound. P has its exact degree 131071
fixed before H; no growth of its degree or rate for its height onset is
requested. Its finite size is not itself the uncovered hypothesis.

Reuse the primary comparisons in
`2026-10-13-clipped-linear-coefficient-joint-sign.md`,
`2026-10-14-clipped-square-absolute-transfer.md` and
`2026-10-14-clipped-square-transfer-critical-audit.md`.
Also read `2026-10-16-actual-amplitude-truncated-quartic.md` and its
canonical step-173 ATTEMPTS record. That review excludes substituting
RH-dependent scalar weighted distributions or repeating the stopped
fixed-p radial split. These restrictions persist for the present test.
No completed duplicate of the P-weighted clipped result was found in
the targeted clipping and finite-witness records. L431's positive
calibration, L435's signed density and L436's obstruction retain their
respective scopes; none asserts the actual desired orientation.

The source review tests whether the required lower bound can be imported
or reached by an assessed approximation. It finds neither in the
inspected sources. No extension of L411 to a new weighted estimate is
proved here, and no clipping or indicator is differentiated or moved
through a holomorphic contour. No scalar sign theorem is interpreted as
independence of the response, critical jets or the three prime phases.

### Primary theorem comparison

**Fixed polynomial apparatus, reused.** Hughes--Young, *The twisted
fourth moment of the Riemann zeta function*, J. reine angew. Math. 641
(2010), 203--236, [0709.2345v2, Theorem 1.1/(16)--(17), pp. 4--5](https://arxiv.org/pdf/0709.2345v2#page=4):
four complex shifts O(1/log T), coprime h,k with
hk<=T^(2/11-epsilon), nonnegative smooth w supported in [T/2,4T],
w^(j)=O_j(T0^(-j)), T^(1/2+epsilon)<<T0<<T. The stated error is
O(T^(3/4+epsilon)(hk)^(7/8)(T/T0)^(9/4)); its complete six-term
main expression is holomorphic. These hypotheses accommodate each
separately fixed rational twist after its onset. They do not allow
w to be a clipped function of the actual jets. Reuse the inspected
residue and sharp-endpoint cases through the L405 assessment; no new
polynomial-weight evaluation or source reproof is undertaken.

Bui--Hall, *On the derivatives of Hardy's function Z(t)*,
[2304.05178v1, Theorem 3 and its defining asymptotic](https://arxiv.org/html/2304.05178v1),
evaluates products of four fixed ordinary Hardy derivatives with one
logarithmic power of error saved. Corollary 1 cancels the leading
coefficient for odd total derivative order. This is not symmetry under
reversing the critical jet in the proposed clipped statistic. L411 uses
the pure fourth-order bounds; L405 uses the polynomial asymptotics.
Their already assessed physical conversions and tail bounds are reused.

Curran--Heycock, *Sharp bounds for joint moments of the Riemann zeta
function*, [2403.00902v1, Theorem 1.1/(2) and Section 4](https://arxiv.org/html/2403.00902v1):
fixed n, h_j>=0, sum h_j<=k and 0<=k<=2 give unconditional upper
bounds for absolute mixed powers of zeta and its derivatives. Extension
to k>2 assumes RH. Section 4 uses small-circle Cauchy transfer, convexity
and the functional equation. It does not evaluate a clipped signed
moment or supply the missing approximation error at fourth-log scale.
An O(log^4 H) envelope alone is not a vanishing clipping-approximation
error. The previous review's scalar sign and distribution comparisons
are reused rather than researched again.

**New primary lead.** Grover--Mezzadri--Simm, *Higher order derivative
moments of CUE characteristic polynomials and the Riemann zeta function*,
[2604.03051v1, 3 April 2026, Proposition 1.3/(1.18), Theorem 1.4/(1.21), Lemma 3.3/(3.17)--(3.27)](https://arxiv.org/html/2604.03051v1):
for fixed derivative lists of lengths at most two on each side, the
unconditional zeta statement takes T to infinity at fixed sigma>1/2,
then sigma down to 1/2. The general-length version assumes Lindelof.
Read the fixed-sigma mean-value proof, including the two-by-two
approximate-functional-equation case and its diagonal/error distinction.
Theorem 1.2's microscopic boundary limit is for CUE; the concluding
discussion conjectures the corresponding zeta transition. Neither
result gives a critical-line joint signed distribution, clipping, or
the present response-correlated lower bound. No such specialization is
imported. This comparison also avoids exchanging the two limits.

### Discovery and access record

Queries included `"Riemann zeta" "clipped" moments derivatives`,
`"Hardy" "joint distribution" derivatives sign moments`,
`zeta derivatives signed truncated fourth moments positive negative part rational twist`,
`"zeta" "sign" "joint moments" Hardy derivatives clipped`,
`"Hardy’s function" "weighted" "distribution" derivatives`,
`"zeta" "truncated" "signed" fourth moment derivatives`,
`Simm 2026 joint moments Hardy zeta function signed derivatives`,
`"zeta" "clipped moment"`, and the exact new paper title.
Unrelated results, model discussions and search snippets were not used
as theorems. The new paper's primary HTML was accessible and its relevant
statements and proof cases were inspected. The Simm--Wei publisher page
and a requested v3 HTML failed; neither is an essential unresolved
access dependency, since no result from them is imported. The
Grover--Mezzadri--Simm paper is a distinct inspected source, not a claim
that the older unread Simm--Wei full-text lead has been verified.

### Route decision and reopening test

No sign or limit of the exact TARGET is decided. The fixed P does not
by citation repair the persistent nonpolynomial signed-evaluation gap.
Park this source-based certificate. Reopening requires a specific
unconditional sign-sensitive theorem or controlled approximation with
the exact jets, full response and sharp fourth-log error; another
unrestricted polynomial moment or scalar sign theorem is insufficient.
This is a scope limitation of checked sources, not an impossibility
theorem or evidence of novelty.

The sole continuation is the REVIEW_REQUIRED proposal in
`2026-10-19-finite-witness-signed-intermediate-feasibility.md`.
It changes the mechanism to a prescribed-response law feasibility test
with both cubic orientations, rather than asking the missing clipping
theorem again. No feasibility, uniform direction, calibration or law
preservation is proved or approved here. Its potential use is to test
whether the new finite obstruction forces orientation even in the
selected-moment relaxation. Actual critical/global realization, actual
clipping, capped nondegeneracy, L413's full-error regulator margin and
the main global mixed-positivity assertion remain independent gaps.
