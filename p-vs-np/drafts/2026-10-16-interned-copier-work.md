# Step 257 — pool-aware complete-record copying

Approved target: implement and completely validate a pool-aware full-record
copier from the six preserved step-253 interned packages into one fresh
append-only store within the existing resource caps. The prior SPECIALIZE
assessment is `drafts/literature/2026-10-16-interned-full-record-copier.md`.

Main gap: unrestricted SAT decision/separation. Intermediate target: explicit
pool ownership, simultaneous substitution and complete record relocation.
Downstream use: possible later L065 receiving interface; no Closure integration
is authorized here. Continue only after complete archive comparison, primitive
replay, checkpoint equality and monitored resource checks pass. Preserve any
failure and park the failed boundary without increasing caps.

Inputs are L056 copying/substitution, L065 complete-record reception, L066 exact
local endpoints and L068 §§6–7, together with the unchanged step-253 archives,
source/envelope and step-255 lossless internal checkpoint. The existing
single-pool substitution and bounded differential test are insufficient for
cross-pool IDs. Each copy call will own its translation memo; destination
replacement terms must carry explicit destination ownership. Production
identity copying will compare every field in both formats through EOF and
retain a source-path/local-row/global-row map. Expanded bytes will be measured
separately from compressed storage and reference-digit changes.

Completed bounded implementation reproduction: canonical account is L068 §8;
full evidence is `scripts/output-zero/output/copier-257/verification-complete.json`.
All 155588 source occurrences are retained after one valid prefix; complete
archive comparison and checkpoint primitive replay pass. Code review repaired
numeric-coercing checkpoint metadata equality, preserving the prior source/run;
the correction receives complete separate replay and comparison. All 44
rejection tests pass. Resource observations remain below the unchanged caps.

Independent implementation audit is pending separate scope approval. The parser
limit 4096, Closure compatibility, coordinate generation/output feasibility,
indexed chain/bridge, nested retention, combined original-source ledger,
ordinary-input completeness, certificate existence, ER/W/V/U and SAT all remain
unresolved. No new lemma, graph edge or abstract argument was added.
