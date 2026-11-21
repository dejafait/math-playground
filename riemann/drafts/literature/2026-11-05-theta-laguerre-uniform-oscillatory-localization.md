# Exact theta integral: completed uniform Laguerre source comparison

TARGET: Assess whether uniform large-degree Laguerre asymptotics apply inside L795's exact theta integral at x=kappa*d/(log d)^2, 1<=kappa<=2, with enough signed phase and remainder control to test a bulk-extremum sign.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step561 searched uniform Laguerre/Bessel/Airy remainder and theta-Jensen localization terminology; inspected DLMF 18.15.14–23, the Frenzen–Wong publisher abstract/access response, and Temme 1990 section 2; reused step559's unshifted-source comparison and L795's full-support stop. No matching signed theta-integral theorem was located; no novelty inference.
SOURCE_EVIDENCE: Live NIST DLMF 18.15(iv), 18.15.17–23, supplies overlapping scaled Bessel and Airy formulas with additive envelope errors; Temme, ZAMP 41 (1990), section 2, pp.115–117, confirms fixed alpha>-1. Frenzen–Wong 1988 full text was inaccessible and its remainder integrals were not read.
COMPARISON: Fixed alpha=-1/2 meets the parameter scope; n=d and scaled argument t=u^2*x/[4(4d+1)] match L795. Kernel phase and remainder domains are available, including a turning-point formula; no cited statement supplies a relative signed theta-average error, barrier margin, or degree-uniform integrated complement.
GAP: Weighted integration and a nonzero signed reference margin remain unpaid; neither fixed-degree integrability nor a pointwise envelope proves an eventual sign. The proposed bulk scaling remains a hypothesis to test.
REASON: SPECIALIZE authorizes use of the cited kernel estimates only; automatic bulk-sign import is parked. A separate, narrower support-localization test can pay an envelope-scale complement without presupposing a sign.
SCOPE: Completed source-scope comparison for d tending to infinity, x=kappa*d/(log d)^2, 1<=kappa<=2, full positive theta support, fixed alpha=-1/2 and fixed truncation order. No signed integral estimate or mathematical attempt is approved by this assessment alone.
LITERATURE_REASON: Changed target and specific unread lead: uniform oscillatory Laguerre asymptotics under L795's unbounded theta integral, rather than step559's coefficient asymptotics or step560's elementary source-inequality audit.

Essential inputs are L019/L021/L795 for the exact kernel, moments and
normalization. L810 is a contrast explaining why the printed uniform
input is unavailable, not a premise of any prospective sign estimate.
No cross-notebook result is proposed. No external theorem has been
imported by this nomination; Mathlib coverage remains unchecked.

## Exact source scope inspected

NIST [DLMF 18.15(iv)](https://dlmf.nist.gov/18.15#iv), live page
checked 5 November 2026, was read from the fixed-argument case through
the Airy coefficients and uniformity statement. In its notation, the
dictionary is

\[
 n=d,\quad \alpha=-1/2,\quad \nu=4d+1,\quad
 z=u^2x/4=\nu t,\quad r_d=d!/(1/2)_d.
\]

These are notation identifications, not a new asymptotic result.
Keep r_d when applying any formula to F_(d,u).

The compact-argument formula 18.15.14 cannot be used as a global
growing-argument estimate. For the scaled alternatives, the precise
source statements to import, without reproof, are:

* [18.15.17–20](https://dlmf.nist.gov/18.15.E19): fixed alpha and
  nonnegative integer M, uniformly 0<=t<=1-delta, with fixed delta>0;
  nu=4n+2alpha+2 and
  xi=(sqrt(t-t^2)+arcsin(sqrt(t)))/2. Inside the common prefactor
  exp(nu*t/2)/[2^alpha*t^(alpha/2+1/4)*(1-t)^(1/4)], the terms are
  xi^(1/2) J_alpha(nu*xi) sum A_m/nu^(2m),
  xi^(-1/2) J_(alpha+1)(nu*xi) sum B_m/nu^(2m+1), and remainder
  xi^(1/2) envJ_alpha(nu*xi) O(nu^(-(2M-1))). Both sums run from
  m=0 to M-1; A_0=1 and B_0 is explicitly given in 18.15.20.
* [18.15.21–23](https://dlmf.nist.gov/18.15.E22): fixed alpha and M,
  uniformly delta<=t<infinity. The signed zeta is negative below 1
  and positive above 1, as defined in 18.15.21. The prefactor is
  (-1)^n exp(nu*t/2) 2^(-alpha+1/2)
  t^(-alpha/2-1/4) (zeta/(t-1))^(1/4).
  The bracket contains Ai(nu^(2/3)*zeta)/nu^(1/3) sum E_m/nu^(2m),
  Ai'(nu^(2/3)*zeta)/nu^(5/3) sum F_m/nu^(2m), and remainder
  envAi(nu^(2/3)*zeta) O(nu^(-(2M-2/3))). E_0=1; F_0 is in
  18.15.23. Use continuous limiting coefficient values at t=1,
  rather than separately evaluating singular displayed factors.

The Airy equality includes the documented 1.0.11 correction replacing
an asymptotic-equivalence symbol by equality with an O remainder.
The formulas cover complementary argument regimes, but the number of
retained terms is fixed. They do not authorize M growing with d,
derivatives of a remainder, or complex-u contour deformations.

Envelope conventions were inspected in DLMF 2.8(iii)–(iv). Those general
ODE statements have their own hypotheses (including nonnegative order
in 2.8(iv)); do not apply that general ODE theorem with negative order.
The cited Laguerre statement itself has fixed alpha scope. For the
half-order Bessel factors the independently explicit identities are
[DLMF 10.16.1](https://dlmf.nist.gov/10.16.E1),
J_(-1/2)(v)=sqrt(2/(pi*v))*cos(v) and
J_(1/2)(v)=sqrt(2/(pi*v))*sin(v), v>0. Endpoint limits still require
care when assembling prefactors. No endpoint estimate is derived here.

## Primary references and access qualifications

C. L. Frenzen and R. Wong, *Uniform Asymptotic Expansions of Laguerre
Polynomials*, SIAM J. Math. Anal. **19** (1988), 1232–1248,
[DOI 10.1137/0519087](https://epubs.siam.org/doi/abs/10.1137/0519087),
is DLMF's named reference. The requested publisher PDF redirected to
its abstract and access page. Only the abstract, bibliographic data
and references were inspected: the abstract specifies fixed alpha>-1
and overlapping real domains, but is not evidence for the detailed
remainder integrals. No such integral is imported here.

N. M. Temme, *Asymptotic estimates for Laguerre polynomials*, ZAMP
**41** (1990), 114–126,
[author/institutional PDF](https://ir.cwi.nl/pub/2379/2379D.pdf),
section 2, pp.115–117, equations (2.1)–(2.2), was inspected as an
author-written account of Frenzen–Wong. It uses fixed 0<b<a<1,
Bessel domain (-infinity,a] and Airy domain [b,infinity), for fixed
alpha>-1. Its section 3 varying-parameter results were not used:
the nonnegative-alpha ranges there do not cover alpha=-1/2. The
original detailed proof remains unread; DLMF's precise statements
suffice for this scope decision, so access is not an essential blocker
to the narrower continuation below. Olver's book pages referred to
by Temme, and Dunster 2017, remain unread leads, not accepted inputs.

## Integral applicability and decision

L019 supplies an actual positive K with the stated superexponential
bound, and L021/L795 supply finite moments and the exact, fixed-degree
absolutely convergent average. Alpha=-1/2 is fixed and greater than -1;
the positive normalization r_d has no zero denominator. Uniformity in
the scaled real argument permits testing a degree-dependent real
u-domain after writing down its exact t-range. The small-u, oscillatory,
turning and unbounded cases must all be retained or bounded.

What is absent is an integrated remainder smaller than a specified
nonzero signed comparison value. The DLMF errors are measured against
special-function envelopes, which need not be small relative to an
oscillatory average. A positive envelope integral cannot be substituted
for that signed value. Neither the existence of an integrable bound at
each d nor positivity of K supplies the needed degree-uniform ratio.
No signed barrier family, lower margin, or integral error bound is
asserted. Thus the sources do not justify automatic sign import. This
is an informative source-scope limit, not a theorem that the mechanism
cannot work or a disproof of any P_d's hyperbolicity.

Queries included `Frenzen Wong 1988 Uniform asymptotic expansions
Laguerre polynomials pdf`; `Laguerre asymptotic theta Jensen polynomials
uniform oscillatory remainder large degree`; `Frenzen Wong 0519087
pdf`; `Laguerre theta Jensen asymptotics signs`; `Laguerre remainder
Frenzen integral uniform alpha -1`; `Laguerre theta localization
asymptotic Jensen`; and `theta Laguerre log degree integral asymptotic`.
Search results outside the sources above were leads only. Local scoped
searches of literature/attempt records found no previous matching
logarithmic-window estimate. Step559's coefficient/shift mismatches,
L795's interlacing stop and L810's false input remain in force within
their own scopes; none rules out the new, actual-weight support test.

The narrower continuation is nominated separately in
[the support-localization assessment](2026-11-05-theta-laguerre-envelope-support-test.md).
Its precise inequality is only a proposed test, with no derivation in
this literature turn. It requires separate next-turn approval. A
creative signed mechanism is still blocked by the absent independent
reference margin and cancellation-sensitive theta remainder.

Downstream use would be an independent signed comparison in one
growing-degree regime. Even success leaves edges, initialization,
shifted/mixed transfer and all-degree actual-Xi positivity unresolved.

Mathlib: full matching coverage is unchecked. No formal theorem or
absence claim is made. This source review adds no mathematical input
to the DAG; any later specialization belongs in its canonical lemma.
