# Step276 — joint endpoint polynomial conditioning

10 November2026. STEP_ID:
2026-11-10-joint-endpoint-polynomial-conditioning-276.
RESEARCH / REPRODUCTION / proof_attempt under the pre-existing
SPECIALIZE review275. ADVANCE is local quantitative specialization,
not a claim of novelty beyond the inspected sources or an RH result.

[L993](../lemmas/L993-joint-endpoint-polynomial-conditioning.md)
proves sigma_min(J_n)>=C/n for every sufficiently large integer,
retaining the exact constants and both possible row orientations.
The new bound follows from quantitative robustness of the recurrence
and integer obstruction; no numerical horizon or new source is used.
Full proof and limitations are canonical there. The saved reasoning is
in `drafts/2026-11-10-joint-endpoint-conditioning-working-276.md`.

The argument now contains joint conditioning, so PROOF.md's gap
paragraph and the single DAG row were updated. To keep the overview
compact, its displaced earlier notes are retained here: L988's O(n^4)
bound was audited; L982 averages, L989 O(n^3), and L991's unbounded
pivot-ratio result remain unaudited. Their proofs are unchanged.
The scalar stops270/272/274 and unfinished working271 are preserved.

A separate conceptual audit of the new all-index proof is nominated
in review276 with REVIEW_REQUIRED, without approving it this turn.
An essential audit takes priority over choosing a fresh creative
mechanism; independent signed arithmetic control remains the missing
input to any central use of the matrix bound. All three outputs and
the other RH transfer obligations remain unpaid. No mathematical
exploration budget or scheduler state was reset; no delegation,
external API, mathematical script or cross-notebook input was used.
