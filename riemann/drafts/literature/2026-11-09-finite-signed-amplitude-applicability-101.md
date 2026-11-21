# Finite signed-amplitude applicability — completed source comparison

TARGET: Assess whether Majerski v2 Theorem 2.4 supplies an admissible finite-energy signed-amplitude certificate for L939 on 8<=E<=48 using audited L951, retaining every boundary contribution.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step102 reused assessment96's exact-object and signed-Laplace discovery and checked the scoped L938/L939/L951 stops; reopened the named primary theorem rather than repeating a general survey. Read L948(1),(4)-(5), C948a's conclusion and L949's hypotheses/conclusion only to identify a different continuation, not to test it.
SOURCE_EVIDENCE: Directly read Majerski arXiv:1511.00302v2, 11 April 2016, Theorems2.1/2.4, printed pp3-7,9-10: A1-A3, N1/N2, equations(7),(9),(17), local ellipsoid, actual-complement and amplitude proof cases; HTML confirmed the exact inequalities. Reused assessment96's other sources and inspected L939(4)-(18), L938(1)-(10), and audited L951's statement.
COMPARISON: The unchanged specialization d=11, Omega=D_r, f=z_r, g=g_r, n=pi exp(2r) fails N1 already at E=8: every contained ball has rho^2<2/33, so xi n<24/11, whereas N1 requires xi n>=11. L951's coercivity cannot remove this source onset condition. This excludes the direct full-interval import, not all signed estimates or larger-energy applications.
GAP: No actual-density sign, finite-energy signed allowance or effective infinite join is supplied. Quantitative amplitude and boundary estimates remain unresolved for other methods; a pointwise signed-response scope at E=8 requires its own source review.
REASON: The completed source-hypothesis comparison identifies a decisive excluded condition and parks the direct Majerski application on the requested closed interval. This is informative negative source evidence, not a new lemma, general Laplace theorem or result beyond the sources checked.
LITERATURE_REASON: Changed target from a scalar Taylor audit to a signed-amplitude theorem application with finite onset and all simplex boundaries; reuse adequate assessment96 evidence and inspect only essential missing theorem details.

## Original nomination, preserved; superseded by step102 below

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
This intermediate source question could enable a later pointwise lower
bound for the exact v(E) on [8,48]. Such a bound could remove part of
the outer negative mass in L949's units. It would leave E>48 and an
effective eventual-sign join, head/global variation, other signs and
degrees, contacts, initialization and realization unresolved. Even a
successful finite interval would not prove RH or pay the whole m-B.

Compare these three mechanisms, preserving their distinct evidence:

- Fixed negative-row Chernoff: L950's exact selected cost is over ten
  million times m-B. Do not tune its exponent or numerical precision.
- Global polynomial balancing: L940 refutes Schur-concavity; L941's
  recorded zero-superlevel obstruction also rules out the proposed
  global sign-set replacement. Neither is an obstruction to every
  signed integral estimate.
- Signed local amplitude expansion with an actual complement bound:
  assessment96 identifies Majerski's explicit-constant alternative.
  L951 supplies one previously missing localization input, but no
  finite-energy theorem admissibility or amplitude estimate. Select
  this independently testable scope, not a new name for either stop.

Use the saved primary-source inspection in
`drafts/literature/2026-11-09-signed-balanced-simplex-outer-budget-96.md`.
The precise lead is Majerski, *Simple error bounds for the multivariate
Laplace approximation under weak local assumptions*,
[arXiv:1511.00302v2](https://arxiv.org/pdf/1511.00302v2),
Theorem2.4 and its amplitude proof, relying on Theorem2.1's N1,N2
conditions and equation(17). Its exact finite admissibility must be
read before proposing a calculation; do not restart the general
Laplace literature survey. Katsevich's unspecified local constants
or L939's eventual o(1) cannot stand in for those conditions.

Essential inputs are L939's exact P, full q, g_r, z_r, H_r and domain,
L951's audited bound, and L938's retained normalization and factors.
L019/L058 are kernel/integrability background. L947/L949 provide the
later exact budget; L940/L941/L950 provide contrasts, not premises.
No cross-notebook input is proposed. Mathlib remains unchecked.

Continue only if the review identifies a precise admissible
specialization or one independently testable missing quantitative
hypothesis. A source exclusion at the lower energy must be recorded
as such, rather than hidden by changing E=8, dropping boundaries,
assuming positivity of the whole amplitude, or calling an unsigned
Gaussian tail the actual complement. If blocked, park that theorem
application and nominate a materially different test. This is not a
protected creative mechanism: no source-covered new central route
is established by this nomination.

## Completed comparison — 9 November 2026, step102

LITERATURE / NOVELTY_UNCHECKED / NEGATIVE. The new evidence is an
excluded quantitative hypothesis for the exact proposed source
specialization. No lemma, mathematical script, density bound or sign
is derived. PROOF and DAG do not change. The source comparison below
records its elementary substitutions fully so that a rounded preview
is not mistaken for evidence.

### Primary theorem and load-bearing cases

Piotr Majerski, *Simple error bounds for the multivariate Laplace
approximation under weak local assumptions*, arXiv:1511.00302v2,
11 April 2016: [PDF](https://arxiv.org/pdf/1511.00302v2),
[primary HTML](https://arxiv.org/html/1511.00302v2), Theorem2.1,
printed pp3-4, proof pp5-7; Theorem2.4 and its complete short proof,
pp9-10. The HTML disambiguates the PDF text's inequality symbols.
Use rho for the paper's radius r, and lambda_min for the smallest
Hessian eigenvalue; neither denotes L939's energy parameter r.

Theorem2.1 requires a measurable domain Omega in R^d, d>=2;
integrability of exp(-n f) for n>=n1; vanishing gradient, positive
Hessian and existing third partial derivatives at zero. A1 requires
a closed ball B_rho contained in Omega and constants C>0, alpha>1
such that, throughout that ball,

    |f(t)-d^2 f(0,t)/2-d^3 f(0,t)/6| <= C ||t||^(2+alpha).

A2 requires convexity on a contained B_delta, and f>=Delta>0 on
Omega outside B_min(delta,rho). Write

    D=(d^(3/2)/6) max_(i,j,k) |partial_(i,j,k) f(0)|,
    xi=min(rho^2 lambda_min,2 Delta).

The two explicit source onset conditions are

    N1: n>=1, d <= (d+2 alpha)log n <= xi n;
    N2: D ((d+2 alpha)/lambda_min)^(3/2) (log n)^(3/2)/sqrt(n)
        +C ((d+2 alpha)/lambda_min)^(1+alpha/2)
                    (log n)^(1+alpha/2)/n^(alpha/2) <= 7/4.

The displayed n0 is inf(N1 intersection N2). In the proof, equations
(7),(9) require these inequalities above the respective onsets.
The actual local ellipsoid is E_epsilon(H), where
epsilon^2=(d+2 alpha)log n/n. Equation(7) ensures its containment
in B_rho. The complement proof, equations(13)-(14), separately uses
the gap outside B_min(delta,rho) and convexity inside that ball.
Its final upper estimate retains I(n1), not just a Gaussian tail.
Remark2.2 permits changing the exponential Taylor constant behind
N2 at the cost of larger errors. It does not relax N1 or containment.

Theorem2.4 adds a measurable g with g(0)!=0, C^(1,1) regularity on
B_rho and a full quadratic amplitude remainder M||t||^2 there.
Besides n>=n0, equation(17) requires

    M(d+2 alpha)/lambda_min * log n/n
      + ||grad g(0)|| sqrt(d(d+2 alpha)/lambda_min)
                                  sqrt(log n/n) <= g(0).

The displayed equation therefore applies in our positive-saddle
case, not automatically to a negative g(0). The error constant K_ul
also retains the complete weighted absolute integral:

    K_ul = 7 sqrt(det H) exp(n3 xi/2)
             / (4 |g(0)| (2 pi)^(d/2))
             * integral_Omega exp(-n3 f(t)) |g(t)| dt.

The paper writes R^d after its domain convention; an application on
Omega must retain the same actual integral. Finiteness of J alone
is not substituted for this absolute-integrability requirement.

The short amplitude proof says equation(17) makes its Taylor brackets
nonnegative on B_rho. Its n-dependent bound controls the shrinking
ellipsoid through the radius estimate, not an arbitrary fixed ball.
No stronger fixed-ball conclusion is imported here. A future use
would have to justify the relevant local domain. We do not repair or
reprove the general theorem, and no success depends on that sentence.

### Exact comparison with L939 at the included endpoint

For the nominated direct application use L939's unchanged eleven
independent coordinates, Omega=D_r, f=z_r, g=g_r and
n=pi exp(2r), with r=sqrt(E/12). L951 supplies the unique minimum
on the full closed constrained simplex. L939(10),(14) give the
algebraic Hessian H=eta(I_11+J_11), eta=1-1/(2r); at r=sqrt(2/3)
this has lambda_min=eta in (0,1). The Hessian identity is evaluation
of the explicit phase at zero, not use of L939(13)'s r>=2 estimate.
The saddle amplitude is C_* q(r)^12>0, as in L939(5),(7),(18).

The excluded source hypothesis can be checked without numerical
exponentials, Taylor constants or theta truncation. At E=8:

    r^2=2/3, 1/2<r<1, n=pi exp(2r)<4 e^2<36.

Here only the standard coarse inequalities pi<4 and e<3 are used.
The point with all eleven independent coordinates equal to r/11
has y_12=-r, hence is outside the open D_r, and its squared
Euclidean norm is r^2/11. Since the paper defines B_rho as closed,
B_rho subset D_r requires rho^2<r^2/11=2/33. Consequently the
source parameters would satisfy

    xi n <= rho^2 lambda_min n < (2/33)*36=24/11 < 11=d.

But N1 requires d<=(d+2 alpha)log n<=xi n for every alpha>1.
Thus no choice of C,D,M,Delta,alpha or a smaller contained radius
can make this direct application admissible at E=8. In particular,
with its fixed phase parameters no n'<=n can belong to N1 either,
because xi n'<=xi n<d; using the printed infimum cannot evade the
failed onset. This is an exact source-hypothesis comparison, not a
numerical observation about v(8). It excludes the claimed certificate
on the full closed interval [8,48], which includes that endpoint.

The scope of this exclusion is deliberately narrow: the specified
Omega, phase, amplitude, coordinates and n are fixed. No theorem
about all nonlinear coordinates, phase reparametrizations or larger
energies is asserted. The measurable zero extension used in L939's
eventual argument does not provide C^(1,1) amplitude control on an
enlarged ball crossing the simplex faces. Such a new extension cannot
be silently supplied to this application. Restricting the energy
interval would leave the original lower endpoint unpaid.

### Independent obligations, stops and continuation

Within a strictly contained local ball the full expressions are
smooth. Quantitative C,D,M, local convexity radii, a useful Delta,
equation(17), a paid K_ul and a total relative error smaller than
the positive saddle are independent requirements. L939(8),(15)
prove qualitative full-theta/boundary integrability with positive beta
parameters; they do not supply the needed finite numerical signed
allowance. L951 does not turn its phase gap into amplitude positivity,
and an unsigned Gaussian tail cannot pay the actual complement.
No such constants or integrals were computed in this source turn.

Reused assessment96's discovery, rather than restarting it. Checked
the completed L951 audit/approval stop, the L940/L941 balancing
obstructions and L950's fixed-row stop at their existing scopes.
Read assessment87's complete signed-response coverage, assessment92's
Bernstein/beta scope, the direct-density notes68 and the coarse
endpoint stop69. The last fails at E=4 with a rowwise allowance;
it is not a refutation of every signed response or another energy.
L948(1),(4)-(5) provides a boundary-integrable pointwise response,
while C948a certifies an integrated error on [4,8]. L949 certifies
v_p>=0 there, not the pointwise actual v(8). No new endpoint sign
or pointwise norm follows from those integrated certificates.

Park this direct Majerski full-interval application. Nominate the
different, boundary-adapted pointwise signed-response question in
assessment102. It tests the lower endpoint before seeking interval
positivity: a certified negative v(8) would refute that sufficient
positive-tail claim from8, and a positive v(8) would remove only
one necessary obstacle. The new pointwise residual scope needs
separate review; no identity, error bound or calculation is approved
or performed here. Full/supporting Mathlib coverage remains unchecked.

The main mixed-positivity gap, signed outer mass, infinite join,
head/global variation, independent signs, contacts, other degrees,
initialization and realization remain open. No source-assessed new
central creative mechanism was identified in this bounded comparison;
the actual signed finite-error bridge remains the blocker. This
specialization must not be relabelled creative to meet a schedule.

Access note: the primary PDF and HTML were accessible through the
web tool. Screenshot returns supplied no usable image; shell curl
could not resolve arxiv.org and an optional ar5iv URL failed. These
are nonessential access failures, not a persistent source blocker:
the complete relevant primary statements and proof cases were read.
