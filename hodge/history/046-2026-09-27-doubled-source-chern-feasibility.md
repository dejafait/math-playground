# 2026-09-27 — Doubled-source Chern feasibility test

STEP_ID: 2026-09-27-hodge-046-doubled-source-chern-feasibility.
Outcome: EXPLORATION. Kind: RESEARCH. Classification: REPRODUCTION.

Read the shared and local instructions, complete proof overview, DAG,
checkpoint and exact prior EXPLORE assessment. Inspected existing changes
and preserved previous work. Reused the adequate
[assessment](../drafts/literature/2026-09-27-doubled-source-cubic-resolution.md)
without modifying it or repeating its searches. The necessary Chern and
invariant-form sources had already been read; no essential source gap
was cleared in this research turn.

The gap is an algebraic representative permitting the missing fourth
NS-fixed RM direction. The intermediate target was the exact doubled
source, with W-restricted product-line presentations, an integral twist,
and stability with invariant first two Chern classes. The saved threshold
required a concrete integral presentation with justified maps and a
bounded stability test, or an informative scoped obstruction. A formal
tensor was explicitly insufficient. Even a successful bundle would still
leave transverse transport and the universal Hodge gap open.

Saved unfinished reasoning in the
[working record](../drafts/2026-09-27-doubled-source-integral-chern-test.md).
The completed arithmetic and full necessary-condition proof are in
[L029](../lemmas/L029-doubled-source-chern-necessary-conditions.md).
Doubling scales the cubic polynomial and leaves an evenness condition;
it prevents reuse of L028's coprime-primary contradiction. An explicit
integral operator and signed product-line class pass that isolated test
in L025's pre-chamber model. The final rational chamber conjugation can
introduce denominators, and no exact presentation or stable bundle has
been constructed. This is a specialization of known Chern/invariant-form
tools, not a discovery beyond the checked literature or an originality
claim. Mathlib coverage of the full statement is not checked.

The result does not meet the saved advance/negative threshold. Recording
a new lemma does not change that: exploration turns used are now 2 of 3,
not reset. The reassessment discards direct sums as a stability mechanism
and further formal tensor searches as insufficient. It retains one final
bounded test of actual mixed presentation maps under the same target,
requiring the final-lattice data and an integral twist. If no actual map
mechanism or new obstruction appears, complete the assessment and stop
this construction approach within the third turn. This is not a general
nonexistence claim or a request to wait for an externally supplied idea.

The exact Next action is unchanged, so its sufficient prior assessment
continues to be NEXT_REVIEW; no new target was investigated. The known
span stays 21-dimensional and the attained directions stay three against
four required. No complete candidate for the main conjecture appeared.

Added L029's four direct mathematical inputs to the ID-only DAG and a
short scoped paragraph to the overview. Updated the compact checkpoint;
all earlier lemmas, scripts, assessments and inactive branches remain.

Validation: `python3 -B scripts/cubic-kahler/check_doubled_source_chern.py`
passed. It checks the exact tensor/operator identities, scaled polynomial,
parity, and signed-line rank and Chern moments. These are arithmetic checks,
not an exactness, stability or Hodge-conjecture certificate.

The required hodge structure checker passed with 30 nodes and 77 edges,
valid links and compact overviews. The initial overview edit exceeded
the 100-line limit; integrating the new scoped note into its existing
bundle discussion restored that limit without removing earlier content.
Review-field checks accepted the unchanged exact EXPLORE target and the
RESEARCH/REPRODUCTION classification. Tracked and new-file whitespace
checks passed. These process checks do not verify the mathematical proof.
