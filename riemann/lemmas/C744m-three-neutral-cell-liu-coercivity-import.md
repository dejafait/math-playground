# C744m: Cited Liu coercivity on three exactly neutral cells

## Hypotheses

Put ell=log(3)/2, L=3ell and a=L/2. Let

\[
 u(x)=\sum_{j=0}^{2}f_j(x-j\ell),\qquad
 f_j\in C_c^\infty((0,\ell);\mathbb C),\qquad
 \int_0^\ell e^{\sigma s/2}f_j(s)\,ds=0
 \quad(\sigma=\pm1).
 \tag{1}
\]

This is precisely L743(2)'s class U_3. Extend functions by zero;
norms use unweighted Lebesgue measure. Use the complete smooth energy
E_L in L744(6), its Fourier convention F_u(z)=integral u(x)e^(-izx)dx,
and its multiplier m(t)=Re psi(1/4+it/2)-log(pi). There is no H2 cap,
fixed collar, parity restriction or RH assumption.

The external computer-assisted input is **Vincent Liu**, *Certified Weil
Positivity Beyond the Unit Window: Source-Exact Block-Schur and
Tail-Compensation Bounds for the Riemann Zeta Function*, manuscript
14 September 2026, Section 2 equation (1), Section 3 **Theorem A**, equation
(3), printed pp.3–4,
[primary manuscript](https://www.alphaxiv.org/abs/2609.weil-positivity-riemann-zeta-bounds.pdf).
In its notation D_1=C_c^infinity((-1,1);C), and

\[
 Q(g)\ge 2^{-151}\|g\|_2^2\qquad(g\in D_1).                 \tag{2}
\]

This theorem is imported, not reproved. Its complete geometric form is

\[
 \begin{split}
 Q(g)={}&\int_{\mathbb R}m(t)|F_g(t)|^2\frac{dt}{2\pi}
       +2\Re\bigl(F_g(i/2)\overline{F_g(-i/2)}\bigr)\\
       &-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                         \Re C_g(\log n),\qquad
 C_g(d)=\int_{\mathbb R}g(x+d)\overline{g(x)}\,dx.
 \end{split}                                                   \tag{3}
\]

The sum is finite on each compact support. The assessment
`drafts/literature/2026-11-11-three-cell-signed-block-covariance-492.md`
records the inspected analytic proof cases and the frozen delivery
identity. In particular, the source archive is pinned to release
[v1.0-mcom-submission](https://github.com/luciferyu666/certified-weil-positivity/releases/tag/v1.0-mcom-submission),
commit b6cd2183c1e79c6c27a34267812a7b2d73ed1b59; its
[reproduction instructions](https://raw.githubusercontent.com/luciferyu666/certified-weil-positivity/b6cd2183c1e79c6c27a34267812a7b2d73ed1b59/REPRODUCIBILITY.md)
were inspected in that assessment. The numerical archive and complete
source-to-sign arithmetic have **not** been locally replayed. Theorem A
uses retained proposals; no clean reconstruction, independent numerical
verification, formalization or journal acceptance is asserted here.

## Conclusion

As a consequence of the cited external theorem, for every u in (1),

\[
 \boxed{E_{3\ell}(u)\ge 2^{-151}\|u\|_2^2.}                \tag{4}
\]

Thus the lower bound is uniform over the entire three-cell neutral
class, including complex tests and all its signed cross terms. This is
a KNOWN_IMPORTED fixed-window consequence, not a new positivity theorem
or a locally reproduced computer certificate. Non-neutral larger
windows, arbitrary support, all-window propagation and
L030–L032/C032a remain unresolved. The argument below is an applicability
check, not a critical audit of the source computation.

## Proof

Each summand in (1) is smooth after zero extension because its support
is compact in its open cell. The finite sum therefore belongs to
C_c^infinity(0,L;C). Define the centered test

\[
 g(y)=u(y+a).
 \tag{5}
\]

It belongs to C_c^infinity(-a,a;C). To check a<1 without a numerical
approximation, the exponential series gives
e^(4/3)>1+4/3+(4/3)^2/2=29/9>3, hence log(3)<4/3 and
a=3log(3)/4<1. Thus g is in the exact source domain D_1.
Translation gives, by changing variables in absolutely convergent
integrals,

\[
 \|g\|_2=\|u\|_2,\qquad
 F_g(z)=e^{iza}F_u(z)\ (z\in\mathbb C),\qquad
 C_g(d)=C_u(d)\ (d\in\mathbb R).
 \tag{6}
\]

On the real Fourier axis the phase has modulus one, so the first
term of (3) is unchanged. These integrals converge: smooth compactly
supported tests have Schwartz transforms on the real axis and m has
logarithmic growth, as in L744's smooth identity. At the two poles,

\[
 F_g(i/2)=e^{-a/2}F_u(i/2),\qquad
 F_g(-i/2)=e^{a/2}F_u(-i/2).
 \tag{7}
\]

The factors are real and reciprocal, so the conjugate pole pairing
in (3) is exactly unchanged. This checks the full expression before
using neutrality. Indeed (1) separately gives

\[
 F_u(\sigma i/2)
 =\sum_{j=0}^{2}e^{\sigma j\ell/2}
       \int_0^\ell e^{\sigma s/2}f_j(s)\,ds=0.
 \tag{8}
\]

No pole term has been omitted on a larger class by assuming a modulus
square. The source theorem itself does not require these vanishings.

For completeness, with the notebook inner product linear in the first
variable, the zero-extension delay has

\[
 \langle T_du,u\rangle
   =\int_{\mathbb R}u(x-d)\overline{u(x)}\,dx
   =\overline{C_u(d)},\qquad
 \langle(T_d+T_d^*)u,u\rangle=2\Re C_u(d).
 \tag{9}
\]

Hence the arithmetic contribution -<B_Lu,u> of L744(6) is exactly the
last term of (3), with the same coefficients and sign. The source's
opposite sesquilinear convention conjugates scalar pairings; it leaves
these real quadratic values, the Fourier modulus and the real pole
pairing unchanged.

There is no missing prime delay. Correlation vanishes for d>=L:
the conditions x in (0,L) and x+d in (0,L) have no common set of
positive measure then. Since e^L=3sqrt(3) and 5<3sqrt(3)<7
(square to compare 25<27<49), the contributing prime powers in the
target are exactly 2,3,4,5. The only additional prime power allowed by
the source window is 7, and log(7)>L makes its correlation zero for
(5). Every prime power beyond 7 vanishes as well by the same support
argument. No tail is discarded by a sign estimate. The two interfaces
and separation-two interactions remain in the full correlation and
Fourier terms.

Equations (6)–(9), (3) and L744(6) therefore give Q(g)=E_L(u) exactly.
Apply the imported theorem (2) and the norm identity in (6) to obtain
(4), also for u=0. This uses only smooth tests, finite sums and ordinary
changes of variable; no closure extension or interchange over an
infinite family is needed. The proof of applicability passes, subject
to precisely the external input qualification in the hypotheses.

## Mathlib

Full matching Mathlib coverage of Liu's computer-assisted theorem or
(4) has not been checked. Translation invariance and Fourier change
of variables are supporting standard facts, not a formalization of
the positivity certificate. No absence claim or Lean verification is
made.
