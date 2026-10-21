# BSD-190 — 2026-10-13

Constructed the actual fixed coupled table and independently replayed
all 476280 terms, 1316 signed occurrences and 72 integer isolations.
All widths <=2^-60<2^-38; all 144 source relations, 59 saturated columns
and quotient reconstructions pass, including 16 zero values. The common
reduced denominator is 12. Canonical proof, complete citations and
qualifications are [L056](../lemmas/L056-conductor36-coupled-normalized-generator-table.md);
full finite report is `scripts/conductor36-table/table_verification.json`.
Two bounded malformed/missing-data cases are rejected with preservation
hashes. This is an ADVANCE in local known-method reproduction, not a
result beyond the checked sources or a BSD candidate. Historical stops
and all existing work are preserved.

The fixed normalization benchmark is complete at production-replay level;
a separate critical audit remains pending. Propose that exact audit with
REVIEW_REQUIRED coverage for the next approval turn. CM prevents L027's
application; arbitrary-curve rank equality and the rational/Sha/complex
comparison gaps remain. No scheduler/shared state was edited.
