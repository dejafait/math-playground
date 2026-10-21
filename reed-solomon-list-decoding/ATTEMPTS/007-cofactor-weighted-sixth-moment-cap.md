# Cofactor-weighted sixth-moment upper test

Tested on 2026-10-04 under saved EXPLORE coverage.

## WHY IT FAILS

The [canonical weighted-energy calculation](../lemmas/L017-cofactor-weighted-energy-and-sixth-moment-cap.md)
keeps the complete cofactor and signed subset sum coupled in the exact
energy J_3-J_2/Q. Its effective estimate uses exact second, fourth and
sixth cycle moments, but then takes an L2 triangle inequality over the
signed permutation terms. The resulting uniform cap is below 56.386
times threshold, improving the older support cap above 1050 times
threshold, while remaining insufficient to certify family safety.
This failure concerns the unsigned-cycle norm estimate; it is not a
lower bound on actual energy, an unsafe-list witness, or a general
obstruction to signed correlations. Further use of the energy identity
must estimate the residual-root collision difference itself or retain
useful signed cross terms, rather than change norms again. The exact
sufficient energy threshold is recorded in L017. The fully split
subtraction remains nonnegative and unused for this upper test.
