# Conditional neutral-cell recurrence diagnostic: next-turn nomination

TARGET: Test under RH whether a fixed nonzero moment-neutral smooth cell profile gives a positive Cesaro mean square of its complete translated causal pairing, and hence obstructs summable beta_m.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step 279's completed moment-neutral-separated-cell-coupling.md comparison: separated-support, semiboundedness, translated Weil Toeplitz and Wiener atom-detection searches. No exact neutral-cell specialization was located; no originality claim. This newly written continuation requires a separate approval next turn.
SOURCE_EVIDENCE: Suzuki 2206.03682v4 pinned PDF Thm1.1(2), Section2.2, Lemma2.1/proof, Sections3.1-3.5 and Prop3.1; Suzuki 2606.09096v3 Thm1.1/(2.5)-(2.10); Cuny-Eisner-Farkas BUW-IMACM18/22 (4 January 2019) Thm1.1 p1 and Prop2.6(a)-(b)/proof pp5-6. L740/L741 provide the local causal generator and positive denominator. Precise links and qualifications are in the completed source comparison.
COMPARISON: The standard smooth Weil zero representation and Wiener's finite-measure atom theorem supply the mechanism. Only the complete causal-energy identification, neutral-profile choice, smoothing convergence and lattice-phase aggregation require specialization; a new general Fourier theorem or sign certificate is unnecessary.
GAP: Prove the stated conditional fixed-profile representation and verify finite nonzero atomic mass without discarding prime powers or assuming distinct lattice phases. No unconditional nonsummability, all-window positivity or RH consequence is covered.
REASON: A discrete-spectrum obstruction must be resolved before a summable-decay upper estimate is credible. This is a bounded reproduction/specialization of known theory, not a creative solution mechanism or a new global sign result.
SCOPE: ell=log(3)/2, m>=2, L_m=(m+1)ell; use the original beta_m definition, complex C_c^infinity(0,ell) profiles with integral exp(plus/minus x/2)f(x)dx=0, and assume RH only for the diagnostic. Keep every prime-power shift and the full continuous/polar contribution in L740. Start and finish on smooth profiles; no larger-window domain theorem is required.

## Exact bounded attempt and test

For one fixed nonzero neutral f, put

    h_m = H_{L_m}(f,tau_m f),   d_f = E_ell(f)>0.

Try to prove, with RH stated explicitly,

    liminf_{M->infinity} (1/M) sum_{m=2}^M |h_m|^2 > 0.

This is a proposed threshold, not an established formula or lower
bound. It is enough to decide whether the proposed uniform absolute
summability is compatible with the intended RH case. It is not a
test for a negative Weil vector or for an off-line zero.

Use the exact generator from L740 and the normalization check in
L741 section 2. Verify the smooth energy/Weil identity on L_m;
L741's finite-window conclusion must not silently be extended as
a domain theorem. Reuse [Suzuki's pinned PDF](https://arxiv.org/pdf/2206.03682v4)
for the compact-smooth zero pairing and its proof, retaining
conjugation and multiplicities. The PDF version date differs from
the served HTML; that discrepancy is recorded in step 279.

Under the stated conditional assumption, try to realize the sequence
as Fourier coefficients of a finite nonzero positive atomic measure
on the unit circle. Establish total mass/convergence before regrouping
phase aliases, and justify that neutrality does not annihilate every
relevant transform value. Lemma 2.1 is an available named input for
the latter question; its underlying distinct-zero estimate was cited,
not independently reproved in the review. Import
[Cuny-Eisner-Farkas Thm1.1](https://imacm.uni-wuppertal.de/fileadmin/imacm/preprints/2018/imacm_18_22.pdf)
with its finite-measure hypotheses. Do not reprove Wiener or infer
the needed measure from a formal critical-axis xi'/xi symbol.

Continue only if the complete coefficients and a surviving atom are
proved. If a positive mean square follows, record the exact conditional
obstruction in a canonical lemma and park this summability route;
do not announce an unconditional counterexample. Otherwise save the
unresolved identity or mass issue and reassess. No script or new
mathematical derivation was performed while writing this nomination.

Downstream use: prevent a spatial positivity argument from requiring
an inappropriate absolute-decay threshold; any successful replacement
would have to retain coherent spectral interactions. Complementary
moment directions, adjacent interactions, unconditional remote control
and the final sign margin remain unresolved. No replacement mechanism
is approved. Matching Mathlib coverage is unchecked.
