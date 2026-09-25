# Attempt 006 — Adding the diagonal to the cubic support

Date: 2026-09-25. Outcome: stopped in the transverse NS-fixed RM direction.

The proposed representative was the reduced union C union Delta_S. Its action U+id would recover the missing cubic RM action after subtracting the diagonal. Unlike C alone, it has two elliptic double curves with genuine local node-smoothing parameters. The full first-order test is [L009](../lemmas/L009-diagonal-union-retains-cubic-obstruction.md).

**WHY IT FAILS.** In a global lift, the diagonal branch defines a vector field on S with possible simple poles along the two elliptic fibres. Its base component is a section of O(4) vanishing at all 21 nodal values, so it is zero. The pole calculation then makes the whole vector field regular, hence zero on the K3, forcing the actual relative diagonal to persist. The residual lift of C is flat along the double curves and extends across the three isolated points using the already computed normal sheaf's Hartogs property. L008's transverse obstruction therefore survives. The union's kernel has dimension three, whereas vanishing in every RM direction requires four. This stops this added component, not every changed representative or the rational Hodge class. A product of elliptic fibres has zero transcendental action but lacks the dominant identity component used in this obstruction argument.
