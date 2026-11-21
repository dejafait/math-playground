# Effective opposed-slice tail — nomination934, completed review935

TARGET: Derive explicit constants m>0 and R>=pi/(2S), S=3B'(1), such that p(S)>=m and abs(K(r)*abs(h(1+ir))^2-2*pi*p(S))<=pi*m for every abs(r)>=R, using the full actual law and C466l's normalized integral.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review935 checked exact reciprocal-Xi/opposed-marginal and theta_1 density-bound queries, complex log-Gamma remainder terminology and rigorous inversion/quadrature sources; no matching effective K theorem was located. Reused reviews930/933 and stop927/stop932; details and unsuccessful retrievals below. This is bounded coverage, not a novelty claim.
SOURCE_EVIDENCE: Inspected DLMF5.11.1/5.11(ii) https://dlmf.nist.gov/5.11 and 25.2.1/25.2.6/25.2.7 https://dlmf.nist.gov/25.2; Brent arXiv:1609.03682v2 Section2 Theorem1 (5)-(12), pp4-5 https://arxiv.org/pdf/1609.03682v2; Johansson arXiv:1309.2877v1 Section2 Theorem1 (5)-(14), pp2-4 https://arxiv.org/pdf/1309.2877v1 and arXiv:1802.07942v1 Sections2/2.1/3.2, pp2-3/6 https://arxiv.org/pdf/1802.07942v1. Compared Sra arXiv:2611.02944v1 Lemma2.4/AppendixB.3-B.4 https://arxiv.org/html/2611.02944v1; retained original inherited density input, without importing changed-source extras.
COMPARISON: Explicit Gamma remainder bounds and rigorous finite quadrature cover essential tools, not the full target. Sra's positive-density proof supplies no numerical m at this S. Quantify the existing C466l proof, retaining complex phases, and certify p(S) by its existing inversion plus explicit tail and finite enclosure; no known identity needs reproof.
GAP: Still to be established mathematically: explicit m and an enclosure of S; explicit full-h and compact bounds; quantitative local complex-ratio error and a uniform moving-frequency majorant/integral error for every abs(r)>=R. The cited methods cover how to attempt these, but no constants, certificate, or effective onset were obtained in review935.
REASON: Ready source coverage supports a bounded quantitative specialization of an audited mechanism. A successful m,R would specify a compact interval for later slice signing, leaving full marginal signs and Xi transfer unresolved. Separate next-turn approval is required for this newly completed assessment; do not derive its mathematical specialization in this literature turn.
SCOPE: Same actual p=theta_1, h, S=3B'(1), original Re(z)=1 and C466l normalized integral; inherited C466k/C466a/L018 qualifications retained. Analytic estimates and, if needed, rigorously enclosed finite inversion are assessed. No finite-core substitute, new contour, RH, PF-infinity, extra zero verification, or independence after conditioning is admitted.
LITERATURE_REASON: Audit934 newly nominated explicit remainder constants, a density lower bound and quantitative integral control; reviews930/933 cover only the unchanged representations and qualitative limit, not this effective scope.

## Completed source comparison935

### Primary estimates and the exact cases inspected

[DLMF5.11(ii)](https://dlmf.nist.gov/5.11#ii), with
[5.11.1](https://dlmf.nist.gov/5.11#E1), bounds the complex
log-Gamma remainder after terms through n-1 by the modulus of the
first omitted term times sec^(2n)(arg(w)/2). For the empty Bernoulli
sum, n=1, that term is 1/(12w). This is a log-Gamma bound, distinct
from the multiplicative Gamma remainder in 5.11.10-11. The relevant
sector for w=sqrt(z)/2+1/4 is already verified in C466a. The logarithm
is the analytic continuation real on the positive axis; taking a
principal logarithm of the Gamma value can change it by 2*pi*i.
No effective constant for the *whole* B(z) expansion follows without
also bounding its polynomial, fixed shift and zeta terms.

[Brent, arXiv:1609.03682v2](https://arxiv.org/pdf/1609.03682v2),
Section2, equations (5)-(12), printed pp4-5, provides an alternative
uniform bound even on the nonzero imaginary axis. In his notation
T_k(w)=B_(2k)/(2k(2k-1)w^(2k-1)) and R_k is the remainder after k-1
terms. For Re(w)>=0, w!=0 and integer k>=1, Theorem1 states
|R_(k+1)| <= sqrt(pi)*Gamma(k+1/2)/Gamma(k)*|T_k| and
|R_k| <= (1+sqrt(pi)*Gamma(k+1/2)/Gamma(k))*|T_k|.
The full proof case was read: the periodic-Bernoulli integral (8),
|u+w|^2>=u^2+|w|^2, the Wallis integral, and R_k=T_k+R_(k+1).
No derivative of a remainder is supplied by those value inequalities.
Use either explicit cited bound; redoing its proof is unnecessary.

[DLMF25.2.1, 25.2.6-7](https://dlmf.nist.gov/25.2)
give the absolutely convergent zeta and derivative series for Re(s)>1.
They cover s=1/2+sqrt(1+it) on the real integration line; enclosing
complex neighborhoods still requires checking that condition, or a
continuation algorithm. Termwise absolute majorants and elementary
series-tail bounds are legitimate proposed specializations, not a
new zero-free-region input. No such bound was derived in this review.

For finite special-function enclosures, [Johansson,
arXiv:1309.2877v1](https://arxiv.org/pdf/1309.2877v1), Section2,
Theorem1 and (5)-(14), printed pp2-4, treats zeta(s,a) and derivatives
in s. Its hypotheses are N,M positive integers, Re(a)+N>1 and
Re(s)+2M>1. It bounds the Euler-Maclaurin remainder coefficientwise
using the explicitly defined J_k, K and C in (12)-(14). The proof
through its final comparison with J_k was inspected, including the
logarithm branch and argument factor. The proposed a=1 case must use
those actual bounds and include all arithmetic errors; a numerical
value alone is insufficient. Removable completion factors must be
handled if an enclosure contains a singularity of an individual factor.

### Positive density versus a certified numerical lower bound

The original imported Hub-v1 density result remains the input in
C466a. That URL timed out twice in this review; existing reviews
already cover the imported assertion. The accessible [Sra,
arXiv:2611.02944v1](https://arxiv.org/html/2611.02944v1), Lemma2.4
and AppendixB.3-B.4, was inspected only for effective overlap. Its
gamma-extraction proof chooses a small-time threshold from an
asymptotic, then a gamma rate; strict positivity uses a residual law
whose support has infimum zero. It does not exhibit numerical choices
or a residual small-ball probability at the present S. Thus the proof
does not directly import the requested m. Other PF claims and direct
certificates in that version were not assessed or imported here.
No equivalence of entire source versions is presumed.

The assessed alternative is the already established C466k(7)
inversion at y=S, with a finite rigorous enclosure and an explicitly
bounded omitted tail. [Johansson, arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942v1),
Section2, printed p2, gives a Petras/Gauss-Legendre method for a
complex analytic integrand bounded by M on an ellipse with foci +/-1:
error <= M*rho^(-2n)*C_rho, with C_rho<50 for rho>1.1. The algorithm
checks complex neighborhoods and bisects if a usable bound fails.
Section2.1, pp3-4, says requested tolerances are not guarantees;
the returned radius is the evidence. Section3.2, p6, requires manual
truncation and a separately justified tail for improper integrals.
Those algorithm and failure cases were read. This covers finite
integration, not a ready p(S) certificate or the unbounded r range.

Applicability obligations for the later attempt are explicit: enclose
c0, x and S; propagate their uncertainty through the integrand; bound
reciprocals on every integration box and check analytic neighborhoods;
add the infinite-tail error; and obtain a strictly positive final lower
endpoint. Passing a tolerance flag, approximate quadrature or appealing
to qualitative p(S)>0 alone does not discharge any of these obligations.
No installation, code execution, or presumed software availability is
part of this source review. The method is an option, not a certificate.

### Exact-target comparison, failures and continuation gate

Queries actually checked include `complex log gamma Stirling explicit
remainder bound right half plane DLMF 5.11.11`, `"reciprocal" "xi"
"density" Laplace transform positive theta Riemann`, `"xi" "opposed"
marginal tail reciprocal density`, `"theta_1" "xi" density lower bound`,
`"K(r)" "h(1+ir)"`, and `Fredrik Johansson rigorous numerical
integration arbitrary precision Petras 2018 arxiv`. Several exact
queries returned unrelated material, not an exact match. Search
snippets, aggregator pages and unrelated preprints are not evidence
for the desired theorem. Failed guessed endpoints (1309.2877v2 and a
FLINT zeta documentation path) were not used; the actual v1 primary
paper resolves the needed evaluation coverage. Current FLINT Gamma
documentation was read for branch conventions only; its API is not
an additional proof input. No further essential source access is pending.

Reuse reviews930/933 for inversion, convolution, Andreief, and the
comparison with nonnegative convolution/positive-dilation theorems.
The changed scope here is effectiveness, not their identities. Local
C466a, C466k and C466l supply qualitative constants only. Stop927
excludes its regular common-product scalar/pair phase mechanism;
stop932 excludes independence after conditioning. Neither is reopened.
The conditional-core stop supplies no lower bound or uniform tail here.

SPECIALIZE means that known explicit estimates cover ingredients;
the *unproved difference* is their quantitative assembly for the full
actual h and this three-factor normalized integral. A direct import of
the entire target was not found. One later research attempt may try
to make C466l(9)-(21) effective and certify p(S), without reproving
the cited theorems. It must cover the moving neighborhoods t=+/-r,
the compact beginning of b, the complex ratio error on a fixed finite
t interval, and the remaining infinite t integral uniformly for all
|r|>=R. A few evaluated r values or an effective Stirling bound alone
cannot meet the target. This is a proposed work specification, not a
new estimate or a claim that the assembly succeeds.

Continue only with actual explicit m,R and the exact requested
inequality, or a bounded attempt recording the first quantitative
obstruction. If essential tools acquire changed hypotheses, stop that
dependent calculation for a separate assessment. This newly ready
assessment receives separate next-turn approval before research;
no mathematical specialization was performed in review935. The
unchanged exact target remains the single continuation. The appropriate
mathematical routing is proof_attempt/development, deep_research/xhigh,
because effective moving-scale domination is difficult established-route
development. Full matching Mathlib coverage remains unchecked; unknown
availability is not evidence of absence.

## Original nomination934 (historical; superseded by review935 above)

The exact target retains p=theta_1, h(z)=xi(1/2+sqrt(z))/c0,
x=B'(1)>0, S=3x, q(u)=h(1)e^(-u)p(u), and the original line
Re(z)=1. Its local input is C466l, via C466k and the inherited
C466a/L018 density, strip, symmetry, paired-product, counting and
verified-low-zero qualifications. The external density and zero
certificates have not been independently replayed. No PF-infinity,
conditional independence, finite-core substitution, or new contour
is proposed.

At nomination934, the requested next turn was literature-only: check primary theorem hypotheses
and explicit constants for the proposed effective estimates; begin
with the exact remainder cases needed on Re(z)=1. Determine what
additional rigorous inversion or positive-density input would provide
m at this particular S. Search the active notebook's relevant
reciprocal-density work for duplicates or already recorded failures
before proposing a calculation. A finite numerical sample, an
unspecified big-O constant, or an approximate positive p(S) is not
the requested evidence. No source is currently declared inaccessible;
the new effective scope is simply unassessed.

The mathematical pass threshold, if subsequently approved, is the
displayed uniform error bound together with explicit m and R. It would
give a finite endpoint for later compact slice signing, but would
not itself sign the remaining interval, the full two-frequency
marginal, its determinant, or any actual-Xi all-degree form.
Failure to obtain the necessary effective source inputs must be
recorded precisely, without relabeling the qualitative limit as an
effective result. A persistently blocked dependent task should be
parked for an independently testable target under the shared rules.

The stops in C466k/stop927, the conditional-core record, and
C466l/stop932 remain intact. No new theorem, effective bound,
mathematical script or numerical certificate was derived in this
nomination. Full matching Mathlib coverage is unchecked. The exact
next routing is literature_comparison, standard/high: determine
applicability and usable constants before any quantitative proof or
implementation. Any newly ready continuation gets separate approval.
