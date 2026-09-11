# A stationary transform alone does not supply first-moment decay

The full-endpoint transform is established in
[L175](../lemmas/L175-last-block-stationary-transform.md).
This is a completed reduction, not a failed transform.

WHY IT FAILS: as an attempt to obtain the desired little-o first moment
using the transform and second moments alone, it returns a logarithmic
sum with Θ(N) terms, order-one amplitudes and square mean N+o(N).
Cauchy–Schwarz still gives only O(sqrt(N)). The uniform transform error
is small enough, but no new cancellation estimate has been supplied.
This does not refute the little-o claim or exclude stronger methods.
