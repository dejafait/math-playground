# L463 shifted-saddle source estimate: bounded audit nomination

TARGET: Critically audit bramble_trace v4 Section 4.5 equations (18i)--(18n) underlying L463, at fixed sigma_0=7/8 and 3/8<c_0<1, checking logarithm bounds, order-uniform shifted-saddle errors, complementary arcs and overlap with C465a while retaining central multiplicities.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the inspected primary cases in 2026-10-25-initial-laguerre-sign-coverage.md and 2026-10-25-l463-import-audit-coverage.md. Narrow searches of L463/shifted-saddle assessment and history paths found the completed application audit, not an independent audit of these analytic estimates. No novelty search is needed for a source-proof audit.
SOURCE_EVIDENCE: bramble_trace, Generalized Laguerre positivity at growing orders, rStation paper 41, displayed v4, 24 October 2026 07:18 UTC, Theorem 1b (4b), Section 4.5 (18i)--(18n); source cases previously read in the October 25 assessments, with the same version and formula/range rechecked on 31 October. The earlier audit explicitly excluded source saddle estimates. C465a's common-onset tail is canonical; the external zero-free theorem remains a retained premise, not an audited input here.
COMPARISON: This is verification of an existing source claim for actual Xi, not a new sign mechanism or lower-threshold result. Formula (18n) retains the exact shifted saddle and covers c_0<=2p/ell<=1. Its upper-order overlap is separately available from C465a. The frozen-saddle formula (4) must not be substituted in the enlarged range.
GAP: Independent correctness of the logarithm-to-relative-coefficient argument is unresolved, especially angular control when its amplitude derivatives are only O(ell^a), a<1. No lower-order signs, endpoint c_0=3/8, effective onset or stronger zero-free premise is covered.
REASON: After the downward-propagation source shortcut lacks an independent sign input, audit this distinct essential analytic input before relying more strongly on its conditional threshold. Existing primary inspection covers the exact source and hypotheses; the new audit scope awaits separate supervisor approval, with no proof replay in this literature turn.
SCOPE: Proof audit of precisely (18i)--(18n) and the stated overlap, fixed 3/8<c_0<1, n=2p even, ell=log(t/(2pi)), actual Xi, arbitrary central multiplicities. Essential local inputs L018 and C465a; L463 identifies the claimed import and exact retained external premise. No external-manuscript audit, local-rectangle extension, source theorem reproof as novelty, or new positivity criterion.
LITERATURE_REASON: The target changes from identity applicability to the source estimate excluded by the completed L463 application audit. Reuse the prior primary reading; only version/range availability was refreshed when preparing this continuation.

Primary source: [paper 41, v4](https://rstation.ai/problems/riemann_hypothesis/papers/41).
Reuse the complete saved source comparison in
[the October 25 assessment](2026-10-25-initial-laguerre-sign-coverage.md).
The [application-audit assessment](2026-10-25-l463-import-audit-coverage.md)
expressly did not approve the analytic estimates themselves. Read the
complete essential Section 4.5 proof before replay; the short previews
and platform referee acceptance are not verification certificates.

Main gap: actual-Xi low-index signs and all-degree positivity. This audit
could validate or repair one conditional upper-tail input and determine
whether its claimed threshold is dependable. It cannot fill the initial
segment. The independent source audit is useful even while those sign
gaps and the external premise's correctness remain unresolved.

Bounded test: check each analytic inference from the pole-regularized
logarithm and derivative bounds through the exact real saddle, angular
Taylor and intermediate arcs, and the complementary-arc exponent gap.
Track constants with c_0 fixed before height and order vary. The two
saddle contributions, positive amplitude, even index, normalization,
central-zero applicability and common-onset overlap must all be checked.
Retain the shifted saddle: sublinear logarithmic errors do not by
themselves permit freezing an exponential amplitude.

Continue only if those precise estimates and quantifiers survive.
A missing estimate is a specific failed implication or unresolved gap:
record it and withhold the source-proof verdict rather than invent a
bound or strengthen a theorem. Do not rederive already audited C465a,
re-audit L463's elementary evenness application, or claim the full
external zero-free theorem was checked. If a genuinely new repair or
lemma is needed outside this scope, save it as uncovered and obtain
separate literature review before dependent proof work.

This is a REPRODUCTION / proof_audit / conceptual_audit nomination,
not creative mathematics. The angular relative-error estimates require
delicate analytic scrutiny, justifying deep_research/xhigh. No creative
sign attempt is yet justified: an independent actual-Xi sign/source
mechanism remains missing. Full Mathlib coverage is unchecked.
