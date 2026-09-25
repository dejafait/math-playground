# L004 — Totally real isometries do not enlarge the diagonal span

## Hypotheses

Let S be a smooth quartic surface in complex projective three-space. Use V = H^2(S,Q), N = NS(S)_Q, T = N perpendicular to the cup-product form q, X = S x S, D^2(X), and the correspondence map Phi of L003. Assume that the **full** algebra E = End_Hdg(T) is a totally real number field. Write d = [E:Q] and rho = dim_Q N.

Let O_Hdg(T,q) consist of the Q-linear Hodge automorphisms of T that preserve q. For each rational Hodge isometry f of V, let z_f be its corresponding class in the middle Kunneth summand V tensor V of Hdg^2(X), using the convention T_z(v) = (pi_2)_*(pi_1^*v cup z). Define

\[
B=D^2(X)+\operatorname{span}_{\mathbb Q}\{z_f:f\in O_{\mathrm{Hdg}}(V,q)\}.
\]

Also allow finite chains of rational Hodge isometries of full second cohomology through smooth projective complex K3 surfaces, starting and ending at S. For each chain take the composition of its algebraic correspondence classes. Let B_chain be the rational span of these classes together with D^2(X).

## Conclusion

\[
O_{\mathrm{Hdg}}(T,q)=\{\operatorname{id}_T,-\operatorname{id}_T\},
\qquad
\operatorname{span}_{\mathbb Q}O_{\mathrm{Hdg}}(T,q)
=\mathbb Q\operatorname{id}_T.
\]

The classes defining B and B_chain are algebraic, and

\[
B=B_{\mathrm{chain}}=D^2(X)+\mathbb Q[\Delta_S],
\qquad \Phi(B)=\mathbb Q\operatorname{id}_T.
\]

Consequently,

\[
\dim B=\rho^2+3,\qquad
\dim\operatorname{Hdg}^2(X)=\rho^2+2+d,\qquad
\dim\bigl(\operatorname{Hdg}^2(X)/B\bigr)=d-1.
\]

For d > 1 the tested isometry mechanism supplies none of the residual directions beyond the diagonal. This is a conditional statement for any S with the stated full endomorphism field, not a construction of such a quartic and not a nonalgebraicity result. The conjecture for X still asks for Phi(A^2(X)) = E, which may be achieved by other correspondences.

## Proof

**The action on the holomorphic line detects field elements.** L003 gives the rational orthogonal Hodge decomposition V = N direct sum T, the nondegenerate form on T, and the one-dimensional space T^(2,0) = H^(2,0)(S). Choose a nonzero omega in this line. For a in E define sigma(a) by a(omega) = sigma(a) omega. Since all elements preserve Hodge types, sigma: E -> C is a unital Q-algebra homomorphism. Its kernel is an ideal in a field and does not contain 1, so it is injective. The totally real hypothesis implies sigma(E) is contained in R.

The cup-product pairing pairs only complementary Hodge types, and its restriction between T^(2,0) and T^(0,2) is perfect by nondegeneracy on T, as in L003. Complex conjugation makes the nonzero vector conjugate(omega) span T^(0,2). Hence q(omega, conjugate(omega)) is nonzero.

For u in O_Hdg(T,q), rationality means u commutes with complex conjugation. Therefore

\[
q(\omega,\bar\omega)
=q(u\omega,u\bar\omega)
=\sigma(u)\overline{\sigma(u)}q(\omega,\bar\omega)
=\sigma(u)^2q(\omega,\bar\omega).
\]

It follows that sigma(u)^2 = 1. Injectivity of sigma implies u = id_T or u = -id_T. Both preserve q and the Hodge structure, proving the group and span assertions. The argument uses the full field E; merely containing a totally real subfield would not suffice.

**Passage to the cohomology appearing in Buskin's theorem.** A rational Hodge isometry f of V maps the rational (1,1)-space N onto itself. Orthogonality then implies f(T) = T, and its restriction to T is a rational Hodge isometry, hence is +id_T or -id_T. Conversely any u in O_Hdg(T,q) extends as id_N direct sum u to a rational Hodge isometry of V. This extension uses only the rational orthogonal decomposition; no claim of integrality or preservation of an ample cone is needed.

Buskin's Theorem 1.1, stated with its exact scope in [the standard isometry input](../foundations/03-buskin-isometry-theorem.md), makes every z_f algebraic. Since Phi(z_f) = f restricted to T, L003 gives

\[
z_f\in\Phi^{-1}(\mathbb Q\operatorname{id}_T)
=D^2(X)+\mathbb Q[\Delta_S].
\]

Thus B is contained in the displayed diagonal span. Conversely, the identity isometry gives Phi(z_id) = id_T = Phi([Delta_S]), so z_id - [Delta_S] belongs to D^2(X). The reverse inclusion follows. The divisor-product classes are already algebraic by L003.

**Closed chains do not enlarge the space.** Let S_0 = S, S_1, ..., S_m = S be such a chain and f_i: H^2(S_(i-1),Q) -> H^2(S_i,Q) its isometries. Their composition f_m ... f_1 is a rational Hodge self-isometry of V. If c_i denotes the algebraic class inducing f_i, composition is implemented by the usual correspondence formula

\[
c_2\circ c_1=(p_{13})_*
\bigl(p_{12}^*c_1\smile p_{23}^*c_2\bigr),
\]

on a product of three surfaces, and iteratively for a longer chain. Pullback, intersection, and proper pushforward preserve algebraicity. The projection formula makes its action on second cohomology f_2 f_1, and hence the chain acts as f_m ... f_1. In particular its image under Phi is +id_T or -id_T. L003 puts every resulting class in D^2(X) + Q[Delta_S]. Chains of length one include all z_f, which proves B_chain = B. The same containment survives rational linear combinations and further compositions of these chain classes: their actions on T remain rational scalar identities. Inserting a divisor-product self-correspondence at S contributes zero action on T.

Finally the dimension formulas and the exact algebraicity threshold are those of L003 with dim_Q E = d. In particular d = 1 is consistent with its positive scalar case, while for d > 1 the achieved transcendental span has dimension 1 instead of the required d. Failure of this prescribed supply of algebraic classes says nothing about the algebraicity of the remaining classes.

## Mathlib

Coverage of the full statement: **not checked**. No full or supporting Mathlib match, and no Mathlib absence, is claimed. Huybrechts, [Chapter 3, section 3.5, p. 59 in the author's draft](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=59), matches the rational-isometry calculation; it does not state this exact generated-correspondence conclusion. Buskin's [Theorem 1.1](https://arxiv.org/pdf/1510.02852v3#page=2) supplies algebraicity of isometries. The quotient, kernel, and dimensions used in the proof are supplied by L003. The projection formula and cycle-class functoriality are supporting inputs, not a full library match.
