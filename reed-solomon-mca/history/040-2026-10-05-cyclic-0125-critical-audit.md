# 040 — 2026-10-05 — Critical audit of the cyclic 0125 exclusion

The separate audit of [L026](../lemmas/L026-cyclic-0125-affine-support-exclusion.md)
found no error. It independently reproduced all 104 minors and rebuilt
the necessary-condition matrix from actual moment nullspaces, obtaining
rank 28 for all eight generators. The complete evidence is
`scripts/cyclic-0125/alternating-obstruction-audit.json`; the canonical
lemma records the extension-field, offset, degenerate-direction and
equality-applicability checks. No mathematical dependency changed.

Completed kind: RESEARCH; classification: REPRODUCTION; task: proof_audit.
Outcome is conservatively EXPLORATION: this new independent check validates
the previous result but establishes no additional bound or error repair.
The global interval remains 11/q–16/q and STATUS remains IN_PROGRESS.
The fixed-label exclusion is now audited, so another repeat audit is not
justified. The [pending arbitrary-label rank assessment](../drafts/literature/2026-10-05-cyclic-0125-arbitrary-label-rank.md)
proposes a distinct test with a deficient labeling as its falsifier; its
broader hypotheses require a separate literature-only approval before
any mathematics. The earlier stops and unfinished work are preserved.
