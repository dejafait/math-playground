# Signed bulk kernel asymptotics — completed source comparison

TARGET: Review primary-source coverage for a uniform signed bulk asymptotic of C997s's complete kernel on I=[7/4,9/4], at z_star and the full band, retaining both windows and all endpoint terms.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step406 searched growing-argument uniform Laguerre/Plancherel-Rotach asymptotics, Frenzen-Wong remainders, Szego's bulk theorem, and short-interval Fourier/complete-cosh-kernel terminology; screened the named local 11-November assessments, review305, spectral-tail341 and paid-leakage372. The inspected sources supply signed pointwise bulk expansions, not this notebook's complete integrated approximation objective; no novelty claim follows from the search.
SOURCE_EVIDENCE: M. Vanlessen, arXiv:math/0504604v2 (29 August2005), Section1/(1.1)-(1.2), Theorem2.4(b)/(2.13), Remarks2.5-2.7, Theorem3.32/(3.110), and Section5.2 Proposition5.1/(5.5)-(5.6), PDF pp1,3-7,34,37-39; primary statement and relevant bulk/remainder proof read. DLMF18.3 Table18.3.1 and 18.15.14-20 inspected for normalization/scaling. Dunster-Gil-Segura arXiv1705.01190v1, Case2 and (5.3)-(5.17), inspected as a domain comparison; (5.11) expressly excludes the oscillatory interval.
COMPARISON: Vanlessen supplies the needed signed growing-argument resource with an additive uniform algebraic error, including zeros of the leading cosine. Laguerre's argument t stays real in BOTH windows; z_star enters only exp(izt). The remaining specialization is normalization and finite-window integration with endpoints and subtraction intact. C999c and C997x/y/z remain stops on their own scopes; no source supplies the capped E_n exponential rate.
GAP: No complete-kernel expansion, numerical error constant, effective onset, derivative bound for a remainder, growing-truncation estimate, band representer or E_n bound has been established here. Fixed-order algebraic error at the bulk envelope must still be paid after the original exp(sqrt(n)) cap; it is not an exponentially small integrated residual.
REASON: The essential source gate is resolved by an accessible primary signed bulk theorem, rather than by the fixed-argument formula or an off-bulk exponential branch. Only a bounded known-theorem specialization is source-covered; its newly written continuation assessment requires separate next-turn approval before mathematics.
LITERATURE_REASON: Startup review405 was REVIEW_REQUIRED: no growing-argument primary theorem had been inspected for this changed signed-kernel target. This turn fills that essential gap and does not repeat literature on an already ready target.
SCOPE: Original integer n>=64, C997s's K_(n+2), g_n, I, z_star=1+i/8, full closed band [15/8,17/8], grid gamma_j and cap exp(sqrt(n)); both beta terms, the moving upper window, the fixed lower window and K's constant subtraction remain in the kernel.

## Main gap and intermediate purpose

The nomination below is preserved as the pre-review question. The completed
comparison in step406 at the end resolves its missing-source language,
without asserting the proposed expansion.

L030-L032/C032a actual-Xi positivity, L966/L968 forcing and L984(H)
remain unpaid. The point-bridge objective E_n in C997s is also open.
The proposed intermediate resource is a uniform signed asymptotic of
the actual kernel, resolving its oscillatory contributions and retaining
every endpoint term with a rigorous absolute remainder. This could
identify cancellation available to a later integrated primal or dual
construction, after C999c rules out the stronger Delta_n approach.

Such an expansion alone would NOT establish E_n=O(exp(-n/64)) or a
contradictory lower rate. An algebraic relative error at a large
exponential envelope is not an exponentially small residual. Any later
use must pay that remainder after the original coefficient cap and
all combinations, and justify possible cancellation among leading
terms. Relative error at a zero of a leading expression is not an
acceptable substitute for an absolute uniform estimate.

## Recovery comparison: three mechanisms

1. Exact centered-moment recovery or generic scalar propagation:
   C997z and C997y already give audited costs above the needed rate.
   No changed hypothesis or new norm estimate is proposed; park them.
2. More degrees or iterations of the two paid-leakage atomic generators:
   the canonical C997s evidence and attempt372 already record the
   candidate-specific failures. No new analytic input justifies that
   repetition; park it without claiming a global dual obstruction.
3. Signed complete-kernel bulk asymptotics: selected for source review.
   This uses the actual Laguerre oscillations on the physical slope
   interval, rather than the absolute spectral-window envelope, a
   germ near c=0, or a numerical optimization sequence. The requested
   quantitative description is independently testable and is not a
   theorem of existence for a band representer.

The previously inspected moving-window adjoint sources in review361
are only comparisons: their conditional range identities and uniqueness
statements do not supply this bulk expansion. No new adjoint construction
is proposed or derived here. Existing endpoint-chain and spectral stops
remain preserved, with no claim to have globally excluded those routes.

## One bounded source test

Locate primary uniform Laguerre asymptotic statements, inspect their
degree/argument scaling, parameter alpha, phase convention, uniform
domain and remainder, and read the proof cases needed for the original
moving windows. Fixed-argument asymptotics must not be substituted for
arguments proportional to n. Check applicability to alpha=2 and degree
n+1 before any specialization. Check whether finite short-window
integration against exp(izt) can be justified uniformly for both the
target and full closed band by the inspected remainder. Retain both
cosh terms, the lower window and constant subtraction explicitly.

Continue only if the inspected sources cover a concrete complete-kernel
expansion with a clearly stated absolute error envelope, or leave a
specific covered specialization to test later. Record a changed target
for separate approval if necessary. If only fixed-argument, pointwise,
unsigned-envelope or unquantified asymptotics are available, record that
precise mismatch and park the dependent test; do not repeat access
attempts or approve an invented remainder. No expansion is derived now.

Essential local input for this proposed work is C997c's complete
spectral representation and C997s's kernel. C999c is a route comparison.
E_n, C997a(8), selected/both-sign transfer, reconstruction,
complements/regulators, L993, L984(H), forcing and Xi signs stay open.
No cross-notebook input. Full matching Mathlib coverage is unchecked.

## Completed comparison — step406, 11 November 2026

### Primary signed bulk input

M. Vanlessen, *Strong asymptotics of Laguerre-type orthogonal polynomials
and applications in random matrix theory*,
[arXiv:math/0504604v2, 29 August 2005](https://arxiv.org/pdf/math/0504604v2),
Theorem2.4(b), equation(2.13), PDF pp5-6; definitions in Section1 and
Section2, PDF pp1,3-5; Remarks2.5-2.7, PDF pp6-7. The accessible
[HTML version](https://arxiv.org/html/math/0504604v2) was also inspected.
Use the degree symbol N here, to avoid confusing the source's degree
with the notebook's n or its spatial variable with the frequency z.

The source assumes the orthonormal polynomial p_N with POSITIVE leading
coefficient for w(t)=t^alpha exp(-Q(t)) on [0,infinity), alpha>-1,
Q a real polynomial with positive leading coefficient. Its MRS scaling
beta_N is defined by(2.1). For fixed sufficiently small delta>0 it gives,
uniformly in the closed bulk region B_delta in the upper half-plane,

    p_N(beta_N x)
      =(beta_N x)^(-alpha/2) exp(Q(beta_N x)/2)
        *sqrt(2/(pi beta_N))*[x(1-x)]^(-1/4)
        *[cos(theta_1,N(x))*(1+O(1/N))
                         +cos(theta_2,N(x))*O(1/N)],
    theta_1,N(x)=(alpha+1)/2*arccos(2x-1)
                    -pi N integral_1^x psi_N(s)ds-pi/4,
    theta_2,N(x)=(alpha-1)/2*arccos(2x-1)
                    -pi N integral_1^x psi_N(s)ds-pi/4,
    psi_N(x)=(1/(2pi i))*sqrt(x-1)/sqrt(x)*h_N(x).

This is a transcription of the SOURCE contract, not a new kernel lemma.
The two order terms are separate scalar errors; replacing their sum by
a relative error multiplying only the first cosine would lose coverage
at its zeros. All powers use principal branches. On the real interval
(0,1), Remark2.5 prescribes limiting values from above; psi_N,+ is the
real equilibrium density in(2.3), and arccos(2x-1) is real in(0,pi).
Uniformity in delta is on compact subsets of(0,delta_0), and in x on
the stated region. The degree tends to infinity; the source does not
claim an effective onset of 64 or a numerical error constant.

Read the relevant proof, Section5.2, Proposition5.1 and(5.5)-(5.6),
PDF p39, together with the normalization(5.1), PDF p38. Formula(5.6)
keeps the TWO cosines as the components of a vector multiplied by the
error matrix R. Theorem3.32, PDF p34, gives R=Id+O(1/N) uniformly, with
bounded analytic coefficient functions off the specified contours.
The preceding small-norm argument(3.108)-(3.109) gives its source of
uniformity. This explains why the error is additive in the bulk, rather
than an inference of small relative error at an oscillatory zero.
No reproduction of the Riemann-Hilbert argument is needed. Higher
fixed-order asymptotic expansions are stated, but neither the theorem
nor the passages read provide constants uniform in a truncation order
that grows with N. No such use is covered.

### Applicability screen, not a kernel derivation

The intended parameters are Q(t)=t, alpha=2, degree N=n+1. These meet
the source hypotheses. Remarks2.3/2.7/3.5 supply the monomial scaling;
the resulting MRS scale is 4N. The combined physical windows of C997s
lie in [n,9(n+2)/4]. For n>=64 their rescaled arguments t/(4N) lie in
the fixed compact bulk interval [1/5,3/5], so they stay away from the
hard and soft edges and fit B_delta for a sufficiently small FIXED
delta<delta_0. This is only a hypothesis check for the chosen theorem;
no transformed kernel estimate is asserted.

[DLMF Table18.3.1](https://dlmf.nist.gov/18.3#T1), Laguerre row, gives
the squared norm Gamma(N+alpha+1)/N! and leading coefficient
(-1)^N/N!. The later specialization must use both the norm and this
sign when translating the positive-leading orthonormal p_N to L_N^(2).
It must then retain C997s's division by n+1 and exact constant -1.
This normalization step is needed; claiming p_N=L_N^(2) would be wrong.

The spatial variable is real in BOTH original windows even for
z=z_star. The frequency set is the compact union
{1+i/8} union [15/8,17/8]. The extra exp(izt) therefore requires
tracking a known finite exponential weight, not analytically extending
the Laguerre argument off the real bulk. Finite interval integration
is the elementary operation still to be performed; no infinite limit
interchange, differentiation of the source error, or contour shift is
licensed. Both endpoints of each window, both beta terms from cosh,
and the constant-subtraction integral must remain explicit.

### Alternative sources and exact limitations

[DLMF18.15.14-16](https://dlmf.nist.gov/18.15#iv) are uniform only on
fixed compact intervals of the UNscaled argument. They are unsuitable
for t proportional to n. In contrast(18.15.17)-(18.15.20) use
nu=4N+2alpha+2, t=nu x, and are uniform for 0<=x<=1-delta. Formula
(18.15.19) retains J_alpha and J_(alpha+1) with an ENVELOPE remainder,
not relative error at Bessel zeros. These passages were inspected and
corroborate the scaling distinction, but Vanlessen is the accessible
primary theorem chosen for the continuation; the MRS scale 4N must
not be silently replaced by DLMF's nu in the source phase.

Frenzen-Wong, SIAM J. Math. Anal.19(5)(1988),1232-1248,
[DOI10.1137/0519087](https://doi.org/10.1137/0519087), was checked at
the publisher page; its requested PDF redirected to abstract/access
information. Its theorem/proof was NOT obtained and is not imported.
The large Szego fourth-edition PDF at Ohio State exceeded the web
reader's size limit; a search extract identifies Theorem8.22.8(a),
(8.22.9), p200, but neither this extract nor model memory counts as
an inspected proof. Those access issues are nonessential because the
Vanlessen statement and relevant proof are accessible; do not loop
on access attempts.

Dunster-Gil-Segura, *Uniform asymptotic expansions for Laguerre
polynomials and related confluent hypergeometric functions*,
[arXiv:1705.01190v1](https://arxiv.org/pdf/1705.01190v1), Case2 in
Section1 and Section5,(5.3)-(5.17), was inspected as a stronger-domain
comparison. The exponential L-G formula(5.11) EXCLUDES the oscillatory
interval between its turning points; its Airy formula(5.12)-(5.17)
has a different domain. No single exponential branch from(5.11) is
an alternative signed bulk formula. The Airy method is unnecessary for
the present compact interior, and its numerical tests are not imported
as error certificates.

### Search record and route decision

Queries included `Laguerre polynomials uniform asymptotic complex plane
bulk remainder Frenzen Wong 1988`; `Szego Orthogonal polynomials pdf
Theorem 8.22.9 Laguerre`; `Frenzen Wong 1988 Laguerre pdf 1232 1248
uniform`; `Laguerre short interval Fourier asymptotic`; and `Laguerre
cosh complete kernel asymptotic`. The initially guessed theorem number
8.22.9 is an equation number: Vanlessen Remark2.6 identifies Szego's
THEOREM as8.22.8. Search-only snippets and unrelated hits were not used
as mathematical inputs. No exact integrated-kernel or capped-band
approximation theorem was identified among the inspected sources;
this is a bounded overlap assessment, not an originality assertion.

Local C997c(1),(4)-(6) and C997s's complete hypotheses/(2) were read.
Named stops341/372 and review361 preserve the spectral-tail, finite
generator and conditional-adjoint limitations; review305 concerns a
different arithmetic short-shift square, not this physical-window
kernel. C997x/y/z and C999c remain the scope comparisons recorded in
the supplied nomination. None is reopened or globally strengthened.

Decision: SPECIALIZE, with only the bounded leading signed formula and
its absolute error admitted as a proposed next mathematical test.
The source makes fixed-order ALGEBRAIC bulk errors available, not the
exponential precision required by E_n=O(exp(-n/64)) after the original
coefficient cap. The later test must display that difference rather
than label a large-envelope asymptotic an E_n certificate. Continue
with a cancellation construction only if its complete error is paid;
otherwise park that consequence unless a materially new quantitative
mechanism is supplied. The expansion can still be a useful intermediate
resource without solving E_n or actual-Xi positivity.

No new lemma, kernel expansion, mathematical script, candidate solution
or change to PROOF/DAG is made in this literature-only step. Matching
Mathlib coverage remains unchecked, including the full bulk theorem;
unknown availability is not absence. The newly saved bounded
specialization assessment is subject to separate next-turn approval.
