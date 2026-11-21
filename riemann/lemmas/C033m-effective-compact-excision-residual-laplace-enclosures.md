# Corollary C033m: effective compact-excision residual Laplace enclosures

## Hypotheses

Retain C033i's exact residual probability mu, obtained from the width-one
law nu_1 by removing the Levy measure on I=[1,3/2]. Thus

    ell_1(t)=H(t/(1+4*t))/(t*sqrt(1+4*t)),
    B_P(s)=integral_I (1-exp(-s*t))*ell_1(t) dt,
    B_R(s)=B_1(s)-B_P(s)>=0,
    Laplace(mu)(s)=exp(-B_R(s)), s>0.                    (1)

Use C032j's normalization of the full positive-ordinate divisor,
including conjugates and multiplicities, and its identity

    p_sigma(0)=H(1/(4*sigma))/sqrt(4*pi*sigma).

Use C032m's entire profiles and lifts, C032q's identification
B_1(w^2)=E_1(w)+O_1(w) for real w>0, and C032w's explicit finite
profile and primitive bounds (4),(6)-(13). Retain the zero-ordinate
exclusion, strip/counting, first-zero/tail, verified-height and heat
inputs, both fixed-v1 preprint qualifications, and Gaussian half-variance
convention of those results. This is not an independent source-wide
audit or a verification of finite zero data. No individual zero
coordinates, positivity of p_sigma on R, density or absence of a zero
atom is assumed. Drift and killing remain zero.

Fix rational s>0 and a rational absolute tolerance epsilon>0.

## Conclusion

There is an explicit ordered finite procedure producing rational q
in [0,1] with

    |q-Laplace(mu)(s)| <= 3*epsilon/4 < epsilon.         (2)

Consequently [max(0,q-3*epsilon/4),min(1,q+3*epsilon/4)] is a
rational enclosure. Every tail, compact quadrature, coefficient,
elementary-arithmetic and exponential error is included below. The
procedure uses finitely many prime powers and elementary evaluations,
without zero coordinates or an unspecified existential constant.

This is a local specialization of existing effective bounds, recorded
19 November 2026 under assessment1752; application audit1755 below
passes under the retained source qualifications. It asserts analytic
effectivity, not useful runtime, an executed numerical certificate or a
separating margin.
C032x's literal implementation cost stop is retained. Rational
separator stability, signed-width support bounds, continuum extrema,
coefficient-amplified separation, cancellation, moments and unsmoothed
Xi realization remain open. No RH candidate is asserted.

## Proof

### 1. Imported tools and exact rescaling

Reuse the ready SPECIALIZE assessment1752 and source-notes1752.
The general explicit formula used by C032w is Alain Connes, *Heat
Expansion and Zeta*, arXiv:2402.13082v1 (20 February 2024),
[Section 2, equations (4)-(9), printed p.4](https://alainconnes.org/wp-content/uploads/heat-zeta.pdf).
Only its identity over complex zeros is used, not an RH-dependent
spectral interpretation. Its Gaussian specialization and the effective
errors are already proved and audited in C032w; they are not reproved.
The profile-at-zero and smoothed-heat identities in C032j come from
Suvrit Sra, *Some positivity properties of Riemann Xi under smoothing*,
[fixed 2611.00345v1](https://hexagonmath.org/pdf/2611.00345v1),
Proposition 3.1 (3.2)-(3.3), pp.5-6, and the last sentence of the proof
of Theorem 4.1, p.9, with C032j's qualifications intact.

For real f in C^2([a,b]), import the composite midpoint estimate

    |integral_a^b f(t)dt - (b-a)/n * sum_j f(t_j)|
        <= (b-a)^3 * sup|f''|/(24*n^2),

where t_j are the n cell midpoints. The precise source is Erik Talvila
and Matthew Wiersma, *Simple derivation of basic quadrature formulas*,
[arXiv:1202.0249v1](https://arxiv.org/pdf/1202.0249v1), Section 1,
(1.1) and composite rule, p.2; Section 4 proof, p.8. Assessment1752
already covers its hypotheses and proof. We supply the application
bound below, rather than reprove the rule.

Set a(t)=1+1/(4*t). Direct substitution, with positive real square
roots, gives

    1/(4*a(t))=t/(1+4*t),
    ell_1(t)=sqrt(pi)*t^(-3/2)*p_{a(t)}(0).             (3)

Indeed sqrt(4*pi*a(t))/sqrt(1+4*t)=sqrt(pi/t), and the remaining
factor is 1/t. The factor 1/2 in the original two-translate profile
has already been included in C032j; no further divisor halving occurs.
The map a decreases from 5/4 to 7/6 on I. Its full closed range is
inside [1,2], so C032w's uniform errors apply at every quadrature
node and at both endpoints.

Define the real function

    f_s(t)=sqrt(pi)*(1-exp(-s*t))*t^(-3/2)*p_{a(t)}(0).

Then B_P(s)=integral_1^(3/2) f_s(t)dt. This is an integral of the
original absolutely continuous Levy restriction, including its endpoint
convention; it does not add endpoint atoms. The atom of mu at zero,
if any, remains included in (1).

### 2. Width derivatives and an explicit compact quadrature bound

Write F(sigma)=p_sigma(0). We first justify, rather than assume, the
width differentiations needed here. For v=z+/-z_rho,

    partial_sigma G_sigma(v)
      =[-1/(2*sigma)+v^2/(4*sigma^2)]G_sigma(v)
      =partial_z^2 G_sigma(v),
    partial_sigma^2 G_sigma(v)
      =[3/(4*sigma^2)-3*v^2/(4*sigma^3)
                              +v^4/(16*sigma^4)]G_sigma(v)
      =partial_z^4 G_sigma(v).

For |z|<=1, 1<=sigma<=2, gamma=Re(z_rho)>14 and
|Im(z_rho)|<1/2, a common bound for the Gaussian and these two
width derivatives is

    exp(9/16)/sqrt(4*pi)
      *[1+(gamma+2)^2+(gamma+2)^4]
      *exp(-(gamma-1)^2/8).

Here |v|<=gamma+2; the Gaussian bound is the one in C032m, and
the displayed derivative coefficients have absolute coefficients at
most one. The counting hypothesis makes this bound summable with
multiplicity: on dyadic ordinate intervals the count grows at most
geometrically times the interval index, while the Gaussian beats the
fixed fourth-degree polynomial. For the precise real-parameter tool,
import Jiří Lebl, *Basic Analysis: Introduction to Real Analysis*,
[Section 6.2.3, Theorem 6.2.10](https://www.jirka.org/ra/html/sec_liminter.html)
(author HTML, statement inspected in source-scope1754 on 19 November
2026). A sequence of C^1 real functions on a bounded interval, whose
derivatives converge uniformly and whose values converge at one point,
has a C^1 limit with the stated derivative. Apply this first to the real
and imaginary parts of the finite Gaussian partial sums as functions
of sigma on [1,2]. The displayed majorant gives uniform convergence
of both the sums and their first derivatives, hence in particular
convergence at sigma=3/2. Apply the theorem again to the partial sums
of first derivatives: their values at 3/2 converge, and their derivatives
(the sums of second width derivatives) converge uniformly by the same
majorant. Both resulting
derivatives are continuous, including on the closed subinterval a(I)
of (1,2). No complex-width holomorphy is used.

C032m already supplies locally uniform spatial holomorphy. Cauchy's
formula identifies its second and fourth spatial derivatives with the
termwise derivatives, which equal the displayed width derivatives.
Conjugation invariance of the full positive-ordinate multiset, with
multiplicity, makes F(sigma) real for real sigma; summability justifies
this pairing. Thus f_s is real, as required by the cited midpoint rule.
Consequently

    F'(sigma)=p_sigma''(0), F''(sigma)=p_sigma''''(0).

For an explicit constant, C032w(4) gives

    P_D=exp((D+1/2)^2/4)+1+(1+D^2/4)*exp(D)+1/2
                         +4*exp(D^2/2)+2+exp((D+5/2)^2/4),
    |F|<=P_0, |F'|<=2*P_1, |F''|<=24*P_1.             (4)

The last two estimates are Cauchy's formula on the spatial unit
circle, not complex-width bounds. Elementary e<3 and sqrt(e)<2
give P_0<21 and P_1<100: respectively bound the exponential terms
by 3,1,4,9 and by 3,15/4,8,81, keeping the other constants in P_D.

On I we have |a'|<=1/4 and |a''|<=1/2. For
h_s(t)=(1-exp(-s*t))*t^(-3/2), differentiation of this elementary
factor gives

    |h_s|<=1,
    |h_s'|<=s+3/2,
    |h_s''|<=s^2+3*s+15/4.

These use t>=1, s>0 and 0<=exp(-s*t)<=1; no unknown heat
derivative or differentiated asymptotic enters. The chain and product
rules applied to f_s=sqrt(pi)*h_s*(F composed with a) give

    |f_s''|<=sqrt(pi)*[(s^2+3*s+15/4)*P_0+(s+4)*P_1]
             < K_s := 42*s^2+326*s+1915/2.              (5)

For clarity, the coefficient of P_1 before simplification is
2*(s+3/2)*(1/4)*2 + (1/16)*24 + (1/2)*2 = s+4.
The rational K_s uses sqrt(pi)<2 and the preceding bounds. In
particular the required C^2 regularity and a fully numerical bound
hold on the complete closed interval.

For n>=1, put h=1/(2*n), t_j=1+(j-1/2)/(2*n), 1<=j<=n.
The imported midpoint rule now gives

    |B_P(s)-h*sum_j f_s(t_j)| <= K_s/(192*n^2).         (6)

### 3. Finite compact evaluation, including arithmetic

Use C032w(6)-(7) with D=0 to construct its exact finite expression
p_tilde_sigma(0), with a common error at most d for every sigma
in [1,2]. To specify all its allowances, write u for its small
archimedean cutoff (distinct from a(t)), A for its large cutoff,
N>=2 for its integer prime-power cutoff, and J for its quadrature:

    d_prime=exp(25/16-(log(N)-5/4)_+^2)/(2*pi*N),
    d_small=(u^2+u/2)/(2*pi),
    d_large=(exp(-A^2/2)/A+exp(-A))/pi,
    L=exp(A/2)/(2*u)*[4*A+1/2+2*(1/2+coth(u))],
    d_quad=L*(A-u)^2/(8*pi*J),
    d=d_prime+d_small+d_large+d_quad.                  (7)

Take 0<u<=1, A>=1 and J>=1. Every omitted prime power is included
in d_prime; the archimedean subtraction stays combined at its small
endpoint. These are imported bounds for the full divisor, not a finite
zero model. For any requested d_*>0, first choose integer N and A
to make their two errors <d_*/4 each, then a positive rational u
for d_small<d_*/4, and only then integer J for d_quad<d_*/4.
The explicit functions give finite choices. Certified rational upper
bounds and strict slack suffice when testing these inequalities.

Let f_tilde_s(t)=sqrt(pi)*h_s(t)*p_tilde_{a(t)}(0).
At the midpoint nodes the profile approximation contributes at most

    h*sum_j |f_s(t_j)-f_tilde_s(t_j)|
         <=sqrt(pi)*d/2 < d.                           (8)

Suppose each finite f_tilde_s(t_j) is evaluated to a rational y_j
with absolute error at most eta. The sum C_hat=h*sum_j y_j is
rational and can be accumulated exactly. Equations (6)-(8) give

    |B_P(s)-C_hat| <= K_s/(192*n^2)+d+eta/2.            (9)

All node arguments and widths are rational. The finite expressions
use exp, log, positive square roots, pi, gamma_E and rational
arithmetic. C032w(13) and its audit1575 give convergent elementary
enclosures, including explicit exp/log remainders, pi's alternating
series, and 0<H_m-log(m)-gamma_E<1/m. The denominator in the
archimedean term is exp(v)-exp(-v)>=2*v>=2*u>0; other denominators
are positive rational factors and square roots of positive quantities.
Interval refinement therefore eventually encloses every finite node
expression to any eta, even in the presence of cancellation. A
computable rational upper bound on each magnitude and positive lower
bound on each denominator can first be obtained by refinement; the
finite arithmetic error then tends to zero with its input intervals.
This uses the established elementary evaluator, not a generic
uncertified integration routine. No actual node evaluation is claimed.

For a desired compact error beta>0 choose n so that (6)<beta/3,
then choose (7) for d<beta/3, and node errors eta<=2*beta/3.
This proves (9)<=beta with an ordered finite procedure.

### 4. Full exponent and its coefficient arithmetic

For the given rational s>0 choose an integer M>=1 with M^2>=s,
and let w=sqrt(s)>0. By C032q, B_1(s)=E_1(w)+O_1(w).
Use C032w's construction at sigma=1 with T>=2*M+1. Its complete
analytic error for the sum is

    Delta_an=2*M^2*tau_M(T)
        +(2*M^2*T+2*pi*M)*d_B
        +2*M^2*T*d_K+2*pi*M*eta_K,                     (10)
    tau_M(T)=4*[10*(2+log(1+T))+P_M]/(3*T).

Here d_B is C032w(6)-(7)'s profile error on the larger disk
D=sqrt(T^2+1), not the D=0 error d of (7) above. For completeness,
with U=T^2, R=U+1, r=U/R and H=P_D+d_B, its explicit Taylor errors
are

    eta_K=H*r^(K+1)/(1-r),
    d_K=(H/R)*r^K*((K+1)-K*r)/(1-r)^2.

The full spatial tail is that of the original combined removable
quotient in C032w(8); no source summand is integrated separately to
infinity. Its convergence and every removable value were already
checked in C032w/audit1575.

To achieve full-exponent error beta, first choose integer T with
the first term of (10)<beta/5. Fix T and its disk, then select
C032w's N,A,u,J so that the second term is <beta/5. Fix these
parameters, then choose K so that the last two terms together are
<beta/5. Each step has the explicit convergent bounds above. In
particular increasing T does not leave earlier profile constants fixed.

Let c_k be the real coefficients in C032w(11), at width one. On
substitution w=sqrt(s), that finite formula is exactly

    E_hat=4*sum_(k=1)^K c_k*sum_(j=0)^(k-1)
       (-1)^j*T^(2*k-1-2*j)*s^(j+1)
                         /[(2*k-1-2*j)*(2*j+2)],
    O_hat=2*pi*sqrt(s)*sum_(k=0)^K c_k*(-1)^k*s^k/(2*k+1).
                                                               (11)

Thus no unknown modulus of continuity in sqrt(s) is needed. If c_k
is approximated by a rational c_hat_k with error epsilon_k, C032w(13)
bounds the resulting error by sum_k epsilon_k*W_k, where

    W_0=2*pi*M,
    W_k=4*sum_(j=0)^(k-1)
       T^(2*k-1-2*j)*M^(2*j+2)/[(2*k-1-2*j)*(2*j+2)]
                       +2*pi*M^(2*k+1)/(2*k+1), k>=1. (12)

Use 4 in place of pi to obtain positive rational majorants Wbar_k.
A common epsilon_k<=beta/(5*sum_k Wbar_k) makes this error at
most beta/5. C032w's coefficient evaluator supplies such rational
approximations from its finite elementary expression, however large
the amplification factors.

With these c_hat_k the expression for E_hat in (11) is rational.
Let S_hat=sum_k c_hat_k*(-1)^k*s^k/(2*k+1), also rational. Enclose
2*pi*sqrt(s) by a rational approximation with error at most
beta/[5*(1+|S_hat|)]; positive square-root bisection and the cited
pi enclosures do so. Multiplication by S_hat then costs at most
beta/5; all remaining rational arithmetic is exact. The resulting
rational B_hat satisfies

    |B_1(s)-B_hat| <= beta.                             (13)

This explicitly accounts for all five error budgets. It proves
finite termination for each fixed s,beta, without a useful complexity
claim. It does not run the literal implementation stopped by C032x.

### 5. Residual and final exponential error

Apply Sections 3 and 4 with beta=epsilon/4. Put r_hat=B_hat-C_hat.
By (1), (9) and (13),

    |B_R(s)-r_hat| <= epsilon/2, B_R(s)>=0.

Set r_+=max(0,r_hat). Projection onto [0,infinity) cannot increase
distance from the nonnegative B_R(s): if r_hat<0, that distance is
reduced from B_R(s)-r_hat to B_R(s); otherwise it is unchanged.
For nonnegative x,y, the fundamental theorem of calculus gives

    |exp(-x)-exp(-y)| <= |x-y|,

because exp(-t)<=1 on their joining interval. Hence

    |exp(-r_+)-Laplace(mu)(s)| <= epsilon/2.             (14)

Evaluate exp(-r_+) to a rational q_0 with error at most epsilon/4
using the same convergent elementary enclosures. Finally project q_0
onto [0,1] to get rational q. The true transform belongs to [0,1]
by C033i's probability-law identification, so this second projection
also cannot increase its error. Equations (14) and the final
arithmetic error give (2).

The use of nonnegativity here concerns B_R, the exponent of the
already established positive residual law. It assumes neither a
positive width representation nor all-degree Xi signs. Subtracting
B_P from B_1 may lose relative accuracy, but both are computed to
explicit absolute tolerances and no unbounded exponential amplification
is needed. C033j's additional C032s assumptions are needed if one
invokes the separate range exclusion; that exclusion is not used in
this evaluator. All other inherited source qualifications remain.
This completes only the approved compact-excision evaluation interface.

### Application audit1755, 19 November 2026

Verdict: (1)-(14) pass the conceptual application audit under unchanged
SPECIALIZE assessment1753, separately approved1754. The real-width
differentiation theorem and its two applications are now explicit in
Section 2. No bound, hypothesis, conclusion or mathematical input ID
has changed. This validates the local specialization of the imported
tools, not a new general theorem, an executed certificate, or the
source-wide correctness of either fixed-v1 preprint.

1. **Normalization, reality and closed domain.** Substitution gives
   4*a(t)=(1+4*t)/t, hence (3) with exactly sqrt(pi)*t^(-3/2).
   The half-sum of the two Gaussian translates has already accounted
   for their factor two. The image of the whole closed I is
   [7/6,5/4], inside (1,2). Conjugate pairing makes F and f_s real.
   Neither the restricted Levy integral nor its quadrature adds an
   endpoint atom; the probability's possible atom at zero stays in
   the transform. C033i supplies finite B_P, finite B_R and B_R>=0
   by restriction of the positive Levy measure, not by subtracting
   infinite total masses.

2. **Both width derivatives and constants.** Each finite Gaussian sum
   is C^2 in real width. On the spatial unit disk, |v|<=gamma+2 and
   |Re(v)|>=gamma-1, while |Im(v)|<=3/2. The Gaussian prefactor and
   exponent therefore give exactly the majorant in Section 2; the
   derivative polynomial coefficients are bounded in modulus by one
   for 1<=sigma<=2. On the nth dyadic ordinate interval the count is
   O(2^n*(n+1)), the fourth-degree factor is O(2^(4*n)), and the
   Gaussian is at most exp(-c*4^n) for some c>0. The resulting series
   converges. This checks Lebl's uniform-derivative and pointwise-value
   hypotheses at each of the two applications, separately for real
   and imaginary parts. This qualitative counting constant is used
   only for differentiation; the effective derivative bounds come
   from C032w's explicit P_D and spatial Cauchy estimates.

   In particular P_0<3+1+1+1/2+4+2+9=41/2<21 and
   P_1<3+1+15/4+1/2+8+2+81=397/4<100. Cauchy's factorials
   are 2 and 24, not width-derivative factorials. Using
   a'=-1/(4*t^2), a''=1/(2*t^3), the product/chain rule yields
   the coefficient s+4 of P_1 in (5). Its rational upper bound is
   2*[21*(s^2+3*s+15/4)+100*(s+4)]=K_s. The midpoint length
   is 1/2, so its cubic-length remainder is K_s/(192*n^2).

3. **Independent compact approximation and arithmetic.** Substituting
   D=0 in C032w(6)-(7) gives all four terms of (7), including b=5/2
   in its prime tail and the lower endpoint in its quadrature error.
   Here A>=1 suffices; the larger primitive disk below has its own
   cutoffs. With N,A fixed first, then u and then J, every term tends
   below its allotted positive tolerance. The node weights sum to
   1/2 and |h_s|<=1, giving sqrt(pi)*d/2<d and eta/2 exactly.
   The beta/3, beta/3, beta/3 allocations cover (9). Finite-node
   denominators are bounded away from zero at the chosen cutoffs,
   so refining the cited elementary intervals pays cancellation in
   absolute error; positivity of the finite profile is not required.

4. **Primitive disk, ordered limits and coefficient amplification.**
   Summing C032w(12) gives exactly (10). Choose M and then T; the
   compact profile disk is D=sqrt(T^2+1), with C032w's requirement
   A>=max(1,2*D). Its d_B is independent of the D=0 compact error.
   Freeze T and all profile parameters before increasing K. Then
   H is finite, 0<r<1, and eta_K and d_K tend to zero, including
   the K*r^K factor. The imported combined quotient includes its
   removable values; no prime term is integrated separately to
   infinity. Every cutoff inequality can be tested by certified
   rational upper bounds with strict slack. If needed, fix a rational
   upper bound for D before the profile cutoffs, and one for H after
   those cutoffs and before K. Refinement and increasing integer
   cutoffs terminate since the displayed bounds tend to zero.

   In (11), w^(2*j+2)=s^(j+1) and w^(2*k+1)=sqrt(s)*s^k.
   Thus even powers need no approximate square-root substitution.
   Since M,T are integers, replacing pi by 4 makes every Wbar_k
   positive rational; the finite sum includes Wbar_0>0. The common
   coefficient allowance pays their entire amplified error. The
   final factor error multiplies the computed rational S_hat, so
   its allowance beta/[5*(1+|S_hat|)] pays that product without an
   omitted cross term: coefficient error was first measured using
   the exact factor. Tail, profile, Taylor, coefficient and final
   arithmetic errors are each at most beta/5. Hence (13) follows.

5. **Residual and final projections.** The two exponent evaluations
   with beta=epsilon/4 cost at most epsilon/2 in their difference.
   Projection onto the nonnegative half-line is valid because the
   exact residual exponent is nonnegative. The exponential is
   1-Lipschitz on that half-line. Its final epsilon/4 allowance,
   followed by projection onto [0,1], proves 3*epsilon/4<epsilon.
   Subtraction may be ill-conditioned in relative error but creates
   no unbudgeted absolute error. The reasoning never assumes that
   mu is a signed width mixture, or that p_sigma is positive on R.

All stated qualifications, zero atoms and zero drift/killing remain.
C033j/C032s are not inputs to this evaluator; their extra assumptions
are needed for the separate exclusion/separation route. Stop1576 still
rules out the literal implementation at its recorded cost, and stop1571
still concerns its different independent boxes. No rational separator
stability, continuum optimization, witnessed gap, uncapped result,
odd cancellation, moments or actual-Xi realization has been certified.
The direct mathematical inputs remain C032j/m/q/w and C033i; the DAG
needs no change. No numerical computation was required for this audit.

## Mathlib

Full matching coverage of this residual evaluator has not been checked
and is unknown. No Mathlib theorem is asserted to implement C032w's
explicit formula, the qualified smoothed laws, or this error procedure.
Supporting integration, derivative and elementary-function APIs have
not been independently assessed in this step. The cited primary
results and the local estimates above are the mathematical inputs.
