# Growing-jet bump projection — bounded mathematical attempt

Invocation-start EXPLORE target: the exact L637 bump and weighted complex
projection onto derivatives through floor((log T)^(1/3)). Supplied
PROOF/DAG and prior assessment used directly. Existing work preserved.

Main gap: actual-Xi initial signs at unbounded heights and all-degree mixed
positivity. The downstream test is whether this growing family can realize
the microscopic observer, independently of its signed transfer budget.
Require uniform projection o(1) or a rigorous refuting sequence; a loose
inverse-Gram envelope is inconclusive. L637's TV stop and L638's fixed
two-dimensional estimate do not settle this test.

Partial reasoning saved before completing estimates:

- Keep Bettin's full two-term main expression with the exact Hardy phase.
  After phase replacement, retain the regular part j(c)=zeta(1+c)-1/c.
  With c=i(r-s)/L and q_t=log(t/(2pi))/L, the pole part is
  L times the Fourier integral on [-q_t/2,q_t/2]. The remaining arithmetic
  terms are exp(i(r-s)q_t/2)j(c) and its reflected companion.
- For a polynomial P of degree n, c^m times the exponential contracts to
  L^(-m) (|P|^2)^(m) at that endpoint. A quantitative Legendre derivative
  estimate may bound this by C(n+1)^2[C(n+1)^2/L]^m times the interval
  norm. This must be justified with all factorials, not assumed.
- The power-saving analytic remainder can tolerate coefficient/Cauchy
  costs exp(O(n log(n+2))). A pointwise convexity plus Cauchy bound has
  the same acceptable cost; paired with the normalized bump it may give
  projection <=T^(-1/2+epsilon+o(1)) times logarithmic factors.

Unresolved at this checkpoint: endpoint polynomial estimates, full regular
main-term contraction and its actual-Gram coercivity, quantitative
coefficient bounds, uniform compact-strip convexity, and normalization of
the bump correlations. No conclusion is established by this checkpoint.
Imports are Bettin Thm 1 and the classical tools in the prior assessment;
L638 Section 1 supplies only the analytic conversion before its O(T)
simplification. L465/L622 supply the gamma/Hardy bounds. No real-axis
Riemann--Siegel error is differentiated; no fourth-moment input is used.

Completed this same attempt: the full proof is canonical in
[L639](../lemmas/L639-growing-hardy-jet-bump-projection.md). The regular
main-term relative cost is at most
4 M (n+1)^2 exp(32(n+1)^2/L)/L; the remaining Cauchy cost uses
A_n=sqrt(2)(n+1)10^n n!. Both required smallness comparisons hold
for the approved n. Actual-Gram coercivity and bump correlations yield
the uniform vanishing projection. This is unaudited obstruction evidence;
the early unresolved list above records the checkpoint, not a later gap.
