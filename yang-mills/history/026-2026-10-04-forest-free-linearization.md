# 2026-10-04 — Forest free operator and Gaussian Ward comparison

Reused the prior SPECIALIZE assessment's exact free-linearization
COVERED_TARGET, without additional literature work. Preserved existing
changes and all stopped branches. [L017](../lemmas/L017-forest-free-generator-and-gaussian-ward-comparison.md)
gives the compensated free operator, checks its scaling against the
forest Hessian and proves equality with L009's two responses for the
actual free Wilson-flow probes. This is a reproduction of covered
tree-gauge and Gaussian quotient machinery, with a new explicit local
representation input and no claim beyond the checked literature.

The [working record](../drafts/2026-10-04-forest-free-linearization.md)
was saved before matrix checks. The exact rational/numerical check
`PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python3 scripts/forest-ward/check_free.py`
passes for two N=4 forests with 81 tree edges each. Six reduced diagonal
entries are nonzero in each sample while the total trace is exactly zero.
Deleting the paths changes the curvature map by exactly 3/80 and 1/24.
Both sample flowed Gaussian responses and their Ward covariances agree
within 9e-17. The samples use rational coefficients, not the original
smooth displacement; the proof covers the actual probes. No interacting
expectation or ultraviolet limit is computed by these checks.

Outcome: **ADVANCE / RESEARCH / REPRODUCTION**, confined to finite
representation compatibility. The reflected-error threshold <= c_box/2,
interacting contractions/matching, physical boundaries, continuum fields,
reflection positivity, infrared control and finite positive mass remain
unresolved. STATUS remains IN_PROGRESS with no complete candidate.

End free-identity audits. The next direction reuses the unchanged ready
combined-response TARGET and assessment of 2026-09-26. The explicit
compensated operator with the forest Hessian supplies the new mechanism
for actual contraction tests in L011, beginning with the connected M2
measure term and a forest-dependence test. Retain the other terms before
interpreting any growth as the full logarithm. Require evaluated
mathematics or an informative obstruction; another unevaluated expansion
would not improve the main gap. The earlier direct-expansion attempts and
exhausted bulk-only import are preserved. No inconclusive mathematical
exploration turn is spent and no external state is changed.

Validation: the new rational/Gaussian matrix check passes, and the shared
documentation checker with --problem yang-mills passes with 17 nodes and
32 unique edges. The five direct mathematical inputs in the new DAG row
were reviewed; L011 is a comparison/use, not an input. Whitespace, unique
step fields, prior COVERED_TARGET coverage and exact unchanged ready
next TARGET matching pass. No existing lemma, script or assessment was
modified; the compact overviews remain within their limits.
