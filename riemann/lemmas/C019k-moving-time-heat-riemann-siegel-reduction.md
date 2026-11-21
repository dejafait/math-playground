# C019k — Uniform moving-time heat reduction to a real finite sum

## Hypotheses

Use C019j's actual xi, positive gamma modulus m(Y), and Polymath heat
family H_t with H_0(z)=xi(1/2+iz/2)/8. Let d tend to infinity through
positive integers, and let T>2 pi e be the unique solution of
\[
 d=\frac{T}{2\pi}\left(\log\frac{T}{2\pi}-1\right).
\]
Set
\[
 Y_-=\frac{T}{\sqrt{2d}},\quad Y_+=\frac{T}{\sqrt d},\quad
 t=t_d(Y)=\frac{Y^2}{2d},\qquad Y\in[Y_-,Y_+].
\]
For specificity, with s=1/2-iY,
\[
 m(Y)=\left|\frac{s(s-1)}2\pi^{-s/2}\Gamma(s/2)\right|>0.
\]
This agrees with C019j's upper-half-plane definition by conjugation.
Use exactly the source functions in D.H.J. Polymath,
*Effective approximation of heat flow evolution of the Riemann xi
function, and a new upper bound for the de Bruijn–Newman constant*,
[arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2),
4 August 2019, (6), (9), (10):
\[
 \begin{split}
 G_0(s)&=\frac18\frac{s(s-1)}2\pi^{-s/2}\sqrt{2\pi}
       \exp\left((s/2-1/2)\operatorname{Log}(s/2)-s/2\right),\\
 \alpha(s)&=\frac1{2s}+\frac1{s-1}
                         +\frac12\operatorname{Log}(s/(2\pi)),\\
 G_t(s)&=\exp\left(\frac t4\alpha(s)^2\right)G_0(s).
 \end{split}                                                    \tag{1}
\]
G_t denotes the source's M_t, not an arithmetic mollifier. Log is
principal and powers of positive real numbers use their real logarithm.
All arguments of G_t and alpha below lie off the source cut (-infinity,1].
Define
\[
 s_*=s+\frac t2\alpha(s),\quad
 N=N_d(Y)=\left\lfloor\sqrt{\frac{Y}{2\pi}+\frac t{16}}\right\rfloor,
\]
\[
 Z_d(Y)=\sum_{n=1}^{N}\exp\left(\frac t4\log^2 n\right)n^{-s_*},
 \qquad S_d(Y)=\frac{16}{m(Y)}\operatorname{Re}\{G_t(s)Z_d(Y)\}.
                                                               \tag{2}
\]
This N is only the source cutoff, not C019j's positive scale N_d(q).
There is no RH, nonvanishing, simple-zero or heat real-zero assumption.

## Conclusion

There exist absolute C,d_0>0 such that for every integer d>=d_0,
\[
 \sup_{Y_-\leq Y\leq Y_+}
 \left|\frac{8H_{t_d(Y)}(2Y)}{m(Y)}-S_d(Y)\right|
                  \leq C Y_-^{-1/4}.                         \tag{3}
\]
The closed band includes every cutoff threshold. Constants and onset
are existential. This is a specialization of a known effective source
theorem; no claim of an advance beyond the checked literature is made.
It establishes neither a signed margin nor any Jensen root count.

## Proof

### Uniform source domain and bounded heat weights

Put L=log(T/(2 pi)) and b=T^2/(dY^2). Then 1<=b<=2 and, exactly,
\[
 d=e^L(L-1),\quad T=\frac{2\pi d}{L-1},\quad
 Y=\frac{2\pi\sqrt d}{\sqrt b(L-1)},\quad
 t=\frac{2\pi^2}{b(L-1)^2}.                                  \tag{4}
\]
These are C019j's scale identities. Since log d=L+log(L-1),
L tends to infinity, Y_- tends to infinity, and, uniformly in b,
\[
 \log Y=\tfrac12\log d-\log(L-1)+\log(2\pi)-\tfrac12\log b.
\]
Consequently there is one absolute K such that, for all sufficiently
large d and every Y in the closed band,
\[
 0<t\leq\tfrac12,\quad 2Y\geq200,\quad
 t(1+\log Y)^2\leq K.                                      \tag{5}
\]
For example the last conclusion follows because log Y=O(L) uniformly
in 1<=b<=2 while t<=2 pi^2/(L-1)^2. In particular it does not treat
t as fixed when d changes. Conditions (5) put x=2Y,y=0 in the full
domain (5) of Polymath Theorem1.3, including arbitrarily small t>0.

Write U=Y/(2 pi) and ell=log U. Enlarge the common onset so U>=4
and ell>=1. Since t/16<=1/32, the actual floor in (2) satisfies
\[
 \tfrac12\sqrt U\leq N\leq2\sqrt U.                         \tag{6}
\]
Indeed N>=sqrt(U)-1 and N<=sqrt(U+1/32). Thus
0<=log n<=log N<=ell/2+log2 for 1<=n<=N. Formula (1),
|s|=|s-1|>=Y and |arg s|<pi/2 give
\[
 |\alpha(s)|\leq C(1+\log Y).                              \tag{7}
\]
Here |Log(s/(2 pi))|<=|log(|s|/(2 pi))|+pi/2 and
Y<=|s|<=Y+1 for Y>=1. All constants are absolute.
Using (5)--(7), define the nonnegative source weights
\[
 w_n=\exp(t\log^2 n/4)n^{-\operatorname{Re}s_*}.
\]
Since Re s_*=1/2+(t/2)Re alpha(s),
\[
 w_n\leq n^{-1/2}
   \exp\{t\log^2 n/4+(t/2)|\alpha(s)|\log n\}
      \leq Cn^{-1/2}.                                      \tag{8}
\]
The same constant works at every cutoff value. No cancellation or
lower bound for the sum is used in (8).

### Exact real-part identity and the gamma-only conversion

Import Polymath Theorem1.3/(13)--(24), equivalently
Corollary6.5 and (70)--(74), with its errors e_A,e_B,e_C,0.
The latter include the full uncorrected Riemann–Siegel remainder.
Its arithmetic error estimates are cited, not reproved here.
At x=2Y,y=0, its B_t(2Y)=G_t(s). Its gamma multiplier and kappa
(which are unrelated to Euler's gamma function) become, exactly,
\[
 \gamma=\frac{G_t(\overline s)}{G_t(s)},\qquad \kappa=0.
\]
Principal Log commutes with conjugation at these nonreal arguments.
Thus G_t(conj s)=conj G_t(s), alpha(conj s)=conj alpha(s),
|gamma|=1, and the two sums in its (14) are Z_d and conj Z_d.
Multiplication by B_t therefore gives
\[
 B_t(2Y)f_t(2Y)=G_t(s)Z_d(Y)
                       +\overline{G_t(s)Z_d(Y)}
                 =2\operatorname{Re}\{G_t(s)Z_d(Y)\}.       \tag{9}
\]
After multiplying its error inequality by 8|B_t|/m, (9) yields
\[
 \left|\frac{8H_t(2Y)}{m(Y)}-S_d(Y)\right|
   \leq Q(Y)(e_A+e_B+e_{C,0}),\quad
 Q(Y)=\frac{8|G_t(s)|}{m(Y)}.                               \tag{10}
\]
This proves the factor16 in (2), with no division by xi or zeta.
G_t(s) is nonzero directly from (1), so the source's normalization
does not impose nonvanishing of H_t either.

To bound Q import Stirling's formula in a fixed sector away from the
negative real axis, [DLMF5.11.3](https://dlmf.nist.gov/5.11.E3),
with g_0=1 in [5.11.4](https://dlmf.nist.gov/5.11.E4).
This is the same standard gamma input used in C019j, not a new
asymptotic theorem. For z=s/2, Re z=1/4 and |arg z|<pi/2,
so its sector hypothesis holds with delta=pi/2 and |z|~Y/2.
It gives, with the same principal powers,
\[
 \Gamma(s/2)=\sqrt{2\pi}
 \exp\{(s/2-1/2)\operatorname{Log}(s/2)-s/2\}
                    (1+O(Y^{-1})).                         \tag{11}
\]
Choose one fixed gamma threshold so that the last factor has modulus
at least 1/2. The polynomial and pi factors in m and 8G_0 cancel
in their modulus ratio. Equations (1), (5), (7), (11) imply
\[
 Q(Y)=\frac{\exp\{(t/4)\operatorname{Re}(\alpha(s)^2)\}}
                 {|1+O(Y^{-1})|}
       \leq2\exp\{t|\alpha(s)|^2/4\}\leq C.                \tag{12}
\]
This ratio is bounded uniformly despite the exponential smallness
of m itself. Only nonzero gamma and explicit factors are divided out.

### All three source errors

At y=0, |gamma|=1 and kappa=0, source (23) reads
\[
 e_A+e_B\leq2\sum_{n=1}^{N} w_n(e^{r_n}-1),\quad
 r_n=\frac{(t^2/16)\log^2(U/n^2)+0.626}{2Y-6.66}.           \tag{13}
\]
From (6), |log(U/n^2)|<=ell+2log N<=2ell+2log2.
Thus by (5),
\[
 t^2\log^2(U/n^2)\leq C t^2(1+\log Y)^2
                         \leq CKt\leq CK/2.
\]
In particular 0<=r_n<=C/Y, uniformly in n,Y,d. At one larger
onset these numbers are at most1, so e^{r_n}-1<=e r_n<=C/Y.
The elementary bound sum_{n=1}^N n^{-1/2}<=2 sqrt N, together
with (6), (8), proves
\[
 e_A+e_B\leq\frac C Y\sqrt N\leq C Y^{-3/4}.              \tag{14}
\]

Source (24), still retaining the uncorrected remainder, becomes
\[
 e_{C,0}\leq U^{-1/4}
 \exp\left\{-\frac t{16}\ell^2
       +\frac{2.48}{N-0.125}
       +\frac{3|\ell+i\pi/2|+10.44}{2Y-12}\right\}.         \tag{15}
\]
The negative exponent may be dropped for an upper bound. By (6),
the other two terms in the exponent are O(Y^{-1/2}) and
O((1+log Y)/Y), respectively. Their denominators are positive
at our common onset, and these terms tend to zero uniformly on
the band. Hence
\[
 e_{C,0}\leq C Y^{-1/4}.                                  \tag{16}
\]
No error has been omitted: (14) covers both finite-sum source errors
and (16) covers the entire remainder used in Theorem1.3.
Combining (10), (12), (14), (16) proves pointwise
\[
 \left|8H_t(2Y)/m(Y)-S_d(Y)\right|
          \leq C(Y^{-3/4}+Y^{-1/4})\leq C Y^{-1/4}.          \tag{17}
\]
Taking the supremum and using Y>=Y_- gives (3).

### Integer cutoffs, simultaneous onset and limitations

Nothing above freezes N or differentiates the finite sum. The source
theorem is pointwise for every x,y,t in its domain. Its underlying
(49)--(51) use a_src=sqrt(T'/(2 pi)), N=floor(a_src),
p=1-2(a_src-N), with T'=Y+pi t/8 from (68).
These give precisely (2), including equality a_src=k. At equality
N=k and p=1; approaching from below gives p tending to -1.
The source's Proposition6.2/(58) bounds C_0 throughout [-1,1],
and Corollaries6.4--6.5 impose no exclusion of integral a_src.
Thus (13)--(17) also hold at equality, including band endpoints.

As a direct consistency check, U+t/16 is strictly increasing in Y:
its derivative is 1/(2 pi)+Y/(16d)>0. At a threshold k, only the
k-th term is newly included. Equations (8), (12) bound the resulting
one-sided jump of S_d in absolute value by
\[
 (16|G_t(s)|/m(Y))w_k\leq Ck^{-1/2}\leq C Y^{-1/4},
\]
because k^2=U+t/16. This checks the natural jump scale; continuity
of S_d is neither true nor needed for the uniform approximation.

There are only finitely many fixed thresholds used: source domain
(5), U>=4, ell>=1, the gamma threshold in (11), positivity of
the printed denominators, and C/Y<=1 in (13). The uniform limits
in (4)--(5) let a single integer d_0 enforce all of them for every
Y in the closed band. There is no Y-dependent choice of onset.

This proof only specializes the named effective theorem and
Stirling's formula. It does not use the source's fixed-positive-time
asymptotics or real-zero theorem. It gives an explicit reference for
later arithmetic estimates, with its exact moving coefficients and
cutoff; it gives no signed/absolute moment deficit, robust ordered
samples, c*sqrt(d) root count, bulk separation, all-degree
hyperbolicity or RH resolution. Those independent gaps remain open.

### Independent specialization audit1376 — 17 November 2026

The audit retains (3), with no correction to (1)--(17). It checks the
actual moving time, rather than importing the source's fixed-time
limit (12). In the source's Theorem1.3, (5) permits y=0 and every
0<t<=1/2. Substituting x=2Y into (6), (9)--(11), (14)--(19),
(23)--(24) gives exactly the functions and errors used above.
In particular (16) is the quotient of conjugate G_t values, and
(18) is zero. Thus the factor16 is exact, and no xi value is a
denominator. Corollary6.5/(70), (74), not the corrected remainder
e_C alone, is the imported approximation.

For an explicit check of the scale estimate, (4) also gives
log Y=L/2-(log(L-1))/2+log(2 pi)-(log b)/2. For L>=4 this is
at most L. Once Y_->=e, it follows that
t(1+log Y)^2<=2 pi^2(L+1)^2/(L-1)^2<=50 pi^2/9.
Consequently (7)--(8) and t|alpha(s)|^2=O(1) hold with one
absolute constant. DLMF5.11.3--5.11.4 applies to s/2 in the
fixed closed sector |arg z|<=pi/2; its relative error is O(1/Y).
Thus |Gamma^*(s/2)|>=1/2 beyond one fixed threshold, proving
(12) uniformly.

Source (23) has precisely the numerator and denominator in (13).
The uniform scale bound gives r_n=O(1/Y), and summing (8) gives
O(sqrt N); hence both sum errors together are O(Y^(-3/4)).
Source (24) has precisely (15), including its leading U^(-1/4)
and the full uncorrected remainder. Its two positive exponent
terms are O(Y^(-1/2)) and O((1+log Y)/Y), proving (16).
These estimates hold for every floor value, without differentiating N.
At a_src=k, Proposition6.2/(49)--(51) gives N=k,p=1;
(58) includes this endpoint. All threshold conditions are fixed
lower bounds on Y or L, or consequences of the displayed uniform
limits. Since Y_->infinity and L->infinity with d, their finite
maximum gives one d_0. No effective d_0 has been certified.

This verifies the local specialization of the cited theorem, without
strengthening its error, producing signs, or resolving any root deficit.

## Mathlib

Full matching coverage for this coupled-scale specialization is not
checked. No Mathlib theorem identifier for (3) or the imported
Polymath effective theorem is asserted. The
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/)
is a lookup location only; supporting gamma or finite-sum facts would
not amount to a formalization of this result.
