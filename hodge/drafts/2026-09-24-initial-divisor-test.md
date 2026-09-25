# Initial source audit and divisor-product test

Date: 2026-09-24. This file saves the reasoning for one bounded step; the current checkpoint belongs only in PROGRESS.md.

## Gap and relevance

The exact gap is surjectivity of rational cycle classes for arbitrary smooth projective varieties. The first dimension/codimension not covered by the elementary Lefschetz results is n = 4, p = 2. Hard Lefschetz and the (1,1) theorem reduce that case to primitive rational (2,2)-classes. This is a restricted target, with higher dimensions still unresolved.

The proposed intermediate target is that these primitive classes lie in the rational span of products of divisors. If true, the (1,1) theorem and algebraic intersections would supply their cycles. The discriminating test is the diagonal of a smooth quartic surface S in S x S, corrected to be primitive for h_1 + h_2. Continue the divisor-only mechanism only if it passes this test; abandon universal divisor generation if a primitive Hodge class lies outside its image.

## Redundancy and alternatives

The initial notebook has no lemmas, attempts, or historical failures, and its local git diff is empty. The source audit is a baseline, not a new theorem about the conjecture. Three mechanisms considered are products of divisors, algebraic correspondences between surfaces, and variation of Hodge classes in families. Divisor products have the quickest exact test. Correspondences can act on the holomorphic two-form and are a plausible next mechanism if that test fails; the family mechanism has no concrete cycle construction in this step.

## Saved calculation before full write-up

For a smooth quartic S, let h be the hyperplane class, e the class of a point, and omega a nonzero holomorphic two-form. Then h^2 = 4e, H^1(S,Q) = H^3(S,Q) = 0, and for the diagonal inclusion i,

\[
i_*h=h\otimes e+e\otimes h,
\qquad
(h_1+h_2)[\Delta_S]=2(h\otimes e+e\otimes h).
\]

Consequently beta = [Delta_S] - (1/2) h_1 h_2 should be primitive. Every product of divisor classes acts as zero on omega by the correspondence action, while the diagonal acts as the identity. The full write-up must check divisor splitting by Kunneth, the coefficient 1/2, and the projection-formula conventions. This is an algebraic class and therefore cannot disprove the Hodge conjecture.

## Required threshold

The target needs all primitive rational (2,2)-classes on every smooth projective fourfold to be algebraic even at this first boundary. Producing this one algebraic primitive class supplies no such surjectivity. A negative test would establish only that any proposed universal construction must go beyond divisor products.

## Completed assessment

The saved calculation was confirmed in full in [L002](../lemmas/L002-primitive-diagonal-outside-divisor-products.md): the coefficient is exactly 1/2, divisor classes split in rational degree-two cohomology, and the diagonal action is the identity under the stated projection convention. The proposed universal divisor-generation assertion fails. The negative result changes the research decision toward correspondences; it does not disprove any case of the Hodge conjecture. The exploration count ends at zero because the test supplied decisive evidence. This closes the initial assessment; no reasoning in the saved calculation remains pending.
