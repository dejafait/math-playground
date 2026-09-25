# Attempt 002 — Divisor products together with the diagonal

Date: 2026-09-24. Outcome: rejected as a universal spanning mechanism on quartic self-products.

The proposed enlarged span was D^2(S x S) + Q[Delta_S] for a smooth quartic S. Unlike Attempt 001, it permits the nonzero identity action on the transcendental cohomology. The exact residual space is computed in [L003](../lemmas/L003-diagonal-residual-hodge-endomorphisms.md), and an algebraic class outside this enlarged span is constructed in [C003a](../lemmas/C003a-fermat-graph-outside-diagonal-span.md).

**WHY IT FAILS.** Divisor products act by zero on T(S), and adjoining the diagonal adds only rational scalar identity maps. On the Fermat quartic, the inverse graph of a coordinate automorphism acts by i on the holomorphic two-form and so is not a rational scalar on T(S). Its residual class is nonzero, including after a divisor-product correction to a primitive class. The achieved span has dimension rho^2 + 3, while the required Hodge space has dimension rho^2 + 2 + dim_Q End_Hdg(T(S)); the example makes the latter at least one dimension larger. The witness is algebraic, so the obstruction concerns the proposed generators, not the Hodge conjecture or all correspondence constructions. The span does suffice when End_Hdg(T(S)) consists only of rational scalars.
