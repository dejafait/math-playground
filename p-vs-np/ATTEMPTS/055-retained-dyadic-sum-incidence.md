# Attempt 055 — retained dyadic-sum incidence batching

Step 538, 2026-10-28. The literal graph, every named sum, both boundary
checks, all transition-row cases and full symbolic resource obstruction
are canonical in
[L121](../lemmas/L121-retained-dyadic-sum-incidence-obstruction.md).
The pre-invocation batched-incidence EXPLORE assessment was reused unchanged.

**WHY IT FAILS.** Sharing unchanged registers in a binary-scale sum network
does compute the path family's binomial-to-monomial conversion, without
the complete placement grid. But a constant-only sum state has zero
right-closed residual; raw suffix arithmetic alone is not a scalar arrow.
The probe first map preserves both boundaries and fails exactly N-1
transition rows, already at N=2. Independently, every one of the kN/2
changed dyadic values has a distinct nonzero full suffix, also distinct
from the N base suffixes. Retaining one vertex for each value therefore
costs at least N+kN/2 vertices even after equal-value sharing, against
S=16N+20. This rejects the retained template with any repaired maps, not
all scalar-sum circuits or chains. Temporary construction circuits,
nonfunctional recoding of named registers and endpoint-only auxiliaries
are outside the count. The path test suffices to stop before rerunning
the cancellation fixtures; L120's ordinary projections survive. No receiver,
cap, production format or historical recovery route changes.
