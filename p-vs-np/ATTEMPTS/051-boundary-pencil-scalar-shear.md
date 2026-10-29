# Attempt 051 — scalar shears with identity stabilization cannot exchange the factors

Step 533, 2026-10-27. The tested stable-equivalence contract, complete
wrapped graphs, both boundary vectors, every closed transition row and
the universal-r power mismatch are canonical in
[L117](../lemmas/L117-boundary-pencil-scalar-shear-obstruction.md).

**WHY IT FAILS.** Scalar invertible two-sided pencil changes induce
similarity after right closure, and adjoining an identity pencil adds
only zero transition states. The four-state operand in L117 computes 1
and has every vertex on a structural accepting path, yet prefixing and
suffixing F_r give nilpotency indices r+2 and r+1. Thus the transition
condition fails for every stabilization size and every scalar shear
support, before any universal resource bound can be tested. This stops
only the scalar-shear/identity-stabilization conversion. Polynomial
multipliers, nontrivial auxiliary graphs and singular rectangular scalar
maps remain outside the obstruction. L115 and Attempts 047–050 are
unchanged. A directly constructed common quotient is a different test
already within the earlier ready unary-product assessment; no quotient
or sparse projection is claimed to exist here.
