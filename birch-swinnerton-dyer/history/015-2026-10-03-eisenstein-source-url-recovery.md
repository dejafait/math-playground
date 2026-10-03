# 2026-10-03 — Eisenstein source-URL recovery

Completed one literature-only recovery for the exact saved target in
[the assessment](../drafts/literature/2026-09-26-eisenstein-kato-extension.md).
The reported missing-URL condition was not reproducible: the file
already contained direct source URLs, and the current read_review
check accepted SPECIALIZE at entry. Added primary PDF URLs directly
to SOURCE_EVIDENCE and updated the check date. The exact target and
SPECIALIZE decision are preserved.

Performed three focused searches and read the cited primary lattice,
BF-class, critical-slope, and weighted-comparison statements. The
assessment distinguishes this recheck from the earlier source reads
that are reused. Corrected the Alonso--Omil-Pazos--Rivero Corollary
5.19 locator to PDF page 21. Its rank-one hypothesis and the
conjectural status of exceptional-factor division remain explicit.

The review confirms the prior decision. Known lattice results apply
to specified free stable submodules; they do not state that an
arbitrary modification retains the actual BF class with the required
nonzero quotient. No new extension, divisibility result, or global
lifting cochain is asserted. The cited results are known inputs,
not progress beyond the checked literature.

The main gap remains q(kappa) = 0 and r >= 2 beyond r <= 2. A lift
would address the mixed obstruction, while its Kummer interpretation,
nonvanishing from m(E) = 2, auxiliary existence, and higher ranks
remain unresolved. The bounded lattice/class test is still unperformed;
the process repair supplies no reason to abandon or restart it.

Step BSD-2026-10-03-015-eisenstein-source-url-recovery has outcome
STALLED, kind LITERATURE, and classification NOVELTY_UNCHECKED.
This is a source-evidence repair with no mathematical advance or new
route-changing negative. Exploration turns remain 0 of 3 from the
prior informative negative; no counter is reset for this recovery.
STATUS stays IN_PROGRESS. No candidate proof or disproof appeared.

Preserved existing work and left lemmas/, scripts/, foundations/,
DAG.md, PROOF.md, and inactive attempts unchanged. Only the active
assessment, current checkpoint, and this history entry were edited.
No shared infrastructure or scheduler state was edited.

Validation: `python3 ../scripts/docs/check_structure.py --problem birch-swinnerton-dyer`
passed with 12 nodes, 11 unique edges, an acyclic graph, complete file
coverage, valid local links, and compact overviews. The literature
reader accepted both STEP_REVIEW and NEXT_REVIEW as SPECIALIZE for
the unchanged exact target with direct source URLs. validate_turn
accepted the literature-only report, and the lemmas/scripts artifact
SHA-256 matched its entry value. `git diff --check` passed. No
mathematical or computational check was needed for this source review.
