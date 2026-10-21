# Step 272 — bounded structural attempt

Approved target: Test whether treewidth at most two of the full signed extension-value DAG suffices for polynomial-full-bit L037 data from a supplied ER refutation.

Prior coverage: `drafts/literature/2026-10-16-treewidth-two-extension-data.md` (SPECIALIZE, unchanged at invocation). Main gap: unrestricted SAT decision/separation; intermediate gap: complete reduced affine-ABP data for L037. The intended use is restricted certificate assembly. Arbitrary ER, formula-only bounds and SAT transfer remain independent obligations.

Checkpoint before the proof attempt: read the complete L026 construction, L025/L037 receiving hypotheses and relevant graph composition, and Attempts 019–021. None establishes a stop under the present structural promise. Existing files and unfinished work are preserved. No mathematical scripts or additional source search are planned.

Mechanism being tested: attach independent selector inputs locally to all vertices of a width-two decomposition and aggregate their gated values along that decomposition. A constant-treewidth single-output circuit would yield one OBDD whose selector restrictions supply every original root in the same induced order. Separately, realize L026's K and W recurrences as forward suffix-state networks with independent local correction blocks; recursive terms are left multiplied, so no recursive block copying should be necessary. These are provisional ideas at this checkpoint, not established claims.

Continuation test: prove a common-order polynomial aggregate bound and the exact free-ring H identities with explicit affine graph encoding; a rigorous partial interface is useful. Narrow/abandon if selecting all roots increases treewidth with input size, or the witness construction needs recursively unfolded paths or circuit-valued edges. Full proof, if completed, belongs in a canonical lemma, not here.

Completed outcome: the full informal restricted construction is now canonical in [L071](../lemmas/L071-treewidth-two-extension-affine-abp-data.md). Both interfaces passed this proof attempt, with a fixed selector-treewidth bound and one aggregate graph/bit ledger. The proof remains unaudited separately; no implementation or finite test was performed. The next audit scope is recorded with REVIEW_REQUIRED and is not approved in this turn. All details and qualifications are in L071 rather than duplicated here.
