# Corollary 645f: a synthetic three-moment boundary residual certificate

## Hypotheses

Retain exactly C645e's finite-family geometry. Explicitly, let

\[
 0<\delta<\tfrac12,\quad d=\tfrac32-\delta,\quad
 R=\tfrac32-\tfrac\delta2,\quad x=-d,\quad
 n\in\mathbb Z,\quad n\ge5,
\]
\[
 t_j=j/n\ (0\le j<n),\qquad
 B_n(z)=\prod_{j=0}^{n-1}\frac{R(z-it_j)}{R^2+it_jz}.
 \tag{1}
\]

Let \(Z\) consist of one, two or three distinct points and contain
\(x\). Each additional point \(a\) satisfies

\[
 |a-x|<\delta/8,\qquad -\tfrac32<\Re a<-1,
 \qquad |a|<R.
 \tag{2}
\]

Every point of \(Z\) avoids the grid \(\{it_j:0\le j<n\}\).
Let \(F\) be meromorphic on an open neighborhood of the closed disk
\(|z|\le R\). Its poles in that closed disk are **exactly** \(Z\),
all simple and all of residue one. Let \(P\) be holomorphic on an
open neighborhood of the closed disk, with

\[
                 P(it_j)=F(it_j)\quad(0\le j<n).
 \tag{3}
\]

The neighborhoods may depend on the data. Both \(Z\) and \(P\) may
depend on \(n\). There is no positivity, symmetry, separation,
degree bound on \(P\), derivative lower bound or actual-Xi hypothesis.

## Conclusion

Put \(E_n=\max_{|z|=R}|F(z)-P(z)|\), and for \(k=0,1,2\) put

\[
 M_k=B_n(x)\sum_{a\in Z}\frac{[n(a-x)]^k}{B_n(a)}.
 \tag{4}
\]

For \(k=0\), the polynomial weight is identically one, including
at \(a=x\). The exact identities, on the counterclockwise circle, are

\[
 M_k=\frac1{2\pi i}\int_{|z|=R}
       \frac{B_n(x)[n(z-x)]^k(F(z)-P(z))}{B_n(z)}\,dz.
 \tag{5}
\]

Every grid residue in (5) is zero, as verified below. In particular,

\[
 \boxed{\displaystyle
 E_n\ge\frac{1}{81R\,n^2(R^2+d^2)\,|B_n(x)|}.}
 \tag{6}
\]

The anchor factor in this expression is exactly

\[
 |B_n(x)|=
 \prod_{j=0}^{n-1}
 \frac{R\sqrt{d^2+(j/n)^2}}{\sqrt{R^4+d^2(j/n)^2}}.
 \tag{7}
\]

The loss after retaining that factor is precisely quadratic in \(n\)
in the evaluated common integral-weight cost used here. This is not
an optimality claim about (6) or about all possible contour weights.
It is a synthetic necessary boundary size, not a boundary upper bound,
an actual-Xi detector or an RH resolution candidate. An independent
proof audit on 1 November 2026 verified (5)--(17) and the complete
C645e application under exactly these hypotheses, without a
mathematical correction; its checks are recorded below.

## Proof

### Imported calculus and scope

Use the standard residue theorem and simple-pole rule in M. Beck
et al., *A First Course in Complex Analysis*,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
and the absolute integral inequality and ML bound in
[Section 6.2, Theorems 6.2.18 and 6.2.19, with (6.2.15) and
the parameterization statement 6.2.11](https://complexanalysis.org/web/sec_contour-integrals.html).
The online text is unversioned; the invocation-start
[SPECIALIZE assessment](../drafts/literature/2026-11-01-three-moment-contour-transfer.md)
records inspection of these statements and proofs on 1 November 2026.
The residue theorem sums all enclosed isolated singularities and
requires analyticity on the contour. The integral inequality retains
the whole boundary modulus. We import these theorems without reproof.

For comparison, the finite-Blaschke division argument in S. Zakeri,
*A Course in Complex Analysis*, author
[Notes and Comments, Section 8.3, after Example 8.33](https://zakerimath.com/CAbook/COM.html)
(unversioned, inspected in the same assessment), uses unit boundary
modulus for a holomorphic quotient. We do not apply a holomorphic
division bound to a residual with poles. Instead we check the exact
finite rational factors and retain all pole contributions in (5).

The local work is the applicability check, the grid removals and the
explicit polynomial-weight cost. The prior source comparison does
not identify an arbitrary holomorphic interpolating \(P\) with a
degree-constrained Hermite or Pade approximant. No such identification
or vanishing of its contour integral is used here. C645d's scalar
cancellation and C645b's factorwise-envelope stop remain valid in
their scopes; neither is a premise of this proof. C645c's product-rate
estimate is also not required: (7) is retained without approximation.

### 1. Rational factors, grid singularities and all genuine poles

The parameter bounds imply \(1<d<R<3/2\) and \(R>5/4\).
For \(|z|\le R\) and every grid parameter \(0\le t_j<1\),

\[
 |R^2+it_jz|\ge R^2-t_jR\ge R^2-R>0.
 \tag{8}
\]

Thus none of the denominators in (1) vanishes on the closed disk;
by compactness this remains true on some neighborhood. For \(t_j>0\)
the corresponding rational-factor pole is \(iR^2/t_j\), of modulus
\(R^2/t_j>R\); for \(t_j=0\) there is no such pole. Consequently
\(B_n\) is holomorphic near the disk, with precisely the distinct,
simple grid zeros there. Its reciprocal can have poles there only at
the grid. Explicitly,

\[
 B_n'(it_j)=\frac{R}{R^2-t_j^2}
       \prod_{\ell\ne j}
       \frac{Ri(t_j-t_\ell)}{R^2-t_\ell t_j}\ne0.
 \tag{9}
\]

Every denominator in (9) is positive since \(R^2>1\), and each
displayed numerator is nonzero by distinctness of the grid nodes.
This includes \(j=0\).

Write \(A=F-P\) and \(W_k(z)=[n(z-x)]^k\). The proposed integrand
is \(H_k=B_n(x)W_k A/B_n\). Since the grid avoids \(Z\), \(A\)
is holomorphic at every grid point. Before invoking (3), the complete
potential grid contribution to the residue sum is

\[
 \sum_{j=0}^{n-1}
 \frac{B_n(x)[n(it_j-x)]^k}{B_n'(it_j)}
             \bigl(F(it_j)-P(it_j)\bigr).
 \tag{10}
\]

Each term is defined by (9) and vanishes by (3). More than a residue
cancellation is true: locally \(A(z)=(z-it_j)a_j(z)\) with \(a_j\)
holomorphic, and \(B_n(z)=(z-it_j)b_j(z)\) with
\(b_j(it_j)=B_n'(it_j)\ne0\). Hence
\(H_k=B_n(x)W_k a_j/b_j\) is holomorphic there. Thus every grid
singularity is removable for all three weights, without discarding
any term or assuming a degree bound.

At \(a\in Z\), \(A(z)=1/(z-a)+h_a(z)\) with \(h_a\)
holomorphic. The grid avoidance and (8) give \(B_n(a)\ne0\), so

\[
 \operatorname{Res}_{z=a}H_k(z)
       =\frac{B_n(x)[n(a-x)]^k}{B_n(a)}.
 \tag{11}
\]

At the anchor these three residues are respectively \(1,0,0\).
For \(k=1,2\) the weight actually removes the anchor pole. Formula
(11) still gives its zero contribution correctly. At each other
point it is exactly the indicated weighted unit residue. There are
no other enclosed singularities: the hypotheses enumerate every pole
of \(F\), \(P\) is holomorphic, the weights are polynomials, and all
rational-factor singularities and grid removals have been checked.
The points of \(Z\), including \(|x|=d<R\), lie strictly inside.
The contour has no grid point or pole on it. The common neighborhood
of the closed disk therefore meets the residue theorem's hypotheses.
Its sum of (10) and (11) is exactly (5).

### 2. Unit boundary modulus and exact anchor factor

For \(|z|=R\) and real \(t\), direct multiplication gives

\[
 R^2|z-it|^2
   =R^4+R^2t^2-2R^2t\Im z
   =|R^2+itz|^2.
 \tag{12}
\]

In combination with (8), this proves \(|B_n(z)|=1\) on the
whole circle. At \(x=-d\), taking the modulus of each exact factor
gives (7). All factors are nonzero. In fact each is below one, because

\[
 R^4+d^2t_j^2-R^2(d^2+t_j^2)
       =(R^2-d^2)(R^2-t_j^2)>0.
\]

No real modulus is substituted for \(B_n\) in the residues; only the
boundary estimate and the final positive anchor size use moduli.

### 3. Evaluate the complete common polynomial-weight cost

The boundary residual is continuous, so \(E_n\) exists and is finite.
Parametrize the counterclockwise circle by \(z=Re^{i\theta}\),
\(0\le\theta\le2\pi\). Applying the imported absolute integral
inequality to (5), including the \(1/(2\pi)\) normalization and
\(|dz|=R\,d\theta\), gives

\[
 |M_k|\le R|B_n(x)|E_n A_k,\qquad
 A_k=\frac1{2\pi}\int_0^{2\pi}
                  n^k|Re^{i\theta}+d|^k\,d\theta.
 \tag{13}
\]

For comparison, the exact circle supremum of each weight is
\(n^k(R+d)^k\), attained at \(\theta=0\) (constant for \(k=0\)).
Thus the ordinary ML bounds, with no hidden factors, are

\[
 |M_0|\le R|B_n(x)|E_n,\quad
 |M_1|\le R|B_n(x)|E_n n(R+d),\quad
 |M_2|\le R|B_n(x)|E_n n^2(R+d)^2.
 \tag{14}
\]

We can evaluate a better **common** cost in (13) without leaving any
unknown norm in the certificate. The zeroth weight gives \(A_0=1\).
The triangle inequality gives \(A_1\le n(R+d)\). For the quadratic
weight the full integral is elementary:

\[
\begin{aligned}
 A_2&=\frac{n^2}{2\pi}\int_0^{2\pi}
              (R^2+d^2+2Rd\cos\theta)\,d\theta\\
    &=n^2(R^2+d^2).
\end{aligned}
 \tag{15}
\]

Since \(R,d>1\) and \(n\ge5\), we have
\(R^2+d^2>R+d>2\), and hence
\(A_0<A_2\) and \(A_1\le n(R+d)<n^2(R^2+d^2)=A_2\).
Consequently the **exact maximum of these three integral-weight
costs** is

\[
            \max_{0\le k\le2}A_k=n^2(R^2+d^2).
 \tag{16}
\]

Evaluating \(A_1\) separately is unnecessary for (16): its explicit
upper bound is already strictly below the computed \(A_2\). Thus
the cost of passing from the three contour identities to their
maximum is fully evaluated, with no unevaluated multiplier norm or
unproved removed term. Combining (13) and (16),

\[
 \max_{0\le k\le2}|M_k|
       \le R|B_n(x)|E_n n^2(R^2+d^2).
 \tag{17}
\]

Our geometry and unit residues meet all hypotheses of C645e (1)--(3),
including its allowance for arbitrarily close distinct poles and
unbounded scaled displacements. Its audited conclusion (4) is
\(\max_k|M_k|\ge1/81\). Applying it to (17) and dividing by the
strictly positive factor \(R|B_n(x)|n^2(R^2+d^2)\) proves (6).
This application, rather than any separate lower bound for one chosen
moment, handles the scalar cancellation permitted by C645d.

### Independent proof audit — 1 November 2026

This audit reused the invocation-start
[SPECIALIZE assessment](../drafts/literature/2026-11-01-c645f-boundary-certificate-audit.md)
and read both the complete proof above and C645e's full finite-product,
moment and uniformity proof. It verified the existing specialization,
not a stronger boundary estimate or a new general theorem.

* **Domain and rational factors.** The strict parameter ranges give
  \(1<d<3/2\), \(5/4<R<3/2\), and
  \(R-d=\delta/2>0\). For each \(j\), the lower bound in (8)
  is strictly positive. Solving the denominator equation gives
  \(z=iR^2/t_j\) for \(t_j>0\), outside the circle; at \(t_j=0\)
  the denominator is constant. Differentiating the vanishing factor
  at \(it_j\) gives exactly \(R/(R^2-t_j^2)\), and evaluating
  every other factor gives (9). No second numerator vanishes there.
  Compactness and the finite number of factors give a common open
  neighborhood on which their denominators do not vanish.
* **Local removals and exhaustive residue list.** Since no grid node
  is a pole of \(F\), (3) gives a holomorphic zero of \(F-P\)
  there. Dividing its local factorization by the simple-zero
  factorization of \(B_n\) removes the singularity, including when
  the residual is identically zero locally. Thus zero residues in
  (10) are supplemented by an actual removability proof. At each
  genuine pole the holomorphic multiplier has value
  \(B_n(x)[n(a-x)]^k/B_n(a)\); unit residue of \(F-P\) gives
  exactly (11). At \(x\) these are \(1,0,0\); multiplication by
  \(z-x\) or \((z-x)^2\) removes that pole for \(k=1,2\).
  All other possible singularities have been excluded. The full pole
  census and \(|a|<R\), not a presumed absence of additional poles,
  justify applying the residue theorem to precisely these terms.
* **Contour hypotheses and normalization.** The common neighborhood
  of the closed disk is enough: by compactness it contains a slightly
  larger disk, and its radius can also avoid all finitely many rational
  denominator zeros. Hence a simply connected domain for the cited
  residue theorem exists. The circle is counterclockwise and free of
  poles and grid zeros. The coefficient is \(1/(2\pi i)\), whose
  modulus is \(1/(2\pi)\); parameterization contributes precisely
  \(R\,d\theta\). No contour length or orientation factor is lost.
* **Boundary and anchor moduli.** Expanding both squares in (12)
  gives the same term \(-2R^2t\Im z\); this checks the sign in
  the denominator of (1). Thus every boundary factor has modulus
  one. At \(x=-d\), its numerator modulus is
  \(R\sqrt{d^2+t_j^2}\), its denominator modulus is
  \(\sqrt{R^4+d^2t_j^2}\), and their squared difference is the
  displayed positive product. This verifies (7) exactly, including
  \(j=0\), and confirms that all divisions by \(|B_n(x)|\) are
  legitimate. Residues retain the complex ratios throughout.
* **Weight costs.** The continuous boundary residual has a finite
  maximum because there are no boundary poles. The imported absolute
  integral inequality, via (6.2.15), bounds the integral by the full
  circle-average modulus, so (13) uses an integral rather than a
  supremum. Direct integration of
  \(|Re^{i\theta}+d|^2=R^2+d^2+2Rd\cos\theta\)
  gives (15). The triangle bound for \(A_1\) suffices:
  \(R^2+d^2>R+d>2\), so \(1<A_2\) and
  \(A_1\le n(R+d)<A_2\). This proves the exact maximum (16)
  without an exact evaluation of \(A_1\). The weaker supremum
  bounds (14) are consistent and not substituted into (17).
* **Full C645e input and uniformity.** Its product, anchor, grid,
  set sizes, unit residues and strict cluster restrictions coincide
  exactly with (1)--(4). Replaying its proof gives
  \(|q_j(h)-1|\le(656/375)|h|<2|h|\) and hence
  \(|A_n(u)-1|\le2|u|/(1-2|u|)\) for \(|u|<1/2\).
  At \(|u|\le1/8\) the latter is at most \(1/3\).
  For three points its identity
  \(M_2-(u+v)M_1+uvM_0=uv\) gives \(1/81\) whenever
  both displacement moduli are at least \(1/8\), including
  arbitrarily large ones. Otherwise a hypothetical maximum below
  \(1/81\) forces the second weight to have modulus greater than
  \(134/81\) and its displacement below
  \((29/162)/(134/81)=29/268<1/8\). Both weights would then be
  within \(1/3\) of one, forcing \(|M_0|\ge7/3\), a
  contradiction. Singleton and two-point cases give respectively
  \(1\) and at least \(1/9\) or \(5/3\).
  There is no division by a node difference, no compactness argument
  in the moving configurations, and no unproved limiting step at a
  collision. These are pointwise uniform inequalities for every
  permitted configuration and \(n\ge5\), with endpoint
  \(\max_k|M_k|\ge1/81\) included. Combining them with (17)
  gives exactly (6).

**Audit verdict:** accepted under the stated synthetic hypotheses,
with no mathematical correction. The citation detail above identifies
the circle-average inequality precisely. C645e is the sole direct
local mathematical input; the source theorems supply the imported
calculus. No dependency or argument change results from this audit.

### Qualifications and downstream test

The only finite-family mathematical input is C645e. Neither pole
separation nor a lower bound for a derivative enters (6). However,
exactly one to three distinct simple unit-residue poles in the disk,
holomorphy near its boundary, and exact interpolation at every grid
point are essential hypotheses here. This result does not extend the
moment bound to larger collections or unrestricted multiplicities.

The entire \(F-P\) remains in the boundary norm. In particular
holomorphic interpolation alone supplies no upper bound for it, and
no term involving \(P\) was removed from the weighted integrals.
For a later detector, an independent upper bound \(U_n\) under these
same hypotheses would need to satisfy
\(81R n^2(R^2+d^2)|B_n(x)|U_n<1\) to contradict (6). No such
upper bound is asserted. Actual-Xi pole census, multiplicities,
interpolant realization, zero-free contour clearance and uniform
boundary control remain open. The exact anchor factor in (7) is not
replaced by a weaker factorwise envelope or a heuristic asymptotic.

This is a local specialization of imported residue and contour
inequalities together with the existing finite moment bound. It is
not reported as a new general interpolation theorem or progress beyond
the literature checked, and it leaves the main RH gap unresolved.

## Mathlib

Full matching coverage for this synthetic certificate is **not checked**;
availability is unknown. No specific Mathlib theorem is used as a
formalization of (5), the grid removals or (6). Residue calculus and
the integral inequality are imported through the precise mathematical
citations above. The argument is informal; scoped documentation
validation is not Lean verification.
