# BSD-170 — fixed reduced-phase critical audit

Initial reasoning saved before full replay. The unchanged SPECIALIZE
assessment is `drafts/literature/2026-10-11-nonunitary-reduced-phase-critical-audit.md`.
The main gap is rank equality for arbitrary analytic order at least two.
This step audits only L051's fixed {1/6,infinity} enclosure on y^2=x^3+1,
using audited L049 and L050's fixed arithmetic and transport evidence.
A successful audit would validate a component of later normalization
production, without solving rational membership, Sha, uniform coefficient
nonvanishing or complex-order comparison.

Reviewed the full L050/L051 proofs, both v2 implementations and the v1
verifier, ATTEMPTS/025 and BSD-168 history. No duplicate separate critical
audit is recorded. Reuse source coverage; no new literature search or
cross-notebook input is needed. Preserve both certificates and reports.

The discriminating test is complete finite replay plus a distinct exact
rational endpoint Taylor calculation for selected cosine boundary/sign
cases and all damping heights, and rejection/persistence tests on altered
load-bearing evidence. Inspect all source applications, tails, signed
closing and minimal-target period. Continue only if inclusion and full
replay justify the actual strict width <2^-20; otherwise repair or record
a concrete failure. These audit tests do not establish generic software
correctness. Full findings will be canonical in L051.

## Completed result

ADVANCE; RESEARCH; REPRODUCTION; ACTUAL_TASK_TYPE proof_audit. The fixed
audit passes; this is local validation of known mathematics, not progress
beyond the sources checked. Full reasoning and citations are canonical in
[L051](../lemmas/L051-nonunitary-cusp-reduced-phase-enclosure.md).
The audit replay checks all 181410 finite terms and all inherited arithmetic.
Distinct exact rational Horner/Taylor/Lipschitz bounds fit inside all seven
selected cosine and all 19 damping enclosures. The independent closing
sum also fits. Six altered inputs are rejected with fresh persisted reports;
both schedules and original reports retain identical hashes. Complete
evidence is `scripts/nonunitary-cusp/audit_full_replay.json` and
`scripts/nonunitary-cusp/audit_discriminating_checks.json`.

The actual width is 38839602421900655/19807040628566084398385987584,
strictly below 2^-38 and the required 2^-20. No fixed inclusion failure
was found; no exact symbol is inferred. The proposed next target is exact
rational recovery with an independently usable denominator bound. Its
essential small-denominator source comparison is not covered by this
audit and is recorded REVIEW_REQUIRED for a separate literature turn.
