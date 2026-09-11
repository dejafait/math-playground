# Separate progression errors in inverse intervals

The exact weighted discrepancy identity and its proved error bound are
recorded in [L220](../lemmas/L220-weighted-inverse-interval-discrepancy.md).

WHY IT FAILS: Expanding the totient weight and coprimality exactly is
valid, but bounding each progression's endpoint error separately pays
a constant where each inverse interval has length O(1/N). The resulting
bound is worse than the existing enclosing-support bound. Moreover the
real main term is nonnegative, so a small error alone would require an
additional bound on that main term to reach Q_N=O(N³). This rejects
only the separate-error proof method: no lower bound for the actual
error or population, and no counterexample to the target estimate,
is claimed.
