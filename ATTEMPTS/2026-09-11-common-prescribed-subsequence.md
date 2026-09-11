# Common prescribed subsequence — 2026-09-11

The proposed strengthening of Lemma 101 asked whether every prescribed
set admits one subsequence working for all permitted heights.
[Lemma 102](../lemmas/L102-no-common-upward-subsequence-at-power-coordinates.md)
refutes it already when every positive integer is prescribed.

WHY IT FAILS: Weighted averaging gives a small value for each fixed
height sequence, but cannot exchange the height and selection
quantifiers. Along any proposed indices, sparse summable height
increments can be placed just after selected indices. The horizontal
successor gaps shrink, so these increments maintain a positive
single-successor contribution at infinitely many selected indices
while the total height remains bounded. This leaves the proved
height-dependent selection intact.
