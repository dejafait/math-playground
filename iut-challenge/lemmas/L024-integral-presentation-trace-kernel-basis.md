# L024 — Integral presentation basis of the trace kernel

## Hypotheses

Let K=Q_3(pi), pi^27=3, O=O_K, G=G_K, U=1+pi O and J=log(O^times), with the continuous logarithm of L016. Fix a presentation **admitted by Kondo's Theorem 1.1**, including its defining closed words x'_0 and x'_1; do not prescribe their reciprocal images. For 0≤i≤27 put u_i=rec_K^(-1)([x_i]) in U and y_i=log(u_i) in J. Here [x_i] is the image in G^ab. The wild-inertia/principal-unit identification, and the agreement of reciprocal rationalization with the actual logarithm, are those used in L019 and L023. This is J, not the shell J/6.

The named inputs are:

- **Kaiji Kondo, Anabelian aspects of the outer automorphism groups of the absolute Galois groups of mixed-characteristic local fields**, **RIMS1991, December 2025**, [primary PDF](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1991.pdf): **Theorem 1.1(1–4), printed p. 8**, reciprocal-coordinate setup, pp. 8–9; **Theorem 1.3, p. 9**, with proof on pp. 9–11. Cross-check: [arXiv:2512.09231v2, December 12, 2025, §1](https://arxiv.org/html/2512.09231v2#S1). The hypotheses are odd residue characteristic, with degree at least two for Theorem 1.3; no Galois or even-degree assumption is used. The admitted presentation has normal wild generators x_0,...,x_27, tame relation sigma tau sigma^(-1)=tau^3, and odd-degree relation

  \[
  \sigma x_0\sigma^{-1}=(x'_0)^t x_1^{3^s}[x_1,x'_1][x_2,x_3]\cdots[x_{26},x_{27}],
  \quad s,t\ge1,\quad x'_0\in\overline{\langle\tau,x_0\rangle}.
  \]

  These are the full defining relations, not merely equalities in a quotient. Theorem 1.3 gives ker(Tr_(K/Q_3))=span_(Q_3)(y_2,...,y_27). Import the presentation and this rational theorem; neither is reproved here.
- **Hoshi–Nishio, On the Outer Automorphism Groups of the Absolute Galois Groups of Mixed-characteristic Local Fields**, **June 2022 revised RIMS1931**, [primary PDF](https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1931revised.pdf): **§1 setup and logarithm diagram, PDF pp. 3–4**, **Lemma 1.3 and proof, PDF p. 5**. Reuse the passage from normal wild generation to integral generation of the reciprocal torsion-free module. Its differently parametrized Proposition 1.1 relator is not substituted for Kondo's relator.
- Local class field theory's reciprocity isomorphism \(\widehat{K^\times}\simeq G^{ab}\), with principal units the wild-inertia image, as used in **Hoshi, Introduction to Mono-anabelian Geometry**, Publications mathématiques de Besançon (2021), 5–44, **Proposition 3.11(i,iv), p. 22** ([published primary PDF](https://www.numdam.org/item/10.5802/pmb.42.pdf)). L019 and L023 justify its unit/logarithm identifications. L016 supplies J's compactness, Z_3-stability and bounds pi^14 O⊆J⊆pi^(-54)O; L019 supplies the torsion-kernel argument.

## Conclusion

The source-defined y_1,...,y_27 form a Z_3-basis of J. Consequently

\[
J\cap\ker(\operatorname{Tr}_{K/\mathbb Q_3})
=\bigoplus_{i=2}^{27}\mathbb Z_3 y_i.
\]

Thus y_2,...,y_27 form the full integral intersection basis, with index one. This is a **REPRODUCTION/specialization** of the cited presentation, generation and rational-kernel results. No novelty, prescribed field coordinates, radius, source-realized violating point, actual-ind3 membership or essential IUT flaw is claimed.

## Proof

### The genuine principal-unit module has no torsion

L016's Eisenstein argument gives [K:Q_3]=27 and residue field F_3. There is no primitive third root of unity in K. Indeed X^2+X+1 has discriminant -3, which is not a square in Q_3 because its valuation is odd. A primitive third root therefore generates a degree-two extension of Q_3; such a subfield cannot lie in an extension of odd degree 27, by the tower formula. Any root of unity of nontrivial 3-power order would yield one of order three by taking a power, so none exists in K.

U is pro-3: the quotients of its principal-unit filtration have order three, and their intersection is {1}, with this filtration giving its topology (the filtration used in L016). A finite-order element of a pro-3 group has 3-power order, as follows by its images in the finite 3-group quotients. Hence U is torsion-free. L019 proves that the kernel of log on O^times is its torsion subgroup, using the inverse log/exp on 1+pi^14 O. Since O^times={±1}×U, log restricts to a continuous bijection U→J. It is a topological isomorphism because U is compact and J is Hausdorff. Continuous powering corresponds to the Z_3-module structure on J; equivalently it follows by taking limits of integer powers. L016's lattice bounds show that J is a free Z_3-module of rank 27: it is a submodule of the finite free module pi^(-54)O and contains the rank-27 submodule pi^14 O.

Choose any uniformizer for the ordinary decomposition K^times≅pi^Z×{±1}×U. Local reciprocity therefore identifies the maximal abelian pro-3 quotient A of G with

\[
A\simeq\mathbb Z_3\oplus U\simeq\mathbb Z_3\oplus J.
\tag{1}
\]

In particular A is torsion-free. The uniformizer choice here computes the abstract quotient only; it does not assign coordinates to any presentation generator.

The projection G^ab→A is injective on its reciprocal subgroup U: in the decomposition G^ab≅Zhat⊕{±1}⊕U it is the identity on the pro-3 factor U. Thus an equality between the images of x_i in A is an equality of their actual reciprocal principal units, not merely an equality modulo an additional unit kernel.

### The full abelianized relator eliminates x_0 integrally

Apply the universal maximal-abelian-pro-3 quotient to the **full** admitted presentation. Before imposing relations, its additive module is free over Z_3 on symbols S,T,X_0,...,X_27 for sigma,tau,x_0,...,x_27. To see this directly, a homomorphism from the free profinite group to any abelian pro-3 group is specified by these generator images; continuous profinite exponents act through their Z_3 components.

Here the closed words belonging to the admitted presentation are fixed before taking any quotient. In particular a representative of x'_0 is a word in the free profinite subgroup on tau,x_0. Its image has only T and X_0 coordinates before imposing the defining relations. Membership of an unspecified element in a closed subgroup after quotienting would not alone authorize this presentation calculation. Kondo Theorem 1.1(1), together with (3) and (4), is the full-presentation input being used.

The tame relation becomes T=3T, hence 2T=0 and T=0 since 2 is a unit in Z_3. Use the defining word for x'_0 from the admitted presentation. Its abelianized image is aT+bX_0 for a,b∈Z_3, because it lies in the closed subgroup generated by tau,x_0. After T=0 this is bX_0. All commutators in the odd-degree relator vanish, including [x_1,x'_1], and conjugation contributes no S-coordinate. Consequently the remaining relation is

\[
cX_0-3^sX_1=0,\qquad c=1-tb\in\mathbb Z_3.
\]

There are no further relation vectors: abelianization sends the closed normal subgroup generated by the defining relators to the closed Z_3-submodule generated by their images. The latter is closed since it is the continuous image of a finite product of compact Z_3 modules. Thus

\[
A\simeq\left(\mathbb Z_3S\oplus\bigoplus_{i=0}^{27}\mathbb Z_3X_i\right)
\Big/\mathbb Z_3(cX_0-3^sX_1).
\tag{2}
\]

One can check the absence of extra relations by the converse universal property. For any finite abelian 3-group D, assign arbitrary images to S,X_0,...,X_27 satisfying cX_0=3^sX_1, and assign zero to T. The admitted words then evaluate in D; both original relators hold. The full presentation supplies a continuous homomorphism G→D with precisely these generator images. Conversely every such homomorphism has these properties. Finite abelian 3-quotients distinguish elements of the compact module in (2), which proves the claimed quotient. The relation submodule is its closed integral span, **not its saturation**; replacing it by its saturation would erase the torsion needed for the next argument.

Necessarily c∈Z_3^times. Otherwise the nonzero vector v=cX_0-3^sX_1 is divisible by 3. Put k=min(v_3(c),s)≥1, taking v_3(0)=+infinity, and w=3^(-k)v. Then w has at least one unit coordinate. Its class in (2) is annihilated by 3^k but is nonzero: w=dv for d∈Z_3 would imply 1=3^k d by a nonzero coordinate, which is impossible. This gives nonzero torsion, contradicting (1). This argument also excludes c=0; it uses the full presentation, not just a relation among elements of an unspecified quotient.

Projecting the resulting equality X_0=(3^s/c)X_1 onto U and then applying log gives

\[
y_0=(3^s/c)y_1,\qquad 3^s/c\in\mathbb Z_3.
\tag{3}
\]

In particular no claim that y_0 vanishes is needed. Nor is any value of b, t or s borrowed from Hoshi–Nishio's different presentation parameters.

To check the logarithm normalization explicitly, let r be reciprocity on fixed units, ell the natural map from reconstructed units to the reconstructed additive space, and F:K_+→k_+(G) the cited additive identification. The diagram checked in L023 is F log=ell r. Consequently the source image ell([x_i]) is exactly F(y_i). Transporting Kondo's rational kernel statement through F therefore uses the actual log(u_i), with no factor 6 and no arbitrary exponent twist. Continuous powers in (3) correspond to Z_3 scalar multiplication under this same log map.

### Normal generation gives an integral basis of J

By Kondo Theorem 1.1(2), the x_i normally topologically generate wild inertia. Their conjugates have identical images in G^ab, so their abelianized images topologically generate its wild-inertia image, which is U by the cited reciprocal identification. Passing through log gives topological additive generation of J by y_0,...,y_27. To check ordinary integral generation, the map

\[
\mathbb Z_3^{28}\longrightarrow J,\qquad (a_i)\longmapsto\sum_{i=0}^{27}a_i y_i
\]

is continuous and has compact, hence closed, image. It contains every integer sum of the generators, and therefore their closure, which is J. Conversely all its values lie in J by Z_3-stability. This is the integral-generation passage used in Hoshi–Nishio Lemma 1.3, applied to the actual admitted generators.

Equation (3) now gives J=∑_(i=1)^27 Z_3 y_i. Since J spans the 27-dimensional Q_3-space K, these 27 generators span K and are Q_3-linearly independent. Their Z_3-linear independence follows immediately. They are therefore a Z_3-basis of the whole J, including the deep ideal and all unit layers; finite logarithm approximations are not used.

### Intersect the cited rational kernel with this integral basis

Apply Kondo Theorem 1.3 with p=3 and odd d=27. It states that the trace kernel is precisely the Q_3-span of y_2,...,y_27. Because y_1,...,y_27 is a basis of K and Tr(1)=27≠0, Tr(y_1)≠0. Every z∈J has a unique expression z=∑_(i=1)^27 a_i y_i with a_i∈Z_3, and

\[
\operatorname{Tr}(z)=a_1\operatorname{Tr}(y_1).
\]

Since Q_3 is a field, this vanishes exactly when a_1=0. This proves the asserted integral intersection and its basis without assuming primitive trace values or comparing rational spans as if they were integral lattices.

**Critical audit, 2026-10-06.** The full-presentation quotient, nonsaturated closed relation submodule, absence of 3-primary unit torsion, injection of U into A, closed integral generation and reciprocal/logarithm normalization have been checked. The index-one conclusion survives. This verifies the existing specialization; it changes no mathematical conclusion and supplies no new bound. Kondo's presentation and rational trace theorem remain imported inputs, not independently reproved theorems. The unchanged Hoshi–Nishio integral-generation coverage is reused; the compact-image argument above explicitly supplies the needed specialization.

**Qualification and downstream use.** The step closes the integral normalization obligation for this source-defined presentation. It can support a later lattice or finite-quotient test of source-defined actions. It neither realizes an arbitrary basis in a presentation nor gives its field-valued coordinates, an action matrix, or an envelope radius. L020's smaller-input containment and L018–L019's old-involution exclusions remain intact. Original-data applicability, permitted native actions, actual-ind3 inputs, higher powers, pilot transport, essentiality and original finite B≥A remain unresolved.

## Mathlib

Full matching integral presentation/trace-kernel theorem: **not checked**. Supporting local reciprocity, continuous unit logarithm, free-module quotient, torsion and trace-kernel basis coverage: **not checked**. Unknown availability is not evidence of absence. The cited primary theorems provide presentation existence and rational trace-kernel coverage; the proof above supplies only the approved integral specialization and its topology/torsion justifications.
