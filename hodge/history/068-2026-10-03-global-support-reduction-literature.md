# 2026-10-03 — Global universal-sheaf support reduction: source review

STEP_ID: 2026-10-03-hodge-068-global-support-reduction-literature.
Outcome: EXPLORATION. Kind: LITERATURE. Classification: NOVELTY_UNCHECKED.

Read the shared goal and prompt, local goal and checkpoint, the
whole proof overview and ID-only DAG. Inspected and preserved
pre-existing changes. The exact saved assessment was
REVIEW_REQUIRED, so this step performed only source review.
An intermediate source checkpoint was saved before finishing
the comparison, then incorporated in the completed
[SPECIALIZE assessment](../drafts/literature/2026-10-03-universal-sheaf-global-support-reduction.md).
The saved target text is unchanged.

The main gap on this route is an independent non-scalar cubic-RM
action on a transverse surface. A global support/action reduction
could identify the geometric input a new stable family needs.
The previous one-moving-point test does not classify boundary
families, so its scalar conclusion was not extrapolated.

The inspected surface moduli theorem gives the slope-graded
double dual and quotient-length invariant; fixed-polystable-bundle
strata and flat zero-dimensional families have symmetric-product
descriptions. Kollár supplies a simultaneous-hull framework,
while Fulton supplies the weighted leading-cycle input.
Markman's action convention is retained. The assessment records
versions, statement numbers, pages, direct links and the stronger
Tajakka and Greb--Toma comparisons. The initial Greb--Toma PDF
extraction was checked against arXiv v3: n>=2 is correct, so its
surface applicability was restored in the final source notes.
Li's inaccessible original PDF is not imported separately;
the accessible Huybrechts--Lehn statements resolve that source scope.

The full boundary-inclusive reduction is not imported. Its
actual fibre hulls, simultaneous family, flat length-three
quotient and mixed transcendental Chern comparison remain a
single bounded specialization test. Continue with that test
in a separate research step, importing the general results
without reproof. Stop or restrict the uniform reduction if
a boundary exception invalidates the needed family statement.
Even success leaves construction and stable descent of a
non-scalar family, transverse coverage and the universal gap open.

No new mathematical result or candidate was produced. Supporting
results are known imports, and no novelty of the remaining
specialization is inferred from the search. The attained span
stays 21 on the Dickson family, with three RM directions against
four required. The stopped scalar recipe contributes one
transcendental dimension against three required. Consecutive
exploration use is one after L038; no runner state was changed.

Updated the assessment, the source qualifications in the overview
and the sole compact checkpoint. The canonical DAG, all lemmas,
mathematical scripts and previous assessments were left unchanged.
Mathlib coverage remains not checked.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 39 nodes and 83 unique edges; bytecode writes were
disabled. `git diff --check -- .` passed. The shared literature
validator accepted LITERATURE / NOVELTY_UNCHECKED with the exact
unchanged target and ready SPECIALIZE assessment. Entry-hash
comparison found only the assessment, checkpoint and overview
updates plus this new history file; no file was removed and
all protected lemma/script bytes were unchanged. No mathematical
or computational test was needed for this source-only step.
Documentation checks do not verify a mathematical result.
