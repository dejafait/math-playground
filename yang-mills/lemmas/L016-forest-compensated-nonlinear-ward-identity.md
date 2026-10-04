# L016 — The pinned forest compensator retains the full nonlinear Ward insertion

## Hypotheses

Use the finite SU(2) Wilson box, variable links E, boundary links fixed to
identity, and positive bare coupling g of L003. Fix its rooted forest F:
each interior vertex belongs to a tree with exactly one boundary root.
All site gauge transformations equal identity on every boundary vertex.
Write B = E minus F and let Q = SU(2)^B be the slice with U_f = 1 for
f in F. Boundary links remain fixed. Superscript F means restriction to
this slice, including evaluation of all full-link functions before
restriction.

Use exactly L009's supported-stencil displacement and endpoint-averaged
clover generator V_a, with

\[
V_a U_e=X_e(U)U_e,\qquad
t^c=i\sigma^c/2,\qquad
\langle H,K\rangle=-2\operatorname{Tr}(HK).
\]

L009 proves that V_a is smooth, acts only on variable links, and is
equivariant for h.U_xy = h_x U_xy h_y^(-1). The link derivative L_e^c
acts along U_e -> exp(s t^c) U_e. Use product normalized Haar measure
on Q and the reduced Wilson probability law

\[
d\mu^F_{a,g}=Z_{a,g}^{-1}e^{-S_g^F(q)}dH_B(q),
\qquad S_g=\frac4{g^2}\sum_p P_p.
\]

L003 identifies this normalization and all gauge-invariant expectations
with their full-link counterparts. No BRST functional, extra determinant,
continuum boundary condition or limit in a is assumed.

## Conclusion

There is a unique boundary-pinned infinitesimal gauge compensator
\(\widehat\omega_v(U)\) such that V_a plus its gauge variation freezes
every forest link. Starting with zero at each boundary root, if p is the
parent of v in its tree, its recursion is

\[
\widehat\omega_v=
\begin{cases}
\operatorname{Ad}_{U_f^{-1}}(\widehat\omega_p+X_f),&f=(p,v),\\
\operatorname{Ad}_{U_f}\widehat\omega_p-X_f,&f=(v,p).
\end{cases} \tag{1}
\]

Every boundary value is zero, including at vertices that are not roots.
On Q this becomes the explicit smooth path sum

\[
\omega_v(q)=\sum_{f\in\gamma_v}\epsilon_{vf}X_f^F(q),
\qquad \omega_v=0\quad(v\text{ on the boundary}), \tag{2}
\]

where \(\gamma_v\) is the path from its root to v and \(\epsilon_{vf}\)
is +1 or -1 according to traversal of the stored positive link. The
induced slice generator \(\mathsf V_a\) is

\[
\mathsf V_a q_e=Y_e(q)q_e,\qquad
Y_e=X_e^F+\omega_x-\operatorname{Ad}_{q_e}\omega_y,
\quad e=(x,y)\in B. \tag{3}
\]

Its **fully differentiated** reduced-Haar divergence satisfies the
pointwise equality

\[
\operatorname{div}_{H_B}\mathsf V_a
=\bigl(\operatorname{div}_{H_E}V_a\bigr)^F
=\frac38\sum_p b_p\operatorname{Tr}q_p
=-\frac34\sum_p b_p P_p(q), \tag{4}
\]

with exactly the planar strain b_p of L010. In particular the reduced
compensator contribution equals the omitted forest-link contribution:

\[
\sum_{e\in B,c}L_e^c
 \langle t^c,\omega_x-\operatorname{Ad}_{q_e}\omega_y\rangle
=\left.\sum_{f\in F,c}L_f^c\langle t^c,X_f\rangle\right|_Q. \tag{5}
\]

Neither side of (5) is asserted to vanish. For every smooth gauge-invariant
observable O, restriction gives

\[
\mathsf V_a O^F=(V_a O)^F,\qquad
I^F:=\mathsf V_a S_g^F-\operatorname{div}_{H_B}\mathsf V_a
=(V_a S_g-\operatorname{div}_{H_E}V_a)^F, \tag{6}
\]
\[
\mathbb E_F I^F=0,\qquad
\mathbb E_F[\mathsf V_a O^F]=\operatorname{Cov}_F(O^F,I^F). \tag{7}
\]

This includes both centered Wilson-flow probes of L010 at tau = 1/16.
The comparison is pointwise, rather than an equality obtained only after
integration. It adds no ultraviolet estimate: finite interacting matching,
physical-boundary remainders and the reflected error <= c_box/2 remain
uncontrolled. It supplies a forest-coordinate representation of the
existing insertion for L011's expansion, not a vanishing nonlinear
divergence or a continuum Yang–Mills construction.

## Proof

### 1. Pinned paths and the compensator

Specialize the known tree path-product map in Freidel–Livine,
[*Spin Networks for Non-Compact Groups*, hep-th/0205268v2](https://arxiv.org/pdf/hep-th/0205268v2),
section 2.1, (2.1)–(2.8), to L003's pinned forest. Their root conjugation
is absent here because all roots are fixed. Let P_v(U) be the ordered
product of the forest links along \(\gamma_v\), using inverses for negative
traversals. Put P_v = 1 at every boundary vertex. Define

\[
\Gamma(U)_e=P_x(U)U_eP_y(U)^{-1}. \tag{8}
\]

For each forest link (8) is identity: if the path traverses f=(p,v)
positively, P_v=P_p U_f; for f=(v,p), P_v=P_p U_f^(-1). Boundary links
are also unchanged. Products and inverses show that Gamma is globally
smooth. The allowed gauge convention gives
P_v(h.U)=P_v(U)h_v^(-1), hence Gamma(h.U)=Gamma(U).

The smooth site variable \(\widehat\omega_v=P_v^{-1}(V_aP_v)\) has zero
boundary value. Differentiating the two path recursions proves (1).
The gauge variation with parameter \(\widehat\omega\) is

\[
(\delta_{\widehat\omega}U)_e
=\widehat\omega_x U_e-U_e\widehat\omega_y.
\]

Thus (1) is precisely
X_f+\widehat\omega_x-\operatorname{Ad}_{U_f}\widehat\omega_y=0 for every
forest link. The rooted recursion determines every interior value uniquely;
it imposes no constraint on a second boundary endpoint because each tree
has only one boundary vertex.

On Q every forest factor in P_v is identity. Its derivative is therefore
the signed sum (2). Differentiating (8) at a slice point gives
\(D\Gamma_q[V_a(q)]_e=Y_e q_e\), with (3), including all derivatives of
both endpoint paths. The same formula gives zero on every forest link.
Off the slice one must use (1), rather than the untransported sum (2).

### 2. The exact product measure and orbit divergence

Extend the Haar reduction already used in L003 to coordinates on the full
configuration manifold. Let k_v=P_v(U)^(-1) at interior vertices and k_v=1
on the boundary. The inverse of (8) is

\[
\Psi(k,q)_e=k_x q_e k_y^{-1},\qquad q_f=1\quad(f\in F). \tag{9}
\]

The path recursions show that (8)–(9) are mutually inverse smooth maps
between SU(2)^(interior vertices) times Q and SU(2)^E. This is a global
trivialization, without a residual root transformation. Its measure is

\[
\Psi^*(dH_E)=\prod_{v\text{ interior}}dk_v\,dH_B(q). \tag{10}
\]

For the explicit applicability check in (10), order the forest edges
by increasing depth. For a positive parent-to-child edge U_f=k_p k_v^(-1);
for the reverse edge U_f=k_v k_p^(-1). With the parent fixed, Haar
invariance and inversion invariance change dU_f to dk_v. This successive
change is triangular. At fixed k, each remaining U_e=k_x q_e k_y^(-1)
changes dU_e to dq_e by left/right Haar invariance. Applied to arbitrary
continuous integrands, these changes prove (10), not just its restriction
to invariant functions. The normalized gauge volume is one.

In these coordinates the fixed gauge action is (k,q) -> (h k,q). By
L009's equivariance, the full field V_a consequently has components

\[
\dot q=\mathsf V_a(q),\qquad
\dot k_v=-k_v\omega_v(q). \tag{11}
\]

Indeed at k=1, differentiation of k=P^(-1) gives -omega, while
differentiation of Gamma gives (3). Equivariance then transports these
components to every k. For a fixed q, each orbit component in (11) has
flow k_v -> k_v exp(-s omega_v(q)), which preserves Haar measure.
Its divergence with respect to dk_v is zero. Dependence of omega on q
does not enter this orbit divergence: the product-coordinate divergence
differentiates each component only in its own coordinate. By (10), the
full divergence is therefore precisely div_(H_B) mathsf V_a at every
(k,q). Setting k=1 proves the first equality of (4).

This argument uses equivariance and the exact product measure; Haar
invariance under a fixed gauge transformation alone would not prove it.
The two plaquette equalities in (4) are the restriction of L010's exact
full-link formula, including its compact-support telescoping. They are
imported from that calculation, not recomputed here.

### 3. Retaining the configuration dependence of the paths

An explicit differentiation of (3) confirms what the comparison retains.
For a remaining link e=(x,y), derivatives in Q hold all forest links
identity, so

\[
L_e^c\omega_v=\sum_{f\in\gamma_v}\epsilon_{vf}L_e^c X_f^F.
\]

Also

\[
L_e^c(\operatorname{Ad}_{q_e}\omega_y)
=[t^c,\operatorname{Ad}_{q_e}\omega_y]
 +\operatorname{Ad}_{q_e}L_e^c\omega_y.
\]

The contraction of its first term with t^c is zero by invariance of
-2 Tr. Accordingly the compensator divergence in (5) is explicitly

\[
\sum_{e\in B,c}\left\langle t^c,
 \sum_{f\in\gamma_x}\epsilon_{xf}L_e^c X_f^F
 -\operatorname{Ad}_{q_e}
  \sum_{f\in\gamma_y}\epsilon_{yf}L_e^c X_f^F
\right\rangle. \tag{12}
\]

Every derivative in (12) acts on the full clover/transport expression for
X_f before restriction. No dependence of a removed-link coefficient on
remaining links is frozen. Nonforest derivatives of X_e^F are exactly the
corresponding full derivatives restricted to Q. Subtracting their sum from
the first equality of (4) proves (5). Thus even a nonzero reduced
compensator divergence restores the old insertion, rather than adding
another insertion to it. This implements the retained tree-link
derivatives emphasized by Ligterink–Walet–Bishop,
[*Towards a Many-Body Treatment of Hamiltonian Lattice SU(N) Gauge Theory*,
hep-lat/0001028v1](https://arxiv.org/pdf/hep-lat/0001028v1), section 3.2,
(55)–(71), with the present pinned root and generator conventions.

### 4. Reduced Ward identity and the two probes

For invariant O, adding the infinitesimal gauge variation changes no
derivative of O. Since V_a plus that variation is tangent to Q at a slice
point, (3) proves mathsf V_a O^F = (V_a O)^F. This also applies to S_g.
Together with (4) it proves (6). Apply L007's compact product-Haar
integration-by-parts identity on Q to the smooth vector field mathsf V_a
and density exp(-S_g^F). Taking O=1 centers I^F, and the same identity
for arbitrary O^F proves (7).

L010 establishes smoothness and gauge invariance of its centered probes
\(\mathcal O_{3,a,g}\) and \(\mathcal O_{6,a,g}\). Their restrictions mean:
start the full Wilson flow at a forest-slice configuration, then evaluate
the same full probe and subtract its Wilson expectation. The flow is not
assumed to preserve the slice. Its expectation equals the reduced one by
L003, and (6)–(7) therefore apply to both probes with unchanged centering.
Equivariance also makes V_a O and the full insertion invariant, so their
reduced expectations and covariances agree with the full Ward equation.

### 5. Discriminating check and scope

`PYTHONDONTWRITEBYTECODE=1 python3 scripts/forest-ward/check.py` uses exact
rational unit quaternions and dual numbers on the pinned N=4 box. It
checks the same clover rule with one-site rational displacement coefficients
whose supported stencils lie strictly inside the box. Lower-face direction-1
and upper-face reversed direction-2 forests each have 81 tree links. For
both forests the full retraction derivative, preservation of all roots and
forest links, action derivative, reduced divergence and L010's plaquette
divergence agree exactly. The compensator divergence equals the omitted
tree divergence and is nonzero: respectively 322843/709800 and 1304/20475.
This detects the erroneous deletion of the path derivatives. The proof
above, rather than these two coefficient samples, covers L009's actual
displacement, every admissible mesh and both Wilson-flow probes. No Wilson
expectation or ultraviolet limit is estimated by the check.

This result is a **reproduction/specialization** of the assessed finite
tree-gauge and Haar-derivative machinery. It resolves the proposed
representation test. The paths may be long and the gauge contribution
need not have the support of u_a; no locality or mesh-uniform norm bound
is inferred. Equation (4) keeps L010's existing nonzero nonlinear
divergence. No part of L012's off-shell boundary failure or L015's smooth
global BRST normalization obstruction is reversed by this ordinary forest
prescription. There is no complete candidate resolution of the mass-gap
problem, and the required reflected-error threshold remains <= c_box/2.

## Mathlib

Coverage of the full pinned compensated Ward statement: **not checked**.
Coverage of supporting Haar integration, product divergence, Lie
derivatives and rooted-tree path maps: **not checked**. No inspected
Mathlib theorem or direct library link is asserted. Freidel–Livine section
2.1, (2.1)–(2.8), and Ligterink–Walet–Bishop section 3.2, (55)–(71), linked
above, are supporting primary results, rather than matches for the full
boundary-pinned L009 statement. The specific compensator, differentiated
path terms and pointwise divergence comparison are proved here.
