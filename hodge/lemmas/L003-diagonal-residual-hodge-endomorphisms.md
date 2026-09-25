# L003 — Residual Hodge classes and transcendental endomorphisms

## Hypotheses

Let S be a smooth quartic surface in complex projective three-space, X = S x S, and pi_1, pi_2 the projections. Write V = H^2(S,Q),

\[
q(u,v)=\int_S u\smile v,\qquad
N=\operatorname{NS}(S)_{\mathbb Q}=\operatorname{Hdg}^1(S)\subset V,
\qquad T=N^{\perp_q}.
\]

Here NS(S)_Q denotes its image in cohomology; the equality with rational (1,1)-classes is Lefschetz (1,1). Let E = End_Hdg(T), the rational vector space of Q-linear endomorphisms whose complexifications preserve each Hodge summand of T. Let D^2(X) be the rational span of products of divisor classes on X, and let Delta_S be the diagonal. Let h be the hyperplane class of S and H = pi_1^*h + pi_2^*h.

For z in Hdg^2(X), use the correspondence convention of L002:

\[
T_z(v)=(\pi_2)_*(\pi_1^*v\smile z).
\]

## Conclusion

Restriction defines a surjective map Phi(z) = T_z restricted to T, with exact sequence of rational vector spaces

\[
0\longrightarrow D^2(X)\longrightarrow\operatorname{Hdg}^2(X)
\xrightarrow{\ \Phi\ }E\longrightarrow0,
\qquad \Phi([\Delta_S])=\operatorname{id}_T.
\]

Consequently,

\[
\frac{\operatorname{Hdg}^2(X)}{D^2(X)+\mathbb Q[\Delta_S]}
\ \simeq\ \frac{E}{\mathbb Q\operatorname{id}_T}.
\]

This is a quotient of vector spaces, not a claimed quotient algebra. Each class modulo D^2(X) has a unique representative in the rational (2,2)-part of T tensor T, and that representative is H-primitive.

If rho = dim_Q N, the dimensions are

\[
\dim D^2(X)=\rho^2+2,\qquad
\dim\bigl(D^2(X)+\mathbb Q[\Delta_S]\bigr)=\rho^2+3,
\]
\[
\dim\operatorname{Hdg}^2(X)=\rho^2+2+\dim E,
\qquad
\dim\frac{\operatorname{Hdg}^2(X)}{D^2(X)+\mathbb Q[\Delta_S]}
=\dim E-1.
\]

With A^2(X) the rational algebraic cycle-class image, the codimension-two Hodge conjecture for X is equivalent to Phi(A^2(X)) = E. In particular it holds if E = Q id_T. The exact sequence alone does not prove that every element of E is algebraic.

## Proof

**Orthogonal splitting over Q.** Use the geometric facts established in L002: S is connected, H^1(S,Q) = H^3(S,Q) = 0, H^4(S,Q) = Qe for a point class with integral one, h^2 = 4e, and H^(2,0)(S) is nonzero. The named geometric theorems are recorded in [the standard inputs](../foundations/02-standard-inputs.md).

The Hodge index theorem makes q restricted to N nondegenerate. Poincare duality makes q nondegenerate on V, so

\[
V=N\oplus T
\]

is a rational orthogonal direct sum with nondegenerate restrictions. It is also a direct sum of Hodge structures: N is entirely of type (1,1), and the cup-product pairing is zero between Hodge components unless their types sum to (2,2). Orthogonality to N therefore imposes a condition only on the (1,1)-component and is preserved by Hodge decomposition. In particular H^(2,0)(S) is contained in T_C, so T is nonzero.

There is no nonzero rational (1,1)-vector in T. Indeed, Lefschetz (1,1) puts any such vector in N, and N intersect T = 0. This does not assert that the complex (1,1)-summand of T vanishes.

**Precisely which Kunneth pieces are divisor products.** The odd-cohomology vanishing gives

\[
H^4(X,\mathbb Q)=
\mathbb Q(e\otimes1)\ \oplus\ (V\otimes V)\ \oplus\ \mathbb Q(1\otimes e),
\]

and H^2(X,Q) is the direct sum of the two copies of V. Kunneth respects Hodge types. Thus every rational divisor class on X is the sum of pullbacks of elements of N. Conversely, every element of N is a rational divisor class by Lefschetz (1,1), so all such pullbacks occur. Expanding products gives

\[
D^2(X)=\mathbb Q(e\otimes1)\ \oplus\ (N\otimes N)\ \oplus\ \mathbb Q(1\otimes e).
\]

Both outer summands occur because h^2 = 4e; every a tensor b with a,b in N is a product of divisor pullbacks. Directness follows from Kunneth. This proves dim D^2(X) = rho^2 + 2 and also D^2(X) contained in A^2(X).

Now split the middle piece by V = N direct sum T. A rational (2,2)-class in N tensor T is zero. To see this without an assumption on Picard rank, choose a rational basis n_1,...,n_rho of N and express the class uniquely as the sum of n_j tensor t_j with t_j in T over Q. Each n_j has type (1,1); hence the condition that the sum have type (2,2), and complex linear independence of the n_j, force every t_j to have type (1,1). The preceding paragraph makes all t_j zero. The same argument applies to T tensor N. Since this is a rational splitting by Hodge structures, the components of a rational Hodge class are themselves rational Hodge classes. We obtain the direct sum

\[
\operatorname{Hdg}^2(X)=D^2(X)\oplus K,
\qquad K=(T\otimes_{\mathbb Q}T)\cap H^{2,2}(X).
\]

**The remaining tensor space is the endomorphism space.** Nondegeneracy of q on T gives a rational linear isomorphism

\[
\Theta:T\otimes T\xrightarrow{\sim}\operatorname{End}_{\mathbb Q}(T),
\qquad
\Theta(a\otimes b)(v)=q(v,a)b.
\]

For r = 0,1,2, the pairing identifies T^(2-r,r) with the complex dual of T^(r,2-r). These restrictions are perfect because q is nondegenerate and all other pairings of Hodge types vanish. Thus the complex type-(2,2) subspace of T tensor T is identified by Theta with

\[
\bigoplus_{r=0}^2\operatorname{End}_{\mathbb C}(T^{r,2-r}),
\]

the block diagonal endomorphisms for the Hodge decomposition. Intersecting with the rational structures proves Theta(K) = E. This proves both directions of the type condition, not merely that a Hodge tensor induces a Hodge endomorphism.

The projection formula gives T_(a tensor b)(v) = q(v,a)b for the middle Kunneth summand. The outer summands act by zero on H^2(S,Q): for e tensor 1 the first-factor product has degree six, while for 1 tensor e its first-factor degree is too small to integrate. The N tensor N piece acts by zero on T by orthogonality. It follows that every rational (2,2)-class acts on T with image in T, that Phi has kernel exactly D^2(X), and that its restriction to K is Theta, hence is surjective. The rational inverse of Theta constructs cohomology tensors only; no algebraicity of those tensors is being assumed.

The diagonal-action calculation in L002 gives T_([Delta_S]) = id on V. Thus Phi([Delta_S]) = id_T. Taking inverse images of the scalar subspace yields

\[
\Phi^{-1}(\mathbb Q\operatorname{id}_T)
=D^2(X)+\mathbb Q[\Delta_S],
\]

which proves the asserted quotient identification. Since T is nonzero, the identity spans one rational dimension and the stated dimension formulas follow.

**Primitivity and the actual algebraicity threshold.** For every t in T, the class h cup t is q(h,t)e = 0, since h belongs to N. Consequently cup product with H kills every tensor in T tensor T. The direct-sum decomposition gives the unique representative in K, and it is H-primitive.

If Phi(A^2(X)) = E and z belongs to Hdg^2(X), choose an algebraic class a with Phi(a) = Phi(z). Then z-a belongs to D^2(X), which is algebraic, so z is algebraic. Conversely, A^2(X) = Hdg^2(X) implies Phi(A^2(X)) = E by surjectivity. When E = Q id_T, the algebraic diagonal already spans the image and proves this equality. When E is larger, the unconstructed endomorphisms cannot be declared algebraic by the tensor identification. The conclusion is restricted to this family of fourfolds.

## Mathlib

Coverage of the full statement: **not checked**. No full or supporting Mathlib theorem match, and no library absence, is asserted. The Hodge index theorem and the tensor/Hom convention have direct references in foundations/02-standard-inputs.md; Kunneth, Poincare duality, Lefschetz (1,1), and cycle-class compatibility are supporting mathematical inputs. The quotient, exact kernel, and primitive representative are proved here rather than attributed to a matching library theorem.
