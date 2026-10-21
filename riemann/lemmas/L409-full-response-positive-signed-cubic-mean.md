# Lemma 409: full-response positive signed cubic mean

## Hypotheses

Use the actual functions and ordinary jets of L406 and L407 on t>=40:

    c=1/(4pi), ell=log H, L=log(2+t),
    (x,y,z)=(f,f'/L,f''/L^2), R=exp(i phi), E=R^2,
    Z=sum_(n>=1) n^(-5/2-it), b=z-x/4,
    M=(z^2+3xz/2+x^2/16-y^2)/2, K=(b-iy)^2/2,
    d=c^2[M|Z|^2+Re(K E Z^2)],
    B0=-c[b Re(RZ)+y Im(RZ)].

Let d_N,B0_N be the same expressions with Z replaced by its head n<=N.
Delta and Bcal are the exact physical quantities in L406, including
the full response and its ordinary derivatives. H tends to infinity
through real values; N is held fixed in every inner height limit.
Use the audited L408 fixed-N coefficient and L407 exact weights and
contour bounds. No RH, phase independence, clipping, favorable margin,
or asymptotic uniform in a growing response head is assumed.

## Conclusion

Put u=mn/gcd(mn,k) and A_u=u^(-2) sum_(a=1)^u gcd(a,u). Then

    beta=(17 c^3/20160)
           sum_(m,n,k>=1) (mn)^(-2) k^(-3) A_u,
    0<17 c^3/20160<=beta<=(17 c^3/20160) zeta(2)^2 zeta(3). (1)

The series is absolutely convergent. Both complete sharp means satisfy

    integral_[H,2H] d B0 dt=beta H ell^2+o(H ell^2),
    integral_[H,2H] Delta Bcal dt=beta H ell^2+o(H ell^2).    (2)

In particular the required signed response-tail passage is valid:

    lim_(N->infinity) limsup_(H->infinity)
      |integral_[H,2H] (d B0-d_N B0_N)dt|/(H ell^2)=0.        (3)

This is a local REPRODUCTION specialization of the assessed kernel
estimate and audited inputs. The separate step-119 critical audit below
validates (1)--(3). It
does not establish a clipped mean, regulator choice, total L367 margin,
actual common-zero upper count, global mixed positivity or RH.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-14-full-response-cubic-passage.md`.
The finite coefficient algebra and Hurwitz calculation in L408 are
reused without change. The missing application obligation is summable
response-parameter dependence; an O_N error would not establish it.
The earlier L394/L399/L400 failures concern different weights and are
contrasts, not mathematical premises. No general cubic-moment theorem
or growing-modulus residue formula is being asserted or reproved.

### 1. Exact carrier expansion and summable sharp connectors

Use L407 (3)--(5), (8) with a=21/20, delta=a-1/2=11/20.
For each of its finitely many monomials nu, write dnu=nu1+2nu2<=6
and C_nu(j) for its exact ordinary-derivative Dirichlet coefficient.
In the estimates below D denotes dnu, not the physical discriminant.
For every fixed eta>0, the coefficient bound in L407 gives

    |C_nu(j)|<=C_eta j^eta [log(2j)]^D,
    sum_j |C_nu(j)|j^(-a)<infinity.                         (4)

The second assertion follows by choosing eta<a-1. The j=1
coefficient is retained. Fix eta=1/100 for the rest of the proof.
The exact weights w_(e,nu) obey L407 (5) on the height rectangle:

    |w|<=C ell^(-D), |w'|<=C ell^(-D)/H.                   (5)

For each response triple put alpha=(mnk)^(-5/2). Its single-carrier
twist is r=mn/k; its zero-carrier twist is r=mnk. The identity L407
(3) extends to the full response by absolute convergence on the real
segment, or by taking heads there. On the entire contour rectangle,
for 0<=q<=delta,

    |r^(s-1/2)|=r^q<=1+r^delta.

Both response sums of alpha(1+r^delta) are finite: in the first
case the exponents of m,n are -39/20 and of k are -61/20;
in the second all three are -39/20. This also proves normal
convergence on a neighborhood of the rectangle: allow
-epsilon<=q<=delta+epsilon for a small fixed epsilon>0, still
strictly inside (-3/2,3/2), so the corresponding power sums converge
at both ends. Thus the response expansions
and integrals can be interchanged; no off-line conjugation is used.

L407 (5), (7) bound each weighted sharp connector, with its twist
factor now explicit, by

    C(1+r^delta) H^(71/120)       (single carrier),
    C(1+r^delta) H^(1/2)          (zero carrier).           (6)

Indeed the critical derivative logarithms cancel ell^(-D).
The single-carrier exponent is sigma-1/2+(5/6)(11/10-sigma),
whose maximum is 71/120 on 1/2<=sigma<=21/20; the zero-carrier
maximum is 1/2. Both connectors have fixed length. These are the
audited L407 estimates with the factor r^(sigma-1/2) retained.
Summing (6) over all triples therefore costs O(H^(71/120)).

### 2. Imported frequency kernel and a uniform rational-twist bound

Import M. B. Milinovich and N. Ng, *Lower bounds for moments of
zeta'(rho)*, author-hosted 19-page manuscript, Lemma 6.1, p. 9,
[complete frequency-level bound](https://home.olemiss.edu/~mbmilino/Lower_Bounds.pdf#page=9),
retrieved in the prior assessment on 2026-10-14 (no reliable version
date is printed). For x>0 and fixed 0<kappa0<=kappa<=2 it states

    (1/(2pi i)) integral_(kappa+i)^(kappa+iV)
                          chi(1-s)x^(-s) ds
      =1_(x<=V/(2pi)) exp(-2pi i x)
       +O(x^(-kappa)[V^(kappa-1/2)
          +V^(kappa+1/2)/(|V-2pi x|+sqrt(V))]).           (7)

The constant is independent of x and V in the indicated range.
We use only kappa=a and V>=H large. This analytic lemma is
unconditional; conditional zero-moment conclusions elsewhere in the
manuscript are not inputs. Its proof uses S. M. Gonek, *Mean values of
the Riemann zeta-function and its derivatives*, Invent. Math. 75 (1984),
Section 3, Lemma 2, p. 130,
[saddle, endpoint and exterior cases](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=8).
The assessment inspected those cases. We import stationary phase rather
than reprove it. Formula (7) uses the complete chi kernel, so includes
both exponential branches of L407 (6).

For every positive real r, apply (7) with x=j/r, multiply by
2pi r^(-1/2) C_nu(j), and sum over j. The right-line Dirichlet
series is absolutely integrable on every finite segment by (4).
Subtract the primitives at H and V, H<=V<=2H. The exact unweighted
primitive of r^(s-1/2) E F_nu(s), in the dt convention, has main term

    2pi r^(-1/2)
       sum_(H<2pi j/r<=V) C_nu(j) exp(-2pi i j/r).         (8)

The coefficient-summed error at either endpoint is at most a constant
times

    H^(a-1/2) r^(a-1/2) sum_j |C_nu(j)|j^(-a)
      +H^(a+1/2)r^(a-1/2)
         sum_j |C_nu(j)|j^(-a)/(|V-2pi j/r|+sqrt(V)).     (9)

Here and below constants depend only on the fixed finite monomial
set and eta, never on r,N,H,V. We now justify the required summation
instead of importing uniformity from a fixed-twist O_N bound.

Outside rH/(4pi)<=j<=2rH/pi, the denominator in the second sum
is at least cH, since H<=V<=2H. Its contribution is therefore
O(H^(11/20)r^(11/20)), by (4). In the indicated band j is
comparable to rH. If the band contains no positive integer its
contribution is zero; otherwise rH is bounded below by a positive
absolute constant. Equation (4) then gives

    |C_nu(j)|j^(-a)
       <=C(rH)^(eta-a)[log(2+rH)]^D.                    (10)

For the remaining denominator sum, the points 2pi j/r have spacing
2pi/r. At most two are nearest to V. Their contribution is
O(H^(-1/2)). Group the others by distance in successive intervals
of length 2pi/r; each interval contains at most two points. Comparing
the decreasing function 1/(sqrt(H)+2pi x/r) with its integral,
up to O(rH) points, gives, uniformly even when rH is small,

    sum_(rH/(4pi)<=j<=2rH/pi)
         1/(|V-2pi j/r|+sqrt(V))
           <=C[H^(-1/2)+r log(2+H)].                   (11)

Equations (9)--(11), using a=21/20, bound the unweighted error by

    C H^(11/20)r^(11/20)
      +C H^eta r^(eta-1/2)[log(2+rH)]^D
                                      [1+sqrt(H)r log(2+H)]. (12)

This covers arbitrarily small or large r and exact endpoint saddles.
At equality the right-continuous convention in (7) gives exactly
H<2pi j/r<=V; no endpoint is silently omitted.

Now apply Stieltjes integration by parts against w(t-i delta), as
in L407. The uniform primitive error is multiplied by
|w(2H-i delta)|+integral_H^(2H)|w'(t-i delta)|dt<=C ell^(-D).
Since log(2+rH)<=C ell(1+log_+r) for H large, the weighted
single-carrier integral equals S_(r,nu,w) in L407, with error at most

    C[H^(11/20) r^(11/20)
       +H^(1/100) r^(-49/100)(1+log_+r)^D
       +H^(51/100) ell r^(51/100)(1+log_+r)^D].          (13)

Both endpoints and all variation terms are included. No derivative
of an unspecified error or asymptotic weight is used.

All three r factors in (13) are summable against alpha for r=mn/k.
In general, alpha r^q=m^(-5/2+q)n^(-5/2+q)k^(-5/2-q);
absolute summability holds for -3/2<q<3/2, also with every fixed
power of log_+r. The powers in (13) lie strictly inside this range.
Consequently the full response-summed error is

    O(H^(11/20)+H^(1/100)+H^(51/100)ell)=o(H ell^2).     (14)

The same bound holds for every subcollection of response triples.

### 3. Main sums and all zero-carrier resonances

It remains to dominate the signed main terms at the correct scale.
For Y>=1, counting the ordered divisor triples as in L407 yields

    sum_(j<=Y) d_3(j)<=Y(1+log Y)^2.

Indeed the first two indices sum reciprocals at most
(sum_(n<=Y)1/n)^2. Bounding each log factor by log(2Y) and using
(5), the full absolute mass of S_(r,nu,w), whose j satisfy
j<=rH/pi, is at most

    C H sqrt(r) ell^2 (1+log_+r)^(D+2).                (15)

If rH/pi<1 the sum is empty. Otherwise the asserted bound follows
from log(2rH/pi)<=C ell(1+log_+r); it does not require r fixed.
Thus the majorant

    B(m,n,k)=(mnk)^(-5/2) sqrt(mn/k)
                              (1+log_+(mn/k))^8           (16)

is summable: its power part is (mn)^(-2)k^(-3), and the logarithm
is at most log m+log n. In particular its tail over max(m,n,k)>N
tends to zero. This bound does not assert a sign for an individual
arithmetic sum or replace it by its modulus as an identity.

For the zero carrier r=mnk is an integer. Separate j=r on the
right line. Its exact contribution is

    T_(r,nu,w)=r^(-1/2) C_nu(r)
                            integral_[H,2H]w(t-i delta)dt. (17)

By (4)--(5), its absolute value is at most
C H r^(-49/100)[log(2r)]^D, after harmlessly dropping ell^(-D).
This is summable against alpha, with total O(H), including r=1.

For j!=r the unweighted oscillatory primitive has modulus at most

    2r^(a-1/2)
         sum_(j!=r)|C_nu(j)|j^(-a)/|log(r/j)|.           (18)

Outside r/2<j<2r, |log(r/j)|>=log 2 and (4) applies. Inside,
the mean-value theorem gives |log(r/j)|>=|j-r|/(2r).
Use integer spacing, (4), and sum_(1<=h<=2r)1/h<=C log(2r).
These bound (18) by

    C[r^(11/20)+r^(51/100)(log(2r))^(D+1)].            (19)

The r=1 case is covered by the same bound, with an empty interior
sum if necessary. Partial summation with (5) preserves (19), again
dropping the factor ell^(-D)<=1. Both terms are summable against
alpha for r=mnk, because their powers are strictly less than 3/2;
the response-summed nonresonant error is O(1). Thus every zero-carrier
resonance and nearby integer frequency is controlled independently of N.

### 4. Full response identity and sequential limit

The exact full carrier identity, the contour shifts and (13), (17)
now give the full analogue of L407 (9): sum over every positive
m,n,k of its S_(mn/k,nu,w_(1,nu)) and T_(mnk,nu,w_(0,nu)),
with prefactor c^3 and final real part. The total error is

    O(H^(71/120)+H^(11/20)+H^(51/100)ell+H^(1/100)+1)
                                                    =o(H ell^2). (20)

All these series converge absolutely at each H by the displayed
majorants. One may equivalently sum the individually shifted identities;
(6), (13), (15), (17), (19) justify every interchange and the limit.
The same identity and majorants apply to the complement of any fixed
head cube. Set epsilon_N=sum_(max(m,n,k)>N) B(m,n,k), with B
from (16). From (15), the summed O(H) resonances, and (20),

    limsup_(H->infinity)
      |integral_[H,2H] (d B0-d_N B0_N)dt|/(H ell^2)
          <=C epsilon_N,       epsilon_N ->0.            (21)

This proves (3). In particular it does not attempt to use the
larger absolute cubic envelope O(H ell^(9/4)) at this scale.

Since 0<A_u<=1 (each of its u gcd terms is at most u), L408's
positive beta_N converge monotonically to the absolutely convergent
series beta in (1). The (1,1,1) term gives its stated lower bound.
For every fixed N the triangle inequality and audited L408 imply

    limsup_(H->infinity)
       |(H ell^2)^(-1) integral d B0-beta|
         <=C epsilon_N+|beta_N-beta|.

Let N tend to infinity only now. This proves the first equation
of (2), without any growing-N asymptotic. L406 (2) bounds the
absolute physical replacement by O(H ell^(5/4)); division by
H ell^2 tends to zero. This proves the second equation of (2),
retaining the full response derivatives and curvature already included
in L406. No relative error against Bcal or Delta is needed at zeros.

The result is an unclipped signed benchmark. A positive mean of the
product does not give its restriction to either sign of Bcal, nor
a sign for the total regulator pencil. Those and the main positivity
and zero-count gaps remain unresolved. The local proof is audited below;
it is not a candidate resolution of RH.

### Separate critical audit — 2026-10-14, step 119

This REPRODUCTION proof_audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-14-full-response-cubic-audit.md`. It reuses
the inspected primary kernel statement (7), L407's audited exact
coefficients and connector tools, L408's audited fixed-N coefficient,
and L406's audited absolute physical replacement. No fresh source
discovery or reproof of stationary phase is needed. The Gonek locator
above is corrected to Section 3; the mathematical statement is unchanged.

**Full continuation and both connectors.** For tau=t-iq the two
response continuations are sum n^(-5/2-q-it) and
sum n^(-5/2+q+it). Their absolute series converge locally uniformly
for -3/2<q<3/2. Thus the entire rectangle and a fixed neighborhood
are covered, with the same finite carrier identity as L407 (3).
The real-line conjugate has been continued by the second series,
not by conjugating a complex-height value. On 0<=q<=11/20,
r^q<=1+r^(11/20), including r<1. Both response patterns therefore
have summable connector bounds. The inherited jet exponent gives
sigma/6+5/12<=71/120 for the single carrier and at most 1/2 for
zero carrier; ell^D cancels its exact coefficient bound. The two
oriented connectors have fixed length and no poles are crossed.
Consequently their infinite sums are O(H^(71/120)), uniformly for
every subcollection of response triples. No fixed-twist constant has
been silently summed.

**Uniform frequency error, extremes and endpoint transitions.** In
(7), kappa=21/20 is in the specified compact range and x=j/r>0
for every r>0. The source constant is independent of x. Multiplying
by 2pi r^(-1/2) gives exactly the r^(a-1/2) factor in (9), while
ds=i dt gives the main factor 2pi. Absolute convergence of
sum |C_nu(j)|j^(-a) licenses summing the source identity before
subtracting its H and V primitives.

Outside the stated band, 2pi j/r is either below H/2 or above 4H.
Its distance from every V in [H,2H] is at least H/2. This gives
the first term in (12), without any assumption on the size of rH.
Inside the band, nonemptiness implies rH>=pi/2, so the comparison
in (10) remains valid even if there is just one lattice point.
For the lattice estimate, retain the at most two nearest points
separately, with bound 2/sqrt(H). Every other distance is bounded
below by a constant times its ordered index divided by r. With
O(1+rH) indices, integral comparison gives

    C H^(-1/2)+C r log(1+C sqrt(H)),

which proves (11) uniformly for tiny or huge r. In particular an
exact endpoint saddle is covered by the nearest-point term. The
H and V source indicators subtract to H<2pi j/r<=V; inclusion
of an endpoint in this arithmetic sum is part of the primitive
formula, even though the original integral is unchanged at a point.

Multiplication of (10)--(11) by H^(a+1/2)r^(a-1/2) gives
H^eta r^(eta-1/2) and H^(eta+1/2)r^(eta+1/2)log(2+H),
times the displayed logarithmic coefficient factor. This checks
every exponent in (12). For the shifted analytic weight, integration
by parts applies to the smooth primitive minus its finite step sum.
Its error is bounded by the primitive supremum times
|w(2H-i delta)|+integral |w'|; both endpoint primitive errors
were already included. No smoothness of an unspecified error is
assumed. Finally log(2+rH)<=C ell(1+log_+r), also for r<1.
This proves precisely (13).

For alpha r^q with r=mn/k the three exponents are
-5/2+q,-5/2+q,-5/2-q. At q=11/20,-49/100,51/100
they are all strictly below -1. Fixed logarithmic powers are harmless,
since log_+r<=log m+log n. Thus (14) is valid for the full sum
and every tail, with constants independent of N. Its largest power
of H is 11/20, strictly below the required first power.

**Absolute main majorant and integer frequencies.** In (15), let
Y=rH/pi. If Y<1 the main sum is empty. Otherwise the exact coefficient
bound by d_3(j)log(2j)^D and the elementary divisor count give
C r^(-1/2)ell^(-D)Y log(2Y)^(D+2). This is the claimed
C H sqrt(r)ell^2(1+log_+r)^(D+2), with no fixed-r restriction.
Since D<=6, the single summable majorant (16) covers all monomials.
Its m,n exponents are -2 and its k exponent is -3; every logarithm
is absorbed by the strictly convergent m,n sums.

For zero carrier r=mnk is always an integer. At j=r, the right-line
factor r^(a-1/2)j^(-a) is exactly r^(-1/2), proving (17)
independently of a. At r=1 the undifferentiated coefficient is retained;
derivative factors with positive order have log 1=0. The uniform
resonance bound has alpha r^(-49/100)log(2r)^D as its coefficient,
which is summable in all three indices and gives total O(H).
For j!=r outside (r/2,2r) the denominator is at least log 2.
Inside, |log(r/j)|>=|j-r|/(2r) and integer spacing makes the
sum of inverse nonzero distances O(log(2r)). The resulting exponent
is (a-1/2)+(eta-a)+1=51/100, exactly as in (19).
Both r^(11/20) and r^(51/100) with their logarithms are summable
against alpha when r=mnk. The small case r=1 needs no limiting
argument. Weight variation costs at most C ell^(-D)<=C. This
checks the full O(1) nonresonant right-line error, besides the
separately counted connectors.

**Sequential passage and physical statistic.** At each fixed H,
the preceding absolute majorants justify summing the individually
shifted identities and taking head limits. The cube-complement
identity follows from the exact cubic expansion; it is not an
absolute bound on the original oscillating cubic integrand.
The main terms on that complement are at most
C H ell^2 epsilon_N. The full resonance bound divided by
H ell^2 is O(ell^(-2)), and every term of (20) divided by
H ell^2 tends to zero uniformly in the subcollection. This proves
(21) with a constant independent of N.

Each A_u is strictly positive and at most one. Hence beta_N
increases to the finite beta in (1), and the term (1,1,1) supplies
its positive lower bound. Given any tolerance, first choose N so
that C epsilon_N+|beta-beta_N| is smaller than that tolerance;
then take H sufficiently large for this fixed N using L408.
There is no requirement that its onset be uniform in N. This is
exactly the claimed all-real-H asymptotic and the H-first passage.

L406 uses the identical x,y,z,c,Z,M,K and B0, with the full ordinary
response derivatives and both curvature corrections. Its absolute
error divided by H ell^2 is O(ell^(-3/4)). It therefore transfers
the complete signed mean without division at zeros, truncating the
physical response, or assuming either factor has a sign.

The audit validates (1)--(3), with no new direct mathematical input
and no change of coefficient or hypotheses. This is verified local
use of the assessed known tools, not a new source theorem or an RH
resolution. In particular the mean on either sign subset of Bcal
is not determined by this unconditioned signed benchmark.

## Mathlib

Full matching coverage of this sharp signed cubic asymptotic and
uniform response summation was not checked. The frequency kernel is
imported by precise primary citation; the parameter summation and
sequential passage are justified above. L407/L408/L406 retain the
citations and qualifications of their established inputs. No absence
from Mathlib or formal verification is claimed. This step uses no
numerical experiment or new mathematical script.
