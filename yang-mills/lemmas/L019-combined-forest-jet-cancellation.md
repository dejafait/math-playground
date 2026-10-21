# L019 — Nonlinear forest jets locate the complete coefficient cancellation

## Hypotheses

Fix an admitted mesh and all the original SU(2), boundary, generator and
Wilson-flow data of L011. Let F,F' be two boundary-rooted forests. All
Taylor polynomials below live on their exact reduced Haar slices; no
higher vertex is assigned to the Hodge Gaussian. L016's path-product
map changes between the slices by a smooth Haar-preserving diffeomorphism.
Use the linear map T of L018 to compare their coordinates.

Near zero write this transition as

\[
\theta'=T\theta+Q(\theta)+C(\theta)+O(|\theta|^4),\qquad
\Phi_g(x)=T^{-1}\theta'(gx)/g
=x+gq(x)+g^2c(x)+O(g^3),
\tag{1}
\]

where Q,q are homogeneous quadratic and C,c are homogeneous cubic. Put
p=c-(Dq)q/2, L=D_q and P=D_p. Bars mean pullback from F' by **T only**,
not by the full nonlinear map. Write M=M_(2,F), bar M'=M_(2,F') composed
with T. All cumulants use F's Gaussian exp(-S2) dx.

For either original probe let f=f_(i,0), r=r0, U=S3, E=S4+M, and define
L011's two groups

\[
\begin{split}
G&=-\kappa(f,r,E)+\tfrac12\kappa(f,r,U,U),\\
H&=\kappa(f_2,r)+\kappa(f_1,r_1)+\kappa(f,r_2)
-\kappa(f_1,r,U)-\kappa(f,r_1,U).
\end{split}\tag{2}
\]

Thus Gamma=G+H. These groups include the coordinate measure, both action
corrections, insertion and flow jets, but exclude L010's separate Ward
Haar-divergence insertion.

## Conclusion

Exact reduced Haar invariance gives the polynomial identities

\[
|\det T|=1,\qquad \operatorname{div}q=0,\qquad
\operatorname{div}p=\bar M'-M.\tag{3}
\]

For h=f or r, the observable jets and action jets transform as

\[
\begin{split}
\bar h'_0&=h,\quad \bar h'_1=h_1-Lh,\\
\bar h'_2&=h_2-Lh_1+\tfrac12 L^2h-Ph,\\
\bar U'&=U-W,\qquad
\bar E'=E-LU+\tfrac12 LW-Z,\\
W&=LS2,\qquad Z=PS2-\operatorname{div}p.
\end{split}\tag{4}
\]

In particular the change of the action/measure group, evaluated after
this linear identification of the Gaussians, is exactly

\[
\begin{split}
\bar G'-G={}&-\kappa(Lf,r,U)-\kappa(f,Lr,U)\\
&+\tfrac12\kappa(L^2f,r)+\kappa(Lf,Lr)
 +\tfrac12\kappa(f,L^2r)\\
&+\kappa(Pf,r)+\kappa(f,Pr).
\end{split}\tag{5}
\]

The other group changes by the negative of (5). Therefore the complete
fixed-mesh coefficient is invariant, with its cancellation explicitly
located in the observable and residual jets. The action/measure group
is invariant by itself only if the right side of (5) vanishes. No claim
of vanishing or nonvanishing of this group is made for either original
box probe. L018's isolated coordinate-density change is specifically
-κ(f,r,div p), which is not in general the change of G.

An exact two-link SU(2) product-map diagnostic below has nonzero group
changes, including +4/3 for G and -4/3 for H. It shows that Haar invariance
alone cannot justify discarding the observable jets. It does not evaluate
any original box contraction. No cutoff logarithm, absence of power
terms, bounded remainder, boundary subtraction or reflected error bound
<= c_box/2 follows.

## Proof

### 1. Transition measure and Jacobian jets

L016's path trivialization writes full product Haar as reduced product
Haar times pinned-site product Haar. The induced change between two
slices is a diffeomorphism: reduction in the reverse forest is its inverse.
Every continuous function of one slice extends uniquely to a pinned-gauge
invariant full-link function. Applying either product trivialization to
that extension proves that the transition preserves reduced Haar, not
just a particular Wilson expectation.

The two slices have the same number of remaining links and the same
normalized local SU(2) Haar constant. In exponential coordinates L011
gives log density -M2(theta)+O(|theta|^4). The change-of-variables identity
at zero first gives |det T|=1. In scaled coordinates it then gives

\[
-g^2 M(x)+O(g^3)
=-g^2\bar M'(x)+\log|\det D\Phi_g(x)|+O(g^3).
\tag{6}
\]

This is an equality of local Taylor jets at each fixed mesh. Expanding
the determinant near the identity yields

\[
\log|\det D\Phi_g|
=g\operatorname{div}q
+g^2\{\operatorname{div}c-\tfrac12\operatorname{Tr}[(Dq)^2]\}
+O(g^3).
\tag{7}
\]

The order-g coefficient is zero. Since

\[
\operatorname{div}((Dq)q)
=\operatorname{Tr}[(Dq)^2]+D_q(\operatorname{div}q),
\]

the order-g^2 coefficient in (7) is div p, proving (3). Quadratic and
cubic jets are explicitly obtainable from the forest path products by
Baker–Campbell–Hausdorff expansion; no global logarithm is required.

### 2. Scalar jets

Through order g^2 the map Phi_g agrees with the time-one flow of the
polynomial vector field g q+g^2 p. On scalar jets its inverse pullback is

\[
1-gL+g^2(\tfrac12 L^2-P).
\tag{8}
\]

This follows directly by composing the local maps, or by differentiating
the local flow; it is a finite Taylor assertion, not a convergence claim
about a global polynomial flow. Gauge invariance equates the original
full-link functions in the two slices. Applying (8) to
h+g h1+g^2 h2 proves the observable formulas in (4). It applies in
particular to the full flowed numerator because Wilson flow is equivariant,
not because the flow stays in a forest slice.

Apply (8) to S2+g S3+g^2 S4. The quadratic action is unchanged under the
linear map T by L018's Gaussian identification. Thus
bar S3'=S3-LS2 and
bar S4'=S4-LS3+L^2 S2/2-PS2. Adding bar M'=M+div p proves the E formula.
Only the quadratic coordinate-density jet is needed at this order.

### 3. Connected Gaussian integration by parts

For any polynomial vector field v and scalar polynomials A1,...,An,
with n>=1, define W_v=D_v S2-div v. Gaussian integration by parts gives

\[
\kappa(A_1,\ldots,A_n,W_v)
=\sum_{j=1}^n\kappa(A_1,\ldots,D_v A_j,\ldots,A_n).
\tag{9}
\]

Indeed Gaussian decay makes the integral of every polynomial divergence
zero, so <W_v>=0. Introduce formal sources and apply this integration
by parts coefficient by coefficient to exp(sum t_j A_j). After formal
normalization it reads
<W_v>_t=sum t_j <D_v A_j>_t. Differentiating once in every source proves
(9). Each coefficient uses finitely many Gaussian polynomial moments;
no moment-generating function for a cubic or quartic polynomial is
assumed to converge. The same identity holds for a nonisotropic Gaussian.
By (3), W_q=W and W_p=Z.

Direct substitution of (4) into G gives

\[
\begin{split}
\bar G'-G={}&\kappa(f,r,LU)-\tfrac12\kappa(f,r,LW)
+\kappa(f,r,Z)\\
&-\kappa(f,r,U,W)+\tfrac12\kappa(f,r,W,W).
\end{split}\tag{10}
\]

Apply (9) to κ(f,r,U,W) and κ(f,r,W,W). The LU and LW terms cancel.
Apply it once more to κ(Lf,r,W), κ(f,Lr,W) and κ(f,r,Z). This gives
exactly (5), with all factors 1/2 retained.

Substituting (4) into H and collecting terms first gives the negative
of (5), together with

\[
\kappa(f_1,r,W)+\kappa(f,r_1,W)
-\kappa(Lf_1,r)-\kappa(f_1,Lr)
-\kappa(Lf,r_1)-\kappa(f,Lr_1).
\]

These additional terms vanish by (9). Hence bar H'-H=-(bar G'-G).
This is an explicit cancellation of the coefficient formula itself,
rather than an inference solely from equality of the exact covariances.
It requires both first- and second-order observable jets; (5) by itself
contains no bound uniform in the mesh or in forest path length.

### 4. Exact nontrivial product-map diagnostic

On two copies of SU(2) use (U,V)->(U^(-1),UV). Inversion and translation
preserve product Haar. In Lie coordinates u,v its linear map is
T(u,v)=(-u,u+v). Removing T as in (1) gives

\[
q=(0,[u,v]/2),\qquad
c=(0,([u,[u,v]]+[v,[v,u]])/12),
\]
\[
p=(0,-[u,[u,v]]/24+[v,[v,u]]/12).
\tag{11}
\]

These jets follow by multiplying the matrix exponential series and
expanding log(1+X) through degree three (equivalently the degree-three
Baker–Campbell–Hausdorff identity). In the basis t_a=i sigma_a/2 the
bracket is minus the ordinary cross product. Its iterated brackets are
the same as for the plus-cross-product convention. Direct differentiation
gives

\[
\operatorname{div}q=0,\quad
\operatorname{div}p=(|u|^2+2u\cdot v)/12
=\{ |u|^2+|u+v|^2-|u|^2-|v|^2\}/12.
\tag{12}
\]

This independently checks the signs in (3). It is a reduced product-map
diagnostic; it is not an assertion that these two variables exhaust an
original-box forest transition, its Wilson action or its probe jets.

Take six independent variance-one Gaussians, S2=(|u|^2+|v|^2)/2,
f=(u1+2v1)^2, r=v1^2, and all higher action/observable jets zero.
Keep M=(|u|^2+|v|^2)/12. Exact polynomial moments give

\[
(G,H)=(-8/3,0),\qquad
(\bar G',\bar H')=(-4/3,-4/3).
\tag{13}
\]

The full coefficient remains -8/3. The isolated Haar change is -4/3;
the action change is therefore +8/3. In this case adding the action
terms does not finish the cancellation: the changed observable jets
supply the remaining -4/3. Thus no general Haar argument makes G alone
invariant, even when the original higher observable jets vanish.

Run
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_forest_cancellation.py`.
The script verifies (3), (5), (9) and (13) with rational polynomial
arithmetic, and independently computes normalized moment-series
covariances before and after the change. With populated cubic/quartic
and observable jets, G changes from 45/4 to 343/12 and H from 113/21
to -251/21; their sum is 1397/84. A diagonal nonisotropic Gaussian
with variances (1,2,3,4,5,6) has W != 0 and tests the changed cubic
action and two-cubic-action cumulant as well; its group changes are
+9784/3 and -9784/3, with full coefficient 1243898/105. These tests check
combinatorics and cancellation, not original lattice sums or asymptotics.

This reproduces finite coordinate-change and Gaussian identities in the
screened specialization. The original-box cutoff logarithm remains
unevaluated. A finite-mesh algebraic identity cannot bound an internal
loop, identify physical-boundary terms, or improve the required interacting
reflected error <= c_box/2. No result beyond the checked literature is
claimed.

## Mathlib

Coverage of the full combined forest-jet statement: **not checked**.
Coverage of supporting polynomial Gaussian integration by parts, finite
cumulants, local Jacobian expansion and degree-three BCH: **not checked**.
No Mathlib theorem is asserted to match this statement. The
[prior SPECIALIZE assessment](../drafts/literature/2026-09-26-current-target.md)
records the inspected primary sources and direct links. In particular
Del Debbio–Patella–Rago, [arXiv:1306.1173v1](https://arxiv.org/pdf/1306.1173v1),
section 6, supplies supporting flowed-translation context, rather than
this coordinate cancellation or a theorem for the all-face boundary.
The Haar/tree input is the inspected Freidel–Livine,
[hep-th/0205268v2](https://arxiv.org/pdf/hep-th/0205268v2), section 2.1,
(2.1)–(2.8), specialized to pinned forests in L016. General flow
renormalizability and bulk stress matching remain cited inputs within
their assessed scope; they are not reproved or used to assign a logarithm.
