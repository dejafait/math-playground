# Bare norm-square ambient rank bound — stopped

2026-10-14. [L069](../lemmas/L069-bare-unit-rank-obstruction.md) proves
that the entire norm-square ordinary-unit subspace has dimension twelve
and E0(K)[2] is zero. The exact model, complete cubic field, archimedean
types and arithmetic are retained; all ten certificate checks pass.
Separate independent critical review on 2026-10-14 confirms this stop:
L069's canonical audit records all 33 independent checks passing and
verifies the field, norm, unit and Kummer hypotheses without correction.

WHY IT FAILS: Any norm-square two-descent upper space retaining all
ordinary unit classes has dimension at least twelve, so subtracting
the actual rational two-torsion gives at least twelve instead of the
required at most eleven. Adding finite support primes or class
contributions cannot repair that size test. This does not lower-bound
actual rank or stop two-descent with genuine local restrictions,
elliptic Chabauty, other global arithmetic or integer lifting. Reopening
this unchanged simplification requires a concrete defect in L069;
removing unit classes through a certified local condition is a different,
independently assessed target. Preserve ATTEMPTS/029–031 unchanged.
