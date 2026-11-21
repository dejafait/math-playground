# Residual-product contour ratio — completed source assessment

TARGET: Assess source coverage for bounding L835's actual quotient ratio M_s/m_1 by a residual canonical product and explicit zero-count tail at fixed k=6002.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step675 checked quotient/product-truncation and reciprocal-square zero-tail terminology, the clustered-pole assessment and step659/667 stops; reused the prior count assessment and L467 audit. Exact queries and primary ranges below. No matching actual quotient theorem was located; no novelty inference.
SOURCE_EVIDENCE: Reuse L832/L834/L835; Katkova math/0505174v1 (6) p.3 and Hadamard passage pp.5–6; Bellotti–Wong 2412.15470v2 Theorem1.1 p.1 and Section5 pp.23–24, with audited L467; Brent–Platt–Trudgian 2009.13791v1 conventions p.1, Theorem1 p.2, Lemma3/proof pp.6–7, Lemma4/Theorem1 proof pp.8–9 and Example1 p.9. Qualifications below.
COMPARISON: Unconditional product and explicit multiplicity-counted tail inputs are available. They do not already give M_s/m_1, certified endpoint data or overlap. The missing work is a standard product-modulus/count specialization retaining endpoints and the square map; no general product or zero-sum theorem needs reproof.
GAP: Construct an evaluable quotient bound and separate the first omitted factor, with a certified finite-data interface. Actual zero enclosures, numerical contour costs, enlarged PF applicability and L835(4) remain unpaid; no bound is derived here.
REASON: Inspected explicit count/tail inputs close essential source coverage and justify a separate bounded specialization. No essential source-access blocker remains for constructing the analytic envelope; finiteness alone still fails the mathematical target.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED scope newly required effective product-tail coverage; ready interpolation and count assessments were reused.
SCOPE: Literature-only step675; newly scoped calculation saved separately for next-turn approval. No lemma, mathematical script, quotient estimate or enlarged PF theorem written.

## Completed comparison — step675, 6 November 2026

The main gap is actual-Xi all-degree mixed positivity. The intermediate
purpose is effective control of L835's actual quotient, potentially joining
its fixed-shift eventual ray to a finite-PF range. Even a successful join
would leave growing shifts and other mixed minors unresolved.

### Product and actual zero correspondence

Reuse L832's product, L834's simple packet/separating disk and L835's
audited quotient and criterion (4). Their relevant proofs were read.
Katkova, *Multiple positivity and the Riemann zeta-function*,
[math/0505174v1](https://arxiv.org/pdf/math/0505174v1), (6), printed p.3,
and the Hadamard passage in Theorem1's proof, pp.5–6, give the
order-one-half product, reciprocal-modulus summability and compact
finite-product passage without RH. L832 already records the excluded
PF44 index issue; that inference is not imported. The genus-zero
normalization has no extra exponential factor to estimate.

Use L834's exact p=-4(rho-1/2)^2 and F(0)=1. Reflected xi zeros give
one F zero with its original multiplicity; positive-height xi zeros
supply representatives. Distinct off-line zeros at one positive height
remain distinct. Conjugate F zeros must be grouped when real products
are used. L834 already gives |p|=4(gamma^2+(beta-1/2)^2) and rules out
unverified smaller-modulus zeros. A total-ordinate tail can therefore
retain possible off-line zeros. No quantitative modulus estimate is
derived from that correspondence in this review.

### Effective count, reused rather than reproved

Chiara Bellotti and Peng-Jie Wong, *Improved estimates for the argument
and zero-counting function of the Riemann zeta-function*,
[2412.15470v2](https://arxiv.org/pdf/2412.15470v2), 7 July 2025,
Theorem1.1, printed p.1, gives, for every T>=e,

    |N(T)-T/(2pi) log(T/(2pi e))|
      <=0.10076 log T+0.24460 log log T+8.08344.

N counts all positive-height strip zeros, with multiplicity and inclusive
upper endpoint. Section5, pp.23–24, has separate large-height parameter
and bounded-height verification cases; both were inspected. Computations
are imported, not rerun. Audited L467 already handles multiplicities,
endpoint limits and closed shells. Its envelope permits an elementary
tail construction without individual high-zero locations. No independent
full-manuscript audit is claimed.

### Convergent zero sums: additional primary coverage

Richard P. Brent, David J. Platt and Timothy S. Trudgian, *Accurate
estimation of sums over zeros of the Riemann zeta-function*, Math. Comp.
90 (2021), 2923–2935, [DOI](https://doi.org/10.1090/mcom/3652),
[inspected preprint 2009.13791v1](https://arxiv.org/pdf/2009.13791v1),
29 September 2020: p.1 retains multiplicities and half endpoint weights.
Theorem1, p.2, assumes nonnegative C^2 phi with phi'<=0, phi''>=0,
2pi<=T0<=T and integrable phi(t)log(t/(2pi)). With Q=N-L and
L=T/(2pi)log(T/(2pi))-T/(2pi)+7/8, it states

    sum'_(gamma>=T) phi(gamma)
      = (1/(2pi)) integral_T^infinity phi(t)log(t/(2pi))dt
        -phi(T)Q(T)+E2(T),
    |E2(T)| <= 2(A0+A1 log T)|phi'(T)|+(A1+A2)phi(T)/T,
    A0=2.067, A1=0.059, A2=1/150.

These are unconditional total-zero sums. Read Lemma3 and its complete
proof, pp.6–7, including endpoints; Lemma4 and the full limiting proof
of Theorem1, pp.8–9. Integrability pays the vanishing boundary at infinity.
Section2 supplies the constants, including a bounded-height computation.
Example1, p.9, treats phi(t)=t^(-2), with
|E2(T)|<=(8.334+0.236 log T)/T^3. The term -phi(T)Q(T) remains payable;
this error alone is not a full tail bound. Any proposed logarithmic
weight needs its own shape check before applying this theorem.

The preprint has only v1; a v2 request returned 404. The published author
offprint's first page was accessible, but later requests timed out. The
numbering above is explicitly v1, not a claimed full comparison with the
published proof. Reuse `2026-10-07-signed-count-oscillation-comparison.md`
for published conventions/Lemma2. The numerical Corollary1 and its large
zero computation are unnecessary; Remark2's RH-dependent closed form is
excluded. No access loop is needed: L467's ready envelope suffices for
the proposed coarse construction.

### Search, recorded failures and bounded decision

Queries: `Riemann xi canonical product explicit tail bound zeros N(T)
Bellotti Wong`; `Brent Platt Trudgian sums over zeros zeta 1 gamma squared
explicit bound tail`; `"xi" "canonical product" "truncation" error zeros
bound`; `"Riemann" "residual product" "Toeplitz" zeros`; and
`"Riemann xi" "minimum modulus" finite product tail`. No inspected source
already supplies L835's normalized ratio. Search results imply neither
absence nor novelty. Growing-order Laguerre and general minimum-modulus
hits remain leads, not imported quotient theorems.

Read and preserve the step659 hybrid and step667 signed-composition
stops. This target uses the actual analytic quotient rather than an
uncertified hybrid determinant or signed growing-order residual minor.
The clustered-pole assessment is reused. Effective product-tail control
would be a local standard-method specialization, not new product theory
or an RH advance beyond the inspected sources.

One bounded construction is nominated separately in
`2026-11-06-residual-product-envelope-specialization.md`: a finite
evaluable upper bound B for log(M_s/m_1), initially at s=(1+q)/2,
with a certified finite-data interface. Isolate the first omitted factor
and retain all endpoints. The later test inserts B into L835(4); no
negative value of that expression is claimed. Larger m needs a separate
applicability argument. Only PF6001 is established locally.

Continue if B is evaluable from specified certified finite inputs and
unconditional sources without assuming a lower contour bound. Stop a
chosen majorant as an overlap certificate if it demonstrably misses
L835(4), preserving that evidence. Missing endpoint enclosures blocks
numerical evaluation, not the separately scoped symbolic construction;
unknown finite constants still fail. Full matching Mathlib coverage is
not checked. No new mathematical result or estimate is produced here.

## Original step674 nomination — preserved

The main gap is actual-Xi all-degree mixed positivity, L030–L032/C032a.
The intermediate purpose is a rigorous, computable upper bound for the
actual ratio in L835(1), potentially usable in its strict overlap test
(4). Even overlap would concern one fixed shift, not growing shifts,
other mixed minors or RH. No numerical ratio, zero enclosure or new
lemma is supplied by this nomination.

Essential inputs are L835 and audited L834/L832, with their inherited
L018/L021/L776 conventions. Keep k=6002, the actual distinct simple
p_1,...,p_k, R=(p_k+p_(k+1))/2, q=p_k/R<s<1 and r>=6001.
Here g(z)=F(Rz)/prod_(l<=k)(1-Rz/p_l), M_s=max_(|z|=s)|g(z)|,
and m_1=min_(|z|=1)|g(z)|. The reviewed target must concern this
actual quotient, not an arbitrary zero-free analytic substitute.

The new coverage question is whether a residual canonical product,
separating explicitly the first omitted pole, admits certified upper
and lower contour bounds from finite zero enclosures and an explicit
zero-count tail. Every zero must retain its multiplicity; reflected
xi zeros must not be counted twice after the square map. Conjugate
pairing, compact product convergence and possible off-line zeros above
H must be handled under actual unconditional hypotheses. The known
genus-zero product is reusable; effective tail estimates and admissible
finite data are essential unread inputs, not established tools here.

Continuation test: identify inspected theorem statements and proof
cases that permit a specified computable envelope under these exact
hypotheses, and nominate one finite, independently checkable bound to
test against L835(4). If the proposed coverage only proves finiteness,
assumes RH or assumes the required lower contour bound, it does not
pay the target. A persistent essential source blocker requires parking
that dependent calculation and choosing an independently testable
target, preserving the blocker. The review may document failure and
need not approve a new lemma or a numerical sweep.

Unresolved assumptions/obligations include certified packet data and
separation, effective residual contour estimates, the actual strict
inequality (4), and applicability of any enlarged PF order m. Only
PF6001 is established locally. The first-hybrid-corner ratio stop
(step659) and the fixed-winding/source-access limitations (step667)
remain evidence; neither is reopened by this proposal. No cross-notebook
input is proposed. Full matching Mathlib coverage remains unchecked.

This is a proposed standard-method quantitative continuation, not a
creative central mechanism. No justified new creative mechanism is
ready: success of the algebraic audit supplies no evidence yet that the
remaining absolute contour costs can be paid. The next turn is a
source comparison, not permission to derive and approve uncovered
mathematics in the same turn.
