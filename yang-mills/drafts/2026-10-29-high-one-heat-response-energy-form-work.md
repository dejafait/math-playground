# Approved high one-heat response test — work in progress

Target: Test whether L301's full-H form estimate makes L297's complete high one-heat-line response o(1) at r_N.
Prior gate: drafts/literature/2026-10-29-high-one-heat-response-energy-form-test.md (SPECIALIZE, supplied at startup).

Main gap: uniform interacting comparison, continuum axioms and positive mass remain open; this test addresses only the terminal complementary response.
Inputs: L301(4), L297(8),(19)--(22) and its admitted fixed high contour, L296(9),(13)--(14) and relative mode count; all upstream premises remain conditional. Keep the exact SU(2) reflected 12-bumps, even N, a=8/N, counting measure, full density, fixed H/Q and all normal endpoints.

Proposed bounded calculation (not yet verified): write L=Ahat-sB_--tB_+, D=L^-1, V=(I-sM_--tM_+)^-1, and represent the high f_theta(L) by D^2 [integral z^3 exp(-theta z)(z-L)^-1 dz/(2pi i)] D^2. This equals L^-1 exp(-theta L) on the high subspace. With fixed outside Ahat half-powers, X=Ahat^(1/2)D^2=V Ahat^-1 V Ahat^-1/2 and Y=D^2 Ahat^(1/2)=Ahat^-1/2 V Ahat^-1 V. The saved count Tr(Ahat^-3)<=C suggests uniform Schatten-2 bounds for X,Y and all required derivatives. Retain all derivatives of both V factors at each end and both resolvent source orders. No weight is commuted through V or M.

Test: prove the complete weighted high trace norm O(lambda_0^-1 exp(-7theta_N/6)), pair each of the four product-rule terms with L301(4), and compare with o(1). If any factor or contour closure lacks a uniform bound, preserve that term and stop without asserting a counterexample. Success concerns this terminal scale only; no uncut or continuum claim. The symmetric four-inverse regularization is the proposed refinement over the unweighted three-inverse representation, not a new imported theorem.

Duplicate/failure screen: L297(20) is unweighted, L301 estimates the low cluster only; the older first-pair weighted-high diagnostic is excluded by the ready assessment. ATTEMPTS/047--050 stop different mechanisms and do not decide this target. No discarded work is overwritten.

## Completed bounded attempt

The proposed factorization closes the weighted estimate. The complete proof is canonical in lemmas/L302-complete-high-heat-response-weighted-trace-bound.md; the tentative reasoning above is preserved as the work checkpoint. Both weighted end factors and every derivative are uniformly Hilbert--Schmidt by the exponents 3 and 6. The full high trace is bounded by lambda_0^-1 exp(-7theta_N/6), paired with L301(4), yielding O(N^-3/4 sqrt(log(eN))) for all four scalar terms. The complete terminal assembly is O(N^-1/20 log(eN)^3), under the imported low and multi-heat bounds. No calculation certificate or numerical evidence is used.

The new proof is not separately audited. A conceptual audit must check the exact high subcontour identity, noncommuting source derivatives of both end factors, uniform source/trace estimates, contour closure and domination, all four Wilson trace terms and the finite terminal assembly. Other scales, uncut estimates, higher remainder and the main construction remain open. This is a specialization/reproduction attempt, not a claimed new mechanism or complete-solution candidate.
