# Step 529 — separate source approval for the L127 audit

2026-10-28. Literature only; no mathematical audit performed.
The exact target remains the TARGET of
`drafts/literature/2026-10-27-l127-critical-audit.md`.

## Source scope checked

Primary source: Michele Fornea, *Plectic Heegner classes*,
[arXiv:2603.28327v2, 13 April 2026](https://arxiv.org/html/2603.28327v2).
Targeted HTML retrieval inspected Definitions 2.6/2.8, Proposition 2.9
and its displayed proof cases, Corollary 2.10, (21)--(23), localization
before Proposition 2.18, Corollary 2.21 and its proof text, Corollary
3.9, Lemma 4.12 with proof, and the paragraph containing (63).
Proposition 2.9 treats tame operators, diamonds and p-operators separately.
Corollary 2.21 requires Assumption 1.4; its global extension is abelian
over the CM field and Galois over the base. The local version additionally
requires definiteness and Assumption 1.7. Lemma 4.12 requires flat base
change. Equation (63) has a diamond-invariant domain after localization.
These statements cover the audit inputs, not an assertion of
W-equivariance. The prior step-527 extraction of the normalized-pushdown
diagram is reused; HTML's empty diagram rows were not independently
decoded here.

## Reused coverage and remaining audit obligations

The step-527 source record retains Schmidt Theorem 3.2.2 and its
prime-power cases, Jacquet--Langlands's division-character case, and
the relevant Fornea construction. No new search for those unchanged
statements is justified. L123/L126's written hypotheses were compared
with L127's statement. Their separate audits at steps 515/526 remain
inputs; this step does not replay them.

L127's elementary local support comparison, compatible residual
projectors and passage to completion, auxiliary unlocalized measures,
full-list inversion, incoming complement term and tensor balancing are
precisely the items to audit. They are not missing inaccessible external
theorems. SPECIALIZE authorizes checking these claims, including finding
an error; it does not import their conclusions or certify their proof.
No full matching theorem was identified in the reused assessment.
No claim of novelty or absence from all literature follows.

ATTEMPTS/061 parks only automatic full-Hecke-linearity. L125 and
ATTEMPTS/060 concern the different full-fiber substitution and are
contrasts, not premises. A conductor-line scalar remains compatible
with the abstract obstruction. Audit success means exact domains and
identities with the stated qualifications; failure means explicitly
correcting or withholding the affected claim before using it to reroute.
Neither outcome alone resolves the scalar or rational Kummer gaps.

The coverage decision remains SPECIALIZE with unchanged TARGET/SCOPE.
This is a completed separate approval, not a fresh mechanism or a
mathematical advance. Mathlib coverage remains not checked.
