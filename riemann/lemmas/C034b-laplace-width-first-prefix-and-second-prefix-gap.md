# Corollary C034b: first Laplace-width prefix; second prefix unresolved

## Hypotheses

Use C033w's qualified actual laws and positive-real identification,
with precisely k(j,sigma)=exp(-b_sigma(sqrt(j))), j=1,2, 1<=sigma<=2.
Use C032m's entire lifts and C032n's first-width regularity, including
all fixed complex derivatives, and its normalized evolution. Explicitly,

    G_sigma(z)=exp(-z^2/(4*sigma))/sqrt(4*pi*sigma),
    p_sigma(z)=(1/2)sum_rho[G_sigma(z-z_rho)+G_sigma(z+z_rho)],
    R_sigma(w)=integral_0^infinity
                     (p_sigma(x)-p_sigma(i*w))/(x^2+w^2) dx,
    E_sigma(w)=4*integral_0^w t*R_sigma(t) dt,
    O_sigma(w)=2*pi*integral_0^w p_sigma(i*t) dt,
    b_sigma=E_sigma+O_sigma, a_sigma=b_sigma''(0)=4*R_sigma(0),
    partial_sigma b_sigma(w)=-b_sigma''(w)+a_sigma.

The quotient includes its continuous removable values and both
primitives vanish at zero. Primes denote complex w derivatives except
where differentiation of a real spatial profile is specified. Width
sigma is Gaussian half-variance. Width differentiation is justified
on the open neighborhood (1/2,3), not just at interior widths of [1,2].

The full positive-ordinate divisor has z_rho=gamma_rho-i*delta_rho,
gamma_rho>14, |delta_rho|<1/2, conjugation invariance and multiplicities.
Retain N(T)=O(T log(T+2)) and the actual retained real zero with ordinate
r in (14,15). Retain C033w's excluded ordinate zero, verified-height100,
reciprocal-square-tail, heat-positivity and separate fixed-j error
qualifications, both fixed-v1 preprint qualifications, and zero drift
and killing. These sources and finite-zero data are not independently
verified here. The estimates below do not require p_sigma>=0, RH,
reality of the remaining zeros, or odd-kernel signs. The nonempty
divisor is essential for strictness; the retained zero also gives the
optional numerical lower bound below.

## Conclusion

Put S4=sum_rho gamma_rho^(-4), w_j=sqrt(j), k_j(sigma)=k(j,sigma), and

    d_j=partial_sigma b_sigma(w_j),
    e_j=partial_sigma^2 b_sigma(w_j).

These are real continuous functions, k_j is C^2 on a neighborhood
of [1,2], and the following identities and bound hold at both endpoints:

    e_j=b_sigma''''(w_j)-b_sigma''''(0),
    k_j'=-k_j*d_j,   k_j''=k_j*(d_j^2-e_j),                 (1)
    d_j>(j/2)*S4>j/(2*15^4)>0, j=1,2.                    (2)

Here k_j primes in (1) are width derivatives. Consequently the first
nonconstant prefix of (1,k_1,k_2) satisfies

    W(1,k_1)=k_1'<-k_1*S4/2<0.                           (3)

For the final prefix, with rows indexed by width derivative order,

    W(1,k_1,k_2)=k_1*k_2*T,
    T=d_1*d_2*(d_1-d_2)+d_1*e_2-d_2*e_1.                (4)

Its sign and nonvanishing remain unproved. If K=K_3 is C032m's
uniform bound for |b_sigma(w)| on |w|<=3, the achieved unsigned bound is

    T in [-C,C], C=64*K^3+384*K^2>0.                      (5)

Thus (5) does not separate the second prefix from zero. The completed
attempt1839 establishes only (2)-(3), not the ECT criterion, the
fixed three-width matrix's nonsingularity, or a determinant zero.
The partial result passes conceptual audit1841 below under exactly the
stated hypotheses; the final-prefix sign is still unresolved.

## Proof

### 1. Source scope and the normalized second derivative

The preexisting EXPLORE assessment1838 covers this exact Laplace-prefix
test. Its source comparison distinguishes C033g/k's odd kernel, their
parked third-width bound, fixed-kernel Hankel positivity and conditional
inverse verification from the present width-dependent Laplace family.
C033m already has second-width Gaussian regularity; merely obtaining
regularity again would not be a new sign input. The additional work
here is the full-divisor signed estimate (2).

The general Gaussian heat identity is imported through C032n from
James Nolen, *Partial Differential Equations and Diffusion Processes*,
Section2.3, (3.17), P0-P1, printed pp14-17,
[Stanford notes](https://math.stanford.edu/~ryzhik/STANFORD/STANF227-10/notes227-09.pdf).
The compact holomorphic integration input used in C032m/n is Friedrich
Haslinger, *Complex Analysis*, Section2.7, Theorem2.39, pp67-68,
[author notes](https://www.mat.univie.ac.at/~has/scriptneu.pdf).
Their general results are not reproved. C032n's Gaussian normal
convergence, integrable spatial majorants and removable quotient
checks are the inputs to every exchange below; neither source is
being applied directly to an unqualified complex divisor.

C032n states that each fixed complex derivative of b is C^1 in
width, with jointly continuous first-width derivative and locally
uniform disk bounds. Hence its exact normalized identity can be
differentiated in width once more. Commuting the already justified
fixed complex derivatives gives

    partial_sigma b_sigma''(w)=-b_sigma''''(w),
    partial_sigma a_sigma=-b_sigma''''(0),
    partial_sigma^2 b_sigma(w)=b_sigma''''(w)-b_sigma''''(0).

This proves C^2 width regularity with continuous second derivative.
It does not differentiate an inequality, discard a primitive constant,
or require a new noncompact integral differentiation theorem.
Composition with the real fixed w_j and the exponential proves (1).
Reality follows from conjugation invariance and the real primitives;
k_j>0 follows from its real exponential, independently of law positivity.

### 2. Exact positive weight with the origin subtraction retained

C032n(14), for real w>0, states

    b_sigma'(w)=4*integral_0^infinity p_sigma(x)*w/(x^2+w^2) dx.

Differentiate once in w on a compact positive-real interval. C032n's
weighted Gaussian majorant justifies this exchange: the differentiated
rational factor is bounded on compact x intervals and O(x^-2) at
infinity. Since

    integral_0^infinity (x^2-w^2)/(x^2+w^2)^2 dx=0,

one may subtract p_sigma(0) inside the resulting integral. The last
identity also follows directly by integrating -d[x/(x^2+w^2)]/dx.
Using a_sigma=4*integral_0^infinity(p_sigma(x)-p_sigma(0))/x^2 dx
then gives, for s=w^2 equal to 1 or 2,

    partial_sigma b_sigma(sqrt(s))
       =integral_0^infinity (p_sigma(x)-p_sigma(0))*Q_s(x) dx,
    Q_s(x)=4*s*(3*x^2+s)/(x^2*(x^2+s)^2)>0.              (6)

At zero, p_sigma(x)-p_sigma(0)=O(x^2) uniformly in width by evenness
and the compact derivative bounds. At infinity Q_s=O(x^-4).
Thus (6) is an ordinary absolutely convergent integral, not a principal
value. Replacing p_sigma(x)-p_sigma(0) by p_sigma(x) would be invalid.

For each divisor member define the real even function

    h_rho(x)=Re((G_sigma(x-z_rho)+G_sigma(x+z_rho))/2).

Normal convergence and conjugation give p_sigma(x)=sum_rho h_rho(x).
The sum of integrals of |h_rho(x)-h_rho(0)|*Q_s(x) is finite.
On [0,1], Taylor's theorem and the summable Gaussian second-derivative
majorant used below prove this. On [1,infinity), Q_s<=12*s/x^4,
the absolute Gaussian series is bounded by C032n's P(x), and
integral_1^infinity P(x)/x^2 dx<infinity. The constants h_rho(0)
also form an absolutely summable series. Tonelli on these absolute
majorants, followed by Fubini, therefore allows (6) to be summed
member by member. No conjugate or multiplicity is discarded.

### 3. A weighted Gaussian estimate for every ordinate

Fix gamma>14 and |delta|<1/2, and suppress rho and sigma in h.
For x>=1, 1<=sigma<=2, the elementary bound needed for both translates is

    x^(-4)*exp(-(x-gamma)^2/(8*sigma))<6*gamma^(-4),
    x^(-4)*exp(-(x+gamma)^2/(8*sigma))<6*gamma^(-4).     (7)

It suffices to prove the first with 8*sigma replaced by16; the
second follows because (x+gamma)^2>=(x-gamma)^2. If x>=gamma, the
claim holds with constant1. If gamma/2<=x<=gamma, set y=gamma-x.
Since log(gamma/x)<=2*y/gamma,

    4*log(gamma/x)-y^2/16
        <=8*y/gamma-y^2/16<=256/gamma^2<3/2.

If 1<=x<=gamma/2, put F(x)=4*log(gamma/x)-(gamma-x)^2/16.
Its derivative is (-x^2+gamma*x-32)/(8*x). On this interval it
can change sign only from negative to positive: the larger quadratic
root is greater than gamma/2. Therefore the maximum is at an endpoint.
At gamma/2, F=4*log2-gamma^2/64<4-196/64<3/2.
At1, F=4*log gamma-(gamma-1)^2/16 decreases for gamma>=14,
and is less than 12-169/16=23/16<3/2, using log14<3.
Finally exp(3/2)=e*sqrt(e)<6. This proves (7) without sampling.

The elementary constants used throughout are 3<pi<4, 8/3<e<3,
exp(3)>16, exp(1/16)<=16/15, and exp(-1/4)>=3/4.
They follow from the exponential series or exp(t)>=1+t;
for exp(1/16) use its series bounded by sum_(n>=0)(1/16)^n.
In particular exp(3)>16 follows already from terms through degree4,
and implies log14<3. No numerical zero coordinates enter these bounds.

### 4. The positive core and both possible negative-phase tails

For x in [gamma-1,gamma+1], the positive-center translate has
|x-gamma|<=1 and |delta*(x-gamma)/(2*sigma)|<=1/4. Thus

    Re G_sigma(x-gamma+i*delta)
       > (1/6)*(3/4)*(31/32)=31/256.                    (8)

Here sqrt(4*pi*sigma)<6, the real Gaussian is at least exp(-1/4),
the factor exp(delta^2/(4*sigma)) is at least1, and
cos(v)>=1-v^2/2>=31/32. Also, on this interval, for s=1 or2,

    x^2+s< (7/6)*gamma^2,
    Q_s(x)>=12*s/(x^2+s)^2>8*s/gamma^4.

For the first inequality, (gamma+1)^2+2 divided by gamma^2 is at
most227/196<7/6. The contribution from this positive core of the
first translate, including the factor1/2 in h and its length2,
therefore exceeds

    (31/32)*s/gamma^4.                                  (9)

Other positive contributions may be dropped in a lower bound, but
all possible negative contributions from both translates must be paid.
Write u=x-gamma or u=x+gamma. If Re G_sigma(u+i*delta)<0, then
|delta*u/(2*sigma)|>pi/2, hence |u|>2*pi*sigma. For delta=0 there
is no negative part. Always

    |G_sigma(u+i*delta)|
       <=(16/15)/sqrt(4*pi*sigma)*exp(-u^2/(4*sigma)).

Use Q_s<=12*s/x^4 and (7) for half the exponential. With
a=2*pi*sigma the remaining whole-line Gaussian tail satisfies

    integral_(|u|>=a) exp(-u^2/(8*sigma)) du
       <=(8*sigma/a)*exp(-a^2/(8*sigma))
       =(4/pi)*exp(-pi^2*sigma/2).

This follows by bounding 1<=|u|/a on each tail and integrating.
Extending the translated domain x>=1 to this full tail only enlarges
the nonnegative upper bound. For either translate, including its
factor1/2, the entire negative contribution on x>=1 is less than

    (s/gamma^4)*(256/15)*exp(-9/2)
       <(9/40)*s/gamma^4.                               (10)

For the first constant use pi>3 and sqrt(4*pi*sigma)>3.
For the second, exp(9/2)=e^4*sqrt(e)>(8/3)^4*(3/2)=2048/27.
Thus the sum of both negative parts costs less than (9/20)*s/gamma^4.
This explicitly pays the complex phases rather than replacing them
by positive real-zero Gaussians.

### 5. Origin interval and constant subtraction

For 0<=x<=1, h'(0)=0. Put u=x-gamma or x+gamma, so |u|>=gamma-1>13.
The differentiated Gaussian and |delta|<1/2 give

    |G_sigma''(u+i*delta)|
       <=(16/45)*(u^2/4+9/16)*exp(-u^2/8).

The function (u^2/4+9/16)*exp(-u^2/8) decreases for u>=13.
Consequently the same bound for the average h'' implies

    sup_(0<=x<=1)|h''(x)|
       <=(4/45)*gamma^2*exp(-(gamma-1)^2/8).              (11)

Indeed (gamma-1)^2+9/4<=gamma^2. Taylor's theorem gives
|h(x)-h(0)|<=x^2*sup|h''|/2. Since
(3*x^2+s)/(x^2+s)^2<=3 on this interval for s=1,2, (6) yields

    |integral_0^1(h(x)-h(0))*Q_s(x) dx|
       <=6*s*sup|h''|
       <=(8/15)*s*gamma^2*exp(-(gamma-1)^2/8)
       <(2/125)*s/gamma^4.                              (12)

For the strict last bound, gamma^6*exp(-(gamma-1)^2/8) decreases
for gamma>=14 and is less than 14^6/16^7<3/100, since
(14-1)^2/8>21 and exp(21)>16^7. The last integer comparison is
100*7529536<3*268435456. These same estimates, with the counting
bound, supply the summable origin majorant asserted after (6).

On x>=1 the subtraction of h(0) costs at most

    |h(0)|*integral_1^infinity Q_s(x) dx
       <=(64/45)*s*exp(-gamma^2/8)
       <s/(10000*gamma^4).                              (13)

Here |h(0)|<=(16/45)*exp(-gamma^2/8) and the integral is at most4*s.
The function gamma^4*exp(-gamma^2/8) decreases for gamma>=14.
Its value is less than 14^4/16^8<1/100000, using gamma^2/8>24
and exp(24)>16^8; explicitly 100000*38416<4294967296.
This proves (13) with room to spare, with no sign assumption on h(0).

Combining (9), both copies of (10), (12) and (13), the complete
single-member contribution to (6) is strictly greater than

    (s/gamma^4)*(31/32-9/20-2/125-1/10000)
       =(s/gamma^4)*(10053/20000)
       >(s/(2*gamma^4)).                                (14)

The absolute summability already proved permits summing this lower
bound over the complete divisor. The count implies S4<infinity;
the retained member r<15 gives S4>15^(-4). Hence (2) and (3) follow.
No cutoff tail, off-line member, conjugate or multiplicity is omitted.

### 6. Final prefix, achieved bound and stopping point

Expanding the determinant with its first column (1,0,0) and using
(1) gives (4) exactly. Since d_1,d_2>0, its sign is equivalently the
sign of

    T/(d_1*d_2)=d_1-d_2+e_2/d_2-e_1/d_1.                (15)

The first-prefix proof supplies no sign for this combination. In
particular the signed curvature correlation d_1*e_2-d_2*e_1 is
not bounded by assigning independent signs to the Gaussian phases.
Nor has d_2-d_1 been established by the two separate lower bounds (2).

For an explicit account of the available unsigned control, let
K=K_3=18*B_3+6*pi*A_3 be the finite positive C032m disk bound.
Unit circles about 0,1,sqrt(2) lie inside |w|<=3. Cauchy's formula
therefore gives |b''|<=2*K and |b''''|<=24*K at all three points,
uniformly for sigma in [1,2]. Thus

    0<d_j<=4*K, |e_j|<=48*K, |d_1-d_2|<=4*K.

Substitution in (4) gives precisely (5). The required threshold is
a strict one-sided bound for T, or another rigorous proof that it
never vanishes throughout the closed interval. The symmetric bound
(5) contains zero at every width. It is inconclusive and is not a
zero, opposite-sign certificate or obstruction to the fixed-site matrix.

The classical all-prefix criterion is Douglas D. Novaes and Joan
Torregrosa, *On extended Chebyshev systems with positive accuracy*,
UAB prepublication13, July2015, printed p2 and Section2 pp5-6 (5)-(9),
[primary PDF](https://mat.uab.cat/dpt/Publ/prep/p13_15.pdf), later
J. Math. Anal. Appl.448(2017),171-186,
[DOI](https://doi.org/10.1016/j.jmaa.2016.10.076).
Assessment1838 inspected its closed-interval C^r, r>=n hypotheses
and the nonvanishing division-derivation proof. Here n=2 and the
regularity, constant prefix1 and first nonconstant prefix are paid.
Its final-prefix hypothesis is not. The theorem is therefore not
invoked to infer nonsingularity at widths1,3/2,2.

Stop this full-prefix attempt here under assessment1838. A later
development needs a materially new signed estimate for (15), with
source review if outside existing coverage; a finer version of the
parked odd-kernel cover or the symmetric disk bound is insufficient.
Inverse bounds, entries and residual m, exact weights, TV<=2, the
full observation interval, cancellation and actual-Xi realization
remain unpaid. L030-L032/C032a actual-Xi positivity is unchanged.
The source search did not establish prior coverage of (2), which is
not a claim of originality. The classical tools and regularity are
reused inputs; the local partial sign estimate is the new notebook work.

### Conceptual audit1841 — 20 November 2026

The full stated partial conclusion passes under unchanged EXPLORE
assessment1839, separately source-approved1840. This is verification
of attempt1839, not a stronger estimate or an originality claim. No
mathematical correction, extra sign premise or changed divisor is
required. The following checks cover (1)-(15), including both endpoints.
The general sources cited above are reused; their wider preprint and
finite-zero claims are not independently validated.

**Input interfaces and normalization.** C033w, through C033l/C032q,
identifies the qualified probability transform with exp(-b(sqrt(s)))
only at the positive real square root; both observation arguments here
are positive. The analytic proof uses C032m/n's actual divisor,
conjugation, multiplicity, strip and count. Probability interpretation
retains all additional hypotheses in this lemma; it is not needed to
infer positivity of a real exponential. The actual retained real zero
is used only for the displayed numerical floor for S4. C033g/k's
different odd kernel and C033m's regularity supply no sign premise.

C032n(8) supplies normal convergence bounds for the Gaussian series and
every fixed complex derivative of its first width derivative on [1/2,3]. Its (9)-(12)
provide a single integrable spatial majorant and include the removable
values at x=w=0. Its proof of (14) cancels p(i*w) against O', and
its integration-by-parts boundary terms vanish using (13) and evenness.
Thus the normalized identity used here holds on (1/2,3), with
b(0)=0 for every width. Applying the justified mixed derivatives to
that identity gives partial_sigma b''=-b'''' and
partial_sigma a=-b''''(0). Their difference proves exactly (1),
including the origin term. This establishes continuous second width
derivatives at 1 and 2 as interior parameter points; no positivity
inequality was differentiated.

**Signed spatial integral and summation.** The w derivative of
w/(x^2+w^2) is (x^2-w^2)/(x^2+w^2)^2. Its integral is zero,
because it equals -partial_x[x/(x^2+w^2)], with zero boundary values
for real w>0. Subtracting p(0) from that integral and from a=4R(0)
therefore gives the positive rational weight in (6) exactly. Evenness
makes the numerator O(x^2) at the origin; the tail weight is O(x^-4).
For each member h, evenness gives h'(0)=0, including nonreal members.
The second translate has imaginary displacement -delta rather than
+delta; the real cosine and absolute Gaussian estimates are unchanged.

On [0,1], (11) bounds the sum of suprema of |h''| by a convergent
polynomial-times-Gaussian series, using the counting hypothesis. On
[1,infinity), the sum of |h| is bounded by a constant times C032n's
P(x), and Q_s<=12s/x^4<=12s/x^2. Also sum |h(0)| is finite and
integral_1^infinity Q_s<=4s. These bounds prove the asserted sum of
absolute integrals is finite, uniformly in the closed width interval.
Tonelli/Fubini apply to these bounds before any signed inequality is
summed. Conjugation identifies sum h with p without deleting either
member of a conjugate pair or changing its multiplicity.

**Whole-tail and rational-constant checks.** In (7), for
y=gamma-x in [0,gamma/2], the quadratic upper bound has maximum
256/gamma^2<3/2. On [1,gamma/2], the larger stationary root is
above gamma/2, so the remaining possible stationary point is a
minimum. The endpoint at 1 decreases with gamma>=14 since
4/gamma-(gamma-1)/8<0 there. Both endpoint bounds are below 3/2.
Thus the constant6 controls the entire x>=1 domain for both
translates; it is not merely a near-core estimate.

On [gamma-1,gamma+1], the real part of the first translate exceeds31/256;
((gamma+1)^2+2)/gamma^2<=227/196<7/6 makes Q_s>8s/gamma^4.
The averaging factor1/2 and interval length2 give31s/(32gamma^4).
For every possible negative phase, |u|>2pi*sigma. Splitting the
Gaussian exponential, using (7), and extending the remaining positive
tail integrand to both real rays gives, per translate,

    (1/2)*12*6*(16/15)*(1/3)*(4/3)*exp(-9/2)
       =(256/15)*exp(-9/2)<9/40.

The last strict inequality follows from
exp(9/2)>(8/3)^4*(3/2)=2048/27. Both tails together cost less
than9/20 in units s/gamma^4, even if they occur inside otherwise
discarded regions. The core is disjoint from [0,1]. No favorable
phase is presumed for any other part of either translate.

For (11), differentiating the Gaussian gives the modulus factor
u^2/4+9/16, and the prefactor is at most16/45. Its product with
exp(-u^2/8) decreases for |u|>=13. Since
(gamma-1)^2+9/4<=gamma^2, the claimed uniform h'' bound follows.
Taylor's factor1/2, the factor4s in Q_s and the bound3 for its
remaining rational factor give exactly6s*sup|h''| in (12).
The logarithmic derivatives of gamma^6 exp(-(gamma-1)^2/8) and
gamma^4 exp(-gamma^2/8) are respectively
6/gamma-(gamma-1)/4 and 4/gamma-gamma/4; both are negative for
gamma>=14. The integer comparisons in (12)-(13) are

    752953600 < 805306368,
    3841600000 < 4294967296.

Together with exp(3)>16 these imply the stated bounds2/125 and
1/10000, including the full constant subtraction on [1,infinity).
Consequently the exact remaining coefficient is

    31/32-9/20-2/125-1/10000
       =10053/20000=1/2+53/20000.

This verifies the required strict margin, rather than only a positive
floating-point preview. The count makes S4 finite, and a nonempty
divisor makes it positive. The retained member r<15 yields
S4>15^(-4). Absolute convergence permits summing (14); a single
strict positive remainder already ensures strictness of the summed
inequality. Thus (2)-(3) follow with the stated factors of j.

**Final prefix and limits of the pass.** Expansion along (1,0,0)
gives k_1'k_2''-k_2'k_1'', which is exactly (4). Division in (15)
is legitimate because both d_j are now strictly positive. C032m(8)
gives K_3=18B_3+6pi A_3. The three unit circles lie strictly inside
the radius3 disk, so |b''|<=2K_3 and |b''''|<=24K_3. Hence
|d_j|<=4K_3, |e_j|<=48K_3, and
|d_1-d_2|=|b''(sqrt(2))-b''(1)|<=4K_3. The cubic and two
mixed products in (4) cost at most64K_3^3 and384K_3^2. This
verifies (5), whose interval contains zero. No ordering of d_1,d_2
and no sign of their curvature correlation follows from the audit.
The cited all-prefix ECT criterion is correctly left unapplied.

Full final-prefix nonvanishing, fixed-site nonsingularity, inverse
control, entries/residual, weights/TV, full observations, cancellation
and actual-Xi realization remain unresolved. The full-prefix stop1839
is unchanged. The direct inputs remain C032m, C032n and C033w; no
dependency is added by the audit, and no new mathematical script or
numerical certificate is used.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is used. Cauchy estimates, Gaussian differentiation, real integration
and finite determinant identities may have supporting APIs, but no
matching theorem for (2), the complete actual-divisor construction,
or its qualified preprint inputs is asserted. This remains an informal,
source-qualified partial result; conceptual audit1841 verifies its
local proof, without asserting source-wide validity or formalization.
