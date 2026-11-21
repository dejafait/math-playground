# C019t — Power-saving actual-P transfer for the fixed squared pair

## Hypotheses

Use exactly C019j/k/m's actual xi, real normalized Jensen value P,
positive gamma modulus m, heat family H_t, finite sum S_d and real
elementary reference V. Retain

\[
 d=\frac{T}{2\pi}\left(\log\frac{T}{2\pi}-1\right),\quad T>2\pi e,
 \quad X=T/\sqrt{2d},\quad q=\log X,\quad
 B=(\sqrt2-1)X,\quad h=3\pi/q,
\]
\[
 J=[X,\sqrt2X],\qquad D=[X,\sqrt2X-h],\qquad
 t_d(Y)=Y^2/(2d),\quad
 N_d(Y)=\left\lfloor\sqrt{Y/(2\pi)+Y^2/(32d)}\right\rfloor.
\]

Thus P(Y)=(-1)^d A_d(-T^2/Y^2)/N_d^{norm}(T^2/Y^2), with
C019m (1)'s strictly positive normalization. V is exactly C019m (7),
with each shifted value retaining its own time and true source floor.
Let d tend through positive integers. All constants and onsets below
are absolute and existential, uniformly on the indicated closed band.

Keep C019p's Euler-product coefficients alpha of zeta(s)^(-1/2) on
Re(s)>1, L=floor(X^(1/1000)), omega(n)=log(L/n)/log L, and

\[
 M(Y)=\sum_{n\le L}\alpha(n)\omega(n)n^{-1/2-iY},\qquad
 W(Y)=|M(Y)M(Y+h)|^2,\qquad R=L^4.
\]

Eventually L>=2 and 0<h<B. No RH, nonvanishing, simple-zero,
random-law or critical-line reciprocal hypothesis is used.

## Conclusion

The inherited actual-Jensen comparison can be strengthened, on this
unchanged band, to

\[
 \sup_{Y\in J}\left|P(Y)-\frac{8H_{t_d(Y)}(2Y)}{m(Y)}\right|
       =O(X^{-1/2}/q),\qquad
 \sup_{Y\in J}|P(Y)+V(Y)|=O(X^{-1/4}).                    \tag{1}
\]

With C019s's exact nonnegative integrals

\[
 I_P=\int_D P(Y)^2P(Y+h)^2W(Y)^2\,dY,\qquad
 I_V=\int_D V(Y)^2V(Y+h)^2W(Y)^2\,dY,
\]

the full squared-mass transfer satisfies

\[
 \|(PP_h-VV_h)W\|_{L^2(D)}
 \le C\{X^{1/4}R^{1/2}q^{1/2}+q^2\}
 =O(X^{63/250}q^{1/2})=o(\sqrt X),                         \tag{2}
\]
\[
 |\sqrt{I_P}-\sqrt{I_V}|
       =O(X^{63/250}q^{1/2})=o(\sqrt B).                   \tag{3}
\]

Consequently the approved target I_P=O(B) holds if and only if
I_V=O(B). This removes the separate unproved mixed-energy thresholds
from C019s's sufficient transfer route. Neither quartic bound is
proved here. All moving-heat quartic channels and their cancellation
remain in I_V. C019s's termwise quartic stop is unchanged.

This is a local reproduction using elementary upper bounds and the
existing comparison machinery, not a new literature-level moment
theorem. It supplies no sign-density theorem, ordered root selection,
bulk separation or RH candidate. Independent conceptual audit1458 below
retains (1)--(3), with the same hypotheses and existential uniform onset.

## Proof

### Existing inputs and the one elementary refinement

The prior ready assessment1402 covers the unchanged squared-pair
target and its actual-P transfer. The refinement below uses the
already proved counting identity L320 (5), C019j's exact normalized
integral formulas and its global tails, C019k's heat-source error,
C019m's unweighted square, C019p's coefficient bounds and C019s's
weight mass and L2 inequality. No inaccessible source or new moment
formula is an input.

For precise inherited source normalization, C019j (7)/(9) specializes
Ken Ono, *An Asymptotic Jensen–Pólya Criterion for GRH*,
[arXiv:2610.38870v1](https://arxiv.org/html/2610.38870v1),
28 October 2026, (2.9) and Lemma12/(4.1)--(4.3), and D.H.J. Polymath,
*Effective approximation of heat flow evolution of the Riemann xi
function, and a new upper bound for the de Bruijn–Newman constant*,
[arXiv:1904.12438v2, Section4, (35)](https://arxiv.org/html/1904.12438v2#S4),
4 August 2019, with (1)/(4)'s normalization. C019k (3) imports that
same Polymath version's Corollary6.5 and (70)--(74), including all
three source errors. Those formulas are retained, not reproved or
applied with a changed floor. The sectorial gamma estimates used in
C019j are also [DLMF5.11.1](https://dlmf.nist.gov/5.11.E1) and
[5.11.3](https://dlmf.nist.gov/5.11.E3), away from the negative real
axis. Their already established local specialization is used below.

Here is the required elementary improvement of the zeta upper bound.
For Y>=2, uniformly in sigma>=1/2 and 3Y/4<=tau<=5Y/4,

\[
 |\zeta(\sigma+i\tau)|\le C\sqrt Y.                         \tag{4}
\]

To see its exact domain without importing a stronger convexity
theorem, put s=sigma+i tau and take the integer N=ceil(Y). Splitting
L320 (5)'s absolutely convergent fractional-part integral at N and
integrating the finitely many intervals below N gives

\[
 \zeta(s)=\sum_{n\le N}n^{-s}
       +\frac{N^{1-s}}{s-1}
       -s\int_N^\infty\{x\}x^{-s-1}\,dx
       \quad(\operatorname{Re}s>0,\ s\ne1).                \tag{5}
\]

For verification of the finite endpoint convention,
s integral_1^N floor(x)x^(-s-1)dx equals
sum_(n<=N)n^(-s)-N^(1-s). Thus (5) uses n<=N with no half-endpoint
term. L320 already justifies analytic continuation and local uniform
convergence of the tail; no further infinite interchange is needed.
For 1/2<=sigma<=2 the three absolute bounds in (5) are respectively

\[
 2\sqrt N,\qquad
 \frac{N^{1/2}}{3Y/4},\qquad
 \frac{|s|}{\sigma}N^{-\sigma}\le C Y/\sqrt N.
\]

Their sum is O(sqrt Y), uniformly. For sigma>=2 the absolutely
convergent Dirichlet series gives |zeta(s)|<=zeta(2). This proves
(4) on its whole stated half-plane. It is elementary truncation of
the existing Euler counting identity, not a zero-free estimate or a
novel bound. The finite calculation is included because its uniform
domain, rather than a pointwise critical-line estimate, is needed.

### Local comparison with the stronger absolute bound

Write f(w)=xi(1/2+w). C019j's gamma factorization, its positive m(Y),
and reflection/conjugation show, for |w-iY|<=Y/4, that

\[
 \frac{|f(w)|}{m(Y)}
       \le C\sqrt Y\exp(C\log Y\,|w-iY|).                 \tag{6}
\]

Indeed w^sharp=|Re(w)|+i Im(w) has the same f modulus and the same
distance to iY; 3Y/4<=Im(w^sharp)<=5Y/4. Equation (4) applies to
1/2+w^sharp, including arbitrarily large real part. In C019j (4)--(6)
the power and g ratios are bounded on this disk, and integrating
Phi'(z)=Log(z/(2*pi))/2 along the segment from iY to w^sharp
costs at most C log Y times that distance. The entire segment stays
in the right half-sector and at modulus at least 3Y/4. These are
exactly the gamma-domain conditions of C019j (10); only its zeta
prefactor Y has been replaced by sqrt Y.

For r_0=1/log Y, Cauchy's estimate on the original entire f, for
|z-iY|+r_0<=Y/4, therefore gives

\[
 \frac{|f'(z)|}{m(Y)}
       \le C\sqrt Y\log Y\exp(C\log Y\,|z-iY|).            \tag{7}
\]

Reflection in (6) is only a pointwise modulus operation; it is never
differentiated. The Cauchy disk may cross the imaginary axis and may
contain zeros. There is no division by f or zeta.

Use C019j's exact two integrals, now with radial argument T^2/Y^2,
and its notation

\[
 a=Y/\sqrt{2d},\quad U=d^{1/8},\quad
 w_d(v)=iY e^{iv/\sqrt{2d}},\quad w_0(v)=iY-av,
\]
\[
 K_d(v)=\exp\{d(e^{i\sqrt{2/d}v}-1-i\sqrt{2/d}v)\}.
\]

On |v|<=U, C019j (12)/(14) give

\[
 |w_d-iY|,|w_0-iY|\le a|v|,\qquad
 |w_d-w_0|\le Yv^2/(4d),
\]
\[
 |K_d-e^{-v^2}|\le C e^{-v^2}|v|^3/\sqrt d.                \tag{8}
\]

Every point on the segment between w_d and w_0 lies at distance
at most aU from iY. The common-onset condition
(aU+r_0)/Y=d^(-3/8)/sqrt(2)+1/(Y log Y) ->0 is uniform on J.
Thus all the disks for (7) lie in (6)'s domain. Since a log Y is
bounded uniformly, (6)--(8) and integration of f' along that segment
give, on this entire growing local interval,

\[
 \frac{|f(w_d)|}{m(Y)}\le C\sqrt Y e^{C|v|},\qquad
 \frac{|f(w_d)-f(w_0)|}{m(Y)}
       \le C\frac{Y^{3/2}\log Y}{d}v^2 e^{C|v|}.
\]

Subtract the exact integrands as
(K_d-e^(-v^2))f(w_d)+e^(-v^2)(f(w_d)-f(w_0)). The integrals of
|v|^2 e^(-v^2+C|v|) and |v|^3 e^(-v^2+C|v|) over the real line
are finite absolute constants. The normalized local difference is
therefore at most

\[
 C\left(\frac{Y^{1/2}}{\sqrt d}
              +\frac{Y^{3/2}\log Y}{d}\right).              \tag{9}
\]

Keep the original, weaker global bounds in C019j (17)/(19).
They pay both the full complementary circle and the unbounded
Gaussian tail by C Y exp(-c U^2), with fixed positive c and the
same closed-band uniformity. No sharper local estimate is used
outside its domain. Combining these tails with (9) yields

\[
 \left|P(Y)-\frac{8H_{t_d(Y)}(2Y)}{m(Y)}\right|
 \le C\left\{\frac{Y^{1/2}}{\sqrt d}
       +\frac{Y^{3/2}\log Y}{d}+Y e^{-c d^{1/4}}\right\}.
                                                               \tag{10}
\]

C019m's scales give Y comparable to X, log Y comparable to q and
d comparable to X^2 q^2, uniformly on J. Both algebraic terms in
(10) are O(X^(-1/2)/q); the exponential term is smaller. This
proves the first assertion in (1). Combining it with C019k (3)'s
O(X^(-1/4)) error and C019m (8)'s S_d+V=O(X^(-3/4)) proves the
second assertion. This comparison includes every source entry;
neither heat time nor floor has been frozen or differentiated.

### All weighted product-comparison terms are paid

C019p's prime-power coefficient proof gives |alpha(n)|<=1, and
0<=omega(n)<=1. Hence, at every real Y,

\[
 |M(Y)|\le\sum_{n\le L}n^{-1/2}\le2\sqrt L,\qquad
 0\le W(Y)^2\le256L^4=256R.                               \tag{11}
\]

C019m (2),(8) imply integral_J V^2=O(Xq), by
V^2<=2S_d^2+2|V+S_d|^2. For j=0,h, D+j is contained in J.
Consequently C019s's mixed energies obey the unconditional, coarse
upper bounds

\[
 E_j=\int_D V(Y+j)^2W(Y)^2\,dY\le C R Xq.                  \tag{12}
\]

These bounds do not assert E_j=O(Xq^2). Their role is different:
the power saving in (1) now makes them sufficient. C019s (2) gives
mathcal H=integral_D W^2=O(Xq^4), including its full off-diagonal
error. Put e=P+V and epsilon=sup_J|e|<=C X^(-1/4). The exact
identity and C019s (3) are

\[
 (PP_h-VV_h)W=(-eV_h-Ve_h+ee_h)W,
\]
\[
 \|(PP_h-VV_h)W\|_2
 \le\epsilon(\sqrt{E_0}+\sqrt{E_h})
                          +\epsilon^2\sqrt{\mathcal H}.
\]

Inserting (12) and the full weight mass gives (2)'s first bound.
Since R<=X^(1/250), X^(1/4)R^(1/2)q^(1/2)
<=X^(63/250)q^(1/2), and q^2 is eventually smaller than that
quantity. Its ratio to sqrt X is
X^(-31/125)q^(1/2), which tends to zero. Equivalently, the squared
L2 transfer cost is O(X^(63/125)q)=o(X); the required threshold is
O(X), so every comparison contribution is paid with room to spare.

Finally sqrt(I_P) and sqrt(I_V) are the L2 norms of PP_h W and
VV_h W. The reverse triangle inequality proves (3), regardless
of their signs or whether any factor vanishes. Since B is the fixed
positive constant (sqrt(2)-1) times X, (3) proves the claimed
equivalence of the two O(B) bounds in both directions.

All mollifier sums and reference entry decompositions are finite.
The only infinite integrals used are (5)'s absolutely convergent
tail and the previously controlled Gaussian integral. The proof
does not identify a quartic stationary tuple, discard a heat channel,
factor correlated moments, import an ordinary fourth-moment formula,
or assert that a previously failed upper bound is a lower bound.
The remaining exact reference quartic is still an open condition.

### Independent conceptual audit1458 — 18 November 2026

This audit uses the prior EXPLORE coverage in assessment1456, completed
by source-review1457. It reuses the cited circle/gamma/heat inputs and
C019j/k/m's separate audits, and checks the precise portions of C019p/s
used here. No new source theorem, quartic estimate or mathematical
hypothesis is introduced. The outcome is retention of (1)--(3), not
a stronger estimate or a claim beyond the sources checked.

**Truncation, reflection and derivative domains.** First take Re(s)>1
in L320(5). Splitting at the integer N gives

    s integral_1^N floor(x)x^(-s-1) dx
      = sum_(n=1)^(N-1) n(n^(-s)-(n+1)^(-s))
      = sum_(n<=N) n^(-s) - N^(1-s).

The tail of floor(x)=x-{x} supplies N^(1-s)/(s-1) after this
subtraction. Thus (5) has exactly the displayed sign and endpoint
convention. For 1/2<=sigma<=2, |s|<=C Y, |s-1|>=3Y/4,
and the fractional-part remainder is at most |s|N^(-sigma)/sigma.
Together with sum_(n<=N)n^(-sigma)<=2sqrt(N) this proves (4),
uniformly for N=ceil(Y). For sigma>=2 the ordinary absolutely
convergent series supplies the independent bound zeta(2).
The identity extends to sigma>0, s!=1 by the locally uniformly
convergent fractional-part tail, as in L320(5); the floor tail is used
only for Re(s)>1. No critical-line reciprocal or zero-free input enters.

For every point w in |w-iY|<=Y/4, reflection preserves both |f(w)|
and the distance to iY, and places the argument in the right half-sector
with imaginary part between 3Y/4 and 5Y/4. Its entire segment from iY
has modulus at least 3Y/4. Thus the precise gamma factorization in
C019j(4)--(6) has bounded power and g ratios there and
|Phi'|<=C log Y. This verifies (6). Cauchy's estimate uses the original
entire f on a radius 1/log(Y) disk, not a derivative of the reflection
map. The extra exponential factor on that disk is bounded by e^C.
For every interpolation segment in (8), all such disks lie in (6)
since their relative distance is at most

    d^(-3/8)/sqrt(2) + 1/(Y log Y) -> 0

uniformly on J. Zeros and crossing the imaginary axis cause no loss.

**Exact normalization, local error and both tails.** The radial
parameter r(Y)=T^2/Y^2 decreases from 2d to d on J and satisfies
T/sqrt(r(Y))=Y. C019j(9) therefore gives exactly P, including parity,
the positive normalization and the factor 1/sqrt(pi). C019j(7) gives
exactly the heat expression with time Y^2/(2d) and factor 8.
Its lower-half-plane gamma modulus in C019k equals m(Y) by conjugation.
The local kernel error is O(e^(-v^2)|v|^3/sqrt(d)), while the argument
error is at most Yv^2/(4d). Applying (6)/(7) and integrating the two
fixed Gaussian majorants gives precisely the two terms in (9).

The stronger prefactor sqrt(Y) is used only in this local part.
On the full complementary circle, C019j(17) supplies
CY exp(-2v^2/pi^2+C|v|); on the entire unbounded heat line,
C019j(19) supplies CY exp(-3v^2/4+C|v|). Their integrals over
|v|>d^(1/8) are O(Y exp(-c d^(1/4))) with one fixed c>0.
In particular the heat tail is not truncated at a second finite height.
Since Y is comparable to X and d to X^2q^2, (10) is
O(X^(-1/2)/q) uniformly. The exact sum of differences is

    P+V = (P-8H/m) + (8H/m-S_d) + (S_d+V).

C019k(3) pays its middle term at O(X^(-1/4)), including the full
uncorrected source remainder; C019m(8) pays its last at O(X^(-3/4)).
Both are pointwise on the closed band with each argument's own heat
time and floor. C019k's source endpoints N=k,p=1 at integral cutoff
are included, as is the p -> -1 limit from below. No finite sum is
differentiated across an entry and no continuity of S_d is assumed.

**Full weight and all three product errors.** C019p's prime-power
calculation gives |alpha(n)|<=1 and |b_k|<=1 for the original finite
tapers, without continuation of zeta^(-1/2) to the critical line.
Thus |M|<=2sqrt(L), W<=16L^2, and W^2<=256L^4=256R.
The power of the weight here is W^2, as required by the L2 norm.
C019m(2),(8) imply integral_J V^2=O(Xq). Since D and D+h are
contained in J, both E_j are at most C R Xq.

C019s(2)'s full weight proof is also checked: |c_r|<=tau(r),
tau(r)^2<=d_4(r) by (e+1)^2<=binom(e+3,3) at every prime power,
and the resulting diagonal is at most |D|(1+log R)^4. For each
unordered unequal pair the two conjugate terms together cost at most
16/log(s/r), because |c_r|/sqrt(r)<=2. Summing with
log(s/r)>=(s-r)/s gives at most 16R^2(1+log R). Thus its
off-diagonal error is retained and is O(X^(1/125)q)=o(X).
This proves the required Hcal=O(Xq^4); no quartic moment of V enters.

With epsilon=O(X^(-1/4)), the two mixed L2 terms are each bounded
by C X^(1/4)R^(1/2)q^(1/2). The pure error is at most
C X^(-1/2)*sqrt(Xq^4)=Cq^2, including the weight error just paid.
The algebraic identity in the proof has all three signs correct,
and D+j subset J permits the same supremum for both error factors.
Since R<=X^(1/250), the exponent is exactly

    1/4 + 1/500 = 63/250 < 1/2.

After division by sqrt(B), the two displayed costs tend to zero as
X^(-31/125)sqrt(q) and X^(-1/2)q^2. The squared combined cost is
O(X^(63/125)q)=o(X)=o(B). This verifies the achieved norm against
the required threshold without assuming either I_P or I_V is O(B).
The reverse triangle inequality then proves (3) and both directions
of their O(B) equivalence, including vanishing or sign-changing factors.

One absolute onset enforces the inherited source/gamma thresholds,
the disk condition, the kernel remainder bound, both Gaussian-tail
cutoffs, L>=2 and h<B. Each condition holds uniformly on the compact
ratio band Y/X in [1,sqrt(2)], so their finite maximum is admissible.
No numerical value for that onset is certified. The audit does not
check unrelated portions of C019s or later uses of this lemma.
The reference quartic, signed numerator, root selection and actual-Xi
all-degree positivity remain independent unproved obligations.

## Mathlib

Full matching coverage is unchecked. Euler summation, analytic
continuation, Cauchy's derivative estimate, gamma asymptotics,
finite-sum bounds and L2 triangle inequalities are supporting
ingredients, not a claimed formalization of this moving-time
actual-Jensen transfer. No absence claim is made.
