# Angular projection: zero-evaluation transfer stop

The approved Fourier test gives the exact nonpositive angular energy
and a noncancelling rationally continued value at u=0 in
[C645p](../lemmas/C645p-angular-projection-zero-evaluation-cost.md).
The transfer factor from that value to the boundary norm is exactly
(80/121)^(n-1)*(n-1)!/n^(n-1), sharp on the ambient common-pole rational
space. Its exponential rate is 1+log(121/80), exceeding 1/32.
The proof is unaudited; the standard Fourier/Blaschke inputs are
specializations, with no certified novelty claim.

WHY IT FAILS: Positivity of the original residues does prevent
cancellation at the continued value, but that value is reached across
all common angular poles. The exact norm of this continuation functional
loses too much. Even retaining the entire spatial continued response
leaves its resulting lower estimate uniformly o(exp(-n/32)) when
M<=n/3. Sharpness concerns the ambient rational space, whose extremizer
has not been realized by the prescribed positive integer residues.
Thus neither the actual projection nor the full angular target is
refuted. A better estimate needs family-specific information beyond
this value and ambient norm; the full signed projection formula is
preserved. The next proposed test instead bounds the full angular
operator mean from above for radius-adjusted Chebyshev families.
