# Exact compensation in the finite-window majorant — proposed test

TARGET: Test the signed van der Corput majorant for B_n at H=floor(sqrt(X)) on dyadic blocks, using exact unit-cell compensation and comparing all endpoint, block and centered-energy costs with the subexponential threshold.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step306's completed deterministic reconstruction search and theorem comparison in 2026-11-10-bulk-laguerre-short-shift-reconstruction-review-305.md, together with completed reviews241/304 and stops233/235/243/302/305. No inspected theorem bounds this compensated energy; no novelty claim.
SOURCE_EVIDENCE: Montgomery2001, Harmonic Analysis as found in Analytic Number Theory, unnumbered finite-sequence van der Corput proof, pp276–277/PDF6–7, https://www.nato-us.org/analysis2000/papers/montgomery.pdf ; primary statement and entire relevant proof read in step306. Reuse review304 for MRT1707.01315v3 Theorem1.3(i), Proposition3.1/Corollary3.2 and essential proof cases, https://arxiv.org/pdf/1707.01315v3 . Finite Cauchy–Schwarz is the named standard block-combination tool.
COMPARISON: The arbitrary-complex-sequence majorant covers the deterministic tool. The difference is exact prime-continuum cell encoding and cost comparison for the growing Laguerre weight; no theorem supplies its needed centered-energy saving. The Gallagher L2 theorem is comparison only and licenses no pointwise or signed-measure transfer.
GAP: Determine whether the fully retained signed majorant and already assessed arithmetic contract can reach B_n^2<=D_epsilon*exp(epsilon*n) for every epsilon>0, or isolate the exact unsupported input or positive-rate upper-bound loss. Neither actual B_n growth nor impossibility of signed-energy methods is asserted.
REASON: This is one bounded standard-tool specialization after completed source coverage. It tests a sufficient inequality rather than requiring equality of all long pairs. The new assessment awaits separate next-turn approval; no cell identity or cost calculation is derived during its nomination.
SCOPE: Exact B_n and K_n from review241, integers n>=2, all prime powers and the full endpoint exp(2n), dyadic pieces intersecting (exp(n),exp(2n)], H=floor(sqrt(X)) at each block scale X, finite complex sequences, signed local correlations and finite block Cauchy–Schwarz. No new arithmetic correlation theorem, growing-order asymptotics, Fourier point-evaluation transfer or replacement of compensation by integer Lambda-1.

## Proposed bounded mathematical attempt

Use review241's unchanged definitions

    K_n(u)=(n-1)^(-1)*sum_(k=2)^n L_(k-1)^(1)(u),
    B_n=sum_(exp(n)<m<=exp(2n)) Lambda(m)*K_n(log m)/m
                                  -integral_n^(2n) K_n(u)du.

The main gap is L030–L032/C032a and L966/L968, with L984(H) unpaid.
A bound for B_n would pay only the bulk; both complementary logarithmic
ranges, their compensation and regulator/infinite-zero obligations remain.

1. Encode each sharp dyadic piece by a finite sequence whose entries
   retain its prime-power contribution and exact integrals over unit
   cells. Prove its total is that piece's compensated sum, explicitly
   accounting for fractional endpoint cells, the possible last cell
   with integral but no integer atom, and any cut cell. Do not substitute
   a sampled integral or presume that an endpoint is an integer.
2. Import Montgomery's cited signed intermediate inequality without
   reproving the known theorem. Keep the true enclosing support length,
   H versus H+1, diagonal, signed correlations and zero-extension cases.
   Combine pieces by a stated finite inequality with every cost retained.
   Do not represent the upper bound as an equality reconstruction.
3. State the precise centered local-energy estimate required to pay
   the every-epsilon B_n^2 threshold after all costs. Compare only with
   already inspected review304 contracts; keep mixed cell-integral and
   integral-integral terms, degree-uniform weights and exceptional shifts.
   A source hypothesis failure can stop the comparison; invent no new
   prime estimate to fill it. Do not run another absolute Laguerre-norm,
   derivative-order or source-search campaign inside this test.

Continue only if this gives a precise usable inequality and an identified
independent signed-energy input reaching the full threshold, or a materially
new refinement addressing a quantified loss. Park this standard-majorant
payment if the remaining premise is unsupported, the original global
square merely reappears as an unpaid residual, or the available bound
retains a fixed positive exponential rate. An insufficient upper bound
is not a lower bound for B_n or a disproof of RH. Save an unfinished exact
specialization with its unresolved assumptions if the bounded comparison
cannot be completed; do not report a new theorem.

Essential local inputs: L984(H); review241's exact observable; L981/L982
endpoint and fixed-index conventions; review304's arithmetic scope;
completed review305/step306's precise Montgomery contract. C999a supplies
no arithmetic premise. Preserve stops233/235/243/302/305. No cross-notebook
input. Full matching Mathlib coverage is unchecked and unknown. This is
REPRODUCTION if executed, with no claim beyond the inspected sources.
