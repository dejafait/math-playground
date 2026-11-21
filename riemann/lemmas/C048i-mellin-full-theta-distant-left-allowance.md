# Corollary C048i: the full-theta absolute distant-left allowance

## Hypotheses

Use C048c's sector, saddle and principal branches:

\[
 r=|p|,\quad L=\log r\ge12,\quad \Re p\ge-r/(4L),\qquad
 w=W_0(2p/\pi)=U+iV,\quad u_0=w/2=x_0+iy,
\]
\[
 h_p(u)=2p\operatorname{Log}u-\pi e^{2u},\qquad
 g(u)=8\pi^2e^{9u/2}/u,\quad K(s)=g(u_0+s)/g(u_0),\quad
 A_0=-h_p''(u_0)/2.
\]

On the open strip |Im u|<pi/4 put

\[
 F(u)=\sum_{n\ge1}\left(n^4-\frac{3n^2}{2\pi e^{2u}}\right)
                  e^{-\pi(n^2-1)e^{2u}},
\]
\[
 T_{\rm farleft}(p)=
 \frac{\displaystyle\int_{1-x_0}^{-1}
  |K(s)F(u_0+s)e^{h_p(u_0+s)-h_p(u_0)}|\,ds}
 {|\sqrt{\pi/A_0}|}.                                      \tag{1}
\]

This is the full F of C048h, including the lower-power first mode.
The square root is principal. The modulus is inside the integral.
No origin continuation, global contour equality or theta positivity
is a hypothesis.

The source is K. Kawano, *Logarithmic Inequalities of Arbitrary Order
for the Riemann Xi Coefficients*, [Preprints.org202611.0383v1,
posted4 November2026, DOI10.20944/preprints202611.0383.v1](https://www.preprints.org/manuscript/202611.0383/v1),
Section5.2(28), Lemma5.1(i), both left-phase cases in the proof of(31),
AppendixB's full-mode inequalities and distant-left tangent method,
and AppendixC's distant-tail allocation of 10^(-4)L^(9/2)/r.
The finite absolute observable is the specialization specified in
source-notes1648, not a separately named source integral. The unchanged
SPECIALIZE assessment1648 approved this reproduction before step1649.
The preprint's quantitative bounds are conclusions to check, not
premises. Its finite-band constants are not used for unbounded L.

## Conclusion

The entire segment in (1) lies in Re u>=1 and |Im u|<pi/4; its
integrand is continuous and its normalization is nonzero. Uniformly
on the full closed sector,

\[
 T_{\rm farleft}(p)
 < B\frac{L^{9/2}}r
 <10^{-4}\frac{L^{9/2}}r,\qquad
 B=\frac{349920}{2^{40}}.                              \tag{2}
\]

The actual source normalization, including its phase, is retained:

\[
 g(u_0)e^{h_p(u_0)}\sqrt{\pi/A_0}
 =\frac{8\pi^{5/2}e^{9w/4}}{\sqrt{p(1+w)}}
    e^{2p\operatorname{Log}(w/2)-2p/w}=S(p).           \tag{3}
\]

This proves the approved finite allowance as REPRODUCTION, using
deliberately coarse constants. It does not assert the stronger
intermediate distant-tail expression printed in AppendixC. Step1649
supplies the proof; independent conceptual audit1651 below validates
the stated bound and normalization without a mathematical correction.
No discovery beyond the checked sources or RH candidate is claimed.
Origin/global assembly, zero counts, inversion and sufficient
actual-Xi all-degree signs remain independent gaps.

## Proof

### 1. Geometry, convergence and exact normalization

C048c(4)-(10) and its branch calculation give

\[
 U>3L/4\ge9,\quad |V|<\pi/2,\quad |w|<L,\quad
 \cos V>1/L,\quad v:=\pi e^U\cos V>2r/L^2,
 \quad \Re A_0>0,\quad |A_0|<6r/L,                  \tag{4}
\]
\[
 |\sqrt{\pi/A_0}|=\sqrt{\pi/|A_0|}>0,
\]

and exactly (3). In particular x_0>9/2, so 1-x_0<-1.
For s in [1-x_0,-1], u=u_0+s=x+iy has

\[
 1\le x\le x_0-1,\qquad |y|<\pi/4<1\le x.
\]

Thus the whole closed finite segment is strictly inside the theta
strip and the principal Log domain. Its denominators do not vanish.

Use only L799's general strip-convergence argument and identity(4),
not its different saddle estimates. On each compact subset of the
strip, Re(pi e^(2u)) has a positive minimum. The theta terms have a
summable polynomial-times-Gaussian majorant, so they converge normally.
With the notation

\[
 P(u)=\sum_{n\ge1}(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2})
                                      e^{-\pi n^2e^{2u}},
 \qquad H(u)=4\pi^2e^{9u/2-\pi e^{2u}},
\]

that strip identity gives F=P/H; H never vanishes. Therefore F is
continuous on the finite segment. Exactly,

\[
 e^{2p\operatorname{Log}u}\frac{2P(u)}u
                  =g(u)e^{h_p(u)}F(u).              \tag{5}
\]

Since du=ds, division of the absolute value of (5) by |S(p)|
using (3) gives precisely (1). The factor 2/u, saddle amplitude and
principal-root normalization have not been dropped or changed.

### 2. Left phase on the enlarged interval x>=1

We reuse C048h Section2's phase argument, checking its hypotheses on
the larger interval [1,x_0]; its near-left amplitude bound is not used.
First take Im p>=0 and write p=sigma+i beta. C048c's branch geometry
gives beta,y>=0. Put

\[
 Q(x)=\frac{\sigma x+\beta y}{x^2+y^2},\qquad
 H_p(x)=\Re h_p(x+iy).
\]

The saddle identity p/u_0=pi e^(2u_0) gives

\[
 Q(x_0)=v>0,\qquad
 H_p'(x)=2Q(x)-2v e^{2(x-x_0)}.                     \tag{6}
\]

If sigma>=0, x>=1>|y| gives

\[
 Q'(x)=\frac{\sigma(y^2-x^2)-2\beta xy}{(x^2+y^2)^2}\le0.
\]

If sigma<0, the numerator sigma*x+beta*y is at least its strictly
positive value at x_0 for every x<=x_0. Thus Q(x)>0 and

\[
 Q'(x)=\frac{\sigma-2xQ(x)}{x^2+y^2}<0.
\]

In either case Q(x)>=v on [1,x_0]. For 1-x_0<=s<=0, reversing
the integration in (6) therefore yields

\[
 H_p(x_0+s)-H_p(x_0)
 =-\int_s^0 H_p'(x_0+t)\,dt
 \le-v\phi(s),\qquad \phi(s)=e^{2s}-1-2s.           \tag{7}
\]

For Im p<0, principal Lambert and Log conjugation send this segment
to that for the conjugate parameter and preserve v and the real
phase. Hence (7) holds there too. For real p the sector forces p>0,
and y=beta=0, so the sigma>=0 case applies. The sigma=0 case and
both closed angular boundaries are already included.

### 3. All theta parameters and all modes

We verify the all-t>0 source envelope explicitly, since C048h's t>2
bound does not apply throughout the present segment. For t>0 set

\[
 Z_4(t)=\sum_{n\ge1}n^4e^{-(n^2-1)t}.
\]

We claim

\[
 Z_4(t)<100(1+t^{-5/2})\quad(t>0).                  \tag{8}
\]

For 0<t<=1 let f_t(a)=a^4 e^(-t a^2), a>=0. Its derivative shows
that it increases up to a_*=sqrt(2/t) and decreases thereafter.
Put k=floor(a_*)>=1. For 1<=n<=k-1, monotonicity gives
f_t(n)<=integral_n^(n+1) f_t(a) da. For n>=k+2 it gives
f_t(n)<=integral_(n-1)^n f_t(a) da. The two omitted summands
at k and k+1 are each at most max f_t. Consequently

\[
 \sum_{n\ge1} f_t(n)
 \le\int_0^\infty f_t(a)\,da+2\max f_t
 =\frac{3\sqrt\pi}{8t^{5/2}}+\frac{8e^{-2}}{t^2}
 <3t^{-5/2}.                                       \tag{9}
\]

The integral is [NIST DLMF5.9.1](https://dlmf.nist.gov/5.9#E1)
with mu=2, nu=5 and z=t>0; all of its positivity/real-part
hypotheses hold. Using the standard gamma recurrence and
Gamma(1/2)=sqrt(pi) gives the displayed value. The strict bound
uses pi<4, e^2>4 and t<=1. Since e^t<=e<3, (9) gives
Z_4(t)<9t^(-5/2), which implies (8) in this range.

For t>=1 put b_n=n^4e^(-(n^2-1)t), n>=2. Then

\[
 \frac{b_{n+1}}{b_n}
 \le\frac{81}{16}e^{-5}<\frac1{10},\qquad
 \sum_{n\ge2}b_n\le\frac{160}{9}e^{-3t}.
\]

Here e>2 and e^2>7 give e^5>98, and 810<16*98.
Thus Z_4(t)<1+160/72=29/9<4, proving (8) also for t>=1.
These series comparisons control every mode. The elementary bounds
2<e<3 follow from the positive exponential series and
n!>=2^(n-1) for n>=2 (strict for n>=3); e^2>7 follows from
the first five terms of the exponential series at 2, whose sum is 7.
This quantitative verification of the source's envelope is needed
for the small-t specialization; it is not a new general theta claim.

For u=x+iy on the segment define

\[
 a(u)=\frac3{2\pi}e^{-2x}<\frac1{14}<\frac12,
 \qquad t=\Re(\pi e^{2u})=\pi e^{2x}\cos V>
                           \frac{\pi e^2}{L}>\frac{21}{L}>0.
\]

Since n^2<=n^4, normal convergence and (8) give

\[
 |F(u)|\le(1+a(u))Z_4(t)
 <150(1+t^{-5/2})
 <150\bigl(1+(L/21)^{5/2}\bigr)<300L^{5/2}.         \tag{10}
\]

This includes both powers of the n=1 term and every n>=2 term;
no cancellation or complex positivity has been assumed. Also

\[
 |K(s)|=e^{9s/2}\frac{|u_0|}{|u_0+s|}
                  <\frac L2 e^{9s/2},              \tag{11}
\]

because |w|<L and |u_0+s|>=x>=1. In particular the growing saddle
ratio on the left is paid. Combining (7), (10) and (11) gives

\[
 |K(s)F(u_0+s)e^{h_p(u_0+s)-h_p(u_0)}|
 <150L^{7/2} e^{f(s)},\quad
 f(s)=9s/2-v\phi(s).                               \tag{12}
\]

### 4. Tangent envelope and the unbounded-L coefficient

The real function f has f''(s)=-4v e^(2s)<0. Its tangent at -1
therefore bounds it from above for s<=-1:

\[
 f(s)\le f(-1)+\lambda(s+1),\quad
 f(-1)=-9/2-v(1+e^{-2})<-v,\quad
 \lambda=f'(-1)=9/2+2v(1-e^{-2})>v>0.              \tag{13}
\]

The last comparison uses e^2>2. This is the reflected tangent
envelope in Luc Devroye, [*Non-Uniform Random Variate Generation*
(1986), ChapterVII Section2.6 pp299-300](https://luc.devroye.org/chapter_seven.pdf),
the envelope before Theorem2.6 and the reflected case/first integral
of its proof. Differentiation in (13) checks the required real
concavity and exact parameter dependence. No log-concavity of a
complex theta sum or probability normalization is being imported.

Only the scalar envelope is extended to -infinity. Equations
(12)-(13), applied first on the actual finite segment, give

\[
 T_{\rm farleft}(p)
 <150L^{7/2}\sqrt{\frac{6r}{\pi L}}\frac{e^{-v}}v
 <75\sqrt{6/\pi}\frac{L^5}{\sqrt r}
                      e^{-2r/L^2}
 <120\frac{L^5}{\sqrt r}e^{-2r/L^2}.               \tag{14}
\]

Here (4) pays the normalization and v>2r/L^2; both e^(-v)
and 1/v decrease for positive v. The final constant uses pi>3
and sqrt(2)<3/2, so 75sqrt(6/pi)<225/2<120.

Divide the last expression by L^(9/2)/r and define

\[
 R(L)=120\sqrt L\,e^{L/2-q(L)},\qquad
 q(L)=2e^L/L^2.
\]

For L>=12, q'(L)=q(L)(1-2/L)>0 and
q(12)>2*2^12/12^2=512/9>40. Therefore

\[
 (\log R)'(L)=\frac1{2L}+\frac12-q(L)(1-2/L)
 <\frac{13}{24}-40\frac56<0.                       \tag{15}
\]

This proves monotonicity on the whole unbounded radial interval,
not just sampled values. At its closed endpoint,

\[
 R(12)=120\sqrt{12}\,e^6 e^{-q(12)}
 <120\cdot4\cdot3^6\cdot2^{-40}
 =\frac{349920}{2^{40}}=B<10^{-4}.                 \tag{16}
\]

The last comparison is the exact integer inequality
3,499,200,000 < 1,099,511,627,776 = 2^40.
Equations (14)-(16) prove (2). No numerical quadrature, finite-mode
truncation, parameter sampling or machine certificate is required.
All geometry and constants include L=12, real p, negative permitted
Re p and both angular boundaries. The strict internal strip
clearance holds at those boundaries by (4).

### Independent conceptual audit1651 — 19 November2026

The unchanged SPECIALIZE assessment1649, separately source-approved
in1650, covers precisely this audit. Read the complete proof and
source-notes1648, C048c's geometry and branch calculation (including
the relevant audit1629), L799's general strip convergence/identity(4),
and C048h Section2. The full bound (2) and complex normalization (3)
pass without a correction. This validates a local reproduction of
the stated source allowance, not a new result beyond those sources.

**Domain and analytic use of the series.** C048c supplies U>3L/4,
|w|<L and cos V>1/L, hence x_0>9/2 and 1-x_0<-1.
On the entire segment, x>=1>|y| and |y|<pi/4. For every fixed p
it is a compact subset of the open strip and the principal Log domain.
The normal convergence proof in L799 applies there independently of
L799's different saddle. Dividing its kernel series by the nonzero
H gives F=1+rho, including the n=1 lower-power term; it is not rho
alone. A common positive strip margin as L tends to infinity is
unnecessary: the subsequent real bounds are uniform in p. No boundary
series evaluation or infinite-path limit is used for this observable.

**Normalization and branches.** Differentiating h_p at the saddle
gives A_0=4p(1+w)/w^2. C048c proves Re A_0>0 and |A_0|<6r/L.
Both |arg w| and |arg sqrt(A_0)| are strictly less than pi/4.
Thus w sqrt(A_0)/2 has positive real part and square p(1+w),
identifying the principal square root without a hidden sign.
Consequently sqrt(pi/A_0)=sqrt(pi)w/(2sqrt(p(1+w))). Multiplication
by g(u_0)=16pi^2 e^(9w/4)/w and exp(h_p(u_0)) yields (3).
All factors are nonzero. Direct cancellation in g exp(h_p)F gives
2 exp(2p Log u)P(u)/u, so (5) retains the exact factor 2/u.
The horizontal parameter increases with ds=du; absolute normalization
is sqrt(|A_0|/pi), not its reciprocal. This verifies (1) as an integral
of moduli divided by |S(p)|, without changing the phase of S.

**Both left-phase cases and reflection.** For sigma>=0 the numerator
of Q' is nonpositive because x>|y| and beta,y>=0. For sigma<0,
sigma x+beta y>=sigma x_0+beta y>0, so the second expression for
Q' is strictly negative on [1,x_0]. Hence Q>=Q(x_0)=v in both cases.
The saddle identity gives H_p'=2Q-2v exp(2(x-x_0)); integration
from s to zero with a minus sign gives exactly -v phi(s) in (7).
No right-side inequality is used backwards without that sign change.
Principal Lambert and Log conjugation treat Im p<0. When Im p=0,
the sector excludes p<0 and p=0, leaving the positive real case.
The sigma=0 case and closed angular boundaries satisfy these same
inequalities directly. The extension from C048h's near-left interval
uses only this phase argument, not its t>2 amplitude conclusion.

**Every theta mode, including arbitrarily small positive t.** In (9),
the increasing intervals for n<=k-1 and decreasing intervals for
n>=k+2 are disjoint and lie in [0,infinity). Only k and k+1 are
omitted, each at most 4e^(-2)/t^2. DLMF5.9.1 applies with
mu=2, nu=5, z=t>0 and gives 3sqrt(pi)/(8t^(5/2)). Since t<=1,
the sum is less than (3/4+2)t^(-5/2)<3t^(-5/2); multiplication
by e^t<3 gives the stated small-t bound. This checks the entire
series, including k=1 and integral values of sqrt(2/t).
For t>=1 the ratio is ((n+1)/n)^4 exp(-(2n+1)t), bounded for
all n>=2 by (81/16)e^(-5)<1/10. Summing the full geometric bound
gives (160/9)e^(-3t); e^3>8 then gives Z_4<29/9<4.
The two ranges include t=1. The elementary exponential inequalities
used in both ranges follow from the positive series as stated.

On the actual segment, a(u)<=3/(2pi e^2)<1/14 and
t>=pi e^2 cos V>21/L. The triangle inequality gives
|n^4-(3n^2/(2pi))e^(-2u)|<=n^4+a(u)n^2
< (3/2)n^4. The exponential modulus is precisely
exp(-(n^2-1)t). Thus (10) pays all lower powers and all modes.
Also |u_0/u|<L/2, because |u|>=x>=1. Multiplying (7), (10)
and (11) verifies the factor 150L^(7/2) in (12).

**Tangent and uniform radial coefficient.** The strictly concave
real function f has tangent slope lambda=9/2+2v(1-e^(-2))>v>0
at -1 and f(-1)<-v. Its tangent exponential integrates over
(-infinity,-1] to exp(f(-1))/lambda<e^(-v)/v. Only this scalar
envelope is extended, after it bounds the actual finite integral.
The reflected Devroye method requires exactly this real concavity
and positive slope, both verified here. Multiplication by
sqrt(6r/(pi L)) gives 150sqrt(6/pi)L^3 sqrt(r)e^(-v)/v.
The decreasing function e^(-v)/v and v>2r/L^2 yield
75sqrt(6/pi)L^5 exp(-2r/L^2)/sqrt(r), confirming every power in (14).
The numerical coefficient is strictly less than 120 using pi>3.

Dividing by L^(9/2)/r gives R(L). On L>=12, q is increasing,
q(12)>512/9>40 and 1-2/L>=5/6; hence (15) is strictly negative
on the entire unbounded interval. At L=12, sqrt(12)<4,
e^6<3^6 and e^(-q(12))<2^(-40), proving (16). The exact final
comparison is 10000*349920=3499200000<1099511627776=2^40.
Thus B is below the required 10^(-4); no sampled or asymptotic
estimate substitutes for endpoint or unbounded-L control.

**Dependency and scope check.** The direct inputs remain C048c,
C048h and L799, exactly as in the existing DAG row; C048h supplies
the explicitly rechecked phase method. L802/L803 and the global
source remainder are not bound premises. The stronger intermediate
AppendixC expression is not proved or needed here. Neither a full
Mellin assembly nor zero counts, inversion or actual-Xi signs follow
from this finite absolute estimate. The November5 automatic-import
stop is preserved. No numerical certificate is needed for this audit.

## Mathlib

A full matching theorem for this moving complex saddle and explicit
absolute distant-left allowance has not been checked in Mathlib;
neither absence nor formal verification is asserted. The proof uses
the canonical local geometry/normalization, the general strip-series
identity, the explicitly rechecked phase argument, and the cited
positive-real Gaussian moment and real tangent method. Standard
convergence, differentiation and integration support alone would not
constitute the full result.
