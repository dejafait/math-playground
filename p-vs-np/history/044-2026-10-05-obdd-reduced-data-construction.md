# 2026-10-05 — Shared OBDD reduced-data construction

Completed the exact prior EXPLORE target in `drafts/literature/2026-10-05-obdd-reduced-data.md`; reused its source comparison and the coefficient-degree assessment. Checked L020/L025, the relevant L024 hypotheses and Attempts 017–018. No new literature turn or cross-notebook input was needed.

[L026](../lemmas/L026-obdd-reduced-original-axiom-data.md) constructs the original-axiom reduced relations with both formal identities and full polynomial size from supplied common-order width-w diagrams. It proves d=max(1,n), h=max(1,2n-1), exact signed roots and a complete binary encoding bound. L025 can consume this restricted data. No unrestricted diagram-size bound, certificate tree conversion, proof lower bound or SAT conclusion follows. The comparison supports POTENTIALLY_NEW, not certified originality or progress beyond all literature.

The full finite certificate is `scripts/obdd-reduced-data/suffix-witness-results.json`: a generic free-ring identity, 308 diagram cases and 3,960 suffix commutator checks pass, with all three deliberately broken correction variants detected. These diagnose the construction; the canonical proof carries the general result. Saved pre-proof reasoning is in `drafts/2026-10-05-obdd-construction-work.md`.

Outcome ADVANCE / RESEARCH / proof_attempt. Mathematical exploration usage resets from 1 to 0 because this establishes the missing restricted data input, not because of the tests or a new lemma count. Preserve the stopped same-output/exact-lift routes and repeated-approval evidence. The next direction is a critical audit of L026, with its newly written exact assessment left REVIEW_REQUIRED for separate approval. No supervisor state was edited.
