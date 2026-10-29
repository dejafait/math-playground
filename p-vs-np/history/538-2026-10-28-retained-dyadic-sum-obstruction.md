# Step 538 — 2026-10-28 — retained dyadic sums do not give a linear chain

Completed one RESEARCH / NEGATIVE / REPRODUCTION step; actual task type
proof_attempt. Reused the unchanged ready
[batched-incidence assessment](../drafts/literature/2026-10-27-batched-incidence-zigzag.md).
The supplied startup overview and DAG preceded targeted proof reads.
Existing notebook changes and unfinished work were preserved; no source
refresh, cross-notebook input, supervisor edit or commit occurred.

[L121](../lemmas/L121-retained-dyadic-sum-incidence-obstruction.md)
specifies one binary-scale two-coordinate sum auxiliary, sharing unchanged
registers and avoiding the placement grid. It computes the right polynomial,
but the proposed first map fails an exact transition row while preserving
both boundaries. Independently, its compulsory changed-register values
force a logarithmic overhead even after all equal-value identifications.
This is new local route evidence from elementary specialization, not a
claimed new general theorem or an obstruction to arbitrary scalar sums.

[Attempt 055](../ATTEMPTS/055-retained-dyadic-sum-incidence.md) retains the
failure. Working notes are in
`drafts/2026-10-28-dyadic-scalar-incidence-work.md`; complete exact replay is
`scripts/batched-incidence/output-538/dyadic-sums.json`. The script checks
every coefficient, gate, count and equation coordinate at N=1,2,4,8,16,32,
retaining all expected failures. The symbolic proof supplies the unbounded
ratio. Selected complete JSON evidence, including the full smallest
counterexample, was inspected. There is no second map or complete chain.

The DAG adds only the used L110 closure/products input; L118 motivates
the candidate without being a proof premise. PROOF.md changes the existing
template-scope paragraph. L120's
cancellation projections were not rerun after this mandatory path failure;
no earlier result or stop was weakened. Mathematical EXPLORATION usage is
zero after this informative negative result.

Reassess the batching mechanism: keeping all partial transforms is itself
too expensive. The next candidate connects just the endpoint placements
using a shared letter-delay spine and scalar sums, with no retained register
per binary stage and no free polynomial multiplier. Its maps remain
unconstructed. The exact target/continuation and routing are solely in
PROGRESS.md, with the same prior ready assessment. No new target assessment
was written or approved in this turn.

Scoped documentation validation passes; the mathematical dependency review
removes the merely motivational L118 edge. Scoped whitespace checks pass.
