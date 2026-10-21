# Step 217 — Abstract rigidity counterexample

Date: 2026-10-14. STEP_ID: 2026-10-14-mca-217-cyclic-linear-nonrigidity.
Task: RESEARCH / POTENTIALLY_NEW / proof_attempt. Outcome: NEGATIVE.

Completed exactly the prior SPECIALIZE target in
[the assessment](../drafts/literature/2026-10-14-linear-sixteen-family-rigidity.md).
[L087](../lemmas/L087-cyclic-linear-family-nonrigidity.md) imports the
known cyclic ruler construction and verifies its incidence hypotheses.
Its complete noncollinearity graph has one component, versus four for
L072. Thus the approved uniqueness bridge to L079 fails. This is a local
comparison result, not a novel construction or verified originality.
The elementary proof is independent of the supplementary script, which
checks all blocks, degrees, 120 block pairs and 120 vertex pairs per
family with no failures; the full certificate is in
`scripts/triangle-incidence/cyclic-nonrigidity-certificate.json`.

The sole DAG input is L072's exact comparison family. Audited L086 is
motivation and L079 is downstream only. No marked triangle, moment
compatibility or RS realization is claimed. The interval 11/q–16/q,
uniform triangle twelve and challenge qualifications remain open.
Stop evidence is preserved in ATTEMPTS/031; no census or label sweep
was begun. Mathematical exploration usage is one focused comparison,
with an informative negative result, zero consecutive EXPLORATION.

The next action is a separate critical audit of L087, with new coverage
marked REVIEW_REQUIRED. Its source-scope approval must occur in a
separate literature turn; it does not invalidate this completed result.
