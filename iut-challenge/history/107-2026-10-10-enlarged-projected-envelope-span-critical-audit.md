# 2026-10-10 — Enlarged projected envelope span audit

The approved critical audit validates [L036](../lemmas/L036-enlarged-projected-envelope-orbit-span.md)
under its unchanged hypotheses. Independent full matrix checks and reverse
Smith replay pass all 2,952 operations and all relative/kernel identities;
the complete evidence is `scripts/cyclotomic-log/projected-envelope-independent-audit.json`.
The quotient orientation, actual residual action and bounded finite-sum
Nakayama obligations pass. This is new verification evidence for a local
known-method reproduction, not a new general theorem or IUT flaw.

The exact-span continuation test succeeds. Preserve ATTEMPTS/020,022–024
and all original applicability gaps. Queue one changed target: the sharp
scaled projected-container comparison, with its assessment REVIEW_REQUIRED
for separate approval. No container threshold or numerical consequence
was derived in this audit. PROOF.md and DAG.md remain unchanged because
the mathematical argument and direct inputs did not change.
