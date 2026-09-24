# Hilbert off-diagonal cancellation checkpoint — 2026-09-13

Prior work through L152 is complete and preserved. Current scoped target: remove
L152's remaining harmonic logarithm in the integrated fourth moment.

Promising route, not yet a proved DAG input: apply the Montgomery--Vaughan
generalized Hilbert inequality to the signed kernel
`1/(log k-log l)` after integration by parts. For the exact moving coefficients,
direct differentiation gives

`a_k'(t)=t^(-1) log(k/N_t^2) a_k(t)`.

The endpoint terms should be controlled by `sum k a_k(t)^2`, and the derivative
term by Cauchy--Schwarz between that energy and
`sum k a_k'(t)^2`. Gaussian absorption at a narrower fixed width should bound
both required energies uniformly by `O(N^(-4) log(2N))`, yielding the target
`O(N^(-4) log(2N))=O(T^(-2)log T)` including the diagonal.

Resume by stating the separated-frequency Hilbert inequality precisely, checking
the infinite truncation limit, both endpoint phases, the derivative identity,
and uniform Gaussian absorption before promoting any claim.

Completed as L153 after those checks. The one-logarithm fourth-moment bound is
proved. No positive-proportion or pointwise conclusion is promoted.
