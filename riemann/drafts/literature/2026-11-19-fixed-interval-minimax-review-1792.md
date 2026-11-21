# Fixed-interval residual minimax nomination1792

TARGET: Specialize Sion minimax to C033l's cap-2 residual approximation on [1,2], proving its exact signed-test dual with attainment and the finite-observation error bound 0<=d_2-d_S<=6h, without using C033v.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact minimax and signed-mass/TV queries, local duplicate comparison C033l/n/o and assessment1570/369, and three-mechanism selection are in drafts/literature/2026-11-19-fixed-interval-minimax-source-notes-1792.md; no numerical error value or novelty inference was found.
SOURCE_EVIDENCE: Sion, Pacific J.Math.8(1958),171-176, Theorem3.4 and full proof/Remark3.6 p174, https://msp.org/pjm/1958/8-1/pjm-v8-n1-p14-p.pdf, inspected with definitions2.4-2.7; reuse Buhler--Salamon2016 Example1.3.7/Theorem3.2.4 and Mimica2015 Remark1.2(i)/Proposition1.4(i), with precise pages/links and inspected coverage in source-notes1792/1748 and C033n.
COMPARISON: Known compact convex minimax and signed-measure compactness supply the tools; audited C033o supplies the cap-2 support value. Remaining work is the original-interval real-payoff application, attainment and uniform observation-mesh comparison, not a new duality theorem or another support calculation.
GAP: Check both weak-star compact strategies, separate continuity, signed Fubini, payoff/support signs and attainment, then obtain the explicit <=6h mesh allowance for every full-class signed input; no d_2 value, positivity or arbitrary-V rate established.
REASON: Supervisor recovery requires a different target; this real-interval variational mechanism is independent of C033v, Gaver inversion and stopped evaluators. Known tools support an independently testable reproduction; separate approval precedes mathematics.
SCOPE: Only W=I=[1,2], C033l's exact qualified residual/probability kernel, every real signed width eta of mass1/TV<=2 and signed observation measure of TV<=1; arbitrary atoms/singular support allowed. No width grid, positive-input substitution, deconvolution, C033v audit, numerical solve, d_2>0, variable-cap extension or Xi transfer.

Use the definitions and proposed formula in
[source-notes1792](2026-11-19-fixed-interval-minimax-source-notes-1792.md).
For finite nonempty S subset [1,2] with covering radius at most h,
d_S replaces the full observation supremum by maximum over S, keeping
the same continuum class A_2. Its finite dual uses real coefficients
with sum of absolute values at most1. Only this finite problem is
proposed to have a finite atomic optimal dual; no such claim is made
for the full interval.

Pass only with exact duality, both attainments and the mesh threshold,
including endpoint/zero/constant cases. Otherwise state and limit the
defect; no return to the parked propagation route is authorized. Cite
C033o's support value and Sion's compact minimax rather than reprove
them. Verify changed uses of C033l compactness/C033n regularity.

This could compare finite certificates to an optimal uniform error on
the prescribed interval. It supplies no evaluated certificate or
positive margin and leaves positivity/height/realization open. Essential
IDs and external qualifications are in source-notes1792. Matching
Mathlib coverage is unchecked/unknown. No derivation or lemma/program
edit occurred in this literature review.
