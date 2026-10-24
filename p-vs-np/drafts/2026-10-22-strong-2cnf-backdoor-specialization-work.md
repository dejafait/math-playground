# Step 411 work checkpoint — supplied strong 2-CNF backdoor

Approved target and STEP_REVIEW: the unchanged TARGET in
`drafts/literature/2026-10-22-source-2cnf-backdoor-specialization.md`.
RESEARCH / proof_attempt / REPRODUCTION. No new coverage decision.

Main gap: unrestricted SAT decision/separation. Intermediate target:
export ordinary source-resolution from the supplied strong 2-CNF
backdoor and apply audited L097 to the exact original occurrence pair.
Downstream use: another restricted source-proof supplier, without an
incidence-decomposition premise. Inputs L087 and L097 (including its
step-380 constant repair). L104/L096 and Attempts 030–035 are comparisons,
not mathematical premises. No failed universal promise is reopened.

Proposed record plan (not yet a completed proof): normalize auxiliary
literal sets only, storing actual source clause positions and retaining
all raw source/occurrence/backdoor records. For each assignment on S,
obtain labelled implication-path branch proofs (or immediate empty
clause), then lift every branch line by the full blocking clause.
Original leaf C_j is a subset of its residual union the blocking clause,
so a paid weakening can realize the lifted leaf with an actual C_j
reference. Resolve the full family of blocking clauses in a binary tree.
Handle units, tautologies, duplicates, k=0, no remaining variables and
early closure. Then compose L097 at its fixed polynomial exponents.

Resource target: at most 2^k poly(Q) archived branch records, each of
width at most k+2 (raw source leaves have width at most three), all
names/references and retained data charged in original Q. Pay global
reference lengths before applying L097. Need a common fixed
C 2^{c k} Q^a for both output and deterministic bit time. No implementation
or finite check is required; the all-size proof must establish this.

Stop/narrow if ordinary-resolution provenance, exact fg/B, or fixed
exponents fail. Small backdoors for arbitrary sources, general short
proofs, M-only bounds, universal W₂, arbitrary ER data and SAT transfer
remain unproved. This file preserves unfinished reasoning; it is not
an established lemma or an independent dependency source.

## Completion pointer

The attempt is now completed informally in canonical L105. The actual
source-resolution archive, boundary cases and fixed-exponent original-Q
ledger are proved there; this work note is not a second proof. Separate
critical audit remains pending. See the current PROGRESS.md for routing.
