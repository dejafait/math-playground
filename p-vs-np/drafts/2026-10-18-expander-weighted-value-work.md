# Step 333 — Weighted expander-value specialization, work checkpoint

Approved target: Test whether L030's expander cut-rank obstruction rules out polynomial-size L085 value graphs for L031's unchanged used extension.

Prior gate: `drafts/literature/2026-10-18-expander-weighted-value-obstruction.md`, SPECIALIZE, unchanged before invocation. Actual work is a mathematical proof attempt, using its inspected all-field lower direction; no additional source search or new graph/rank proof is needed.

Main gap: unrestricted SAT decision/separation. Intermediate target: an exponential explicit-size bound for the designated faithful positive h, in every L085 order. Downstream use: stop universal polynomial availability of that restricted supplier while leaving arbitrary affine ABPs, nonfaithful data, alternative proofs/certificates and SAT transfer open. Continue if scalar-terminal reception, evaluation-map direction and full-bit accounting all hold; abandon the rank mechanism if one fails or a polynomial graph for this same root is found.

Inputs read: L030's complete rank argument (rank M >= 2^(c n) at every half-prefix); L031's exact positive root, signed-unit ancestry and full T bound; L085's precise layered value model. Attempts 019/020/029 distinguish deterministic diagrams, general same-output degree conversion and unsimplified structural trees from this target. No cross-notebook input.

Work in progress: abelianize the supplied free-ring path polynomial. If A_i is the rectangular affine transition matrix, e the initial row and t the scalar terminal column, the commutative polynomial is e A_1 ... A_n t. Absorb e into A_1 and t into A_n, and zero-pad internal dimensions to their maximum w. This is the cited width-w roABP model without a new variable. The normalization is polynomial in the explicit input; arbitrary parallel/zero edges and all original records remain charged.

At the actual half-prefix, let D span all prefix-specialized residual polynomials. Evaluation on Boolean suffixes maps D linearly onto the truth-matrix row space, so rank M <= dim D. The imported Kayal–Nair–Saha Lemma 12, Appendix B lower direction gives dim D <= w over F₂. Hence w >= 2^(c n). Need finish the literal encoding bound and unchanged-T comparison in a canonical result, preserving both unit signs and no claim about alternative certificates.

This checkpoint is unfinished reasoning, not a separately approved theorem or a final outcome. A separate critical audit remains appropriate after the specialization is written.

Completion: the canonical proof is now in `lemmas/L086-expander-faithful-weighted-value-size-obstruction.md`. Its finalized receiving matrices use distinct incoming-edge heads as internal coordinates, retaining unreachable heads and charging all original records, so w<=E<=B without assuming one bit per isolated vertex. This supersedes the tentative vertex-record accounting above. Outcome NEGATIVE / REPRODUCTION; separate critical audit pending.
