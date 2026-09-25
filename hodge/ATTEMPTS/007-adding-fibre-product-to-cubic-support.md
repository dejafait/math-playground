# Attempt 007 — Adding a smooth fibre product to the cubic support

Date: 2026-09-25. Outcome: stopped in the transverse NS-fixed RM direction.

The tested representative was the reduced union C union (F_+ x F_+). Its added component has a divisor-product class and zero action on T(S). Unlike the diagonal, it does not project dominantly to S, so the preceding identity-branch obstruction did not settle this test. Its intersection with C is a diagonal elliptic curve with a local node-smoothing parameter. The full calculation is [L010](../lemmas/L010-fibre-product-union-retains-cubic-obstruction.md).

**WHY IT FAILS.** Relative to an explicitly lifted fibre product, any lifted component defines a normal section with at most a simple pole along its diagonal. The normal bundle is trivial, and genus-one Riemann–Roch forces every such section to be regular. A product of moving fibres therefore persists in the union. The colon by that component gives a flat lift of C, including its points at infinity because the added component avoids them. L008's obstruction then leaves a three-dimensional kernel, against four RM tangent dimensions required. This rejects the specified reduced addition, not every changed representative; a length-two nonreduced component has no reduced branch to which this pole argument directly applies.
