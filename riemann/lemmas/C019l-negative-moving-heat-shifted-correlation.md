# C019l — Negative shifted correlation for the moving heat reference

## Hypotheses

Use exactly C019k's functions and conventions, including its positive
integer d, T, principal branches, gamma modulus m, moving time
t_d(Y)=Y^2/(2d), finite real sum S_d, and actual source floor
\[
 N_d(Y)=\left\lfloor\sqrt{\frac{Y}{2\pi}+\frac{Y^2}{32d}}\right\rfloor.
\]
Put
\[
 X=Y_-=\frac{T}{\sqrt{2d}},\quad Y_+=\sqrt2X,\quad
 B=(\sqrt2-1)X,\quad q=\log X,\quad h=\frac{3\pi}{q}.
\]
All assertions are for sufficiently large d, with one absolute,
existential onset. In particular q>1 and 0<h<B. Each factor
S_d(Y+h) uses its own time and its own floor. No RH, nonvanishing,
simple-zero, or heat real-zero hypothesis is made.

## Conclusion

Define the absolute real constant
\[
 {\cal K}=\frac{2}{\sqrt2-1}
   \int_1^{\sqrt2}\int_0^{1/2}
     \exp\left(\frac{\pi^2\lambda^2z^2}{8}\right)
       \cos(3\pi z)\,dz\,d\lambda.
                                                               \tag{1}
\]
Then
\[
 \int_X^{\sqrt2X-h}S_d(Y)S_d(Y+h)\,dY
     =Bq{\cal K}+O(X\log q),\qquad
 {\cal K}\leq-\frac{2}{3\pi}.                                  \tag{2}
\]
In particular the proposed correlation (C) holds, with the absolute
choice c=1/(3*pi):
\[
 \int_X^{\sqrt2X-h}S_d(Y)S_d(Y+h)\,dY
       \leq-\frac{1}{3\pi}B\log X                              \tag{3}
\]
beyond a common onset. The constant implicit in (2) is absolute.

The separate conceptual audit1381 below retains this local intermediate
result. It gives neither quantitative ordered sign samples nor a Jensen
root count. Actual-Xi all-degree positivity and RH remain unresolved.
The assessed sources do not state this moving-heat specialization;
no certified originality or progress beyond all literature is claimed.

## Proof

### Standard inputs and uniform scales

The exact starting formulas are C019k (1)--(2). For the gamma modulus,
use the same fixed-sector Stirling input as C019k:
[DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3) and
[5.11.4](https://dlmf.nist.gov/5.11.E4), with leading coefficient g_0=1.
It applies to s/2=1/4-iY/2 uniformly in the fixed sector
|arg(s/2)|<=pi/2. We use its relative O(1/Y) estimate only pointwise;
no derivative of its error is taken.

We also import two classical estimates, as stated with their hypotheses
in H. Kösters, *On the Occurrence of the Sine Kernel in Connection with
the Shifted Moments of the Riemann zeta function*, 5 September 2008,
[arXiv:0803.1141v2, Appendix A](https://arxiv.org/html/0803.1141v2#A):

* Lemma A.2 (Titchmarsh, *The Theory of the Riemann Zeta-function*,
  second edition, Lemma 4.4): for real twice differentiable F on
  [a,b] with F''>=epsilon>0 throughout, or F''<=-epsilon throughout,
  the absolute value of the integral of exp(iF) is at most
  8/sqrt(epsilon).
* Lemma A.3 (the same book, Lemma 7.2):
  sum_{1<=m<n<=M} 1/(sqrt(m*n)*log(n/m))=O(M log M).

The first estimate will be applied on every subinterval and then
extended to varying amplitudes by integration by parts. Its derivative
hypothesis is verified below. No shifted-zeta moment theorem, frozen
heat time, or unweighted correlation formula is imported. This proof
derives the weight, phase and entry-domain changes required here.

Write L=log(T/(2*pi)). The exact scale identities in C019k give
\[
 d=e^L(L-1),\quad
 X=\frac{\sqrt2\pi\sqrt d}{L-1},\quad
 q=\frac L2-\frac12\log(L-1)+\log(\sqrt2\pi).
                                                               \tag{4}
\]
Consequently q~L/2, X tends to infinity, d is comparable to X^2q^2,
and, uniformly for X<=Y<=sqrt2X,
\[
 t=\frac{Y^2}{2d}=O(q^{-2}),\quad
 \ell=\log(Y/(2\pi))=q+O(1),\quad
 t q^2=O(1),\quad N_d(Y)\asymp\sqrt X.                         \tag{5}
\]
All constants below are independent of d,Y and the summation indices
in their stated ranges. Let M=N_d(sqrt2X); then M<=C sqrt X.
Auxiliary functions for every 1<=n<=M will be considered throughout
the whole band, even before n has entered the actual sum.

### A paid elementary phase reduction

Set s=1/2-iY and u=log n. Combining all three heat factors in
C019k gives the exact identity
\[
 S_d(Y)=2\operatorname{Re}\left\{
  \frac{8G_0(s)}{m(Y)}
   \sum_{n\leq N_d(Y)}n^{-1/2}e^{iYu}
       \exp\left(\frac t4(\alpha(s)-u)^2\right)\right\}.        \tag{6}
\]
The exact formulas there imply
\[
 \alpha(s)=\frac{\ell}{2}-\frac{i\pi}{4}+O(Y^{-1}),\qquad
 \frac{8G_0(s)}{m(Y)}
      =-e^{-i\vartheta(Y)}(1+O(Y^{-1})),\quad
 \vartheta(Y)=\frac Y2\ell-\frac Y2-\frac{\pi}{8}.              \tag{7}
\]
Here the error in the second formula is complex. To check its phase
and sign without any differentiated asymptotic, put z=s/2. The
factor s(s-1)=-(Y^2+1/4) is negative real. The imaginary part of
(z-1/2)Log(z)-z is
-arg(z)/4-(Y/2)log|z|+Y/2. Using
arg(z)=-pi/2+O(1/Y) and log|z|=log(Y/2)+O(1/Y^2), and adding
(Y/2)log pi, gives -vartheta(Y)+O(1/Y). Stirling makes the
modulus of 8G_0/m equal to 1+O(1/Y). The first formula in (7)
follows directly from the two rational terms in alpha and the
principal Log(s/(2*pi)).

Define, for all 1<=n<=M,
\[
 v_n(Y)=\frac{\ell}{2}-\log n,\quad
 a_n(Y)=n^{-1/2}
   \exp\left\{\frac t4\left(v_n(Y)^2-\frac{\pi^2}{16}\right)\right\},
\]
\[
 f_n(Y)=\vartheta(Y)-Y\log n+\frac{\pi t}{8}v_n(Y),\qquad
 V(Y)=2\sum_{n\leq N_d(Y)}a_n(Y)\cos f_n(Y).
                                                               \tag{8}
\]
Since |v_n|<=Cq and t q^2<=C, replacing alpha in (6) by its
leading value changes its heat exponent by O(t q/Y)=O(1/Y).
The exponents have bounded real parts, so this is a relative
O(1/Y) error in each bounded weight. Equations (6)--(8) thus give,
uniformly, including at every floor threshold,
\[
 S_d(Y)=-V(Y)+O(X^{-3/4}),\qquad
 |S_d(Y)|+|V(Y)|\leq C X^{1/4}.                               \tag{9}
\]
Indeed sum_{n<=M} n^{-1/2}<=2 sqrt M. In particular,
\[
 \int_X^{\sqrt2X-h}S_d(Y)S_d(Y+h)\,dY
  =\int_X^{\sqrt2X-h}V(Y)V(Y+h)\,dY+O(\sqrt X).                \tag{10}
\]
Both floors and times are still exact. The gamma normalization has
been removed with a paid product error, not simply dropped.

### Variation, explicit phase derivatives and actual entry intervals

Put c_0=pi/8, used only in the following derivative formulas.
Direct differentiation of the elementary functions (8) gives
\[
 \begin{split}
 (\log a_n)'&=\frac{t}{2Y}
          \left(v_n^2+\frac{v_n}{2}-\frac{\pi^2}{16}\right),\\
 f_n'&=v_n+\frac{c_0t}{Y}(2v_n+1/2),\\
 f_n''&=\frac{1}{2Y}+\frac{c_0}{2d}(2v_n+3/2),\\
 f_n'''&=-\frac{1}{2Y^2}+\frac{c_0}{2dY}.
 \end{split}                                                  \tag{11}
\]
Thus, uniformly for 1<=n<=M on the whole band,
\[
 |a_n|\leq Cn^{-1/2},\quad |a_n'|\leq C(X\sqrt n)^{-1},
 \quad f_n''=\frac1{2Y}+O(q/d),\quad |f_n'''|\leq C/X^2.
                                                               \tag{12}
\]
For each ordered pair m,n define its actual integration domain
\[
 I_{mn}=\{Y\in[X,\sqrt2X-h]:
             m\leq N_d(Y),\ n\leq N_d(Y+h)\}.                 \tag{13}
\]
The function U_d(Y)=Y/(2*pi)+Y^2/(32d) is strictly increasing
for Y>0, since U_d'(Y)=1/(2*pi)+Y/(16d)>0.
For an integer k, k<=N_d(Y) is exactly k^2<=U_d(Y).
If r_k is the unique positive solution U_d(r_k)=k^2, (13) is
therefore the interval
[max(X,r_m,r_n-h),sqrt2X-h], if nonempty.
This includes both true entry times, without equating them.
Values at its endpoints have no effect on the integral; the identities
themselves also hold there with the stated floor convention.

On any such interval write A_{mn}(Y)=a_m(Y)a_n(Y+h). From (12),
\[
 \sup |A_{mn}|\leq\frac{C}{\sqrt{mn}},\qquad
 \int_{I_{mn}}|A_{mn}'(Y)|\,dY\leq\frac{C}{\sqrt{mn}}.        \tag{14}
\]
If a phase has its unweighted integral bounded by K on every
subinterval, integration by parts against its primitive gives a
weighted bound K(sup|A|+integral|A'|). We use this only with the
smooth functions (8) on the individual interval (13).
There is no differentiation of a floor or an unaccounted jump.

### Both channels of the real product

The finite cosine identity gives exactly
\[
 \int_X^{\sqrt2X-h} V(Y)V(Y+h)\,dY
 =2\sum_{m,n\leq M}\int_{I_{mn}} A_{mn}(Y)
  \{\cos(f_m(Y)-f_n(Y+h))+\cos(f_m(Y)+f_n(Y+h))\}\,dY.
                                                               \tag{15}
\]
An empty interval contributes zero.

For the sum phase F_+=f_m(Y)+f_n(Y+h), (11)--(12), d comparable
to X^2q^2, and Y,Y+h<=sqrt2X imply, beyond one onset,
\[
 F_+''(Y)\geq\frac{1}{4X}.                                    \tag{16}
\]
The cited second-derivative estimate on every subinterval of I_{mn},
followed by (14), bounds its weighted integral by
C sqrt X/sqrt(mn). Summing over all pairs costs
\[
 C\sqrt X\left(\sum_{n\leq M}n^{-1/2}\right)^2
       \leq C\sqrt X\,M=O(X).                               \tag{17}
\]
This includes equal indices, unequal indices and all near-stationary
cutoff endpoints. No first-derivative separation is needed here.

For the difference phase F_-=f_m(Y)-f_n(Y+h) with m!=n, put
eta=log(n/m). Subtracting the explicit derivatives at the same Y
and then integrating f_n'' over the shift gives exactly
\[
 F_-'(Y)=(1+c_0Y/d)\eta-\int_Y^{Y+h}f_n''(r)\,dr.             \tag{18}
\]
Here |eta|>=1/M, since for n>m, log(n/m)>= (n-m)/n>=1/M,
and likewise after swapping m,n. The integral in (18) is O(h/X).
Since hM/X tends to zero, |F_-'|>=|eta|/2 uniformly.
Differentiating (18), using (12), gives
\[
 |F_-''(Y)|\leq C|\eta|/d+Ch/X^2,\qquad
 \int_{I_{mn}}|F_-''|\leq CX|\eta|/d+Ch/X.                    \tag{19}
\]
Elementary integration by parts of A*exp(iF_-) against 1/(iF_-')
is valid by this nonvanishing derivative. Its endpoint, A' and F_-''
terms, bounded with (14), (18), (19), give
\[
 \left|\int_{I_{mn}}A_{mn}e^{iF_-}\,dY\right|
 \leq\frac C{\sqrt{mn}}\left\{
   \frac1{|\eta|}+\frac{X}{d|\eta|}
                    +\frac{h}{X|\eta|^2}\right\}
 \leq\frac C{\sqrt{mn}|\log(n/m)|}.                           \tag{20}
\]
The last inequality uses X/d=o(1) and
h/(X|eta|)<=hM/X=o(1). Thus monotonicity of F_-' is not assumed.
The cited sum estimate A.3 now bounds all unequal-index difference
terms in (15) by
\[
 O(M\log M)=O(\sqrt X\log X).                                \tag{21}
\]
This supplies every non-diagonal term; (17) also supplies the
entire other channel.

### The diagonal with its moving cutoff

Because N_d is nondecreasing, the surviving equal-index difference
terms at a given Y have precisely 1<=n<=N_d(Y).
Equations (11)--(12) and integration over [Y,Y+h] show, uniformly,
\[
 a_n(Y+h)=a_n(Y)(1+O(h/X)),\qquad
 f_n(Y+h)-f_n(Y)=h v_n(Y)+O(h/X).                             \tag{22}
\]
For the phase estimate, f_n'-v_n=O(tq/X)=O(1/(Xq))
and f_n''=O(1/X), so the Taylor error O(h^2/X) and the
additional h*O(1/(Xq)) are both covered in (22).
The cosine is Lipschitz with constant 1. Since sum_{n<=M}1/n=O(q),
the integrated error from (22) is O(hq)=O(1).
Combining (10), (15), (17), (21) and (22) therefore gives
\[
 \int_X^{\sqrt2X-h}S_d(Y)S_d(Y+h)\,dY
 =2\int_X^{\sqrt2X-h}\sum_{n\leq N_d(Y)}\frac1n
      \exp\left\{\frac t2
           \left(v_n(Y)^2-\frac{\pi^2}{16}\right)\right\}
          \cos(hv_n(Y))\,dY+O(X).                            \tag{23}
\]
Here sqrt X*log X=O(X) at a common sufficiently large onset.

For completeness, the sum-to-integral error in (23) is uniform
even where its floor changes. At fixed Y put
\[
 g_Y(u)=\exp\left\{\frac t2
       ((\ell/2-u)^2-\pi^2/16)\right\}\cos(h(\ell/2-u)).
\]
On 0<=u<=log N_d(Y), and on the short extension to ell/2,
|g_Y|<=C and |g_Y'|<=C(tq+h)<=C/q.
Hence x^{-1}g_Y(log x) has derivative bounded by C/x^2.
Comparison on the unit intervals, with the final endpoint term,
proves
\[
 \sum_{n\leq N_d(Y)}\frac{g_Y(\log n)}n
      =\int_1^{N_d(Y)}\frac{g_Y(\log x)}x\,dx+O(1).
\]
The actual formula for N_d gives
N_d(Y)=sqrt(Y/(2*pi))+O(1), so
log N_d(Y)=ell/2+O(X^{-1/2}); replacing only this upper
integral endpoint by ell/2 costs O(X^{-1/2}). Thus (23) is
\[
 2\int_X^{\sqrt2X-h} e^{-\pi^2t/32}
          \int_0^{\ell/2} e^{t v^2/2}\cos(hv)\,dv\,dY+O(X).
                                                               \tag{24}
\]
The inner integral has absolute value at most Cq. Extending the
outer integral in (24) by its missing length h costs O(hq)=O(1).
This is a paid endpoint extension of the diagonal expression only.

### Full limiting coefficient, error scale and sign

In (24) put Y=lambda X and v=qz. From (4),
\[
 t(\lambda X)=\frac{\pi^2\lambda^2}{(L-1)^2},\qquad
 \frac{t(\lambda X)q^2}{2}
       =\frac{\pi^2\lambda^2q^2}{2(L-1)^2}
       =\frac{\pi^2\lambda^2}{8}
                    +O\left(\frac{\log q}{q}\right).
                                                               \tag{25}
\]
The last error is uniform for 1<=lambda<=sqrt2: (4) implies
q/(L-1)=1/2+O(log L/L), with L comparable to q.
Also ell/(2q)=1/2+O(1/q), hq=3*pi exactly, and
exp(-pi^2t/32)=1+O(q^{-2}).
All arguments of the remaining exponential stay in a fixed compact
real interval. The mean value theorem, the O(1/q) change in the
inner integration endpoint and (25) consequently show that (24)
equals
\[
 2Xq\int_1^{\sqrt2}\int_0^{1/2}
       e^{\pi^2\lambda^2z^2/8}\cos(3\pi z)\,dz\,d\lambda
            +O(X\log q).                                    \tag{26}
\]
This proves the full asymptotic in (2); the other channel has already
been paid in (17), so (26) is not a lone-diagonal conjecture.

For fixed lambda let w(z)=exp(pi^2 lambda^2 z^2/8).
It is increasing on [0,1/2]. The cosine is nonnegative on
[0,1/6] and nonpositive on [1/6,1/2]. Therefore
\[
 \int_0^{1/2}w(z)\cos(3\pi z)\,dz
 \leq w(1/6)\int_0^{1/2}\cos(3\pi z)\,dz
 =-\frac{w(1/6)}{3\pi}\leq-\frac1{3\pi}.                     \tag{27}
\]
Integrating in lambda proves the coefficient bound in (2).
Finally
X log q/(Bq)=log q/((sqrt2-1)q) tends to zero.
Choose one onset making the absolute error in (2) at most
Bq/(3*pi), together with all earlier uniform thresholds.
Then (3) follows. No numerical test or effective value of the
onset is required or asserted.

### Qualifications and downstream gap

Every sum is finite and every interchange in (15) is finite. Both
true floors were retained in (13); their one-term entries were never
differentiated. The gamma phase and modulus were paid in (7)--(10),
and no possible xi or zeta zero was a denominator. Both real-product
channels, both index cases and all band endpoints are covered.
No RH-equivalent positivity or heat real-zero theorem was assumed.

A negative integral can supply opposite-sign reference pairs, but this
proof supplies no uniform pointwise margin or quantitative distribution
of such pairs. In particular it does not pay the actual-Jensen errors
from C019j and C019k at ordered disjoint samples, prove c*sqrt(d)
additional roots, or separate such roots from existing bulk counts.
Those tasks, every-degree hyperbolicity and L030-L032/C032a's positivity
remain open. Stops1345/1355/559 and the parked direct (A) route are
unaffected.

### Independent conceptual audit1381 — 17 November 2026

The audit retains (1)--(3), with no change to their constants, error
order or hypotheses. It checks the defined finite sum, using C019k's
exact (1)--(2); neither its approximation theorem nor a Jensen sign
transfer is a new premise of the correlation calculation. The sole
direct notebook input remains C019k. DLMF 5.11.3--5.11.4 and Kösters
v2 A.2--A.3 are the precise standard inputs cited above; their source
coverage is reused. The following checks supply the complete acceptance
test, including the cases at which a diagonal-only argument would fail.

**Normalization and uniformity.** Combining G_t/G_0, n^{-(s_*-s)} and
exp(t*log(n)^2/4) gives exp(t*(alpha-log n)^2/4), so the factor 2
in (6) is exact. For z=1/4-iY/2, write theta=arg(z). Then
Im((z-1/2)Log(z)-z)=-theta/4-(Y/2)log|z|+Y/2.
Here theta=-pi/2+O(1/Y) and
log|z|=log(Y/2)+O(1/Y^2). Including pi^{-s/2} gives
-vartheta(Y)+O(1/Y); the negative real s(s-1) contributes the
minus sign. Fixed-sector Stirling controls the ratio to the exact
gamma modulus by 1+O(1/Y). Thus the leading imaginary heat exponent is
-pi*t*v_n/8, and taking the real part gives exactly the phase sign
in (8), together with S_d=-V+error. This uses no derivative of a
Stirling remainder. The exact identities (4) imply
d/X^2=(L-1)^2/(2*pi^2) and q/(L-1)->1/2. All weights remain
bounded multiples of n^{-1/2}, including before entry for n<=M.
The pointwise error is O(X^{-1}*sqrt(M))=O(X^{-3/4}); multiplying
by the O(X^{1/4}) bounds and integrating over length O(X) pays
O(sqrt(X)) in (10), including the product of the two errors.

**Derivatives, entries and both product channels.** Differentiating
with t'=2t/Y and v_n'=1/(2Y) gives every identity in (11), in
particular f_n'''=-1/(2Y^2)+c_0/(2dY). The amplitude logarithmic
derivative is O(1/X), so its shift and every pair's total variation
are uniform. The strictly increasing U_d maps the two index conditions
to r_m<=Y and r_n-h<=Y. Thus I_{mn} is one actual closed interval,
with exactly the endpoints in (13); no phase estimate differentiates a
floor jump. Empty intervals, single-point intervals and floor equalities
cause no integral contribution omitted by the finite expansion.

For the sum phase, the two main second derivatives have sum at least
1/(sqrt(2)*X), while their total perturbation is O(q/d)=o(1/X).
This proves (16) simultaneously for every pair and every subinterval.
Kösters A.2 applies to these real smooth phases, including diagonal
indices and stationary first derivatives at entry. Partial integration
with (14) and sum n^{-1/2}<=2*sqrt(M) gives total O(X), exactly
as in (17).

For the difference phase at unequal indices, put eta=log(n/m).
The same-point derivative difference is (1+c_0*Y/d)*eta, and the
shift contributes -integral_Y^{Y+h} f_n''. Since |eta|>=1/M and
h*M/X->0, its modulus is at least |eta|/2. This works for n>m
and n<m on their different intervals. Differentiating the shift by
integrating f_n''' gives (19). The integrated-by-parts expression
has endpoint and amplitude-derivative costs O(1/(sqrt(m*n)*|eta|));
the remaining cost is at most
C/(sqrt(m*n))*(X/(d*|eta|)+h/(X*|eta|^2)).
Their ratios to the first cost are X/d and h/(X*|eta|), both
bounded and tending to zero uniformly. No monotonicity of F_-' is
needed. A.3 bounds each unordered sum by O(M*log M); both orders
only change its constant. This verifies (20)--(21) with all endpoints.

**Diagonal and floor replacement.** Monotonicity of N_d leaves
exactly n<=N_d(Y) on the equal-index difference channel. The shift
of log(a_n) is O(h/X). The phase increment differs from h*v_n
by O(h/(X*q)+h^2/X), which is covered by (22). After the harmonic
sum and integration, the total replacement cost is O(h*q)=O(1).
For the sum-to-integral passage, the derivative of
x^{-1}g_Y(log x) is (g_Y'(log x)-g_Y(log x))/x^2. Its absolute
integral on [1,N_d(Y)] is at most C*integral_1^infinity x^{-2}dx=C.
Comparing consecutive unit intervals and retaining
the final value at N_d proves the stated O(1) error uniformly.
Since t/16=O(q^{-2}), the difference between
sqrt(Y/(2*pi)+t/16) and sqrt(Y/(2*pi)) is O(q^{-2}/sqrt(X));
rounding adds at most 1. Hence the logarithmic endpoint error is
O(X^{-1/2}) even at every floor equality. The associated integrated
cost is O(sqrt(X)), inside (24)'s O(X). Extending only the resulting
diagonal integral across the final length h costs O(h*q)=O(1).

**Coefficient and common onset.** Substitution Y=lambda*X, v=q*z
has Jacobian X*q. The exact heat coefficient is
pi^2*lambda^2*q^2/(2*(L-1)^2), converging to pi^2*lambda^2/8
with uniform error O(log(q)/q). The varying upper endpoint differs
from 1/2 by O(1/q), and the outside exponential differs from 1
by O(q^{-2}). Bounded integrands and their coefficient derivatives
therefore give total O(X*log q), with no limiting interchange on
an unbounded domain. The factor 2 in (15) survives, yielding (1).
On [0,1/6] the nonnegative cosine is multiplied by w(z)<=w(1/6);
on [1/6,1/2] the nonpositive cosine is multiplied by w(z)>=w(1/6).
Both inequalities have the same direction after multiplication.
Their sum is at most -w(1/6)/(3*pi), establishing (27) and
K<=-2/(3*pi).

All non-leading costs are O(sqrt(X)), O(X),
O(sqrt(X)*log X), O(1), and O(X*log q), each already accounted
for above. Their combined ratio to B*q tends to zero. In particular
the absolute constant C in (2) satisfies
C*X*log q <= B*q/(3*pi) eventually. Every earlier threshold is
a consequence of X,q tending to infinity and the uniform scale
identities; their finite maximum supplies one integer onset. The
audit establishes no effective value of that onset.

This is a reproduction and verification of the existing local proof,
not a stronger bound or a theorem newly imported from the sources.
No defect was found. Actual-Jensen transfer still requires a separate
error argument: the uniform approximations alone have not been inserted
into this correlation. No ordered samples, root count, bulk separation,
all-degree positivity or RH conclusion is added by this audit.

## Mathlib

Full matching coverage for (2)--(3) is not checked. No formalization
of this moving-heat correlation or the imported source estimates is
asserted. Standard finite-sum identities, differentiation or integral
estimates, if available, would be supporting results only. The precise
analytic inputs used here are the named DLMF and Titchmarsh/Koesters
statements above, not a claim based on a Mathlib homepage.
