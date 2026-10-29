# Seminvariant-first bounded test — working record

2026-10-25. Approved input assessment:
`drafts/literature/2026-10-25-marked-elliptic-seminvariant-enumeration.md`.
Essential mathematical input is L128; L112 supplies only lower rank one
and L127 explains a possible downstream use. The main Beal gap and all
independent point/recovery obligations remain open. ATTEMPTS/050–053
were checked; no backend probe or raw coefficient-loop retry is intended.

Before calculation, fix the sieve as exact divisibility by 27 together
with square-image tests modulo 64, 5, 7, 11 and 13. For this invariant
pair, divisibility by 27 reduces to p=0 modulo 3. The mod-64 predicate
will be compressed to modulus 8 only after an exhaustive 64-residue
check. No further moduli or alternative sieve trials are allowed here.

Translate all signed source regions first. Count type-one a=1,2,...
using inner integer p-intervals, so any counted pair lies in the exact
region. CRT progressions are counted by an exact floor difference.
The ledger charges every square-table cell, p-residue predicate cell,
CRT pair trial, aggregate interval count and signed-region preparation.
An explicit (a,p) inspection or b-root trial, if reached, is also charged.
Caps remain 200000 work units and 2000000 expanded candidates.

Stop if a prefix already forces more than 200000 explicit pair
inspections, or counting work reaches its cap. Neither event certifies
the unvisited region or counts actual square syzygies. Enumeration is
allowed only after a complete feasibility count fits both caps.
The coverage proof must retain both r signs and zero, all b roots in
the half-open reduced interval, integral reconstruction and identity.

Completed: L129 gives the signed translation and conditional complete
reconstruction. The type-one prefix a=1,...,34 contains 216116 modular
pairs, above the inspection cap. Counting and complete verification use
100113+91850=191963 units per execution. The initial ledger omitted 204
CRT inverse preparations; repairing it and rerunning the same scripts
caused two executions, or 383926 actual cumulative units, above the
cap. This overrun is an execution limitation, not a larger authorized
budget. All 44172 saved
progression contributions were inspected by the independent CRT verifier.
No exact square test, b-root trial or expansion ran; the unvisited source
regions remain uncounted. Full certificates are under
`scripts/pair-genus-two/seminvariant-workload-*.json`.

The fixed sieve/per-p inspection traversal stops; stronger sieves are
not ruled out but no retuning was attempted. ATTEMPTS/054 preserves the
stop. A three-descent source comparison is proposed as a different
mechanism and is REVIEW_REQUIRED, not ready mathematics. No rank or
Selmer claim follows from this result; L108 and previous work remain.
