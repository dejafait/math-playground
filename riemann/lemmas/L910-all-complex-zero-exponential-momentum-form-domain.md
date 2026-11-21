# L910: all complex-zero images belong to the fixed exponential-momentum form domain

## Hypotheses

Use exactly w,D,L of L906, the primitives u_alpha of L907, and the
complex transform normalization L908(1). In logarithmic coordinates,

\[
W(x)=w(e^x),\qquad U_\alpha(x)=u_\alpha(e^x),\qquad
G_\alpha(x)=(Lu_\alpha)(e^x).
\]

Retain every complex alpha satisfying Xi(alpha)=0; no reality,
simplicity, indexing or height bound is assumed. Use the unitary
Fourier convention

\[
\mathcal F f(k)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-ikx}\,dx.
\]

On L2(R,dx), let P be the self-adjoint momentum realization
\(\mathcal F^{-1}k\mathcal F\), and define M=exp(-P/4) by spectral
calculus. Its quadratic-form domain, distinct from its operator domain, is

\[
Q=\operatorname{Dom}(M^{1/2})
=\left\{f\in L^2:\int_{\mathbb R}e^{-k/4}|\mathcal F f(k)|^2dk<\infty\right\}.
\]

## Conclusion

For every retained complex zero alpha, G_alpha belongs to Q. More
precisely, G_alpha has a holomorphic extension to |Im z|<1/4,
continuous on each finite portion of the closed strip, and

\[
\int_{\mathbb R}e^{-k/4}|\mathcal F G_\alpha(k)|^2dk
=\int_{\mathbb R}|G_\alpha(x+i/8)|^2dx<\infty.                 \tag{1}
\]

The full finite spectral span of L-images therefore lies in Q.
Constants below may depend on alpha. This proves a domain prerequisite
only: pair symmetry, generalized eigenvectors, completion and actual-Xi
mixed positivity are not conclusions. The separate step161 critical
audit below passes for the stated domain claim.

## Proof

**Imported construction and reason for the direct estimates.** The
positive exponential-momentum construction is known: Ahmed,
*Pseudo-Hermiticity of Hamiltonians under imaginary shift of the
co-ordinate: real spectrum of complex potentials*,
[quant-ph/0108016v2](https://arxiv.org/pdf/quant-ph/0108016v2),
pp2-3, (4)-(6). We do not use its formal translation argument as a
domain theorem. The rigorous spectral construction, square-root form
domain and Fourier realization are the specialization of Teschl,
*Mathematical Methods in Quantum Mechanics* (2009),
[primary text](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
Theorem3.2/(3.25), pp91-92, (3.50)-(3.51), p97,
Theorem7.5, p164, and Section8.1/(8.4), pp173-174.
Theorem7.5 supplies Plancherel with the stated normalization.
These inputs are reused from the approved source assessment; none
establishes domain inclusion for the particular G_alpha.

The unchanged theta series and primitives are those of Hedenmalm,
*Spectral interpretation of Riemann zeta zeros*,
[2606.17494v1](https://arxiv.org/html/2606.17494v1), (1.2.3),
(3.2.1)-(3.2.2), Theorem3.3.3 and Section4.2, as qualified in
L906-L908. Only L908(1) is used, not its real-only norm estimates
or its step154 addition. The application requires the following
explicit denominator and endpoint estimates; it cannot be inferred
from real-line smoothness or Schwartz decay. Cauchy's integral theorem
and the identity theorem are used in their standard holomorphic forms.

**Holomorphic theta series and a complete denominator bound.** Write

\[
W(z)=e^{z/2}\sum_{n\ge1}P_0(v_n)e^{-v_n},\qquad
P_0(v)=2v^2-3v,\qquad v_n=\pi n^2e^{2z}.                  \tag{2}
\]

This series and each fixed-order z derivative converge locally
uniformly in the connected strip S={|Im z|<pi/4}. On a compact
subset of S, Re(pi exp(2z)) has a strictly positive minimum;
the derivative terms are bounded by a constant times n^N exp(-c n^2)
for a fixed N and c>0. Those majorants are summable. Thus (2)
is holomorphic, and L906's real identity W(-x)=W(x) extends by
the identity theorem to W(-z)=W(z) throughout S.

First take z=x+iy with x>=0, |y|<=1/4. Put

\[
R=\pi e^{2x}>3,\quad v=\pi e^{2z},\quad
a=\operatorname{Re}v=R\cos(2y),\quad c=7\pi/8.
\]

The elementary inequality cos(t)>=1-t^2/2 gives cos(2y)>=7/8,
so a>=7R/8>2 and a>=c exp(2x). Also

\[
|P_0(v)|\ge R(2R-3)\ge R^2,\qquad
|P_0(n^2v)|\le3n^4R^2.
\]

For completeness, the entire relative tail is bounded without
sampling. Set b_n=n^4 exp(-2(n^2-1)), n>=2. L906 proves e^3>20.
Consequently

\[
b_2=16e^{-6}<1/25,\qquad
\frac{b_{n+1}}{b_n}
\le(3/2)^4e^{-10}<\frac{81}{128000}<\frac1{1000},
\]

where e^10>e^9>8000. Hence

\[
\sum_{n\ge2}n^4e^{-a(n^2-1)}
\le\sum_{n\ge2}b_n<\frac{40}{999},\qquad
3\sum_{n\ge2}b_n<\frac{40}{333}<\frac18.                  \tag{3}
\]

The last bound controls the full tail relative to the n=1 term
of (2). The reverse triangle inequality and the upper estimates give

\[
\frac78 e^{x/2}R^2e^{-a}\le |W(z)|
\le4e^{x/2}R^2e^{-a}.                                    \tag{4}
\]

For the upper bound, specifically, 3(1+40/999)<4.
There is no cancellation assumption in either direction.

Termwise differentiation, justified above, uses L906's polynomial
P_1(v)=-4v^3+15v^2-(15/2)v. For |v|>=3 its absolute value is
at most 10|v|^3. For d_n=n^6 exp(-a(n^2-1)), n>=1,

\[
\frac{d_{n+1}}{d_n}\le64e^{-6}<\frac4{25},\qquad
\sum_{n\ge1}d_n\le\frac{25}{21}<2.
\]

It follows that |W'(z)|<=20 exp(x/2) R^3 exp(-a). Dividing by
(4), which also proves nonvanishing, yields
|W'(z)/W(z)|<24R. Reflection by W(-z)=W(z) gives both conclusions
on x<=0, including W'(-z)=-W'(z). Thus W has no zeros on
|Im z|<=1/4. For r=|x|, throughout that closed strip we have

\[
|W(x+iy)|\le4\pi^2 e^{9r/2-c e^{2r}},\qquad
|q(x+iy)|\le24\pi e^{2r},\quad q=W'/W.                    \tag{5}
\]

In particular q is holomorphic on the open strip and continuous
on every finite part of its boundary. The lower bound (4), rather
than real-axis positivity alone, justifies this division.

**Complex-zero primitives at both ends.** Fix alpha=A+ib with
Xi(alpha)=0, and put B=|b|. In S define

\[
H_\alpha(z)=\int_{-\infty}^0 e^{i\alpha s}W(s)ds
              +\int_0^z e^{i\alpha\zeta}W(\zeta)d\zeta,
\qquad U_\alpha(z)=e^{-i\alpha z}H_\alpha(z).              \tag{6}
\]

The real improper integral converges by L906, or (5); the finite
path integral is independent of path in the simply connected strip
S by Cauchy's theorem. This gives a holomorphic extension of L907's
primitive and the exact identity U_alpha'=-i alpha U_alpha+W.

For |y|<=1/4, deforming the left-end path in (6) gives

\[
U_\alpha(z)=e^{-i\alpha z}
       \int_{-\infty+iy}^{z}e^{i\alpha\zeta}W(\zeta)d\zeta.
\tag{7}
\]

Here and below horizontal integrals are oriented toward increasing
real part. To justify the endpoint in this contour deformation,
on either vertical side z=+/-T+it, |t|<=1/4, (5) bounds the
absolute integrand e^(i alpha z)W(z) by

\[
4\pi^2\exp\big((B+9/2)T+|A|/4-c e^{2T}\big),             \tag{8}
\]

which tends to zero. The side lengths are bounded, and the horizontal
integrals converge absolutely by the same estimate. This proves (7)
by a finite rectangle followed by its left-end limit, without assuming
a transformation rule for the improper primitive.

A rectangle with both endpoints tending to infinity similarly gives

\[
\int_{-\infty+iy}^{\infty+iy}e^{i\alpha\zeta}W(\zeta)d\zeta
=\int_{\mathbb R}e^{i\alpha x}W(x)dx
=\tfrac12\Xi(\alpha)=0,                                 \tag{9}
\]

using L908(1), which holds for complex alpha. Thus (7) is also
minus the upper-end primitive. Equivalently, for every such z,

\[
U_\alpha(z)=\int_0^\infty e^{-i\alpha s}W(z-s)ds
          =-\int_0^\infty e^{i\alpha s}W(z+s)ds.           \tag{10}
\]

These are absolute integrals for each fixed complex alpha.
Reality of alpha, unit-modulus factors, simplicity and numerical
root enclosures have not been used.

Define the finite positive constant

\[
C_B=\int_0^\infty
     e^{(B+9/2)s-c(e^{2s}-1)}ds
=\frac{e^c}{2}\int_1^\infty t^{B/2+5/4}e^{-ct}dt<\infty.
\tag{11}
\]

The last integral converges because exponential decay dominates each
fixed real power. For x<=0 use the first integral in (10), and for
x>=0 the second. In either case the real part of the W argument
has absolute value r+s. Since exp(2r)>=1, (5) and
|exp(+/-i alpha s)|<=exp(Bs) give the uniform bound

\[
|U_\alpha(x+iy)|\le4\pi^2 C_B e^{9r/2-c e^{2r}}
\quad(|y|\le1/4).                                      \tag{12}
\]

For clarity, the additional factor under the s integral is
exp((B+9/2)s-c exp(2r)(exp(2s)-1)), at most the integrand of
(11). This verifies the bound for all r>=0, including the joining
point x=0 and arbitrarily large fixed |Im alpha|.

**Full image bounds and the exact Fourier weight.** Extend the
L-image by

\[
G_\alpha(z)=-i(U_\alpha'(z)-q(z)U_\alpha(z))
=-\alpha U_\alpha(z)-iW(z)+iq(z)U_\alpha(z).
\]

This is holomorphic in the open strip and agrees with the prescribed
G_alpha on the real line. From (5) and (12), putting

\[
K_\alpha=4\pi^2\left[1+(|\alpha|+24\pi)C_B\right],
\]

we obtain on the entire closed strip

\[
|G_\alpha(x+iy)|\le
K_\alpha e^{13r/2-c e^{2r}}.                             \tag{13}
\]

This majorant is in both L1(dx) and L2(dx), and tends to zero
at both ends, uniformly in y. In particular, all horizontal traces
used next are genuine L1 and L2 functions, with the explicit bound

\[
\int_{\mathbb R}|G_\alpha(x+iy)|^2dx
\le K_\alpha^2\int_1^\infty t^{11/2}e^{-2ct}dt<\infty.
\tag{14}
\]

This follows by squaring (13), splitting into two half-lines, and
substituting t=exp(2r); no finite-tail truncation is involved.

For fixed real k and 0<=y<=1/8, apply Cauchy's theorem to
G_alpha(z)exp(-ikz) on the rectangle with horizontal sides at
heights 0 and y and endpoints +/-T. The vertical integrals tend
to zero by (13), since |exp(-ikz)|<=exp(|k|/8) there. Both
horizontal limits converge absolutely. The orientations and the
factor exp(-ik(x+iy))=exp(ky)exp(-ikx) therefore give

\[
\mathcal F\big(G_\alpha(\,\cdot+iy)\big)(k)
=e^{-ky}\mathcal F G_\alpha(k)\qquad(k\in\mathbb R).       \tag{15}
\]

This identity is proved for the L1 transforms pointwise. By the
L1/L2 compatibility and Plancherel in the cited Teschl Theorem7.5,
it is also the equality of the corresponding L2 transforms.
Taking y=1/8 in (15) and applying Plancherel to that trace proves
(1), with the finite upper bound (14). Squaring exp(-k/8)
produces exactly exp(-k/4), the required form weight. We have not
replaced it by the stronger operator-domain weight exp(-k/2).

Finally any finite linear combination of the G_alpha belongs to Q:
both its unweighted L2 norm and its weighted Fourier L2 norm are
finite by the triangle inequality. This retains every complex-zero
generator. The proof establishes no orthogonality or pair symmetry.
It is a direct application estimate for the known form, classified
as REPRODUCTION, with no claim of originality beyond the inspected
sources. The independent symmetry and main positivity gaps remain. ∎

### Independent critical audit, 9 November 2026 (step161)

The audit passes without changing the hypotheses, constants or
conclusion. This is verification of the local application to a known
form, classified REPRODUCTION, not new source-level mathematics or
pair symmetry. The prior spectral/Fourier assessment is reused;
neither Ahmed's formal translation nor a new strip-space theorem is
imported. The following checks cover the full series, both endpoints
and the precise form domain.

**Denominator and strip.** The series (2) is holomorphic on S because
every compact subset has Re(pi exp(2z)) bounded below by a positive
number, including compacts with negative real part. Its fixed-order
derivatives have summable polynomial-times-Gaussian majorants. Both
W(z) and W(-z) are holomorphic on the same connected S and agree on
the real axis by L906, so the identity theorem applies. The smaller
closed strip |Im z|<=1/4 lies strictly inside S; the boundary estimates
do not require evaluating the theta series at |Im z|=pi/4.

For x>=0, R>3 gives |2v-3|>=2R-3>=R and
|2n^4v^2-3n^2v|<=3n^4R^2. Also a>=7R/8>2. Independently
checking (3), L906's strict e^3>20 gives b2<16/400=1/25,
and the consecutive ratio for n>=2 is at most
(3/2)^4 exp(-10)<81/128000<1/1000. Summing the whole geometric
majorant gives sum b_n<40/999, with 3 sum b_n<40/333<1/8
because 320<333. This is a relative bound against the nonzero first
term, so the reverse triangle inequality proves the lower bound in
(4); the upper bound follows from 3(1+40/999)<4. There is no
unexamined finite interval in x or omitted tail in n.

Differentiating (2) gives exactly P_1 as printed. At |v|>=3,
|P_1(v)|<=(4+5+5/6)|v|^3<10|v|^3. For its full n>=1
series the ratio is at most 64 exp(-6)<4/25, hence its sum
is at most 25/21<2. The quotient bound uses
20/(7/8)=160/7<24. Reflection sends x+iy to -x-iy in the same
strip and gives W'(-z)=-W'(z), so both the nonvanishing conclusion
and the bounds (5) hold for x<=0 as well. A positive lower bound
uniform in x is neither asserted nor needed.

**Complex cancellation and both primitive tails.** For alpha=A+ib,
|exp(i alpha (x+it))|=exp(-bx-At). On x=+/-T this is at most
exp(|b|T+|A|/4), exactly the factor used in (8). Combined with
(5), it makes each vertical side tend to zero, uniformly in its
height. The same full envelope makes the horizontal integrals
absolutely convergent. Thus the finite rectangles legitimately yield
(7) and (9), including negative y. The normalization from L908(1)
is Xi(alpha)/2 for every complex alpha; its nonzero scalar cancels
at an exact zero without assuming alpha real. The source's inconsistent
printed coefficient and L908's step154 addition are not used.

In (7), substituting z-s for the integration variable yields the
first integral in (10). Zero total integral yields the minus sign
in the second, with substitution z+s. Their exponential factors
have modulus at most exp(Bs), with no unaccounted factor depending
on x or y: exp(-i alpha z) cancels the common endpoint factor.
For the appropriate endpoint, |Re(z+/-s)|=r+s. Factoring out
exp(9r/2-c exp(2r)) leaves precisely the integrand bounded in
(11). The substitution t=exp(2s) gives exponent
(B+9/2)/2-1=B/2+5/4. This proves the finite C_B and (12),
including x=0, without a uniform-in-alpha claim.

**Image and Fourier-domain membership.** From D=-i d/dx and
U'=-i alpha U+W, the image is -alpha U-iW+iqU, with the
signs in the proof. Multiplication by q costs at most exp(2r);
the coefficient K_alpha and exponent 13r/2 in (13) therefore
bound all three terms. The full two-sided squared integral, with
t=exp(2r), is bounded by
K_alpha^2 integral_1^infinity t^(13/2-1) exp(-2ct) dt,
which is exactly (14); the two half-lines cancel the substitution's
factor 1/2. The unsquared majorant is also integrable. This supplies
both unweighted L2 membership and genuine L1/L2 horizontal traces.

For each fixed real k the vertical sides in the last rectangle are
bounded by a constant times exp(|k|/8) times the vanishing envelope
(13). The contour orientation gives
integral G(x) exp(-ikx) dx = exp(ky) integral G(x+iy) exp(-ikx) dx,
so the sign in (15) is negative. There is no interchange with a
k integral here: the identity is first proved pointwise for the L1
transforms. Their agreement with the L2 transforms, and Plancherel
for the already L2 trace, then establish weighted integrability.
At y=1/8 the squared multiplier is exp(-k/4), exactly the weight
in the squared norm of exp(-P/8)G. This proves membership in Dom(M^(1/2)); it does
not require assuming membership in Dom(M) or using a formal complex
translation of arbitrary L2 functions.

The finite-span conclusion follows from the two L2 triangle
inequalities. Every retained complex zero is covered, with constants
allowed to depend on it; repeated zeros add no new generators under
L907's definition. No generalized eigenvectors, completion, symmetry
or mixed-positivity assertion follows. L906, L907 and L908 are exactly
the direct local inputs in the unchanged DAG row; L909 is a contrast,
not an input to this audit or the domain proof.

## Mathlib

Full matching coverage for this theta-specific domain inclusion is
unchecked. Supporting coverage for holomorphic contour deformation,
the Fourier shift identity and spectral quadratic-form domains is
also unchecked; no absence claim is made. The proof uses the stated
standard complex-analysis theorems and the cited Fourier/spectral
inputs, not a Mathlib implementation.
