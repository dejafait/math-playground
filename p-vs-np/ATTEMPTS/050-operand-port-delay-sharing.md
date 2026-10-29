# Attempt 050 — preserving every operand-state delay prevents linear sharing

Step 530, 2026-10-27. The precise interface restriction, full finite-rank
proof and original-endpoint ledger are canonical in
[L116](../lemmas/L116-operand-port-delay-state-obstruction.md).

**WHY IT FAILS.** A shared delay whose n-by-n port transfer is
(1+x)^r I_n needs at least n(r+1) vertices, even with arbitrary sharing,
constant edges and cancellation. Its finite coefficient matrix has that
rank. For r=n=N and an n-vertex unary path operand, the original endpoints
have combined size 16N+14. The ratio is unbounded before any scalar maps
or repeated intermediates are charged. This stops the all-operand-state
identity-delay interface, including compressed descriptions that leave
its transfer unchanged. It is not a proof that every batching mechanism
requires such an interface, and no full batched chain was asserted. A
boundary-coupled construction preserving only the accepting scalar is a
different test. Attempts 042–049 and L115 remain intact; no receiver,
format, cap or historical administrative route is reopened.
