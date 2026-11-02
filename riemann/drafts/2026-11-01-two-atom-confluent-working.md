# Two-atom confluent specialization: working checkpoint

The approved target and assessment are in
`drafts/literature/2026-11-01-hardy-two-atom-confluent-error-test.md`.
No conclusion was claimed at this early checkpoint. The completed proof
is now canonical in L638; its separate critical audit remains pending.

Use exactly L637's w,T,X,L,Z,W,M,E,G. Proposed proof: apply the two
observer divided differences to L637 (20)'s complete holomorphic error
before absolute values. Fixed derivative orders should give a bound
O((|c0|^2+|c1|^2) T^(19/25)L^2), without inverse powers of h.
Derive the smooth second moment from Bettin with fixed physical shifts
at every endpoint. Its limiting Gram functions are 1 and
(exp(i h u)-1)/h on [-1/2,1/2]; compare the second function with i u
to prove uniform complex coercivity for real 0<|h|<=1/2.

Still to justify: every smooth-weight partial integration and phase/pole
limit, the error after both observer differences, and curvature for the
divided-difference observer. For curvature obtain complex shifted L4
bounds from the complete fourth generator, then normalized first
derivative L4 bounds by Cauchy/Minkowski; never divide a TV bound by h.
Remaining main-goal gaps include higher-order/large dictionaries,
realization, signed approximation and main-term margins.
