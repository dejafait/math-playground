# Series mass audit — 2026-09-12

L138 is complete and preserved. This step examines the magnitude distribution in its explicit S(t), without claiming a lower bound for S.

Candidate calculation: N=sqrt(t/(2π)), f_N(x)=x^(-2)exp(-(log(x/N))²). Its integral on (0,∞) is sqrt(π)e^(1/4)/N, and its maximum is e/N² at x=N/e. A bounded-variation sum/integral comparison should give Σ f_N(n)=sqrt(π)e^(1/4)/N+O(N^(-2)). Hence any o(N) selected terms carry o(1) of the absolute mass and cannot dominate their complement by the reverse triangle inequality. All claims in this paragraph are draft until audited.

Resume by proving the quadrature bound, recording the precise scope of this obstruction, and retaining the unresolved cancellation comparison with O(1/t).

Completed: L139 proves the mass asymptotic and the precise sublinear-subset dominance obstruction. The draft calculation is superseded by that canonical proof. The full-series lower bound and its comparison with the additive remainder remain unresolved.
