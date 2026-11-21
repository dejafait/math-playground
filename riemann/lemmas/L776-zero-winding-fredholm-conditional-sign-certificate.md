# Lemma 776: conditional zero-winding Fredholm certificate for an exceptional minor

## Hypotheses

Use the completion and moments of L018 and L021. Define the actual entire
function and its ordinary coefficients by

\[
 G(w)=\frac18\xi\left(\frac12+\frac{\sqrt w}{2}\right)
     =\sum_{n\ge0}a_nw^n,\qquad
 a_n=\frac{M_{2n}}{8\,4^n(2n)!}>0.
\]

The square-root notation denotes the entire function given by the series;
reflection about 1/2 makes it independent of the square-root choice. Fix an
integer r>=2, write k=r-1, and assume R>0 satisfies both conditions:

1. G has no zero on |w|=R.
2. G has exactly k zeros in |w|<R, counted with multiplicity.

No further zero-location, zero-simplicity or coefficient-minor sign is
assumed. Set

\[
 D_{(r,k)}=\det[a_{k+j-i}]_{i,j=0}^{r-1},\qquad
 \phi(z)=z^{-k}G(Rz)\quad (|z|=1).
\]

Fourier coefficients use f_j=(2pi)^(-1) int_0^(2pi)
f(e^(it))e^(-ijt)dt. On the complex Hilbert space l2(N), with coordinates
starting at 1, set H(f)_(i,j)=f_(i+j-1), tilde f(z)=f(1/z), and let P_r
retain coordinates 1,...,r and Q_r=I-P_r. Operator norm, trace norm and
Hilbert–Schmidt norm are denoted respectively by ||.||, ||.||_1 and ||.||_2.

## Conclusion

There is a unique logarithm ell of phi on a sufficiently small connected
annulus about |z|=1 normalized by ell(1)=log G(R), with the real logarithm
on the right. It satisfies ell(conj z)=conj ell(z), so all its Laurent
(equivalently, circle Fourier) coefficients ell_j are real. Define, with
the constant term placed exactly as below,

\[
 \phi_-(z)=\exp\left(\sum_{j\ge1}\ell_{-j}z^{-j}\right),\qquad
 \phi_+(z)=\exp\left(\sum_{j\ge0}\ell_jz^j\right),\qquad
 b=\phi_-/\phi_+,\quad c=\phi_+/\phi_-.
\]

Both H(b) and H(tilde c) are Hilbert–Schmidt. The operator

\[
 A_{r,R}=Q_rH(b)H(\widetilde c)Q_r
\]

is trace class and commutes with coordinatewise complex conjugation.
There is the exact identity

\[
 D_{(r,r-1)}=
 R^{-r(r-1)}\exp\left(r\ell_0+
               \sum_{j\ge1}j\ell_j\ell_{-j}\right)
               \det(I-A_{r,R}).                                      \tag{1}
\]

The prefactor is strictly positive. Consequently the additional, unpaid
hypothesis ||A_(r,R)||<1 implies D_(r,r-1)>0. This is only a sufficient
condition; no necessity, actual norm estimate or existence of such R is
asserted.

## Proof

**Entire function and zero index.** L021's globally convergent expansion
of Xi, together with Xi(z)=xi(1/2+iz) from L018, gives the displayed
coefficients of G by substituting z=-i sqrt(w)/2. Absolute convergence
on every bounded w-disk follows by the same substitution in the absolute
Xi series. Thus G is entire, has real coefficients and G(R)>0. In
particular G(0)=a_0>0.

By contour nonvanishing and compactness, choose 0<rho_0<1<sigma_0 such
that G(Rz) has no zeros on the annulus U={rho_0<|z|<sigma_0}. The annulus
is invariant under conjugation and phi is holomorphic and nonvanishing
there. The argument principle gives

\[
 \frac1{2\pi i}\int_{|z|=1}\frac{\phi'(z)}{\phi(z)}\,dz
 =-k+\frac1{2\pi i}\int_{|w|=R}\frac{G'(w)}{G(w)}\,dw
 =-k+k=0.                                                       \tag{2}
\]

The integral on any closed curve in U is zero: phi'/phi is holomorphic
there, and every closed curve has a homology class which is an integer
multiple of the unit circle. The standard holomorphic logarithm theorem
(equivalently, the vanishing-period criterion for phi'/phi) therefore
provides a holomorphic ell with exp ell=phi. Since phi(1)=G(R)>0,
choose its additive multiple of 2pi i so that ell(1)=log G(R). The
connectedness of U gives uniqueness with this normalization. No logarithm
on the disk containing the k zeros has been taken.

**Real structure, without pointwise reality.** Real coefficients give
phi(conj z)=conj phi(z) on U. The holomorphic function
ell^sharp(z)=conj(ell(conj z)) is another logarithm of phi on U, and
ell^sharp(1)=log G(R). Uniqueness implies ell^sharp=ell. Comparing the
unique Laurent expansions gives ell_j=conj ell_j for every integer j.
This proves coefficient reality; it does not assert that ell(e^(it))
is real for general t.

For rho_0<rho<1<sigma<sigma_0, the Laurent coefficient estimates on
|z|=rho and |z|=sigma give constants C_-, C_+ such that

\[
 |\ell_{-j}|\le C_-\rho^j\quad(j\ge1),\qquad
 |\ell_j|\le C_+\sigma^{-j}\quad(j\ge0).                       \tag{3}
\]

The split series and their exponentials thus define the displayed
factors holomorphically on a common annulus about the circle. Their
product is phi, both are nonzero, and they have conjugation symmetry.
The same holds for b and c. In particular their Laurent coefficients
are real. All these restrictions to the unit circle are smooth, hence
belong to C^beta for any fixed noninteger beta>1/2, for example beta=3/2.

**Operator hypotheses.** Choose two radii rho_1<1<sigma_1 in that common
annulus. Cauchy estimates for b and c give finite B,C with

\[
 |b_j|\le B\sigma_1^{-j},\qquad
 |c_{-j}|\le C\rho_1^j\qquad(j\ge1).
\]

Each positive integer j occurs exactly j times as i+h-1 for i,h>=1.
It follows that

\[
 \|H(b)\|_2^2=\sum_{j\ge1}j|b_j|^2<\infty,\qquad
 \|H(\widetilde c)\|_2^2=\sum_{j\ge1}j|c_{-j}|^2<\infty.        \tag{4}
\]

The standard Schatten ideal product inequality implies that their product
is trace class, with trace norm at most the product of the two displayed
Hilbert–Schmidt norms. Multiplication by the orthogonal projections Q_r
preserves trace class. Real matrix entries make both Hankel operators
commute with coordinate conjugation, first on finitely supported
sequences and then by boundedness on l2. This property is preserved by
products and by Q_r, so A_(r,R) is a real operator. Selfadjointness or
positive semidefiniteness is not assumed.

**Imported exact identity and its normalization.** Apply A. Böttcher
and H. Widom, *Szegő via Jacobi*,
[arXiv:math/0604009v1](https://arxiv.org/pdf/math/0604009v1),
Section 1 equations (1)–(2), Theorems 1.1–1.2, pp.1–3; the exact-identity
proof is Section 3, p.5, and the prefactor identity is Section 4, pp.5–6.
The required hypotheses are a nonvanishing zero-index C^beta symbol,
beta>1/2 noninteger. They have all been verified for the whole symbol
phi. The factor normalization above is the source normalization. Writing
g(phi) for the source's scalar G(phi) to distinguish it from our entire G,
the imported theorem and prefactor identity state

\[
 \det T_r(\phi)=g(\phi)^r E(\phi)\det(I-A_{r,R}),\quad
 g(\phi)=e^{\ell_0},\quad
 E(\phi)=\exp\left(\sum_{j\ge1}j\ell_j\ell_{-j}\right).        \tag{5}
\]

Here T_r(phi)_(i,j)=phi_(i-j), 1<=i,j<=r. Equation (3) proves absolute
convergence of the exponent in E. Its summands and ell_0 are real, so
g(phi)^r E(phi)>0; no sign of an individual summand is needed. We use
only the exact identities, not the source's fixed-symbol asymptotic
remainder. There is no shifted-minor boundary determinant in this
zero-index application and no assumption that T_r(phi) is invertible.
More explicitly, Theorem 1.1 states that I-H(b)H(tilde c) is
invertible and places its determinant in the denominator. Theorem 1.2
identifies the reciprocal of that denominator with E(phi). This
uncompressed invertibility is a theorem conclusion under the verified
symbol hypotheses, not an additional norm assumption on A_(r,R).

The actual Fourier coefficients are phi_h=a_(k+h)R^(k+h), with a_n=0
for n<0. If S=diag(R^1,...,R^r) and B_(i,j)=a_(k+i-j), then

\[
 T_r(\phi)=R^k S B S^{-1},\qquad
 \det T_r(\phi)=R^{kr}\det B=R^{kr}D_{(r,k)}.                  \tag{6}
\]

The final equality is matrix transposition, which adds no determinant
sign. Since k=r-1 all indices in B are nonnegative. Equations (5)–(6)
prove (1), including its positive radius factor.

**Strict determinant sign under the norm bound.** Put A=A_(r,R) and
q=||A||<1. The case q=0 gives A=0 and determinant 1. Otherwise A^m is
trace class and the ideal and trace inequalities give

\[
 |\operatorname{tr}(A^m)|\le\|A^m\|_1
             \le\|A\|_1q^{m-1},\qquad
 \sum_{m\ge1}\frac{|\operatorname{tr}(A^m)|}{m}
             \le\frac{\|A\|_1}{1-q}<\infty.                    \tag{7}
\]

Every trace is real: A^m commutes with conjugation, its diagonal entries
in the standard real orthonormal basis are real, and the diagonal trace
sum is absolutely convergent for a trace-class operator. Plemelj's
trace-class determinant formula, in F. Bornemann, *On the numerical
evaluation of Fredholm determinants*,
[arXiv:0804.2543v2](https://arxiv.org/pdf/0804.2543v2),
Section 3, pp.9–10, equation (3.3), now gives

\[
 \det(I-A)=\exp\left(-\sum_{m\ge1}
                         \frac{\operatorname{tr}(A^m)}m\right)>0. \tag{8}
\]

Indeed spectral radius is at most q<1, so the norm-small point z=-1
lies in the formula's convergence domain; (7) independently verifies
absolute convergence here. The exponent is finite and real. Thus the
argument establishes positivity, not merely nonvanishing, without using
Bornemann's separate positive-selfadjoint Lemma 4.1. Combining (8) with
(1) completes the conditional certificate.

This is a reproduction/specialization of known identities; no reproof
of the Borodin–Okounkov formula is intended. The extra work is precisely
the actual-G index, symmetry, regularity, normalization and sign checks.
No numerical computation is used. The norm condition remains unproved
for actual admissible pairs (r,R), and existence of such R for all needed
r is independent: equal zero moduli and multiplicities can skip counts.
Other indices, all-degree mixed positivity and RH remain unresolved.

**Conceptual audit, 2026-11-04 (step429).** Equations (1)–(8) pass under
the stated hypotheses. The audit checked L018/L021's entire-function
normalization, the zero-count period on the annulus, the normalized
conjugation identity, both Laurent tails and Schatten hypotheses, the
source's one-based indices and placement of ell_0, the positive radius
factor and transpose, and absolute convergence and reality of the
Plemelj exponent. Böttcher–Widom v1 pp.1–3 and Sections 3–4, pp.5–6,
and Bornemann v2 Section 3, pp.9–10, were directly rechecked for these
imports. In particular, the sign argument uses neither a pointwise-real
logarithm nor a positive-selfadjoint operator. No mathematical defect,
new hypothesis or stronger estimate was found. This verifies a local
specialization of known theorems; it supplies no actual norm below one,
certified admissible radius or additional coefficient sign. The direct
local mathematical inputs remain L018 and L021; no L777 conclusion is
used to prove this lemma.

## Mathlib

Full matching coverage is not checked. In particular no Mathlib theorem
for this Toeplitz/Fredholm specialization is claimed present or absent.
The cited primary results and the standard named argument principle,
holomorphic logarithm theorem, Laurent estimates and Schatten ideal
inequalities are the informal inputs; formalization is not asserted.
