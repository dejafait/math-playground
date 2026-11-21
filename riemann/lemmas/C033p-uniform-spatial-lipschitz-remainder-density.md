# Corollary C033p: a parameterized uniform spatial Lipschitz bound

## Hypotheses

Retain C033j's family and all C032j/C032s external-input qualifications.
The actual positive-ordinate nontrivial zeta divisor is counted with
multiplicity, z_rho=gamma_rho-i*(beta_rho-1/2), with conjugate pairing,
excluded ordinate zero, |beta_rho-1/2|<1/2 and gamma_rho>14. Retain
the cited counting, through-height-100 real-zero verification,
retained first real zero in (14,15), reciprocal-square tail and heat
inputs. Both fixed-v1 preprints and the finite-zero data remain
external inputs, not independently certified here. Sigma denotes
Gaussian half-variance. Put W=[1,2] and, for u,t>0,

    H(u)=sum_(rho in Z+) exp(-u*z_rho^2),
    K(u)=sqrt(u)*H(u),  u_sigma(t)=t/(1+4*sigma*t),
    ell_sigma(t)=t^(-3/2)*K(u_sigma(t)),
    D_sigma(t)=ell_sigma(t)-ell_1(t),
    Q_sigma(dt)=D_sigma(t)dt,  M_sigma=integral_0^infinity D_sigma(t)dt.

C033j supplies the finite real signed measures and their continuous
density representatives away from zero:

    R_sigma=exp(-M_sigma)*sum_(n=0)^infinity Q_sigma^{*n}/n!
           =exp(-M_sigma)*delta_0+r_sigma(x)dx,
    r_sigma(x)=exp(-M_sigma)*sum_(n=1)^infinity d_(sigma,n)(x)/n!,
    d_(sigma,n)=D_sigma^{*n} on the positive half-line.

Use the separately controlled heat errors through fixed order j=2
specified below, in addition to C033j's j=0,1 inputs. No differentiated
asymptotic remainder, sign of D_sigma, moment condition, width measure,
full cancellation J_eta=0, inverse stability or Xi realization is assumed.

## Conclusion

There is an explicit finite formula in specified, generally
nonnumerical heat constants and compact suprema for a common Lipschitz
constant L. With B1,B2 defined in the proof, put

    C=4*B1,  E=10*B1+4*B2,  K_mass=2*pi*B1,
    S=sqrt(5*pi/4),  z=C*S,
    L=(32/9)*S*(C+E)*exp(K_mass+z).                     (1)

Then for every sigma in [1,2] and x,y in [3/4,5/4],

    |r_sigma(x)-r_sigma(y)|<=L*|x-y|.                  (2)

The proof constructs a jointly continuous spatial derivative on
W times (1/2,3/2) and bounds its absolute value on W times
[3/4,5/4] by L. The zero atom exp(-M_sigma)delta_0 remains present;
(2) concerns only the density representative on the stated interval.

This is a local regularity specialization under the qualified inputs,
not a computable numerical modulus: heat constants/onsets and compact
suprema have no numerical certificates here. It pays one prerequisite
for possible finite-sample jump resolution, not signed tail errors,
inverse or coefficient costs, finite separator data, a margin/runtime,
unrestricted width variation, moments, cancellation or actual-Xi signs.
The local proof passes the separate conceptual audit1768 below, under
the unchanged external-input qualifications.
Assessment1764 found no matching uniform estimate in the sources
checked; that does not certify originality or progress beyond all
existing literature. No claim toward a complete RH argument follows.

## Proof

### Imported results and the precise additional estimate

Use the unchanged SPECIALIZE assessment1764, separately approved in
recovery1765, and its source-notes1764/1740. The exact Gaussian formula
is Suvrit Sra, *Some positivity properties of Riemann Xi under
smoothing*, [2611.00345v1, 11 November 2026](https://hexagonmath.org/pdf/2611.00345v1),
Proposition 3.1/(3.2)-(3.3), pp.5-6, complete proof C.1, p.21.
The zero normalization and half-variance match C032j exactly. We
import the formula, not a new Gaussian computation or a limit at sigma=0.

For heat convergence and estimates import Sra, *On some positivity
properties of the Riemann Xi function*,
[2610.00584v1, 20 October 2026](https://hexagonmath.org/pdf/2610.00584v1),
Section 2.1/(2.1)-(2.3), p.3, Lemma 2.1 and proof, p.4, and
Proposition B.1 and its proof, p.17. Fixed heat derivatives converge
locally absolutely on Re u>0. The proof of B.1 separately bounds the
counting error at each fixed j by O(u^(-j)*log(1/u)), and the complex
displacement error by O(u^(1/2-j)*log(1/u)). The approved coverage
includes j=2. We use those error estimates, not merely the proposition's
leading derivative equivalents. They give a common u_h in (0,1/8]
and finite nonnegative h_0,h_1,h_2 such that, with

    A=1/(8*sqrt(pi)),  c=gamma_E+2*log(4*pi),
    I(u)=A*u^(-1/2)*(log(1/u)-c),

one has separately for j=0,1,2,

    |H^(j)(u)-I^(j)(u)|<=h_j*u^(-j)*log(1/u),
                                      0<u<=u_h.       (3)

Take a minimum of the three source onsets and enlarge their error
constants to absorb displacement, using u<=1. The source's Gaussian
main integral differentiates to I^(j) on positive compact intervals:
the logarithm is integrable at zero and Gaussian decay controls every
fixed polynomial at infinity. No error term in (3) is differentiated.
All h_j and u_h are existential, without numerical values in this step.

We also import Euler's beta integral,
[NIST DLMF (5.12.1)](https://dlmf.nist.gov/5.12.E1), with positive
real parameters, and the standard Lebesgue dominated convergence and
Fubini-Tonelli theorems. C033j already identifies the signed exponential
and its continuous density, including its zero atom and total-variation
convergence. Those constructions are not reproved. The new obligation
is a uniform derivative majorant and summation, which the cited heat
and beta results do not themselves state for this family.

### Parameterizing the heat constants and the width derivative

Differentiating the exact product sqrt(u)*H(u) gives

    K'(u)=H(u)/(2*sqrt(u))+sqrt(u)*H'(u),
    K''(u)=-H(u)/(4*u^(3/2))+H'(u)/sqrt(u)+sqrt(u)*H''(u).

The main term sqrt(u)*I(u)=A*(log(1/u)-c) has derivatives
-A/u and A/u^2. Substituting the three independent errors (3) thus gives

    |K'(u)+A/u|<=(h_0/2+h_1)*u^(-1/2)*log(1/u),
    |K''(u)-A/u^2|<=(h_0/4+h_1+h_2)*u^(-3/2)*log(1/u).

For 0<u<1, sqrt(u)*log(1/u)<=2/e: its derivative vanishes at
u=e^(-2), with zero limiting value at both ends. Define

    B1=max{A+(2/e)*(h_0/2+h_1),
           max_(u_h<=u<=1/4) u*|K'(u)|},
    B2=max{A+(2/e)*(h_0/4+h_1+h_2),
           max_(u_h<=u<=1/4) u^2*|K''(u)|}.             (4)

These positive finite constants are well-defined by the local heat
convergence; their compact maxima are specified exactly but not
numerically bounded here. Equations (3)-(4) yield

    |K'(u)|<=B1/u,  |K''(u)|<=B2/u^2,  0<u<=1/4.      (5)

For theta in [1,2], write a_theta(t)=1+4*theta*t. The argument
u_theta(t)=t/a_theta(t) lies in (0,1/4), so (5) applies for every
positive t. Differentiating the exact Gaussian expression in theta
and integrating from 1 to sigma gives

    D_sigma(t)=-4*t^(1/2)*integral_1^sigma
                    a_theta(t)^(-2)*K'(u_theta(t)) dtheta. (6)

All derivatives here and in the next display are continuous on every
compact positive-t rectangle. Differentiation under this finite
theta integral is therefore justified by bounded difference quotients.
Equation (5) first gives the useful normalization estimate

    |D_sigma(t)|<=4*B1*(sigma-1)*t^(-1/2)/(1+4*t)
                <=C*t^(-1/2),  C=4*B1.                (7)

Since integral_0^infinity t^(-1/2)/(1+4*t) dt=pi/2
(substitute t=v^2 and integrate 2/(1+4*v^2)),

    ||Q_sigma||_TV<=2*pi*B1=K_mass,
    |M_sigma|<=K_mass,  exp(-M_sigma)<=exp(K_mass).    (8)

This bound is used only to control the density's normalization.
It also retains both endpoints of the full signed measure.

Differentiating (6) in t, using u_theta'(t)=a_theta(t)^(-2), gives

    D_sigma'(t)=integral_1^sigma [
      -2*t^(-1/2)*a_theta^(-2)*K'(u_theta)
      +32*theta*t^(1/2)*a_theta^(-3)*K'(u_theta)
      -4*t^(1/2)*a_theta^(-4)*K''(u_theta)] dtheta.

The absolute values of these three terms are bounded respectively by

    2*B1*t^(-3/2)/a_theta,
    32*theta*B1*t^(-1/2)/a_theta^2,
    4*B2*t^(-3/2)/a_theta^2.

Use a_theta>=1, 4*theta*t<=a_theta and 0<=sigma-1<=1.
Consequently

    |D_sigma'(t)|<=E*t^(-3/2),  E=10*B1+4*B2, t>0.    (9)

No sign of either K' or D_sigma was used. At sigma=1 both D_sigma
and its derivative vanish. The envelope in (9) is not integrable at
zero, so an unqualified convolution Leibniz rule there would not be
justified. The fixed-simplex argument below supplies the needed factor.

### Integrable derivative majorants on the fixed simplex

For n>=2 let Delta_(n-1) consist of v_i>0 for i<n with sum_(i<n)v_i<1,
and put v_n=1-sum_(i<n)v_i. C033j's actual convolution density is

    d_(sigma,n)(x)=integral_Delta G_(sigma,n)(x,v) dv,
    G_(sigma,n)(x,v)=x^(n-1)*product_(i=1)^n D_sigma(x*v_i). (10)

For x>0 and v in the simplex interior, differentiation is ordinary
product differentiation. By (7) and (9),

    |D_sigma(x*v_i)|<=C*x^(-1/2)*v_i^(-1/2),
    |v_i*D_sigma'(x*v_i)|<=E*x^(-3/2)*v_i^(-1/2).

The chain-rule factor v_i is essential. It gives

    |partial_x G_(sigma,n)(x,v)|
      <=[(n-1)*C^n+n*E*C^(n-1)]
                       *x^(n/2-2)*product_i v_i^(-1/2). (11)

Repeated beta integration, with every parameter positive, yields

    integral_Delta product_i v_i^(-1/2) dv
                    =pi^(n/2)/Gamma(n/2)<infinity.    (12)

For example, integration of one simplex coordinate contributes a beta
factor with parameters 1/2 and (n-1)/2, and induction reduces to
the n=2 beta integral. Thus no boundary singularity is omitted.

On J_0=[1/2,3/2], the x factor in (11) is bounded by
(1/2)^(-2)*(3/2)^(n/2). The right side is a single integrable
dominator in v, uniform in sigma and x. For a difference quotient at
an interior x of J_0, the mean value bound along its short x interval
is the same dominator. Dominated convergence therefore differentiates
(10). It also shows that the resulting derivative is jointly
continuous in (sigma,x): the differentiated integrand is jointly
continuous at every interior v and has this common majorant.
In particular, for 1/2<x<3/2,

    |d_(sigma,n)'(x)|
      <=[(n-1)*C^n+n*E*C^(n-1)]
              *pi^(n/2)*x^(n/2-2)/Gamma(n/2).         (13)

For n=1 the same formula reduces exactly to (9), since
pi^(1/2)/Gamma(1/2)=1. No integral over a zero-dimensional simplex
is needed in that case.

### Uniform differentiated summation and the Lipschitz constant

For any closed [a,b] inside (1/2,3/2), put z_b=C*sqrt(pi*b)>0.
From (8) and (13), the nth derivative term in the density series is
bounded uniformly on W times [a,b] by

    exp(K_mass)*a^(-2)*[(n-1)+n*E/C]
                       *z_b^n/[n!*Gamma(n/2)].       (14)

For positive integers n, Gamma(n/2)>=1/2. Indeed the cases n=1,2,3
are sqrt(pi),1,sqrt(pi)/2; subsequent cases follow from
Gamma(s+1)=s*Gamma(s), which follows by integration by parts in
the gamma integral. Therefore (14) is at most

    2*exp(K_mass)*a^(-2)*(1+E/C)*n*z_b^n/n!.

This is summable, since sum_(n>=1) n*z_b^n/n!=z_b*exp(z_b).
Hence the differentiated series converges uniformly, with bound

    2*a^(-2)*sqrt(pi*b)*(C+E)*exp(K_mass+z_b).          (15)

For completeness, termwise differentiation does not follow merely
from the convergence of the original measures. Each finite density
sum satisfies the fundamental theorem of calculus on [a,b]. Its
original series converges uniformly there by C033j, and its derivative
series converges uniformly by (14). Passing to the limit in that
integral identity shows that its continuous derivative-series limit
is the derivative of the specified representative r_sigma. Joint
continuity follows from the uniform convergence of the jointly
continuous derivative terms and continuity of M_sigma from C033j.
These arguments apply on each such interval, giving the asserted
derivative on W times (1/2,3/2), including the closed width endpoints.

Finally take a=3/4 and b=5/4 in (15). Then 2*a^(-2)=32/9,
sqrt(pi*b)=S and z_b=z, giving exactly L in (1). The fundamental
theorem of calculus between x and y proves (2). All constants in
that formula have been specified in (3)-(4) and (1); only the
elementary operations and numerical interval endpoints are effective
here. No numerical values for the heat inputs or compact suprema
have been established. This completes the claimed conditional local
estimate, leaving the qualifications and independent gaps stated above.

### Conceptual audit1768 — 19 November 2026

**Verdict.** The stated bound (1)-(2) and joint spatial derivative
pass under the unchanged SPECIALIZE assessment1766, separately
approved1767. No mathematical hypothesis, formula or dependency needs
correction. This verifies the local specialization; it is not a new
estimate, an independent certification of either preprint or the
finite-zero data, or evidence of a complete RH argument. Full C033p,
C032j, the relevant heat-input portion of C032s, and C033j's endpoint,
signed-exponential and density construction were inspected. Primary
coverage is reused from source-notes1764/1740 and recovery1765, including
the separately inspected fixed-j=2 proof case. No source was newly
retrieved or silently replaced by another version.

1. **Heat normalization and two cancellations.** The Gaussian formula
   with half-variance sigma gives exactly t^(-3/2)K(u_sigma(t)). The
   actual divisor retains conjugation and multiplicity; H, K, D_sigma
   and M_sigma are consequently real. Excluded ordinate zero, the
   strict strip, gamma>14, counting, through-height-100 verification,
   retained real zero and reciprocal-square tail remain qualified
   inputs. The audit uses no stronger zero statement or heat positivity
   to sign D_sigma. With R_j=H^(j)-I^(j), the two error expressions are

       K'+A/u=R_0/(2*sqrt(u))+sqrt(u)*R_1,
       K''-A/u^2=-R_0/(4*u^(3/2))+R_1/sqrt(u)+sqrt(u)*R_2.

   Applying (3) separately gives precisely h_0/2+h_1 and
   h_0/4+h_1+h_2. The fixed-j displacement error is absorbed because
   u^(1/2-j)<=u^(-j) for u<=1. Taking the minimum of the three onsets
   and 1/8 supplies one u_h. No derivative of a remainder is taken.
   The maximum of sqrt(u)log(1/u) is 2/e. Local absolute convergence
   of the fixed heat derivatives makes both maxima in (4) finite on
   the closed interval [u_h,1/4]. Thus (5) holds on its whole interval;
   B1>=A>0 also justifies later division by C=4B1.

2. **Width/time differentiation, normalization and endpoints.** For
   a=1+4theta*t, the exact derivatives are partial_theta u=-4t^2/a^2
   and partial_t u=1/a^2. These give (6) and all three displayed terms
   of D_sigma'. Their absolute bounds are respectively

       2*B1*t^(-3/2)/a,
       8*B1*t^(-3/2)*(4theta*t)/a^2,
       4*B2*t^(-3/2)/a^2.

   Since 4theta*t<=a and a>=1, their integral over a theta interval
   of length at most one is bounded by (10B1+4B2)t^(-3/2).
   The finite theta integrations and differentiations are justified
   on every positive-t compact rectangle by continuous bounded
   derivatives. All transformed times lie in (0,1/4), including the
   widths 1 and 2. There is no zero-width or large-u asymptotic limit.
   The stronger D envelope in (7) integrates over the whole half-line:
   4B1 times pi/2 is exactly K_mass=2pi B1. Hence |M_sigma|<=K_mass
   and exp(-M_sigma)<=exp(K_mass), without a sign assumption on M_sigma.
   This is the normalization factor alone, not a mistaken bound on
   the entire signed exponential. C033j retains its n=0 zero atom;
   differentiating a density on x>0 neither differentiates nor discards
   that measure. At sigma=1, Q_1=0, M_1=0 and r_1=0, consistently.

3. **Singular simplex boundaries.** The change t_i=x*v_i contributes
   x^(n-1); differentiating this Jacobian gives the (n-1)C^n term
   in (11). Differentiating each one of the n factors contributes
   v_i*D_sigma'(x*v_i). Its bound is E*x^(-3/2)*v_i^(-1/2), so that
   each full product has x power n/2-2 and every v exponent -1/2.
   No nonintegrable v_i^(-3/2) is integrated. Repeated beta integration
   has positive parameters and gives exactly pi^(n/2)/Gamma(n/2),
   including the n=2 integral pi. On [1/2,3/2], x^(n/2-2) is at most
   4*(3/2)^(n/2). This is a common integrable majorant for fixed n,
   all widths and all short spatial difference quotients. Dominated
   convergence therefore proves both differentiation and joint
   continuity of each derivative. Simplex boundary sets have measure
   zero; their approach is controlled by the same majorant. The n=1
   case is separately D_sigma', and (13) reduces to E*x^(-3/2).

4. **Uniform series and the specified density.** For 0<a<=x<=b with
   [a,b] inside (1/2,3/2), use x^(n/2-2)<=a^(-2)b^(n/2). Dividing
   (13) by n! and including the normalization gives exactly (14).
   Gamma(1/2), Gamma(1), Gamma(3/2) are sqrt(pi), 1, sqrt(pi)/2,
   all above 1/2. The recurrence advances n by two; from n=2 and
   n=3 onward its multiplier n/2 is at least one. Thus the asserted
   gamma lower bound holds for every integer n>=1. Also
   (n-1)+nE/C<=n(1+E/C). Summing n*z_b^n/n! gives z_b*exp(z_b),
   yielding exactly (15), with no unaccounted factor of C or n.

   C033j supplies two distinct facts: absolute L1 convergence identifies
   its density series with the signed measure, and local uniform
   convergence specifies its continuous representative. For each fixed
   sigma, finite partial sums satisfy the fundamental theorem of
   calculus. Uniform convergence of those sums and of their derivatives
   allows passage to the integral identity on [a,b]. Its right-hand
   side is the integral of a continuous function, so the given density
   representative has precisely the claimed derivative. Continuity of
   M_sigma, together with uniform convergence of the jointly continuous
   terms, proves joint continuity, including both closed width endpoints.
   There is no differentiation in sigma or assumption of a positive
   remainder. Finally a=3/4 and b=5/4 give 2a^(-2)=32/9 and
   z_b=C*sqrt(5pi/4). This recovers (1) exactly; integrating the derivative
   between any two points of the closed interval proves (2).

The achieved threshold is a finite, explicitly parameterized uniform
Lipschitz constant, with h_j, u_h and compact maxima still nonnumerical.
No new majorant or changed assertion was needed in the audit. Numerical
effectivity, finite-sample signed tails and inverse/coefficient costs,
separator data and margin/runtime, moments, full cancellation, uncapped
variation and actual-Xi realization remain unpaid. Stops1571/1576 are
not contradicted by this local regularity result. Further repetition of
the same source approval or audit is not a mathematical continuation.

## Mathlib

Full matching coverage for this signed, width-uniform density estimate
has not been checked and is unknown. Supporting Gaussian, beta/gamma,
dominated-convergence and convolution APIs have not been assessed
here. No Mathlib result is substituted for either fixed-v1 preprint,
the finite-zero data or the derivative majorants proved above.
