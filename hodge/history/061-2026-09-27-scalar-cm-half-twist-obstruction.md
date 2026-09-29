# 2026-09-27 — Scalar CM extension fails the half-twist prerequisite

STEP_ID: 2026-09-27-hodge-061-scalar-cm-half-twist-obstruction.
Outcome: NEGATIVE. Kind: RESEARCH. Classification: REPRODUCTION.

Read the shared goal and prompt, local goal and checkpoint,
whole proof overview and ID-only DAG, then the saved SPECIALIZE
assessment. Inspected existing changes and preserved prior work.
Reused that assessment unchanged; a direct reread of van Geemen's
cited sections confirmed the existing criterion. No new literature
gate was cleared in this research turn.

The local gap was an effective polarized weight-one auxiliary
structure that could support an abelian realization of the cubic
action. A successful half twist would leave algebraic comparison
cycles unresolved. The discriminating test was zero forbidden
top-piece support for at least one CM type; failure for every
type would stop the precise scalar-extension recipe. The older
Clifford/Prym and bundle exclusions did not compute this support.

[L035](../lemmas/L035-scalar-cm-extension-has-no-effective-half-twist.md)
gives the full proof. Both conjugate embeddings over the real
top-piece embedding occur. Each of the eight CM types therefore
has defect one, against zero required. The formal shift retains
two non-effective Hodge lines, so polarization cannot rescue the
required effective structure. The
[attempt record](../ATTEMPTS/026-auxiliary-scalar-cm-half-twist.md)
stops this recipe within its stated scope.

This is a negative application of known mathematics, not a claim
beyond the checked literature. The half-twist criterion is
imported by precise citation; its scalar-extension application
is reproduced. Mathlib coverage is not checked. No script or
numerical experiment is needed for the embedding calculation.

The bounded window finishes in its third invocation with this
informative negative result, following two exploration turns.
The uniform question about arbitrary CM actions on finite direct
sums will test whether changing the action can help. It has a
[REVIEW_REQUIRED assessment](../drafts/literature/2026-09-27-cubic-rm-direct-sum-cm-half-twists.md);
no support calculation or conclusion for that new target is made.

The attained span stays 21 and the attained RM directions stay
three against four required. Both Kuga--Satake algebraicity
inputs and the universal Hodge target remain open. STATUS stays
IN_PROGRESS; no complete candidate appears. The overview records
the new scoped obstruction. L035 uses the stated Hodge data and
the named source, with no earlier lemma as a mathematical input;
its new DAG row has an empty right side. PROGRESS.md is the sole
current checkpoint.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 36 nodes and 83 edges, valid links and compact
overviews. The shared literature validator accepted the RESEARCH
turn, unchanged prior SPECIALIZE assessment and exact new target
with REVIEW_REQUIRED. Single metadata fields, section order and
whitespace checks passed. File hashes confirmed that all prior
lemma/script files and assessments were preserved; only the
three current overview/checkpoint/graph files changed, with four
new scoped records added. The mathematical check is the complete
embedding argument in L035, not a computational certificate or
a claim that structural validation proves the Hodge conjecture.
