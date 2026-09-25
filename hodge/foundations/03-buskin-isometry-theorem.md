# Algebraicity of rational K3 Hodge isometries

Sources checked on 2026-09-25. Cohomology and cycle coefficients below are rational.

## Hypotheses

Let S_1 and S_2 be smooth projective complex K3 surfaces. Let psi: H^2(S_1,Q) -> H^2(S_2,Q) be an isomorphism preserving Hodge types and the cup-product pairings. Under Poincare duality and Kunneth, let Z_psi in H^2(S_1,Q) tensor H^2(S_2,Q) be the unique tensor whose correspondence action is psi.

## Conclusion

The codimension-two Hodge class Z_psi on S_1 x S_2 is algebraic.

## Proof

This is Nikolay Buskin, *Every rational Hodge isometry between two K3 surfaces is algebraic*, [Theorem 1.1, arXiv:1510.02852v3, p. 2](https://arxiv.org/pdf/1510.02852v3#page=2). It is a match for the stated algebraicity theorem. Its hypothesis is an isometry, not an arbitrary isomorphism of rational Hodge structures. It does not assert algebraicity of every endomorphism of transcendental cohomology.

The [unnumbered corollary, p. 3](https://arxiv.org/pdf/1510.02852v3#page=3), covers S x S when the full transcendental endomorphism field is CM. Its proof uses spanning by rational Hodge isometries in that case. No such spanning assertion for totally real endomorphism fields is part of the theorem.

For comparison, Daniel Huybrechts, *Lectures on K3 Surfaces*, [Chapter 3, section 3.5, the paragraph following Remark 3.14, printed p. 59 in the author's draft](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=59), explicitly gives only +id and -id as rational Hodge isometries when the full endomorphism field is totally real. That is a match for the isometry-group calculation, not for the correspondence-span conclusion assembled here. The local proof uses the action on the holomorphic two-form and does not need the classification of endomorphism fields. In particular, the integral-lattice isometry statements earlier in the chapter are not being substituted for rational ones.

## Mathlib

Coverage: **not checked** for the full Buskin theorem, the endomorphism-field results, or their geometric hypotheses. No full or supporting Mathlib theorem name has been verified. The direct sources above are mathematical references, not evidence of Mathlib coverage or absence.
