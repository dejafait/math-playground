# L007 — A compact local translation does not isolate the stress triplet

## Hypotheses

Let D = (-4,4)^4. For a smooth vector field u and a symmetric tensor T, write

\[
\tau=\sum_\mu T_{\mu\mu},\qquad
t_\mu=T_{\mu\mu}-\tau/4,\qquad
d_\mu(u)=\partial_\mu u_\mu-\operatorname{div}u/4,
\]
\[
s_{\mu\nu}(u)=\partial_\mu u_\nu+\partial_\nu u_\mu\quad(\mu<\nu),
\qquad
\mathcal K_u[T]=\int_D\sum_{\mu,\nu}\partial_\mu u_\nu\,T_{\mu\nu}.
\]

The geometric assertions concern all smooth symmetric tensors, without assuming that a quantum stress tensor has been constructed. Tensor distributions can also be paired with compactly supported smooth strains. A continuum Ward equation below is a *normalization condition to be justified*, not an established interacting Yang–Mills identity.

For the exact finite-lattice identity, use the product of SU(2) variable links with links contained in the boundary fixed to identity, and the probability density

\[
Z^{-1}e^{-S}dH,\qquad
S=\frac4{g^2}\sum_p\left(1-\tfrac12\operatorname{Tr}U_p\right),\quad g>0.
\]

Here dH is product normalized Haar measure. V is any smooth vector field on this finite product, acting only on variable links, and O is any smooth real observable. For interpreting diagonal insertions, use the centered site plaquette averages of L006 and set

\[
\widehat t_\mu=2\sum_{\nu\ne\mu}\widehat h_{\mu\nu}
-\sum_{\alpha<\beta}\widehat h_{\alpha\beta},
\qquad
\widehat D=\widehat h_{12}-\widehat h_{34}.
\]

Thus \(\sum_\mu\widehat t_\mu=0\), and L006's stress normalization gives \(\widehat t_1+\widehat t_2-\widehat t_3-\widehat t_4=4\widehat D\). This algebraic identity is exact for these lattice definitions; their identification with a matched interacting stress tensor remains open.

## Conclusion

The strain contraction decomposes exactly as

\[
\mathcal K_u[T]=\int_D\left[
\sum_\mu d_\mu(u)t_\mu
+\sum_{\mu<\nu}s_{\mu\nu}(u)T_{\mu\nu}
+\frac{\operatorname{div}u}{4}\tau\right]. \tag{1}
\]

There is **no nonzero** \(u\in C_c^\infty(D;\mathbb R^4)\) with all off-diagonal strains \(s_{\mu\nu}(u)=0\). In particular, no such displacement selects only the diagonal traceless channel as an identity for arbitrary symmetric tensors. This does not exclude cancellations after pairing with a specially chosen probe or combining several Ward equations.

For \(k=(1,1,-1,-1)\), the affine displacement \(v_\mu=k_\mu x_\mu\) selects \(t_1+t_2-t_3-t_4\), equal to \(4(h_{12}-h_{34})\) for the classical curvature stress normalization of L006, but does not preserve the fixed box. Its integration-by-parts formula retains a surface term. There exists an explicit compactly supported divergence-free displacement equal to v near any prescribed compact set in D. It removes the singlet term in (1), while necessarily retaining off-diagonal strain in the transition region.

At fixed lattice spacing the exact identity is

\[
\mathbb E[VO]=\operatorname{Cov}(O,I_V),\qquad
I_V=VS-\operatorname{div}_H V,\qquad \mathbb E I_V=0. \tag{2}
\]

It does not identify \(I_V\) with the triplet insertion. For the compact divergence-free construction, a proposed triplet/shear normalization has the form

\[
W_O=z_3 C_3(O)+z_6 C_6(O)+r_O. \tag{3}
\]

The terms are specified in the proof. Unless the shear response is canceled or independently matched and the residual is controlled, this is not a determination of \(z_3\). There is no estimate here of a matching coefficient's finiteness, of a residual as the cutoff is removed, or of the interacting reflection error required to be at most \(c_{\rm box}/2\).

## Proof

### 1. Local strain and the fixed boundary

Separate the diagonal and off-diagonal terms in the definition of \(\mathcal K\). Symmetry of T pairs the two terms for each unordered off-diagonal index pair. Substituting \(T_{\mu\mu}=t_\mu+\tau/4\), and using \(\sum t_\mu=0\), gives (1). These are algebraic equalities, including for distributional T when all smearing functions have compact support.

For its classical translation interpretation, use a smooth connection with action density \(\mathcal L=(4g^2)^{-1}\sum_{c,\alpha,\beta}(\mathcal F^c_{\alpha\beta})^2\), and tensor

\[
T_{\mu\nu}=\frac1{g^2}\sum_{c,\alpha}
\mathcal F^c_{\mu\alpha}\mathcal F^c_{\nu\alpha}
-\frac{\delta_{\mu\nu}}{4g^2}
\sum_{c,\alpha,\beta}(\mathcal F^c_{\alpha\beta})^2.
\]

The gauge-covariant variation \(\delta_u\mathcal A_\nu=u_\rho\mathcal F_{\rho\nu}\) gives, by differentiating the curvature and using its Bianchi identity,

\[
\delta_u\mathcal F_{\mu\nu}
=(\partial_\mu u_\rho)\mathcal F_{\rho\nu}
-(\partial_\nu u_\rho)\mathcal F_{\rho\mu}
+u_\rho D_\rho\mathcal F_{\mu\nu}.
\]

Contracting with \(\mathcal F_{\mu\nu}/(2g^2)\), summing color and coordinate indices, and integrating the term \(u\cdot\partial\mathcal L\) yields

\[
\delta_u S_{\rm cl}=\mathcal K_u[T]
+\int_{\partial D}(u\cdot n)\mathcal L\,d\sigma.
\]

For compact u the surface term vanishes. This motivates the intended quantum normalization condition
\(W_O^{\rm R}(u)=\int_D\partial_\mu u_\nu\,\langle T^{\rm R}_{\mu\nu}O\rangle_c\),
where the left side must be the response to a normalized local translation and the products/contact terms must be defined. The classical computation does not establish that quantum condition. The lattice version below keeps its residual explicitly.

For \(v_\mu=k_\mu x_\mu\), the divergence and all shear coefficients vanish, while \(d_\mu=k_\mu\). Consequently \(\mathcal K_v[T]=\int_D(t_1+t_2-t_3-t_4)\). For a smooth tensor on the closed box, the divergence theorem gives

\[
\int_D\sum_\mu k_\mu t_\mu
=\int_{\partial D} n_\mu v_\nu T_{\mu\nu}\,d\sigma
-\int_D v_\nu\partial_\mu T_{\mu\nu}. \tag{4}
\]

Indices in (4) are summed. A compact-support translation identity for the divergence cannot simply be applied to v: v has a nonzero normal component on each face, and its flow moves those faces. Equation (4) is a geometric identity, not an assertion that the fixed-boundary path integral has a boundary Ward identity with no additional terms.

Fixing tangential gauge fields to zero does not set the displayed stress flux to zero. Here is a classical check of that implication. Near the upper face \(x_4=4\), choose a single-color connection with

\[
\mathcal A_1=(4-x_4)\eta(x_4)\rho(x_1,x_2,x_3)T^1,
\qquad \mathcal A_2=\mathcal A_3=\mathcal A_4=0,
\]

where \(\rho\) is a nonzero smooth bump supported away from the lateral faces, and \(\eta\) equals one near the upper face and vanishes away from it. All tangential boundary components vanish on every face. On the upper face the only nonzero curvature is \(\mathcal F^1_{41}=-\rho\). The classical tensor above therefore has \(T_{44}=\rho^2/(2g^2)\) and \(T_{4j}=0\) for \(j\ne4\) there. The surface term in (4) is \(-4\int \rho^2/(2g^2)\), which is nonzero. This is a boundary-condition test, not a classical solution or a quantum expectation calculation.

### 2. Why a compact displacement cannot remove every shear coefficient

Extend \(u\in C_c^\infty(D;\mathbb R^4)\) by zero to \(\mathbb R^4\). Suppose \(s_{ij}=0\) for every \(i\ne j\). Fix a component k and choose distinct i,j different from k. Commuting derivatives gives

\[
2\partial_i\partial_j u_k
=\partial_i s_{jk}+\partial_j s_{ik}-\partial_k s_{ij}=0. \tag{5}
\]

For fixed other coordinates, \(\partial_j u_k\) is constant in \(x_i\). It vanishes when \(|x_i|\) is large, by compact support, so it is zero everywhere. Then \(u_k\) is constant in \(x_j\), and the same compact-support argument makes it zero. This applies to every k. The argument needs dimension at least three and requires no Ward identity or equation of motion.

For (1) to depend only on the diagonal traceless part for *every* symmetric T, test T with one arbitrary smooth off-diagonal component and then with an arbitrary scalar multiple of the identity. The fundamental test-function pairing implies \(s_{\mu\nu}=0\) and \(\operatorname{div}u=0\). The first condition already forces u = 0. Nonzero shear coefficients therefore cannot be discarded by an operator-level choice of compact displacement alone. The assertion does not imply that their correlation with every possible probe is nonzero.

### 3. Localize the desired strain without introducing a singlet

Choose \(\chi\in C_c^\infty(D)\) equal to one on a neighborhood of a compact set containing the observable supports. The elementary choice \(u_\nu=\chi k_\nu x_\nu\) gives

\[
r:=\operatorname{div}u=\sum_\nu k_\nu x_\nu\partial_\nu\chi,
\qquad
s_{\mu\nu}=k_\nu x_\nu\partial_\mu\chi
+k_\mu x_\mu\partial_\nu\chi,
\]
\[
\mathcal K_u[T]=\int_D\chi\sum_\mu k_\mu t_\mu
+\int_D\left[
\sum_\mu\left(k_\mu x_\mu\partial_\mu\chi-r/4\right)t_\mu
+\sum_{\mu<\nu}s_{\mu\nu}T_{\mu\nu}+r\tau/4\right]. \tag{6}
\]

Every term after the first is supported where the cutoff varies. Distance from the observable support does not make these correlations zero or cutoff-suppressed; no such estimate is available.

There is a better localization for eliminating the scalar term. Define a smooth antisymmetric matrix field by

\[
\Psi_{13}=\chi x_1x_3,\qquad \Psi_{24}=\chi x_2x_4,
\qquad \Psi_{31}=-\Psi_{13},\quad \Psi_{42}=-\Psi_{24},
\]

with every other entry zero, and set \(u_\mu=\sum_\nu\partial_\nu\Psi_{\mu\nu}\). Antisymmetry and commuting derivatives give \(\operatorname{div}u=0\) identically. On the region where \(\chi=1\), direct differentiation gives \(u=(x_1,x_2,-x_3,-x_4)\). Outside the support of \(\chi\) it vanishes. Thus the core strain is exactly the desired triplet contraction and there is no scalar contribution anywhere. Since u is nonzero, step 2 proves that some shear coefficient remains. It lies in the transition region, where u differs from the affine displacement. Compact support removes the geometric surface term, without removing the effect of the box on correlation functions.

The same construction admits an exact discrete divergence-free version. Extend the sampled \(\Psi\) by zero on the full lattice and use the central differences

\[
\nabla^c_\mu f(x)=\frac{f(x+ae_\mu)-f(x-ae_\mu)}{2a},\qquad
u_{a,\mu}=\sum_\nu\nabla^c_\nu\Psi_{\mu\nu}.
\]

Their commutation and the antisymmetry of \(\Psi\) give \(\sum_\mu\nabla^c_\mu u_{a,\mu}=0\) exactly. For sufficiently small a all these stencils stay away from the boundary. In any core whose two-step stencil stays in \(\{\chi=1\}\), central differentiation of the quadratic polynomials is exact, so the core displacement and strain are v and k. This statement does not equate discrete sampling of a continuum divergence-free field with discrete divergence-freeness; u_a is constructed with the discrete derivatives themselves.

### 4. Exact finite-lattice identity and the missing normalization data

Write \(V=\sum_{e,c}v_e^c L_e^c\), where \(L_e^c\) is a left-invariant Lie derivative on a variable link. Haar invariance gives \(\int L_e^c F\,dH=0\) for every smooth F. Apply it to \(v_e^c Oe^{-S}\), sum over e,c, and use the product rule:

\[
0=\mathbb E[VO+O\operatorname{div}_H V-O VS],
\qquad
\operatorname{div}_H V=\sum_{e,c}L_e^c v_e^c.
\]

Taking O = 1 proves the mean-zero assertion and then (2). All manipulations are finite-dimensional integrations of smooth functions on a compact manifold. No continuous spatial translation symmetry is assumed. A field-dependent V need not have zero Haar divergence. The absence of a configuration-space boundary term does not grant a spatial translation symmetry of the fixed box.

For a precise candidate condition, let \(d_{a,\mu}\) and \(s_{a,\mu\nu}\) use the same central differences and the discrete u_a from step 3. Let \(\widehat S_{\mu\nu}\), \(\mu<\nu\), be any chosen centered, smooth lattice representatives of the off-diagonal stress components with specified normalization. Define

\[
J_3=a^4\sum_{x,\mu}d_{a,\mu}(x)\widehat t_\mu(x),
\qquad
J_6=a^4\sum_{x,\mu<\nu}s_{a,\mu\nu}(x)\widehat S_{\mu\nu}(x).
\]

Their supports stay in the interior. The core part of J_3 is \(4a^4\sum_{x\text{ in core}}\widehat D(x)\); it also includes a diagonal contribution from the transition region. The discrete trace coefficient vanishes exactly. No classification or finite matching theorem for the chosen off-diagonal representatives is being asserted here.

Fix a proposed lattice variation V associated with this displacement. For any proposed numbers \(z_3,z_6\), define

\[
R=I_V-z_3J_3-z_6J_6,
\quad W_O=\mathbb E[VO],\quad
C_i(O)=\operatorname{Cov}(O,J_i),\quad
r_O=\operatorname{Cov}(O,R).
\]

Equation (2) is exactly (3). With this definition of R, (3) is a tautological decomposition, not a proof that R is small. To use it as a continuum translation normalization requires an independently justified approximation of \(I_V\), control of contact and boundary effects, and a normalization of V as a translation generator. Finite group integration supplies none of these limits.

Even if that additional work made r_O known, and \(C_3(O)\ne0\), the equation would give only

\[
z_3=\frac{W_O-z_6C_6(O)-r_O}{C_3(O)}.
\]

With \(C_6(O)\ne0\), one equation leaves z_3 undetermined when z_6 is unknown. If a probe has \(C_6(O)=0\), or several conditions eliminate the shear response, this particular obstruction does not apply; such a cancellation has not been established for the notebook's observable. Two probes could instead give a nonsingular response matrix, but its rank, stability in the cutoff, and residual estimates would all need proof. The geometric theorem proves only that the shear term cannot be deleted before choosing and analyzing the probes.

The [source qualification](../foundations/05-lattice-stress-tensor-matching.md#local-translation-identities) records the related lattice translation-breaking and generator-normalization issues in the literature. It is supporting context; the geometric obstruction and the finite Haar identity were proved here. Neither the source nor this condition supplies an interacting reflection comparison, a field construction, or a physical mass bound.

## Mathlib

Coverage of the full local-translation obstruction and its lattice normalization application: **not checked**. Coverage of supporting mixed-derivative commutation, compact-support arguments, the divergence theorem, and invariant integration on compact groups: **not checked**. No inspected Mathlib theorem name or library link is asserted. The primary literature cited in the source qualification is supporting Ward-identity context, not a match for the full statement proved here.
