# Hardy-translate dual test: calculation checkpoint

Completed in lemmas/L637-hardy-translate-dual-cost-and-absolute-error-budget.md.
That file is the canonical full proof, presently awaiting a separate audit.
The intermediate checkpoint below is retained as working history.

Approved target: test the Fourier-filtered dual certificate and its complete
TV-summed shifted-moment error. Invocation assessment:
`drafts/literature/2026-11-01-hardy-translate-dual-test-scope.md` (EXPLORE).
One mathematical attempt; no new source assessment is being approved.

Main gap: actual-Xi initial pointwise signs at unbounded heights. The fixed
normalized microscopic bump is a realization diagnostic only; signed
approximation and continuum-observer positivity remain independent gaps.

Partial reasoning, not yet a completed proof: use angular Fourier transform
psi_hat(xi)=integral exp(-i*x*xi) psi(x) dx. Choose a smooth real even chi,
0<=chi<=1, chi=1 on [-3/4,3/4], supported in [-1,1]. Let
h=F^{-1}[(1-chi)psi_hat]. Then ||h||_2<=||psi||_2 and
<psi,h>/||psi||_2^2>=1-1/pi, by support length one and Plancherel.
Use a smooth macroscopic spatial cutoff supported where w>=w(u0)/2,
and divide by w only there. The resulting weighted dual vector should
have limiting norm <=1 and overlap >=1-1/pi, leaving a positive margin
above the 1/4 tolerance.

Correlation proof to finish: freeze the Riemann--Siegel index at a, retaining
all cutoff crossings in an absolute error. For t=a+(x+s)/L comparable to T,
the number of changed terms is <=1+C*|x+s|/(L*sqrt(T)), each of size
O(T^(-1/4)). Phase linearization costs O((x+s)^2/(T*L^2)) times
sum_(n<=N(a)) n^(-1/2)=O(T^(1/4)). Schwartz tails of h should make the
spatial truncation negligible. Both signed linear frequencies are within
the removed band, uniformly in X and |s|<=1. The undifferentiated
Riemann--Siegel remainder has the sought O(T^(-1/4)) integral scale.

If all these bounds hold, finite-complex-sum weak duality gives TV at
least c*T^(1/4)*sqrt(L). Independently finish the exact h=k=1 moment
extension using L622 Sections 1--4: fixed-radius complex shift Cauchy
bounds, all coefficient pairs, exact six-term main expression and phase,
and translated absolute fourth moments for curvature. The nominated
raw bound is C_w*TV^2*(T^(19/25)*L^2+T^(-1)*L^4).

Continuation/abandonment test: establish overlap and the uniform atom
correlation, then compare the proved envelope even with T*L^6. An
incompatible upper envelope would stop only this sufficient absolute-error
mechanism, not lower-bound the true remainder or rule out cancellation.
Known tools are imported/reproduced; the inverse estimate is unverified
and no novelty or RH claim is made at this checkpoint.

## Completed analytic calculation, pending canonical write-up and later audit

The cutoff comparison above works uniformly, even exactly at an integer
Riemann--Siegel cutoff. Both endpoint indices are comparable to sqrt(T),
so every changed summand has size O(T^(-1/4)); the extra one in the count
must be retained. Linearization of the phase is used only inside an
integral against a Schwartz function, and does not require its pointwise
error to be small throughout the macroscopic cutoff support.

The complete moment extension uses Q=partial_1 partial_2
-(partial_1^2+partial_2^2)/2 at (0,0,s_j,s_k), with unit Cauchy radii in
the first two coordinates and the entire six-term source expression.
Each error is O_w(T^(19/25)*L^2); absolute summation is exactly bounded
by (sum |c_j|)^2. For curvature, a fixed smooth majorant of all translates
w(u-s/(TL)), |s|<=1, imports L622's unshifted fourth-moment bound uniformly.
Weighted Holder then bounds every mixed product by O_w(T*L^4), yielding
the additional O_w(T^(-1)*L^4*TV^2) term.

The lower cost makes the displayed envelope scale divided by T*L^6 at
least c*T^(13/50)/L^3, which diverges. The sufficient budget instead
requires TV=o(T^(3/25)*L^2). This is a limitation of using that complete
absolute upper bound; it is not a lower bound on the actual error.
No numerical evidence or mathematical script is needed for these estimates.
