# Lemma 831: reproduction audit of the actual-H full-sector estimate

## Hypotheses

Let

\[
 \omega(t)=\sum_{k\ge1}(2\pi^2k^4t^2-3\pi k^2t)e^{-\pi k^2t},\qquad
 H(z)=2^{1-2z}\int_0^\infty u^{2z}e^{u/4}\omega(e^u)\,du.
\]

On the original ray use the real logarithm of u>0; on deformed
contours use the principal logarithm. Suppose
S={z: |arg z|<=pi/4, |z|>=4000}. For z in S set
w=W_0(2z/pi)=a+ib, T=|z|/a, and

\[
 H_*(z)=4\pi^2e^{7w/4}\sqrt{\frac{2w}{1+w}}
       \exp\{2z(\operatorname{Log}(w/2)-1/w)\}.
\]

W_0, the square root and the elementary logarithm are principal.
No nonvanishing assumption on H is made.

## Conclusion

For every z in the entire closed sector S,

\[
 a>6,\quad T\ge(\pi/2)e^6>630,\quad
 |H(z)/H_*(z)-1|<30/T,\qquad
 |\operatorname{Log}(H(z)/H_*(z))|<32/T<51/1000.
                                                        \tag{1}
\]

The last logarithm is the power-series branch Log(1+v),
v=H/H_*-1. H is nonzero on S, and this logarithm is holomorphic
on an open neighborhood of S. No uniform neighborhood width is asserted.

This discharges precisely L830's unpaid sector assumptions. Applying
that conditional result, for every real n>=12000 the actual moment
interpolation Lambda=H/Gamma(2z+1) has the stated compatible logarithm,
and its g_0=-Delta^2 Log Lambda satisfies

\[
 \left|g_0(z)-\frac{2W_0(2z/\pi)}{z(1+W_0(2z/\pi))}\right|
 <18/n^2\quad (|z-n|\le n/2).
\]

This is a reproduction of Yanxin Liu and Jianxi Mao,
*Infinite log-concavity of the Taylor coefficients of the Riemann
xi-function*, [arXiv:2610.04972v1](https://arxiv.org/html/2610.04972v1),
4 October 2026, Lemmas3.1–3.2, equations (3.1)–(3.51), printed
pp.8–31 ([versioned PDF](https://arxiv.org/pdf/2610.04972v1)).
The source already proves the stated estimate. This audit checks its
analytic cases and constants; it claims no improvement or new discovery.
Proposition4.5, the all-iterate theorem, determinant transfer, exceptional
mixed signs and bounded indices are not conclusions.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-11-05-liu-mao-sector-independent-audit.md`.
Independent verification of this load-bearing preprint estimate, rather
than novelty, justifies this reproduction. We import the principal-W
facts from Corless, Gonnet, Hare, Jeffrey and Knuth, *On the Lambert W
function*, Adv. Comput. Math. 5 (1996), 329–359, Section4
([DOI](https://doi.org/10.1007/BF02124750)): W_0 is holomorphic off
(-infinity,-1/e], |Im W_0|<pi, W_0(x)>0 for x>0, and We^W is
the identity. We also import the complex Gaussian formula for
Re kappa>0, with the positive-axis square-root normalization, from
Folland, *Harmonic Analysis in Phase Space* (1989), Appendix A,
Theorem1. Cauchy's integral theorem, the Weierstrass theorem on locally
uniform holomorphic sums, dominated convergence and Taylor's integral
remainder are standard named inputs. None assumes an Xi zero condition.

All terminating decimals below are exact rationals. The final subsection
specifies an exact-arithmetic replay of every rounded scalar comparison.
Analytic estimates and infinite-range reductions are proved here.

### Sector geometry and analytic domains

Write R=|z| and theta=arg z. If a<=0, the principal-W strip bound gives

\[
 2R/\pi=e^a\sqrt{a^2+b^2}<e^a(-a+\pi)
 \le\pi e^a(1-a)\le\pi.
\]

The last inequality is e^(-a)>=1-a. This contradicts R>=4000;
therefore a>0. The continuous function
b+arctan(b/a)-theta takes values in 2pi Z on the connected sector S
and vanishes on its positive real ray. Thus

\[
 b+\arctan(b/a)=\theta,\quad |b|\le|\theta|\le\pi/4,
 \quad \operatorname{sgn}b=\operatorname{sgn}\theta.
                                                        \tag{2}
\]

If a<=6, then
R=(pi/2)e^a sqrt(a^2+b^2)<= (pi/2)e^6 sqrt(36+pi^2/16)<4000,
again a contradiction. In particular

\[
 1\le |w|/a\le\sqrt{1+\pi^2/576}<1.009,\qquad
 T=(\pi/2)e^a|w|/a>630,\quad
 \pi e^a\le2T,\quad T<1.585e^a,\quad T\le R/6.          \tag{3}
\]

The argument-continuity reasoning includes both edges of S. At b=0,
z is positive real. On compact subsets of Re z>-1/2, the original
H integral converges normally: near zero its integrand is bounded by
C u^(2m), where m is the compact set's minimum real part, and at infinity
by C u^(2M)e^(9u/4) exp(-pi e^u). To obtain the latter bound, factor
exp(-pi e^u) from the theta sum and dominate the remaining k sums
by sums of k^4 exp(-pi(k^2-1)). Hence H is holomorphic there.
This also justifies splitting the first theta term from the rest.

### Contour and Gaussian normalization

Set phi(u)=2z Log u-pi e^u, beta in {5/4,9/4}, and
J_beta=integral_0^infinity exp(phi(u)+beta u) du. The equation
phi'(w)=0 follows from we^w=2z/pi. For each fixed z, Cauchy's theorem
on a truncated right-half-plane contour, indented at zero, gives

\[
 J_\beta=\int_0^{ib}e^{\phi(u)+\beta u}\,du
          +\int_{-a}^{\infty}e^{\phi(w+y)+\beta(w+y)}\,dy. \tag{4}
\]

Here are the limiting details. On either small quarter-circle
u=epsilon e^(it), |t|<=pi/2, the integrand is bounded by
C_z epsilon^(2 Re z), and arc length is pi epsilon/2. Its integral
tends to zero. The little omitted real and imaginary segments also
tend to zero because 2 Re z>-1. On u=A+it with t between 0 and b,
the joining integral is bounded by

\[
 |b|C_z A^{2\Re z}\exp(\beta A-\pi e^A/\sqrt2)\longrightarrow0.
\]

The same bound proves convergence of the horizontal ray. Signed contour
orientations give (4) also for b<0; for b=0 it is the original ray
and the vertical integral is zero. These limits are pointwise in z;
no unproved uniform contour limit is subsequently differentiated.

Put kappa=-phi''(w)=pi e^w(1+1/w). Equations (2)–(3) give

\[
 \Re\kappa=\pi e^a\left(\cos b+
             \frac{a\cos b+b\sin b}{a^2+b^2}\right)>1.4T,
 \qquad |\kappa|\le7T/3.                               \tag{5}
\]

Indeed Re kappa>=pi e^a/sqrt2>sqrt2 T/1.009>1.4T.
The imported Gaussian formula therefore applies with its exact
right-half-plane hypothesis:

\[
 G=\int_{\mathbb R}e^{-\kappa y^2/2}\,dy
   =\sqrt{2\pi}\,\kappa^{-1/2},\qquad
 |G|\ge\sqrt{6\pi/7}\,T^{-1/2}>1.64T^{-1/2},\qquad
 M_\beta=e^{\phi(w)+\beta w}G.                           \tag{6}
\]

### Local Gaussian error

Split the horizontal ray into [-a,-a/2], [-a/2,-.1], [-.1,.1],
and [.1,infinity). Call their integrals I_d,I_-,I_G,I_+, and call
the vertical integral I_v. On |y|<=.1, Taylor's integral remainder is

\[
 \phi(w+y)=\phi(w)-\kappa y^2/2+c_3y^3+R_4(y),\quad
 c_3=\phi'''(w)/6,\quad |c_3|\le19T/54<.4T,
 \quad |R_4(y)|\le .1T|y|^4.                            \tag{7}
\]

For completeness phi'''(u)=4z/u^3-pi e^u and
phi^(4)(u)=-12z/u^4-pi e^u. Since a/(a-.1)^4 decreases for a>=6,

\[
 \sup_{|y|\le.1}|\phi^{(4)}(w+y)|
 \le T(72/5.9^4+2e^{.1})<2.4T,
\]

and R_4(y)=(y^4/6) integral_0^1 (1-t)^3 phi^(4)(w+ty) dt
proves (7). Let X=beta y+c_3y^3+R_4(y). The inequalities

\[
 |X|\le\beta|y|+.041Ty^2\le .091Ty^2+\beta^2/(.2T),
 \qquad e^{|X|}\le1.2e^{.091Ty^2},
\]
\[
 |X|^2\le3\beta^2y^2+.48T^2y^6+.03T^2y^8
\]

follow from completing a square, beta<=9/4 and T>630. Using
|e^X-1-X|<=(|X|^2/2)e^|X|, subtract the odd terms beta y+c_3y^3
before integrating against the even complex Gaussian. Their integrals
on [-.1,.1] are exactly zero. Thus the local error E satisfies

\[
 |E|\le .1T\int_{\mathbb R}y^4e^{-.7Ty^2}\,dy
       +.6\int_{\mathbb R}e^{-.6Ty^2}
                 (3\beta^2y^2+.48T^2y^6+.03T^2y^8)\,dy. \tag{8}
\]

The weakening .7-.091=.609>.6 is in the safe direction.
The real Gaussian moment formula
integral_R y^(2j)e^(-v y^2)dy=(2j-1)!! sqrt(pi)/(2^j v^(j+1/2))
follows by integration by parts from the Gaussian integral; its boundary
terms vanish for v>0. Dividing (8) by the lower bound (6), the
coefficients of 1/T are respectively

\[
 A_4=\frac{.1\cdot3\sqrt{7/6}}{4(.7)^{5/2}},\quad
 A_2=\frac{.6\cdot3(81/16)\sqrt{7/6}}{2(.6)^{3/2}},\quad
 A_6=\frac{.6\cdot.48\cdot15\sqrt{7/6}}{8(.6)^{7/2}},
\]

and the coefficient of 1/T^2 is
A_8=.6*.03*105 sqrt(7/6)/(16(.6)^(9/2)). Their complete sums obey
A_4+A_2+A_6<14.4 and A_8<1.3. Gaussian truncation at |y|=.1 costs

\[
 |G|^{-1}\int_{|y|\ge.1}e^{-.7Ty^2}\,dy
 \le\frac{2}{.14(1.64)}\frac{e^{-.007T}}{\sqrt T}
 <\frac{8.8e^{-.007T}}{\sqrt T}.                         \tag{9}
\]

To see this, write y=.1+t and use (.1+t)^2>=.01+.2t.
Consequently |I_G/M_beta-1|<14.4/T+1.3/T^2+8.8e^(-.007T)/sqrt(T).

### Absolute horizontal and distant-left tails

Let Psi(y)=Re(phi(w+y)-phi(w)). For y>=-a/2 and b>=0,
0<=2 arg(w+y)<=4b/a<=(2/3)theta, so
arg(2z/(w+y)^2) lies between theta/3 and theta. Its real part
is positive; the same holds for b<0 by conjugation. Therefore
Psi''(y)<0 on the whole interval. On |y|<=.1 more precisely

\[
 -\Psi''(y)\ge\pi e^{a-.1}/\sqrt2
 >\frac{\sqrt2e^{-.1}}{1.009}T>1.26T.
\]

Since Psi(0)=Psi'(0)=0, integration and concavity give, on both tails,

\[
 \Psi(y)\le-.0063T-.126T(|y|-.1).
\]

With t=|y|-.1>=0, beta y<=2.25t+.225. Integrating this pointwise
envelope over each tail, extending the finite left interval to infinity,
proves the stronger bound

\[
 \frac{\displaystyle\int_{[-a/2,-.1]\cup[.1,\infty)}
                    |e^{\phi(w+y)+\beta(w+y)}|\,dy}{|M_\beta|}
 \le\frac{2e^{.225-.0063T}}{|G|(.126T-2.25)}
 <\frac{12.6e^{-.0063T}}{\sqrt T}.                      \tag{10}
\]

The coefficient is bounded by
2e^.225/[1.64(.126-2.25/630)]<12.6. This is an integral-of-modulus
estimate, not merely a bound for |I_-|+|I_+|; it is the form used below.

For -a<=y<=-a/2, |w+y|/|w|<=sqrt(1/4+pi^2/576)<.52.
For w+y nonzero the action's real part is

\[
 \Psi(y)=2\Re z\log\frac{|w+y|}{|w|}
 -2\Im z(\arg(w+y)-\arg w)+\pi e^a\cos b(1-e^y).
\]

Both Im z and the argument difference have the sign of b, by (2).
Their contribution is nonpositive, including the endpoint by continuity
when b!=0. If b=0, the argument contribution is zero and the
integrand at y=-a is its zero limit. As Re z>=R/sqrt2 and a>=6,

\[
 \Psi(y)\le R(\sqrt2\log(.52)+1/3)<-.58R.
\]

Since beta y<0, this proves the absolute-integral bound

\[
 \frac{\displaystyle\int_{-a}^{-a/2}
                  |e^{\phi(w+y)+\beta(w+y)}|\,dy}{|M_\beta|}
 \le\frac{a\sqrt T}{3.28}e^{-.58R}<R e^{-.58R}.           \tag{11}
\]

We retain a factor 20 for the theta remainder. For R>=4000,
e^(.08R)>(.08R)^3/6>20R and
e^(R/2)>R^3/48>100R/6>=100T. The polynomial comparisons hold
at R=4000 and improve as R increases. Thus

\[
 20R e^{-.58R}<e^{-R/2}<1/(100T).                         \tag{12}
\]

### Absolute vertical tail

On u=it from 0 to ib, t has the sign of Im z. For t!=0,
Re(phi(it)+i beta t)=2 Re z log|t|-pi|Im z|-pi cos t<=0.
The integrand tends to zero at t=0; its absolute integral is
at most |b|<=pi/4<1. In contrast, |arg w|<=pi/24, |w|>=6,
and pi e^a<=R/3 give

\[
 \Re\phi(w)\ge R(\sqrt2\log6-\sqrt2\pi/24-1/3)>2R.
\]

Here the negative argument term is bounded using |Im z|<=R/sqrt2.
Consequently

\[
 |M_\beta|>e^{2R}/\sqrt T>2R^2/\sqrt T
 \ge72T^{3/2}>100T.                                    \tag{13}
\]

This proves |I_v/M_beta|<.01/T for both beta values, also at b=0.

### The actual theta remainder

Define

\[
 E_\theta(u)=e^{u/4}\sum_{k\ge2}
 (2\pi^2 k^4e^{2u}-3\pi k^2e^u)e^{-\pi k^2e^u},\qquad
 I_\theta=\int_0^\infty u^{2z}E_\theta(u)\,du.
\]

On every compact subset of |Im u|<pi/2, Re(e^u) has a positive
minimum. A constant times sum k^4 exp(-c k^2), c>0, normally
dominates the series. Thus E_theta is holomorphic and bounded near
zero. On Re u=A>=0, |Im u|<=pi/4, it is bounded by
C e^(9A/4) exp(-pi e^A/sqrt2): factor the k=1 exponential and
use a fixed convergent Gaussian k sum for the rest. The same small-arc
and far-joining estimates used in (4) apply. Hence I_theta is the sum
of its vertical and horizontal integrals. No termwise interchange with
an unbounded contour is assumed.

For r=Re(e^u)>=1/sqrt2, factoring exp(-4pi r) in the positive
series gives

\[
 \sum_{k\ge2}k^4e^{-\pi k^2r}<17e^{-4\pi r},\qquad
 \sum_{k\ge2}k^2e^{-\pi k^2r}<5e^{-4\pi r}.              \tag{14}
\]

Indeed, for p=2 or 4, t_k=k^p exp(-pi(k^2-4)r), k>=3,
satisfies t_3<=81e^(-5pi/sqrt2)<.002 and
t_(k+1)/t_k<=(4/3)^4e^(-7pi/sqrt2)<10^(-6).
Their geometric sum is <.002/(1-10^(-6))<1. This proves (14)
for the full infinite sums. On our contour Re u>=0, so (14) implies

\[
 |u^{2z}E_\theta(u)|
 <20(2\pi^2)e^{-3\pi r}|e^{\phi(u)+9u/4}|,              \tag{15}
\]

because 34pi^2+15pi<40pi^2. We now check all three regions.

For y>=-a/2, r=e^(a+y)cos b>=e^(a/2)/sqrt2. On |y|<=.1,
the local envelope gives |exp(-kappa y^2/2+X)|<=1.2exp(-.6Ty^2).
Adding the absolute tails (10) yields

\[
 \frac{\displaystyle\int_{-a/2}^\infty
                 |e^{\phi(w+y)+9(w+y)/4}|\,dy}{|M_{9/4}|}
 <\frac{1.2}{1.64}\sqrt{\pi/.6}+\frac9T<2.              \tag{16}
\]

Here 12.6 sqrt(T)e^(-.0063T) is decreasing for T>=630 and
is <9 at 630. Equations (15)–(16) give a normalized theta cost
<40 exp(-(3pi/sqrt2)e^(a/2)). Put v=e^(a/2)>=e^3>20. Since
T<1.585e^a, 40*1.585<64, and 3pi/sqrt2>6.6, its product with T
is <64v^2e^(-6.6v). This decreases for v>=20 and is at most
64*20^2 e^(-132)<.01, the last inequality following already from
e^132>132^4/24. Thus this region costs <.01/T.

For -a<=y<=-a/2, drop the factor e^(-3pi r) in (15). The
normalized absolute theta integral is bounded by 20 times (11),
which is <.01/T by (12). This explicitly pays the factor 20.

On u=it, (14), even with an added k=1 term, gives

\[
 |E_\theta(it)|\le(2\pi^2+3\pi)e^{-\pi/\sqrt2}
       +(34\pi^2+15\pi)e^{-4\pi/\sqrt2}<4.
\]

Also |(it)^(2z)|=|t|^(2 Re z)e^(-pi|Im z|)<=1.
The vertical absolute theta integral is <4. Dividing by
2pi^2|M_(9/4)| and using (13) and 4/(2pi^2)<1 gives <.01/T.
The b=0 case contributes zero. Altogether

\[
 |I_\theta|/(2\pi^2|M_{9/4}|)<.03/T.                    \tag{17}
\]

### Error assembly, nonvanishing and branches

Equations (9)–(13) and the local estimate give

\[
 |J_\beta/M_\beta-1|
 <14.4/T+1.3/T^2+
   (8.8e^{-.007T}+12.6e^{-.0063T})/\sqrt T+.02/T<24/T.  \tag{18}
\]

For c=.007 and .0063, sqrt(T)e^(-cT) decreases on T>=630;
the sum at 630 is <9. The remaining coefficient is
14.4+1.3/630+9+.02<24. This checks the complete budget, not
separate rounding of terms that could exceed it.

We have G^2=e^(-w)2w/(1+w). Also Re(w/(1+w))>0 and
Re kappa>0 on S. Thus both G and e^(-w/2)sqrt(2w/(1+w))
are holomorphic and nonzero in some connected open neighborhood
of S. Such a neighborhood exists by taking the component containing
S of the open domain where the displayed strict real-part conditions
hold; S is connected. Their quotient has square 1 and equals 1 on
the positive real ray. Hence they agree throughout that component.
In particular there is no unaccounted sign in the Gaussian factor.
Since Log(w/2)=Log w-log2 on Re w>0,

\[
 2^{1-2z}2\pi^2M_{9/4}=H_*,\qquad
 M_{5/4}/M_{9/4}=e^{-w}.                               \tag{19}
\]

Both H_* and its defining branches are nonzero and holomorphic
near S. From (3) and (18), the lower-order first-theta contribution is

\[
 \frac{|3\pi J_{5/4}|}{2\pi^2|M_{9/4}|}
 \le\frac{3}{2\pi}(1+24/T)e^{-a}
 <\frac{3(1.009)}{4T}(1+24/630)<.8/T.                   \tag{20}
\]

The exact decomposition
H=2^(1-2z)(2pi^2 J_(9/4)-3pi J_(5/4)+I_theta), with
(17)–(20), now proves
|H/H_*-1|<(24+.8+.03)/T<30/T<1/21. Nonvanishing is a
consequence, not an input. The open set |H/H_*-1|<1 contains S,
so Log(1+v) is holomorphic on a neighborhood of S and agrees with
the real logarithm on the positive real ray. Finally,

\[
 |\operatorname{Log}(1+v)|\le\frac{|v|}{1-|v|}
 <\frac{30/T}{1-30/630}=31.5/T<32/T<.051.
\]

This proves (1) with both sector edges and b=0 included. Applying
L830 is legitimate because its H, H_*, branches, domain and threshold
are exactly those just verified. It supplies the asserted curvature
consequence without any further saddle or Xi-zero assumption.

### Exact scalar verification and limits of the audit

Reproduction command:
`python3 scripts/liu-mao-sector/audit_constants_657.py`.
The full certificate is
`scripts/liu-mao-sector/audit_constants_657.json`. All 37 strict
comparisons pass. Every decision compares rational interval endpoints
with the required exact rational bound; displayed floating decimals
are diagnostic only. In particular the certified intervals lie in
(14.2726,14.2727) for A_4+A_2+A_6 (required <14.4),
(1.2709,1.2710) for A_8 (required <1.3),
(1.6885,1.6886) for (16)'s scalar upper bound (required <2), and
(8.6596,8.6597) for the combined exponential budget (required <9).

The enclosure algorithm is elementary and completely specified.
Fraction arithmetic is rounded outward to a grid of width 10^(-30).
Square-root lower bounds are floor(sqrt(floor(q*10^48)))/10^24;
the corresponding upper bound adds one grid unit. For x>=0, exp(x)
uses S_120=sum_(k=0)^120 x^k/k!, with a remainder between zero and
[x^121/121!]/[1-x/122]; every argument is <122. Negative arguments
use reciprocal intervals and general intervals use monotonicity.
For x>=1, set t=(x-1)/(x+1); log(x) uses
2 sum_(k=0)^159 t^(2k+1)/(2k+1), with tail at most
2t^321/[321(1-t^2)]. For x<1 use -log(1/x).
Pi is enclosed by Machin's identity
pi=16 arctan(1/5)-4 arctan(1/239), using 80 alternating terms
and the first omitted term for each remainder. The identity follows
from the tangent addition formula with the angle in (0,pi/2).
Thus neither transcendental library rounding nor a sampled sector grid
is a premise. The certificate verifies scalar reductions only; the
contour, uniformity, infinite sums and branches are justified above.

No essential failed inequality was found. The first script run hit
Python's integer-string digit limit before producing a certificate;
outward rational rounding fixed that representation issue. It was
not a failed mathematical comparison. The final run completed all cases.

The audit certifies this analytic premise only. A curvature-to-minor
comparison, its growing-degree error budget, and the low coefficient
indices are unpaid. L772 is a contrast showing that generic positivity
is insufficient; it is not a mathematical input to this proof.

## Mathlib

Full matching coverage is not checked. Supporting results for Cauchy
contours, dominated holomorphic integrals, Gaussian moments, Lambert W
and interval arithmetic have not been matched to this exact theorem.
No absence claim is made. [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
