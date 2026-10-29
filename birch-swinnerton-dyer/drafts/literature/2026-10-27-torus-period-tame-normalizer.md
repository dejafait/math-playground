# Complete CM torus period and a degree-one tame normalizer — source review

TARGET: Determine whether L124's w can be replaced by a tame level normalizer W in the complete projected CM norm moment by an explicitly justified CM-torus translation.
CHECKED: 2026-10-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 523 searched toric periods, CM conjugation at arbitrary level and optimal-embedding normalizers; located and inspected Voight's general prime-power local results and compared Fornea's exact projected invariance construction. Queries, duplicates and prior failures are recorded in drafts/source-notes/2026-10-27-torus-period-tame-normalizer-comparison.md.
SOURCE_EVIDENCE: Voight, Quaternion Algebras (Springer 2021), Chapter 30 https://doi.org/10.1007/978-3-030-56694-4_30, Proposition 30.5.3, (30.6.2), Lemmas 30.6.3/30.6.9 with full proofs; Fornea arXiv:2603.28327v2 https://arxiv.org/html/2603.28327v2, (2), Section 2.2 level definitions/(22), Lemma 4.7, Theorem 4.13, Corollary 4.15, (63), Proposition 4.18/Corollary 4.19 and Section 4.3-4.4 with full relevant proofs; prior L123/L124 audited construction and step-518 classical comparison reused.
COMPARISON: Voight covers local Eichler prime powers, including exponent two, without relying on the square-free Gonzalez-Rotger lemma. Fornea supplies simultaneous rational action and complete specialized torus-cap-product machinery, not raw measure invariance. Their assembly for L124's full norm kernel, both local orientations and the original indexed CM list is a remaining specialization, not an imported identity.
GAP: Match conductor-one optimal embeddings to each local theorem, assemble w=psi(a)W with a_p=W_p=1 and W normalizing the entire tame level, and justify equality of the complete projected norm moments with rational representatives, p-cells, invariant domains and descent retained.
REASON: New applicable prime-power embedding coverage and the inspected projected-invariance proof justify a bounded known-source specialization attempt; no essential source is blocked. The full-fiber substitution remains parked, and neither factorization nor moment equality is derived or accepted in this literature-only step.
SCOPE: L123/L124 hypotheses and complete projected trivial-character norm moment only; no scalar eigenvalue for W, nonvanishing, rational Kummer membership, local finite condition or BSD conclusion is preapproved.

Step 522 proposed this continuation with REVIEW_REQUIRED. Step 523 is
the separate literature review of that saved target. Its exact text is
unchanged. The next mathematical attempt may specialize the inspected
inputs, but its conclusion remains unproved. Preserve the exact original
indexed CM list until a proved complete-moment argument permits changing
its representatives. The full source comparison and proof obligations
are in [the source record](../source-notes/2026-10-27-torus-period-tame-normalizer-comparison.md).

The proposed test has two linked obligations: the tame local factorization
must cover good split, nonsplit and ramified places and split conductor
exponents up to two; its torus factor must disappear in the actual
projected class without a pointwise projection or a raw invariance
assumption. The source construction's rational G-action, possible
p-component of a rational representative, and the full kernel weight
must be tracked. The action of W on that class is a further independent
question, not part of the requested equality.

Essential existing inputs are L123 with its step-515 audit and L124
with its step-520 audit. L125 motivates the new mechanism through a
local support obstruction; it has not received a separate critical audit
and must not be used as a nonscalarity theorem. Its proof and qualifications
are canonical in its lemma file. The old scalar assessment remains a
historical ready comparison for its exact scope, not permission to
continue the failed automatic full-fiber substitution.

The downstream use would be to reduce the scalar question to an actual
degree-one tame operator, removing the measured branch ambiguity. It
would not itself evaluate that operator or R. Continue on a complete
projected replacement with all local hypotheses justified, or on a
precise failed local/domain hypothesis. Abandon this replacement if that
failure cannot be repaired within the saved assumptions. No torus-period
identity or local factorization is proved in this file; approval covers
the attempt only. Mathlib coverage has not been checked.
