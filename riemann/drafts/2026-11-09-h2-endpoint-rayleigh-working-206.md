# Fixed endpoint Rayleigh calculation — step206

Prior gate: `drafts/literature/2026-11-09-h2-endpoint-head-margin-feasibility-review.md`, SPECIALIZE, supplied before invocation. Execute its exact TARGET, with no change of endpoint, cutoff, direction or saved enclosure. The supervisor's mismatch warning is addressed by retaining that exact target as the completed action; no mathematical scope is added.

Main gap: L030–L032/C032a all-degree mixed positivity. Intermediate target: one upper bound for c^T A(0)c/(c^T c), testing only L919's strict sufficient margin. A bound <=5691/10^9 obstructs that margin; any larger or straddling bound ends this test without refinement or inference of feasibility.

Inputs read: L019/L036/L037/L058, L874 definitions, full relevant L917 enclosure/audit and L919 product/tail/audit. The complete saved panel0 and arithmetic contracts were inspected. Local duplicate/failure search found the unperformed nomination, L917's determinant-box stop, and step204's closed approval loop. No new source coverage is needed. No cross-notebook input.

Algebra to implement: Dc=(1,-400,40000), c^T c=6. The full numerator is S2-800 S3+240000 S4-32000000 S5+1600000000 S6. Each zero contributes zeta^-4(1-400 zeta^-2+40000 zeta^-4)^2, with algebraic squares. Its absolute value is bounded by the five absolute expanded coefficients times |zeta|^-4,...,|zeta|^-12. L919(10), with log100<5, therefore bounds the entire omitted directional sum. Subtracting an unknown signed tail requires adding its absolute bound to the full upper endpoint. No tail positivity is assumed.

Completed: the exact Fraction calculation, complete five-power directional bound, nine-entry replay and threshold comparison are canonical in L920 and `scripts/heat/h2-endpoint-rayleigh-206.json`. The head interval [-0.000045239559,0.000046415197] straddles B; the bounded attempt ends inconclusively without refinement. All 23 finite checks pass. Decimal-library correctness remains inherited; a separate independent audit has not been performed. No H2 sign, margin feasibility or margin obstruction follows.
