# Corollary C034m: original-width observation dual injectivity

## Hypotheses

Retain exactly C033l's original probability laws and residual mu. In
particular, Z+ is the multiset of positive-ordinate nontrivial zeta
zeros, counted with multiplicity, z_rho=gamma_rho-i*delta_rho,
gamma_rho>14, |delta_rho|<1/2, and N(T)=O(T*log(T+2)). Set

    H(u)=sum_(rho in Z+) exp(-u*z_rho^2),
    u_sigma(t)=t/(1+4*sigma*t),
    ell_sigma(t)=H(u_sigma(t))/(t*sqrt(1+4*sigma*t)),
    B_sigma(s)=integral_0^infinity (1-exp(-s*t))*ell_sigma(t)dt,
    k_sigma(s)=exp(-B_sigma(s)), sigma,s>0.

C032j's exact heat transform identifies these expressions with the
original laws for every positive real sigma, with zero drift/killing.
Sigma is Gaussian half-variance. Retain the actual divisor/conjugation
and multiplicity conventions, excluded ordinate zero, strict strip,
counting, verified zeros through100 and retained real zero in (14,15),
reciprocal-square tail, heat positivity, separate fixed-j heat-error
qualifications through2, and both fixed-v1 preprint qualifications.
Neither those preprints nor their finite-zero data are independently
verified here. Only the j=0 small-time error is used below; no error
term is differentiated. No RH or positivity of the Gaussian profile
p_sigma is assumed.

Let S=[1,2] be the observation interval and W=[1,2] the original width
interval. Let h be an arbitrary finite real signed Borel measure on
S, with V=|h|(S)<infinity, and c a real number. Atoms, infinite support
and singular continuous parts are allowed, without a common bound on
V, any smoothness, or any restriction on sign changes. Assume

    integral_S k_sigma(s) dh(s)=c for every sigma in W.       (1)

The residual transform muhat is exactly C033l's probability transform:
its Levy measure is ell_1(t)dt restricted outside [1,3/2], with zero
drift/killing. It is not replaced by an approximation.

## Conclusion

Equation (1) forces h=0 and c=0. Consequently there are no h,c of the
stated class satisfying (1) and integral_S muhat(s)dh(s)!=c.

The proof supplies two quantitative qualitative inputs, with finite
constants that need not be effective: locally uniform complex-width
domination on Re sigma>0, |Im sigma|<Re sigma, and, uniformly for s in S,

    B_(q/4)(s)=a(s)*(log(q)-d)+E(q,s),
    a(s)=sqrt(s)/4, d=gamma_E+2*log(4*pi),
    sup_S |E(q,s)| <= C_E*(1+log(q))/sqrt(q), q>=q_0.        (2)

This is a qualified local result from attempt1887; conceptual audit1888
below passes under the retained inputs. Assessment1885/notes1886 found no matching theorem
among the sources inspected; POTENTIALLY_NEW is not a novelty claim.
Known analytic integration, identity, Cauchy and Laplace-uniqueness
theorems are imported, not presented as new discoveries.

The result excludes this continuous affine dual obstruction when width
variation is unrestricted. It does not produce finite signed width
approximants, a variation rate, nonnegative output, full odd cancellation,
moments, signed-height payment, actual-Xi realization or RH positivity.
It does not contradict C033j's exact all-Borel range exclusion, C034l's
fixed-cap separation or C034k's two-observation interpolation.

## Proof

### Source scope and why an additional argument is needed

Reuse the EXPLORE assessment1885 saved before this invocation, and its
complete source comparison in notes1886. For the heat transform import
Suvrit Sra, *Some positivity properties of Riemann Xi under smoothing*,
[2611.00345v1, 11 November 2026](https://hexagonmath.org/pdf/2611.00345v1),
Proposition3.1/(3.2)-(3.3), printed pp5-6, complete proof C.1, p21.
C032j checks the exact all-positive-width normalization.

For the heat sum and the j=0 error import Sra, *On some positivity
properties of the Riemann Xi function*,
[2610.00584v1, 20 October 2026](https://hexagonmath.org/pdf/2610.00584v1),
Lemma2.1, printed p4, and PropositionB.1/(B.2)-(B.3) with its proof,
printed p17. Precisely the j=0 estimate recorded in C032s is

    H(u)=A*u^(-1/2)*(log(1/u)-d)+r_0(u),
    |r_0(u)|<=C_0*log(1/u), 0<u<=u_0,
    A=1/(8*sqrt(pi)), d=gamma_E+2*log(4*pi).                (3)

Decrease u_0 so that u_0<=exp(-2). Constants in (3) are independent
of u. The source's separate derivative errors are not used to
differentiate (3). Its statement alone is not a uniform estimate for
B_sigma or a uniqueness theorem for the observation kernel.

For holomorphic parameter integration and the identity principle import
Friedrich Haslinger, *Complex Analysis*, undated author notes, version
inspected20 November2026,
[Theorems2.39 and2.15, printed pp67-68 and54](https://www.mat.univie.ac.at/~has/scriptneu.pdf).
Integration requires holomorphic sections and an integrable dominator
on each parameter disk; identity requires a connected open domain and
an interior accumulation point. All of these are checked below. Also
use the standard Cauchy integral theorem and Cauchy integral formula
on disks, and the standard Gaussian integral. These named general
theorems are not reproved.

For ordinary Laplace uniqueness import Ante Mimica, *Laplace transform*,
Dresden course27 April-1 May2015,
[Proposition1.8 and proof, printed pp9-10](https://web.math.pmf.unizg.hr/~amimica/lt.pdf).
It determines finite positive measures on [0,infinity) from their
positive-real transforms. Apply it only to finite positive Jordan parts.
No signed support theorem, perturbed-Laplace uniqueness theorem, PSD
kernel identity or scalar-span closure is imported or assumed.

### 1. Complex-width continuation with a common integrable majorant

Let D={sigma: Re sigma>0, |Im sigma|<Re sigma}. This sector is open
and connected and contains every positive real width. Use the principal
square root of 1+4*sigma*t; its real part before taking the root is
positive for sigma in D and t>0. Define the complex-width expressions
by the displayed heat formula, not by a complex probability law.

Fix a compact K contained in D, put alpha=min_K Re sigma>0 and
M=max_K |sigma|. For u=u_sigma(t)=v+i*w, direct calculation gives

    v=t*(1+4*t*Re sigma)/|1+4*sigma*t|^2>0,
    |w|/v=4*t*|Im sigma|/(1+4*t*Re sigma)<1.

For z=gamma-i*delta with gamma>14 and |delta|<1/2,

    Re(u*z^2)=v*(gamma^2-delta^2)+2*w*gamma*delta
      >=v*(gamma^2-1/4-gamma)>=v*gamma^2/2.                (4)

The last bound follows from gamma^2/2-gamma-1/4>0 for gamma>14.
Moreover,

    v>=t/(1+4*M)^2,               0<t<=1,
    v>=4*alpha/(1+4*M)^2,         t>=1.                  (5)

The counting input implies, for every fixed b>0,

    sum_rho exp(-b*t*gamma_rho^2)
       <=C_b*t^(-1/2)*(1+log(1/t)), 0<t<=1.             (6)

For completeness, extend the counting bound to all y>=0 by increasing
its constant; N(y)=0 near zero. Stieltjes integration by parts has
vanishing endpoints and writes the sum as
2*b*t*integral_0^infinity y*exp(-b*t*y^2)*N(y)dy. Bound N(y) by
C*y*log(y+2) and put x=sqrt(t)*y. The inequality
log(x/sqrt(t)+2)<=log(1/t)/2+log(x+2) proves (6), since both resulting
Gaussian integrals are finite. This also proves finiteness of the
fixed-time sums used for t>=1 and counts every multiplicity.

Combining (4)-(6) and |1+4*sigma*t|>=1+4*alpha*t gives a constant C_K
such that, uniformly on K,

    |ell_sigma(t)|<=C_K*t^(-3/2)*(1+log(1/t)), 0<t<=1,
    |ell_sigma(t)|<=C_K*t^(-3/2),               t>=1.

For real s in S, 0<=1-exp(-s*t)<=min(2*t,1). Thus the integrand of
B_sigma(s) has the common Lebesgue-integrable majorant

    2*C_K*t^(-1/2)*(1+log(1/t)), 0<t<=1,
    C_K*t^(-3/2),                t>=1.                  (7)

For fixed t, the heat series converges locally uniformly in sigma by
(4)-(6) and consists of holomorphic terms. Hence its sum and the
integrand of B are holomorphic in sigma. The cited parameter-integration
theorem and (7) make B_sigma(s) holomorphic on D for every s in S.
Dominated convergence also gives joint continuity in sigma,s and a
bound |B_sigma(s)|<=M_K' on K times S. Consequently k_sigma(s) is
jointly continuous there, holomorphic in sigma, and bounded by exp(M_K').

Apply the same integration theorem to each Jordan part of h, with the
finite measure |h| and that constant majorant. Therefore

    T_h(sigma)=integral_S k_sigma(s)dh(s)

is holomorphic on D. Agreement T_h=c on W has an accumulation point
inside D. The identity principle extends (1) to every sigma in D,
in particular every positive real width. This is a continuation of
the exact original family; no limit of approximate kernels was used.

### 2. A uniform large-width estimate, including the full remainder

For real q=4*sigma choose q>=q_0 with 1/q<=u_0. Put
u=t/(1+q*t), so 0<u<1/q, and K_H(u)=sqrt(u)*H(u). Equation (3) gives

    K_H(u)=A*(log(1/u)-d)+r(u),
    |r(u)|<=C_0*sqrt(u)*log(1/u).

The function sqrt(u)*log(1/u) is increasing on (0,exp(-2)]. Hence
|r(u)|<=C_0*log(q)/sqrt(q) for every t>0. Exactly,

    ell_(q/4)(t)=t^(-3/2)*K_H(t/(1+q*t)),
    log(1/u)=log(q)+log(1+1/(q*t)).                       (8)

Write w_s(t)=(1-exp(-s*t))*t^(-3/2). Integration by parts followed
by the Gaussian integral gives

    integral_0^infinity w_s(t)dt=2*sqrt(pi)*sqrt(s).       (9)

The boundary terms vanish: (1-exp(-s*t))/sqrt(t) tends to zero at
both endpoints. Thus all terms in the following exact decomposition
are absolutely integrable:

    B_(q/4)(s)=a(s)*(log(q)-d)+E(q,s),
    E(q,s)=A*integral_0^infinity w_s(t)*log(1+1/(q*t))dt
           +integral_0^infinity w_s(t)*r(t/(1+q*t))dt.    (10)

Here 2*sqrt(pi)*A=1/4, fixing the coefficient a(s)=sqrt(s)/4.
For the logarithmic correction, w_s(t)<=2*t^(-1/2), so t=y/q gives

    integral_0^infinity w_s(t)*log(1+1/(q*t))dt
      <=2*q^(-1/2)*integral_0^infinity
                       y^(-1/2)*log(1+1/y)dy
      <=(12+4*log(2))*q^(-1/2).                         (11)

Indeed, on (0,1] use log(1+1/y)<=log(2)+log(1/y), whose weighted
integral is 2*log(2)+4. On [1,infinity) use log(1+1/y)<=1/y, whose
weighted integral is2. This bound controls the moving small-t region
as well as the large-t tail; it is not pointwise asymptotics under an
unpaid integral. The second term of (10), by (9), has absolute value
at most 2*C_0*sqrt(2*pi)*log(q)/sqrt(q), uniformly in s. Equations
(10)-(11) prove (2).

Let y=log(q), a_-=1/4, a_+=sqrt(2)/4, and w(s)=exp(d*a(s)). The
function w is positive, continuous and bounded above and below on S.
Increasing y_0 if needed, (2) ensures sup_S|E(exp(y),s)|<=1 for
y>=y_0. The elementary inequality |exp(-E)-1|<=exp(|E|)*|E| now gives
the exact representation

    k_(exp(y)/4)(s)=w(s)*exp(-a(s)*y)*(1+R(y,s)),
    sup_S|R(y,s)|<=C_R*(1+y)*exp(-y/2), y>=y_0.          (12)

In particular k_(exp(y)/4) tends to zero uniformly on S. Since V is
finite and (1) holds for these positive widths, |c|<=V*sup_S|k| tends
to zero. Therefore c=0. This alone would not settle the target; the
following exact signed-transform argument is essential.

### 3. Signed error control and an exact Cauchy-transform recovery

Let nu be the pushforward of the finite signed measure w(s)dh(s)
under the homeomorphism a:S->[a_-,a_+]. It is finite, real, and
supported on [1/4,sqrt(2)/4]. Define for y>=0

    F(y)=integral_[a_-,a_+] exp(-a*y)dnu(a).

Using the extended equality T_h=0 and (12), for y>=y_0 we obtain
the exact identity and absolute signed bound

    F(y)=-integral_S w(s)*exp(-a(s)*y)*R(y,s)dh(s),
    |F(y)|<=C_R*max_S(w)*V*(1+y)*exp(-3*y/4).             (13)

No sign assumption or lower bound on the leading signed integral is
used. The decisive threshold is

    3/4 > sqrt(2)/4 = a_+.                              (14)

The error thus forces an ordinary transform to decay strictly faster
than the largest possible exponent on its entire support. Instead of
invoking an unassessed signed-support theorem, the next argument
recovers the transform by an explicit contour identity.

For Re z>-3/4 set

    J(z)=integral_0^infinity exp(-z*y)*F(y)dy.

On [0,y_0], F is bounded and continuous by its finite-measure definition.
On [y_0,infinity), (13) gives a common integrable majorant for every
compact subset of that half-plane. Thus the cited integration theorem
makes J holomorphic there. Separately define

    G(z)=integral_[a_-,a_+] 1/(z+a)dnu(a),
    z in C\[-a_+,-a_-].

Positive distance of each compact set from the segment and finite
|nu| justify holomorphy of G. For Re z>0, absolute Fubini is valid
because integral_0^infinity exp(-(Re z+a)*y)dy<=1/(Re z+a_-).
It gives the exact, not asymptotic, identity J(z)=G(z).

The open set {Re z>-3/4}\[-a_+,-a_-] is connected: the removed finite
segment lies strictly inside the half-plane and paths can pass around
either endpoint. The identity principle therefore gives J=G throughout
that set. In particular G has the holomorphic continuation J through
the entire negative support segment.

Take the counterclockwise circle C centered at -1/3 with radius1/4.
Its closed disk has Re z>=-7/12>-3/4. Since a_+<3/8, the negative
support lies inside [-3/8,-1/4], at distance at most1/12 from -1/3;
it is strictly inside C. For every tau>0, Cauchy's theorem gives

    0=integral_C exp(tau*z)*J(z)dz
     =integral_[a_-,a_+] [integral_C exp(tau*z)/(z+a)dz]dnu(a)
     =2*pi*i*integral_[a_-,a_+] exp(-tau*a)dnu(a).         (15)

The second equality uses J=G on C. Its Fubini exchange is absolute:
the circle has finite length, its distance from the negative support
is positive, its exponential factor is bounded, and |nu| is finite.
The last equality is Cauchy's integral formula, with every pole -a
strictly inside the circle. It includes atoms at either endpoint and
singular continuous measures without modification.

Equation (15) makes the ordinary Laplace transforms of nu's two finite
positive Jordan parts equal for every tau>0. Extend these parts by
zero to [0,infinity) and apply Mimica's Proposition1.8. They coincide,
so nu=0 as a Borel measure. No inversion display at zero is used.

Finally a is a Borel isomorphism and w is bounded away from zero.
For every Borel E in S, (w*h)(E)=nu(a(E))=0. Multiplication by the
bounded function 1/w gives h=0, and the earlier argument gives c=0.
The residual is a probability transform bounded by1 on S, so its
integral against h is zero and cannot differ from c. This proves the
stated answer to the original dual question under the retained inputs.

### Scope of the discriminating test

The signed remainder is controlled in total variation in (13), and
the continuation and contour identities are exact. This avoids the
invalid inference from leading asymptotic agreement alone. It is
independent of the parked finite dictionaries, inverse-cost mechanisms
and odd-kernel scalar-span recursion. No original width outside W is
added to an approximation class: widths beyond W are used solely by
analytic continuation of a hypothesized dual equation. No new zero-free
region, unsmoothed endpoint, sign for Xi, or proof of RH is supplied.
The remaining source qualifications and all independent realization,
cancellation, signed-height and all-degree positivity gaps stay open.

### Conceptual audit1888 — 20 November 2026

The proof was independently replayed in a fresh research invocation
under the unchanged EXPLORE assessment1885. This is a REPRODUCTION
audit, not a new injectivity theorem, new literature assessment or
source-wide validation. The exact target, arbitrary finite signed
measure class and original-law normalization have not changed.
Source notes1886 and the canonical input statements in C032j, C032s
and C033l supply the assessed tools; no unread uniqueness or support
theorem is needed. The following checks accept the claimed result
conditional on those inputs.

1. **Normalization and input strength.** C032j uses Gaussian variance
   2*sigma and identifies the original law at every positive real
   width with precisely H(t/(1+4*sigma*t))/sqrt(1+4*sigma*t).
   No additional factor from the two translates or conjugate zeros
   is introduced. C032s's imported j=0 estimate is the absolute
   remainder |H(u)-A*u^(-1/2)*(log(1/u)-d)|<=C_0*log(1/u),
   not merely a leading equivalent. This is the strength required
   in (10)-(13). Its j=1,2 estimates are not differentiated or used.
   Inherited finite-zero, tail, positivity and fixed-v1 assumptions
   remain qualifications, even where this argument needs less.

2. **Holomorphy before continuation.** For u=v+i*w the real part of
   u*(gamma-i*delta)^2 is v*(gamma^2-delta^2)+2*w*gamma*delta.
   The sector gives |w|<v, so the worst displacement subtracts at
   most v*(gamma+1/4); gamma>14 makes (4) valid. For t<=1 the
   denominator |1+4*sigma*t|^2 is at most (1+4*M)^2. For t>=1 it
   is at most t^2*(1+4*M)^2 while the numerator is at least
   4*alpha*t^2. These prove both bounds in (5) uniformly on K.
   The counting integral in (6) has zero boundary terms because
   N vanishes near zero and has polynomial-logarithmic growth at
   infinity. Gaussian decay then proves the required sums finite.
   The principal square root has no branch crossing, since
   Re(1+4*sigma*t)>1. The resulting majorants in (7) are integrable
   at both endpoints and uniform in s in [1,2]. Thus the heat
   summation, parameter integration, continuity and integration
   against each Jordan part of h are all licensed before the
   identity principle is used. W lies in the interior of connected
   D; no boundary uniqueness theorem or complex probability law
   is assumed.

3. **Full uniform remainder.** The identity
   ell_(q/4)(t)=t^(-3/2)*K_H(t/(1+q*t)) is exact. Once
   1/q<=u_0<=exp(-2), the monotonicity of sqrt(u)*log(1/u)
   controls r for every t>0, including t tending to zero with q.
   The integral in (9) gives 2*sqrt(pi)*sqrt(s), and therefore
   2*sqrt(pi)*A=1/4 as claimed. The logarithmic correction uses
   w_s(t)<=2*t^(-1/2) on the entire positive half-line. After
   t=y/q, its integral over y<=1 is bounded by 2*log(2)+4,
   and over y>=1 by2; the external factor2 gives exactly
   12+4*log(2). Its tail is integrable despite the coarse bound
   on w_s. The r term is bounded by its uniform supremum times
   (9), at most 2*C_0*sqrt(2*pi)*log(q)/sqrt(q). This proves the
   asserted integrated error without differentiating an error or
   interchanging an unpaid asymptotic with the time integral.

4. **Signed decay, not a sign assumption.** Choose y_0>=0 large
   enough that |E|<=1. Formula (12) is an exact definition of R,
   with its bound furnished by |exp(-E)-1|<=exp(|E|)*|E|.
   Uniform decay makes c=0 because V is finite. The pushforward
   nu has total variation at most max_S(w)*V. Equation (13)
   controls the absolute action of R by |h|; it does not lower
   bound a potentially canceling signed leading term. Its rate
   is a_-+1/2=3/4, strictly above a_+=sqrt(2)/4. There is no
   uniform-in-h constant requirement: each h has finite V.

5. **Exact transform and endpoint recovery.** F is bounded on
   [0,y_0], and its tail bound makes J absolutely convergent and
   holomorphic for Re z>-3/4. On Re z>0, the absolute Fubini
   integral is at most |nu|([a_-,a_+])/(Re z+a_-); hence J=G
   is exact there. The slit half-plane is connected and contains
   paths around both endpoints, so the identity principle applies
   on its entirety. The chosen contour disk is wholly in that
   half-plane, with its left edge -7/12 exceeding -3/4 by1/6.
   Every point of the negative support is at distance at most
   1/12 from the center -1/3; its distance from the circle is
   therefore at least1/6. This pays the contour Fubini bound
   uniformly in the support variable for every fixed tau>0.
   Cauchy's theorem applies to J throughout the disk, while
   Cauchy's formula for 1/(z+a) encloses each pole strictly.
   There is no omitted endpoint residue, half-atom convention or
   assumption that nu has a density. Thus (15) gives equality
   of the ordinary Laplace transforms of the finite positive
   Jordan parts for every tau>0. The cited Mimica uniqueness
   theorem applies on [0,infinity); no inversion formula at zero
   is used. Finally a is a Borel isomorphism and w has bounded
   reciprocal, so nu=0 implies h=0.

All direct mathematical inputs are still C032j, C032s and C033l;
the DAG requires no change. Other local results mentioned in this
file are contrasts, not hidden premises. No correction to the proof
or strengthening of its conclusion is required. The audited result
excludes the proposed affine continuous dual witness. It does not
establish a closure theorem or an approximating sequence in this
step. The numerical and inverse-cost stops1571/1576/1781/1782/1790/1792
and the separate odd-kernel warnings are unchanged. Actual-Xi
realization, signs, cancellation, moments and signed-height payment
remain independent open obligations. This is no RH candidate.

## Mathlib

Full matching coverage for this original-law observation-dual theorem
has not been checked and is unknown. Supporting holomorphic integration,
Cauchy, pushforward/Jordan and Laplace-uniqueness APIs were not assessed
in this step. Audit1888 verifies the displayed mathematical argument
under its imported assumptions. No formal verification or source-wide
verification of the fixed-v1 inputs is claimed.
