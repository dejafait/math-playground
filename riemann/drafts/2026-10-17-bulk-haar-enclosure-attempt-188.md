# Bounded exact-integral enclosure attempt — step 188

Initial plan saved before implementation. The gate is the unchanged
SPECIALIZE assessment `drafts/literature/2026-10-17-bulk-haar-integral-enclosure.md`.
The exact target is to determine whether L426's I is nonzero. This is a
calculation / REPRODUCTION using known interval inclusion, not a new
integration theorem. The main gap remains global mixed positivity.

Inputs are audited L426 (exact integral/product law), L423 (fixed mixture),
L422 (certified coefficient endpoints), L419 (lexicographic strict pairs,
ordered complements and both equality rules), L425 (selector geometry),
and L424 (prospective trajectory test). L368/L369/L390 enter only through
the audited reduction; no additional actual-phase assumption is made.
The step-175 sampling stop remains in force. No duplicate certified I
evaluation was found in these inputs.

Declared cap: 32,768 product cells, three prime coordinates (2,3,5),
and 512 full-circle selector intervals. Each prime modulus coordinate
has four intervals on [0,pi], using the exact cosine reflection symmetry.
The whole remaining Euler logarithm is bounded uniformly. Exact inherited
coefficient intervals are used without fitting. Arithmetic uses integer
fixed-point outward intervals, rational Taylor bounds and integer square
roots. Unresolved selector cells include all equality cases via a global
state bound. There will be no unvalidated sampling.

Continue this implementation only if the completed enclosure usefully
narrows the range and its remaining budgets suggest a concrete attainable
zero-excluding bound. If the full response tail, selector dependency or
coarse product cells defeat that test, preserve the evidence and stop
this capped implementation. Neither an interval containing zero nor
sampling is a proof of vanishing. A nonzero I would separate this law
from the necessary trajectory test, but would not resolve clipping,
actual realization in general, L413's regulator margin or RH.

## Completed result

Outcome: NEGATIVE for the uniform capped-mesh implementation, not a
negative value of I. The exact integral is enclosed in [-0.301,0.207],
which contains zero. Full mathematical justification and arithmetic
qualifications are canonical in L426's step-188 enclosure section.
The executable is `scripts/discriminant/enclose_bulk_haar_integral.py`;
the full cell certificate is
`scripts/discriminant/bulk-haar-integral-enclosure-188.json`.

An initial evaluation of the same cell mesh recomputed the complementary
trace from dependent intervals, producing unresolved angle mass 7/16
and range approximately [-0.461977,0.406109]. Reusing L425's exact
complementary gaps (-D_k,D_k) repairs that avoidable overestimation.
The final unresolved mass is 3/64; its joint contribution is about
+/-0.030124. The strict-cell contribution still has width about
0.446799. This arithmetic refinement did not change the integral,
the prescribed basis, the prime coordinates, cell cap or source scope.

All 32768 distinct product records were scanned for full coverage and
exact aggregation; the load-bearing aggregate, parameter intervals,
tail and branch budgets were inspected. Every validity check passes;
the explicit failure is that zero is not excluded. The result is a
local implementation feasibility finding using known methods; it is
not a discovery of I's sign or a result beyond the sources checked.

Stop the uniform mesh. One further bounded attempt on the same ready
target can replace uniform product cells by adaptive cells driven by
certified observable widths, while retaining the exact trace-gap
identity. This is within the existing assessment's finite-cell scope;
no new next assessment or literature approval is claimed. It must
declare a new work cap and compare strict-cell, full-tail and residual
branch widths with zero exclusion. If it fails to narrow the total
budget materially, reassess this range-integration mechanism after its
second attempt. The compact continuation remains in PROGRESS.md.
