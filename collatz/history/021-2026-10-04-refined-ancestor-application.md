# 2026-10-04 — Imported refined ancestor bound at the fixed least root

Step `collatz-2026-10-04-021-refined-ancestor-application` completed one
RESEARCH source application, outcome ADVANCE, classification
KNOWN_IMPORTED. STATUS remains IN_PROGRESS. The exact target was
preapproved by the saved
[IMPORT assessment](../drafts/literature/2026-10-03-residue20-residual-ancestor-selector.md),
which was reused unchanged. Existing notebook and other notebooks'
changes were preserved; no literature search was performed.

[L015](../lemmas/L015-residue20-least-bad-ancestor-valuation-bound.md)
records the precise source theorem and checks its applicability to the
same least bad root supplied by L014. The actual forward identity
transfers convergence from the smaller positive residue-20 ancestor,
including when it has reached 1 before the specified root hit. The
[calculation checkpoint](../drafts/2026-10-04-refined-ancestor-application.md)
records the relevance test and comparison with the prior restriction.

The application passes and excludes v_3(4n+1)>=13 at a hypothetical
least root. This is a relevant imported input added to the local
argument, not a discovery beyond the checked source. Universal
convergence or eventual descent for the complementary infinite class
is still missing. No complete candidate or global return rank appears.
Attempts 009 and 010 and all prior evidence remain intact.

The next direction is the exact guarded lower-row application already
covered by the same assessment. It tests additional cited exclusions
against the original root, without extending source scope or requiring
another review. No mathematical EXPLORATION turn was spent and no
counter reset. PROOF.md records the added restriction and DAG.md records
L015's genuine use of L014 to obtain the least bad root.

The proof is a citation and an all-integer convergence argument; no
finite orbit replay, mathematical script, or Lean build was needed.
Validation: `python3 ../scripts/docs/check_structure.py --problem collatz`.
