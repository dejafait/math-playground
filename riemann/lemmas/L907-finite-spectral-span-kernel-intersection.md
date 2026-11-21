# L907: trivial kernel intersection on the finite complex-zero span

## Hypotheses

Use the positive smooth theta function w and the differential operators
from L906, on (0,infinity):

\[
\delta=t\frac{d}{dt},\qquad D=\frac{\delta}{i},\qquad
\phi=-\log w,\qquad Lf=Df+(D\phi)f.
\]

Let Z be the complete set of complex zeros denoted by Xi(alpha)=0
in Hedenmalm, *Spectral interpretation of Riemann zeta zeros*,
[arXiv:2606.17494v1](https://arxiv.org/pdf/2606.17494v1),
Theorem 3.3.3 and Section 4.2, p7. With powers defined using the real
logarithm on (0,infinity), put

\[
u_\alpha(t)=t^{-i\alpha}\int_0^t y^{i\alpha}w(y)\,\frac{dy}{y},
\qquad
H_{\rm finite}=\operatorname{span}_{\mathbb C}
       \{u_\alpha:\alpha\in Z\}.
\]

The span means finite linear combinations, with all complex zeros
retained. Repeated zeros specify the same displayed function; no
parameter derivatives or generalized eigenfunctions are adjoined.
The kernel of L is taken in C^infinity((0,infinity); C).
No RH, simplicity, positive metric, completion or inverse is assumed.

## Conclusion

\[
\ker L\cap H_{\rm finite}=\{0\}.
\]

Thus L is injective on this specified finite span. This removes the
kernel-based representative ambiguity on that domain only. It does
not give a positive symmetric realization or any actual-Xi mixed sign.
In particular, it neither overturns L906's obstruction on
V=span{w,Dw} nor asserts injectivity on a completion of H_finite.

## Proof

**Source use and scope.** The integral is exactly the source's
definition on p7; its real-parameter differential identity is (3.3.2),
p5. The complex-parameter integral and differential identity are
justified below because that complex proof is omitted in the source.
The full zero/boundary-value characterization and any Mellin-to-Xi
normalization are unnecessary here and are not imported as proved.
L906 supplies positivity, smoothness and the complete estimates

\[
|\delta^k w(t)|\le C_k t^{2k+9/2}e^{-\pi t^2}\quad(t\ge1),
\qquad
|\delta^k w(t)|\le C_k t^{-2k-9/2}e^{-\pi/t^2}\quad(0<t\le1),
\tag{1}
\]

for every integer k>=0 and finite constants C_k. The proof uses these
estimates, not the source's unaudited printed small-t asymptotic.

**The complex integral identity.** Fix alpha=a+ib in Z, with a,b real.
For 0<y<=1 the absolute value of its integrand is bounded by

\[
|y^{i\alpha}w(y)/y|
\le C_0 y^{-b-11/2}e^{-\pi/y^2}.
\]

Its integral from 0 to r<=1, after z=1/y, is at most

\[
C_0\int_{1/r}^{\infty}z^{b+7/2}e^{-\pi z^2}\,dz<\infty.
\]

This holds for every fixed real b. On each compact subinterval of
(0,infinity) the integrand is smooth. Splitting the integral at a fixed
positive point and applying the fundamental theorem of calculus shows
that the integral, and hence u_alpha, is smooth there. It gives

\[
\delta u_\alpha=-i\alpha u_\alpha+w,
\qquad
Du_\alpha=-\alpha u_\alpha+w/i.
\tag{2}
\]

No integral to infinity, parameter differentiation, uniformity in alpha
or zero simplicity is used.

**A hypothetical kernel vector forces finite invariance.** Since w>0,
the product and quotient rules give

\[
Lf=Df-\frac{Dw}{w}f=wD(f/w).
\tag{3}
\]

Thus Lf=0 if and only if f=cw for a complex constant c: a function
with zero ordinary derivative is constant on the connected interval
(0,infinity). Suppose that some nonzero f in H_finite has Lf=0.
Choose a finite representation f=sum_(j=1)^n c_j u_(alpha_j) and set

\[
F=\operatorname{span}_{\mathbb C}
       \{u_{\alpha_1},\ldots,u_{\alpha_n}\}.
\]

By (3), f=cw with c!=0, so w belongs to F. Equation (2) now gives
D(F) subset F. Consequently A=D restricted to F is a genuine complex
linear endomorphism of the finite-dimensional space F, with
1<=d=dim F<=n. No independence of the listed generators is asserted
or needed, and no operator using L^{-1} has been defined.

Apply the standard **Cayley–Hamilton theorem** to A: its characteristic
polynomial p(z)=det(z I-A) is monic of degree d and satisfies p(A)=0.
In particular p is nonzero. Because D preserves F, the powers of A
are the restrictions of the corresponding powers of D. Hence

\[
p(D)w=0.
\tag{4}
\]

This is the only finite-dimensional theorem imported; it requires
neither diagonalizability nor real or distinct eigenvalues.

**Logarithmic Schwartz estimates.** Define W(x)=w(e^x) for real x.
Repeated application of the chain rule gives
W^(k)(x)=(delta^k w)(e^x). Both halves of (1) therefore yield

\[
|W^{(k)}(x)|\le C_k
 \exp\big((2k+9/2)|x|-\pi e^{2|x|}\big)
\quad(x\in\mathbb R).
\tag{5}
\]

For each pair of nonnegative integers N,k, the logarithm of
(1+r)^N exp((2k+9/2)r-pi e^(2r)) tends to minus infinity as r tends
to infinity: the negative exponential term dominates both the linear
and logarithmic terms. This continuous function is bounded for r>=0.
Equation (5) thus proves every Schwartz seminorm bound

\[
\sup_{x\in\mathbb R}(1+|x|)^N|W^{(k)}(x)|<\infty.
\tag{6}
\]

In particular, each derivative is integrable (use N=2) and tends to
zero at both ends (use N=1). Also W(0)=w(1)>0 by L906.
The logarithmic change of variables sends D to (1/i)d/dx; thus (4)
becomes

\[
p\left(\frac1i\frac{d}{dx}\right)W=0.
\tag{7}
\]

**Fourier contradiction.** Use the convention

\[
\widehat W(\xi)=\int_{\mathbb R}W(x)e^{-2\pi i x\xi}\,dx.
\]

The standard inputs are Tao, *245C, Notes 2: The Fourier transform*
(6 April 2009), [Exercise 30 and Remark 31, Definition 32,
Exercise 38, and Fourier inversion (11)](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/).
They give Fourier differentiation, preservation of the Schwartz class
and pointwise inversion on that class. Conditions (6) verify the full
Schwartz hypothesis. In particular, every derivative used below is in
L1 and satisfies the fundamental theorem of calculus on finite
intervals. Its vanishing endpoint values remove the boundary terms.
Integration by parts therefore gives, with the precise convention,

\[
\widehat{W^{(k)}}(\xi)=(2\pi i\xi)^k\widehat W(\xi),
\qquad
\widehat{((1/i)d/dx)^kW}(\xi)=(2\pi\xi)^k\widehat W(\xi).
\]

Applying this to the finite polynomial in (7) yields

\[
p(2\pi\xi)\widehat W(\xi)=0\quad(\xi\in\mathbb R).
\tag{8}
\]

Since p is nonzero, it has only finitely many real roots. Equation (8)
forces W-hat to vanish off the corresponding finite set of real xi.
The Fourier transform is Schwartz, hence continuous, so it vanishes
at that finite set as well by continuity from its dense complement.
Fourier inversion now gives

\[
W(x)=\int_{\mathbb R}\widehat W(\xi)e^{2\pi i x\xi}\,d\xi=0
\quad\text{for every real }x.
\]

This contradicts W(0)>0. The hypothetical nonzero kernel vector cannot
exist, proving the stated intersection.

**Qualifications.** This is a local specialization of standard
Cayley–Hamilton and Fourier results with the audited theta estimates,
not a claim of progress beyond the literature checked or of a new
real-spectrum construction. The proof addresses finite spans only;
no assertion about generalized eigenfunctions, infinite sums, closure,
completeness or spectral multiplicities follows. Positivity of w is
not a positive symmetric form for the operator pair. Neither such a
form nor mixed positivity is proved. The zero set is retained exactly
as specified, and its definition never supplies a sign assumption. ∎

### Independent critical audit, 8 November 2026 (step148)

The audit passes for the stated finite span, with no change to the
theorem or its hypotheses. The version-1 source's (3.3.2), kernel
reduction in Theorem 3.3.1, complex integral in Theorem 3.3.3 and
finite-span definition in Section 4.2 were checked in the primary
[HTML](https://arxiv.org/html/2606.17494v1). The latter includes possible
nonreal zeros. The displayed integral matches the local definition.
The proof does not import the omitted complex boundary-value proof,
the printed endpoint asymptotics or any Mellin normalization.

For fixed alpha=a+ib, |y^(i alpha)|=y^(-b). Multiplying the k=0
small-y bound by y^(-b-1) gives exactly y^(-b-11/2). Under z=1/y,
the Jacobian contributes z^(-2), giving z^(b+7/2), with the limits
reversed. A Gaussian dominates this fixed real power at infinity,
so the lower-end integral is absolutely convergent for every such
alpha. On each compact positive interval it is a constant plus an
ordinary smooth integral. Thus the FTC and product differentiation
used in (2) do not differentiate an improper endpoint or a parameter.
Division by i sends -i alpha to -alpha, confirming both signs in (2).
No common bound over the zero set is needed for a finite combination.

Equation (3) holds in the full smooth domain because w is positive.
The connected positive half-line makes its kernel exactly Cw.
Under the contradiction hypothesis, the nonzero kernel vector f=cw
has c!=0; hence w=f/c lies in that very same finite span F. Only at
this point is D(F) subset F asserted. Applying (2) to its generators
establishes this inclusion even when they are dependent or repeated.
The dimension d is positive because w!=0 and finite because the
generating list is finite. Cayley-Hamilton therefore applies to an
actual endomorphism A of F; its monic characteristic polynomial is
nonzero. Inductively A^j w=D^j w for every j, so (4) follows without
an inverse, diagonalization or a real-spectrum premise. There is no
assertion that D preserves H_finite absent the contradiction hypothesis.

The chain rule sends delta^k w to W^(k), without any additional
coefficient. Substitution t=e^x in the two complete L906 estimates
gives (5) with |x| at both ends. For each fixed N,k, the logarithm
of its weighted right side is
N log(1+r)+(2k+9/2)r-pi e^(2r), which tends to minus infinity.
It is continuous on r>=0 and thus bounded above. This verifies
every seminorm in (6), not merely the first d derivatives. Taking
N=2 proves absolute integrability of each W^(m), and N=1 proves
its vanishing at both infinities.

In particular the improper FTC required by Tao's Exercise 30 also
holds, not just its finite-interval version. For any integer m>=0
and finite a<x, smoothness gives

\[
W^{(m)}(x)-W^{(m)}(a)=\int_a^x W^{(m+1)}(s)\,ds.
\]

Letting a tend to minus infinity is justified by W^(m)(a)->0 and
W^(m+1) in L1, and yields
W^(m)(x)=integral_(-infinity)^x W^(m+1)(s) ds at every x.
On a finite interval [a,b], integration by parts against
exp(-2pi i x xi) has boundary term
[W^(m)(x)exp(-2pi i x xi)]_a^b and integral coefficient +2pi i xi.
Both boundary terms vanish as the endpoints tend separately to their
infinities; both integrals converge absolutely. Iteration gives the
stated derivative multiplier, and division by i gives exactly 2pi xi.
Only a finite polynomial is transformed; no infinite interchange occurs.

The cited [Tao Notes 2](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/)
Exercise 30/Remark 31, Definition 32, Exercise 38, and inversion (11)
were checked again, including the Gaussian inversion argument using
Exercises 40-42. Their hypotheses are met by the preceding checks.
The nonzero complex polynomial p has finitely many real roots;
p(2pi xi) has a finite real zero set as well. Its complement is dense.
Thus (8) and continuity of W-hat imply zero everywhere, including at
those roots regardless of multiplicity. Pointwise Schwartz inversion,
with the opposite sign in its exponent, gives W=0 everywhere,
contradicting the independently established W(0)=w(1)>0.

No failed implication or additional hypothesis was found. Writing out
the improper FTC above makes an existing implication explicit; it does
not repair a false assertion or strengthen the conclusion. The sole
local mathematical input remains L906. This is local verification of
a standard-theorem specialization, not progress beyond the checked
literature. The V-domain obstruction, missing metric and symmetry,
completion questions and actual-Xi mixed-positivity gap all remain.

## Mathlib

The reused assessment inspected the supporting Cayley–Hamilton
statements
[LinearMap.aeval_self_charpoly](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Charpoly/Basic.html#LinearMap.aeval_self_charpoly)
and
[LinearMap.charpoly_monic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Charpoly/Basic.html#LinearMap.charpoly_monic).
Their finite-free-module setting applies to the finite-dimensional
complex vector space F. Full matching coverage for this theta-domain
intersection is unchecked. Supporting Fourier/Schwartz implementation
coverage is also unchecked; no absence claim is made. The proof uses
the cited standard theorems and does not depend on a Lean implementation.
