# Shared bank: paired interval-endpoint implementation stop696

Canonical formulas, qualifications and proof:
[C998p](../lemmas/C998p-shared-taylor-bank-and-interval-work-stop.md).
Finite evidence: `scripts/separation-seven/shared-taylor-bank-696.json`.

WHY IT FAILS: The fixed implementation accumulates two interval endpoints
for every interior and endpoint moment and evaluates separate paired
Horner polynomials for three D calls and three elementary logs per node.
Together with audited C998o setup, a mandatory prefix costs22199915,
exceeding20000000 by2199915, even with three midpoint nodes and all bank
generation, remaining constants, coefficient/entry assembly and final
contraction free. The finite bank formula and ideal-interior error bound
do not pay finite primitive, density, node-propagation or exact-Z error.
No full batch ran. This stops that explicit implementation; it is not a
lower bound for consolidated primitives, aggregated error radii or other
shared-moment realizations. The new bank remains unaudited, and earlier
C998j/k/l/m and C998n/audit693 stops are preserved with their original
scopes. No signed comparison or RH counterexample follows.
