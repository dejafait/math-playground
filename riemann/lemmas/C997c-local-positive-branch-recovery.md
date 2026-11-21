# Corollary 997c: a bounded local operator recovers the positive-exponential branch

## Hypotheses

Use L997's original polynomial, including its constant subtraction,

    K_(n+2)(t)=(L_(n+1)^(2)(t)-1)/(n+1),
    I=Gamma=[7/4,9/4], Gamma_in=[15/8,17/8], n>=2.

Here n is an integer. Let mu be any finite COMPLEX Borel measure on I,
with V=||mu||_TV.
Use C997a(1)-(2)'s complete competitor response

    R_n(gamma;mu)=integral_I q_n(c;3/8,gamma)dmu(c).

With g_n(t)=K_(n+2)(t)*exp(-t/2)*cosh(3t/8), define exactly

    H_n^+(gamma;mu)=-2*integral_I exp(-cn/4)*[
       integral_(cn)^(c*(n+2)) g_n(t)*exp(i*gamma*t)dt
       -integral_n^(n+2) g_n(t)*exp(i*gamma*t)dt]dmu(c).       (1)

The reflected beta contribution, lower interval and K's -1 are retained.
These are finite hypothetical quartet responses, not actual zeta zeros.
No global signal norm, unknown spectral density, actual reconstruction,
RH, or positivity hypothesis is assumed.

## Conclusion

There is a SINGLE sequence of bounded complex-linear operators

    A_n:C(Gamma,C) -> C(Gamma_in,C)

depending only on the specified intervals, n and fixed numerical constants,
such that for n>=48

    ||A_n||_(sup->sup)<=n^2,
    ||A_n(R_n|Gamma)-H_n^+|Gamma_in||_infinity
                              <=C*exp(-n/32)*V,              (2)

with fixed finite C independent of n and mu. Consequently the same
sequence satisfies every positive exponential norm allowance: for each
epsilon>0 one may take C_epsilon=max{1,4/epsilon^2} in
||A_n||<=C_epsilon*exp(epsilon*n). Set A_n=0 for 2<=n<48.

The construction is a finite sum of accessible point evaluations. It
does not use an unbounded derivative or principal-value operator.
An explicit, stronger error certificate before absorbing polynomials is

    rho=log(49)/12-9/32>1/32,
    error <= [ (525/4)*exp(27/16)*(n+2)*exp(-rho*n)
              +8*exp(3/4)*(n+2)*(2*n^2+1)*exp(-n/16) ]*V.    (3)

Step320, 10 November 2026: RESEARCH / REPRODUCTION under the unchanged
pre-invocation EXPLORE assessment review318, approved in step319. This is
a local ADVANCE by explicit polynomial-filter specialization, not a claim
of originality beyond the checked sources. The proof was unaudited at
step320; the independent conceptual audit in step322 below accepts (2)-(3)
without changing their hypotheses or bounds. Branch recovery supplies an
intermediate resource only: selected
normalization, continuation to the selected response, the original slope
assay, actual reconstruction, signed forcing, infinite-zero complements,
regulator uniformity, L993 and L984(H) remain unpaid. No RH candidate.

## Proof

### Exact spectral measures and their variation

L997(4) supplies |K_(n+2)(t)|<=2*(n+2)*exp(t/2) for t>=0.
This is the previously justified real Laguerre bound based on
[DLMF18.14.8](https://dlmf.nist.gov/18.14.E8), with the constant
subtraction included. We use that local input without re-proving it.

Define finite complex Borel measures nu_U and nu_L on the positive t axis
by integrating, with respect to mu(c), the following absolutely continuous
measures:

    dnu_(U,c)(t)=-2*exp(-cn/4)*1_{cn<=t<=c(n+2)}*g_n(t)dt,
    dnu_(L,c)(t)= 2*exp(-cn/4)*1_{n<=t<=n+2}*g_n(t)dt.        (4)

For fixed n the integrands are Borel measurable and integrable against
dt*d|mu|(c) on a compact rectangle. Fubini for finite complex measures
therefore defines their integrals and gives the variation bound by the
integral of their absolute densities. Endpoints of the t intervals have
Lebesgue measure zero, so the closed-interval notation is harmless even
when mu has endpoint atoms. Thus

    supp(nu_U) subset [7*n/4,9*(n+2)/4],
    supp(nu_L) subset [n,n+2],
    ||nu_U||_TV<=18*exp(27/16)*(n+2)*exp(9*n/32)*V,
    ||nu_L||_TV<= 8*exp(3/4)*(n+2)*exp(-n/16)*V.             (5)

Indeed, |g_n(t)|<=2*(n+2)*exp(3t/8). The upper density in (4) has
variation at most 8*c*(n+2)*exp(c*n/8+3*c/4); maximize at c=9/4.
The lower one has variation at most
8*(n+2)*exp((3/8-c/4)*n+3/4); maximize at c=7/4. Integration against
|mu| proves (5). This establishes Fourier-measure TV directly; it is not
inferred from an entire-function sup envelope.

For j=U,L write H_j(gamma)=integral exp(i*gamma*t)dnu_j(t) and
R_j(gamma)=integral [exp(i*gamma*t)+exp(-i*gamma*t)]dnu_j(t).
The definition (1) and C997a's exact cosine response give

    H_n^+=H_U+H_L, R_n=R_U+R_L.                             (6)

This uses 2*cos(gamma*t)=exp(i*gamma*t)+exp(-i*gamma*t).
For complex mu no conjugacy between the branches is assumed.

### A finite sign polynomial with a paid global bound

The only general series input here is the standard named generalized
binomial theorem: (1-v)^(-1/2)=sum_(j>=0) b_j*v^j for |v|<1,
where b_j=binomial(2j,j)/4^j>0. Multiplying it by itself gives
sum_(l=0)^j b_l*b_(j-l)=1. Define the polynomial P_j(z) by

    (1-2*z*u+u^2)^(-1/2)=sum_(j>=0) P_j(z)*u^j             (7)

near u=0, with value one at u=0. These are the classical Legendre
coefficient polynomials; no extremal theorem or asymptotic is used.
We give the finite coefficient estimates because a multiplier-error
theorem alone does not pay the representing operator's norm.

If alpha+beta=2z and alpha*beta=1, the same binomial theorem gives

    P_j(z)=sum_(l=0)^j b_l*b_(j-l)*alpha^l*beta^(j-l).        (8)

For real |z|<=1 the roots alpha,beta lie on the unit circle, hence
|P_j(z)|<=1. For -1201/49<=z<-1 they are negative real and both have
modulus at most 49: the larger modulus is |z|+sqrt(z^2-1), which is
increasing in |z| and equals (1201+1200)/49=49 at the left endpoint.
Consequently

    |P_j(z)|<=1 on [-1,1],
    |P_j(z)|<=49^j on [-1201/49,1].                         (9)

All formulas are finite coefficient identities; in particular P_j is
a real polynomial of degree at most j. Put

    s=24/25, r=1/49, z(x)=(1250*x^2-1201)/49,
    F_m(x)=(50/49)*x*sum_(j=0)^m (-r)^j*P_j(z(x)).          (10)

Then F_m is an odd real polynomial of degree at most d=2m+1. For
|x|<=1, z(x) belongs to [-1201/49,1], so (9) proves

    sup_[-1,1]|F_m| <= (50/49)*(m+1).                       (11)

For s<=|x|<=1, z(x) is in [-1,1], and

    x^2=(2401/2500)*(1+2*r*z(x)+r^2).

Evaluate the absolutely convergent series (7) at u=-r. With the positive
real square root it follows that (50/49)*x times the infinite sum equals
x/|x|. The tail, bounded by a geometric series using (9), gives

    |F_m(x)-sgn(x)| <= (25/24)*49^(-(m+1)), s<=|x|<=1.      (12)

Indeed (50/49)/(1-1/49)=25/24 and |x|<=1. The bound (11) covers
the entire intervening interval as well; no exponentially large
unobserved-frequency multiplier has been hidden.

### Finite shifts, closed-window access and operator norm

For n>=48 set

    Delta=3/(4*n), m=floor((n-6)/12), d=2*m+1.

Then d<=n/6 and d*Delta<=1/8. Expand the trigonometric polynomial

    F_m(sin(theta))=sum_(k=-d)^d a_k*exp(i*k*theta).

Define, for every continuous complex f on Gamma,

    (A_n f)(gamma)=f(gamma)/2
                     +(1/2)*sum_(k=-d)^d a_k*f(gamma+k*Delta),
                                            gamma in Gamma_in. (13)

Every evaluation lies in Gamma, including when gamma is either closed
endpoint of Gamma_in. A finite sum of translates is continuous in gamma
and complex-linear in f. The elementary Fourier-coefficient formula and
(11) give |a_k|<=(50/49)*(m+1). Thus

    ||A_n|| <= 1/2+(25/49)*(4*m+3)*(m+1) <= n^2.            (14)

For the last inequality use m+1<=n/12+1/2<=n/8 and
4*m+3<=n/3+1<=n/2 for n>=48. Their substitution gives
1/2+25*n^2/784<=n^2. This proves boundedness on the FULL continuous
input space, not just the response range. The standard finite Fourier
expansion here is an identity for a polynomial in sin(theta); its
coefficient bound follows directly by integrating over one period.

The multiplier on exp(i*gamma*t) is

    M_n(t)=(1+F_m(sin(t*Delta)))/2.                          (15)

This sign convention selects the positive-exponential branch in (1).
It does not produce a twice-normalized analytic signal.

### Uniform upper-band separation and the complete error

For t in the FULL upper support in (5) and n>=48,

    21/16 <= t*Delta <= 27/16+27/(8*n) <= 225/128.

Using 3<pi<22/7, this interval lies within distance 29/112 of pi/2:
11/7-21/16=29/112 and 225/128-3/2=33/128<29/112. Therefore

    sin(t*Delta)>=1-(29/112)^2/2
                  =24247/25088>24/25.                      (16)

Here cos(y)>=1-y^2/2 was applied to the distance from pi/2. On the
negative upper support the sine is the negative of this quantity.
Equations (12),(15) consequently give, uniformly on the upper support,

    |M_n(t)-1|, |M_n(-t)| <= (25/48)*49^(-(m+1)).            (17)

Apply the finite operator (13) inside the integrals in (6), which is
legitimate by finite summation and finite variation. For every real
gamma in Gamma_in the two branch errors sum to at most
(25/24)*49^(-(m+1))*||nu_U||_TV. No cancellation or positivity of
nu_U is needed. Since m+1>(n-6)/12,

    49^(-(m+1))<=7*exp(-log(49)*n/12).

Together with (5), this is the first term of (3). For the lower interval,
use (14) and the exact expressions (6), rather than omitting it:

    ||A_n(R_L|Gamma)-H_L|Gamma_in||_infinity
         <=(2*||A_n||+1)*||nu_L||_TV.

This is the second term of (3), proving that estimate for every complex
mu and uniformly on the closed output interval.

For completeness the positive rate margin has an elementary exact
certificate. Integrating the geometric series for 1/(1-x^2) on
[0,3/4] gives

    log(7)=2*sum_(j>=0) (3/4)^(2*j+1)/(2*j+1)
          >3/2+9/32+243/2560=4803/2560>15/8.

In fact rho>1/32+1/5120. Extract exp(-n/32) from (3). The remaining
upper factor (n+2)*exp(-n/5120) is bounded by 5122. For the lower
factor expand (n+2)*(2*n^2+1)=2*n^3+4*n^2+n+2 and use
sup_(x>=0) x^k*exp(-x/32)<=(32*k)^k for k=1,2,3. For example,

    C=(525/4)*exp(27/16)*5122
          +8*exp(3/4)*(2*96^3+4*64^2+34)                   (18)

is finite and suffices in (2). Finally n^2*exp(-epsilon*n)<=4/epsilon^2
for epsilon>0, so the same A_n meets all the requested norm allowances.

### Scope of the advance

The narrow COMPLETE upper band is essential to (16). The construction
does not assert the same rates for arbitrary bandlimited data, a ray
of positive frequencies, or an observation interval with no interior
margin. The lower band is paid by its original slope-TV decay. The
constants do not depend on mu, its atom count, or actual unknown zeros.

Only the nominated H_n^+ is recovered. No equation connecting its local
values to the selected normalization with a paid continuation cost is
established, and there is no inversion for mu. This neither closes the
original signed-slope assay nor upgrades the fixed-filter stops. The
proof uses no numerical sampling, interchange over actual zeros, or
target-equivalent positivity assumption.

### Exact scalar verification

Reproduce the rational arithmetic with
`python3 scripts/adaptive-slope/local-branch-filter-arithmetic-320.py`.
The full certificate is
`scripts/adaptive-slope/local-branch-filter-arithmetic-320.json`.
Its complete `/checks` object was inspected using
`python3 ../scripts/loop/inspect_json.py scripts/adaptive-slope/local-branch-filter-arithmetic-320.json --pointer /checks --full`.
All 18 checks pass, including sine floor 24247/25088>24/25 and
rate lower bound 161/5120>1/32 with margin 1/5120. These are exact
scalar checks supporting the written proof; they do not independently
verify the measure argument, all-n construction or operator identities.

### Independent conceptual audit — step322, 10 November 2026

RESEARCH / REPRODUCTION under pre-existing SPECIALIZE review320's exact
covered audit. The audit accepts (1)-(18), including the SAME sequence
quantifier, for every finite complex Borel mu and all integer n>=48.
This verifies a local input, not a stronger theorem, a novelty claim or
an RH candidate. No bound or mathematical dependency needed correction.

**Imported contracts and their scope.** Reuse the primary contracts
inspected in review320: NIST DLMF version 1.2.8,
[4.6.7](https://dlmf.nist.gov/4.6.E7) (generalized binomial theorem),
[18.12.11](https://dlmf.nist.gov/18.12.E11) with the section 18.12 domain
qualification (Legendre generating function), and
[1.8.4](https://dlmf.nist.gov/1.8.E4) (finite Fourier coefficient
normalization). For measures use Sheldon Axler,
[*Measure, Integration & Real Analysis*](https://measure.axler.net/MIRA.pdf),
author version 12 June 2026, 9.10 pp260-261 and 9.41(b) p274, and
Terence Tao, [*245A, Notes6*](https://terrytao.wordpress.com/2010/10/30/245a-notes-6-outer-measures-pre-measures-and-product-measures/),
30 October 2010, Theorem 43 (Fubini for absolutely integrable complex
functions on sigma-finite positive product measure spaces).
These general theorems are imported, not reproved. The following
specialization checks are necessary because those contracts alone do
not supply the joint finite-window norm and slope-TV error estimate.

**Complex measures and the full response.** Write dmu=h d|mu| with
measurable |h|=1 almost everywhere, by Axler 9.41(b). On the fixed compact
rectangle I times [0,9(n+2)/4], each density in (4), multiplied by h(c),
is measurable and absolutely integrable for the positive product
d|mu|(c) dt. Integrating this density on I times a Borel t-set defines a
countably additive complex measure; its variation is at most the
integral of the absolute density. This follows either by summing over
finite partitions or by Axler 9.10 before taking the t marginal.
Theorem 43 applies to the completed finite measures. The closed interval
indicators are Borel, and their t endpoints have Lebesgue measure zero
for each c; hence even atoms at c=7/4 or 9/4 cause no omitted term.
Compact support also makes H_j and R_j continuous by dominated
convergence. No infinite-zero sum or regulator limit is involved.

L997(4) applies at m=n+2 and t>=0 to the ORIGINAL K, including -1.
With cosh(3t/8)<=exp(3t/8), the upper density integrates in absolute
value to at most 8c(n+2)exp(cn/8+3c/4), and the lower one to at most
8(n+2)exp((3/8-c/4)n+3/4). The increasing upper and decreasing lower
c dependence give exactly (5). Both reflected beta contributions
remain in cosh. C997a(1)'s pointwise -4 cosine identity gives (6)
after complex-linear integration; no extension of its real-measure
Hahn-Banach theorem is needed. In particular the factor in H is -2,
and the negative branch is not replaced by a complex conjugate.

**Coefficient identity and global norm.** For any fixed real z, choose
the roots alpha,beta with alpha+beta=2z and alpha*beta=1. On a sufficiently
small disk |u|<min(1/|alpha|,1/|beta|), the two binomial series converge
absolutely and their product is the analytic square-root germ in (7)
with value one at zero. Equality of its coefficients proves (8).
This is a finite coefficient identity even for z<-1; evaluation at
u=-1/49 is used ONLY for z in [-1,1], where the generating series has
radius at least one. The nonnegative coefficient convolution equals
one because (sum b_j u^j)^2=(1-u)^(-1). The root moduli are one on
[-1,1] and at most 49 on [-1201/49,-1), establishing both parts of (9).
Thus each summand r^j P_j(z(x)) is bounded in modulus by one over the
FULL interval |x|<=1, proving (11) without an unobserved exponential
growth cost. On 24/25<=|x|<=1 the identity for x^2 in (10)-(12) uses
the positive real square root and gives x/|x|, including both endpoints.
The omitted series tail is bounded by (25/24)49^(-(m+1)).

For all n>=48, m>=3, d=2m+1<=n/6 and d Delta<=1/8. The finite
Fourier expansion has at most 2d+1=4m+3 terms. Its coefficients satisfy
|a_k|<=sup_theta|F_m(sin(theta))| by the normalized integral formula.
Taking absolute values of the weights therefore proves (14) on the
entire complex Banach space C(Gamma), not merely on generated signals.
The inequalities m+1<=n/8 and 4m+3<=n/2 hold for every such n,
and 1/2+25n^2/784<=n^2. Since Gamma_in has distance 1/8 from each
endpoint of Gamma, all evaluations in (13) are accessible even at
gamma=15/8,17/8. No derivative, limiting sum or off-window datum is used.

**Signs, rates and uniform quantifiers.** Substituting exp(i gamma t)
directly into (13) gives precisely M_n(t) from (15). Substituting its
negative-frequency counterpart gives M_n(-t). The complete positive
upper support has Delta t in [21/16,225/128]; using 3<pi<22/7 places
it within 29/112 of pi/2. Thus its sine is at least 24247/25088>24/25.
Oddness supplies the negative-band estimate. Each upper-branch
multiplier error is at most (25/48)49^(-(m+1)); adding their absolute
integrals gives (25/24)49^(-(m+1))||nu_U||_TV, uniformly for real gamma.
The floor inequality m+1>(n-6)/12 gives the factor 7. Inserting (5)
yields exactly the first term in (3), including 525/4. For the entire
lower response, ||R_L||<=2||nu_L||_TV and ||H_L||<=||nu_L||_TV;
the full operator norm then yields the second term with 2n^2+1.

The first three positive terms of the log7 series give the strict
lower bound 4803/2560, hence rho>161/5120=1/32+1/5120. After extracting
exp(-n/32), the upper polynomial is bounded by 5122, and the lower
polynomial by 2*96^3+4*64^2+34 as in (18). Thus C is independent of n,
mu and gamma. The same sequence (13), with A_n=0 below 48, satisfies
every epsilon allowance because n^2 exp(-epsilon n)<=4/epsilon^2;
no epsilon-dependent choice of m or operator is made.

Replayed the existing scalar script and inspected the complete /checks
object: all 18 checks pass, no failures, sine floor 24247/25088>24/25,
rho lower bound 161/5120>1/32. This certifies arithmetic only; the
all-n, measure, sign and operator checks are the analytic argument above.
Direct mathematical inputs remain exactly L997(4) and C997a(1)-(2).
Selected continuation/normalization, the original suppression/TV assay,
actual reconstruction, signed recovery, infinite-zero complements,
regulator uniformity, L993, L984(H) and actual-Xi positivity remain open.

## Mathlib

Full matching coverage for this finite-window branch-recovery statement
has not been checked and is unknown. The named generalized binomial
theorem, finite Fourier identities and complex-measure Fubini are used
as standard informal inputs, with the needed coefficient and variation
calculations written above; no claim about matching Mathlib theorem
names or absence is made. The Laguerre input retains L997's qualification.
