# Signed-log specialization working record1509

Closed after completion: the canonical proof is
[C028d](../lemmas/C028d-reciprocal-jensen-signed-log-height-and-fixed-degree-tail.md).
The provisional notes below are retained; they are not a new task.

Approved target: assessment1507, unchanged SPECIALIZE scope. Research in
progress; no degree-uniform or RH claim. Existing work is preserved.

Write Q_d(y)=P_d(y-b_1) and alpha_j=z_j+b_1. The first centered
coefficient vanishes, and the second is -binom(d,2)S_2 by C028a.
Thus sum alpha_j=0 and sum alpha_j^2=d(d-1)S_2. These finite
coefficient identities should cancel the 1/y log tail.

Candidate proof: keep finite symmetric cutoffs for each factor.
Split log|y-(a+ib)|-log|y| into the nonnegative vertical term
(1/2)log(1+b^2/(y-a)^2) and log|y-a|-log|y|. Tonelli applied
to integral_0^|b| t/((y-a)^2+t^2) dt gives pi|b| for the first;
the second has symmetric integral tending to zero, using
Phi(u)=u log|u|-u. Do not give the latter separate one-sided integrals.

For rho=max|alpha_j|, the convergent exterior log series gives
f(y)+f(-y)=-sum_(k>=1) Re(sum_j alpha_j^(2k))/(k y^(2k)).
Proposed tail remainder after -d(d-1)S_2/T is bounded by
sum_j|alpha_j|^4/[6T^3(1-(rho/T)^2)] for T>rho. Check all
constants, the real-singularity cases, and coefficient-only cutoff.

Unpaid after success: actual H_d=o(d), any uniform-in-degree
integrability, and every bulk estimate. Source notes1507 cover the
known finite-factor method; no new literature search is needed.
