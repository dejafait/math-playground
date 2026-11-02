# Fixed L233 Stein diagnostic — saved reasoning

Approved target: test only the fixed L233 mixture's Stein nonincrease.
Main gap remains actual-Xi all-degree signs at unbounded heights. This
diagnostic tests a proposed sufficient hypothesis, not the Xi kernel.

Put q=exp(-4), g(u)=exp(-u^2)/sqrt(pi), and
k=g+[g(u-2)+g(u+2)]/4. For N(u)=integral_u^infinity v k(v)dv,
tau=N/k is smooth, N'=-u k, k'(0)=0, and

tau''(0)=-1-tau(0) k''(0)/k(0).

Direct shifted-Gaussian integration gives
N(0)=k(0)/2+integral_0^2 exp(-v^2)dv/sqrt(pi),
k(0)=(1+q/2)/sqrt(pi), k''(0)=(-2+7q)/sqrt(pi).
The elementary bounds exp(4)>13 and integral_0^2 exp(-v^2)dv>2/3
give tau(0)>185/162 and -k''(0)/k(0)>38/27. Thus
tau''(0)>1328/2187>0, and tau'(u)>0 for all sufficiently small u>0.

Canonical proof will verify the differentiations, shifted integrals,
and strict bounds. Import L233's Fourier failure without recomputation.
No parameter change, actual-theta calculation, or generic transfer proof.
