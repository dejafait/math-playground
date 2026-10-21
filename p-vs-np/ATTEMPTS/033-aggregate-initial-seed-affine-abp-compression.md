# Attempt 033 — Polynomial affine-ABP compression of the isolated aggregate

The target allowed arbitrary sharing, cancellation and refactoring of
L099's exact initial-seed contribution S_n after B substitution, setting
later Z_i=0 first and stopping before the final multiplier b. It went
beyond Attempt 032's literal whole-seed cache rule.

**WHY IT FAILS.** [L100](../lemmas/L100-renaming-aggregate-seed-affine-abp-obstruction.md)
exhibits an identity coefficient submatrix of order 2^(n−1) in the
lowest homogeneous component. Nisan's cut factorization, specialized
to affine DAGs over the actual growing alphabet, charges this rank to
the original graph's vertices. The resulting bound exceeds every fixed
polynomial in L099's original Q. This is an all-size informal proof,
whose separate step-392 critical audit finds no substantive defect;
four complete finite checks support it but do not prove the asymptotic
result. The audit is canonical in L100 and changes no bound or input.

Stop exact-output affine-ABP compression of this isolated contribution.
Preserve Attempts 020/032. The full K_n retains later seeds and has
B image p; the lower bound therefore cannot be promoted to hardness
of the complete certificate or its alternatives. A route using that
cross-seed cancellation would be materially different and would need
its own independently testable target and source coverage. The source
CNFs still have easy alternative proofs. No SF/EF or SAT lower bound
is claimed.
