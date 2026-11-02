# 2026-10-31: three-wave stationary bulk threshold test

STEP_ID: 2026-10-31-three-wave-bulk-calculation-01

Completed one mathematical calculation under the prior EXPLORE assessment
`drafts/literature/2026-10-31-three-wave-stationary-bulk-review.md`.
[L577](../lemmas/L577-three-wave-stationary-bulk-clipped-upper-bound.md)
checks the whole K, stationary derivatives and bounded paired support,
but gives a computer-assisted upper bound <13/4000<1/288 on clipped
mass. The complete exact certificate is
`scripts/three-wave/certificate.json`; the mathematical error analysis
and reproduction command are canonical in L577. This is a relevant
NEGATIVE result for this bulk, not a new arithmetic theorem or RH result.
The initial sample was exploratory only and is not used in the proof.

The numerical part enumerates all 543338496 nodes with rational trig
enclosures and exact integer arithmetic. Final actual upper is
0.0031367172376983833; required threshold is 1/288. Complete selected
certificate fields, including all trig enclosures, finite slices, exact
bounds and overflow inequalities, were inspected. The rational phase
error uses the verified pi<22/7; no floating trigonometry enters the sum.

The [attempt stop](../ATTEMPTS/2026-10-31-three-wave-stationary-bulk-stop.md)
preserves this specific failure separately from L576's two-wave identity.
L577 uses L473's matrix; L576/L471 are contrasts/motivation only.
PROOF now records the added obstruction and DAG has the single direct
input edge. Unrelated unfinished changes were preserved.

Nominate an independent certificate audit with source coverage reused
from the original target, pending separate approval of
`drafts/literature/2026-10-31-l577-independent-certificate-audit.md`.
No justified new creative central-gap mechanism is prepared: actual
nonlinear Hardy law/tail transfer and full stationary fourth realization
remain missing. The next ordinary audit is not labeled creative.

Scoped documentation validation passed: 605 nodes, 1499 edges, acyclic
and complete local coverage. The new direct input is L473 only; source
scope and exact certificate replay remain subject to the nominated audit.
Notebook-scoped whitespace validation also passed. The overview was
shortened to its byte budget without moving proof details out of L577.
