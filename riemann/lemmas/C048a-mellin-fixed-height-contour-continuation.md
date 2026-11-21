# Corollary C048a: the fixed-height theta-Mellin contour prerequisite

## Hypotheses

Use the actual theta kernel, with the normalization of L019 and L048,

\[
 \Phi(z)=\sum_{m\ge1}(4\pi^2m^4e^{9z/2}-6\pi m^2e^{5z/2})
                  e^{-\pi m^2e^{2z}},\qquad K=2\Phi\quad\hbox{on }\mathbb R.
\]

Initially let \(I(p)=2\int_0^\infty u^{2p-1}\Phi(u)\,du\) for
\(\Re p>0\). Powers on nonreal paths use the principal logarithm.
Write \(\Phi(z)=\sum_{n\ge0}c_nz^{2n}\) near zero. Define

\[
 \mathcal S=\{p:r=|p|\ge e^{12},\ L=\log r,
                      \Re p\ge-r/(4L)\}.
\]

The source being audited is K. Kawano, *Logarithmic Inequalities of
Arbitrary Order for the Riemann Xi Coefficients*,
[Preprints.org 202611.0383v1, posted 4 November 2026](https://www.preprints.org/manuscript/202611.0383/v1),
(4)-(5), Section5.1 (25), and the first two proof paragraphs of
Lemma5.1. Only their branch/contour prerequisite is at issue. No
source remainder bound, zero exclusion, inverse-density sign or
certificate is assumed. The unchanged SPECIALIZE assessment1621
approved this audit before step1622.

## Conclusion

For \(p\in\mathcal S\), the principal value
\(w=W_0(2p/\pi)=U+iV\) satisfies \(U>0\), \(|V|<\pi/2\),
and \(V\) has the sign of \(\Im p\). These inequalities hold on
open neighborhoods of the sector points. Thus \(y=V/2\) is an
admissible theta-strip height, including the sector's closed boundaries.

For each **fixed** \(0<y<\pi/4\), put \(a=\min(y,1/4)\). The
following equality holds meromorphically for every complex \(p\):

\[
\begin{split}
 I(p)={}&\sum_{n\ge0}\frac{c_n(ia)^{2p+2n}}{p+n}
       +2\int_{ia}^{iy}z^{2p-1}\Phi(z)\,dz\\
       &+2\int_0^\infty(x+iy)^{2p-1}\Phi(x+iy)\,dx.       \tag{1}
\end{split}
\]

The finite segment is oriented upwards and is zero if \(a=y\).
The two integrals in (1) are entire in \(p\). The series is locally
normally convergent off the nonpositive integers; its residue at
\(p=-n\) is \(c_n\). Such a pole is actual exactly when \(c_n\ne0\).
The corresponding downward formula holds for negative fixed \(y\).

This continuation agrees exactly with source (25):

\[
 16^pI(p)=\sum_{n\ge0}\frac{c_n16^{-n}}{p+n}
   +\int_{1/4}^\infty\frac{2\Phi(u)}u
                       e^{2p\log(4u)}\,du.              \tag{2}
\]

One may therefore evaluate (1), after proving it at fixed height,
at \(y=\Im W_0(2p/\pi)/2\) for each \(p\in\mathcal S\) in the
upper half-plane; conjugation treats the lower half-plane. At \(y=0\)
the sector point is positive real and the unshifted integral applies.
There are no possible poles in \(\mathcal S\).

This validates the nominated prerequisite as REPRODUCTION, without a
correction to the source contour statement. It does not validate any
quantitative part of Lemma5.1, including its stronger Lambert bounds,
relative saddle errors, or zero count. It gives no mixed-sign bridge
or advance beyond the source's stated mathematics.

## Proof

### Kernel applicability and the earlier local continuation

L799's complex-convergence proof and audit517 establish holomorphy of
exactly this series on \(\mathcal T=\{|\Im z|<\pi/4\}\), independently
of its later saddle-domain hypotheses. Explicitly, for compact
\(E\subset\mathcal T\),
\(d_E=\min_E\Re(\pi e^{2z})>0\), and the summands are bounded by
\(C_E(m^4+m^2)e^{-d_Em^2}\). This summable bound verifies the
normal-convergence hypothesis actually used here. No real-axis tail
bound is being extended to a complex strip without justification.

L019's differentiated series is twice this kernel. L048 constructs
the same real kernel for all real arguments by compact termwise
differentiation of \(A(u)=e^{u/2}\psi(e^{2u})\), and proves its
evenness from the theta transformation. Only that evenness is used,
not L048's curvature assertion. The identity theorem, applied to
\(\Phi(z)-\Phi(-z)\) on the connected strip, gives complex evenness.
Normal convergence of the real-coefficient exponential series also
gives conjugation symmetry. Hence the coefficients \(c_n\) are real
and the odd Taylor coefficients vanish.

For any \(1/4<\rho<\pi/4\), Cauchy's coefficient estimate yields
\(|c_n|\le M_\rho\rho^{-2n}\), where
\(M_\rho=\max_{|z|=\rho}|\Phi(z)|<\infty\). No numerical value of
this constant or source (26) is needed.

The fixed-ray continuation is already proved in L804, equations
(2)-(4), and audited in step538. Its symbol \(P\) is precisely
\(\Phi\); its initial exponent is \(2s\). Apply only that
fixed-ray portion, valid for every independent \(|y|<\pi/4\), with
\(s=p-1/2\) and multiply its integral by 2. Using evenness gives

\[
 2\int_0^{ia}z^{2p-1}\Phi(z)\,dz
       =\sum_{n\ge0}\frac{c_n(ia)^{2p+2n}}{p+n}
                         \quad(\Re p>0).               \tag{3}
\]

The factor 2 cancels the monomial denominator's factor 2. This is a
reuse of L804's continuation, not a new endpoint theorem; its saddle,
outward height, normalized endpoint bound and domain \(D\) are not
being imported. For clarity, the needed normal convergence follows
from \(a/\rho<1\), bounded \(|(ia)^{2p}|\) on compact \(p\)-sets,
and \(|p+n|\ge n/2\) for all sufficiently large \(n\) uniformly
on such sets. Near \(-n\), the series with its nth term removed is
holomorphic. That term has residue \(c_n(ia)^0=c_n\). This checks
the exponent change, orientation and pole normalization explicitly.

### Principal Lambert branch throughout the closed sector

The standard branch input is
[NIST DLMF4.13.1 and the principal-branch domain paragraph](https://dlmf.nist.gov/4.13):
\(W_0(z)e^{W_0(z)}=z\), \(W_0\) is analytic off
\((-\infty,-e^{-1}]\), and it is positive real for positive real
input. Only these properties are imported; no asymptotic expansion
or sector estimate is assumed.

Fix \(r\ge e^{12}\), set \(R=2r/\pi\), and put
\(\alpha=\arcsin(1/(4L))\), \(\theta_* =\pi/2+\alpha<\pi\).
The upper part of the sector at this radius has precisely
\(0\le\theta=\arg p\le\theta_*\). The arc
\(R e^{i\theta}\) stays off the branch cut. Start at
\(w(0)=W_0(R)>0\). Differentiating its defining identity at zero
gives \(w'(0)=iw(0)/(1+w(0))\); thus for small positive \(\theta\),
\(U>0\) and \(0<V<\pi/2\).

Suppose there is a first exit from this region before or at
\(\theta_*\). Continuity on the compact arc ensures that at that
exit \(U\ge0\) and \(0\le V\le\pi/2\). There are three possibilities.

* If \(V=0\), then \(we^w\) is positive real (or zero), impossible
  for \(0<\theta\le\theta_*<\pi\).
* If \(U=0\), then \(|we^w|=|w|=V\le\pi/2\), whereas
  \(R=2r/\pi>\pi/2\). For example \(e^{12}>13\) and
  \(3<\pi<4\) already imply this strict modulus inequality.
* If \(V=\pi/2\) and \(U>0\), then
  \(U+\log|w|=\log R<L\), so \(U<L\), since \(|w|\ge\pi/2>1\).
  In this case the argument of \(we^w\), with no wrapping, is
  \[
    \pi/2+\arctan(\pi/(2U))
       >\pi/2+\arctan(\pi/(2L))>\pi/2+\alpha.
  \]
  The final comparison is exact: \(\tan\alpha=1/\sqrt{16L^2-1}
  <1/(3L)<\pi/(2L)\) for \(L\ge12\). This contradicts
  \(\theta\le\theta_*\).

Thus no exit occurs, including at the closed angular boundary. At
\(\theta=0\), \(V=0\); otherwise \(V>0\). Complex conjugation of
\(W_0\), obtained from its real values and the identity theorem,
handles negative angles. In particular the chosen height is strictly
inside the theta strip. Analyticity of \(W_0(2p/\pi)\) and the strict
inequalities provide open neighborhoods at every sector point,
including \(r=e^{12}\). No uniform clearance at infinity is asserted.

### Full horizontal decay and the initial contour equality

Fix \(0<y<\pi/4\) independently of \(p\), and let
\(c=\cos(2y)>0\). On \(z=x+it\), \(x\ge0\), \(0\le t\le y\),
the explicit series gives the bound

\[
 |\Phi(x+it)|\le C_c e^{9x/2}e^{-\pi c e^{2x}},\qquad
 C_c=\sum_{m\ge1}(4\pi^2m^4+6\pi m^2)e^{-\pi c(m^2-1)}<\infty. \tag{4}
\]

Indeed \(\cos(2t)\ge c\), \(e^{5x/2}\le e^{9x/2}\), and
\(e^{2x}\ge1\); factoring out the first exponential gives (4).
This bound is on the full theta sum and on the full far vertical
segment, not just on a saddle neighborhood.

For a compact parameter set \(B\subset\mathbb C\), the principal
power satisfies \(|z^{2p-1}|\le C_B(1+x)^{N_B}\) when \(x\ge1\),
\(0\le t\le y\), \(p\in B\). This follows from
\(|z^{2p-1}|=|z|^{2\Re p-1}e^{-2\Im p\arg z}\), bounded imaginary
parts and \(|\arg z|\le\pi/2\). Together with (4), it supplies an
integrable majorant and a far-vertical bound tending to zero,
locally uniformly in \(p\).

For \(\Re p>0\), apply Cauchy's theorem in the rectangle with
vertices \(0,X,X+iy,iy\), removing a quarter disk of radius
\(\epsilon<y\) at zero. The integrand is
\(f_p(z)=2z^{2p-1}\Phi(z)\). The contour and its interior away
from zero lie in the theta strip and principal-log domain. On
compact \(B\subset\{\Re p>0\}\), with \(b=\min_B\Re p>0\),
the circular-arc integral is \(O_B(\epsilon^{2b})\), since \(\Phi\)
is bounded near zero. The initial vertical integral converges for
the same reason. The right vertical integral tends to zero by (4).
Taking \(\epsilon\downarrow0\), then \(X\to\infty\), gives

\[
 I(p)=2\int_0^{iy}z^{2p-1}\Phi(z)\,dz
       +2\int_0^\infty(x+iy)^{2p-1}\Phi(x+iy)\,dx.      \tag{5}
\]

Both paths on the right have their displayed positive orientations.
In particular the origin term has a plus sign and is not discarded.

### Continuation, agreement with (25), and endpoints

Split the first integral of (5) at \(ia\). Equation (3) continues
its initial part. The remaining finite segment avoids zero and the
logarithm cut, so its integral is entire in \(p\). The horizontal
integral is also entire: its bounded initial part is separated from
zero by \(y>0\), while (4) proves locally uniform convergence of its
tail for every compact parameter set. The parameter-integral theorem
therefore applies on all of \(\mathbb C\).

Independently, splitting the original real integral at \(b_0=1/4\)
and integrating its normally convergent Taylor series gives
\(\sum c_n b_0^{2p+2n}/(p+n)\) plus the entire real tail. Multiplying
by \(16^p\), and using \(16^pb_0^{2p}=1\), proves (2). The same
Cauchy-coefficient bound proves its local meromorphic convergence.
Consequently (1) and (2) are meromorphic functions on the whole plane
and agree on the open half-plane \(\Re p>0\). The meromorphic
identity theorem makes them equal everywhere, with matching principal
parts. No extra entire term or regularization constant is available.

There is no change of height in this identity-theorem argument. At
a selected nonreal sector point, first fix its numerical height
\(y=V/2\), apply the meromorphic identity just proved, and only then
evaluate at that \(p\). The expression so evaluated equals \(I(p)\);
no holomorphy of the separate moving-height summands is needed or
asserted. In a neighborhood of that point the same fixed height may
be retained if a holomorphic representation is needed.

At \(p=-r<0\) membership in \(\mathcal S\) would imply
\(1\le1/(4\log r)\), impossible when \(\log r\ge12\). Zero is also
excluded. Thus none of the possible poles is evaluated. If \(V=0\)
in the sector, the branch proof shows \(p>0\), where no deformation
is needed. Locally near such a positive real point, within
\(\Re p\ge b>0\), the original short vertical integral is
\(O(y^{2b})\), so there is no additional zero-height origin term.
This is local compatibility, not a uniform claim at arbitrarily
negative real parts. Conjugating (1) gives the downward contour,
principal powers and the correct orientation for the lower half-plane.
All asserted cases are now covered.

The standard analytic inputs are the Weierstrass M-test, Cauchy's
integral theorem and coefficient estimate, the parameter-integral
theorem under local compact domination, and the meromorphic identity
theorem. The fixed-ray implementation and its standard Mellin
subtraction citations are reused from L804. The newly checked
specialization is the present sector, complete contour, normalization
and agreement with source (25), rather than a general reproof of those
standard theorems. No numerical experiment is used.

## Mathlib

Full matching coverage for this sector-specific contour identity has
not been checked and is unknown. No absence or formal-verification
claim is made. L016 records supporting real-theta/Poisson summation
references; those do not by themselves provide the complex contour
or branch result. No particular Mathlib declaration is claimed to
cover this corollary. The independent bounds and convergence arguments
above are the informal verification evidence.
