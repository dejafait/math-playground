# Fixed negative-heat center expansion — 2026-09-12

Checkpoint before calculation: L137 is complete. Set a=1, H(t)=((2-it)(1-it)/2)π^(-(2-it)/2)Γ((2-it)/2), so F(0,t+3i/2)=H(t)ζ(2-it). Candidate expansion as t→+∞:

F(-1,t+3i/2)/H(t) = Σ_{n≥1} n^(-2+it) exp((-π/4+i(log n−(log(t/(2π)))/2))²)) + O(1/t).

This is a candidate only. Resume by proving the H(t+v)/H(t) expansion on |v|≤t^(1/4), bounding the remaining Gaussian tails relative to |H(t)|, and justifying the Dirichlet sum interchange. An additive O(1/t) error is not a relative asymptotic when the displayed sum cancels. No center lower bound follows without a separate comparison of the leading sum and the error.

Completed: the audited additive expansion and absolute-mass comparison are proved in L138. The candidate formula above is superseded by its canonical statement. A lower bound for the explicit series remains unproved; no lower-bound conclusion was promoted.
