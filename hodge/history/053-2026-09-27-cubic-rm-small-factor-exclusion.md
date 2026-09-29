# 2026-09-27 — Low-dimensional Weil transfer excluded

STEP_ID: 2026-09-27-hodge-053-cubic-rm-small-factor-exclusion.
Outcome: NEGATIVE. Kind: RESEARCH. Classification: REPRODUCTION.

Read the shared goal and prompt, local goal and checkpoint, the
whole proof overview and ID-only DAG. Inspected existing changes
and preserved all earlier unfinished work. The exact saved target
had a prior SPECIALIZE assessment, which was reused unchanged.
Reread the named representation statements at their primary PDFs
to check the full representation and its left-multiplication action.

The local gap is algebraic beta_U beyond the Dickson family, with
algebraic kappa still separate. The selected intermediate target
was an abelian subquotient of A=KS(T) of dimension at most six,
needed for the low-dimensional Weil-cycle supply via abelian
homomorphisms. The stop threshold was a lower bound greater than
twelve for every nonzero rational weight-one subquotient.

[L032](../lemmas/L032-cubic-kuga-satake-has-no-small-abelian-subquotients.md)
establishes dimension at least 64 for those Hodge subquotients and
therefore at least 32 for abelian subquotients. It retains the full
H^1, all eight complex spin types and their multiplicity 256,
and explains rationality, complete reducibility and cohomological
contravariance. The bound also holds for all powers and isogenies.
No dimension-32 factor or sharp rational classification is asserted.
This supplies a new scoped negative result for the notebook by
specializing the reviewed representation theory; it is not a
claim of progress beyond those sources.

The required small-factor prerequisite fails, so the selected
homomorphism recipe is recorded as stopped in
[the attempt record](../ATTEMPTS/022-cubic-kuga-satake-low-dimensional-weil-transfer.md).
This is different evidence from the divisor-algebra obstruction;
that result and the old support/bundle failures are not mathematical
inputs here. L032 therefore has an empty input row in the DAG.

The [working record](../drafts/2026-09-27-cubic-rm-small-factor-test.md)
preserves the preliminary reasoning and its completed checks.
The previously reviewed generalized Prym theorem allows higher-
dimensional sources, which this result does not exclude. Its exact
tensor transfer has not been assessed, so the new action has a
[REVIEW_REQUIRED assessment](../drafts/literature/2026-09-27-cubic-rm-generalized-prym-transfer.md).
Only that pending scope was recorded; no new-target computation
or source assessment was performed in this research step.

The prior exploration window completes its test and stop decision
on the third turn. The consecutive exploration count is zero
after this informative negative result. Span 21 on the Dickson
family and three attained directions against four required are
unchanged. No algebraic cycle or complete candidate appears;
STATUS remains IN_PROGRESS. Mathlib coverage is not checked.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 33 nodes and 80 edges, valid links and compact overviews.
The metadata check accepted SPECIALIZE / RESEARCH / REPRODUCTION
for the completed target and the exact new REVIEW_REQUIRED target.
An exact integer check confirmed eight types of dimension 64 with
multiplicity 256, total H^1 dimension 131072=2^17, and 64>12.
These checks verify structure and arithmetic, not the proof itself.
The mathematical review checked the left action, rational
subquotients, cohomology-map directions and the scoped stop decision.
No mathematical scripts were added or modified, the prior assessment
was not rewritten, and earlier lemmas and unfinished work were kept.
Only PROGRESS, PROOF and DAG changed among existing files; the new
lemma, working record, pending assessment, attempt and this history
are the additions. Whitespace checks passed.
