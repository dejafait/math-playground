# Pointwise derivative route to the last-block first moment

Date: 2026-09-13. The scoped audit is proved in
[L174](../lemmas/L174-derivative-test-limit-for-last-block-first-moments.md).

WHY IT FAILS: the second derivative of the logarithmic phase stays of
constant order, while the third is of order 1/N. The classical tests
therefore supply only O(N) and O(N^(5/6)) pointwise bounds. Averaging
these is weaker than the existing O(sqrt(N)) mean bound. The available
lower bound also allows a vanishing normalized first moment. This
failure applies to these estimates, not to the desired little-o claim
itself. A transform retaining arithmetic phase structure is still an
unresolved option.
