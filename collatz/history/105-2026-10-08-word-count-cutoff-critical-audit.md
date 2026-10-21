# 105 — 2026-10-08: fixed word-count cutoff critical audit

STEP_ID: collatz-2026-10-08-105-word-count-cutoff-critical-audit

The separate audit in [L043](../lemmas/L043-postspell-word-count-cutoff.md)
found no defect in the exclusion through twelve and the precisely qualified
scalar feasibility at thirteen. The independent
[exact verifier](../scripts/postspell-word-count/audit_cutoff.py) passed
62/62 checks; its [full certificate](../scripts/postspell-word-count/audit-certificate.json)
records actual and required bounds. The source applicability, all-real
monotonicity and series remainder were also checked. The original
certificate and unfinished notebook work are preserved.

EXPLORATION, RESEARCH/REPRODUCTION, actual task proof_audit, under the
unchanged pre-invocation [SPECIALIZE assessment](../drafts/literature/2026-10-08-word-count-cutoff-audit.md).
This audit gives no stronger exclusion, repair or new theorem beyond the
checked sources. Full reasoning is canonical; the
[working record](../drafts/2026-10-08-word-count-cutoff-audit.md) preserves
the checkpoint. No mathematical assembly or dependency changed, so PROOF.md
and DAG.md remain untouched; the canonical audit supersedes pending wording.

The specified scalar comparison is exhausted at thirteen, without producing
a cycle. The [pending changed-target assessment](../drafts/literature/2026-10-08-unrelaxed-thirteen-word-estimates.md)
requires separate review of L041's omitted unrelaxed per-word estimates.
It contains no derived or approved improved bound. This differs from merely
rerunning the exhausted scalar test; rejecting one tuple would not suffice.
Attempt 019 and history 069 remain intact. Source computations, original
Rhin/Crandall proofs, external Lean and Mathlib matching remain unchecked;
entry, unrestricted counts, arbitrary cycles, divergence and universal
eventual descent remain open. One bounded mathematical EXPLORATION audit
was used; prior recorded usage is retained and no supervisor state is edited.
