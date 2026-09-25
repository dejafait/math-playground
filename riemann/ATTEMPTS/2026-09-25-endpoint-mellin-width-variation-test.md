# Endpoint Mellin-width moving-vector test — 2026-09-25

Gap and intermediate target: the endpoint arithmetic margin at the
prescribed pairs remains unproved. Test the checkpoint's
W_N V_N²=O(1) for L349's nonconstant coefficients with the maximum
weights of L347. This would make a normalized weighted sampling
norm o(1) sufficient for a vanishing discrete mean. Exceptional
indices and all remaining low Laguerre signs would still be open.
Continue if this moving-vector budget is bounded; abandon this
particular norm separation if the budget necessarily diverges.

Redundancy review: read the shared and local goals, the whole proof
overview and DAG, and inspect existing tracked and untracked work.
L347's divergence concerns the different normalization at 1+1/r.
L349 removes that mass obstruction at 1+1/sqrt(r) but does not
bound variation. L344–L348's direct, dual and norm failures are
retained evidence, not proofs against the new coefficient family.
No earlier result located by the variation and second-difference
search supplies this target. Existing unfinished work is preserved.

Unfinished reasoning saved before the analytic calculation: use
t=sqrt(r)v in L349's Mellin integral, so both Euler ratios depend
on δ=r^(-1/2) and on (1+it)δ. Differentiating their logarithmic
coefficient series appears to cost O((1+|t|)/r), and twice
O((1+t²)/r²), multiplied by the same Euler norm. The scaled
kernel should absorb these polynomial factors on its central
Gaussian region; its far tail needs the crude Euler-product norm.
The intended estimates are ||b'_r||_1=O(1/r) and
||b''_r||_1=O(1/r²), with all equal-ratio grouping retained.

For scalar samples z_j and w=max_j|z_j|, discrete integration by
parts bounds Σ|z_(j+1)−z_j|²/w by the absolute first differences
at the two ends plus the sum of absolute second differences.
After summing frequencies, the intended derivative estimates
would make this O(1/N); Cauchy–Schwarz over N increments would
then give V_N=O(1). The maximum-weight mass follows from the
first derivative alone. This argument still needs proof,
including zero weights, signs and the differentiations under the
infinite coefficient integral. No bound or sampled sign is claimed
at this saved stage. Zero unresolved exploration turns precede it.

Calculation saved before final proof review: put u=2(1+it)/sqrt(r)
and H(u)=u−log(1+u). The scaled kernel is
k_r(t)=c_r exp(rH(u))/(1+u), with
c_r=Γ(r+1)exp(r)r^(-r-1/2)/π. Its logarithmic derivative is
c'_r/c_r+u/(2r(1+u))+J(u), where
J(u)=H(u)−u²/(2(1+u)) and J'(u)=u²/(2(1+u)²).
The existing analytic Stirling remainder controls c_r and two
derivatives. On the central contour this gives derivative bounds
C r^(-j)(1+t^(2j))exp(−t²/4), j=0,1,2. On the far
contour retain four powers of 1+(v/c)², use the polynomial
Euler norm, and obtain O(r^(5/2)2^(-r/4)) after integration.
The Euler logarithm derivatives use only B(1+δ)=δ^(-1)+O(1)
and −B'(1+δ)=δ^(-2)+O(1). These estimates appear to establish
both coefficient derivative bounds. Discrete integration by
parts then gives the intended O(1) budget. Full proof, dependency
review and the final continuation decision are still pending here.

Completed assessment — 2026-09-25: ADVANCE.
[L350](../lemmas/L350-endpoint-mellin-width-moving-vector-bound.md)
proves the two ℓ¹ derivative estimates and W_N V_N²=O(1).
The maximum is only over sampled coefficients; the discrete energy
identity handles coefficients that vanish or change sign without
an unproved lower bound on any individual weight. The budget has
liminf at least 9, so boundedness is the attained threshold, not
vanishing or absolute closeness to one.

Continue to a test of the sampling matrix. Writing
ρ_N=||G_N||op/(N W_N), L350 gives
D_N^w≤(C sqrt(ρ_N)+C/N)². The elementary bounds are only
1/N≤ρ_N≤1. Its normalized Hilbert–Schmidt square H_N satisfies
ρ_N²≤H_N≤ρ_N by positivity and unit normalized trace, making
H_N a concrete scalar diagnostic for the still-missing threshold.
Even success there would leave exceptional prescribed indices;
the required pointwise positive margin, all lower-index signs and
every established sign/exclusion range are unchanged. No RH
candidate; zero consecutive unresolved exploration turns.

Analytic review checked the exact scaled kernel and its logarithmic
derivatives, local analytic Stirling remainders, both Euler
logarithm derivatives, the far-tail integrable powers, dominated
ℓ¹ differentiation, the grouping contraction, both boundary terms
in the discrete identity and zero maximum weights. The new check
`python3 scripts/laguerre/check_endpoint_mellin_width_variation.py`
passes 9,837 exact finite energy identities and inequalities,
including seven zero-weight cases. It certifies finite algebra
only. The DAG adds only L347 and L349 as direct mathematical
inputs. Full Mathlib coverage is not checked; inherited supporting
names and links retain their qualifications. Earlier work is preserved.
