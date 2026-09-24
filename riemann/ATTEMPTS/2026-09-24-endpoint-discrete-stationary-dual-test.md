# Endpoint discrete stationary-dual test — 2026-09-24

Gap and target: test the actual coupled discrete mean D_N=o(1) in
L344 by transforming its sampling phase before estimating it. Seek
uniform partial-sum control o(N), with summable frequency errors and
the moving coefficient variation retained. This could contribute to
positive endpoint margins on a density-one subset of the prescribed
pairs; exceptional pairs, low Laguerre indices and the global mixed
positivity gap would remain. Continue only if the transformed
certificate saves over N after its errors are included. A proved
order-N budget stops this certificate, not the actual discrete mean.

Redundancy review: read GOAL.md, PROGRESS.md, the whole PROOF.md and
the global DAG, and inspected the tracked diff and untracked files.
L344 stops derivatives in the sampling index. L175, L178 and L319
already warn that stationary duality alone need not improve a bound;
the new test must calculate the exponentially long dual, its weights,
frequency uniformity and endpoint errors for these actual samples.
L333's continuous-height mean and L343's translated-return obstruction
do not settle this discrete mean. All existing changes are preserved.
The September 21 admission condition is superseded by GOAL.md;
its mathematical evidence remains relevant.

Unfinished reasoning saved before the uniform transform: L333's
divisor majorant should give sum |h_r(omega)| |omega|=O((r+1)^9),
so frequencies above exp(N) have negligible mass. L344 already
controls frequencies below exp(-2N). In the remaining band the
square-root phase differs from omega exp(4x) by O(exp(-3N))
for x>=N. A smooth cutoff can equal exactly one at the retained
integers and zero at all others, with transitions between integers.
Poisson summation then suggests the dual phase
G_omega(k)=k(1-log(k/(4omega)))/4, stationary amplitude 1/(2sqrt(k)),
and stationary point x_k=log(k/(4omega))/4. A local smooth
stationary-phase expansion should have summable error
O((omega exp(4N))^(-1/2)), including transition regions. The
second derivative is -1/(4k); on each multiplicative block the
weighted second-derivative budget is order one, with order N blocks.
Higher fixed derivatives appear worse. These claims and the
moving-weight comparison require proof; they are not yet a sign
theorem or a conclusion about D_N. Zero consecutive unresolved
exploration turns precede this test. No RH candidate.

Review checkpoint — 2026-09-24: this turn found the preceding saved
reasoning and an unregistered L345 draft already in the working tree.
The single step is to review and finish that result, preserving its ID.
The local smooth Poisson calculation has been checked through the
Gaussian remainder and both frequency tails: its error is uniformly
O(exp(−N)), and exact moving-weight Abel summation costs only
O(N^8 exp(−N)) for that error. On the plateau, the second-derivative
certificate costs a constant on each of order N dyadic blocks.
The remaining review concerns the scope of the lower-budget claim,
its comparison with the fully weighted o(1) target, and the route
decision after the two derivative-based tests. This saved assessment
does not assert a lower bound on the actual signed sum.

Completed assessment — 2026-09-24: NEGATIVE.
[L345](../lemmas/L345-endpoint-discrete-stationary-dual-budget.md)
proves the smooth dual formula uniformly for every partial interval
and exp(−2N)≤|ω|≤exp(N). The low- and high-frequency tails are
O(N^17 exp(−2N)+N^9 exp(−N)); replacing all partial sums in the
moving-weight identity costs O(N^8 exp(−N)). Thus the endpoint
transitions, square-root correction and summed transform errors
meet the required scale. The remaining weighted derivative budget
is comparable to the original partial-interval length, and its
fully weighted certificate has positive liminf rather than o(1).
The review makes the full coefficient-weighted target explicit in
(7a): an unweighted o(N) assertion alone would not suffice.

WHY IT FAILS: the [canonical proof](../lemmas/L345-endpoint-discrete-stationary-dual-budget.md)
shows that curvature |G''(k)|=1/(4k) gives an order-one weighted
second-derivative cost per dyadic interval. There are order N such
intervals. Every allowed fixed higher derivative, the trivial bound,
and subdivisions retain this lower budget; absolute Abel summation
then retains a positive fraction of L344's grouped coefficient mass.
This stops the specified certificate, not actual cancellation within
or between blocks or frequencies. It does not show D_N fails to tend
to zero, or that the certificate exceeds the fixed threshold 1/4.

Decision: the direct and dual derivative tests now both fail their
targets, so stop this approach rather than iterate the transform.
A joint large-sieve estimate is a different mechanism: it would use
sample and frequency correlations before separate absolute bounds.
The repository search found no prior test of that estimate for D_N;
continuous means, stationary involutions and uniform-return failures
do not provide it. Such an estimate would still have to handle the
moving coefficients and their tails. The pointwise endpoint margin,
exceptional pairs and lower-index signs remain unresolved; all sign
and exclusion ranges are unchanged. Zero consecutive unresolved
exploration turns remain, and there is no RH candidate.

Verification: reviewed the smooth cutoff at each integer, compact
partition, uniform Gaussian remainder, nonstationary Fourier tails,
geometric error sum, rationalized phase correction, divisor-weighted
frequency tails, all-order exponent comparison and exact Abel target.
The primary Heath-Brown source confirms equation (1) and Theorem 1;
DLMF supports the stationary-phase method only. L345 preserves the
direct citations and the separate Mathlib status, which is not checked.
No numerical sign or sampled-height experiment is used. The DAG adds
only the two mathematical inputs used by L345; the earlier involution
results are comparisons. All pre-existing work and identifiers are
preserved.
