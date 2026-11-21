# Corollary C033j: the finite-subfactor residual is outside the signed width range

## Hypotheses

Retain C032j's actual-zero normalization and all its external-input
qualifications. Thus Z+ counts positive-ordinate nontrivial zeta zeros
with multiplicity, z_rho=gamma_rho-i*(beta_rho-1/2), and

    H(u)=sum_(rho in Z+) exp(-u*z_rho^2),
    u_sigma(t)=t/(1+4*sigma*t),
    H_sigma(t)=H(u_sigma(t))/sqrt(1+4*sigma*t),
    ell_sigma(t)=H_sigma(t)/t,
    B_sigma(s)=integral_0^infinity (1-exp(-s*t))*ell_sigma(t) dt.

C032j supplies positive Levy densities ell_sigma and Borel probabilities
nu_sigma on X=[0,infinity) with Laplace transforms exp(-B_sigma(s))
for s>0, with zero killing and drift. Retain the actual divisor,
conjugation, multiplicities, exclusion of ordinate zero, strip/counting,
verified zeros through height 100, first-zero/tail, heat and both fixed-v1
preprint qualifications. Neither the preprints' source-wide correctness
nor their finite-zero data are independently certified here. Sigma is
Gaussian half-variance. C032s's separately controlled j=0,1 heat errors
are retained; differentiating an asymptotic error is not allowed.

Let W=[1,2]. Use C032q's setwise law

    nu_eta(A)=integral_W nu_sigma(A) deta(sigma)

for any finite real signed Borel measure eta on W. Atoms and singular
parts are allowed. There is no common bound on |eta|(W). In particular
we impose no positivity, moment, density or full cancellation J_eta=0
condition on eta or nu_eta, and no unsmoothed Xi realization or RH.

Use C033i's exact construction: L(dt)=ell_1(t)dt on (0,infinity),
I=[1,3/2], P=L restricted to I, m=P(X)>0, and

    lambda=exp(m)*sum_(n=0)^infinity (-1)^n P^{*n}/n!,
    mu=nu_1*lambda.

Here P^{*0}=delta_0, m is finite, and mu is the probability with
zero drift/killing and Levy measure L restricted to (0,infinity)\I.

## Conclusion

There is no finite real signed Borel eta on [1,2] with nu_eta=mu.
In particular there is none with mass one. The equality being excluded
is equality on every Borel subset of X, not a finite transform fit.

The necessary condition establishing this exclusion is as follows.
Put D_sigma=ell_sigma-ell_1 and M_sigma=integral D_sigma. There exist
finite signed mass-one measures

    R_sigma=exp(-M_sigma)*E(D_sigma(t)dt),
    E(Q)=sum_(n=0)^infinity Q^{*n}/n!,
    nu_sigma=nu_1*R_sigma.                              (1)

They have uniformly bounded total variation for sigma in W. For each
finite eta, the setwise integral R_eta=integral_W R_sigma deta exists
and satisfies nu_eta=nu_1*R_eta. Its restriction to (1/2,3/2) has a
continuous density. C033i's lambda admits no such continuous density.

This is a qualified range exclusion, passing conceptual audit1744 below
under the stated inputs. Known measure-exponential, heat and
integration tools are imported; the continuum bounds and range test
are the local development. Assessment1740 found no matching range
theorem among the sources checked; this does not certify originality.
The result delimits the use of C033i's arbitrary-output reflection
counterexample in this particular width family. It does not prove
positivity reflection within that family, decide C032q/r's joint
cancellation/positivity problem, pay moments/tails, or prove Xi signs
or RH. C032u's positive two-width example is a contrast, not an input.

## Proof

### Cited tools and the difference from the covered results

Reuse the separately approved EXPLORE assessment1740 and its primary
source/proof coverage in source-notes1740 and recovery-notes1741.
The exact Gaussian formula is Suvrit Sra, *Some positivity properties
of Riemann Xi under smoothing*,
[2611.00345v1, 11 November 2026](https://hexagonmath.org/pdf/2611.00345v1),
Proposition 3.1/(3.2)-(3.3), pp.5-6, complete proof C.1, p.21,
as applied in C032j. For H and its derivatives use Sra, *On some
positivity properties of the Riemann Xi function*,
[2610.00584v1, 20 October 2026](https://hexagonmath.org/pdf/2610.00584v1),
Lemma 2.1, pp.3-4, and the separate j=0,1 error estimates in the proof
of Proposition B.1, p.17, as recorded and applied in C032s. These
give local convergence and the derivative estimate used below; we do
not reprove either source or assume its asymptotic errors differentiable.

For the finite-signed-measure convolution exponential and its norm
bound import Vydas Cekanavicius and Palaniappan Vellaisamy, *On closeness
of two discrete weighted sums*, Modern Stochastics: Theory and
Applications 5(2) (2018), 207-224,
[Section 1 after (1), and (23)-(24)](https://www.vmsta.org/journal/VMSTA/article/114/read),
DOI 10.15559/18-VMSTA103. The framework concerns arbitrary finite
real signed measures on R; its later discrete approximation theorems
are not used. In particular ||E(Q)||_TV<=exp(||Q||_TV).

For uniqueness import Ante Mimica, *Laplace transform*, Dresden course,
27 April-1 May 2015,
[Proposition 1.8, pp.9-10](https://web.math.pmf.unizg.hr/~amimica/lt.pdf):
finite positive Borel measures on [0,infinity) with equal Laplace
transforms on s>0 coincide. The convolution transform is Proposition
1.4(iv), pp.6-7. For signed measures we explicitly use Jordan parts
and absolute integrability below; no signed inversion formula is used.

The convolution-density estimate uses Euler's beta integral,
[NIST DLMF (5.12.1)](https://dlmf.nist.gov/5.12.E1), with positive
real parameters, and the standard Lebesgue dominated convergence,
Fubini-Tonelli and Weierstrass uniform convergence theorems. No
holomorphic-integral or time-analyticity theorem is needed. The
source tools alone give neither a uniform continuum width estimate
nor a continuous density for the signed exponential. Those are
proved here, rather than inferred from total-variation convergence.

### Uniform integrable width differences

Set K(u)=sqrt(u)*H(u). The exact Gaussian formula gives

    ell_sigma(t)=t^(-3/2)*K(u_sigma(t)).                  (2)

C032s's separately controlled heat errors give, for sufficiently
small u>0, with A=1/(8*sqrt(pi)),

    K'(u)=-A/u+O(u^(-1/2)*log(1/u)).                    (3)

This is the cancellation obtained from both H and H' errors, not
the derivative of an O term. Since sqrt(u)*log(1/u) tends to zero,
there are u_0 in (0,1) and C>0 with |K'(u)|<=C/u for 0<u<=u_0.
For 0<t<=u_0 and 1<=sigma<=2, one has 0<u_sigma(t)<=u_1(t)<=t.
The fundamental theorem of calculus and (2) therefore give

    |D_sigma(t)|
      <=C*t^(-3/2)*log(u_1(t)/u_sigma(t))
       =C*t^(-3/2)*log((1+4*sigma*t)/(1+4*t))
      <=4*C*(sigma-1)*t^(-1/2)
      <=4*C*t^(-1/2).                                  (4)

Here log(1+y)<=y for y>=0 was applied with
y=4*(sigma-1)*t/(1+4*t). The estimate includes sigma=1, where
D_1=0. It uses no sign for K' or D_sigma.

For t>=1 and every sigma in W, u_sigma(t) belongs to [1/9,1/4].
K is continuous there by local convergence of the heat series. If
K_* is its maximum absolute value, (2) implies

    |D_sigma(t)|<=2*K_* t^(-3/2), t>=1.                 (5)

The map (sigma,t)->D_sigma(t) is jointly continuous on W times
(0,infinity). On the remaining compact interval [u_0,1] it is
uniformly bounded. Increasing a finite constant C_0 in (4) gives
the common integrable envelope

    |D_sigma(t)|<=h(t),
    h(t)=C_0*t^(-1/2) for 0<t<=1,
    h(t)=C_infinity*t^(-3/2) for t>1.                  (6)

Take C_infinity=2*K_*. Thus K_0=integral h=2*C_0+2*C_infinity
is finite. Extend Q_sigma(dt)=D_sigma(t)dt by zero to R. These are
finite signed measures on X with no zero atom, ||Q_sigma||<=K_0,
and |M_sigma|<=K_0. Dominated convergence using 2h makes
sigma->Q_sigma continuous in total variation, and M_sigma continuous.
The constants need not be numerically effective for this range test.

### Signed exponential, transform identification and zero atom

The cited exponential defines R_sigma in (1), with

    ||R_sigma||<=exp(2*K_0),
    R_sigma(X)=exp(-M_sigma)*exp(M_sigma)=1.             (7)

All convolution powers are carried by X, so the same is true of their
total-variation limit. For n>=1 they have Lebesgue densities (by
Fubini applied to the integrable absolute densities), hence no atom
at zero. Therefore

    R_sigma({0})=exp(-M_sigma).                         (8)

No assertion that R_sigma is positive is made. Its atom can exceed
one. Its transform is evaluated by the absolutely convergent series:

    Laplace(R_sigma)(s)
      =exp(-M_sigma)*exp(integral exp(-s*t) dQ_sigma(t))
      =exp(-integral (1-exp(-s*t))*D_sigma(t)dt).        (9)

Termwise transforms are legitimate because exp(-s*t) is bounded on
X and the series is absolutely convergent in total variation.
The two B_sigma integrals are finite by C032j, so subtracting their
integrable integrands shows that the exponent in (9) is
-(B_sigma(s)-B_1(s)).

We will use signed uniqueness in exactly this form. If two finite
real signed measures on X have identical transforms on s>0, their
difference theta has Jordan parts theta^+, theta^- with equal
transforms. Both are finite positive measures; Mimica's positive
uniqueness theorem identifies them on all Borel sets. Hence theta=0.
This includes {0}; it requires no density or moment assumption.
For finite signed convolution, the transform product formula follows
from Fubini, since |exp(-s(x+y))|<=1 on X times X and the product
variation measure has finite mass.

Combining (9) with the transform of nu_1 thus gives
Laplace(nu_1*R_sigma)=exp(-B_sigma). Signed uniqueness proves (1)
as measures on X, including zero.

### Continuous density near one, with a uniform bound

For every finite b>0, (6) and joint continuity give a finite C_b
such that |D_sigma(t)|<=C_b*t^(-1/2) for 0<t<=b, uniformly on W.
For n>=1 let d_(sigma,n) be the density obtained by convolving
D_sigma with itself n times on the positive half-line. The n=1
case is D_sigma. Absolute integration and repeated beta integration
give, for 0<x<=b,

    |d_(sigma,n)(x)|
      <= C_b^n * Gamma(1/2)^n / Gamma(n/2)
                        * x^(n/2-1).                  (10)

Indeed convolution of x^(a-1) and x^(c-1), a,c>0, is
x^(a+c-1)*Gamma(a)*Gamma(c)/Gamma(a+c) by DLMF (5.12.1).
Starting with a=c=1/2 and then using a=n/2,c=1/2 proves (10)
inductively. All intermediate integrals of the absolute majorants
are finite. Fubini consequently identifies these functions with
the densities of Q_sigma^{*n}; also

    integral_0^infinity |d_(sigma,n)(x)|dx<=K_0^n.       (11)

Each d_(sigma,n) is jointly continuous for sigma in W and x>0.
For n>=2 this follows directly on every W times [a,b], 0<a<b,
by writing the convolution integral on the fixed simplex:

    d_(sigma,n)(x)
      =x^(n-1)*integral_(v_i>0, sum_(i<n)v_i<1)
                          product_(i=1)^n D_sigma(x*v_i) dv,
    v_n=1-sum_(i<n)v_i.

The absolute integrand, including x^(n-1), is bounded there by
b^(n-1)*C_b^n*a^(-n/2)*product v_i^(-1/2). Repeated beta integration
makes this dominator integrable on the simplex. At every interior
simplex point the integrand is continuous in (sigma,x), so dominated
convergence applies. For n=1 joint continuity was already established.

The density of the non-atomic part of R_sigma is therefore

    r_sigma(x)=exp(-M_sigma)*sum_(n=1)^infinity
                                      d_(sigma,n)(x)/n!, x>0. (12)

This is an actual density, not merely a formal expression: (11)
gives absolute convergence in L1, whose associated measures agree
with the total-variation exponential. The same series converges
uniformly on every W times [a,b], 0<a<b. To see this, (10) bounds
its nth term in absolute value by

    exp(K_0)*a^(-1)*(C_b*sqrt(pi*b))^n / (n!*Gamma(n/2)). (13)

Writing A_b=C_b*sqrt(pi*b), the ratio of the (n+2)nd to the nth
majorant is 2*A_b^2/[n*(n+1)*(n+2)], which tends to zero.
Both parity subseries therefore converge. By uniform convergence
and continuity of M_sigma, r_sigma is jointly continuous on each
such compact set, with a common finite bound there. The pointwise
series and its L1 limit coincide almost everywhere by absolute
summability in L1; hence (12) gives a continuous representative
away from zero of the measure density. In particular

    R_sigma=exp(-M_sigma)*delta_0+r_sigma(x)dx,           (14)
    sup_(sigma in W, 1/2<=x<=3/2) |r_sigma(x)|<infinity.

Only continuity on this last interval is used in the exclusion.

### Integration over arbitrary finite signed widths

We justify the setwise integral in the conclusion, including its
measurability and countable additivity. Finite convolution satisfies
||Q_sigma^{*n}-Q_tau^{*n}||<=n*K_0^(n-1)*||Q_sigma-Q_tau||
by the telescoping identity and the convolution norm inequality.
Summing with 1/n! shows that E(Q_sigma) is continuous in total
variation. Together with continuity of M_sigma this makes R_sigma
continuous in that norm. Thus sigma->R_sigma(A) is continuous for
every Borel A and bounded by exp(2*K_0).

For V=|eta|(W)<infinity define R_eta(A)=integral R_sigma(A)deta.
For disjoint Borel A_j, the partial sums R_sigma(union_(j<=N)A_j)
converge pointwise to R_sigma(union_j A_j) and are bounded by
exp(2*K_0). Dominated convergence against |eta| proves countable
additivity. For any finite Borel partition, the sum of absolute
R_eta masses is at most integral ||R_sigma|| d|eta|. Consequently

    ||R_eta||<=V*exp(2*K_0),    R_eta(X)=eta(W).          (15)

Integration of bounded Borel functions commutes with this mixture:
prove it first for simple functions and then use uniform approximation
by bounded simple functions and the bounds (7),(15).

For a Borel A, the function g_A(y)=integral 1_A(x+y)dnu_1(x)
is Borel, lies in [0,1], and defines convolution against nu_1.
The bounded integration identity just established, followed by (1),
gives on every Borel set

    (nu_1*R_eta)(A)
      =integral_W (nu_1*R_sigma)(A)deta(sigma)
      =integral_W nu_sigma(A)deta(sigma)=nu_eta(A).      (16)

There is no unbounded test or positivity of a signed factor here.
From (14) and the compact uniform bound, Fubini on W times
J=(1/2,3/2) gives R_eta restricted to J the density

    r_eta(x)=integral_W r_sigma(x)deta(sigma), x in J.

It is continuous by dominated convergence against the fixed finite
measure |eta|. No common variation cap on the class of eta was used.
The zero atom is outside J, but it remains in (16) and in uniqueness;
explicitly R_eta({0})=integral exp(-M_sigma)deta(sigma).

### Exact deconvolution and the incompatible continuous representative

Suppose nu_eta=mu. By (16) and C033i, nu_1*R_eta=nu_1*lambda.
The number Laplace(nu_1)(s)=exp(-B_1(s)) is strictly positive for
every s>0, since B_1(s) is finite. Cancel it in the transform identity.
Signed uniqueness proved above yields R_eta=lambda on every Borel
subset of X. This cancellation does not assert that the entire law
nu_1 has a finite convolution inverse or reflects positivity.

C033i's P is carried by [1,3/2] and has density ell_1 there;
P^{*n} is carried by [n,3n/2] for n>=1. On (1/2,1), neither the
zero-jump atom nor any positive-jump term of lambda is present.
On (1,3/2), only the n=1 term is present. Hence equality of measures
forces

    r_eta=0 almost everywhere on (1/2,1),
    r_eta=-exp(m)*ell_1 almost everywhere on (1,3/2).    (17)

The function ell_1 is continuous at all positive points by (2)
and local continuity of H, and ell_1(1)>0 by C032j's strict heat
positivity. A continuous real function vanishing almost everywhere
on an open interval vanishes everywhere there: a nonzero value
would retain its sign and a positive lower absolute bound on some
subinterval of positive Lebesgue measure. Apply this to r_eta on
the left interval and to r_eta+exp(m)*ell_1 on the right.
Thus (17) holds pointwise on each of these open intervals.
Continuity at 1 would then require both

    r_eta(1)=0,    r_eta(1)=-exp(m)*ell_1(1)<0,

which is impossible. No claim depends on the value of a density at
a single point or on whether endpoints are included in I. This
proves the exact range exclusion. A representation would in any
case have eta(W)=nu_eta(X)=mu(X)=1 by C032q. The stronger statement
with arbitrary finite input mass follows as well. ∎

The required threshold was a continuous representative near 1 plus
all-Borel deconvolution, not a quantitative approximation error.
Both have been supplied under the stated inputs. This excludes only
C033i's fixed residual law from this width range. Other outputs,
other signed remainders, full J_eta cancellation and the main RH
positivity gap remain undecided.

### Conceptual audit1744 — 19 November 2026

Verdict: the exact qualified exclusion passes under unchanged EXPLORE
assessment1742, separately approved1743. The full C033j argument and
C033i construction were read, along with C032j's source application,
C032s's separate heat-error estimates and C032q's signed-kernel
construction. Source-notes1740/1552 and the recorded approvals supply
the primary theorem coverage. This verifies the local proof; it does
not independently certify either fixed-v1 preprint or the zero data.
No change to a mathematical hypothesis, bound or conclusion is required.

1. **One uniform endpoint envelope.** In C032s, the errors in H and H'
   are separately bounded by C_0 log(1/u) and C_1 u^(-1) log(1/u).
   Their contributions to K' are bounded by
   (C_0/2+C_1)u^(-1/2)log(1/u). The exact derivative of sqrt(u)I(u)
   is -A/u; hence one onset gives |K'|<=C/u, independently of sigma.
   Every integration segment [u_sigma(t),u_1(t)] lies below that onset
   when t does. Its logarithmic length is at most 4(sigma-1)t, so
   (4) gives the integrable t^(-1/2) envelope including sigma=1.
   For t>=1 the minimum of t/(1+4sigma t) is 1/9 and the supremum
   is 1/4. The compact-time bound therefore proves (5) for all widths,
   rather than substituting a large-u heat asymptotic at finite u.
   Joint continuity handles the intervening compact rectangle. The
   integral of (6) is exactly 2C_0+2C_infinity. Neither a global sign
   of D_sigma nor C032s's effective endpoint signs enter this proof.

2. **Finite signed factors and zero.** All Q_sigma have integrable
   real densities; conjugation in the actual divisor makes H real.
   The exponential series converges absolutely in total variation,
   with norm at most exp(K_0). Multiplication by exp(-M_sigma) costs
   at most exp(K_0), giving (7). Nonzero convolution powers have
   integrable densities, so the atom exp(-M_sigma)delta_0 is retained
   exactly. Bounded transform tests pass through the norm-convergent
   series. The two finite B integrals can be subtracted, yielding (9).
   If two finite signed transforms agree, the Jordan parts of their
   difference are finite positive measures with equal transforms;
   Mimica's positive uniqueness applies on all of X. It includes zero
   without applying the source's qualified inversion display at zero.
   Fubini is bounded by the product of total variations, so it gives
   the signed convolution transform. This proves (1) without positivity
   of R_sigma or a finite inverse for nu_1.

3. **A continuous representative, not only an L1 limit.** The beta
   parameters at successive convolutions are n/2 and 1/2, both positive.
   Thus (10) includes n=1 and justifies absolute simplex integration.
   On W times [a,b], the displayed fixed-simplex dominator is integrable
   because every endpoint exponent is -1/2. Pointwise continuity holds
   in the simplex interior; its boundary is irrelevant to the integral.
   This proves joint continuity of each convolution density. The L1
   norm bound K_0^n identifies the exponential's density as a measure.
   Separately, x^(n/2-1)<=a^(-1)b^(n/2) yields (13). The exact
   two-step ratio is 2A_b^2/[n(n+1)(n+2)], so both parity subseries
   converge uniformly. These two distinct convergence arguments prove
   that the continuous series represents the measure density almost
   everywhere and has a common bound near 1. No regularity is inferred
   from total-variation convergence alone.

4. **All finite signed width inputs.** The telescoping convolution
   inequality and the exponential norm series prove norm continuity
   of R_sigma. Every Borel set evaluation is therefore measurable.
   Partial disjoint unions are bounded in absolute mass by exp(2K_0),
   so dominated convergence against each fixed finite |eta| proves
   countable additivity. The partition estimate gives (15). Uniform
   simple approximation establishes the bounded Borel integral identity.
   The convolution test g_A is Borel by parameter integration of the
   Borel indicator of x+y in A and is bounded by one; hence (16) holds
   on every Borel A. Local density integration uses finite Lebesgue
   length and the common bound from (14), then dominated convergence
   against |eta| gives continuity of r_eta. Atoms and singular parts
   of eta cause no problem. The estimates depend on its finite variation;
   no uniform variation cap over all eta is asserted or needed.

5. **Cancellation and the actual contradiction.** Since B_1(s)<infinity,
   exp(-B_1(s)) is nonzero for every s>0. Cancelling this scalar and
   applying the signed uniqueness just checked identifies R_eta=lambda
   as measures, including their zero atoms. C033i's supports [n,3n/2]
   leave zero density on (1/2,1) and precisely -exp(m)ell_1 on (1,3/2).
   The common factor's density is continuous and strictly positive at 1
   by the exact heat formula and C032j. Almost-everywhere equality on
   each open interval therefore fixes the two one-sided limits of the
   continuous representative, respectively 0 and -exp(m)ell_1(1)<0.
   No pointwise choice of density, boundary atom or cancellation among
   higher powers can remove their incompatibility.

The direct mathematical inputs remain C032j, C032q, C032s and C033i;
their stated uses suffice, and no extra lemma edge is introduced.
C032u and the older route stops are comparisons only. The achieved
threshold is exact exclusion for this mu and this compact width interval.
It supplies no quantitative distance from the range, positivity reflection
inside the range, full odd cancellation, moment payment or Xi realization.
This is verification of the local development, not a further theorem or
a claim of progress beyond the sources checked.

## Mathlib

Full matching coverage of the qualified continuum-width regularity and
range exclusion has not been checked and remains unknown. Supporting
signed-measure convolution, Laplace uniqueness, Bochner/kernel integral
and beta-integral APIs have not been assessed here. Neither the fixed-v1
preprint inputs nor this new application are certified by Mathlib.
