# Corollary 028n: an entire reciprocal does not force boundary PF to propagate

## Hypotheses

Fix, independently of every order parameter,
\[
 P(z)=\frac{(1+z)((z+2)^2+1)}5
     =1+\frac95z+z^2+\frac15z^3,
 \qquad F(z)=P(z)\sum_{j=0}^\infty\frac{z^j}{(2j)!}.
\]
Write the last series as \(\cosh\sqrt z\); it is entire and does
not require a square-root branch at zero. For a smooth real function,
put \(d_k=k(k-1)/2\) and
\[
 D_k(f;x)=(-1)^{d_k}\det[f^{(i+j)}(x)]_{i,j=0}^{k-1}.
\]
Global PF means nonnegativity of all ordered translation minors of
all finite sizes on the whole real line.

Use these assessed external inputs at exactly the stated scopes:

* NIST DLMF, [4.28.2](https://dlmf.nist.gov/4.28#E2),
  [4.33.2](https://dlmf.nist.gov/4.33#E2),
  [4.36.2](https://dlmf.nist.gov/4.36#E2): the exponential identity,
  series and product for cosh.
* A. Belton, D. Guillot, A. Khare and M. Putinar,
  *Hirschman-Widder densities*,
  [arXiv:2101.02129v2, 9 April 2022](https://arxiv.org/pdf/2101.02129v2),
  Definition 1.1 and Theorem 1.2, pp.1–2: a product
  \(C e^{\delta s}\prod_j(1+\alpha_j s)\), with
  \(C>0,\delta\ge0,\alpha_j\ge0,0<\sum_j\alpha_j<\infty\),
  is the reciprocal transform of a one-sided PF function; the
  function is positive beyond \(\delta\) and smooth when infinitely
  many \(\alpha_j\) are nonzero. Conversely a one-sided PF function
  has a reciprocal of this form, in particular with only real zeros.
* T. Simon, *Positive stable densities and the bell-shape*,
  [arXiv:1302.0956v1, 5 February 2013](https://arxiv.org/pdf/1302.0956v1),
  Section 3.2, pp.9–10: a positive law with Laplace transform
  \(\exp[-\gamma_0s-\int_0^\infty(1-e^{-st})k(t)dt/t]\),
  where \(\gamma_0\ge0\), \(k\) is nonnegative and nonincreasing
  and the defining integral is finite, is self-decomposable.
* S. Sra, *On some positivity properties of the Riemann Xi function*,
  [arXiv:2611.02944v1, 2 November 2026, primary manuscript mirror](https://arxiv.cnoctave.top/pdf/2611.02944),
  Lemma C.1 p.20 and Lemma C.16, first assertion (C.47), pp.37–38:
  if \(f\in C^{2m-2}(I)\), \(I=(a,b)\), and
  \(D_j(f;t)>0\) for \(t\in I,1\le j\le m\), then ordered
  translation minors of size \(k\le m\) are positive whenever
  \(a<x_1-y_k\) and \(x_k-y_1<b\).

Sra's Lemma C.17, pp.38–39, motivates the finite three-factor
inverse, and Proposition C.25, pp.44–45, supplies the reviewed
saddle/determinant method. Neither asserts the present combined
fixed-law conclusion. We specialize the finite inverse explicitly
to identify and normalize this same law, and prove the changed cosh
Fourier estimates below; we do not reprove the general PF or
self-decomposability theorems. C028m supplies its proof's general
Gaussian determinant and tilt/scale identities, not its half-stable
law or its negative minor. Assessment1689 and source-notes1689
record the primary-source and duplicate/failure comparison.

## Conclusion

There is one probability density \(p\), positive on \((0,\infty)\),
zero on \(( -\infty,0]\), with a \(C^\infty\) zero extension and
a self-decomposable law, such that
\[
 \int_0^\infty e^{-sx}p(x)\,dx=\frac1{F(s)}\quad(s\ge0).       \tag{1}
\]
The function \(F\) satisfies \(F(0)=1\), has exact entire order
\(1/2\), and every ordinary Taylor coefficient is strictly positive.
For every integer \(m\ge1\), there is \(\epsilon_m>0\) such that
\[
 \det[p(x_i-y_j)]_{i,j=1}^k>0
 \quad(1\le k\le m),                                      \tag{2}
\]
for all strictly increasing real tuples \(x,y\) whose every cross
difference belongs to \((0,\epsilon_m)\). Nevertheless \(p\) is
not globally PF.

This is a countermodel to the generic implication with precisely
these premises; separate conceptual audit1693 below validates that
scope relative to the cited external inputs. It is an
established-method specialization, not a certified novelty claim.
It supplies no order-uniform interval, specified size of a negative
minor, global log-concavity assertion, actual-Xi realization, or
actual-Xi conclusion \(S_F=0\). RH remains unresolved.

## Proof

### 1. Entire function and the same positive smooth law

The cited product gives
\[
 \cosh\sqrt z=\prod_{n=0}^\infty(1+z/\lambda_n),
 \qquad\lambda_n=\pi^2(n+1/2)^2.
\]
All \(\lambda_n\) are positive and \(0<\sum_n1/\lambda_n<\infty\),
by comparison with \(\sum_{n\ge1}n^{-2}\). The BGKP theorem with
\(C=1,\delta=0,\alpha_n=1/\lambda_n\) therefore provides a
one-sided PF function \(b\), positive for every \(x>0\), with a
smooth zero extension, and transform \(1/\cosh\sqrt s\).
Its integral is one: monotone convergence as \(s\downarrow0\)
identifies it with the limiting transform value one. The infinite
number of nonzero parameters pays the theorem's smoothness condition.

The finite inverse, extended by zero for \(t\le0\), is
\[
 h(t)=\frac52\{e^{-t}-e^{-2t}(\cos t+\sin t)\}\quad(t>0).
\]
For \(t>0\), \(\cos t+\sin t\le1+t<e^t\), so \(h(t)>0\).
It is integrable, and elementary absolutely convergent Laplace
integrals give, for \(s\ge0\),
\[
 \int_0^\infty e^{-st}h(t)dt
 =\frac52\left\{\frac1{s+1}-\frac{s+3}{(s+2)^2+1}\right\}
 =\frac5{(s+1)((s+2)^2+1)}=\frac1{P(s)}.                 \tag{3}
\]
In particular \(\int h=1\). Define \(p=b*h\). Tonelli's theorem
for nonnegative functions proves its mass one and (1), including
\(s=0\). For \(x>0\) the integrand \(b(x-t)h(t)\) is strictly
positive on \(0<t<x\), so \(p(x)>0\).

For any compact set of real \(x\)'s choose \(M>0\) above its upper
endpoint. For \(t>M\), every \(b^{(r)}(x-t)\) is zero. For
\(0\le t\le M\) these derivatives are bounded uniformly in that
compact set; \(h\) is integrable there. Differentiation under the
convolution is thus valid at every order, locally uniformly. This
proves the asserted smooth zero extension, including flatness at
zero, rather than merely identifying an almost-everywhere density.

The constant term of \(F\) is one. Multiplication of its entire
series by the displayed positive-coefficient polynomial shows every
coefficient is positive: the contribution \(1/(2j)!\) alone is
strictly positive. For \(|z|\le r\), the series gives
\(|F(z)|\le P(r)\cosh\sqrt r\le C(1+r)^3e^{\sqrt r}\).
On the positive ray \(F(r)=P(r)\cosh\sqrt r\ge e^{\sqrt r}/2\).
These two bounds imply \(\log M_F(r)=\sqrt r+O(\log r)\) and
\(\limsup\log\log M_F(r)/\log r=1/2\). This pays exact order,
not just an upper bound.

### 2. Spectral positivity, monotonicity and integrability

Define, for \(t>0\),
\[
 k(t)=\sum_{n=0}^\infty e^{-\lambda_nt}+k_b(t),
 \qquad k_b(t)=e^{-t}+2e^{-2t}\cos t.                    \tag{4}
\]
The subscript on \(k_b\) denotes the finite block, not the base
density \(b\). All base terms are decreasing and the series and its
derivative converge uniformly on \([\eta,\infty)\) for every
\(\eta>0\), by the quadratic growth of \(\lambda_n\).

The finite block is itself strictly decreasing. Indeed
\[
 k_b'(t)=-e^{-t}-2e^{-2t}(2\cos t+\sin t).
\]
For \(0<t\le3/2<\pi/2\), the trigonometric terms are nonnegative.
For \(t\ge3/2\), Cauchy–Schwarz gives
\(|2\cos t+\sin t|\le\sqrt5\), whence
\[
 k_b'(t)\le-e^{-t}+2\sqrt5e^{-2t}<0.
\]
For the strict last inequality, the exponential series gives
\(e^3>\sum_{j=0}^8 3^j/j!=806769/40320>20\); thus
\(e^t\ge e^{3/2}>2\sqrt5\). Since \(k_b(t)\to0\) at infinity,
strict decrease also proves \(k_b(t)>0\). Consequently \(k\) is
nonnegative and nonincreasing.

The required Levy integrability is explicit. By Tonelli,
\[
 \int_0^1\sum_ne^{-\lambda_nt}dt\le\sum_n\lambda_n^{-1}<\infty,
 \qquad
 \int_1^\infty\sum_ne^{-\lambda_nt}\frac{dt}t
 \le\sum_n\frac{e^{-\lambda_n}}{\lambda_n}<\infty.
\]
The finite block is bounded at zero and absolutely bounded by
\(e^{-t}+2e^{-2t}\) at infinity, so
\(\int_0^\infty(1\wedge t)k(t)dt/t<\infty\).

For a complex \(a\) with \(\Re a>0\), the absolutely convergent
integral \(\int_0^\infty(1-e^{-st})e^{-at}dt/t\) equals
\(\log((a+s)/a)\), for real \(s\ge0\), with logarithm chosen
continuously from zero at \(s=0\). To check this Frullani
specialization, differentiate under the integral to obtain
\(1/(a+s)\) and use value zero at \(s=0\). The domination is
uniform on compact nonnegative \(s\)-intervals, both at zero and
infinity. Summing the conjugate cases \(a=2+i,2-i\) and the
real case \(a=1\) gives \(\log P(s)\). Summing the real cases
\(a=\lambda_n\) uses Tonelli and the convergent product, and gives
\(\log\cosh\sqrt s\). Therefore
\[
 \frac1{F(s)}=
 \exp\left[-\int_0^\infty(1-e^{-st})\frac{k(t)}t dt\right].   \tag{5}
\]
The preceding integrability also proves that this integral is finite
for every \(s\ge0\). Apply Simon's stated criterion with zero
drift. It applies to the same law already constructed in (1), and
establishes self-decomposability, not just infinite divisibility.

### 3. Tilt scales and pointwise characteristic-function limit

Put \(B(s)=\log F(s)\) for \(s>0\), and define
\[
 f_s(x)=e^{B(s)-sx}p(x),\quad x_s=B'(s),\quad
 \sigma_s^2=-B''(s),\quad
 g_s(z)=\sigma_s f_s(x_s+\sigma_s z).
\]
Differentiation of (1) identifies \(x_s\) as the tilted mean and
\(\sigma_s^2\) as its variance. For each derivative order and
fixed \(s>0\), the required domination follows from boundedness
of \(x^re^{-sx/2}\) on the positive half-line against the
probability measure \(p(x)dx\). The variance is strictly positive
because the tilted density is positive on the whole positive
half-line. Thus these definitions describe genuine normalized
density tilts and standardizations.

On \(|z-s|\le s/2\) at large positive \(s\), use the principal
square root and the logarithms of \(z+1,z+2+i,z+2-i\). Then
\[
 B(z)=\sqrt z+\log P(z)-\log2+R(z),\quad
 R(z)=\log(1+e^{-2\sqrt z}).                              \tag{6}
\]
These branches agree with real \(B\) at \(s\). Since
\(\Re\sqrt z\ge\sqrt{\Re z}\ge\sqrt{s/2}\), the last logarithm
is analytic there and bounded by \(C e^{-\sqrt{2s}}\).
Cauchy estimates on smaller disks, together with differentiation
of the first two terms, give
\[
 x_s=\frac1{2\sqrt s}+\frac3s+O(s^{-2}),\qquad
 \sigma_s^2=\frac1{4s^{3/2}}+\frac3{s^2}+O(s^{-3}),           \tag{7}
\]
and \(B'''(z)=O(s^{-5/2})\) uniformly on \(|z-s|\le s/4\).
The exponentially small errors and their Cauchy derivative bounds
are absorbed in the displayed powers. In particular, eventually
\[
 \tfrac14s^{-3/4}\le\sigma_s\le s^{-3/4}.                 \tag{8}
\]

The Laplace transform identity extends to \(\Re z>0\): the
integral is holomorphic by domination and agrees with \(1/F(z)\)
on the positive ray. The latter is holomorphic in this half-plane,
as the product and the finite factors have no zero there. Hence
the characteristic function of \(g_s\) is
\[
 \psi_s(u)=e^{-iu x_s/\sigma_s}\frac{F(s)}{F(s-iu/\sigma_s)}.
                                                                    \tag{9}
\]
For fixed real \(u\), set \(t=u/\sigma_s\). Then
\(|t|=O(s^{3/4})=o(s)\), so Taylor's theorem applied to (6) on
the vertical segment gives
\[
 B(s)-B(s-it)-itx_s
   =\tfrac12t^2B''(s)+O(|t|^3s^{-5/2})
   =-u^2/2+O_u(s^{-1/4}).                              \tag{10}
\]
Thus \(\psi_s(u)\to e^{-u^2/2}\). Pointwise convergence alone is
not used to infer any density derivative limit.

### 4. A bound at every frequency and every fixed derivative

For \(a=s+2>1\) and real \(t\),
\[
 |(s+2-it)^2+1|^2
  =(a^2+1)^2+2(a^2-1)t^2+t^4\ge(a^2+1)^2.
\]
Also \(|s+1-it|\ge s+1\), so \(|P(s)/P(s-it)|\le1\).
Let \(A=\Re\sqrt{s-it}\). Then \(A\ge\sqrt s\), and the
exponential identity for cosh implies
\(|\cosh\sqrt{s-it}|\ge\sinh A\). Consequently, for \(s\ge1\),
\[
 \left|\frac{F(s)}{F(s-it)}\right|
 \le C_0\exp[-(A-\sqrt s)],\qquad C_0=\frac2{1-e^{-2}}.     \tag{11}
\]
This lower bound on the denominator holds at every real \(t\),
including those with large imaginary part of the square root.

For \(v\ge0\) write
\[
 H(v)=\sqrt{\frac{\sqrt{1+v^2}+1}2},\qquad
 H(v)-1=\frac{v^2}{2(\sqrt{1+v^2}+1)(H(v)+1)}.
\]
If \(0\le v\le1\), both parenthesized factors are at most 3.
If \(v\ge1\), they are at most \(3v\) and \(3\sqrt v\),
respectively. Therefore, for every \(v\ge0\),
\[
 H(v)-1\ge\frac1{18}\min\{v^2,\sqrt v\}.                \tag{12}
\]
Now take \(t=u/\sigma_s\), put \(\ell_s=s\sigma_s\), and
increase a fixed threshold so that (8) holds and \(s\ge1\).
Since \(\ell_s\le s^{1/4}\), (12) gives
\[
 A-\sqrt s=\sqrt s\,[H(|u|/\ell_s)-1]
 \ge\frac1{18}\min\left\{
       \frac{\sqrt s}{\ell_s^2}u^2,
       \frac{\sqrt s}{\sqrt{\ell_s}}\sqrt{|u|}\right\}
 \ge\frac1{18}\min\{u^2,\sqrt{|u|}\}.
\]
Combining with (9) and (11) yields the common majorant
\[
 |\psi_s(u)|\le C_0
 \exp\left[-\frac1{18}\min\{u^2,\sqrt{|u|}\}\right].       \tag{13}
\]
For every fixed nonnegative integer \(r\), this bound times
\(|u|^r\) is integrable on the real line: near zero it is
bounded after multiplication; at infinity substitute
\(w=\sqrt{|u|}\) to obtain a polynomial times \(e^{-w/18}\).

Fourier inversion for an integrable characteristic function gives
the continuous density \(g_s\); it agrees with the previously
constructed continuous representative. Applying the weighted
version of (13) permits differentiation under that integral at
every fixed order. Dominated convergence using (10) proves
\[
 g_s^{(r)}(0)=\frac1{2\pi}\int_{\mathbb R}(-iu)^r\psi_s(u)du
 \longrightarrow\frac1{2\pi}\int_{\mathbb R}(-iu)^re^{-u^2/2}du
 =\varphi^{(r)}(0),\qquad
 \varphi(z)=(2\pi)^{-1/2}e^{-z^2/2}.                    \tag{14}
\]
No unproved contour deformation, weak-limit differentiation, or
frequency cutoff is involved.

### 5. Determinants, complete intervals, and ordered minors

Use C028m's proved general identities
\[
 D_k(\varphi;0)=\varphi(0)^k\prod_{j=0}^{k-1}j!,\qquad
 \frac{D_k(p;x_s)}{p(x_s)^k}
 =\sigma_s^{-2d_k}\frac{D_k(g_s;0)}{g_s(0)^k}.             \tag{15}
\]
The first comes from the Gaussian moment Gram determinant and
monic Hermite squared norms \(j!\); the sign \((-1)^{d_k}\)
cancels the product of the row and column Fourier phases. For the
second, multiplication by \(e^{cx}\) acts on the derivative matrix
by the triangular congruence with entries
\(T_{ij}=\binom ij c^{i-j}\), diagonal one. Positive constant
factors cancel after division by the density power. Standardization
contributes determinant factor \(\sigma_s^{k^2}\) and density
power factor \(\sigma_s^k\); their quotient is
\(\sigma_s^{2d_k}\). Thus these same general identities apply
to the present tilt, without importing a half-stable asymptotic.

For each fixed \(k\), (14) through order \(2k-2\) and continuity
of a finite determinant show
\[
 \frac{D_k(p;x_s)}
 {p(x_s)^k(\sigma_s^2)^{-d_k}\prod_{j=0}^{k-1}j!}
 \longrightarrow1.                                    \tag{16}
\]
Here \(g_s(0)\to\varphi(0)>0\), and \(p(x_s)>0\). Fix \(m\)
and choose a common finite threshold \(S_m\) beyond the finitely
many eventual positivity thresholds in (16), \(k\le m\).
The mean satisfies \(x_s>0\), \(x_s'=-\sigma_s^2<0\), and
\(x_s\to0\) by (7). It is continuous and therefore maps
\((S_m,\infty)\) onto \((0,x_{S_m})\). Set
\(\epsilon_m=x_{S_m}>0\). Every \(D_k(p;x)\), \(k\le m\), is
positive throughout this entire interval.

The stated C.16 criterion now applies with
\(I=(0,\epsilon_m)\), and proves (2). To spell out both domain
and orientation requirements, for permitted tuples choose
\(\delta>0\) with
\(2\delta<\min\{x_1-y_k,\epsilon_m-(x_k-y_1)\}\).
Every difference on the enlarged rectangle
\((x_1-\delta,x_k+\delta)\times(y_1-\delta,y_k+\delta)\)
belongs to \(I\). For each fixed \(y\), the initial Wronskians
of \((-1)^jp^{(j)}(x-y)\), indexed by \(j=0,\ldots,k-1\),
are precisely \(D_r(p;x-y)>0\). The first Wronskian criterion
gives positive evaluation determinants at each initial subset of
the \(x_i\). Their transposes are the initial Wronskians, in
variable \(y\), of the functions \(p(x_i-y)\) in increasing
\(i\). The second criterion gives the required evaluation
determinant at the increasing \(y_j\), with unchanged sign after
transposition. Required derivatives have order at most \(2m-2\),
already available. Neither the law nor \(F\) depends on \(m\);
the positivity interval is allowed to do so.

### 6. Failure of global PF for this same law

Suppose that \(p\) were globally PF. It is a nonzero integrable
one-sided density, so BGKP Theorem 1.2 would give its reciprocal
transform as an entire product \(E\) having only real nonpositive
zeros (and a possible exponential factor). On real \(s>0\),
(1) implies \(E(s)=F(s)\). The identity theorem for the two
entire functions implies \(E=F\) everywhere. But \(P\), and
hence \(F\), has the nonreal zeros \(-2+i,-2-i\). The cosh
product has only negative real zeros, so it introduces no ambiguity
at these points. This contradiction proves failure of global PF.

The obstruction is applied only after constructing and identifying
the same positive law and transform. It implies existence of a
negative finite minor by the definition of global PF, but specifies
neither its order nor its location. It does not assert failure of
PF2 or the absence of global log-concavity. All conclusions are
about this fixed countermodel, not actual Xi. ∎

### Separate conceptual audit — 19 November 2026, step1693

**Verdict: passes at the stated fixed-law scope.** Assessment1691,
separately approved1692, covers this audit. The primary statements and
essential proof cases saved in source-notes1689 and1685 are reused.
This verifies the specialization, not the general source theorems or
any actual-Xi positivity assertion. No correction, new hypothesis,
factor adjustment or stronger conclusion is needed.

**One law, including its endpoint.** The cosh product has summable
positive parameters and infinitely many nonzero parameters, precisely
the BGKP existence, positivity and smoothness hypotheses. Its transform
normalization follows by monotone convergence. In (3), the numerator
after taking a common denominator is
\(((s+2)^2+1)-(s+3)(s+1)=2\), so the factor \(5/2\) gives
exactly \(1/P\). The inequality \(\cos t+\sin t\le1+t<e^t\)
holds for every positive \(t\). For a compact \(x\)-set, differentiated
base factors vanish for \(t\) above a fixed \(M\); on \([0,M]\)
they are uniformly bounded at each fixed order. Convolution thus gives
the positive smooth representative, flat zero extension, mass one and
transform (1) for a single law. The radial upper and lower estimates
give exact order \(1/2\); the constant term of \(P\) alone pays
strict positivity of every Taylor coefficient. No order parameter
has entered the construction.

**Spectral criterion.** For \(t\le3/2\), both trigonometric terms
in \(2\cos t+\sin t\) are nonnegative. For \(t\ge3/2\), the
strict comparison follows from
\(806769>20\cdot40320=806400\), hence \(e^{3/2}>2\sqrt5\).
The finite block therefore decreases strictly to zero and is positive.
The quadratic-rate series and its derivative converge uniformly away
from zero. The two displayed Levy integrals separately pay small and
large times. In the absolutely convergent Frullani integrals, the
conjugate logarithms sum continuously from zero to the real logarithm
of the positive quadratic ratio. Tonelli applies to the nonnegative
base terms. Thus (5) describes the already normalized law (1), with
zero drift and a nonnegative nonincreasing spectral function. Simon's
criterion applies to that same law, not a replacement with matching
moments.

**Branches, variance and pointwise limit.** The outer disk in (6)
has \(\Re z\ge s/2\); the principal root and shifted logarithms
are analytic there. Also
\(\Re\sqrt z=\sqrt{(|z|+\Re z)/2}\ge\sqrt{s/2}\).
The power-series logarithm of \(1+e^{-2\sqrt z}\) is therefore
analytic and exponentially small for large \(s\). Cauchy estimates
on the inner quarter disk and the explicit root/polynomial derivatives
give (7) and \(B'''=O(s^{-5/2})\) there. Tilt differentiation uses
\(x^r e^{-sx/2}\) against a probability measure; it gives the mean
and strictly positive variance. In the expansion of \(B(s-it)\),
the linear term is \(-itB'(s)\) and the quadratic term is
\(-t^2B''(s)/2\). The centering phase cancels the first, leaving
\(-u^2/2\) in (10). The lower bound in (8) keeps the whole segment
in the inner disk for fixed \(u\), with error \(O_u(s^{-1/4})\).

**Every frequency and every fixed polynomial weight.** The quadratic
modulus identity before (11) has nonnegative \(t^2,t^4\) coefficients;
the two conjugate factors are not separately assumed monotone. For
\(w=A+iC\),
\(|\cosh w|^2=\sinh^2 A+\cos^2 C\ge\sinh^2 A\).
Since \(A\ge\sqrt s\ge1\), this proves (11) even at oscillatory
frequencies. The two denominator factors in (12) are bounded by
\(3,3\) on \([0,1]\), and by \(3v,3\sqrt v\) on
\([1,\infty)\), so both regimes and their endpoint are covered.
The upper bound in (8) implies
\(\sqrt s/\ell_s^2\ge1\) and
\(\sqrt s/\sqrt{\ell_s}\ge s^{3/8}\ge1\).
Thus (13) is independent of \(s\). For \(|u|\ge1\), its weighted
integral is bounded by a constant times
\(\int_1^\infty w^{2r+1}e^{-w/18}\,dw<\infty\);
on \(|u|\le1\) it is bounded. Integrable characteristic-function
inversion identifies the previously constructed continuous density.
The weighted bound permits differentiation, and adding the integrable
Gaussian weighted bound permits dominated convergence in (14).
This pays every fixed derivative, not derivatives with order growing
in \(s\), and does not infer derivatives from weak convergence.

**Determinants and both interval transfers.** C028m's general proof
gives total Gaussian phase \((-1)^{d_k}\), cancelled in \(D_k\),
and Gram determinant \(\prod_{j<k}j!\). Its binomial triangular
congruence applies to this exponential tilt. Standardization contributes
powers \(\sigma_s^{k^2}\) and \(\sigma_s^k\), giving exactly
\(\sigma_s^{-2d_k}\) in (15). Only derivatives through \(2k-2\)
are used. There are finitely many thresholds for \(k\le m\).
Continuity, \(x_s'=-\sigma_s^2<0\) and limit zero make the late
mean range the entire interval \((0,x_{S_m})\), by the intermediate
value theorem, not a sampled subset.

The strict endpoint margins permit the enlarged rectangle in section5.
For every fixed \(y\) in its second interval, the first Wronskian
has entries \((-1)^j p^{(i+j)}(x-y)\) and determinant
\(D_r(p;x-y)\). Positive evaluation determinants for the first
\(r\) ordered \(x_i\) transpose to the \(y\)-Wronskians of
\(p(x_i-y)\). The second C.1 application and transposition back
introduce no sign change. All intermediate differences stay inside
the certified interval, and all needed derivatives exist. This pays
the exact first assertion of C.16, without a support-boundary variant
or an order-uniform neighborhood.

**Global obstruction and dependencies.** If this same \(p\) were
globally PF, the one-sided BGKP converse would give an entire reciprocal
\(E\) with only real nonpositive zeros. Its equality with \(F\)
on the positive ray has an accumulation point in their common domain
\(\mathbb C\), so the identity theorem applies. Multiplication by
an entire factor cannot cancel the nonreal zeros \(-2\pm i\) of
\(P\). This contradiction yields a negative finite minor of unspecified
size and location, not a PF2 counterexample. C028m's general identities
are the sole local mathematical input. C028g and the older stops are
contrasts. No DAG edge changes or actual-Xi premises are required.
The generic route is now an audited stop; actual-Xi realization,
all-degree signs and \(S_F=0\) remain open.

## Mathlib

Full matching coverage has not been checked. No declaration for this
combined countermodel, the self-decomposability criterion, or the
finite-interval PF transfer is asserted. Standard entire-function,
Fourier inversion, determinant and dominated-convergence ingredients
are mathematical inputs, not a claimed matching formal theorem.
