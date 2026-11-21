# C618b: Suzuki's decomposition and small-window coercivity

## Hypotheses

Fix real numbers \(a_1>0\) and \(c>1\). Let \(0<a\le a_1\)
and \(\phi\in L^2((-a,a);\mathbb C)\), with Lebesgue measure.
There is no mean-zero, parity, reality or smoothness restriction.
Use \(\widehat\phi,\Phi,E_y,L_T\) and the compact primitive
\(q_\phi\) of C618a; in particular
\(\Phi(\phi,z)=(\widehat\phi(z)-\widehat\phi(0))/z\), with its
removable value at zero, and \(E_0=\int_{\mathbb R}|\Phi(\phi,r)|^2dr\).

Here \(\psi=\Gamma'/\Gamma\), \(\Lambda\) is the von Mangoldt
function, \(m_n=n+1/4\), and \(S=\sum_{n=0}^\infty m_n^{-2}\).
Define real even functions on \(\mathbb R\) by
\[
\begin{split}
g_0(t)&=-4(e^{t/2}+e^{-t/2}-2),\\
g_1(t)&=\sum_{n\le e^{|t|}}\frac{\Lambda(n)}{\sqrt n}(|t|-\log n),\\
g_\infty(t)&=-\frac{|t|}{2}\bigl(\psi(1/4)-\log\pi\bigr)
 -\frac14\sum_{n=0}^\infty\frac{1-e^{-2m_n|t|}}{m_n^2},
\qquad g=g_0+g_1+g_\infty.
\end{split}                                                     \tag{1}
\]
Thus \(g=-\Psi\) for Suzuki's function, and all four values at zero
are zero. Write
\[
G_h(t,u)=h(t-u)-h(t)-h(-u)+h(0),\qquad
Q_a(\phi)=\int_{-a}^a\int_{-a}^aG_g(t,u)\phi(u)\overline{\phi(t)}\,du\,dt.
                                                               \tag{2}
\]

The result reproduced is Masatoshi Suzuki, *Aspects of the screw
function corresponding to the Riemann zeta-function*, J. London Math.
Soc. 108 (2023), 1448–1487,
[DOI 10.1112/jlms.12785](https://doi.org/10.1112/jlms.12785),
[arXiv:2206.03682v4](https://arxiv.org/pdf/2206.03682v4), internal
date 31 May 2023: Theorem 4.2, (4.2), (4.5)–(4.11), printed
pp.12–15. Definition (1) is its (1.1)/(4.8), expressed using the
absolutely convergent Lerch series. The one-sided transforms below
are imported from Section 2.1, (2.1)–(2.5), printed p.6. The source's
small-window conclusion is known; the proof here verifies its full
complex-test domain and reconciles the suspect constant conventions.

Additional named inputs are the Fourier inversion theorem for an
integrable function with integrable Fourier transform (equality at
continuity points), Cauchy's integral theorem on rectangles, and
the gamma facts in [NIST DLMF 5.2(i), (5.2.1)–(5.2.2)](https://dlmf.nist.gov/5.2)
and [DLMF 5.11(i), (5.11.2)](https://dlmf.nist.gov/5.11#E2).
The latter expansion is used only in a fixed sector
\(|\arg w|\le\pi-\delta\), \(\delta>0\), as \(|w|\to\infty\).
C618a supplies the Fourier normalization and its two form estimates;
they are not reproved here.

## Conclusion

Set \(s(z)=1/2-iz\),
\[
P(s)=\frac1{s-1}+\frac1s,\quad Z(s)=\frac{\zeta'(s)}{\zeta(s)},\quad
A(z)=\frac12\psi(1/4-iz/2)-\frac12\log\pi,\quad W(r)=\Re A(r),
\]
and
\[
\mathcal S_\phi(z)=\Phi(\phi,z)\overline{\Phi(\phi,\bar z)}
              +\Phi(\phi,-z)\overline{\Phi(\phi,-\bar z)}.
\]
Then the following identity holds, with every integral absolutely
convergent and each \(I_j\) equal to the form of \(G_{g_j}\):
\[
\begin{split}
Q_a(\phi)&=I_0+I_1+I_\infty,\\
I_0&=\frac1{2\pi}\int_{\mathbb R}P(s(r+ic))\mathcal S_\phi(r+ic)\,dr,\\
I_1&=\frac1{2\pi}\int_{\mathbb R}Z(s(r+ic))\mathcal S_\phi(r+ic)\,dr,\\
I_\infty&=\frac1{2\pi}\int_{\mathbb R}W(r)
             \bigl(|\Phi(\phi,r)|^2+|\Phi(\phi,-r)|^2\bigr)\,dr.
\end{split}                                                     \tag{3}
\]

Here are consistent choices giving a uniform small-window bound.
Put \(\sigma=1/2+c>1\) and
\[
M=\max\left\{\frac1{\sigma-1}+\frac1\sigma,
                   \sum_{n=2}^\infty\frac{\Lambda(n)}{n^\sigma}\right\},
\quad C_2=e^{2ca_1},\quad C=2MC_2+1.                         \tag{4}
\]
Choose \(T>0\) such that \(W(r)\ge C\) for \(|r|\ge T\), and set
\[
D=\max\{0,-\min_{|r|\le T}W(r)\},\quad C_3=\frac{2T}{\pi},
\quad a_0=\min\left\{a_1,\frac1{2(C+D)C_3}\right\}>0.       \tag{5}
\]
These constants exist and are independent of \(a\) and \(\phi\).
For \(0<a\le a_0\),
\[
\boxed{\displaystyle Q_a(\phi)\ge\frac{E_0(\phi)}{2\pi},}
\qquad E_0(\phi)>0\quad\hbox{if }\phi\ne0\text{ in }L^2.     \tag{6}
\]
No numerical value of \(T\) or \(a_0\) is certified. The coercive
quantity is \(E_0\), not the original \(L^2\) norm of \(\phi\).
This establishes the stated local form result without RH; it does
not give arbitrary-window positivity, signed arithmetic/complement
control or Xi/common-graph realization. L030/L032/C032a are context,
not mathematical premises. No progress beyond the source's local
positivity theorem is asserted.

## Proof

### One-sided inversion, including both spatial signs

For \(j\in\{0,1,\infty\}\), let \(h_j(t)=g_j(t)\) for \(t\ge0\)
and \(h_j(t)=0\) for \(t<0\). These functions are continuous, including
at zero. For \(g_1\) this follows from local finiteness and the zero
value of each newly entering summand at \(t=\log n\). For
\(g_\infty\), uniform convergence follows from domination by the
summable sequence \(m_n^{-2}\), and each summand vanishes at zero.

For large positive \(t\), \(g_0(t)=O(e^{t/2})\),
\(g_\infty(t)=O(1+t)\), and
\[
0\le g_1(t)\le t^2\sum_{n\le e^t}n^{-1/2}\le2t^2e^{t/2}.
\]
The last bound uses \(\Lambda(n)\le\log n\le t\); changing a
bounded initial range does not affect integrability. Consequently
\(f_j(t)=e^{-ct}h_j(t)\) is continuous and in \(L^1(\mathbb R)\).

The cited source transforms, with their signs reversed from \(\Psi\)
as required by (1), give
\[
\int_0^\infty g_j(t)e^{izt}\,dt=\frac{B_j(z)}{z^2},
\quad B_0(z)=P(s(z)),\ B_1(z)=Z(s(z)),\ B_\infty(z)=A(z),    \tag{7}
\]
on \(\Im z=c\). The pole and prime formulas require \(c>1/2\);
the linear/digamma formulas require \(c>0\). Both are satisfied.
For the prime interchange an explicit absolute bound is
\[
\sum_{n=2}^\infty\frac{\Lambda(n)}{\sqrt n}
 \int_{\log n}^\infty(t-\log n)e^{-ct}\,dt
 =\frac1{c^2}\sum_{n=2}^\infty\frac{\Lambda(n)}{n^{1/2+c}}<\infty.
\]
For the digamma series the corresponding integral is at most
\(S/(4c)\). Thus the source transforms apply as ordinary absolutely
convergent integrals on this line. Equation (7) for \(j=\infty\)
comes from adding the linear transform (2.2) to (2.4); it retains
the factor \(1/2\) on both \(\psi\) and \(\log\pi\).

On \(\Re s=\sigma\), the absolutely convergent source Dirichlet
series \(Z(s)=-\sum_{n\ge2}\Lambda(n)n^{-s}\) and the elementary
pole bounds give \(|P(s)|,|Z(s)|\le M<\infty\). Finiteness follows
also from \(\Lambda(n)\le\log n\) and \(\sigma>1\).
For the gamma factor, if \(z=r+iy\), \(0\le y\le c\), then
\[
\Re(1/4-iz/2)=1/4+y/2\in[1/4,1/4+c/2].
\]
DLMF 5.2 excludes poles and zeros of \(\Gamma\) here. DLMF 5.11.2
applies uniformly in this strip, contained in the sector
\(|\arg w|\le\pi/2\), and yields
\[
|A(r+iy)|\le K\log(2+|r|)\quad(0\le y\le c)                \tag{8}
\]
for some finite \(K\). Compactness covers bounded \(r\).
Therefore all three functions \(B_j(r+ic)/(r+ic)^2\) belong to
\(L^1(dr)\). They are exactly the positive-exponent Fourier
transforms of \(f_j\), by (7).

Fourier inversion for \(f_j\) and its integrable transform, using
inverse measure \(dr/(2\pi)\), now gives at every real \(x\)
\[
h_j(x)=\frac1{2\pi}\int_{\mathbb R+ic}
                    \frac{B_j(z)}{z^2}e^{-izx}\,dz.           \tag{9}
\]
In particular this inverse is zero for \(x<0\), equals \(g_j(x)\)
for \(x>0\), and is zero at \(x=0\). This proves both spatial
cases without an unsupported contour limit \(c\to\infty\).
Since \(g_j(x)=h_j(x)+h_j(-x)\), including at zero, subtracting
twice (9) at zero gives
\[
g_j(x)=\frac1{2\pi}\int_{\mathbb R+ic}\frac{B_j(z)}{z^2}
                      (e^{izx}+e^{-izx}-2)\,dz.             \tag{10}
\]
All integrals here are absolute for each fixed spatial argument.

### The increment kernels, contour shift and complex tests

Define the entire quotients \(R_\pm(v,z)=(e^{\pm izv}-1)/z\)
with \(R_\pm(v,0)=\pm iv\), and put
\[
H(t,u,z)=R_+(u,z)R_-(t,z)+R_-(u,z)R_+(t,z).
\]
Substitution in (10) and expansion of the two products gives
\[
G_{g_j}(t,u)=\frac1{2\pi}\int_{\mathbb R+ic}B_j(z)H(t,u,z)\,dz.
                                                               \tag{11}
\]
Indeed each product numerator is the corresponding exponential at
\(t-u\) minus the exponentials at \(t\) and \(-u\), plus one.

For \(|v|\le a_1\), \(z=r+iy\) and \(0\le y\le c\), the
integral representation of the removable quotient gives
\(|R_\pm(v,z)|\le a_1e^{ca_1}\). For \(|r|\ge1\) one also has
\(|R_\pm(v,z)|\le(e^{ca_1}+1)/|r|\). Thus, for a fixed finite
constant \(K_1\), uniformly on \(|t|,|u|\le a_1\),
\[
|H(t,u,r+iy)|\le\frac{K_1}{1+r^2}\quad(0\le y\le c).       \tag{12}
\]
These estimates justify all the finite kernel subtractions in (11).
They also give an integrable majorant for the gamma integrand,
\(KK_1\log(2+|r|)/(1+r^2)\), throughout the closed strip.

The function \(A(z)H(t,u,z)\) is holomorphic on a neighborhood of
that strip: the gamma argument has positive real part, and the
quotients are entire, including at \(z=0\). On the vertical edges
\(z=\pm R+iy\), \(0\le y\le c\), its absolute value is
\(O(\log R/R^2)\), uniformly in \(t,u\) on the compact square.
Each edge integral is therefore \(O(c\log R/R^2)\to0\).
Cauchy's theorem on the finite rectangle, followed by dominated
convergence on its horizontal sides, proves
\[
G_{g_\infty}(t,u)=\frac1{2\pi}\int_{\mathbb R}A(r)H(t,u,r)\,dr.
                                                               \tag{13}
\]
Only this increment-kernel integrand has been shifted; no singular
unsubtracted \(A(z)/z^2\) is moved through zero.

Since \(\|\phi\|_1\le\sqrt{2a}\|\phi\|_2\), multiplying
(11) or (13) by \(|\phi(u)\phi(t)|\) leaves an absolutely
integrable triple integral, by (8), (12), and the bound \(M\)
on the shifted line. Fubini therefore applies directly to the full
complex \(L^2\) class. In particular,
\[
\int\!\int H(t,u,z)\phi(u)\overline{\phi(t)}\,du\,dt
 =\Phi(\phi,z)\overline{\Phi(\phi,\bar z)}
  +\Phi(\phi,-z)\overline{\Phi(\phi,-\bar z)}.              \tag{14}
\]
The conjugated arguments are essential; no reality of \(\phi\)
is used. On the real axis (14) is the nonnegative even function
\(\mathcal S_\phi(r)=|\Phi(\phi,r)|^2+|\Phi(\phi,-r)|^2\).
Moreover \(A(-r)=\overline{A(r)}\): conjugation follows from
Euler's gamma integral in the positive half-plane, differentiation,
and nonvanishing there. Changing \(r\) to \(-r\) in the absolutely
convergent integral proves that \(A\) may be replaced by \(W=\Re A\)
in (13) after integration against the test. This proves (3).

For clarity, the gamma-weighted integrals are absolute even for a
test with nonzero mean: for \(|r|\ge1\),
\(|\Phi(\phi,\pm r)|\le2\|\phi\|_1/|r|\); near zero the
removable quotient is bounded by \(a\|\phi\|_1\). Combined
with (8), these give an explicit integrable majorant. No smooth
approximation or unproved limit exchange is needed. The original
forms exist because their kernels are continuous on the compact
square. Each is real, by the real symmetric kernel and the same
absolute integrability.

### Consistent constants and the positive coefficient

C618a, (10), applied on the actual line \(\Re s=1/2+c\), bounds
each of the two products in each of \(I_0,I_1\) by
\(MC_2 E_0/(2\pi)\) in absolute value. The real-valuedness just
proved therefore yields the direction needed for coercivity:
\[
I_0+I_1\ge-|I_0|-|I_1|\ge-\frac{4MC_2}{2\pi}E_0.          \tag{15}
\]

On the real line the same DLMF expansion gives
\[
W(r)=\tfrac12\log|1/4-ir/2|-\tfrac12\log\pi+O(1/|r|)
       \longrightarrow+\infty\quad(|r|\to\infty).
\]
Thus the threshold \(T>0\) in (5) exists for the actual normalized
weight. Its continuity on the compact band makes \(D\) finite,
nonnegative and a genuine lower bound: \(W\ge-D\) on that band.
For each of the two signs in (3), split the absolutely convergent
integral into the band and its complement. Reflection preserves
both \(E_0\) and \(L_T\), so
\[
I_\infty\ge\frac{2}{2\pi}\{C E_0-(C+D)L_T\}.              \tag{16}
\]
Using C618a's \(L_T\le aC_3E_0\) and (15), we get for every
\(0<a\le a_1\)
\[
Q_a(\phi)\ge\frac{2}{2\pi}
       [C-2MC_2-(C+D)aC_3]E_0
 =\frac{2}{2\pi}[1-(C+D)aC_3]E_0.                         \tag{17}
\]
For \(a\le a_0\), the bracket is at least \(1/2\), proving (6).
This defines the constants in the order \(a_1,c,M,C_2,C,T,D,C_3,a_0\);
none depends on the eventual test or the smaller window. The factors
of two count the two frequency signs and the two non-gamma terms.

Finally C618a's exact Plancherel identity gives
\(E_0=2\pi\|q_\phi\|_2^2\). If this is zero, the absolutely
continuous representative of \(q_\phi\) on each half-interval is
identically zero: continuity and almost-everywhere vanishing imply
pointwise vanishing there. Its derivative is \(-\phi\) almost
everywhere on each half, so \(\phi=0\) almost everywhere on
\((-a,a)\). The point zero has measure zero and its allowed jump
adds no exceptional test. Hence (6) is strictly positive for every
nonzero \(L^2\) test.

This is the promised reproduction with explicit bookkeeping. It
does not use the source's multiplier bound on the different line
\(\Re s=1+c\), its differently normalized later gamma displays,
its maximum in place of a lower-band loss, or an upper bound as a
lower bound. Their discrepancies do not refute Theorem 4.2; (3)–(17)
justify its local form conclusion with consistent replacements.

### Independent conceptual review — 16 November 2026, step1126

Accepted (3)–(17) and the full stated complex-test conclusion under
the separately approved assessment1124. This review found no remaining
analytic obligation in this local theorem and made no change to its
hypotheses, constants or mathematical argument. It verifies a known
source reproduction, not an extension of Suzuki's conclusion.

The review checked the complete proof against the primary v4 passages
cited above and the full C618a input. In particular:

- In (7), reversing the sign of the source's (2.1) gives the pole
  transform, and reversing (2.3) gives the prime transform with
  \(Z=-\sum\Lambda(n)n^{-s}\). Reversing (2.4) and adding the
  linear term from (2.2) gives
  \([\psi(s/2)-\psi(1/4)+\psi(1/4)-\log\pi]/(2z^2)
  =A(z)/z^2\). Thus both the sign and the gamma half-factor agree.
  The displayed absolute sum bounds justify these uses on the actual
  line \(\Re s=1/2+c>1\), without a zero hypothesis.
- Fourier inversion is applied to \(f_j=e^{-ct}h_j\), not directly
  to its growing even extension. Its integrable transform and
  continuity include the origin. Multiplication of the inverse by
  \(e^{cx}\) gives exactly (9) at positive, negative and zero \(x\);
  the subtracted constant in (10) integrates to zero. No inverse
  identity is being inferred from a positive-spatial case alone.
- The uniform bounds (8),(12) control the whole rectangle and both
  infinite horizontal integrals. The gamma argument stays in the
  fixed positive-real-part strip and fixed DLMF sector. The removable
  quotients, rather than \(A(z)/z^2\), cross zero. The compact-square
  majorant multiplied by \(|\phi(u)\phi(t)|\) is integrable, so the
  contour passage and Fubini remain valid for non-smooth complex tests.
- In (14), integrating \(R_-\) against \(\phi\) gives
  \(-\Phi(\phi,-z)\); the paired conjugate factor has the other
  minus sign. Their product has the asserted positive sign. On the
  real axis the sum of the two squares is even for every complex
  test, although either individual square need not be even. This
  is precisely the symmetry needed to replace \(A\) by \(W\).
- C618a bounds each of four non-gamma products by
  \(MC_2E_0/(2\pi)\). Both gamma terms supply the same full energy
  and band loss. The resulting coefficient is exactly
  \([1-(C+D)aC_3]/\pi\), at least \(1/(2\pi)\) for
  \(a\le a_0\), including equality at the endpoint. The order of
  choosing constants has no dependence on the eventual test or on
  a smaller window. The finite lower-band loss is \(D\), not the
  source's differently normalized maximum.
- C618a's primitive may jump at zero; the proof never discards that
  jump or assumes zero mean. Its absolutely continuous restrictions
  on the two half-intervals prove injectivity from \(E_0=0\), with
  the single point zero contributing no exceptional \(L^2\) test.

C618a remains the sole direct local mathematical input. The reviewed
proof contains no numerical onset, lower bound by \(\|\phi\|_2^2\),
arbitrary-window sign, low-mode coupling estimate or Xi realization.
Those independent gaps remain open. No numerical test was used to
accept the identities or the uniform coercivity claim.

## Mathlib

Full matching coverage and supporting theorem names were not checked
in Mathlib. This is not a claim of absence. The named inversion,
complex-analysis and DLMF inputs above, together with C618a, specify
the imports; all specializations and convergence arguments used here
are written out. No Lean verification or numerical certificate is
claimed. This step is a conceptual reproduction audit of a known
theorem, not a complete RH candidate.
