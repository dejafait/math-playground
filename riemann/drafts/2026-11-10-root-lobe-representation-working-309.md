# Exact-root lobe specialization — working checkpoint, step309

Approved target: review308's exact representation and aggregate high-zero
tail <=100*(n+2)^6. This is REPRODUCTION under SPECIALIZE, not a
signed positive-lobe estimate. Inputs read: L985's exact connection,
audited L988 in full, reviews249/251 and review288's explicit-formula
contract; comparison stops233/235/243/307 remain in force.

Proposed test function: F(x)=2*pi*exp(pi*x)*K_n(-2*pi*x) on
[-b/(2*pi),-a/(2*pi)], zero elsewhere. The endpoints vanish exactly.
Its transform should be T_(n,I)(s); check the source normalization.
It is compactly supported, continuous, piecewise C^1, and zero near0.

Two finite integrations by parts should leave only derivative
endpoints and the second-derivative integral. L988's constants
a_n=n(n+1)/6, b_n=n(n+1)(n-2)/24, P=2(a_n+b_n)
bound each interval by P*exp(n)/gamma^2. At most n-2 complete
intervals occur since K_n has degree n-1 (no real-root or simplicity
assumption needed). Thus the proposed aggregate bound is at most
(n-2)*P*(40*n+80*log2), below the target by elementary inequalities.

Pending before canonical completion: verify the precise source
gamma term and cancellation of Phi(0), absolute convergence before
identifying the symmetric zero sum, prime-power endpoint convention,
small n and all aggregate constants. Expected representation is
C_(n,I)=-sum_rho T_(n,I)(rho)-integral_a^b K_n(u)*exp(-3*u)
/(1-exp(-2*u))du; this line is not yet certified in this checkpoint.
No low-zero signs, clipped intervals, both logarithmic complements,
or regulator/infinite-degree interchange is supplied.

Completion: the pending checks above are discharged in canonical C988a,
including the displayed sign/exponent of V and the complete all-n
inequality. This checkpoint is retained as the unfinished reasoning
saved before the primary normalization check; consult C988a for the
finished proof. Independent audit is nominated under review309.
