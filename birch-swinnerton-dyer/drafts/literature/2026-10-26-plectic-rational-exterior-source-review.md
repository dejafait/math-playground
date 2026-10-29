# Plectic geometry — rational exterior-class source comparison

TARGET: Assess whether plectic Heegner-point constructions give a proved rational exterior-square class for E/Q that can supply L005's nonzero strict Kummer input without assuming finite Sha.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Local plectic/mock/polyquadratic search found only the startup proposal; external construction/rationality/exterior-power searches located the 2022 polyquadratic theorem, 2025 mock construction, 2024 Iwasawa refinement and 2026 partially global classes; queries and read ranges are in drafts/source-notes/2026-10-26-plectic-rationality-coverage.md.
SOURCE_EVIDENCE: Inspected arXiv:2104.12575v1 Section 1.4; arXiv:2203.15998v1 Assumptions 1.1/1.5/1.7/4.1, Theorems A-C/5.1-5.3 and relevant proofs; published Darmon-Fornea (2025) Theorem 3.8 and Conjecture 3.13; arXiv:2311.03100v2 Theorem 3.4 and Conjecture 2.16; arXiv:2603.28327v2 Theorems A-C, Corollary 4.24 with proof and Conjectures 1.9-1.10.
COMPARISON: Proved polyquadratic algebraicity is a projected/normed determinant over auxiliary CM fields with algebraic coefficient extension; mock refinements give Selmer information and the 2026 construction a global H^1 factor, while their rational determinant comparisons remain conjectures; none inspected supplies the required nonzero strict rational Kummer class over Q.
GAP: Rational Kummer membership, justified Q-descent and nonvanishing remain missing; multiplicative reduction at the construction prime also lies outside L005's good-reduction hypotheses; no complex-order comparison is obtained.
REASON: New theorem-level evidence rejects the direct rational-exterior import while identifying a genuinely partially global arithmetic object for a narrower, separately gated local test; this is an informative negative comparison, not a universal nonexistence result.

## Completed source-review contract

This literature-only step establishes source scope, not a new lemma.
The full hypotheses, versions, precise references and proof-case
comparison are recorded in the [source notes](../source-notes/2026-10-26-plectic-rationality-coverage.md).
The OUP final full-text endpoint was unavailable; the polyquadratic
claims are tied to its inspected arXiv v1. This is not persistent source
blockage and does not justify assuming the final text is identical.

The general construction's rationality is Conjecture 1.3 of
[Fornea-Gehrmann, 2104.12575v1](https://arxiv.org/html/2104.12575v1).
The substantive exception is [2203.15998v1, Theorem 5.3, pp.15-16](https://arxiv.org/pdf/2203.15998v1#page=15):
its proof wedges Heegner points from distinct twists over the auxiliary
CM field and compares only after the specified projection and norm.
It does not state the desired Q-descent. The algebraic quadratic
coefficient extension must not be confused with a field of definition
of points or with arbitrary Q_p coefficients.

[Fornea, 2603.28327v2, Theorem A and Corollary 4.24](https://arxiv.org/html/2603.28327v2)
construct a tensor with a genuine global cohomology factor. Its finite
field descent is proved, but Selmer membership and the exterior
determinant statement are Conjectures 1.9-1.10. The mock specialization
has a proved Selmer criterion, and [2311.03100v2, Theorem 3.4](https://arxiv.org/html/2311.03100v2)
gives Selmer corank two from nonvanishing; Remark 1.4 does not replace
that corank by point rank without finite p-primary Sha. This reproduces
the type of logical limitation in ATTEMPTS/003, /004 and /030, now for
different actual constructions. The new sources do not overcome it by
terminology. L122 remains a conditional criterion, not a producer.

The direct-import route is parked with its precise scope in ATTEMPTS/058.
EXPLORE records that no adequate match was found in this bounded search;
it is not approval to prove the original rationality conjectures or any
newly nominated target. The same-prime localization of the 2026 class
is a narrower candidate test with separate REVIEW_REQUIRED coverage.
Its potential use is to test a local obstruction before attempting
global Kummer membership; no cancellation, nonvanishing or Q-rational
point follows from this review. Mathlib coverage is **not checked**.
