# 2026-09-26 — Boundary exclusion already covered by Cohen

STEP_ID: beal-2026-09-26-012-boundary-cohen-literature
STEP_KIND: LITERATURE
STEP_OUTCOME: NEGATIVE
STEP_CLASSIFICATION: KNOWN_IMPORTED

Completed one source review of the saved fourth-power-difference descent target, preserving that exact target in the [assessment](../drafts/literature/2026-09-26-current-target.md). The previously read Darmon theorem does not cover exponent 3. Following Bennett–Chen–Dahmen–Yazdani Section 5 led to Cohen, *Number Theory II*, Proposition 14.6.6, pp. 484–485. The complete statement and both proof cases were read through a transcription of the book, with publisher metadata and source-access qualifications recorded. This supplies the required fixed-signature source result with no parity or base-one omission.

The new evidence changes the decision from developing a descent to importing known mathematics. NEGATIVE describes redundancy of the proposed independent route, not an impossibility proof for that mechanism or a Beal counterexample. KNOWN_IMPORTED describes the cited source content; no new mathematical derivation, descent map, or elliptic-rank computation was performed. No result beyond the checked literature is claimed. Exploration turns used: 0/3 after this informative overlap finding.

The desired threshold was zero primitive solutions, not bounded-height evidence or fixed-signature finiteness. The source reaches that threshold for this boundary equation. The mathematical assembly has not yet been extended: the local application and L002 divisor consequences are the reason for the [screened import target](../drafts/literature/2026-09-26-cohen-boundary-import.md). Repeated-cube primes in L011's complement and unrelated mixed signatures still require global exclusions. No complete candidate appeared.

All existing work was preserved. Lemmas, mathematical scripts, PROOF.md, and DAG.md were left unchanged because this turn only completed the literature assessment. The compact checkpoint records the continuation; no inactive branch was removed. Mathlib coverage is not checked.

`python3 ../scripts/docs/check_structure.py --problem beal` passed: 12 nodes, 15 unique edges, an acyclic graph, complete file coverage, valid links, and compact overviews. `git diff --check -- .` passed. A read-only field check confirmed one value per required field, preservation of the original reviewed target, and exact matching between the new Next action and its ready IMPORT assessment. No mathematical computation was needed for this source review; these checks certify documentation structure only.
