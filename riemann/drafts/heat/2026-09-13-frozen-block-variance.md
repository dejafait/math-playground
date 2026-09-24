# Frozen block variance checkpoint — 2026-09-13

Existing L169 work is complete and preserved. For u=c_j/T the frozen
square has diagonal c₀² T^(3/2) N^(−4) Σ h_u(n/N), with
h_u(x)=x^(−4) exp(−2(log x−(log u)/2)²), 1≤x≤2.
The candidate limit is V(u)=c₀²(2π)^(3/2) ∫_1^2 h_u(x)dx.
Constant-coefficient integration gives off-diagonal error
O(sqrt(T)log T/h), uniform in the midpoint. Mesh variation gives
O(T^(−1/2)) for the diagonal. At H=T^(3/4) both errors vanish.
V'(1)>0 because its integrand is 2 log(x)h_1(x).

Checkpoint: audit constants, mesh endpoints and uniform errors; prove the
nonconstant profile and precisely distinguish a common moment-preserving
law from a common weak limit. No cutoff conclusion is proved here.

Completed: the analytic audit and qualified common-law obstruction are
stored in L170. The cutoff covariance remains unproved.
