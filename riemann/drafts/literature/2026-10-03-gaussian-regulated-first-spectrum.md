# Gaussian-regulated first Laguerre spectrum — pending assessment

TARGET: Test whether L357's Gaussian-regulated approximants satisfy F_ε′²−F_εF_ε″≥0 at every real frequency for all sufficiently small ε, using an exact Mellin representation and a large-frequency sign test.
CHECKED: 2026-10-03
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: No target-specific spectral search has been performed; the prior Gaussian zero-mode review screened weighted whole-line convergence and explicitly excluded spectral-sign conclusions.
SOURCE_EVIDENCE: The saved approximation assessment inspected DLMF 20.7.32, Sutherland Lecture 17 Lemma 17.10 and Paris arXiv:2101.01589v1 Theorem 1; these give scalar and polynomial-weighted Gaussian identities, not a first Laguerre sign for the regulated family. No new theorem-level source comparison has been completed for this target.
COMPARISON: L357 supplies the approximation and two real Fourier derivatives with O(ε) absolute error; L233 identifies the limiting sign requirement and a generic positive-kernel counterexample. Neither establishes the changed regulated family's spectrum or a nonnegative margin at every frequency.
GAP: Assess exact Mellin-transform and Fourier-sign coverage for these approximants before testing whether a certificate holds throughout a vanishing regulator interval, or fails at frequencies escaping as ε tends to zero.
REASON: This is a changed spectral target outside the ready approximation assessment's explicit scope; the next invocation must complete only its source review and preserve mathematical lemmas and scripts unchanged.
SCOPE: Exactly k_ε and its real-axis Fourier transform F_ε from L357, 0<ε≤1; a sufficient certificate would give one ε_0>0 with F_ε′²−F_εF_ε″≥0 on R for every 0<ε≤ε_0. No complex entire extension, real-root preservation, or higher-level condition is assumed.

The preceding assessment is
[the Gaussian zero-mode source review](2026-10-03-gaussian-regulated-modular-zero-mode.md).
Its exact scalar identity and derivative-tail coverage should be reused;
they do not need another proof or repeated search. Its explicit scope
excludes the new spectral-sign target, so it cannot clear this gate.

The completed approximation result is
[L357](../../lemmas/L357-gaussian-zero-mode-subtraction-repairs-weighted-convergence.md).
It meets the weighted convergence threshold and controls the first
Laguerre expression in uniform absolute error. The missing downstream
input is a sign certificate for the approximants; convergence itself
does not produce that premise. The historical finite-average and
separate-parity failures remain separate, preserved obstructions.

The next review should compare available theta/Mellin transform
statements, first-associated-kernel criteria, stronger zero-preserving
results and relevant negative-sign obstructions with this precise
shifted-parameter, differentiated, subtracted and reflected family.
Reuse the existing sources where they apply. No particular unread
lead has yet been established as essential; source discovery and
theorem-level applicability comparison for the sign test are pending.
No representation, asymptotic, sign calculation or new result for
this target has been derived in the approximation step.

A future mathematical test would continue only with a concrete
nonnegative margin or an exact mechanism covering all real frequencies.
An analytic negative value for arbitrarily small ε would stop the
vanishing-regulator certificate. Tail signing alone would still leave
the complementary frequency range unresolved. Even a successful
first-level transfer would leave the higher Laguerre and mixed-form
gap to RH. These are screening criteria, not asserted results.

## Mathlib

Full spectral target and target-specific Mellin/Fourier support:
**not checked**. The saved scalar supporting reference
[Real.tsum_exp_neg_mul_int_sq](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gaussian/PoissonSummation.html#Real.tsum_exp_neg_mul_int_sq)
is not a match for this sign requirement. No full matching theorem
or library absence is asserted.
