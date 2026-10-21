# 2026-10-10 — Parameterized dual-kernel audit and failure-report repair

RESEARCH / proof_audit / REPRODUCTION, ADVANCE in local validation of a
known-algorithm input. The approved finite audit is complete. The
[canonical L030 audit](../lemmas/L030-conductor-389-full-relative-integration-line.md)
records the complete source-to-code argument and evidence. All seven original
hashes matched and their bytes are preserved. The byte-identical rebuilt
certificate passes full conductor-389 replay, rank 64 at d=65, nullity one
and exact determinant -58000; all generator/relation checks, 22 rejections
and four core-only diagnostics pass.

A real subordinate-report defect was reproduced: a path assertion rejected
a malformed Gamma0 witness but left a stale success report. The adapter now
persists an input-bound failure before rethrowing; the same corruption rejects
in both reports. Original and repaired evidence is retained under
`scripts/dual-kernel/critical-audit/`, whose manifest has 11/11 passing audit
checks and no unexpected failures. No false line acceptance was demonstrated.
See the [working record](../drafts/2026-10-10-parameterized-dual-kernel-critical-audit.md).

No new mathematical lemma, DAG input or argument change; PROOF/DAG stay
untouched. Generic arithmetic remains conditional and the general adapter
still lacks a new elliptic-instance run. The next distinct bounded target
is a proposed conductor-11 general-adapter replay, beginning with separate
[REVIEW_REQUIRED coverage](../drafts/literature/2026-10-10-conductor-eleven-general-adapter-replay.md).
No new arithmetic for that model was derived here. Existing production stops
and source blockers persist. Mathematical exploration stays 0 of 3;
STATUS remains IN_PROGRESS, without a BSD candidate or beyond-source claim.
