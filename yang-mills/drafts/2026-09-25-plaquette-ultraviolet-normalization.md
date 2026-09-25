# Plaquette ultraviolet-normalization test, 2026-09-25

## Preflight and bounded target

Read the shared GOAL.md and PROMPT.md, local target and checkpoint, the entire PROOF.md and DAG.md, existing changes, L002 and L003, the source conventions, and both recorded failed approaches. Existing work is preserved. Reopened the official Jaffe–Witten description, section 4 and its renormalization footnote; its nontrivial continuum theory and finite positive mass requirements are unchanged.

Gap: L003 gives a positive Gaussian coefficient but no ultraviolet-uniform interacting correction for its bare single-orientation plaquette. The required comparison is an error at most c_box/2 along a specified renormalized trajectory. The proposed intermediate target is the leading logarithmic renormalization of this observable, taking its tensor content and its explicit factor 1/g_0^2 into account.

Plausible downstream use: identify a correctly normalized observable sector before seeking the uniform reflection lower bound. The interacting cutoff removal, control beyond perturbation theory, full limiting reflection positivity, infrared limit, all gauge groups, and finite positive mass remain unresolved.

Discriminating test: check the scalar and stress-tensor projections of an oriented curvature square against precise perturbative renormalization identities. A nonzero logarithmic mismatch would reject treating the plaquette as an automatically finite scalar insertion; cancellation must be checked in the actual bare normalization. Continue only with a definite normalization or mixing prescription; if the full oriented coefficient is not determined, record that limitation instead of treating a scalar projection as the answer for Q_(a,g).

This addresses the ultraviolet correction selected in the checkpoint. It is distinct from the independent-link white-noise failure and the unsupported direct MRS positivity import, and is not implied by either free-field lemma. No repeated unproductive turns have accumulated on this test.

## Saved reasoning before source and normalization checks

The six curvature squares indexed by unoriented coordinate planes contain a scalar sum, diagonal stress-tensor combinations, and further tensor components. A fixed 12 square is not the rotational scalar sum. Conservation protects the stress tensor, but this alone says nothing about all components of the rank-four curvature product. A scalar trace-anomaly formula must also be converted from the connection convention (action F^2/(4g_0^2)) to the notebook's canonical Gaussian normalization. In particular, pole terms from composite and coupling renormalization may cancel; no anomalous-dimension sign or one-loop obstruction is assumed before checking that cancellation.

The primary source being checked is Hiroshi Suzuki, *Energy–momentum tensor from the Yang–Mills gradient flow*, arXiv:1304.0533, especially its operator-renormalization identities. Its perturbative identities cannot supply a nonperturbative uniform remainder for the fixed-boundary Wilson measure without an additional argument.

## Completed assessment

The source and normalization check gave a definite obstruction, recorded with full hypotheses and proof in [L004](../lemmas/L004-oriented-curvature-square-renormalization-mismatch.md). The [source record](../foundations/04-perturbative-curvature-renormalization.md) pins Suzuki v6, section 2 and equation numbers. Although the connection-curvature scalar has no one-loop pole in its own Z_S, the notebook's factor 1/g_0^2 changes the relevant ratio to Z_S/Z, with residue b_0. The corresponding traceless stress-tensor ratio Z_T/Z is one. Thus a common multiplicative factor for the oriented plane family is inconsistent with the two projections.

The exact six-plane decomposition retains a scalar direction, three diagonal stress directions, and two remaining diagonal tensor directions. In particular, h_12 - h_34 lies entirely in the stress directions. No claim that scalar and stress projections exhaust h_12 was made. The [exact arithmetic check](../scripts/curvature-normalization/check.py) verifies mutually orthogonal projectors of ranks 1, 3, and 2, the complementary-plane identity, and the first-order pole ratios.

The full leading logarithmic term of the original fixed-box reflection coefficient was not obtained. The uncontracted tensor mixing, reflected cross terms, finite lattice and boundary matching, and higher-order remainder still matter. A pole in one operator projection does not prove divergence or even the sign of the particular smeared reflection correction. The achieved result is an informative negative test of a single-factor/scalar-only prescription; it supplies no numerical error bound to compare with c_box/2.

Decision: stop that prescription, preserve the original Gaussian calculation, and use the stress-tensor projection as the reason for changing the observable under study. Its Gaussian lower bound must be tested in the actual box before any interacting comparison can use it. The historical endpoint and direct-import failures remain distinct and unchanged. There were zero inconclusive exploration turns in this test, and no complete candidate argument emerged.
