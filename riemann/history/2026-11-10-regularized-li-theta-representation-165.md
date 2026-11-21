# 10 November 2026 — step165: exact regularized Li/theta representation

Completed the approved bounded SPECIALIZE attempt, reusing the unchanged
[assessment](../drafts/literature/2026-11-10-regularized-li-theta-representation-review-163.md).
[L966](../lemmas/L966-regularized-li-theta-resolvent-representation.md)
gives finite positive rational coefficients, the full two-point resolvent
identity, and Q_eta=N_n-R_n in positive actual-theta multiple integrals.
Its proof retains all nodes, multiplicities, chain-rule terms and the
distant-point subtraction. The explicit unpaid comparison is L966(16).

Exact denominator-cleared polynomial and residue checks for n=1,...,12
passed with zero residual; coefficient signs were positive. Full evidence:
[certificate](../scripts/li-theta/regularized-resolvent-check-165.json),
reproducible by its adjacent Python script. These diagnostics do not
replace the general proof or establish the theta inequality.

Outcome ADVANCE, RESEARCH, POTENTIALLY_NEW: a local representation input
using known calculus, with no certified originality or new actual sign.
The original reasoning remains in the step165 working record. No source
refresh or cross-notebook input was needed. Existing generic-logarithm
and theta-realization obstructions remain intact.

Continue with an independent conceptual audit of this representation
under the same exact target and unchanged source coverage. No creative
remainder estimate has been assessed; the new identity first needs audit.
R_n<=N_n, actual mixed positivity and the sufficient regularization scope
for an RH implication remain unresolved. STATUS stays IN_PROGRESS.
