# C019 — Saddle and endpoint reduction for the fixed real prime witness

## Hypotheses

Use exactly C019y's definitions and fixed witness, with positive integers
d tending to infinity, and no change to alpha, taper, heat times or floors:
\[
 d=\frac{T}{2\pi}(\log(T/(2\pi))-1),\quad T>2\pi e,\quad
 X=T/\sqrt{2d},\quad q=\log X,\quad B=(\sqrt2-1)X,\quad h=3\pi/q,
\]
\[
 D=[X,\sqrt2X-h],\quad L=\lfloor X^{1/1000}\rfloor,
 \quad R=L^4,\quad H=M(Y)M(Y+h),\quad W=|H|^2,
 \quad H^2=\sum_{r\le R}c_r r^{-1/2-iY}.
\]
Here M has C019y's original linear taper and the real Euler-product
coefficients of zeta(s)^(-1/2) defined on Re(s)>1. In particular
\(|c_r|\le\tau(r)\), by C019p's finite convolution bound.
Keep the smooth auxiliary factors, also when their sources have not entered,
\[
 t(Z)=Z^2/(2d),\quad u(Z)=\tfrac12\log(Z/(2\pi)),\quad
 E_n(Z)=\exp\{t(Z)((u(Z)-\log n)^2-\pi^2/16)/4
                          +i\pi t(Z)(u(Z)-\log n)/8\},
\]
\[
 N(Z)=\lfloor\sqrt{Z/(2\pi)+Z^2/(32d)}\rfloor,
 \quad N_*=N(\sqrt2X),\quad
 \theta(Z)=\tfrac Z2\log(Z/(2\pi))-\tfrac Z2-\pi/8.
\]
Let v run through products of unordered distinct primes p1<p2 in
\([\sqrt X/10,\sqrt X/5]\), and put
\[
 a_v(Y)=p_2^{-ih}E_{p_1}(Y)E_{p_2}(Y+h)
                  +p_1^{-ih}E_{p_2}(Y)E_{p_1}(Y+h),
 \quad A=e^{i(\theta(Y)+\theta(Y+h))}\sum_v a_v(Y)v^{-1/2-iY}.
\]
As in C019y, let \(F(Z)=e^{i\theta(Z)}\sum_{n\le N(Z)}E_n(Z)n^{-1/2-iZ}\),
\(V=F+\overline F\), \(U=F(Y)F(Y+h)\),
\(C=F(Y)\overline{F(Y+h)}\), and \(S=W(A+\overline A)\).
All statements are beyond an absolute existential integer onset.
The result concerns the unchanged finite reference channels; it uses
no estimate or additional hypothesis for actual P.

## Conclusion

Define the finite sums \(\Sigma_A,\Sigma_U,\Sigma_+,\Sigma_-\) in
(8) below, including their truncated Fresnel integrals and endpoint
corrections. With an absolute implied constant,
\[
 \begin{split}
 \int_D W^2A^2&=\Sigma_A+O(\eta_X),\qquad
 \int_D W^2UA=\Sigma_U+O(\eta_X),\\
 \int_D W^2CA&=\Sigma_++O(\eta_X),\qquad
 \int_D W^2C\overline A=\Sigma_-+O(\eta_X),
 \end{split}
 \qquad \eta_X=X^{63/125}q^2=o(B).                         \tag{1}
\]
These are complex error bounds, uniform over all sufficiently large
integer d. Source entries and stationary centers at any endpoint are
included. In C019y's notation they give
\[
 \mathcal D=\mathcal D_0+\mathcal O(J,J)
                         +2\operatorname{Re}\Sigma_A+O(\eta_X),
\]
\[
 \mathcal N_P=\mathcal N_0+\mathcal O(G,J)
       +2\operatorname{Re}(\Sigma_U+\Sigma_++\Sigma_-)
       +\mathcal E_P+O(\eta_X).                            \tag{2}
\]
In particular the analytic error here is smaller than C019z's
Bq^2 resonant scale. No bound or sign for any Sigma or unequal-index
sum is asserted. Neither a cBq^2 lower bound nor an O(B) upper bound
for the full quotient follows. The actual-P residual is unchanged.

This is a reproduction and explicit specialization of the assessed
elementary oscillatory-integral method. The retained boundary correction
is needed to obtain a summable error for these larger coefficient sums;
no new general stationary-phase theorem or novelty is claimed. This
local quadrature and finite assembly passed conceptual audit1421 below.
C019y/z's resonant sign and size conclusions are not certified by that audit.

## Proof

### 1. Smooth phases, exact entries, and derivative bounds

For kappa>0 use the three real phases
\[
 \phi^{(2)}_\kappa(Y)=2\theta(Y)+2\theta(Y+h)-Y\log\kappa,
 \quad \phi^{(0)}_\kappa(Y)=2\theta(Y)-Y\log\kappa,
 \quad \phi^{(h)}_\kappa(Y)=2\theta(Y+h)-Y\log\kappa.
                                                               \tag{3}
\]
Their derivatives and stationary centers are respectively
\[
 \begin{array}{c|c|c}
 &\phi'(Y)&x\\ \hline
 (2)&\log\!\dfrac{Y(Y+h)}{4\pi^2\kappa}
       &(-h+\sqrt{h^2+16\pi^2\kappa})/2\\
 (0)&\log\!\dfrac{Y}{2\pi\kappa}&2\pi\kappa\\
 (h)&\log\!\dfrac{Y+h}{2\pi\kappa}&2\pi\kappa-h
 \end{array}                                                   \tag{4}
\]
For (h), x can lie to the left of zero; no positive-center assumption
is needed in the nonstationary case below. On [X/2,2X], all three
phases satisfy, uniformly in kappa,
\[
 c/X\le\phi''\le C/X,\qquad
 |\phi^{(j)}|\le C_j X^{1-j}\quad(2\le j\le6).           \tag{5}
\]
This follows directly from \(\phi''=1/Y+1/(Y+h),1/Y,1/(Y+h)\).

The defining scales give d comparable to X^2q^2, as in C019u/z.
For n<=N_*=O(sqrt(X)) and X/3<=Z<=3X, write v_n=u(Z)-log n.
Then |v_n|<=Cq, t=O(q^(-2)), and for each fixed j>=1,
\(|v_n^{(j)}|\le C_jX^{-j}\) and
\(|t^{(j)}|\le C_jq^{-2}X^{-j}\) (the latter is zero for j>2).
Differentiating the displayed logarithm of E_n and then its
exponential gives
\[
 \max_{0\le j\le3}X^j|E_n^{(j)}(Z)|\le C.               \tag{6}
\]
The zeroth bound uses the bounded real part of log E_n. Therefore
each of the four amplitudes
\(a_va_w, E_mE_{n,h}a_v, E_m\overline{E_{n,h}}a_v,
E_m\overline{E_{n,h}}\overline{a_v}\), and their conjugates,
has a uniform bound (6) on [X/2,2X]. Here E_(n,h)(Y)=E_n(Y+h).
This is an extension of smooth auxiliary formulas only, not of F or P.

Let rho_n be the unique positive solution of
\(\rho_n/(2\pi)+\rho_n^2/(32d)=n^2\). Strict monotonicity
makes n<=N(Z) exactly Z>=rho_n, including equality. Thus the
joint source domain is the interval
\[
 I_{mn}=[\max(X,\rho_m,\rho_n-h),\sqrt2X-h],             \tag{7}
\]
interpreted as empty if its left endpoint is at least its right
endpoint. A singleton has zero integral. Every witness prime is
inside both floors throughout D by C019y's cutoff fact. Hence
the A^2 channel has domain D, while the other three have I_mn.
No floor has been differentiated or discarded.

### 2. The explicit finite sums

Sections 3–4 define a linear quadrature functional
\(\mathfrak F_\phi[\beta;I]\) for each phase in (3), smooth
amplitude beta, and interval I contained in D. Put
\(\mathfrak F^-_\phi[\beta;I]
=\overline{\mathfrak F_\phi[\overline\beta;I]}\).
For empty intervals both functionals are zero. In the following sums
r,s range from 1 to R, m,n from 1 to N_*, and v,w independently
over all witness prime pairs; repeated primes between v and w
are allowed. All four sums are finite:
\[
 \Sigma_A=\sum_{v,w,r,s}\frac{c_r\overline{c_s}}{\sqrt{vwrs}}
     \mathfrak F_{\phi^{(2)}_{vwr/s}}[a_va_w;D],
\]
\[
 \Sigma_U=\sum_{m,n,v,r,s}
       \frac{c_r\overline{c_s}n^{-ih}}{\sqrt{mnvrs}}
     \mathfrak F_{\phi^{(2)}_{mnvr/s}}[E_mE_{n,h}a_v;I_{mn}],
\]
\[
 \Sigma_+=\sum_{m,n,v,r,s}
       \frac{c_r\overline{c_s}n^{ih}}{\sqrt{mnvrs}}
     \mathfrak F_{\phi^{(0)}_{mvr/(ns)}}
                    [E_m\overline{E_{n,h}}a_v;I_{mn}],
\]
\[
 \Sigma_-=\sum_{m,n,v,r,s}
       \frac{c_r\overline{c_s}n^{ih}}{\sqrt{mnvrs}}
     \mathfrak F^-_{\phi^{(h)}_{nvs/(mr)}}
                    [E_m\overline{E_{n,h}}\overline{a_v};I_{mn}].
                                                               \tag{8}
\]
To check all signs, W^2 contributes exp(iY log(s/r)). The source
products UA, CA, C conjugate(A) contribute respectively the main
phases 2theta(Y)+2theta(Y+h), 2theta(Y), -2theta(Y+h), and the
logarithmic frequencies -log(mnv), log(n/(mv)), log(nv/m).
Their shifted-source constants are n^(-ih), n^(ih), n^(ih).
For A^2 the main phase is 2theta(Y)+2theta(Y+h), with frequency
-log(vw). These are precisely (8); in particular the last phase
has negative sign and the reciprocal rational twist shown there.
Before replacing the four integrals by their functionals, (8) is
the exact finite expansion of the four integrals in (1).

### 3. Stationary range, including clipped endpoints

Suppose the x in (4) lies in [X/2,2X]. For Y in that interval set
\[
 z(Y)=\operatorname{sgn}(Y-x)\sqrt{\phi(Y)-\phi(x)},
 \quad z(x)=0.
\]
Strict convexity makes this a smooth increasing change of variable,
with derivative at x equal to sqrt(phi''(x)/2). Let Y(z) denote
its inverse, and put
\[
 b(z)=\beta(Y(z))Y'(z),\quad b_0=b(0)
       =\beta(x)\sqrt{2/\phi''(x)},\qquad
 r(z)=\frac{b(z)-b_0}{2iz},\quad r(0)=b'(0)/(2i).
\]
For I=[a,b] contained in D, define
\[
 \mathfrak F_\phi[\beta;I]=e^{i\phi(x)}
 \left\{b_0\int_{z(a)}^{z(b)}e^{iz^2}\,dz
                    +[r(z)e^{iz^2}]_{z(a)}^{z(b)}\right\}. \tag{9}
\]
The endpoint named b in I is unrelated to the function b(z).
The integral in (9) has its actual finite limits, even if the
center is outside I or equals a source-entry or band endpoint.
Values of beta at x outside I are allowed because beta is the
smooth auxiliary amplitude, with the source indicator already
fully represented by I. No value of F outside its true floor is used.

Here are uniform derivative details needed for the error. Set
y=Y/X, c=x/X and
\(\Phi(y)=(\phi(Xy)-\phi(Xc))/X\). Then
\(\Phi(c)=\Phi'(c)=0\), and Taylor's integral identity gives
\[
 \Phi(y)=(y-c)^2 P_c(y),\qquad
 P_c(y)=\int_0^1(1-t)\Phi''(c+t(y-c))\,dt.
\]
By (5), P_c is bounded above and below by positive absolute
constants and has uniformly bounded derivatives through order four
on 1/2<=y,c<=2. Thus
\(w=z/\sqrt X=(y-c)\sqrt{P_c(y)}\) is smooth. Its derivative
is bounded above and below positively: away from c use
\(dw/dy=\Phi'(y)/(2w)\) and integrate the positive bounded
Phi'' between c and y; at c take the continuous limit.
The inverse y(w) consequently has uniformly bounded derivatives
through order four on its interval. This also follows by successive
differentiation of w(y(w))=w, since dw/dy is bounded away from zero.

Write \(b(z)=\sqrt X\,\widetilde b(w)\). By (6) and the inverse
bounds, tilde(b) has uniformly bounded derivatives through order
three. Set
\(R_0(w)=(\widetilde b(w)-\widetilde b(0))/(2iw)\), with its
continuous value at zero. The identity
\[
 R_0(w)=\frac1{2i}\int_0^1\widetilde b'(tw)\,dt
\]
shows that R_0 and its first two derivatives are uniformly bounded.
The w-interval has bounded length. Hence r(z)=R_0(z/sqrt(X)) and
\[
 \sup|r'|+\operatorname{Var}(r')\le C X^{-1/2}.           \tag{10}
\]
All connecting points tw belong to the inverse interval, since it
contains zero and both endpoints. These bounds include the case
x=X/2 or 2X by one-sided limits of the same smooth formulas.

Substitute the change of variable and integrate the term
\(b(z)-b_0=2iz\,r(z)\) by parts. The exact residual after (9) is
\[
 -e^{i\phi(x)}\int_{z(a)}^{z(b)}r'(z)e^{iz^2}\,dz.       \tag{11}
\]
The imported second-derivative estimate, Koesters, arXiv:0803.1141v2,
Appendix A, Lemma A.2 (=Titchmarsh, *The Theory of the Riemann
Zeta-function*, second edition, Lemma 4.4), bounds the integral
of exp(iF) by 8/sqrt(epsilon) when F'' has one sign and absolute
value at least epsilon. Apply it to F(z)=z^2, epsilon=2, on any
subinterval. Its primitive is therefore uniformly bounded. An
integration by parts against that primitive and (10) bounds (11)
by C X^(-1/2). The inspected primary statement is at
https://arxiv.org/html/0803.1141v2#A ; assessment1402 and
source-notes1410 already cover this tool. We import that bound,
not reprove it. The preceding explicit change of variables and
boundary correction supply the required specialization.

### 4. Nonstationary range

If x is outside [X/2,2X], define instead
\[
 \mathfrak F_\phi[\beta;[a,b]]
                  =[\beta(Y)e^{i\phi(Y)}/(i\phi'(Y))]_a^b.
                                                               \tag{12}
\]
On D the expressions in (4) then have absolute value at least a
positive absolute constant. For example for type (2), x<X/2
compares Y(Y+h) with (X/2)(X/2+h), while x>2X compares it
with 2X(2X+h). The ratios are bounded away from one on D.
The types (0),(h) use the corresponding ratios Y/x and
(Y+h)/(x+h); x+h is positive for type (h) even when x<0.
The same conclusion holds uniformly for arbitrarily remote centers.

Let gamma=(beta/(i phi'))'. Bounds (5),(6) and the positive
lower bound for |phi'| give |gamma|<=C/X and |gamma'|<=C/X^2.
One integration by parts yields (12) minus integral gamma exp(i phi).
A second integration by parts bounds this last integral by
C/X: its endpoint terms are O(1/X), and the derivative of
gamma/(i phi') is O(1/X^2) over an interval of length O(X).
Thus the error is O(X^(-1)), in particular O(X^(-1/2)).
This argument uses the actual endpoints of I and does not introduce
or discard any source-entry interval.

Combining both ranges, for every phase, amplitude and interval used
in (8),
\[
 \left|\int_I\beta(Y)e^{i\phi(Y)}dY
                    -\mathfrak F_\phi[\beta;I]\right|
                         \le C X^{-1/2}.                 \tag{13}
\]
Complex conjugation proves the identical bound for the negative-phase
functional. No bound deteriorates as a stationary center crosses an
endpoint. The change between definitions (9),(12) need not be
continuous; each has the stated uniform error for its assigned range.

### 5. Summation at the required scale

The finite convolution bound gives
\[
 \sum_{r\le R}|c_r|/\sqrt r
 \le\sum_{ab\le R}(ab)^{-1/2}
 \le2\sqrt R\,(1+\log R).
\]
Also \(\sum_{m,n\le N_*}(mn)^{-1/2}\le4N_*=O(\sqrt X)\).
No prime-distribution theorem is needed for the upper bound
\[
 \sum_v v^{-1/2}
 \le\tfrac12\left(\sum_{p\in\mathcal P}p^{-1/2}\right)^2
 \le\tfrac12\left(\sum_{n\le\sqrt X/5}n^{-1/2}\right)^2
 =O(\sqrt X).
\]
Consequently the absolute sum of the outer coefficients in each
line of (8) is at most
\[
 C X R(1+\log R)^2.                                      \tag{14}
\]
This includes all equal or unequal indices and all repeated prime
patterns; no orthogonality or cancellation is used to pay errors.
Multiplying (13) by (14) gives
\(O(X^{1/2}R(1+\log R)^2)\).
Since R<=X^(1/250), this is O(X^(63/125)q^2)=o(B), proving
(1). Substitution into C019y (5) proves (2). C019z gives the
separately qualified resonant order Bq^2, used only for the scale
comparison in the conclusion, not to estimate any signed remainder.

The first unpaid numerator expression is now
\(\mathcal O(G,J)+2\operatorname{Re}(\Sigma_U+\Sigma_++\Sigma_-)\);
the denominator retains \(\mathcal O(J,J)+2\operatorname{Re}\Sigma_A\).
Their bounds do not follow from (13). C019y's residual identity
and its qualified C019t discussion remain unchanged. In particular
this proof assumes neither a positive denominator nor an actual-P
transfer estimate. RH, the M2 decision and the later Jensen-density
steps remain open.

### 6. Conceptual audit1421: uniformity through every entry crossing

18 November 2026. This audit retains (1), the finite assembly (2), and
(6),(9)--(14), under the original hypotheses and one common sufficiently
large integer onset. It specializes the already assessed A.2 input; it
does not reprove that theorem, evaluate a Sigma, or audit C019z's signed
resonant asymptotic. The following checks make explicit the points at
which uniformity could have failed.

**Scales and coefficient payment.** With lambda=log(T/(2*pi)), the
defining equations give
\[
 d=e^\lambda(\lambda-1),\quad
 X^2=\frac{2\pi^2e^\lambda}{\lambda-1},\quad
 q=\lambda/2-\tfrac12\log(\lambda-1)+\log(\sqrt2\pi).
\]
Consequently d/(X^2q^2) tends to 2/pi^2, and N*=O(sqrt X).
The limits are along the stipulated integer d, since the positive
branch lambda tends to infinity there. For every n<=N* and
Z in [X/3,3X], log E_n and its first three derivatives have the
uniform bounds used in (6). For instance, t^(j)=O(q^(-2)X^(-j))
for j<=2, u-log n=O(q), and its positive derivatives are
O(X^(-j)). Every term in the first three derivatives of log E_n
is therefore O(X^(-j)), and its real part is O(1). The chain rule
gives (6). For base arguments in [X/2,2X], their translates by h
or -h remain in [X/3,3X] eventually, so the same bounds apply.
This uses smooth auxiliary formulas and does not differentiate a floor.

For completeness, the already checked finite coefficient input of
C019p gives (|alpha|*|alpha|)(n)<=1: its prime-power series is
(2-sqrt(1-z))^2, with coefficients 1,1,4a_2,4a_3,..., where
a_2=1/8 and the positive a_j decrease. Convolving this inequality
with itself, and retaining tapers of modulus at most one, gives
|c_r|<=(1*1)(r)=tau(r). This use is entirely on the coefficient
level in Re(s)>1. It imports no reciprocal continuation. Thus
\[
 \sum_{r\le R}\frac{|c_r|}{\sqrt r}
 \le \sum_{ab\le R}\frac1{\sqrt{ab}}
 \le 2\sqrt R\sum_{a\le R}\frac1a
 \le2\sqrt R(1+\log R).
\]
The source pair and witness pair budgets in Section 5 are each
O(sqrt X). For the A^2 channel two witness budgets replace the
source and witness budgets; their product is still O(X).
This verifies (14) for all four expansions, without discarding
equal indices, repeated primes, zero coefficients, or short intervals.

**Connecting segments.** The inverse in Section 3 is defined on the
image of the whole [X/2,2X], not only on the image of I. It includes
z=0 even if x lies outside I. Its rescaled w-image is an interval
containing zero; every tw, 0<=t<=1, in the integral formula for R_0
therefore belongs to the domain of the scaled inverse y(w).
The positive lower bound on Phi'' holds throughout each segment
from c to y. It bounds P_c above and below and, by differentiating
its integral formula, bounds its first four derivatives. Hence w(y)
has four bounded derivatives and a derivative bounded away from zero;
the inverse y(w) has four bounded derivatives. In
tilde b(w)=beta(X*y(w))*y'(w), the three amplitude derivatives and
four inverse derivatives suffice for three bounded derivatives of
tilde b. No derivative of order four of the amplitude is required.
The same smooth formulas extend to a neighborhood of the endpoint
centers, or equivalently give their one-sided limits.

Differentiating R_0's integral formula twice gives uniform bounds
on R_0',R_0''. The w-image has bounded length. Therefore
\[
 \sup|r'|\le C/\sqrt X,\qquad
 \int_{z(a)}^{z(b)}|r''(z)|\,dz
 =\frac1{\sqrt X}\int_{w(a)}^{w(b)}|R_0''(w)|\,dw
 \le C/\sqrt X.
\]
This proves the total-variation part of (10), including intervals
on either side of the stationary point. Set
P(z)=integral from z(a) to z of exp(i t^2) dt. The precisely cited
Kösters A.2 bound gives |P|<=8/sqrt(2) on every such finite interval.
Integration by parts bounds the absolute value of (11) by
(8/sqrt(2))*(sup|r'|+integral|r''|), hence by C/sqrt X.
This is the required weighted application; an absolute bound on
the length of the original oscillatory integral was not used.

**Remote centers and domains.** The logarithmic derivative ratios
in Section 4 stay separated from one on D by an absolute margin
when x is outside [X/2,2X]. For the shifted phase, x+h=2*pi*kappa
is positive even if x<0. The margin holds uniformly for x arbitrarily
close to either excluded auxiliary boundary and for arbitrarily
remote x. Differentiating 1/phi' only uses this lower bound and
phi''=O(1/X), phi'''=O(1/X^2), so the stated bounds for gamma
and gamma' are uniform in kappa. The second integration by parts
costs C/X for every subinterval of D. No endpoint value is lost.

Strict monotonicity of Z/(2*pi)+Z^2/(32d) gives exactly (7).
The fixed gap 1/5<1/sqrt(2*pi) puts every witness prime inside
N(X) eventually, including the floor. Empty and singleton source
domains have zero integral and zero quadrature by definition;
nonempty domains have both endpoints retained. A source-entry
equality or an endpoint equal to x introduces no singular term.
All constants above are independent of the indices and of the
locations of these equalities. Combining them gives
\[
 \frac{X^{1/2}R(1+\log R)^2}{B}
 \le C X^{-62/125}q^2\longrightarrow0,
\]
since R<=X^(1/250). This verifies the required o(B) threshold.
The finite expansion signs in (8) and C019y's identities (3)--(5)
give (2). Bounds or signs for the remaining finite sums, the
actual-P residual, and a nonzero denominator do not follow.

## Mathlib

Full matching coverage for this fixed-witness, moving-heat and
endpoint-corrected reduction has not been checked. Supporting
calculus or integral inequalities would not alone formalize (1).
The classical second-derivative bound is cited precisely above;
its assessed availability is not a claim of Mathlib coverage.
