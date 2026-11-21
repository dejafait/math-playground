# Fixed modulated-kernel test — work in progress, step 263

Gate: the supplied EXPLORE assessment `drafts/literature/2026-11-04-critical-point-modulated-kernel-test.md` predates this invocation and covers exactly this fixed calculation. No parameter change or actual-Xi transfer is authorized.

Main gap: unconditional actual-Xi mixed positivity. Intermediate target: all admissibility/strict-log-concavity conditions and F>0, F''>0 on [6,7], F'(6)<0<F'(7) for the fixed kernel in that assessment. Success rules out the generic shape-to-critical-sign inference only; failure parks this exact parameter choice. Other centers, degeneracies, higher signs and theta-specific control remain open.

Duplicate/source comparison reused: L050 proves nonreal zeros without this stationary minimum; L607 proves an unconstrained negative first sign. Neither is a mathematical input here. Csordas Definition 1.2 supplies the admissibility convention; the DLMF Gaussian row supplies only the undamped transform.

Proposed calculation, NOT YET VERIFIED: write delta=10^(-8), a=1/100, b=10. The logarithmic curvature is bounded above by -2+100/99-12 delta u^2. Compare F with the shifted Gaussian transform G. The derivative errors for j=0,1,2 should be bounded by (101/100) delta integral_R |u|^(j+4)e^(-u^2)du. These absolute errors must be compared with uniform signed Gaussian margins, not sampled values. Establish all constants and endpoint signs before claiming a counterexample.

Completed: the proposed bounds were established, with all four strict
margins, in canonical L738. The initial “not yet verified” calculation
above is retained as the pre-work checkpoint, not the current result.
All twelve scalar comparisons passed the exact-rational replay in
`scripts/critical-minimum/fixed-rational-margins-263.py`; the analytic
proof remains unaudited. See the step-263 history and PROGRESS for the
current route and separate review continuation.
