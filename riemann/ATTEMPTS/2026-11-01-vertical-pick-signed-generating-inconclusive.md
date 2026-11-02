# Vertical Pick block — signed generating test is inconclusive

WHY IT FAILS: The exact scalar generating coordinates in
[L640, (19)--(22)](../lemmas/L640-vertical-pick-full-gram-arithmetic-reduction.md)
retain all prime-power phases and reduce the Hermitian norm to a
supremum of signed scalar sums with a completely controlled tail.
No uniform bound below the required ell_X/2 threshold and no asymptotic
unit-vector witness were found. Applying the available absolute bound
to the scalar coefficients returns the first attempt's inconclusive
majorant. A coefficient-sensitive bound proves that consecutive blocks
with m4^m=o(log T) have relative corrections tending to zero, so vectors
confined to them cannot supply an asymptotic witness. This excludes a
specific lower-witness test but does not control distributed vectors or
arbitrary sparse supports with large gaps. The full-dimension upper bound
is inconclusive. No numerical spectrum was obtained or used. This is the second
inconclusive arithmetic attempt, so repeating its algebraic reduction
is parked. A materially different rational-kernel concentration/all-zero
count witness is nominated for separate source review; its rank, tail
and off-line-zero requirements are unresolved. The stop concerns this
method, not the norm budget itself and not RH.
