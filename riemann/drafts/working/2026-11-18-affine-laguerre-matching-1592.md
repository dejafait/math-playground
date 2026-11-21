# Affine Laguerre matching checkpoint1592

Approved target: assessment1591's three-coefficient feasibility and retained
Schmeisser-cost diagnostic for unchanged P_d. Reuse its source coverage;
no additional literature or higher actual coefficients are needed.

Let v=S_2>0, tau=S_3>0 and N=d+alpha. The imported finite Laguerre
formula gives the binomial-normalized descending coefficients of q_d
as the first d exponential-series coefficients of
exp(-m*t)(1-sigma*t)^N. Thus their first three cumulants are
-(m+sigma*N), -sigma^2*N, -2*sigma^3*N. C028a gives the corresponding
actual quantities b_1, -v, 2*tau. Matching forces

    sigma=-tau/v, N=v^3/tau^2, m=-b_1+v^2/tau.

Admissibility is N>d-1, so matching cannot persist as d tends to
infinity. No fourth/fifth calculation or numerical constant is necessary.
This is a proposed family obstruction, not an actual-height lower bound.
Canonical proof and qualifications are being recorded in C028j; it still
needs a separate subsequent audit. No assumptions on S_4,S_5 or RH.
