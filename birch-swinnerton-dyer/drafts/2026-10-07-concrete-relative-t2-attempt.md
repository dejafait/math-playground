# Concrete relative T_2 attempt — work in progress

Approved target: Construct and verify a full-relative Manin, geometric-reflection and T_2 dual-kernel certificate for E: y^2+y=x^3+x^2-2x, testing L029's dimension-one threshold with independently certified conductor and eigenvalue data.

Prior assessment: drafts/literature/2026-10-07-concrete-relative-t2-certificate.md (SPECIALIZE, supplied before invocation). Actual task: implementation; classification: REPRODUCTION.

Main gap: rank E(Q)=m(E) for m(E)>=2. This finite instance test addresses L029's line premise; L028 could use it after independent twist calibration. It cannot supply q, period normalization, C, b, rational membership or the complex-order comparison.

Plan saved before implementation: independently certify the equation's invariants, minimality, conductor, non-CM status and F_2 point count; enumerate all projective cosets and lifts; diagonalize all integral Manin relations with reversible unimodular row/column operations, retaining the saturated lattice and integral quotient coordinates. Reduce each transformed endpoint path by exact continued fractions. Verify all relations and quotient matrices, then give complete rational elimination evidence for the stacked full-relative dual matrix.

Continue only at kernel dimension one with complete evidence. A larger kernel stops this single-operator test; no additional prime is approved. Any missing saturation, endpoint/operator or rank evidence prevents L029's application. ATTEMPTS/022--023's repeated conditional audits remain stopped. No BSD candidate is asserted. All existing unfinished files are preserved.

Completed: [L030](../lemmas/L030-conductor-389-full-relative-integration-line.md) records the proof and precise citations. The complete instance certificate and separate verifier give N=389, a_2=-2, 390 cosets, 780 relation rows, relation rank 325, saturation index two, integral quotient dimension 65, and full dual rank 64 with kernel dimension one (required one). All 8,142 segment witnesses are verified. No extra Hecke operator was used. This supplies the real line as a known-source specialization; q, Neron normalization and BSD comparisons remain unresolved. The final replay report is scripts/relative-t2/verification.json.
