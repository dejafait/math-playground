# Standard geometric inputs

These are named standard theorems, not assumptions of the Hodge conjecture. The notation is fixed in [the target statement](01-target-and-scope.md).

## Hypotheses

Unless specified otherwise, X is a smooth projective complex variety of complex dimension n; h is the first Chern class of an ample line bundle; L is cup product with h. Cohomology has rational coefficients unless complex Hodge types are displayed.

## Conclusion

The following inputs are available in this notebook.

- **Lefschetz (1,1) theorem:** rational Hodge classes in H^2(X,Q) are rational divisor classes.
- **Hard Lefschetz:** L^(n-k): H^k(X,Q) -> H^(2n-k)(X,Q) is an isomorphism for 0 <= k <= n. It shifts Hodge type by (n-k,n-k).
- **Weak Lefschetz:** restriction to a smooth ample hypersurface Y in X is an isomorphism in degree j < dim(Y). In particular H^1(S,Q) = 0 for a smooth quartic surface S in P^3.
- **Kunneth, Poincare duality, and the projection formula:** rational cohomology of a product decomposes into tensor products; on smooth projective varieties the decomposition respects Hodge types. Integration and proper Gysin maps have their usual degree shifts and satisfy f_*(f^*a cup b) = a cup f_*b.
- **Adjunction:** a smooth degree-d surface S in P^3 has canonical bundle O_S(d-4). Thus a connected smooth quartic has H^(2,0)(S) = H^0(S,K_S) of dimension one.
- **Hodge index theorem:** on a smooth projective surface, the cup-product pairing on rational divisor classes has signature (1, rho-1), where rho is their dimension. In particular, this restriction is nondegenerate.
- **Cycle-class compatibility:** algebraic cycles have the corresponding (p,p) type; their intersection products, pullbacks in this setting, and proper pushforwards agree with the cohomological operations.

## Proof / precise citations

The Lefschetz (1,1) theorem is explained via the exponential sequence and GAGA in Deligne, [The Hodge Conjecture, section 2(iii)](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2). Clearing denominators gives the rational version.

For Hard and Weak Lefschetz use Mark Andrea de Cataldo, *The Hodge Theory of Projective Manifolds* (2007), [Theorem 7.3.4(a), printed p. 78](https://www.math.stonybrook.edu/~mde/papers/MyHodgeTheoryBook.pdf#page=89) and [Theorem 7.4.1, printed p. 80](https://www.math.stonybrook.edu/~mde/papers/MyHodgeTheoryBook.pdf#page=91). An ample bundle becomes very ample after a positive power, which only rescales the Lefschetz maps by nonzero rational numbers. A quartic is a hyperplane section after the degree-four Veronese embedding of P^3.

Kunneth, Poincare duality, the projection formula, the adjunction formula, and compatibility of the cycle-class map with intersections are used as named standard results. For the specific quartic facts, see Daniel Huybrechts, *Lectures on K3 Surfaces*, [Chapter 1, Example 1.3(i), printed p. 8 in the author's draft](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=8). That source gives adjunction and H^1(S,O_S) = 0; Hodge decomposition and conjugation also imply H^1(S,Q) = 0. Smooth quartics are connected, also by degree-zero Weak Lefschetz.

These references were checked on 2026-09-24. The Huybrechts link is explicitly a prepublication draft; the section locator refers to that draft. The references supply supporting standard facts, not a theorem asserting the full result of the divisor-product test.

For the Hodge index theorem in the projective K3 case, see Huybrechts, [Chapter 1, section 2.2](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11). The tensor/Hom convention for Hodge structures is explained in [Chapter 3, section 1.1(iv)](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=41). These are supporting inputs, not a citation for the full residual-quotient calculation.

## Mathlib

Coverage: **not checked** for any of these full geometric statements or for their combination. No Mathlib theorem names have been verified, and unknown coverage is not recorded as absence.
