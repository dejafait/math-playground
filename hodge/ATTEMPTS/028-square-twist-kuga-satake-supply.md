# Square-twist Kuga--Satake cycle supply

Tested on 2026-10-03 under the saved SPECIALIZE assessment.
The specified form twist is a square and the known abelian
comparison applies. See the full scoped result in
[L037](../lemmas/L037-square-twist-kuga-satake-comparison.md).

WHY IT FAILS: The functorial comparison transports the modified
embedding to kappa b, with b=U^2+U-id, whereas transport of the
ordinary algebraic embedding alone gives kappa_a b^{-1} and
returns only id. Using the actual geometric transpose and an
invertible algebraic normalization, L037 proves that, assuming
ordinary kappa algebraic, the required modified cycle is
algebraic exactly when U is. Encoding the modified tensor with
q_a instead returns b^{-1} and retains the same missing action.
The isogeny supplies neither surface cycle. This stops automatic
cycle supply by this comparison, not independent constructions
of the modified cycle, other input forms, or the Hodge conjecture.
