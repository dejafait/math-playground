# Jerby binomial-to-step unweighted interface — step29

The approved consistency audit is resolved by
[L877](../lemmas/L877-spira-binomial-unweighted-norm-divergence.md).
Under the exact first-N-coordinate definitions of the inspected
arXiv:2405.12557v2 displays, the unweighted norm diverges; the required
threshold was convergence to zero. This is an informative negative
result for that proposed arithmetic interface, not a disproof of RH.

WHY IT FAILS: The total mass of the accelerated coefficient vector is
asymptotically half the step vector's mass. The finite
Cauchy–Schwarz bound in L877 turns this mass deficit into a growing
unweighted ell2 distance. The extra triangular endpoint contributes a
nonnegative squared error and cannot repair the common-coordinate
failure. Park this exact norm justification. Weighted norms, other
cutoffs, oscillatory sums and actual-Xi signs remain separate questions;
none was tested or rejected by this step. Reopening requires a changed,
separately assessed interface and a sufficient signed downstream claim.
