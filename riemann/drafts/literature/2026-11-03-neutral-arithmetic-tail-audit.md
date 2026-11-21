# Neutral arithmetic tail interface: separate audit nomination

TARGET: Independently audit paper 18/v3's arithmetic neutral-tail estimate (36)--(40), using the prime-kernel functional, complex coefficients and the j=1 jump.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The dyadic-contraction review searched active-notebook records for neutral gradients, paper 18 and Ehm without a duplicate; its external Vasyunin/Selberg searches located the exact source. Reuse 2026-11-03-triangular-mobius-dyadic-energy-contraction.md; no novelty claim.
SOURCE_EVIDENCE: bramble_trace paper 18/v3 (22 October 2026), definitions, complete anchored Gram identity (4), absolute divisor identities (6)--(8), and full proof (36)--(40), including the coefficient inversion at j=1, were inspected.
COMPARISON: The source gives the real-coefficient arithmetic estimate. Audit its uniform constants and endpoint, expressing the target functional directly as the prime-kernel series and checking the complex pairing convention; no new sign or convergence theorem is sought.
GAP: Local verification of all regroupings, the finite jump inversion and N,K-uniform bound remains; representer identification, neutral density, anchored-to-unanchored transfer and complementary residual control are excluded and remain unresolved.
REASON: This is an independently testable arithmetic interface for possible future neutral preconditioning. The original dyadic contraction lacks a paid signed estimate; replay of an unreviewed manuscript's load-bearing tail argument is justified before importing it.
SCOPE: Source coverage is prepared for this audit only; the newly written assessment requires separate approval next turn. No mathematical result is established in this literature step. After approval use REPRODUCTION, not a novelty classification.

## Exact proposed audit and source conventions

Primary source: [paper 18/v3](https://rstation.ai/problems/riemann_hypothesis/papers/18/v3),
*Fixed and growing neutral gradients of the anchored Selberg–Mobius
approximant*, 22 October 2026. The current paper URL inspected was
`https://rstation.ai/problems/riemann_hypothesis/papers/18`, labeled v3.
This is an unreviewed source claim, not a locally verified theorem.

Use its Hilbert space H=L2((1,infinity),dy/y^2),

    rho_m(y)=floor(y/m)-floor(y)/m,
    a_m=(m-1)/(2m), f_m=rho_m+a_m,
    K_m(t)=integral_t^infinity f_m(y)dy/y^2,
    T_m(n)=sum_(j>=1) K_m(j*n).

Here f_m is periodically extended to [0,infinity) as in the source.
For integers N,K>=2 set L=log N and take the source's triangular
anchored approximant g_N. Let u=sum_(2<=m<=K)c_m rho_m satisfy
sum c_m a_m=sum c_m T_m(1)=0. Define K_u=sum c_m K_m.
Use the inner product linear in its first argument. For complex u,
the proposed comparison functional is explicitly

    Q(u)=-sum_(k>=1) Lambda(k)*conjugate(K_u(k)).

The audit must verify the source's bounds in this convention:

    |L*<1-g_N,u>-Q(u)| <= zeta(2)/(4*N)*sum_(m=2)^K m*|c_m|,
    sum_(m=2)^K m*|c_m| <= 3*sqrt(2)*zeta(3/2)*K^(5/2)*||u||.

These are source-audit targets, not conclusions of the present turn.
The direct functional avoids relying on the source's separate
analytic identification Q(u)=<q,u>. No new zeta continuation,
zero-free region, simplicity or derivative moment is contemplated.
The use of mu and Lambda is ordinary arithmetic, not an arbitrary
coefficient model. The absolute divisor identities in (6)--(8)
and their standard Mobius-inversion inputs suffice for this scope.

## Bounded acceptance and failure test

Check the source's full periodic primitive, finite Gram identity,
absolute infinite divisor regrouping, signed finite tail, integral
comparison for every N>=2, and complex conjugations. In jump
inversion retain u_0=0 and the j=1 jump. Verify the coefficient
inequality as a norm bound uniform in K, without a hidden inverse
Gram estimate or a suppressed logarithmic factor.

Pass only if both displayed estimates survive with the stated
absolute constants, or explicitly repaired absolute constants.
An unbounded omitted tail, endpoint error or extra factor that
invalidates the growing range is a failure to be preserved. Do
not audit density, the representer contour, second-order descent,
saturation or the original contraction in this attempt. If successful,
a canonical cited reproduction can be saved; it is local validation
of known source mathematics, not progress beyond the checked source.

L018 fixes the actual arithmetic setting; L728 is contextual and
supplies no mathematical estimate here. No cross-notebook input.
The possible downstream use is to separate two moment directions
from a controlled arithmetic observation before proposing a new
preconditioner. No estimate for the complementary residual or for
the prescribed dyadic update is assumed. Repeating the contraction
proposal requires materially new quantitative information.
Mathlib matching coverage not checked; no absence claim.
