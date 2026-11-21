# Endpoint calculation644 — working checkpoint

Completion: the tentative derivation below is now written in full in
[C999z](../lemmas/C999z-response-endpoint-carleman-remainder.md), with
separate critical audit pending. This initial checkpoint is preserved.

Approved target: review642/comparison643 TARGET, unchanged. Main gap:
L030-L032/C032a actual-Xi positivity. This is a REPRODUCTION calculation,
not an S3 sign claim. No external source retrieval or new general theorem.

From C744v Section3 put a=log(3)/4, c_j=2j+1/2, t=a-y,
phi_j(t)=exp(-c_j t), psi_j(t)=exp(-c_j(2a-t)),
b_j=exp(-2ac_j), d=1-exp(-a). The exact product correction after
subtracting phi_j(t)phi_j(s) is

    R_eps,j=[eps b_j phi_j phi_j+psi_j psi_j
             +eps(phi_j psi_j+psi_j phi_j)]/(1-eps b_j).

Its uniform absolute bound is 4exp(-ac_j)/d, so the tail j>=J
is at most 4exp[-a(2J+1/2)]/[d(1-exp(-2a))]. j=0 is retained.
The uncorrected sum is F(u)=exp(-u/2)/(1-exp(-2u)). Its pole is
1/(2u); h=F-1/(2u), h(0)=1/4. Let
q(u)=integral_0^1 exp(-2uv)dv and B(u)=exp(-u/2)/q(u).
On 0<=u<=2a, q>=exp(-4a)=1/3, |q'|<=1, |q''|<=4/3.
The quotient rule gives |B''|<=303/4; thus |h'|<=303/16
using h(u)=1/2 integral_0^1 B'(theta u)dtheta.

Candidate finite rank remainder: midpoint m-cell kernel h(t_i+t_k),
plus R_eps,j for 0<=j<J. Rank <=m+2J. Kernel sup error <=
303a/(16m)+4exp[-a(2J+1/2)]/[d(1-exp(-2a))]. Operator error
<=a times this by Teschl Section6.3 (6.9). Need finish full operator
identity/limits on complex L2 using bounded Carleman kernel and compact
interior tests, and check both endpoint cases, symmetry and all constants.
No proof is yet claimed by this working note. Final canonical proof will
replace the tentative status without deleting this checkpoint.

Continuation after this bounded attempt should be a separate conceptual
audit before use in any inverse/reference. Coercivity, signed induced
coupling, S3, higher endpoints and original analytic/core/c_* contracts
remain open. Prior598 rank-two and32-prefix stops are preserved.
