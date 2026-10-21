# L067 critical audit — completed record

STEP_ID: 2026-10-11-mca-154-antipodal-critical-audit

Approved scope: exactly the TARGET in
`literature/2026-10-11-antipodal-triangle-bound-audit.md` (prior EXPLORE).
Main gap: arbitrary triangle counting and extraction, independently of the
challenge-definition gap. Intermediate target: validate L067's antipodal
isolated maximum three and conditional twelve bound for later classification.
Continue only if every normalization, support row, scalar union, original
moment witness and L066 inclusion checks; otherwise repair or restrict the
claim. L057/L066 are audited inputs; L067 is the object of this audit.
L060–L064, arbitrary-pair bounds, extraction and ABF26 identification are
not assumed. ATTEMPTS/025's stopped sampling route remains preserved.

Saved before full replay: read L067, L066 and its prior audit, L057's full
recovery statement and original-chart derivation, and the entire C++ producer,
replay and Python summary/witness checker. Equations (1)–(3) have the correct
signs after substitution in L057; scaling Q by s^7 and lambda by s^-7
preserves actual errors and multiplies moment j by s^j. All ordered roles
are retained. C++ initialization, masks, modular arithmetic, Gauss elimination
and tuple encoding have been inspected; full replay and an independent
packed-row scalar aggregation are still to run. No completed audit is yet
claimed. The continuation must retain lower-weight rows and both-zero lifts.

## Completed result

The full audit is canonical in
[L067](../lemmas/L067-antipodal-triangle-isolated-anchor-bound.md), including
the evaluation signs, scaling action, shared C++ utilities, every row and
assignment, original-chart witness and audited L066 assembly. No defect or
argument change was found. The complete fresh equation replay agrees with
the previous replay; a separate tuple/set aggregation reads all 21,621,600
rows and reproduces every assignment maximum and histogram. Maximum three
remains below four required anchors, with all zero-weight rows retained.
The three witness errors satisfy all eight original-pencil moments.

Evidence: `scripts/triangle-recovery/antipodal-anchor-audit-replay.json`
and `scripts/triangle-recovery/antipodal-anchor-critical-audit.json`.
The latter's checker is `scripts/triangle-recovery/audit_antipodal_certificate.py`.
This is ADVANCE / RESEARCH / REPRODUCTION: validation of the existing
restricted input, not a new bound or certified novelty. PROOF.md and DAG.md
are unchanged because the argument and dependencies are unchanged; the
current audit status is recorded in L067 and PROGRESS.md.

Next proposed target allows an arbitrary third singleton pair while keeping
the first two antipodal. Its exact isolated-count claim needs a separate
coverage review, recorded REVIEW_REQUIRED; it is not approved or attempted
here. The original finite gates, relaxed zero weights, L066 full-anchor
condition, arbitrary-pair gap and challenge-definition gap remain explicit.
