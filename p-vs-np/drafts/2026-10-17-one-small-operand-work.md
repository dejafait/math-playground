# One-small-operand construction — step 300

Authorized target: the unchanged EXPLORE target in
`literature/2026-10-17-one-small-operand-affine-abp-data.md`.

Main gap: unrestricted SAT decision/separation; nearer gap: polynomial
all-root L037 data for general supplied ER. Test the operand-only promise,
without asserting it for arbitrary proofs.

Work in progress: partition source nodes by syntactic support at threshold
k=floor(log₂(T+2)). Replace each small positive root by its ordered support
truth-table formula, with exact complement wrappers. Retain ordered
products at large outputs. Each remaining large AND has at most one large
child, suggesting a single large-node chain per unfolded root, with paid
small table formulas attached. A small output has only small ancestors,
so its actual operand representatives should equal L026's ordered
diagram representatives. Use L071's audited post-compilation component
only there; large-output relations should be identically zero.

Continue if the chain bound, formal small-root identification, both H
identities, all-root dictionaries, pre-substitution degrees and bit time
fit one polynomial in actual T. Stop this mechanism if an interface
needs Boolean equality outside the increasing multilinear subspace or
unbounded copying. Preserve Attempts 019–020; neither is a counterexample
to this specific syntax. No new external source or cross-notebook input.

This initial checkpoint claimed no completed result. The attempt then
closed the stated interfaces; the full informal proof and ledger are in
`lemmas/L078-one-small-operand-affine-abp-data.md` (not duplicated here).
Its separate critical audit remains pending. No mathematical scripts were
run and no originality or unrestricted complexity conclusion is claimed.
