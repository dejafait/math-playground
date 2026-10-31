# Explicit local circle count: source comparison

TARGET: Establish a strict Rouche count of one real simple H_t zero in |z-X|<1/log(X/(4*pi)) at every real center g(X,t) in Z, for 1/25<=t<=11/50 and X>=4*pi*exp(10000)+2.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the inspected phase/count review and its exact searches; supplemented with H_t/Rouche/Polymath, explicit heat-flow real-simple-zero and 1904.12438/circle queries, including arXiv-restricted searches. No additional matching numerical theorem was inspected; queries, negative-search limits and duplicate/failure checks are in drafts/heat/2026-10-30-explicit-local-circle-source-review.md.
SOURCE_EVIDENCE: D. H. J. Polymath, arXiv:1904.12438v2 (4 August 2019), https://arxiv.org/html/1904.12438v2 , (4)–(11),(13)–(24),(26), Theorems 1.3 and 1.5(i)–(ii), Proposition 9.1(i) and its reflection case, Lemma 9.2 and proof (100)–(101), and both count/exhaustion cases (102)–(104) inspected directly. Versioned PDF locations: Theorem 1.5 pp.9–10; Section 9 pp.56–60. Saddle proofs remain imported, not audited.
COMPARISON: Theorem 1.5 gives an existential-onset count on unspecified small disks; L488 already replays its qualitative strict comparison. Neither fixes this onset or radius. Audited L490 supplies the upper-strip additive residual and audited L491 the full-unit-disk logarithmic ratio. Source conjugation and fixed logarithms cover the remaining techniques, leaving an explicit quantitative application rather than an uncovered mechanism.
GAP: The proposed count remains unproved: reconcile the opposite s_+ conventions, choose one nonvanishing holomorphic normalization, track the lower-half residual in that normalization, and prove TOTAL error strictly smaller than boundary modulus at radius 1/log(X/(4*pi)), including multiplicity and reality.
REASON: Approve only this bounded quantitative specialization of a known counting method; an explicit selected-disk count could support a later numerical real/simple tail but does not provide exhaustion, collision exclusion or zero-time control. No new result or margin is derived in this literature-only turn.
SCOPE: Exact TARGET only, with inputs L490 and L491 and source definitions/reflection. L488 is a qualitative comparison, not a numerical premise. A future attempt is REPRODUCTION; new source-scope changes need review. Full matching Mathlib coverage is unchecked.
LITERATURE_REASON: The saved nomination was REVIEW_REQUIRED because its full-disk numerical count lay outside the L491 audit; this step resolves that essential theorem comparison, without repeating an approved audit or extracting unnamed constants.

## Completed comparison

The full comparison and bounded application obligations are recorded in
[the source note](../heat/2026-10-30-explicit-local-circle-source-review.md).
The source inputs are accessible and adequate for an attempt; SPECIALIZE
does not assert that the attempted margin will pass. Do not infer a
numerical count from Theorem 1.5 or use source (76). The literal
Theorem 1.3 hypotheses and L490's retained imports govern the residual.
No global strip theorem is needed just to count a selected disk.

Continue only after a strict boundary comparison on the full disk
passes. If it fails, preserve the exact normalized error and required
lower bound; a failed coarse bound does not disprove the count. A
future new ready continuation remains subject to separate approval.

## Original nomination and unproved test (preserved)

Essential local inputs to compare: L490, L491 and the source
definitions of H_t, M_t, B_t and g. L488 is a qualitative comparison
and known-case reference, not a numerical-onset premise. Inspect
its strict-circle case together with the primary source's exact
hypotheses and normalization. Do not infer full-disk control merely
by repeating the upper-strip residual or by using the same letter
s_+ in L490 and L491: their sign conventions differ.

At nomination, the next source turn was required to check exact literature coverage and any
stronger ready theorem, reuse the inspected source evidence where
adequate, and distinguish an unspecified onset from this numerical
domain. If covered, approve only the identified quantitative
specialization. No mathematical derivation or approval of the new
count was performed during the L491 audit.

Continuation test for a later approved mathematical turn: exhibit
a nowhere-zero holomorphic normalization over the full disk and
a boundary lower bound strictly exceeding the TOTAL reflected
residual and gamma-model errors, uniformly in all stated t and X.
Accept only a count including multiplicity and a justified reality
inference. Preserve any failed margin or normalization identity.

This target does not claim exhaustion, a complete numerical tail,
zero spacing outside the selected disks, collision exclusion or
zero-time control. The generic collision/energy obstructions have
not been overcome. It is an established-route specialization,
not a proposed new central mechanism. Full matching Mathlib
coverage is unchecked. That nomination authorized no new lemma or
calculation until the separate comparison resolved REVIEW_REQUIRED;
the completed comparison above now records SPECIALIZE for the same target.
