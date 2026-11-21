# Complete normalized-primitive comparison on one two-sine slice

TARGET: Test Q(Pf)/||Pf||_2^2 <= Q(f) for every real unit f in span{sin(pi*x),sin(2*pi*x)} satisfying Q(f)<=1/250, using C759a's complete form and rigorous full-tail bounds; certify the whole eligible slice or exhibit an eligible positive defect.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the bounded primitive/parity exact-statement, stronger-result and local-failure search completed in review812/step813; the fixed slice is within that comparison. No inspected source supplies its signed answer and no novelty is claimed.
SOURCE_EVIDENCE: Primary URLs and inspected passages are in review812/step813: https://arxiv.org/html/2606.09096v2#S2.SS4 Theorem1.1/(1.8)/Section2.4, https://arxiv.org/html/2606.09096v3#S8.SS2 Sections8.2/8.4/8.5 and (8.2)/(8.7), https://dlmf.nist.gov/5.9#ii (5.9.12)-(5.9.13). Reuse C759a's domain/full Q, C759d's cap and C759e's audited kernel/evaluation method, not its fixed-function numerical tail.
COMPARISON: Known complete-form, primitive-norm and digamma identities support explicit finite-dimensional specialization. The difference to derive is the entire capped two-mode comparison with the primitive's actual norm and every signed term; no spectral, positivity or general parity theorem is imported.
GAP: All eligible directions in this slice, exact endpoint cases, domain/nonzero normalization and new complete tail must be checked. Even a pass leaves the whole remaining odd domain, simplicity/sign, other windows and Xi realization open.
REASON: One bounded materially different map test can refute the full proposal through a single eligible failure; it can also provide limited finite-slice evidence without claiming the uniform assertion. Separate next-turn approval is required for this newly written ready assessment.
SCOPE: Exactly window[-1,1], cap1/250, real L2-unit span of the first two odd sine modes, Pf(x)=integral_-1^x f(t)dt on the interval and zero outside; complete unneutralized C759a Q. Subsequent calculation classification REPRODUCTION.

This is a nomination for a subsequent mathematical step, not a calculation
or new lemma in step813. The main gap is actual-Xi all-degree mixed
positivity; the plausible use is a variational parity-ordering input.
The reviewed broader target remains unresolved.

Use only C759a's exact normalization and domain. Establish the chosen
inputs' and primitives' admissibility, parity, traces and nonzero norm;
handle the source's D=i d/dx convention explicitly. Directly integrate
these elementary functions rather than claim a new inverse theorem.
No numerical inverse-Neumann spectral computation is needed.

Compute the complete form entries on the input and primitive spans and
their actual L2 metric. Prove all expansions, correlations and endpoint
limits needed to evaluate them. Both imaginary Fourier factors and all
five overlapping prime powers2,3,4,5,7 remain present, with Lambda(4)=log2.
Retain the entire archimedean tail with an analytic remainder valid for
these new functions. L741 is used only for its audited full-line multiplier
identity, not a different window's positivity. C759d supplies an already
eligible input; C759e and C998z are contrasting modulus stops only.

The decision threshold is zero for the normalized output-minus-input
energy. A candidate violating vector must have certified unit norm,
input energy<=1/250, positive primitive norm and strictly positive defect.
For a pass certify every eligible real direction, including boundaries
of the cap, not just a sampled parameter grid or the first sine. Interval
uncertainty is inconclusive. Save complete evidence and any unresolved
analytic remainder rather than silently use a midpoint.

Stop this test after the fixed slice. A positive eligible defect abandons
the exact universal primitive comparison. An all-direction pass is only
a finite-slice partial result, not evidence deciding the complementary
odd sector or RH; do not automatically enlarge the mode set. A creative
infinite-domain continuation would need a specific signed-form mechanism
and fresh coverage. No such mechanism has been approved here.

No reproof of the general realization or norm theorem is requested.
The new specialization is necessary because the inspected sources do
not evaluate this capped complete-form comparison. Full matching Mathlib
coverage is unchecked; supporting elementary integral/Fourier theorems
would not establish its sign.
