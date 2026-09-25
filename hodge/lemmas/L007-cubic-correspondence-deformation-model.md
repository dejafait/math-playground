# L007 — The cubic correspondence has a non-lci double point

## Hypotheses

Let S be a very general member of [the cubic RM family](../foundations/05-cubic-rm-family.md), with a nonzero, and let X = S x S. Write zeta = exp(2 pi i/7). Let C be the reduced support of the cycle C_1 constructed in L006, so on the dense Weierstrass chart it is parameterized by

\[
 (x,y,v)\longmapsto ((x,y,t),(x,y,s)),\qquad
 t=v+a/v,\quad s=\zeta v+\zeta^{-1}a/v.
\]

Let o be the point of the zero section of S over t = infinity, and p = (o,o). Let I_C be the ideal sheaf of C in X, and put

\[
 \mathcal N=\mathcal Hom_{\mathcal O_C}(I_C/I_C^2,\mathcal O_C).
\]

This is the normal **sheaf**, without an assumption that it is a vector bundle. A first-order deformation is over A = C[epsilon]/(epsilon^2). For a first-order deformation S_A with Kodaira–Spencer class kappa, let X_A = S_A x_A S_A and write kappa_X for its induced class in H^1(X,T_X).

## Conclusion

The cycle C_1 has generic multiplicity one, hence C_1 = [C] as an effective cycle. At p the support has two smooth analytic surface branches meeting transversely in the smooth fourfold X. Its completed local ring is

\[
 \widehat{\mathcal O}_{C,p}\simeq
 \mathbb C[[r_1,r_2,s_1,s_2]]/
 (r_1s_1,r_1s_2,r_2s_1,r_2s_2).
\]

In particular C is not a local complete intersection at p. With B denoting this ring, the completed normal module is

\[
 \widehat{\mathcal N}_p\simeq
 \mathbb C[[r_1,r_2]]^{\oplus2}\oplus
 \mathbb C[[s_1,s_2]]^{\oplus2}
 \quad\text{as a B-module}.
\]

Its fibre at p has dimension four, while its rank on either branch is two. Every formal local first-order embedded deformation at this point is induced by an ambient infinitesimal coordinate change. Thus the singularity both invalidates a rank-two normal-bundle calculation and supplies no local first-order nonlifting certificate by itself.

The exact **global first-order** lifting condition, valid also for this singular C, is

\[
 \operatorname{ob}_C(\kappa):=
 H^1(\delta)\bigl(\kappa_X|_C\bigr)=0
 \quad\text{in }H^1(C,\mathcal N),\qquad
 \delta:T_X|_C\longrightarrow\mathcal N,
 \quad\delta(D)(f)=D(f)\bmod I_C.
\]

Here vanishing is equivalent to the existence of a flat closed subscheme C_A in X_A with special fibre C. No value of this global class is computed for a transverse RM direction. When the marking preserves both NS(S) and the RM action, the flat class [C] stays of Hodge type (2,2), by L006's cohomological decomposition. That fact alone does not give the displayed vanishing, higher-order lifts, or an algebraic family of cycles.

## Proof

**Multiplicity and the two branches.** On the dense chart,

\[
 v=\frac{s-\zeta^{-1}t}{\zeta-\zeta^{-1}}.
\]

The pair of image points therefore recovers v, as well as x and y. The map from the irreducible cover to its image is birational, so the proper pushforward in L006 has generic multiplicity one. Resolution does not alter this degree or the reduced image.

Near o put u = 1/t. The minimal Weierstrass coordinates at infinity are

\[
 X_t=u^4x,\qquad Y_t=u^6y.
\]

These are the usual transitions for a Weierstrass K3 with fundamental line bundle O(2); direct substitution also makes all coefficients regular at u = 0. The zero section is smooth and the elliptic fibration is smooth near its point o, including when other points of this fibre are singular. The resolution of the Weierstrass model does not change this neighbourhood. A fibre parameter there is z = -X_t/Y_t; the expression extends across the zero section and has a simple zero there. Thus (u,z) are local analytic coordinates on S at o.

For an explicit check of this last assertion, write the projective Weierstrass equation as Y_h^2 Z_h = X_h^3 + A(u)X_h Z_h^2 + B(u)Z_h^3. At the zero point [0:1:0], the chart Y_h = 1 has derivative one in Z_h for the left side minus the right side. The equation therefore solves for Z_h in terms of (u,X_h), and z = -X_h on that chart. This also shows directly that no resolution changes this point.

In the second factor use w = 1/s and z' = -X_s/Y_s. On the correspondence the same affine x,y occur in both factors, so

\[
 z'=(u/w)^2z.
\]

The base map v -> t has precisely two preimages of infinity, namely v = infinity and v = 0, and is unramified at both. Near v = infinity, using q = 1/v, its two target base coordinates are

\[
 u=\frac{q}{1+aq^2},\qquad
 w=\frac{q}{\zeta+\zeta^{-1}aq^2}.
\]

Consequently w/u tends to zeta^(-1). Near v = 0 the formulas are

\[
 u=\frac{v}{a+v^2},\qquad
 w=\frac{v}{\zeta^{-1}a+\zeta v^2},
\]

and w/u tends to zeta. Each gives an analytic map from a neighbourhood of o in the first S to the second S: its base coordinate is w(u), and its fibre coordinate is (u/w(u))^2 z. The ratios are analytic units. These maps agree with the original correspondence off infinity and hence give its two branches through p.

There are no additional branches at p. Indeed, over a sufficiently small analytic neighbourhood of o, the degree-two base change of S is the disjoint union of these two neighbourhoods, because the base map is unramified at its two preimages. The second rational map is regular on both by the displayed coordinates. Their two graph images are closed over this neighbourhood and contain the dense part used to define C. Taking the reduced closure therefore gives exactly their union.

In the coordinates (u,z) and (w,z'), the derivatives of these graph maps at o are

\[
 M_\infty=\operatorname{diag}(\zeta^{-1},\zeta^2),
 \qquad M_0=\operatorname{diag}(\zeta,\zeta^{-2}).
\]

Their difference is invertible, since

\[
 \det(M_\infty-M_0)
 =(\zeta^{-1}-\zeta)(\zeta^2-\zeta^{-2})\ne0.
\]

Neither factor vanishes for a primitive seventh root. Graph tangent planes of two linear maps have zero intersection precisely when their difference is invertible. The two surface branches are thus transverse.

**The ideal and failure of the local complete intersection hypothesis.** Two transverse smooth surface branches in a smooth fourfold can be simultaneously straightened in analytic coordinates: take two local defining functions for each branch; their four differentials are independent, so the analytic inverse function theorem makes these four functions coordinates. In the completed ambient ring

\[
 R=\mathbb C[[r_1,r_2,s_1,s_2]],
\]

the branch ideals are (r_1,r_2) and (s_1,s_2). Since C is reduced, its ideal is their intersection. A power series belongs to that intersection exactly when every monomial contains an r and an s, whence

\[
 I=(r_1,r_2)\cap(s_1,s_2)
   =(r_1s_1,r_1s_2,r_2s_1,r_2s_2).
\]

The four quadratic generators are linearly independent modulo m_R I: that latter ideal has no nonzero quadratic homogeneous part. They generate I, so Nakayama's lemma gives exactly four minimal generators. The ideal has height two. A regular codimension-two embedding in the smooth ambient space would have a two-generator regular-sequence ideal, contradicting this count. A local complete intersection before completion would remain one after completion. Thus C is not lci at p. The criterion agrees with the [Stacks Project's definition of a local complete intersection, Section 10.135](https://stacks.math.columbia.edu/tag/00S8); the generator calculation here is the proof for this support.

**The completed normal module.** Set B = R/I. An element of B is a pair of power series on the two planes whose constant terms agree. Let phi: I -> B be R-linear and write phi_ij = phi(r_i s_j). Such maps are the same as Hom_B(I/I^2,B).

The relations

\[
 r_2\phi_{1j}=r_1\phi_{2j},\qquad
 s_2\phi_{i1}=s_1\phi_{i2}
\]

force the constant term of every phi_ij to be zero. Decompose each image uniquely as f_ij(r) + g_ij(s), with both summands having zero constant term. Restrict the first relation to the r-plane. Because r_1 and r_2 are relatively prime in C[[r_1,r_2]], it gives

\[
 f_{1j}=r_1A_j(r),\qquad f_{2j}=r_2A_j(r)
\]

for a unique A_j. The second relation restricted to the s-plane gives unique B_i with g_i1 = s_1 B_i(s) and g_i2 = s_2 B_i(s). Therefore

\[
 \phi(r_i s_j)=r_i A_j(r)+s_j B_i(s).
\]

Conversely, arbitrary four series A_1,A_2,B_1,B_2 give such a homomorphism: use the ambient derivation D defined by D(s_j) = A_j(r), D(r_i) = B_i(s), and restrict D to I modulo I. This also shows directly that all ideal relations, not just the four displayed ones, are respected. Uniqueness gives the asserted B-module decomposition. Completion commutes with this Hom calculation because I/I^2 is finitely presented.

Modulo the maximal ideal, the module has four independent constants, whereas away from the intersection point it is the rank-two normal module of a smooth branch. It cannot be a locally free rank-two module at p. Every phi is induced by D, so the ambient automorphism 1 + epsilon D realizes it to first order. This is a statement about formal local embedded deformations modulo infinitesimal ambient automorphisms; it neither glues these automorphisms globally nor asserts a nonzero global obstruction.

**The global first-order criterion.** We give the ideal-sheaf argument to avoid applying a smooth-subvariety theorem outside its hypotheses. Cover the smooth X by affine opens over which X_A is trivial. Such local trivializations exist for a first-order deformation of a smooth affine scheme: its coordinate algebra is formally smooth, and a section to the square-zero reduction, together with flatness over A, identifies the deformation with the trivial one. On overlaps the trivializations differ by 1 + epsilon D_ij, with D_ij representing kappa_X.

For any ideal J in an affine C-algebra R_0, the first-order ideals in R_0[epsilon] that reduce to J and have flat quotient over A are parametrized by

\[
 \phi\in\operatorname{Hom}_{R_0}(J,R_0/J).
\]

Explicitly the corresponding ideal consists of f + epsilon g with f in J and g mod J = phi(f). R_0-linearity makes this an ideal; its intersection with epsilon R_0 is epsilon J. The latter equality verifies flatness by the square-zero flatness criterion. Conversely flatness gives this equality for any lift, making g mod J well-defined and R_0-linear as a function of f. This proves the parametrization, also recorded in Buchweitz–Flenner, [*A Semiregularity Map for Modules and Applications to Deformations*, Lemma 7.6, arXiv version printed p. 50](https://arxiv.org/pdf/math/9912245#page=50).

Apply this with J = I_C on each open. Local lifts are parametrized by sections phi_i of N. Under a transition 1 + epsilon D_ij the change in the parameter is delta(D_ij). Thus these ideals glue if and only if the Cech 1-cocycle delta(D_ij) is a coboundary. The affine cover and its affine intersections compute cohomology of the coherent sheaf N, so this is exactly the displayed vanishing in H^1(C,N). Changing ambient trivializations adds a coboundary and does not change the class. This proves both necessity and sufficiency for the stated first-order lift. It does not identify H^1(C,N) with the full obstruction theory for arbitrary higher-order lifts of a non-lci subscheme.

**Hodge preservation and the remaining gap.** L006 shows that [C_1] acts on T(S) as U, the cubic RM generator. Its remaining Kunneth components lie in NS(S)_Q tensor NS(S)_Q and the two degree-zero/degree-four summands. There are no rational mixed NS/transcendental Hodge tensors. Keeping the marked NS lattice and RM action fixed consequently preserves all these Hodge types and the (2,2) type of the flat class [C]. This is only the cohomological condition.

For comparison, Ran's [*Semiregularity, obstructions and deformations of Hodge classes*, Theorem 0, printed pp. 809–810](https://www.numdam.org/article/ASNSP_1999_4_28_4_809_0.pdf#page=2), assumes an embedded submanifold and puts relative obstructions in the kernel of a semiregularity map; vanishing would additionally need control of that kernel. This support is not such a submanifold, and even the lci hypothesis for a normal-bundle version fails. Singular versions exist: Buchweitz–Flenner [Theorem 7.8 and Remark 7.11(1), printed pp. 50–51](https://arxiv.org/pdf/math/9912245#page=50) use the appropriate cotangent obstruction space and distinguish its lci specialization. No required injectivity is proved here. Replacing C by the smooth resolution W used for its pushforward cycle does not make W an embedded submanifold of X.

The present computation therefore stops the smooth-support semiregularity shortcut. It does not stop all deformation methods, obstruct a different cycle representative, or contradict the Hodge conjecture. The unresolved quantitative test is whether ob_C vanishes on the fourth RM tangent direction beyond the three-dimensional explicit family. The required transcendental span remains three and the required total dimension remains 21; no additional surface outside the known family has been shown to attain it here.

The supporting command `python3 scripts/cubic-deformation/check_local_model.py` checks the nonzero determinant exactly modulo the seventh cyclotomic polynomial, the four quadratic generators, and the graded normal-module dimensions in image degrees zero through five. These finite computations support the local formulas; the all-degree normal-module argument and the geometric and global qualifications are proved above.

## Mathlib

Coverage of the full statement: **not checked**. No full matching theorem, supporting Mathlib name, or absence is claimed. The Stacks local-complete-intersection definition, Buchweitz–Flenner Lemma 7.6 and Theorem 7.8/Remark 7.11(1), and Ran Theorem 0 are named external supporting references with direct links above, not Mathlib matches or citations for this particular correspondence's singularity. L006 supplies the geometric correspondence and its cohomological action; the local singularity, normal module, and first-order ideal-gluing criterion are proved here. No global transverse obstruction value is asserted.
