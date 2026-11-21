# Lemma 855: a positive radial germ at a finite-multiplicity divisor point

## Hypotheses

Retain the actual entire function G, radius R=R_1>0 and normalization
C=R^2/G(R)^2>0 of L775 and the full r=2,k=1 form of L847:

\[
 \begin{split}
 F(z_1,z_2)&=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},\\
 \omega&=F\frac{dz_1}{iz_1}\wedge\frac{dz_2}{iz_2}
 =C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^3z_2^3}
       dz_1\wedge dz_2.                                      \tag{1}
 \end{split}
\]

Explicitly hypothesize a pair (zeta,eta) with zeta!=0, eta!=0,
zeta!=eta, G(eta)!=0, and G(zeta)=0 of finite multiplicity
n>=1. Choose real lifts theta^0_1 of arg(zeta) and theta^0_2 of arg(eta),
meaning exp(i theta^0_1)=zeta/|zeta| and
exp(i theta^0_2)=eta/|eta|. No particular pair, zero simplicity,
L853 crossing, cutoff tangent or numerical input is assumed.

## Conclusion

There is an open neighborhood O of theta^0 in R^2 and a real analytic
map u:O -> R^2 such that the local radial graph

\[
 \Phi_u(\theta)_j=R\exp(u_j(\theta)+i\theta_j)
\]

passes through (zeta,eta). Its first coordinate has real rank two
throughout O, and G(Phi_u,2)(Phi_u,1-Phi_u,2) is nonzero there.
With the original orientation dtheta_1 wedge dtheta_2,

\[
 \Phi_u^*\omega=q_u\,d\theta_1\wedge d\theta_2,\qquad
 q_u(\theta^0)=0,\qquad
 q_u(\theta)>0\quad(\theta\in O\setminus\{\theta^0\}).       \tag{2}
\]

In particular q_u is exactly real, not just real to finite order.
The full factor J=det(I-i Du)=1-det Du-i tr Du is retained:
J(theta^0)=0 and J has no other zero in O. Formulas (10)-(11) below
give the exact density and Jacobian, including their central zeros.

This is a local existence statement for each fixed finite n; its
neighborhood may depend on the pair and n and is not effective.
It imposes no old boundary data or first derivative. It gives no
periodic extension, prescribed collar, exchange compatibility,
global positive torus, other order/shift, or RH conclusion. This
known-model specialization is recorded as REPRODUCTION under the
prior SPECIALIZE assessment. Its first independent conceptual audit
on 6 November 2026 accepts this local statement; this is not a claim
of mathematical novelty beyond the sources.

## Proof

### Imported tools and the difference checked here

Use the unchanged invocation-start assessment
`drafts/literature/2026-11-06-primitive-monomial-local-germ.md`
and its completed transverse-divisor comparison. The standard tools
and their essential proof cases were inspected in those assessments:

- Jiří Lebl, *Guide to Cultivating Complex Analysis*, v1.10,
  5 November 2026, [Theorem 2.4.7, pp49-50, and Corollary 3.2.12
  with the segment-primitive proof, pp67-68](https://www.jirka.org/ca/ca.pdf):
  isolated-zero Taylor factorization and primitives on star-like
  plane domains. Here the function is entire and the primitive
  domain in the second variable is a disc.
- Lebl, *Tasty Bits of Several Complex Variables*, v4.4,
  31 May 2026, [Theorem 1.2.1 and proof, pp20-21](https://www.jirka.org/scv/scv.pdf#page=20):
  a holomorphic function on a polydisc, continuous on its closure,
  has a power series converging uniformly absolutely on compact
  subsets, and conversely. We choose the closed polydisc inside
  a larger holomorphic neighborhood before applying this theorem.
- Marc Chaperon, *On the Cauchy-Kowalevski theorem*, 9 January 2007,
  [Section 1, Corollary 1 and its real/complex justification,
  p2](https://webusers.imj-prg.fr/~marc.chaperon/Chaperon_Cauchy_Kowalevski.pdf#page=2):
  the analytic local inverse theorem when the derivative is
  invertible, over either R or C. The two applications below have
  separately checked complex and real derivatives.
- Franc Forstnerič, *Analytic disks with boundaries in a maximal real
  submanifold of C2*, Ann. Inst. Fourier 37(1) (1987), 1-44,
  DOI 10.5802/aif.1076, [Section 2, Lemma 8, determinant proof and
  monomial examples, pp14-16](https://users.fmf.uni-lj.si/forstneric/papers/1987Ann.Inst.Fourier.pdf#page=15):
  graph models of isolated complex points and their index calculation.
  These supply the known model method; we do not need to import an
  index conclusion or an existence theorem preserving (1).

We do not reprove these general theorems. The explicit primitive,
tangent choice and pullback calculations below are necessary to
specialize the model to the vanishing form (1), its original angles
and their orientation. A one-variable primitive theorem alone would
not establish the joint coordinate change, and an index alone would
not establish the full density sign.

### A joint primitive coordinate retaining the divisor

Put w=z_1-zeta. Taylor factorization gives
G(zeta+w)=w^n g(w), with g holomorphic and g(0)!=0. On a sufficiently
small product of discs about (0,eta), set

\[
 H(w,z)=C\frac{g(w)G(z)(\zeta+w-z)^2}{(\zeta+w)^3z^3},
 \qquad H_0=H(0,\eta)\ne0.                                 \tag{3}
\]

Choose their closures inside a larger product on which g(w), G(z),
zeta+w, z and zeta+w-z are all nonzero. Such a choice follows from
their nonzero values at (0,eta) and continuity. In particular H is
jointly holomorphic and nonzero. In these variables the full form is
omega=w^n H(w,z) dw wedge dz; the factor w^n has not been removed.

Define, along the straight segment in the second disc,

\[
 V(w,z)=\int_\eta^z H(w,t)\,dt.                              \tag{4}
\]

For joint holomorphicity, expand the actual H on this polydisc as
sum_{a,b>=0} h_ab w^a(z-eta)^b by the cited power-series theorem.
Uniform absolute convergence on smaller compact polydiscs permits
integration along the segment term by term. Consequently
V=sum_{a,b>=0} h_ab w^a(z-eta)^(b+1)/(b+1), converging locally
uniformly absolutely, hence holomorphic by the converse theorem.
The primitive identity gives V_z=H and V(w,eta)=0, so V_w(w,eta)=0.
This verifies the parameter dependence missing from a bare
one-variable primitive invocation.

The holomorphic map (w,z) -> (w,V(w,z)) sends (0,eta) to (0,0)
and has determinant H_0!=0 there. The complex analytic inverse
theorem supplies open neighborhoods U and B and a holomorphic inverse
(w,v) -> (w,h(w,v)), with U inside the chosen product. For all
sufficiently small w, uniqueness and V(w,eta)=0 give h(w,0)=eta.
Differentiating V(w,h(w,v))=v gives

\[
 h_w(0,0)=0,\qquad h_v(w,v)=\frac1{H(w,h(w,v))}.
\]

Since dw wedge dV=H dw wedge dz, the exact expression in the
new coordinates is

\[
                         \omega=w^n\,dw\wedge dv.           \tag{5}
\]

No division by w, G(zeta+w), F or a surface Jacobian was used.
The central vanishing of the form is preserved in (5).

### The monomial surface and its exact pullback

Choose the holomorphic tangent coefficient

\[
 A=-iH_0\frac\eta\zeta,
 \qquad v(w)=Aw+\frac{i}{n+1}\overline w^{\,n+1},
 \qquad S(w)=(\zeta+w,h(w,v(w))).                            \tag{6}
\]

The notation A here is a scalar, not the matrix Du of L847.
For w in a sufficiently small open disc W about zero,
(w,v(w)) belongs to B; this follows from continuity and v(0)=0.
Thus S is an actual real analytic surface in U, with no formal
inversion or convergence assumption left over. Its first coordinate
makes it an embedding and an immersion of real rank two.

Writing w=x+iy, one has
dv=A dw+i conjugate(w)^n d conjugate(w) and
dw wedge d conjugate(w)=-2i dx wedge dy. Therefore (5) gives

\[
                     S^*\omega=2|w|^{2n}\,dx\wedge dy.       \tag{7}
\]

This identity holds on the whole disc, including zero; it has no
uncontrolled higher-order term. Every n>=1 gives a polynomial in
w and conjugate(w), so there is no fractional-power regularity issue.
At zero its antiholomorphic derivative vanishes. Using (6) and the
inverse derivatives above yields

\[
 dS_1(0)=dw,\qquad dS_2(0)=-i\frac\eta\zeta\,dw.           \tag{8}
\]

### The original angular projection and its orientation

After shrinking W, use the holomorphic logarithm branch near 1
obtained by the complex analytic inverse theorem for exp at 0,
whose derivative is 1. Composing with S_1(w)/zeta and S_2(w)/eta
gives real analytic functions of (x,y), normalized to zero at w=0.
Define their real angle lifts
Theta_j(w)=theta^0_j+Im log(S_j(w)/S_j(0)). By (8),

\[
 d\Theta_1(0)=\operatorname{Im}(dw/\zeta),\qquad
 d\Theta_2(0)=\operatorname{Im}(-i\,dw/\zeta).
\]

If 1/zeta=p+it with p,t real, the derivative in the oriented
coordinates (x,y) is

\[
 D\Theta(0)=\begin{pmatrix}t&p\\-p&t\end{pmatrix},\qquad
 \det D\Theta(0)=p^2+t^2=|\zeta|^{-2}>0.                    \tag{9}
\]

This sign follows from the chosen tangent A; it is not an arbitrary
reorientation of the requested angle coordinates. The real analytic
inverse theorem gives a neighborhood on which Theta is a real analytic
diffeomorphism. Shrink W to a disc within that neighborhood and all
previous domains, with
lambda(w):=det DTheta(w)>1/(2|zeta|^2) throughout W. Its image
O=Theta(W) is open, and its inverse w=w(theta) is real analytic.
All the nonzero factors chosen in (3) remain nonzero on S(W).

Define u_j(theta)=log(|S_j(w(theta))|/R). These are real analytic
real functions because the coordinates stay nonzero. By the angle
definition, S_j(w(theta))=R exp(u_j(theta)+i theta_j), so this is
precisely a local graph of the requested kind. Its first coordinate
zeta+w(theta) has real rank two everywhere. Changing variables in
(7), with the strictly positive determinant just proved, gives

\[
 q_u(\theta)=\frac{2|w(\theta)|^{2n}}{\lambda(w(\theta))}.   \tag{10}
\]

It vanishes only at theta^0 and is strictly positive and real at
every other point of the full open neighborhood O. This proves (2).

### Keeping the complex Jacobian zero

For clarity check the factor J itself, rather than inferring sign
after deleting it. On S(W), the identity h_v=1/H gives
S^*(dz_1 wedge dz_2)=2 conjugate(w)^n/H(w,S_2(w)) dx wedge dy.
Dividing only by the nonzero factors i z_1 and i z_2 and then
changing to theta coordinates yields

\[
 J(\theta)=
 -\frac{2\overline{w(\theta)}^{\,n}}
 {H(w(\theta),\Phi_{u,2}(\theta))
  \Phi_{u,1}(\theta)\Phi_{u,2}(\theta)\lambda(w(\theta))}.
                                                                  \tag{11}
\]

This is exactly det(I-i Du) by L847's full pullback calculation,
which is local and does not require periodicity. All denominator
factors in (11) are nonzero. Thus J has its allowed central zero
and no other zero. Moreover (1) and (3) give
F=-w^n H z_1 z_2 on S(W), so FJ is exactly (10), at and away
from the center. The density zero is a smooth zero of order 2n;
both the multiplicity-n divisor factor and the multiplicity-n
Jacobian factor have been retained.

Only freely chosen local tangent data were used. In particular no
conclusion about matching an existing collar or extending the germ
can be inferred from the inverse theorem or from the strict sign
on O. The construction passes the stated local discriminator, and
all global and all-degree obligations remain open.

### Independent conceptual audit — 6 November 2026

The first audit under
`drafts/literature/2026-11-06-l855-positive-germ-conceptual-audit.md`
accepts (3)–(11), with the following explicit common-domain check.
The pair and its finite n are hypotheses throughout; the audit does
not establish any particular crossing. L775 supplies the stated G,R,C.
Only L847's local differential identity is used: its periodicity and
product-graph obstruction are not prerequisites for a local graph.
The already inspected primary sources above suffice; this audit
imports no new existence or positivity theorem.

Choose the product in (3) first, with closure in a larger product
where every listed factor is nonzero. The segment in (4) remains in
its second disc. On every smaller compact polydisc the integrated
series is absolutely uniformly convergent: its terms are bounded by
the corresponding absolute series for H times the second-disc radius.
It therefore gives a jointly holomorphic V with V_z=H and
V_w(w,eta)=0. The complex derivative of (w,z)->(w,V) at the base
point is diag(1,H_0). Restrict its inverse neighborhoods so the image
of h lies in that product. Their openness supplies a small w-disc
both with (w,eta) in U and (w,0) in B; uniqueness then justifies
h(w,0)=eta. This also checks that the inverse's first component is w.

Next restrict the w-disc so (w,v(w)) lies in B. Restrict it further
so both S_j(w)/S_j(0) lie in the inverse-exponential neighborhood of
1. Thus the logarithms and Theta exist on the same disc as S, not on
unrelated inverse domains. The tangent (8) and matrix (9) are exact;
the antiholomorphic term contributes no first derivative because
n>=1. Apply the real inverse theorem to this Theta, and take a final
disc W inside its injectivity neighborhood and all previous domains,
with det DTheta>1/(2|zeta|^2). Its image O is open and contains theta^0.
Restriction preserves both inverses, all nonzero factors and the
positive orientation. This single W, and hence this single O, works
for every property claimed for the fixed pair and n.

The two wedge signs in (7) and (11) are independently consistent:
i conjugate(w)^n dw wedge d conjugate(w)=2 conjugate(w)^n
dx wedge dy, before multiplying by w^n. Thus (7) is
2|w|^(2n) dx wedge dy, whereas dividing dz_1 wedge dz_2 by
(i z_1)(i z_2) supplies the minus sign in (11). Changing to angles
divides by the positive lambda. Multiplying F=-w^n H z_1 z_2 by
(11), including w=0, proves (10) without deleting a zero.
As a separate central check, write dw/zeta=alpha+i beta. Then
(dtheta_1,dtheta_2)=(beta,-alpha) and (du_1,du_2)=(alpha,beta),
so Du(theta^0)=[[0,-1],[1,0]], det Du=1 and tr Du=0.
Consequently J(theta^0)=0 directly from det(I-i Du) as well.

Finally log(|S_j|/R) is real analytic on the retained nonzero
coordinate neighborhood, with u(theta^0)=log(|S_j(0)|/R)
componentwise. The inverse w(theta) has invertible real derivative
everywhere in O. Hence transversality, the unique density zero and
the unique J zero follow on all of O, not merely as jets at its
center. Their real-analytic vanishing orders are respectively 2n
and n. No uniform radius in n, prescribed outer data, collar
matching, exchange extension or higher-order positivity is proved.
The audit found no mathematical correction necessary; its outcome
is verification of the existing local specialization.

## Mathlib

Full matching coverage of this positive radial germ is not checked.
Mathlib coverage of the supporting factorization, several-variable
power-series and real/complex analytic inverse tools is also not
checked in this step. The precise primary citations above are the
standard inputs; no formal verification or absence claim is made.
