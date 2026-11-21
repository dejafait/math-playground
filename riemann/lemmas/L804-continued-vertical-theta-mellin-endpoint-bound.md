# Lemma 804: the continued vertical theta-Mellin endpoint

## Hypotheses

Use the saddle and domain of L797 and the phase and principal branches
of L798:

    D={s: |s|>=6000, Re(s)>=-|s|/(8 log|s|)},
    c=9/4, F(z)=z(pi exp(2z)-c), F(x)=s, x=u+ih,
    q=pi exp(2x), Q=pi exp(2u), d=3/(16u),
    S_s(z)=2s Log z+(9/2)z-pi exp(2z),
    A=2F'(x)/x, B=|A|, theta=Arg A, a=exp(-i theta/2),
    C=sqrt(2pi/A), |C|=sqrt(2pi/B).

L797 gives u>3, |h|<pi/4-1/(4u), Q>1000, c/Q<1/400,
log|s|>2u, and conjugation symmetry. L798 gives Re A>0,
B<5Q and the nonzero denominator C. Use exactly L799's normally
convergent holomorphic series on U={z: |Im z|<pi/4}:

    P(z)=sum_{n>=1} [4pi^2 n^4 exp(9z/2)
                    -6pi n^2 exp(5z/2)] exp(-pi n^2 exp(2z)).

Use the actual L802 height, not the saddle height itself:

    x-da=v_L+i y_L,
    y_L=h+d sin(theta/2),
    |y_L|<pi/4-13/(112u).

L802 proves that y_L has the sign of h, |y_L|>=|h|, y_L=0 when
h=0, and y_L changes sign under conjugation. For every independent
fixed real y with 0<|y|<pi/4, initially define

    V(s,y)=integral_[0,i y] exp(2s Log z)P(z) dz,
    Re(s)>-1/2,

on the oriented straight segment, with principal Log off its endpoint
zero. Outside that half-plane, V means the fixed-y meromorphic
continuation proved below. Only afterwards is y=y_L(s) substituted.
For the actual h=0 case define V(s,0)=0.

The unchanged, separately approved SPECIALIZE assessment is
`drafts/literature/2026-11-05-mellin-vertical-endpoint-test.md`.
The source claim is bramble_trace, *A continuum certificate for the
decreasing Levy factor associated with Riemann xi*,
[paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
18 October 2026, Section3 Lemma2 (10)–(14), and the endpoint paragraphs
and 07:10:31 UTC revision of
[post20](https://rstation.ai/r/riemann_hypothesis/posts/20).
Neither its endpoint inequality nor its circle constant is assumed.

## Conclusion

For every fixed nonzero y in the stated range, V has a meromorphic
continuation to all s. If P(z)=sum_{n>=0}p_n z^n near zero, its only
possible poles are s=-(n+1)/2, n>=0, with residue p_n/2. Such a pole
is actual exactly when p_n!=0; p_0>0, so -1/2 is an actual pole.
No assertion that every listed pole is actual, or that odd coefficients
vanish, is needed. All fixed-height evaluations used on D avoid poles.

For every s in D,

    |V(s,y_L)|/|4pi^2 exp(S_s(x)) C| <= exp(-Q/2).       (1)

The proof gives the stronger strict bounds exp(-6Q/5) when
0<|h|<=1/2 and exp(-59Q/20) when |h|>1/2. The left side is zero
when h=0. The actual values V(s,y_L(s)) tend to zero as h tends to
zero along D, uniformly even when u is unbounded. In particular the
prescribed degenerate value agrees with the limits at positive real s.
No analyticity of the moving-height composite is asserted.

This is a known-method reproduction/specialization of a source
component, completed in step536 and independently audited in step538
below without a mathematical correction. It is local progress, with no novelty beyond the sources checked
claimed. It proves neither a global contour identity nor a combined
Mellin budget, quotient/inversion estimate, certificate or sufficient
actual-Xi sign implication. It is not an RH candidate.

## Proof

### Fixed-height continuation and its exact singularities

The standard continuation input is Taylor subtraction for a truncated
Mellin transform: D. Zagier, *The Mellin transform and other useful
analytic techniques*, appendix to E. Zeidler, *Quantum Field Theory I*,
Springer (2006), pp305–323, Section1, subtraction identity after (2),
[author PDF pp1–2](https://people.mpim-bonn.mpg.de/zagier/files/tex/MellinTransform/fulltext.pdf).
The finite-interval method is also described in
[DLMF2.5(ii), (2.5.17)–(2.5.25)](https://dlmf.nist.gov/2.5#ii).
Only that finite-interval component is used, with Mellin exponent
w=2s+1; no decay on an infinite imaginary ray is assumed.
Here analyticity of P permits an exact Taylor-series implementation,
which we spell out to verify the exponent, orientation and poles.

Fix y!=0 with |y|<pi/4, and choose any R with |y|<R<pi/4.
L799 gives holomorphy on a neighborhood of the closed radius-R disc.
Cauchy's formula gives

    P(z)=sum_{n>=0}p_n z^n,     |p_n|<=M_R R^(-n),
    M_R=sup_{|z|<=R}|P(z)|<infinity.                    (2)

The precise standard formulas used are
[DLMF1.9.30–31](https://dlmf.nist.gov/1.9#iii) and
[DLMF1.9.48](https://dlmf.nist.gov/1.9#vi); their contour and
analyticity hypotheses hold on this disc. The series converges
absolutely and uniformly on the segment in question.

Writing z=i y r for 0<r<=1, with its orientation included in dz,
gives for Re(s)>-1/2

    V(s,y)=(iy)^(2s+1) integral_0^1 r^(2s)P(iyr) dr
          =sum_{n>=0} p_n (iy)^(2s+n+1)/(2s+n+1).     (3)

Every power of iy uses the same principal Log(iy). Indeed
Log(iyr)=Log(iy)+log r on this oriented ray, also when y<0.
Termwise integration is valid since (2) supplies the summable majorant
M_R sum_{n>=0}(|y|/R)^n times r^(2 Re(s)), integrable at zero.

The series on the right of (3) converges normally on every compact
s-set avoiding {-(n+1)/2:n>=0}. To see this, |(iy)^(2s+1)| is
bounded on such a compact set; for all sufficiently large n,
|2s+n+1|>=n/2 uniformly there. Equation (2) then supplies a convergent
geometric majorant; the remaining finitely many denominators are
bounded away from zero. Thus (3) defines the meromorphic continuation
and agrees with the initial integral on its half-plane.

Equivalently, after subtracting N Taylor terms, the formula is

    V(s,y)=(iy)^(2s+1) [
       sum_{n=0}^{N-1}p_n(iy)^n/(2s+n+1)
       + integral_0^1 r^(2s)
           (P(iyr)-sum_{n=0}^{N-1}p_n(iyr)^n) dr ].  (4)

The remainder is O(r^N) for this fixed y. The integral is holomorphic
for Re(s)>-(N+1)/2: on every compact subset its absolute value is
bounded by a constant times r^(-1+epsilon) for some epsilon>0.
This verifies the singular-endpoint compact convergence required in
[DLMF1.10.18–19 and the integral M-test](https://dlmf.nist.gov/1.10#viii).
For consecutive subtraction orders, integrating the extra monomial
proves equality on their common convergence region, with the
denominator terms understood meromorphically. All orders therefore
agree with (3). No arbitrary regularization constant is introduced.

At s=-(n+1)/2 only the nth term of (3) can be singular; its numerator
equals p_n there and its denominator has derivative 2. Its residue
is p_n/2, independently of y. Hence its singularity is removable
exactly when p_n=0. At zero, the defining complete P series gives

    p_0=sum_{m>=1}2pi m^2(2pi m^2-3)exp(-pi m^2)>0,

because pi>3 and every summand is positive. This identifies an actual
pole without an unjustified parity assertion. All possible poles are
negative real. No negative real number belongs to D: for s=-r,
r>=6000, its defining inequality would require 8 log r<=1,
whereas L797's log r>2u>6 holds on D. Thus no pole is evaluated.

The defining series of P respects conjugation by normal convergence,
so its Taylor coefficients p_n are real. Formula (3) consequently gives

    V(conjugate(s),-y)=conjugate(V(s,y)).              (5)

The saddle, endpoint and normalization also respect conjugation by
L797/L798/L802 and their principal branches. It suffices below to treat
h>0, and then h=0. Write s=sigma+it and alpha=Arg x.
For h>0, L802 gives Q cos(2h)>c and y:=y_L>=h>0. Therefore

    sigma=Q(u cos(2h)-h sin(2h))-cu,
    t=uQ sin(2h)+h(Q cos(2h)-c)>0,
    0<alpha=arctan(h/u)<1/3.                         (6)

### A paid complete-kernel bound on the chosen circle

For each u>3 choose, only for estimates,

    R=pi/4-13/(224u),   beta=1/(50u).

Then 0<y<R<1 and R-y>13/(224u), by L802's height clearance.
The whole closed disc lies strictly inside U. For |z|<=R,

    Re(pi exp(2z))
      >=pi exp(-2R)cos(2R)
       =pi exp(-2R)sin(13/(112u))
       >39/(1792u)>beta.                            (7)

Here pi>3, exp(2)<8 and R<1 give pi exp(-2R)>3/8.
The sine argument is between zero and 1/6, so sin r>=r/2;
the last rational comparison is 39*50=1950>1792. These bounds
hold throughout the disc, not just at a sampled point of its circle.

The exponential bounds in L797 give e<11/4, whence e^5<200 and
e^3<21. Since pi<4 and |Re z|<1, each complete-series summand
is bounded in absolute value so that

    |P(z)|
      <=(4pi^2 e^(9/2)+6pi e^(5/2))
                              sum_{n>=1}n^4 exp(-beta n^2)
       <14000 sum_{n>=1}n^4 exp(-beta n^2).           (8)

In fact the coefficient is less than 64*200+24*21=13304.
The sum is bounded as follows, without assuming a circle constant
from the source. For v in [n-1,n], (v+1)^4>=n^4 and
exp(-beta v^2)>=exp(-beta n^2). Consequently

    sum_{n>=1}n^4 exp(-beta n^2)
      <=integral_0^infinity (v+1)^4 exp(-beta v^2) dv
      <=8 integral_0^infinity (v^4+1)exp(-beta v^2) dv
       =3sqrt(pi) beta^(-5/2)+4sqrt(pi) beta^(-1/2)
       <14 beta^(-5/2).                             (9)

The second inequality is convexity of the fourth power:
((v+1)/2)^4<=(v^4+1)/2. The Gaussian moment evaluations are the
real Gaussian integral and two integrations by parts, as explicitly
given in L798, after restricting the even integrals to the half-line.
Their boundary terms vanish and the integrands are integrable.
Finally beta<1 and sqrt(pi)<2 give the last inequality. Thus (8)
bounds the whole normally convergent P series and yields

    M_R<196000(50u)^(5/2)<4*10^9 u^(5/2).            (10)

Indeed sqrt(50)<8, so the numeric coefficient is less than
196000*2500*8=3920000000<4*10^9. No real or complex theta sign
has been used in this circle estimate.

All the prefactors can be paid uniformly by

    M_R sqrt(Q)<exp(Q/20).                          (11)

To verify this for every u>3, use sqrt(Q)<2exp(u) and e^2>7:
e^24>7^12=13841287201>8*10^9. Equations (10) and log u<u give

    M_R sqrt(Q)<exp(24+(5/2)log u+u)
                 <exp(12u)<exp(Q/20).

For the middle comparison, 24<8u and 8+5/2+1<12.
For the last, exp(2u)/u is increasing for u>=3, so L797 gives
Q/u>pi exp(6)/3>1000/3>240. Also L798 gives

    1/|C|=sqrt(B/(2pi))<sqrt(Q),   4pi^2>1.          (12)

Keeping the complete normalization, its phase contribution satisfies

    e^(-pi t)y^(2sigma) / |exp(S_s(x))|
       =exp(E),
    E=2sigma log(y/|x|)-t(pi-2alpha)
                                -(9/2)u+Q cos(2h).  (13)

This identity retains exactly the principal-power phase on the
imaginary ray. It is not a modulus-square replacement.

### Small heights: the convergent integral

Suppose 0<h<=1/2. L802 and |sin(theta/2)|<5/7 give

    0<y<h+15/(112u)<=1/2+5/112<3/5.

Since cos(2h)>=1-(2h)^2/2>=1/2 and h sin(2h)<=1/2,
the real part in (6) satisfies

    sigma>=Q(u/2-1/2)-cu
           >=uQ(1/3-c/Q)>uQ/4>0.                  (14)

Thus the original integral defining V converges. In particular no
continued-series denominator bound involving 1/t is used near h=0.
Equations (2), (6), and the oriented-ray expression give

    |V(s,y)|<=M_R exp(-pi t)y^(2sigma+1)/(2sigma+1).

Here the whole segment is in the chosen disc. Dividing by the exact
denominator in (1) and applying (12)–(13), using y/(2sigma+1)<1,
gives

    |V(s,y)|/|4pi^2 exp(S_s(x))C|<M_R sqrt(Q)exp(E). (15)

Now y/|x|<1/5 and log 5>3/2: the latter follows from
e^3<(11/4)^3<25. Also t>0 and pi-2alpha>0. Hence

    E<-3sigma+Q<-(3u/4-1)Q<-5Q/4.

Together with (11) and (15), this proves the asserted bound
exp(-6Q/5) throughout this entire regime, including h=1/2.

### Larger heights: the continued Taylor series

Suppose 1/2<h<pi/4. Since sin(2h)>=sin 1>=1-1/6=5/6
and cos(2h)>0, (6) implies

    t>(5/6)uQ-c>(3/4)uQ.                            (16)

Indeed h<1, and c/(uQ)<1/12 by u>3,Q>1000. In (3),
every denominator has modulus at least 2t, independent of sigma
and of its index. Cauchy's coefficient bounds (2) therefore give

    |V(s,y)|
      <=M_R exp(-pi t)y^(2sigma+1)
                              R/[2t(R-y)].          (17)

This is an absolutely convergent estimate of the meromorphic
continuation, not an ordinary integral in a possibly divergent
half-plane. The height clearance and (16) give

    R/[2t(R-y)]<448/(39Q)<1.                        (18)

Since y<1, (12)–(13) and (17)–(18) again give (15).

It remains to bound E even when sigma is negative. From L797,
|s|<(401/400)Q|x| and log|s|>2u. Also h<1,u>3 imply
|x|/u<sqrt(10/9)<16/15. The defining inequality of D, including
its equality boundary, consequently yields

    sigma>=-|s|/(8 log|s|)>-(401/6000)Q>-Q/14.       (19)

The final comparison is 401*14=5614<6000. With y>=h>1/2,

    1<|x|/y<(32/15)u<3u,    log(3u)<u.             (20)

The last inequality holds at u=3 since e^3>14>9, and its gap
u-log(3u) is increasing thereafter. If sigma>=0, the first term
of E is nonpositive; if sigma<0, (19)–(20) bound it by uQ/7.
Thus this bound on that term holds in both cases. Moreover
alpha<1/3, pi>3 and (16) imply
t(pi-2alpha)>2t>(3/2)uQ. Discarding the negative -(9/2)u,
we obtain

    E<(1+u/7-3u/2)Q=(1-19u/14)Q<-3Q.              (21)

Equations (11), (15) and (21) prove the asserted exp(-59Q/20)
bound. This covers arbitrary large u and negative sigma without a
circle-denominator singularity or a supplementary source estimate.

### The degenerate height and compatibility

For h=0, L802 gives y_L=0, and s=F(u)=u(Q-c)>0. The prescribed
V(s,0)=0 proves (1). The continuation for nonzero fixed y need not
have a limit at y=0 for arbitrary fixed s; no such statement is used.
We instead verify the actual limit along D.

For 0<h<=1/2, direct real and imaginary parts of
A=4q+2(q-c)/x, with v=u^2+h^2, give

    Re A=2Q[(2+u/v)cos(2h)+(h/v)sin(2h)]-2cu/v
          >=2Q-2c/u>Q,
    Im A=4Q sin(2h)
           +2[Q(u sin(2h)-h cos(2h))+ch]/v
          <=8Qh+4Qh/u+2ch/u^2<10Qh.                (22)

For the first line use cos(2h)>=1/2 and nonnegativity of the
remaining terms; for the second use sin(2h)<=2h and v>=u^2.
The last strict inequality follows from u>3,Q>1000,c=9/4.
L802 supplies 0<theta<pi/2, so theta<=tan theta<10h. Hence

    0<y_L=h+d sin(theta/2)<(1+5d)h<2h.              (23)

As h tends to zero, eventually y_L<1/2. By L799, the fixed compact
disc |z|<=1/2 has a finite bound M_* for |P(z)|, independent of u.
For r in (0,y_L], equation (14) gives sigma>0, and (6) gives t>0.
Thus |(ir)^(2s)|=r^(2sigma)exp(-pi t)<=1, so the convergent
integral satisfies |V(s,y_L)|<=M_* y_L<2M_*h. This proves the
claimed uniform limit, also when u is unbounded. Conjugation (5)
gives the same statement for h<0, and also supplies both nonzero
height estimates already proved. At any finite positive-real point
of D the normalization is continuous and nonzero by L797/L798,
so the normalized value is compatible there as well.

All inequalities were obtained for every saddle in the closed D,
including |s|=6000 and Re(s)=-|s|/(8 log|s|). They impose no upper
bound on u. The displayed stronger estimates, their conjugates and
the exact zero at h=0 prove (1).

The full computation is included because the cited source's endpoint
outline does not pay these constants for L802's actual longer-diameter
height or spell out the fixed-height pole qualifications. The approved
SPECIALIZE scope authorizes precisely this verification of known
methods. No unread supplement, global contour identity or actual-Xi
positivity is a premise.

### Independent conceptual audit, 5 November 2026 — step538

The unchanged SPECIALIZE assessment
`drafts/literature/2026-11-05-mellin-vertical-endpoint-audit-scope.md`
approves this exact audit. Its inspected Taylor-subtraction, Cauchy,
compact-convergence and Gaussian inputs are reused. The following
checks validate (1) and its stated qualifications, without importing
the source's endpoint estimate or an unread supplement. No correction
to the proof is needed. This is verification of a reproduced local
component, not progress beyond the checked sources or a sign theorem.

**Fixed ray and continuation.** For either sign of y, the parameter
z=iyr has dz=iy dr and Log(iyr)=Log(iy)+log r. Multiplying the
monomial by dz gives exactly (iy)^(2s+n+1), with no missing orientation
factor for y<0. The geometric coefficient majorant on the chosen
radius-R disc is integrable against r^(2sigma) for sigma>-1/2.
On a compact s-set avoiding the listed poles, the large-n denominators
are at least n/2 and the finitely many others have positive lower
bounds. Thus the infinite tail is holomorphic locally at every listed
pole too, after omitting its single singular term. The numerator of
that term equals p_n at s=-(n+1)/2, and the derivative of its denominator
is 2. This proves the exact residue and removability statement.
Every summand of p_0 is positive. No parity or full nonvanishing of the
other coefficients is required.

For (4), the Taylor remainder is bounded by a constant times r^N,
uniformly for r in [0,1]. On any compact set in
Re(s)>-(N+1)/2 this gives an integrable r^(-1+epsilon) bound.
The parameter-integral theorem cited above therefore applies, and
integration of one additional monomial verifies compatibility of
successive subtraction orders. This is the unique continuation of
the initial integral. At a negative real s=-r with r>=6000, membership
in D would imply 1<=1/(8 log r), which is impossible. All evaluations
on D consequently avoid even the possible poles. Fixed y is kept
independent of s throughout this analytic argument; the later choices
y=y_L(s) and R=R(u) are evaluations and estimates, not a claimed
holomorphic moving-height substitution.

**Actual height and complete circle bound.** L802's formulas give
y>=h>0 and R-y>13/(224u) when h>0. For every point of the closed
disc, Re z>=-R and |Im z|<=R, so the two positive factors in
Re(pi exp(2z)) have the simultaneous lower bounds used in (7).
With R<1 and 13/(112u)<1/6 this yields
39/(1792u)>1/(50u); the comparison is 1950>1792. Thus the disc
is strictly inside L799's holomorphy strip even as u grows.
L799's full-series triangle inequality, rather than a finite theta
truncation, gives (8) with coefficient at most 13304<14000.

For each n>=1 the integrand (v+1)^4 exp(-beta v^2) dominates
n^4 exp(-beta n^2) on [n-1,n]. Its integral is bounded using
(v+1)^4<=8(v^4+1). The two half-line Gaussian moments are
3sqrt(pi)/(8 beta^(5/2)) and sqrt(pi)/(2 sqrt(beta)); their
coefficients 8 give exactly (9). All boundary terms vanish for
beta>0. As beta<1 and sqrt(pi)<2, their sum is strictly less than
14 beta^(-5/2). Hence the bound on M_R in (10) is valid for the
complete holomorphic P. The prefactor check (11) also holds for
unbounded u: 7^12=13841287201>8*10^9,
24+(5/2)log u+u<12u, and Q/u>1000/3>240. Finally B<5Q and
2pi>6 give 1/|C|<sqrt(Q), with C nonzero on D.

**Phase and both height regimes.** Directly taking the real part of
S_s(x) gives 2sigma log|x|-2t alpha+(9/2)u-Q cos(2h).
The ray power has modulus exp(-pi t)y^(2sigma). Their quotient is
therefore exactly exp(E) from (13); in particular its sign-sensitive
factor exp(-pi t) is retained. L802 gives Q cos(2h)>c, so (6)
has t>0. Also alpha<1/3 and pi-2alpha>2.

For 0<h<=1/2, y<61/112<3/5 and
sigma>=uQ(1/3-c/Q)>uQ/4>0. Thus the convergent integral is
available throughout this case, with y/(2sigma+1)<1. Since
y/|x|<1/5 and log 5>3/2, (13) gives
E<-3sigma+Q<-(3u/4-1)Q<-5Q/4. Adding the prefactor cost Q/20
proves the strict exponent -6Q/5, including h=1/2. There is no
use of a singular 1/t bound near zero height.

For h>1/2, sin(2h)>=5/6 and h<1 give
t>(5/6)uQ-c>(3/4)uQ. Hence every denominator of (3) has modulus
at least 2t even when sigma is negative. Summing its geometric
majorant and using the actual clearance gives
R/[2t(R-y)]<448/(39Q)<1. The remaining factor y is also <1.
The closed-domain inequality gives
sigma>-(401/6000)Q>-Q/14, since log|s|>2u and
|x|/u<16/15; the last comparison is 5614<6000. Also
1<|x|/y<3u and log(3u)<u. Consequently the first term in E
is at most zero for sigma>=0 and less than uQ/7 for sigma<0.
Together with t(pi-2alpha)>(3/2)uQ, this yields
E<(1-19u/14)Q<-3Q because u>3. Adding Q/20 proves the
strict exponent -59Q/20. No ordinary divergent endpoint integral
has replaced the meromorphic series in this regime.

**Conjugation, zero height and closed boundaries.** Normal convergence
of the real-coefficient P series gives real p_n; the principal logs
of iy and -iy are conjugates. Thus (5) holds throughout continuation.
L797's saddle and L798's principal root C respect conjugation,
and L802 reverses y_L while leaving u unchanged. This transfers
both bounds to h<0 without changing their normalizations.

When 0<h<=1/2, the real and imaginary parts of A in (22) give
Re A>=2Q-2c/u>Q and
Im A< Qh(8+4/3+1/2000)<10Qh; here
2c/(u^2Q)<1/2000 follows from u>3,Q>1000. Since 0<theta<pi/2,
theta<=tan theta<10h and y_L<(1+5d)h<2h. For h<1/4 the
whole ray is in the fixed radius-1/2 disc. Its bound M_* is
independent of u, and r^(2sigma)exp(-pi t)<=1 on the ray.
Thus |V(s,y_L)|<=M_* y_L<2M_*h uniformly in u. Conjugation
proves the same estimate with |h| on the other side. At h=0,
y_L=0 and s=u(Q-c)>0, so the prescribed zero is compatible.
At each finite such s the nonzero normalization is continuous,
which also proves compatibility of the normalized value there.
No uniform raw-to-normalized limit at infinity is being asserted.

Every estimate uses u>3, the strict saddle/height clearances and
the defining non-strict inequality of D, all supplied on both its
closed boundaries. No upper bound on u or exclusion of |s|=6000
or the curved left boundary occurs. The input uses remain exactly
L797, L798, L799 and L802; there is no new DAG edge. Global contour
equality and combined budget, quotient/inversion, certificates and
the sufficient actual-Xi sign implication are still unpaid.

## Mathlib

Full matching coverage is not checked, and no absence claim is made.
The standard supporting mathematics is Taylor expansion and Cauchy
coefficient estimates on a disc, normal convergence of holomorphic
series, holomorphic parameter integration, truncated Mellin Taylor
subtraction, and the real Gaussian integral with its even moments.
The primary formulas and their applied hypotheses are cited above;
no specific Mathlib theorem name or formal verification is asserted.
