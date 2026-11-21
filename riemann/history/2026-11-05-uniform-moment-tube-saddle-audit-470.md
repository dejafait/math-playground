# 2026-11-05 — step470: tube and full-saddle audit

RESEARCH / REPRODUCTION, conceptual proof audit on the unchanged prior
SPECIALIZE gate. The local advance is the full proof in
[L789](../lemmas/L789-uniform-kernel-tube-and-saddle-audit.md): the required
small-strip tubes, real initialization, complete-disk derivative bound,
both Rouché comparisons and holomorphic full-saddle continuation close
for k>=10^9. This verifies restricted source claims, not new mathematics
beyond the inspected source or an actual minor sign.

L788's tube premise now explicitly states the small-strip restriction
used by its proof. It remains a conditional implication, with no input
from L789 inside that proof. L789 restates and verifies its formulas
without any local lemma premise; the new DAG row is empty. PROOF records
the newly verified inputs while leaving saddle action/Taylor control,
other wedge gates and the central gap open.

The exact scalar certificate is
`scripts/complex-moment-audit/tube-saddle-470.json`. The initial run used
11/10^13 instead of L788's 11/10^12 larger-tube threshold; its failed
certificate is retained in `tube-saddle-470-initial-threshold-error.json`
in the same directory. Correcting that transcription, without changing
any source requirement, gives passing comparisons. The canonical proof
contains the domain and analytic reasoning; no ancillary code was used.

The [next assessment](../drafts/literature/2026-11-05-uniform-moment-taylor-coefficient-audit.md)
is REVIEW_REQUIRED for the genuinely changed Proposition3.7 scope.
One separate source-comparison turn is needed before that audit. No
coefficient derivation or approval was made here. Step465's missing
central signed mechanism still blocks justified creative routing;
the source audit does not reopen the L765/L774 stops. One mathematical
audit, zero EXPLORATION calculations; no scheduler or quota edits.

Overview compaction preserves these displaced status details: L776–777
remain conditional; L778–780/L783 remain stops; L766/L774–775/C785a
remain unaudited. L786's higher-order gap is unchanged. No result is
promoted by the shorter PROOF paragraph. The first documentation check
reported 8408 bytes in PROOF; this compaction repairs that size failure
without changing any canonical mathematical statement.
