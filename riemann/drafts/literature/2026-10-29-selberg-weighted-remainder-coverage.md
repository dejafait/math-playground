# Selberg local expansion: completed weighted remainder comparison

TARGET: Inspect the unconditional Selberg local logarithmic-derivative expansion cited by Ge and determine whether it supplies a zero-safe approximation to L471 (6) with Xi(t)^2/A(t)^2-weighted L1 remainder o(T(log T)^3) on [T,2T].
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Followed Ge v2 reference [14] to the IAS original, visually inspected its complete relevant formulas and proof sketch on numbered pages 2--5, checked derivative cases on pages 6--10, and searched the specific local signed/negative-mass records; queries, version and comparison below. No matching weighted differentiated theorem was found; no novelty is inferred.
SOURCE_EVIDENCE: Ge arXiv:2211.08571v2 Section 2, Proposition 2.1 and reference [14]; Selberg, unpublished IAS DOCtrond_0.pdf, numbered pp. 2--5, (6)--(18), and pp. 6--10, (20)--(34). The original is accessible and supplies an unconditional expansion, but no differentiated local-remainder estimate with the required weight.
COMPARISON: Selberg uses an ordinate cutoff, a zero-dependent auxiliary shift and an undifferentiated remainder with unweighted moments; (11) controls a derivative at the shifted point only. Neither this nor the later derivative-value distribution claims supplies the critical-line weighted absolute remainder threshold. Park this direct microscopic implementation; no impossibility theorem is claimed.
GAP: Differentiation of the moving-cutoff/zero-dependent remainder and Xi-amplitude weighted L1 control are unsupplied. The retained signed term, individual heights, higher signs and mixed positivity remain unresolved even if an approximation error is later bounded.
REASON: New primary-source evidence fails the saved continuation test for a direct citation application. Preserve the source and route stop; nominate a separately reviewed, direct-product truncation test rather than silently differentiate this remainder or repeat the completed L468 audit.
SCOPE: Actual Xi, L471's A(t), N(T) and equation (6); arbitrary nonreal zeros and multiplicities; no RH, spacing, simplicity, displacement lower bound, external 7/8 premise or differentiation of an uncontrolled error term.
LITERATURE_REASON: The previous comparison explicitly leaves the unconditional Selberg local expansion unread. Its weighted differentiated remainder is a changed, uncovered target; the three rejected direct transfers do not cover it.

## Original nomination and stopping test

The main gap remains initial actual-Xi signs at unbounded heights and
global mixed positivity. The proposed intermediate input is a
controlled arithmetic/local-zero approximation to the signed expression,
before taking its negative part. A sufficiently small weighted error
could make a later cancellation test meaningful; it would not itself
prove N(T)=o(T(log T)^3), much less RH.

Keep L471's exact normalization:

    A(t)=(t^2+1/4) pi^(-1/4)|Gamma(1/4+it/2)|/2,
    N(T)=integral_T^(2T) (-D_1(Xi;t))_+/A(t)^2 dt.

The desired comparison concerns D_1(Xi;t)/Xi(t)^2 away from real
zeros, followed by multiplication by Xi(t)^2/A(t)^2 and a justified
zero-safe extension or integrable limit. An approximation's remainder
E_T(t) would have to satisfy the explicitly tested threshold

    integral_T^(2T) Xi(t)^2/A(t)^2 * |E_T(t)| dt
        = o(T(log T)^3).

This is a proposed target, not an estimate established here. Real-zero
singularities, multiplicities, all completion terms and the sign of the
retained main expression must be kept visible. A principal-value
identity alone would not establish this absolute weighted estimate.
The source review must distinguish the theorem's stated hypotheses
from any additional localization or differentiation it would require.

Follow the exact unconditional reference in
[Ge v2](https://arxiv.org/html/2211.08571v2), then read the primary
statement and essential proof/error cases before longer extracts.
Record the precise theorem/page, all parameter ranges and whether
differentiated control is actually supplied. The linked Ge result is
a discovery lead here; its RH-dependent theorem is not an input to an
unconditional test. No assertion of novelty follows from local searches.

Continue only if the source supports a concrete smoothing/localization
regime with a credible route to the displayed error threshold and a
retained expression on which a separate sign test can be stated. If
the available control is only O(T(log T)^3), assumes the desired
real-zero/sign property, or requires an uncontrolled differentiated
remainder, record that specific mismatch and park this implementation.
Do not approve a creative proof attempt just because the expansion is
unconditional. A genuinely new cancellation mechanism would need its
own bounded test and escalation justification after this source gate.

Reuse the prior signed comparison's failures: Ge's inspected mean
assumes RH and close-tuple control; BGST has a different full-zero
weight; the inspected explicit-formula sign comparison needs real
ordinates. Preserve L251's generic first-sign masking, L472/L473's
finite-moment obstruction, L475's absolute-envelope cost and the
selected-energy/Dirichlet stops. They constrain route selection but
are not assumed as arithmetic inputs to the proposed estimate.

Mathlib: full matching coverage is unchecked; no source import, formal
verification, lemma or mathematical script is produced by this note.

## Completed source review, 29 October 2026

Outcome NEGATIVE concerns source applicability, not a negative theorem
about N(T). No lemma, mathematical script, DAG or PROOF.md was changed.
The main gap, intermediate threshold and downstream sign limitation
are the ones fixed above. Startup changes and unfinished work are preserved.

### Search and precise source identification

The exact lead is Ge's reference [14], **not** the 1946 paper first
suggested by generic search results. It is Selberg's unpublished
*On the value distribution of the derivative of the Riemann zeta-function*,
hosted under the IAS heading
[On the value distribution of derivatives of zeta-functions](https://publications.ias.edu/selberg/section/2483).
The primary scan is [DOCtrond_0.pdf](https://publications.ias.edu/sites/default/files/DOCtrond_0.pdf),
10 numbered pages, retrieved 2026-10-29; SHA256
`6512d69072f3346e2d69b696075c9af81c3de2b5e96a46c91fc2e5ab17749d1f`.
It has no dated theorem number; the formula and page numbers below
identify the inspected claims. This is a proof sketch, not an
independently audited published theorem.

Queries actually tried included `Selberg local approximation zeta
logarithmic derivative 1946 1943 1944 Radziwill lemma 5`,
`Selberg Contributions Collected Papers pdf`, and `Radziwill Gaps
between zeros of zeta lemma 5 pdf`. The 1946 bibliographic results
and Radziwill arXiv:1301.3232 were discovery leads only, not theorem
inputs. Ge v2's bibliography and Section 2 resolved the exact reference.
All 10 scan pages were visually inspected, with pp. 2--5 the essential
local-expansion/error cases. No Mathlib coverage claim is made.

### What the original actually states

For 4<=x<=t^2, t>0, (6)--(8), pp. 2--3, set

    sigma_x,t=1/2+2 max_rho(beta-1/2,2/log x),
    |t-gamma|<=x^(3(beta-1/2))/log x,
    s=1/2+it, s_x=sigma_x,t+it,
    P_x(t)=sum_(n<x^3) Lambda_x(n)n^(-s_x).

The maximum uses zeros satisfying the displayed condition;
Lambda_x is the piecewise smoothed von Mangoldt weight (8).
Equations (9)--(11) bound the auxiliary reciprocal-square sum,
zeta'/zeta(s_x), and (zeta'/zeta)'(s_x). Equation (12), p. 4,
expands about s_x with a full-zero remainder. Equations (14)--(16),
pp. 4--5, state

    zeta'/zeta(s)=Sigma_1(t)+Sigma_2(t),
    Sigma_1(t)=sum_(|t-gamma|<=1/log H) 1/(s-rho),
    Sigma_2(t)=O((sigma_x,t-1/2)log H (|P_x(t)|+log t)),
                                                            t<H.

Here H denotes the scan's upper endpoint T, not L471's dyadic
lower endpoint. The cutoff is by ordinate, not complex distance;
all nontrivial zeros and their multiplicities are retained. At a
pole the formula requires the meromorphic/punctured interpretation.
With x a sufficiently small power of H depending on positive integer
k, (17) states

    integral_9^H |Sigma_2(t)/log t|^k dt=O_k(H).

The sketch invokes Lemma 12 of its reference [2] for this moment.
It does not spell out the low-height reconciliation between
4<=x<=t^2 and a fixed power x=H^a in an integral starting at 9;
no uniform parameter claim for that whole interval is imported here.
The remaining pages discuss distributions of derivative values and
linear combinations; they do not state a weighted derivative bound
for Sigma_2 at s=1/2+it.

### Comparison with the requested estimate

The preceding is a source transcription and scope comparison, not
a derivation of a new estimate. In particular, the auxiliary derivative
in (11) is not a derivative estimate for Sigma_2. The real-variable
maximum sigma_x,t and the moving ordinate cutoff do not supply a
holomorphic remainder bound on a neighborhood. One cannot invoke
Cauchy's inequality from (16), or differentiate its O-symbol or (17).
A replacement would have to account for changes in the selected zeros
and for the zero-dependent shift. None is supplied by these formulas.

L471 (6) needs a reciprocal-square identity for the *completed* Xi.
Transferring zeta'/zeta requires the differentiated completion terms
as well as the remainder. L471/L465 already contain valid completion
normalizations; Selberg's formulas do not authorize replacing those
by a derivative of an uncontrolled real-variable error.
At real zeros the true residues can be subtracted before taking
limits, but the source does not give the requested weighted absolute
L1 estimate across those neighborhoods. Unweighted fixed moments in
(17) neither state that estimate nor a little-o saving after adding
the Xi(t)^2/A(t)^2 weight. No full-scale lower bound or impossibility
of such a saving follows from this mismatch.

Thus the direct microscopic differentiated-Selberg implementation
fails the nomination's continuation test: the required differentiated
weighted error is absent. Access is resolved; this is not SOURCE_BLOCKED.
The uninspected proof of the old Lemma 12 is unnecessary for this
negative applicability decision, since even accepting (17) does not
supply the missing derivative. It remains an unread supporting source,
not a theorem imported here. No new lemma or reproof is justified.

### Independent continuation nomination

A different approximation can be tested directly on L471's exact
reciprocal-square series, with a wider shrinking ordinate window.
Its purpose is to isolate a signed local term while estimating only
the discarded tail. L467's closed unit-shell counts and L471's zeroth
Hardy moment are available inputs; whether they deliver the proposed
error is deliberately left for a separate approved mathematical step.
The nomination is in
[direct-product truncation coverage](2026-10-29-mesoscopic-signed-truncation-coverage.md).
It does not assert a tail bound or small negative mass. In particular,
it is a specialization proposal, not a new creative cancellation
mechanism. A creative central-gap attempt remains blocked by the
absence of a concrete arithmetic sign test for the retained expression.
No historical stop is elevated to a global ban.
