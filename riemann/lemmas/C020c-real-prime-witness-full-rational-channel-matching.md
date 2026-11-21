# C020c — Full rational mixed-channel matching with retained endpoints

## Hypotheses

Use exactly C019 and C019y's fixed witness as positive integers d tend
to infinity. Thus d=T(log(T/(2*pi))-1)/(2*pi), T>2*pi*e,
X=T/sqrt(2d), q=log X, B=(sqrt(2)-1)X, h=3*pi/q,
D=[X,sqrt(2)X-h], L=floor(X^(1/1000)), R=L^4 and N*=N(sqrt(2)X).
Keep the original real Euler-product coefficients alpha of zeta^(-1/2)
on Re(s)>1, all four linear tapers w(a)=(1-log(a)/log L)_+, and

\[
 c_r=\sum_{a_1a_2a_3a_4=r}
       \prod_{j=1}^4\alpha(a_j)w(a_j)(a_2a_4)^{-ih}.
\]

In particular |c_r|<=tau(r), c_r=0 for r>R, and
M(Y)^2M(Y+h)^2=sum c_r r^(-1/2-iY), W=|M(Y)M(Y+h)|^2.
Here tau(r) denotes the divisor function, not the phase variable below.
Retain the exact smooth auxiliary functions

\[
 t(Z)=Z^2/(2d),\quad u(Z)=\tfrac12\log(Z/(2\pi)),\qquad
 E_j(Z)=\exp\{t(Z)((u(Z)-\log j)^2-\pi^2/16)/4
                         +i\pi t(Z)(u(Z)-\log j)/8\},
\]
\[
 N(Z)=\left\lfloor\sqrt{Z/(2\pi)+Z^2/(32d)}\right\rfloor,
 \quad\theta(Z)=\tfrac Z2\log(Z/(2\pi))-\tfrac Z2-\pi/8,
 \quad F(Z)=e^{i\theta(Z)}\sum_{j\le N(Z)}E_j(Z)j^{-1/2-iZ}.
\]

For unordered distinct witness primes p<b in
P=[sqrt(X)/10,sqrt(X)/5] intersect {primes}, put v=pb and

\[
 a_v(Y)=b^{-ih}E_p(Y)E_b(Y+h)+p^{-ih}E_b(Y)E_p(Y+h),
 \quad A(Y)=e^{i(\theta(Y)+\theta(Y+h))}\sum_v a_v(Y)v^{-1/2-iY},
 \quad C(Y)=F(Y)\overline{F(Y+h)}.
\]

All witness sources lie inside both floors on D, as retained in
C019y. Every sum below has m,n<=N*, r,s<=R and all witness v;
no restriction on common factors or rational denominators is added.
No estimate for actual P, RH, nonvanishing or random law is assumed.
C019's quadrature and C019y's finite identities passed audit1421;
C019y's separate resonant estimates remain outside that audit.

## Conclusion

Define the real coefficients g_r=r^(ih/2)c_r. For each tuple put

\[
 \kappa=\frac{mvr}{ns},\quad x=2\pi\kappa,\quad
 \tau=\frac h2\log\frac{mn}{\kappa},\quad
 \gamma_v=2\cos\!\left(\frac h2\log\frac p b\right).
                                                               \tag{1}
\]

For X/2<=x<=2X use the two exact domains, Fresnel integrals and
boundary corrections defined in (4)--(7). Set

\[
 H_0=E_m(x)\overline{E_n(x)}E_p(x)E_b(x),\quad
 Z_j=e^{-ix-i\pi/4}H_0\mathcal F_j\quad(j=0,1),
\]
\[
 k_{mnvrs}=\frac{g_rg_s\gamma_v\sqrt{2x}}{\sqrt{mnvrs}},
 \quad Z_{\rm av}=(Z_0+Z_1)/2,\quad Z_{\rm dif}=(Z_0-Z_1)/2.
\]

Then the complete mixed part of the reference numerator is

\[
 \boxed{\quad
 2\operatorname{Re}\int_D W^2(CA+C\overline A)
 =4\sum_{X/2\le x\le2X}k_{mnvrs}
       \{\cos\tau\operatorname{Re}Z_{\rm av}
              -\sin\tau\operatorname{Im}Z_{\rm dif}\}
       +\mathcal B+\mathcal H
       +O(X^{63/125}q^2).\quad}                           \tag{2}
\]

The error is o(B), uniformly over all sufficiently large integers d.
The finite signed sums B and H in (7),(8) retain, respectively, every
near-center boundary correction and every remote-center endpoint term.
The Fresnel limits retain the true source entries and band endpoints.
Only the smooth center amplitudes have been matched; their displacement
error alone is O(h X^(1/2) R(1+log R)^2)=o(B).

This extends the channel pairing to every rational twist with a paid
analytic residual. It does NOT estimate the displayed signed sums.
In particular F0-F1, B and H have not been shown negligible, and the
finite Fresnel integrals cannot be replaced by full Gaussians here.
The exact shift phase tau is retained, without a small-phase estimate. C020b's
fixed integer-family conclusions remain compatible with (2), but
they supply neither its full arithmetic sum nor its boundary terms.

No lower bound cBq^2 or upper bound O(B) for the fixed quotient follows.
The denominator, unequal-frequency numerator O(G,J), UA channel and
actual-P residual remain unpaid. This is a finite algebra/calculus
specialization of the covered method, not a new general stationary-phase
theorem or a certified originality claim.

## Proof

### 1. Exact coefficient symmetry and channel pairing

Exchange (a1,a3) with (a2,a4) in the finite formula for c_r. The
real tapered product is unchanged, and conjugation of the phase gives

\[
 \overline{c_r}=r^{ih}c_r,\qquad g_r=\overline{g_r}.       \tag{3}
\]

This uses all four original tapers, including their zero boundaries;
it is not an untapered Euler-product approximation.

Let rho_j be the unique positive solution of
rho_j/(2*pi)+rho_j^2/(32d)=j^2. Define

\[
 I_{mn}=[\max(X,\rho_m,\rho_n-h),\sqrt2X-h],\quad
 J_0=I_{mn},\quad J_1=I_{nm}+h,
\]
\[
 J_1=[\max(X+h,\rho_n+h,\rho_m),\sqrt2X],
 \quad \phi(Z)=2\theta(Z)-Z\log\kappa,
\]
\[
 \beta_0(Z)=E_m(Z)\overline{E_n(Z+h)}a_v(Z),\qquad
 \beta_1(Z)=E_n(Z-h)\overline{E_m(Z)}\overline{a_v(Z-h)}.
                                                               \tag{4}
\]

An interval with left endpoint at least its right endpoint contributes
zero to every expression below. In the minus channel of C019 (8)
make the bijective replacement (m,n,r,s) -> (n,m,s,r) and then Z=Y+h.
Its rational twist becomes kappa, and
-phi^(h)_kappa(Z-h)=-phi(Z)-h log kappa. Consequently the exact two
terms for this tuple, before any quadrature, are

\[
 \frac1{\sqrt{mnvrs}}\biggl(
 c_r\overline{c_s}n^{ih}\int_{J_0}\beta_0e^{i\phi}
 +c_s\overline{c_r}m^{ih}e^{-ih\log\kappa}
                   \int_{J_1}\beta_1e^{-i\phi}\biggr).    \tag{5}
\]

Thus both source floors and both translated band endpoints are exact.
Each original term occurs once. The two smooth auxiliary amplitudes
are defined outside their source domains only for quadrature; no
extension of the truncated F or of actual P is made.

### 2. Uniform quadrature and its retained terms

For X/2<=x<=2X, phi'(x)=0, phi''(Z)=1/Z, phi(x)=-x-pi/4.
Use C019's quadratic coordinate

\[
 z(Z)=\operatorname{sgn}(Z-x)\sqrt{\phi(Z)-\phi(x)}.
\]

It is smooth and increasing through x. For a nonempty J_j=[a_j,b_j]
let

\[
 \mathcal F_j=\int_{z(a_j)}^{z(b_j)}e^{iz^2}\,dz.
                                                               \tag{6}
\]

Write Z(z) for the inverse, b_beta(z)=beta(Z(z))Z'(z),
b_beta(0)=beta(x)sqrt(2x), and
r_beta(z)=(b_beta(z)-b_beta(0))/(2iz), with
r_beta(0)=b_beta'(0)/(2i). Define

\[
 \mathfrak b(\beta,J)=e^{i\phi(x)}
                [r_\beta(z)e^{iz^2}]_{z(a)}^{z(b)},
 \quad\mathfrak b^-(\beta,J)
                =\overline{\mathfrak b(\overline\beta,J)},
\]
\[
 \mathcal B=2\operatorname{Re}\sum_{X/2\le x\le2X}
 \frac{c_r\overline{c_s}n^{ih}\mathfrak b(\beta_0,J_0)
       +c_s\overline{c_r}m^{ih}e^{-ih\log\kappa}
                           \mathfrak b^-(\beta_1,J_1)}{\sqrt{mnvrs}}.
                                                               \tag{7}
\]

Empty intervals give F_j=0 and boundary term zero. There is no
interior-center assumption: x may coincide with or lie outside a
source or band endpoint.

For x outside [X/2,2X], keep the nonstationary endpoint functional
e(beta,J)=[beta(Z)e^(i phi(Z))/(i phi'(Z))]_a^b and
e^-(beta,J)=[beta(Z)e^(-i phi(Z))/(-i phi'(Z))]_a^b, again zero
on empty intervals. Define

\[
 \mathcal H=2\operatorname{Re}\sum_{x\notin[X/2,2X]}
 \frac{c_r\overline{c_s}n^{ih}\mathfrak e(\beta_0,J_0)
       +c_s\overline{c_r}m^{ih}e^{-ih\log\kappa}
                            \mathfrak e^-(\beta_1,J_1)}{\sqrt{mnvrs}}.
                                                               \tag{8}
\]

Here and in (7) the phase and boundary functionals depend on the tuple.
They are exact finite definitions, not bounds for their signed sums.

C019 (5),(6),(9)--(13) supply the quadrature with error O(X^(-1/2))
per integral. The following verifies the small change of domain and
amplitude required here. The scales give d comparable to X^2q^2.
For j<=N* and X/3<=Z<=3X, C019 (6) bounds
X^k |E_j^(k)(Z)| by an absolute constant for 0<=k<=3. The same
bounds hold for beta0,beta1 on [X/2,2X], since their arguments
differ by at most h=o(X) and a_v is a sum of two products. Both
nonempty J_j are contained in [X,sqrt(2)X]. The proof of C019's
quadratic-coordinate estimates uses only these derivative bounds
and the enlarged compact interval, not the particular upper endpoint
sqrt(2)X-h. Thus it applies to J1 as well as J0.

More explicitly, r_beta'(z) has supremum plus total variation
O(X^(-1/2)) on the transformed interval. The exact residual is
-e^(i phi(x)) integral r_beta'(z)e^(iz^2) dz. The imported
second-derivative bound gives a uniformly bounded primitive of
e^(iz^2), so partial summation pays that residual. The known input
is Kösters, *On the Occurrence of the Sine Kernel in Connection
with the Shifted Moments of the Riemann zeta function*,
arXiv:0803.1141v2, Appendix A, Lemma A.2 (=Titchmarsh, second
edition, Lemma 4.4), https://arxiv.org/html/0803.1141v2#A . Its
twice-differentiable real phase has second derivative of one sign,
with magnitude at least epsilon>0; here F(z)=z^2 and epsilon=2.
Assessment1409/source-notes1410 already cover this input. The same
bound also gives |F_j|<=C for any of the finite limits in (6).

For remote x, |phi'|=|log(Z/x)| is bounded below positively on
both J_j. Two integrations by parts, using beta^(k)=O(X^(-k))
for k<=2 and phi^(k)=O(X^(1-k)) for k=2,3, give the endpoint
functional with error O(X^(-1)). The same reasoning with negative
phase gives e^-. This verifies the specialization even if the
center x-h used in the unshifted minus coordinate would fall on
the other side of C019's auxiliary regime boundary.

### 3. Matching the smooth center amplitudes

By the derivative bounds just checked, shifting any argument of
an E factor by at most h costs O(h/X), uniformly over every source.
At x in the near regime, therefore,

\[
 \beta_0(x)=v^{-ih/2}\gamma_v H_0+O(h/X),\qquad
 \beta_1(x)=v^{ih/2}\gamma_v\overline{H_0}+O(h/X).       \tag{9}
\]

No heat factor has been replaced by 1, including for small m,n.
The exact identity b^(-ih)+p^(-ih)=v^(-ih/2)gamma_v accounts for
both terms of a_v. Its conjugate gives the other line. Using (3)
and kappa=mvr/(ns), both coefficient phases reduce to the same one:

\[
 c_r\overline{c_s}n^{ih}v^{-ih/2}=g_rg_s e^{i\tau},
\]
\[
 c_s\overline{c_r}m^{ih}e^{-ih\log\kappa}v^{ih/2}
                                      =g_rg_s e^{i\tau}. \tag{10}
\]

The second identity retains the translation phase -h log kappa.
Omitting it would give an incorrect pairing even for integer centers.
The near-center leading terms in (5) now sum to

\[
 k_{mnvrs}e^{i\tau}(Z_0+\overline{Z_1}).                 \tag{11}
\]

Since k is real, twice the real part of (11) is exactly
4k(cos(tau) Re Z_av - sin(tau) Im Z_dif). This is the main sum
in (2), without deleting a rational phase or an endpoint difference.

### 4. Complete summation of the analytic errors

The finite convolution bound gives
sum_(r<=R) |c_r|/sqrt(r)<=2sqrt(R)(1+log R). Also
sum_(m,n<=N*) (mn)^(-1/2)=O(sqrt X), and, by comparison with
all integers rather than any prime-distribution theorem,
sum_v v^(-1/2)=O(sqrt X). Hence

\[
 \sum_{m,n,v,r,s}\frac{|c_rc_s|}{\sqrt{mnvrs}}
                   \le CXR(1+\log R)^2.                 \tag{12}
\]

The same bound holds with |g_rg_s|. Multiplying (12) by the
per-integral quadrature error X^(-1/2) pays both near errors;
the remote error X^(-1) is smaller. In (9), the leading Gaussian
scale is sqrt(2x)=O(sqrt X), and |F_j|<=C. The replacement error
is consequently O(h/sqrt X) per outer coefficient, not O(h).
Its total is at most Ch X^(1/2)R(1+log R)^2. Since
R<=X^(1/250) and h=O(1/q), all these errors are bounded by
C X^(63/125) q^2=o(B). This proves (2).

This payment does not bound the endpoint sums. In particular J0
and J1 generally differ: one cannot silently substitute F1=F0.
If both intervals are nonempty their endpoints differ by at most
2h, whence |F0-F1|<=Ch/sqrt X. If only one interval is nonempty,
its length is at most 2h, giving the same bound; if both are empty
it is immediate. Thus the elementary absolute budget for deleting
the difference part in (2) is only

\[
 O\bigl(hXR(1+\log R)^2\bigr).                           \tag{13}
\]

Relative to Bq^2 this available envelope is of order R/q (using
log R comparable to q), which diverges. This is an inadequate
upper budget, NOT a lower bound or proof that the difference sum
is large. B and H also remain in (2). Full real matching with all
these terms negligible has therefore not been established.

### 5. Exact place in the fixed-quotient problem

C019y (5) becomes N_P=N0+O(G,J)+2 Re integral_D W^2 UA plus
the right side of (2), plus E_P. All terms outside the mixed part
are retained unchanged. The denominator is still
D0+O(J,J)+2 Re integral_D W^2 A^2, with the original convention
at zero denominator. No actual-P estimate is used. A later use of
C019t must retain its unaudited C019j/k/l/s, L320 and L018/L021
contracts. Sign density, ordered intervals, reciprocal root mapping,
bulk separation and L030-L032/C032a positivity remain independent.

### 6. Conceptual audit1421: translation, matching and endpoints

18 November 2026. The audit retains (2)--(13), with every domain,
boundary term and coefficient as stated. C019 audit1421 verifies
the inherited near and remote quadrature and its absolute payment.
Here are the additional checks for this specialization.

The permutation of four factors in (3) is bijective even when a
taper vanishes. The shifted product a2*a4 becomes r/(a2*a4), so
conjugate(c_r)=r^(ih)*c_r exactly. Hence g_r is real, with no
claim that it is positive. In the minus channel, swapping m,n and
r,s changes n*v*s/(m*r) to kappa=m*v*r/(n*s). Under Z=Y+h,
\[
 -2\theta(Y+h)+Y\log\kappa
 =-\bigl(2\theta(Z)-Z\log\kappa\bigr)-h\log\kappa.
\]
The source lower endpoint becomes max(X+h,rho_n+h,rho_m),
the upper endpoint becomes sqrt(2)X, and the amplitude is exactly
beta1 in (4). This proves (5), with the translation factor and
both floors, before any asymptotic approximation.

All arguments in beta0 and beta1 on [X/2,2X] lie in [X/3,3X]
eventually. The derivative proof of C019 therefore applies on
the entire segment connecting x to either endpoint of J0 or J1.
In particular it applies to an external center. For remote x,
both domains lie in [X,sqrt(2)X], so |log(Z/x)|>=log(sqrt(2))
when x>2X and |log(Z/x)|>=log 2 when 0<x<X/2.
Replacing the phase by its negative is exactly conjugation of the
positive functional with conjugated amplitude; it changes neither
error size nor endpoint coverage. Selecting the regime by the
translated x, rather than x-h, is therefore legitimate on both
sides of an auxiliary regime crossing.

The mean value estimate with |E_j'|<=C/X and bounded factors gives
an absolute O(h/X) error in each line of (9), uniformly for every
tuple. It is not a relative estimate and does not divide by any
heat factor. The exact identity
p^(-ih)+b^(-ih)=v^(-ih/2)*gamma_v and its conjugate give the
displayed leading factors. Writing c_r=r^(-ih/2)*g_r, the phase
of each coefficient in (10) is
\[
 h\log n+\tfrac h2\log(s/(vr))
 =\tfrac h2\log(mn/\kappa)=\tau.
\]
For the second coefficient this calculation includes -h log kappa.
Thus the paired leading term is exactly (11). Since
Z0+conjugate(Z1)=2 Re Z_av+2i Im Z_dif, taking twice its real
part gives the factor 4 and the minus sign in (2).

The common bound on the finite Fresnel primitives is the unweighted
Kösters A.2 specialization to F(z)=z^2, epsilon=2, already cited
in Section 2. Multiplication by sqrt(2x) makes the center matching
error O(h/sqrt X), not O(h). The total absolute coefficient mass
is (12), so quadrature and matching together cost at most
\[
 C(1+h)X^{1/2}R(1+\log R)^2
 \le C X^{63/125}q^2=o(B).
\]
This proves the required uniform payment after both the reindexing
and translation. It pays errors only, not B, H or the leading sum.

For completeness let l_j,u_j be the numerical endpoints defining
J_j before an empty interval is set to zero. The maximum formulas
give 0<=l1-l0<=2h and u1-u0=h. If both intervals are nonempty,
their symmetric difference has length at most 3h. If J0 is
nonempty but J1 is empty, l1>=u1 implies l0>=u0-h; if only J1
is nonempty, l1>=l0>=u0. Thus in either one-empty case the
surviving interval has length at most h. On the relevant interval
z'(Z)<=C/sqrt X by the same uniform inverse-coordinate bounds.
Writing F_j as the integral of exp(i*z(Z)^2)*z'(Z) over J_j
proves |F0-F1|<=Ch/sqrt X in every case. Equality or a singleton
has zero contribution. This verifies (13), but its absolute
envelope divided by Bq^2 is of order R/q, which diverges.
The old endpoint-deletion stop is therefore unchanged.

This is a successful local audit of the existing reduction, not an
arithmetic cancellation result. C020a/b, C019y's resonance estimates,
the other numerator channels, denominator and actual-P transfer
are not certified by it. No all-degree Xi sign follows.

## Mathlib

Full matching coverage for this finite, tapered, moving-heat formula
has not been checked. Supporting conjugation, finite-sum or integral
theorems would not alone prove (2) with its uniform error and floors.
The precise classical oscillatory input is cited above and reused
from the prior assessment; no new source theorem or formalization
is claimed. The local reduction passed the scoped conceptual audit1421
above; this is not a formal-library verification.
