# 2 November 2026 — approximate values for a dense narrow cloud

STEP_ID: 2026-11-02-approximate-cluster-values-research-01.
RESEARCH / ADVANCE / POTENTIALLY_NEW; actual task: proof_attempt.
Reused the unchanged ready joint-full-grid assessment and its inspected
sources. No new literature approval, source audit or novelty claim.

[L655](../lemmas/L655-approximate-cluster-value-joint-bound.md)
proves the required squared rate 1/16 with constant 1/4 for n>=8192
and all |a-x|<=1/16384, allowing the full original distinct-count and
mass range. Chosen-degree Taylor approximation pays relative value
error instead of matching every nearby pole exactly. The canonical
proof retains the full norm, correction and original squared residues;
its low-mass case uses L654. It remains separately unaudited.

All 14 scalar checks passed in
`scripts/one-sided-hankel/approximate-cluster-constants.json`; the full
checks array was inspected. These arithmetic witnesses do not replace
the analytic proof or establish the unrestricted target. Preliminary
reasoning is preserved in
`drafts/2026-11-02-approximate-cluster-values-working.md`.

DAG inputs L650, L651 and L654 respectively supply the complete
response, Gram/correction/anchor bounds, and small-mass case. The
standard Fourier coefficient extraction is specialized with its
convergence hypotheses in L655. No unproved positivity is an input.

Continue the unchanged ready target on spatially spread families using
one polynomial with controlled cross-cloud errors and full norm, and
confluent handling as centers merge. Preserve the grouping, recovery,
pointwise remainder and prefix stops. Do not extrapolate the narrow
interval to arbitrary support. Xi realization and signs remain open;
there is no RH candidate. No mathematical EXPLORATION budget was used
this turn and no supervisor state was edited.
