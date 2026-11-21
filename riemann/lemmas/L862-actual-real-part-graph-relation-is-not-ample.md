# Lemma 862: the actual real-part graph relation is not ample in any base frame

## Hypotheses

Use L847(1)-(3), including its actual entire G with positive ordinary
coefficients, R>0 and C=R^2/G(R)^2>0. Thus

\[
 \Phi_y(\theta)_j=R e^{y_j+i\theta_j},\qquad
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2}.
\]

The zero-jet domain is the open subset of T2 x R2 on which
f=F(Phi_y(theta))!=0. At a fixed zero-jet write f=p+iq, p,q real,
and let A be an independent real 2-by-2 derivative matrix in the
original angular coordinates. Test exactly the open relation

\[
 \mathcal R_f=\{A:H_f(A)>0\},\qquad
 H_f(A)=\operatorname{Re}\bigl(f\det(I-iA)\bigr)
       =p(1-\det A)+q\operatorname{tr}A.                 \tag{1}
\]

No phase equality, prescribed collar, smallness, bound on y,
exchange condition or global formal solution is assumed. This is
not the enlarged nonstrict relation at the full F divisor.

Import the principal-space and ampleness definitions from M. L.
Gromov, *Convex integration of differential relations. I*, Math.
USSR-Izv. **7** (1973), 329-343, definitions 1.2.1-1.2.6,
pp330-331, and the local-coordinate hypothesis of Theorem 1.3.1,
p331; Corollary 1.3.2 uses all principal directions. See the
[primary English article](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=2250&what=fullteng).
A principal space fixes the zero-jet and the derivative on a base
hyperplane. Ampleness requires each nonempty path component of
its intersection with the relation to have the entire affine
principal space as convex hull. An empty intersection is ample
by convention. These hypotheses were inspected in
`drafts/literature/2026-11-06-real-part-graph-relation-scope.md`;
the invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-06-real-part-principal-slice-test.md`.

## Conclusion

For every f!=0, nonzero real covector xi and matrix A0, the
principal plane and exact scalar restriction are

\[
 \begin{split}
 \mathcal P&=\{A_0+v\xi^T:v\in\mathbb R^2\},\\
 H_f(A_0+v\xi^T)&=H_f(A_0)+\ell\cdot v,\\
 \ell&=q\xi-p\operatorname{cof}(A_0)\xi,\qquad
 \operatorname{cof}\begin{pmatrix}a&b\\c&d\end{pmatrix}
       =\begin{pmatrix}d&-c\\-b&a\end{pmatrix}.           \tag{2}
 \end{split}
\]

If ell!=0 the intersection is a nonempty proper open half-plane,
with one component whose convex hull is itself. If ell=0 then
p!=0: the intersection is full for p>0 and empty for p<0. These
are all cases. Every direction has a proper half-plane slice
through an admissible derivative. Thus the full relation is not
ample in any direction at any off-divisor zero-jet, and no local
base coordinate frame repairs its failure.

The actual coefficient attains a negative real value at
theta=(0,0), y=(0,log 2). There, every principal plane through
any admissible derivative has proper half-plane intersection, in
every direction. No nonempty subrelation over that zero-jet can
be ample there, even after a local bundle coordinate change.

This stops the direct import of Gromov 1.3.1 or 1.3.2 for the full
off-divisor graph relation. It does not exclude a graph avoiding
particular zero-jets, a different relation/construction, graph-free
contours, or RH. No global contour or Xi minor sign is proved.

## Proof

### Exact principal slices, including degenerate cases

Equation (1) uses the full L847 pullback. Two linear maps agreeing
on ker(xi) differ uniquely by v xi^T for fixed xi!=0. The exact
rank-one expansion is

\[
 \det(A_0+v\xi^T)=\det A_0+
       \bigl(\operatorname{cof}(A_0)\xi\bigr)\cdot v,
 \qquad \operatorname{tr}(v\xi^T)=\xi\cdot v.
\]

For A0=(a b; c d), the determinant increment is
d v1 xi1-c v1 xi2-b v2 xi1+a v2 xi2; the quadratic term
v1 v2(xi1 xi2-xi2 xi1) vanishes. This verifies the cofactor
convention without assuming A0 invertible and proves (2).
For ell!=0, the strict inequality is a proper open half-plane.
It is convex and path-connected, so its sole component's convex
hull is that half-plane, not the entire principal plane.

If p=0 then q!=0, hence ell=q xi!=0. If p!=0, choose an
orthogonal O with O e1=xi/|xi|. Replace A0 by A'=O^T A0 O and
v by v'=O^T v; determinant and trace are unchanged and the rank-one
direction is |xi| v' e1^T. These are invertible affine changes of
the plane. Writing A'=(a b; c d), vanishing of its linear coefficient
means q-p d=0 and p b=0. Thus d=q/p, b=0 and

\[
 H_f(A_0)=p(1-ad)+q(a+d)
         =p+q^2/p=(p^2+q^2)/p.                           \tag{3}
\]

The constant is nonzero and has the sign of p. This establishes
every full/empty case; no zero constant case is omitted off f=0.
In particular if p<0 and A0 is admissible, ell cannot vanish for
any xi, proving the stronger assertion at such a zero-jet.

### Bad slices in every direction of the full relation

Take A0=tI. Then

\[
 H_f(tI)=p(1-t^2)+2qt,\qquad \ell=(q-pt)\xi.           \tag{4}
\]

If p=0 choose t=q, obtaining H=2q^2>0 and ell!=0. If p!=0
put t=q/p+s. Then H=(p^2+q^2)/p-p s^2 and ell=-p s xi.
For p>0 choose 0<|s|<sqrt(p^2+q^2)/p. For p<0 choose
|s|>sqrt(p^2+q^2)/|p|. Both choices give H>0 and ell!=0.
The same t works for every xi!=0. Thus every direction has a
nonample slice through an admissible derivative. For p>0 some
other slices are full; ampleness of the entire relation would
require the condition for every component, so those do not help.

### All local frames and an actual negative coefficient

Let x be any base coordinates and B=D_x theta at the point,
invertible over R. In the original fiber coordinates the derivative
M=D_x y represents A=M B^(-1). Varying just column j of M varies
A by v e_j^T B^(-1). The row e_j^T B^(-1) is a nonzero covector,
so this is one of the full principal planes just tested. The
inequality uses the fixed angular orientation: if coordinates
reverse orientation, their volume coefficient changes as well,
not the underlying relation (1).

More generally use fiber coordinates y=h(x,z), with D_z h
invertible. For N=D_x z, the chain rule gives
M=D_x h+(D_z h)N at a fixed zero-jet. Varying column j of N now
varies A by (D_z h)v e_j^T B^(-1). The free vector still ranges
over R2. The fixed translation D_x h adds no new directions.
Thus these are affine isomorphisms of the tested principal planes;
they preserve path components and convex hulls. This verifies the
quantifiers for all local bundle frames. Abandoning the angular
graph condition is a different problem.

For the actual zero-jet theta=(0,0), y=(0,log 2), one has z1=R,
z2=2R and

\[
 f=-\frac{C G(R)G(2R)}{4R^2}<0.                          \tag{5}
\]

The two G values are positive by L847's positive ordinary
coefficients. The radii are distinct and nonzero; therefore this
is genuinely off the full F divisor, not an arbitrary complex
coefficient assumed attainable. The constant periodic graph
y=(0,log 2) realizes the zero-jet; its derivative need not satisfy
(1). Independent first derivatives tI, t>1, are admissible at
(5), since H=p(1-t^2)>0, and a local affine graph realizes each
such first jet. No global solution is inferred from that fact.

Here p<0, so (3) shows that every slice through an admissible
derivative is a proper half-plane. For any nonempty subrelation,
choose one of its derivatives and a principal plane through it.
The component through it is contained in that half-plane, and so
is its convex hull; it cannot fill the entire plane. The coordinate
identifications above preserve this obstruction. This proves the
scoped direct-import failure, not impossibility of global sign
graphs. Divisor extension, exchange symmetry, formal existence,
higher orders and all-degree positivity remain separate gaps.

The general theorem and definitions are imported, not reproved.
The elementary matrix specialization is retained because it is
the uncomputed applicability difference. This is a reproduction/
specialization with useful local negative evidence, not new general
convex-integration theory or a claim of certified originality.

## Mathlib

Full matching coverage of this actual-F slice result is not checked;
no absence claim is made. Supporting determinant and trace algebra
would not alone constitute a match. The sphere-eversion project's
general open-ample theorem in the source assessment does not verify
these hypotheses. This is an informal exact calculation, with no
numerical experiment, mathematical script or formal verification.
