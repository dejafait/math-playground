# Common-terminal eta budget — step202 working checkpoint

Completion note: the calculation below is now written in full in
[L974](../lemmas/L974-common-terminal-eta-triangular-error-budget.md),
with B_n<=A*(n^2+119/648)<16*A*n^2. Independent proof audit is
pending. The original unfinished checkpoint is preserved below.

Approved target: the exact B_n<=16 A n^2 test in
`literature/2026-11-10-triangular-eta-error-review-201.md`.
Main positivity/signed-forcing gap remains unresolved.

Unfinished calculation, not yet certified: for u=eta_n, H_k=a_k^2,
write E_n(k)=-k^2 F_u+r_k, where
F_u=u sum_j beta_j/(beta_j+u) and
r_k=-u sum_j beta_j(H_k(beta_j)-k^2)/(beta_j+u).
L964's unconditional Cauchy bound suggests |F_u|<=A and
|r_k|<=A*9^(k-n)/8 for 1<=k<=n. All separated sums must be
checked absolute before using these expressions.

The finite weighted difference is expected to give
T_n=E_n(n)-(n-1)E_n(2)+(n-2)E_n(1)=E_n(n)-J_n.
Consequently the quadratic part contributes at most A*n^2 to
|J_n|+|T_n|; the remaining bound is
A/8*[1+2(n-1)9^(2-n)+2(n-2)9^(1-n)].
At n=3 the bracket is 119/81, and both n-dependent terms decrease.
Pending checks: finite endpoints, exact initial expressions,
convergence, monotonicity and comparison with 16 A n^2.
No RH, new source, theta off-diagonal extension or tail modulus used.
This is a component specialization, not central cancellation or RH.
