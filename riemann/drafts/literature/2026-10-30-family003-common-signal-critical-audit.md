# Conditional common-signal continuation audit — ready coverage

TARGET: Independently audit the conditional common-signal continuation proposition in Section 2 of OpenAI family 003 at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a, checking endpoint integrability, Fourier identification, poles and family-uniform quantifiers without assuming the claimed zero-free conclusion.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the nomination and targeted duplicate/failure searches in drafts/literature/2026-10-30-family003-zeta-audit-scope.md; recovery directly reopened the pinned primary TeX and pinned Mathlib source, without broad discovery or an independent mathematical audit.
SOURCE_EVIDENCE: https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex Section 2, lem:continuation-criterion, complete statement/proof and following substitutions (rendered lines 339–477); https://raw.githubusercontent.com/leanprover-community/mathlib4/d0207795ac79006da92d98544e1ce915ae386160/Mathlib/Analysis/Fourier/Inversion.lean lines 150–182, exact inversion theorem hypotheses. Final theorem use remains covered by the nomination.
COMPARISON: The manuscript already proves this exact conditional result; the proposed work verifies its analytic applicability and quantifiers and is REPRODUCTION, not new mathematics. Import Fourier inversion rather than reprove it, checking the exact forward-transform integrability hypothesis or another applicable orientation. Supporting inversion coverage does not establish the proposition or its low/high arithmetic assumptions.
GAP: Independently check every operation in the conditional proof, including both endpoints, local uniform convergence, the Fourier convention, continuation through possible zeros, principal poles and the uniform positive distance needed when the supremum is not attained. No arithmetic margin, H construction or Dirichlet transfer is being audited in this target.
REASON: The external half-plane input remains qualified in L452/L461. A bounded check of an essential analytic reduction can improve confidence or isolate a real defect without rediscovering the stated zero-free bound; passing it alone cannot remove the overall external-premise qualification.
SCOPE: Only Section 2's conditional proposition over the stated primitive finite-order Hecke family; its low/high bounds, H contract and family-independent positive margins are explicit assumptions. Preserve poles, Euler deletions and strict half-planes. No new bound, full manuscript audit, Lean build, alternate proof, Liu improvement or RH claim.

This assessment was written during the completed literature nomination and
was repaired in a separate literature-only recovery turn; supervisor approval is still required before research. It
does not record an audit verdict or authorize derivation during its writing.

Use the complete statement and proof-case record in the
[completed source review](2026-10-30-family003-zeta-audit-scope.md), particularly
its exact beta_* definition, target-dependent data and target-independent
omega/sigma. Its links identify the pinned primary source and exact supporting
Mathlib statements. No local lemma is required as a mathematical premise;
L452/L461 identify the downstream use of the separately unaudited theorem.

The discriminating test is whether the conditional hypotheses suffice for a
holomorphic reciprocal on Re(s)>beta_*-epsilon_* with one epsilon_*>0
independent of the primitive character. Audit the claimed mechanism rather
than assume that continuation. A successful audit must explicitly handle
the principal meromorphic case and a supremum not attained by any zero.
If a precise gap appears, preserve it without calling the external theorem
false; if all checks pass, report a qualified conditional verification only.
No source-proof closure, initial Xi signs, effective overlap, or RH follows.
No independently justified new creative mechanism was prepared by this
source review. Matching Mathlib coverage of the complete proposition remains
unchecked; only Fourier-inversion support was inspected.

## Direct-source recovery, 2026-10-30

LITERATURE_REASON: Supervisor rejected ready coverage without a direct source URL; repair that exact source gate and verify the linked theorem hypotheses, without expanding the target.

The primary URLs in SOURCE_EVIDENCE were successfully opened. The manuscript
passages match the nominated conditional claim. This is source verification,
not verification of the argument or its arithmetic contracts. No new lemma,
calculation or independent audit was undertaken. Existing duplicate and failed
route checks are reused unchanged.

The pinned Mathlib source requires a correction to the nomination's prose:
`MeasureTheory.Integrable.fourier_fourierInv_eq` explicitly assumes
`Integrable f`, `Integrable (𝓕 f)`, and `ContinuousAt f v`; its conclusion
is `𝓕 (𝓕⁻ f) v = f v`. The companion theorem has the same hypotheses
and the opposite composition. It does not literally state the
inverse-transform integrability hypothesis previously attributed to it.
The audit must select an applicable orientation and justify its exact
hypotheses and frequency convention. This correction does not establish a
defect in the manuscript or settle that applicability. All type hypotheses
and the distinction between supporting coverage and a full matching theorem
remain as recorded above.

Decision remains SPECIALIZE for a source-proof REPRODUCTION audit. No
conditional verdict, arithmetic estimate, family-uniform margin or RH result
is imported by this repair. The existing endpoint/pole/supremum test remains
the sole continuation test; stop the claimed conditional verification upon
finding an essential unjustified operation and record its exact hypothesis.
