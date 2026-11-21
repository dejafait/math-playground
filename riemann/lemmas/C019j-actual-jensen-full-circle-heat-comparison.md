# C019j — Actual Jensen full-circle comparison with vanishing-time heat flow

## Hypotheses

Let d tend to infinity through positive integers. Use the actual Riemann
xi-function of L018 and the coefficient convention of L021:
\[
 f(w)=\xi(1/2+w),\qquad F(z)=f(\sqrt z)
     =\sum_{j\geq0}\frac{\gamma(j)}{j!}z^j,\qquad
 \gamma(j)=\frac{j!M_{2j}}{(2j)!}.
\]
The square-root expression denotes its single-valued entire expansion.
Define
\[
 J_d(X)=\sum_{j=0}^d\binom dj\gamma(j)X^j,\quad
 R_d(y)=y^dJ_d(1/y),\quad A_d(y)=(T^2/d)^dR_d(dy/T^2),
\]
with the polynomial extension at y=0, and let T>2 pi e solve
\[
 d=\frac{T}{2\pi}\left(\log\frac{T}{2\pi}-1\right).
\]
These are the conventions of C019c/C019i; none of their saddle estimates
or root-count conclusions is used here. For real d<=q<=2d put
\[
 P_d=d!/d^d,\quad Y=T/\sqrt q,\quad a=Y/\sqrt{2d},\quad t=a^2,
 \quad s_Y=1/2+iY,
\]
\[
 m(Y)=\left|\frac{s_Y(s_Y-1)}2\pi^{-s_Y/2}\Gamma(s_Y/2)\right|,
 \qquad N_d(q)=\frac{P_dq^de^d m(Y)}{\sqrt{2\pi d}}.
\]
The pi power uses the real logarithm. Use precisely D.H.J. Polymath
v2's heat family H_t, normalized by H_0(z)=xi(1/2+iz/2)/8,
as specified in the citation below. No nonvanishing of xi or zeta,
RH, simple zeros, or heat-flow real-zero theorem is assumed.

## Conclusion

There are absolute constants C,d_0>0 such that for every integer d>=d_0,
\[
 \sup_{d\leq q\leq2d}
 \left|\frac{(-1)^dA_d(-q)}{N_d(q)}
             -\frac{8H_{Y^2/(2d)}(2Y)}{m(Y)}\right|
 \leq \frac C{\log d}.                                      \tag{1}
\]
In particular this is the uniform o(1) comparison proposed in
assessment1368. Both normalization factors are strictly positive.
Constants and onset are existential, not certified numerical values.
The separate conceptual audit1372 retains (1), with the uniform-domain
checks below. It supplies no
reference sign margin, root count, simplicity or RH conclusion.

## Proof

### Imported formulas and their exact scope

Use Ken Ono, *An Asymptotic Jensen–Pólya Criterion for GRH*,
[arXiv:2610.38870v1](https://arxiv.org/html/2610.38870v1),
28 October 2026, (2.9), Lemma 12/(4.1)–(4.3) including its explicit
gamma-remainder construction, and the whole-half-plane estimate (4.8)
and its proof. These give, for K=Q,
\[
 A_d(-q)=\frac{P_d}{2\pi i}\oint F(T^2u)e^{-dqu}
                         \frac{du}{u^{d+1}},                \tag{2}
\]
on every counterclockwise circle about zero, and
\[
 |\zeta(s)|\leq C|s|\quad(\Re s\geq1/2,\ |s|\geq2).           \tag{3}
\]
The source proves (3) by cancelling the pole before applying
Phragmen–Lindelof in a strip, then uses the Euler product farther right.
Its unrestricted (3) is used here, not Lemma 13's saddle ratios or
Euler logarithms restricted to q<=c_0 T.

Write c_Q=2^(-1/4) pi^(1/4) and
\[
 \Phi(w)=\frac w2\left(\Log\frac{w}{2\pi}-1\right).
\]
The explicit gamma identity in Lemma 12's proof says
\[
 \frac{(1/2+w)(-1/2+w)}2\pi^{-(1/2+w)/2}
       \Gamma(1/4+w/2)
   =c_Q w^{7/4}e^{\Phi(w)}g(w).                             \tag{4}
\]
Here principal powers are used, and g is holomorphic and nonvanishing
on a neighborhood of the large closed right half-sector
|arg w|<=pi/2. Uniformly there, g(w)=1+O(1/|w|).
Equation (4) is a gamma-factor identity, not cancellation of zeta
from an identity at its possible zeros. With (3) it gives
\[
 f(w)=c_Qw^{7/4}e^{\Phi(w)}g(w)\zeta(1/2+w)                 \tag{5}
\]
in that sector. Its use on both imaginary boundary rays is permitted.
The uniform Stirling input is also recorded in
[DLMF 5.11.1](https://dlmf.nist.gov/5.11.E1) and
[5.11.3](https://dlmf.nist.gov/5.11.E3), in a fixed sector away from
the negative real axis. All uses below remain in the right half-sector.
Gamma is nonzero and has no pole at 1/4+iY/2
([DLMF 5.2(i)](https://dlmf.nist.gov/5.2#i)); thus m(Y)>0.
In particular (4) at w=iY gives the exact and asymptotic identities
\[
 m(Y)=c_QY^{7/4}e^{-\pi Y/4}|g(iY)|
       \asymp Y^{7/4}e^{-\pi Y/4}.                          \tag{6}
\]

Finally import D.H.J. Polymath, *Effective approximation of heat flow
evolution of the Riemann xi function, and a new upper bound for the
de Bruijn–Newman constant*,
[arXiv:1904.12438v2, Section 4, (35)](https://arxiv.org/html/1904.12438v2#S4),
4 August 2019, with its normalization (1)/(4). Its Gaussian integral
holds for every complex z and t>0. At z=2Y, with the integration
variable reversed, it gives exactly
\[
 \frac{8H_{a^2}(2Y)}{m(Y)}
  =\frac1{\sqrt\pi}\int_{\mathbb R} e^{-v^2}
                \frac{f(iY-av)}{m(Y)}\,dv.                 \tag{7}
\]
No zero-location result from that paper is imported.

For clarity, the field substitution is N=r_1=Delta_Q=1, r_2=0,
a_Q=2 pi, mu_Q=7/4. The source's explicit construction specializes to
\[
 g(w)=\left(1-\frac1{4w^2}\right)
 \frac{\Gamma(w/2+1/4)}
 {\sqrt{2\pi}(w/2)^{w/2-1/4}e^{-w/2}}.
\]
Substitution in the gamma prefactor gives exactly c_Q in (4);
this equality does not cancel a possibly zero zeta value. The bound
(3) is the separate whole-half-plane bound in the proof of Lemma 13,
not that lemma's q-restricted conclusion. All its uses below have
Re(s)>=1/2 and |s|>=2. In (7), the source first gives f(iY+av);
v -> -v is permissible by its absolute Gaussian integral formula.
Thus the heat time is t=a^2, with no further factor of four.

These standard formulas and estimates are cited, not reproved.
The coupled-scale error estimate below is the specialization left open
by assessment1368; the checked sources did not print this comparison.
That is a statement of the search's scope, not certified originality.

### Uniform scales and exact full-circle normalization

Put L=log(T/(2 pi)). The defining equation gives
d=e^L(L-1), so L tends to infinity and
log d=L+log(L-1)~L. Consequently, uniformly on the closed q band,
\[
 T\asymp d/\log d,\quad Y\asymp\sqrt d/\log d,\quad
 \log Y\asymp\log d,\quad
 a\log Y=O(1),\quad Y/d=o(1).                               \tag{8}
\]
More explicitly, writing b=q/d in [1,2] gives
\[
 T=\frac{2\pi d}{L-1},\quad
 Y=\frac{2\pi\sqrt d}{\sqrt b(L-1)},\quad
 a=\frac{\sqrt2\pi}{\sqrt b(L-1)},\quad
 \log Y=\tfrac12\log d-\log(L-1)+\log(2\pi)-\tfrac12\log b.
\]
These formulas verify that the constants in (8) are independent of q,
including bounded a log Y. The finitely many onset conditions used
below are checked together at the end of the proof.

In (2) take u=-q^(-1) exp(i theta), -pi<=theta<=pi. This traverses
the circle counterclockwise once. Its endpoints coincide at u=1/q;
the negative-real junction is theta=0. On this entire parameter
interval one may use the continuous square root iY exp(i theta/2)
inside f, since f is even by L018. Also
\[
 u^{-d}=(-1)^d q^d e^{-id\theta},\qquad du/u=i\,d\theta.
\]
Thus, setting v=sqrt(d/2) theta and
\[
 I_d=[-\pi\sqrt{d/2},\,\pi\sqrt{d/2}],\quad
 K_d(v)=\exp\{d(e^{i\sqrt{2/d}\,v}-1-i\sqrt{2/d}\,v)\},
 \quad w_d(v)=iY e^{iv/\sqrt{2d}},
\]
we obtain the exact equality
\[
 \frac{(-1)^d A_d(-q)}{N_d(q)}
    =\frac1{\sqrt\pi}\int_{I_d}K_d(v)
                   \frac{f(w_d(v))}{m(Y)}\,dv.             \tag{9}
\]
Indeed the angular prefactor after normalization is sqrt(d/(2 pi));
the change of variable contributes sqrt(2/d).
There is one full-circle integral, with no doubling of a semicircle,
no connector and no extra radius factor. Equations (7) and (9)
verify the proposed parity, factor 8, time and positive prefactor.

### A local absolute derivative bound, including zeros

For Y sufficiently large and |w-iY|<=Y/4, reflection and conjugation
from L018 give
\[
 |f(w)|=|f(w^\sharp)|,\qquad
 w^\sharp=|\Re w|+i\Im w .
\]
Here Im w>0, |w^\sharp-iY|=|w-iY|, and
3Y/4<=|w^\sharp|<=5Y/4. The segment from iY to w^\sharp
lies in the closed right half-sector, at distance at least 3Y/4
from zero. Along it
\[
 \Phi'(z)=\tfrac12\Log(z/(2\pi)),\qquad
 |\Phi'(z)|\leq C\log Y.
\]
Using (3), (5), the bounded power ratio and bounded g ratio in (6)
therefore proves the absolute estimate
\[
 \frac{|f(w)|}{m(Y)}
       \leq CY\exp(C\log Y\,|w-iY|).                       \tag{10}
\]
This reflection is used only for a modulus bound; it is not
differentiated. When Re(w)<0, w^sharp=-conj(w) and
f(w^sharp)=conj(f(w)); when Re(w)>=0 it is w. For every point
of every disk used in (11), the same pointwise operation therefore
applies, even though it is not a holomorphic map. At the reflected
point |1/2+w^sharp|>=|w^sharp|>=3Y/4, so the entire disk is within
the domain needed for (3) once Y is large. Cauchy's estimate itself
is applied to the original entire f on the original disk.

Let r=1/log Y. Since f is entire, the Cauchy derivative estimate
on a disk of radius r about any z with |z-iY|+r<=Y/4 gives,
from (10),
\[
 \frac{|f'(z)|}{m(Y)}
       \leq CY\log Y\exp(C\log Y\,|z-iY|).                 \tag{11}
\]
The extra factor exp(C log Y r) is an absolute constant.
This argument does not divide by f, so (10)–(11) also hold through
zeros and when a disk crosses the imaginary axis.

### The local comparison

Choose V=d^(1/8). For |v|<=V put h=v/sqrt(2d) and
w_0(v)=iY-av. Taylor's formula for real h gives
\[
 |w_d(v)-iY|\leq a|v|,\quad |w_0(v)-iY|=a|v|,\quad
 |w_d(v)-w_0(v)|\leq \frac{Yv^2}{4d}.                     \tag{12}
\]
Every point of the segment joining these two arguments is within
a|v| of iY. By (8),
aV/Y=V/sqrt(2d) tends to zero and r/Y tends to zero.
Thus every radius-r disk needed in (11) stays in the region of (10)
for one common onset. Since a log Y is bounded, (10)–(12) imply
\[
 \frac{|f(w_d(v))|}{m(Y)}\leq CY e^{C|v|},\quad
 \frac{|f(w_d(v))-f(w_0(v))|}{m(Y)}
       \leq C\frac{Y^2\log Y}{d}v^2e^{C|v|}.              \tag{13}
\]
The difference follows by integrating f' on that straight segment.

Set theta=sqrt(2/d) v. The real-variable Taylor remainder gives
\[
 D_d(v):=d(e^{i\theta}-1-i\theta)+v^2,\qquad
 |D_d(v)|\leq \frac{\sqrt2}{3}\frac{|v|^3}{\sqrt d}.
\]
For |v|<=V the right side is at most (sqrt2/3)d^(-1/8),
and hence at most 1 eventually. Since K_d=e^{-v^2}e^{D_d},
\[
 |K_d(v)-e^{-v^2}|
       \leq C e^{-v^2}\frac{|v|^3}{\sqrt d}.              \tag{14}
\]
Subtract the integrands using
(K_d-e^{-v^2})f(w_d)+e^{-v^2}(f(w_d)-f(w_0)).
The integrals over R of |v|^j exp(-v^2+C|v|), j=2,3,
are finite constants independent of d,q. Thus (13)–(14) show
\[
 \left|\frac1{\sqrt\pi}\int_{-V}^V
    \frac{K_d(v)f(w_d(v))-e^{-v^2}f(w_0(v))}{m(Y)}\,dv\right|
 \leq C\left(\frac Y{\sqrt d}+\frac{Y^2\log Y}{d}\right).
                                                               \tag{15}
\]

### The entire complementary circle

For every v in I_d set h=|v|/sqrt(2d), so 0<=h<=pi/2.
Reflection and conjugation reduce |f(w_d(v))| to the value at
\[
 w^\sharp=Y\sin h+iY\cos h.
\]
Its modulus is Y, so (3) is <=CY and the power and g ratios in
(5)–(6) are bounded. Directly from the principal argument pi/2-h,
\[
 \Re\Phi(w^\sharp)+\pi Y/4
 =\frac Y2\sin h\bigl(\log(Y/(2\pi))-1\bigr)
       +\frac Y2h\cos h+\frac{\pi Y}4(1-\cos h).
\]
For large Y, log(Y/(2 pi))>=0. On [0,pi/2],
sin h<=h, h cos h<=sin h, and 1-cos h<=h^2/2.
It follows that
\[
 \Re\Phi(w^\sharp)+\pi Y/4
       \leq \frac Y2h\log(Y/(2\pi))+\frac{\pi Y}{8}h^2
       \leq C|v|+\frac{\pi Y}{16d}v^2,                    \tag{16}
\]
where (8) pays the linear coefficient uniformly.
For |theta|<=pi, 1-cos theta>=2 theta^2/pi^2, so
|K_d(v)|<=exp(-4v^2/pi^2). Increasing the common onset until
pi Y/(16d)<=2/pi^2 proves, on the whole I_d,
\[
 \frac{|K_d(v)f(w_d(v))|}{m(Y)}
       \leq CY\exp(-2v^2/\pi^2+C|v|).                    \tag{17}
\]
Thus the portions V<|v|<=pi sqrt(d/2), including the endpoints,
have total absolute integral at most
CY exp(-c V^2), for a fixed c>0 and sufficiently large d.
This covers both sides of the negative-real junction and all
complementary angles; no fixed-strip approximation was used.

### The unbounded heat tail

For every real v, reflection and conjugation reduce |f(iY-av)|
to |f(x+iY)| with x=a|v|>=0. Put R=|x+iY|.
Now R>=Y, so (3)–(6) apply even when x is unbounded and yield
\[
 \frac{|f(iY-av)|}{m(Y)}
  \leq CY(1+x/Y)^{11/4}
              \exp\{\Re\Phi(x+iY)+\pi Y/4\}.              \tag{18}
\]
The power 11/4 is 7/4 from the gamma prefactor plus 1 from (3).
The exact exponent, with the limiting interpretation at x=0, is
\[
 \Re\Phi(x+iY)+\pi Y/4
   =\frac x2\bigl(\log(R/(2\pi))-1\bigr)
        +\frac Y2\arctan(x/Y)
   \leq \frac x2\log(Y+x).
\]
The inequality uses Y arctan(x/Y)<=x and R<=Y+x.
As log(Y+x)<=log Y+x/Y, this gives
\[
 \Re\Phi(x+iY)+\pi Y/4
       \leq \frac{a\log Y}{2}|v|+\frac{Y}{4d}v^2.
\]
Also (1+x/Y)^(11/4)<=exp(11|v|/(4 sqrt(2d))).
By (8), for one common onset, (18) consequently gives
\[
 e^{-v^2}\frac{|f(iY-av)|}{m(Y)}
       \leq CY\exp(-3v^2/4+C|v|)\quad(v\in\mathbb R).     \tag{19}
\]
This also verifies absolute integrability uniformly with the stated
prefactor, without restricting v to a fixed vertical strip.
The entire tail |v|>V is at most CY exp(-c V^2).

For completeness, the Gaussian-tail step used for (17) and (19)
follows by taking V>=2C/b in exp(-b v^2+C|v|): on |v|>=V
it is at most exp(-b v^2/2), whose tail is bounded by a constant
times exp(-b V^2/4). Fixed b=2/pi^2 or 3/4 suffices.

### Assembly and qualifications

Combining the exact formulas (7)/(9), local bound (15), and both
absolute tails gives a complete uniform majorant
\[
 |E_d(q)|\leq
 C\left(\frac Y{\sqrt d}+\frac{Y^2\log Y}{d}
                           +Y e^{-c d^{1/4}}\right).      \tag{20}
\]
By (8), its first two terms are O(1/log d) and its last is
o(1/log d), uniformly for d<=q<=2d. This proves (1).
It also implies an eventual bound below 1/20, with no effective
onset claimed.

**Separate uniform-domain audit1372 (17 November 2026).** The exact
field and heat substitutions above were checked against Ono v1 (2.9),
Lemma 12 and the proof of (4.8), and Polymath v2 (1)/(4)/(35).
For (9), write B=T^2. The j-th contribution to the coefficient of
u^d in F(Bu)e^{dyu} is gamma(j)B^j(dy)^(d-j)/(j!(d-j)!);
summing over 0<=j<=d and multiplying by d!/d^d gives the stated
A_d. The square root runs from Y through iY to -Y;
evenness identifies its endpoint values, while du/u=i dtheta fixes
the counterclockwise sign. The polynomial expression is real;
the heat integral is real since its integrands at v and -v are
conjugates. No sign is thereby assigned to either expression.

Here is a simultaneous onset check rather than a q-dependent
choice. Choose the gamma threshold so that 1/2<=|g(w)|<=3/2
in the relevant large right half-sector; fix the constants in (3)--(6) and
one bound for a log Y from the exact b-formulas. Uniformly in b,
min Y tends to infinity, max Y/d tends to zero, and
\[
 \frac{aV+1/\log Y}{Y}
   =\frac{d^{-3/8}}{\sqrt2}+\frac1{Y\log Y}\longrightarrow0.
\]
Consequently one integer d_0 can enforce all of: 3Y/4 above the
gamma threshold and 2; log(Y/(2 pi))>=0; the displayed disk ratio
at most 1/4; (sqrt2/3)d^(-1/8)<=1; pi Y/(16d)<=2/pi^2;
Y/(4d)<=1/4; and V above the two fixed Gaussian-tail cutoffs.
Enlarging this integer also puts [-V,V] inside I_d. These are
finitely many conditions holding uniformly on the closed band.

In (16), combine -sin h+h cos h<=0 first, then use
sin h*log(Y/(2 pi))<=h*log(Y/(2 pi)); no sign assumption on
log(Y/(2 pi))-1 is needed. The resulting quadratic coefficient
is absorbed by the stated circle condition. In (18), for every
x>=0, |1/2+x+iY|<=3R/2 (Y>=1) pays the zeta factor and
R/Y<=1+x/Y pays the power 11/4. The positive arctangent term is
at most x/2 and is canceled by -x/2; log(Y+x)<=log Y+x/Y holds without
an upper bound on x. Hence the heat condition pays the quadratic
term for every real v, not just a growing finite window.

Finally, the exact b-formulas give
\[
 \frac{Y}{\sqrt d}=\frac{2\pi}{\sqrt b(L-1)},\qquad
 \frac{Y^2\log Y}{d}=\frac{4\pi^2\log Y}{b(L-1)^2}.
\]
Both are O(1/log d); the last term of (20) is smaller uniformly.
This independently replays the claimed rate and its common onset.
No mathematical error requiring a change to (1) was found; the
expanded checks document its specialization, not a stronger result.

Every error above is already divided by m(Y); an absolute error
before normalization would not establish (1). No lower bound for xi
or zeta enters, and the reference itself may vanish. No contour
deformation, series rearrangement or asymptotic extension of a
separated-saddle theorem is needed. The only infinite heat integral
is the cited (7), and its full tails have been bounded in (19).
The result concerns the approved closed band only. Independent
reference signs with margins exceeding the comparison error, enough
ordered sample points, strict interval separation and the all-degree
positivity goal remain unproved.

## Mathlib

Full matching coverage is not checked. No theorem identifier for this
coupled-scale Jensen/heat comparison is asserted. The
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/)
is a lookup location only; standard gamma, Cauchy or Gaussian support
would not constitute a formalization of (1) or its uniform tails.
