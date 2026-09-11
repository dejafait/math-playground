# Quadratic penalization does not supply a uniform local bound

Date: 2026-09-11.

The attempted shortcut was to deduce small upward interaction directly from maximality of Im ρ−ε(Re ρ)² and reciprocal-square summability. [Lemma 71](../lemmas/L071-quadratically-penalized-height-maxima.md) proves attainment, convergence of the selected heights, and an explicit finite-interior/tail bound, but supplies a finite-product obstruction to a uniform local estimate.

WHY IT FAILS: maximality bounds a positive height difference by ε times a difference of squared horizontal coordinates. Dividing by the squared distance leaves an inverse horizontal gap, which can be arbitrarily large. The lemma's symmetric polynomial examples have uniformly bounded strip height and reciprocal-square mass yet arbitrarily large upward interaction at a penalized maximizer for fixed ε. This refutes a bound uniform over this class, not a fixed-product limiting theorem. Favorable-sequence existence remains unproved; one must control local spacing more carefully or use an additional selection argument.

## Fixed-product strengthening — 2026-09-11

[Lemma 72](../lemmas/L072-fixed-product-obstruction-to-penalized-upward-vanishing.md) now supplies one infinite product and a penalty sequence for which every maximizer has upward contribution greater than 1.

WHY IT FAILS: fixed-product reciprocal-square summability still permits increasingly close horizontal neighbors at increasingly distant clusters. Their height gains can lie below the quadratic score cost while their positive interaction remains bounded away from zero. Thus passing from a uniform-in-product estimate to a full limit for each fixed product does not repair the shortcut. Favorable-sequence existence and the signed interaction remain separate questions.
