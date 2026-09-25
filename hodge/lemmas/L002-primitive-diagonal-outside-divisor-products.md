# L002 — A primitive algebraic class outside divisor products

## Hypotheses

Let S be a smooth quartic surface in complex projective three-space. Such surfaces exist: the Fermat equation x_0^4 + x_1^4 + x_2^4 + x_3^4 = 0 is smooth because its four partial derivatives have no common projective zero. Put X = S x S and let pi_1, pi_2 be the projections. Let h be the hyperplane class of S, h_j = pi_j^*h, H = h_1 + h_2, and Delta_S the diagonal. The class H is ample, from the Segre embedding of the product.

Let D^2(X) be the rational span of all products of two divisor classes on X, including divisors other than the two hyperplane pullbacks. A class in H^4(X,Q) is called H-primitive if its cup product with H is zero.

## Conclusion

The class

\[
\beta=[\Delta_S]-\tfrac12 h_1h_2
\]

is a nonzero H-primitive rational (2,2)-class represented by a rational algebraic cycle, and beta is not in D^2(X). In particular,

\[
D^2(X)\cap P_H^4(X,\mathbb Q)
\subsetneq
\operatorname{Hdg}^2(X)\cap P_H^4(X,\mathbb Q).
\]

This refutes universal generation of primitive Hodge classes by divisor products. It is not a counterexample to the rational Hodge conjecture.

## Proof

The standard geometric inputs and their citations are recorded in [foundations/02-standard-inputs.md](../foundations/02-standard-inputs.md).

**Cohomology of S.** Weak Lefschetz gives H^1(S,Q) = 0 and connectedness, and Poincare duality gives H^3(S,Q) = 0. Adjunction gives K_S = O_S, so choose a nonzero omega in H^(2,0)(S). If e in H^4(S,Q) is the class of a point, then integral_S e = 1 and h^2 = 4e, since S has degree four.

**Primitivity, including the coefficient.** For the diagonal inclusion i: S -> X, the Kunneth decomposition is

\[
H^6(X,\mathbb Q)=
\bigl(H^2(S,\mathbb Q)\otimes H^4(S,\mathbb Q)\bigr)
\oplus
\bigl(H^4(S,\mathbb Q)\otimes H^2(S,\mathbb Q)\bigr).
\]

Here and below a tensor means the cup product of the corresponding pullbacks. We claim

\[
i_*h=h\otimes e+e\otimes h.
\]

To verify the claim, pair both sides with pi_1^*u for any u in H^2(S,Q). The left side pairs to integral_S h u by the projection formula, and the right side has the same value because integral_S e = 1; the term e cup u vanishes by degree. Pairing with pi_2^*u gives the same check for the other summand. These classes exhaust H^2(X,Q) by Kunneth and H^1(S,Q) = 0. Poincare duality between H^6(X,Q) and H^2(X,Q) proves the claim.

Since i^*H = 2h, the projection formula now gives

\[
H[\Delta_S]=i_*(2h)=2(h\otimes e+e\otimes h).
\]

On the other hand,

\[
Hh_1h_2=h_1^2h_2+h_1h_2^2=4(e\otimes h+h\otimes e).
\]

Subtracting one half of the second identity from the first gives H beta = 0.

**Divisor products annihilate the holomorphic two-form.** Kunneth gives

\[
H^2(X,\mathbb Q)=\pi_1^*H^2(S,\mathbb Q)\oplus\pi_2^*H^2(S,\mathbb Q).
\]

This is a decomposition of Hodge structures. Thus the class of any divisor on X is pi_1^*a + pi_2^*b for rational (1,1)-classes a,b on S. For this conclusion it suffices that divisor classes have type (1,1); no claim about line bundles themselves splitting is required. Products of two such classes are linear combinations of classes of the forms

\[
c\otimes1,\quad a\otimes b,\quad1\otimes c,
\qquad c\in H^4(S,\mathbb Q),\quad a,b\in\operatorname{Hdg}^1(S).
\]

For z in H^4(X,Q), define its correspondence action on v in H^2(S,C) by

\[
T_z(v)=(\pi_2)_*(\pi_1^*v\smile z)\in H^2(S,\mathbb C).
\]

For z = c tensor 1, T_z(omega) = 0 because omega cup c has degree six on a surface. For z = 1 tensor c, it is zero because integration on the first surface vanishes on degree two. For z = a tensor b,

\[
T_z(\omega)=\left(\int_S\omega\smile a\right)b=0,
\]

since omega cup a has Hodge type (3,1), which is zero on a complex surface. Linearity proves T_z(omega) = 0 for every z in D^2(X).

**The diagonal is detected.** The projection formula and pi_1 i = pi_2 i = id_S give \(T_{[\Delta_S]}(v)=v\) for every v in H^2(S,C). The correction h_1h_2 is a divisor product, so

\[
T_\beta(\omega)=\omega\ne0.
\]

Hence beta is nonzero and cannot lie in D^2(X). Finally, if C is a hyperplane section of S, then beta is the class of the rational algebraic cycle Delta_S - (1/2)(C x C). It is therefore rational and of type (2,2). Together with the primitivity computation, this proves every assertion.

The use of the complex vector omega only separates rational cohomology classes: equality over Q would persist after extension to C and would imply equality of their actions on omega. No rationality of omega, Picard-rank assumption, or description of all Hodge classes on X is needed.

## Mathlib

Coverage of the full statement: **not checked**. Supporting mathematics is Kunneth, Poincare duality, the projection formula, Weak Lefschetz, and adjunction, with sources in foundations/02-standard-inputs.md. No theorem matching this full statement in Mathlib, and no absence from Mathlib, is asserted.
