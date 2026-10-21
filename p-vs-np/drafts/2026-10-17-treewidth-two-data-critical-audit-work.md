# Step 274 — L071 critical audit

Approved target: Critically audit L071's all-root selector reduction, affine-ABP suffix realization and aggregate full-bit bound under the full signed treewidth-two promise.

Coverage is the unchanged SPECIALIZE assessment
`literature/2026-10-17-treewidth-two-data-critical-audit.md`. The shared and
local startup snapshot, full overview and DAG were supplied and read. Read
L071 in full, L026's complete proof, L025's receiving hypotheses/conclusion,
L037's receiving hypotheses and graph operations, the structural assessment,
history/271–272 and Attempts 019–021. Existing local changes are preserved.
No cross-notebook input, new source search or mathematical script is used.

Main gap: unrestricted SAT decision/separation. Intermediate target: verify
that L071 really supplies the promised restricted L037 data, including one
common order, formal identities and full binary size. The downstream use is
L037's conditional certificate construction, not a SAT algorithm. Continue
if every interface survives or admits a bounded repair; otherwise isolate
the exact defect and narrow the construction.

Checkpoint before final ledger audit: the degree-two elimination/minor
argument and the selector bags check out. K paths switch only from the
commutator region to a value suffix; W paths make one final exit from the
pair region. These match the written L026 recurrences without reordering
factors. Remaining checks are path degrees, all endpoint degeneracies and
the aggregate encoding convention. No final correctness verdict yet.

Completed verdict: the all-size audit in
[L071](../lemmas/L071-treewidth-two-extension-affine-abp-data.md) finds no
substantive defect. It explicitly checks all bag occurrences, ordered path
partitions, degree bounds and the aggregate dictionary convention. This is
verification of the existing restricted input, not a stronger theorem or
progress beyond the sources through a new construction. No executable
certificate was produced or claimed. The argument and DAG are unchanged,
so PROOF.md is left untouched as required; its earlier pending-audit wording
is superseded by the canonical audit and current checkpoint.

Next proposed scope: logarithmically many supplied original-variable
deletions leaving treewidth two. That changed promise is not covered or
derived here. Its assessment is REVIEW_REQUIRED for a separate literature
turn; potential incompatible conditioned orders and formal gluing costs
must be assessed before any mathematical attempt.
