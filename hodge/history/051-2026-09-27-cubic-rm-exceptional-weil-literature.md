# 2026-09-27 — Exceptional Weil-cycle supply assessed

STEP_ID: 2026-09-27-hodge-051-cubic-rm-exceptional-weil-literature.
Outcome: EXPLORATION. Kind: LITERATURE. Classification: NOVELTY_UNCHECKED.

Read the shared goals and prompt, local goal and checkpoint, whole
proof overview and ID-only DAG; inspected existing changes and
preserved unfinished work. The exact saved target had a
REVIEW_REQUIRED assessment, so the turn remained literature-only.

The gap is a cycle representative for the missing fourth cubic RM
direction. The intermediate target was a published exceptional
cycle supplying beta_U after L031's full divisor-algebra obstruction.
A valid import must include an algebraic transfer reaching the
whole tensor, including its nonzero torus-weight component. It
would leave algebraicity of kappa and the universal target separate.

Completed the [assessment](../drafts/literature/2026-09-27-cubic-rm-exceptional-weil-cycles.md)
with primary statements from both Schoen papers, Markman's
fourfold/sixfold theorem, his general CM-field construction and
2026 survey, Floccari--Fu and Patel--Zhang. Schoen's addendum
corrects an omitted polarization hypothesis in the 1988 theorem.
Newer results have broader field/discriminant scope, but none of
the inspected statements identifies the required tensor image.
The general CM-field construction explicitly retains algebraicity
under deformation as an assumption. Generalized Prym results also
need actual geometric data absent from the current construction.

This adds a theorem-level applicability comparison, not a new
mathematical obstruction or cycle. The known results are recorded
by citation and not reproduced. No novelty is claimed; unanswered
algebraicity is counted as exploration. No essential source remains
unread for the stated comparison, and the completed assessment is
EXPLORE. The earlier divisor certificate is reused without changes.

The selected continuation asks whether the full Kuga--Satake
variety has an abelian subquotient of dimension at most six. This
is a concrete prerequisite for direct transfers through abelian
homomorphisms from the proven low-dimensional supplies. An absent
factor would stop that recipe; an available factor would still
need its Weil hypotheses and tensor image checked. No factor bound
was calculated here. The exact action has a separate
[REVIEW_REQUIRED assessment](../drafts/literature/2026-09-27-cubic-rm-kuga-satake-small-factors.md).
Other correspondences and higher-dimensional Pryms are not excluded.

Exploration count is one after L031's informative negative result;
the new target shares the same three-turn allowance. The span
remains 21 on the Dickson family and the attained directions remain
three against four required. STATUS remains IN_PROGRESS and there
is no complete candidate. Lemmas, mathematical scripts and DAG
are unchanged. Mathlib coverage remains not checked.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 32 nodes and 80 edges, valid links and compact overviews.
The literature validator accepted the preserved starting target,
LITERATURE classification and exact new REVIEW_REQUIRED target.
File hashes confirmed that only PROGRESS, PROOF and the completed
assessment changed among existing files; the new assessment and
this history are the only additions. All lemmas, scripts, DAG and
other unfinished work were preserved. Whitespace checks passed.
No mathematical or computational experiment was run.
