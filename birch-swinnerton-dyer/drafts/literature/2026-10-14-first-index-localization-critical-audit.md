# First-index localization criterion — approved audit coverage

TARGET: Critically audit L061's first-index localization criterion, including coefficient transitions, both corank branches and finite discrete images.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the production assessment and parent assessment's exact-statement queries and duplicate checks; compared L005/L026/L061 and ATTEMPTS/031 specifically to the new audit scope. No broadened target or novelty search is needed.
SOURCE_EVIDENCE: Directly rechecked Kim https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf (2025-05-12, printed pp. 10--12, 14--15, 20, 25--28: Sections 2.1--2.3/2.4.1, Definition 2.12, Theorem 2.13(5), Proposition 3.13, (5.1), complete Sections 5.3.2--5.3.4); Wuthrich https://www.maths.nottingham.ac.uk/plp/pmzcw/download/fine.selmer.pdf (25-page author version, printed pp. 5--6, Section 3 diagram and Lemma 3.1).
COMPARISON: Sources cover the imported statements with both branches and finite comparison errors; L061's stronger global/local torsion hypotheses and coefficient-transition arguments require an applicability audit, not a reproof of the structure theorem.
GAP: Coverage is now approved, but the mathematical critical audit of L061 remains unperformed; no successful index or rational Kummer membership is produced.
REASON: Approve the unchanged exact audit target for one separate mathematical turn, preserving every L026 hypothesis and all finite-image qualifications.
SCOPE: Audit only L061's source applicability, coefficient transitions, strict kernel, rationalized dimensions and finite-image branches; repair actual assembly errors without producing an index or strengthening arithmetic hypotheses.
LITERATURE_REASON: The saved new audit continuation was REVIEW_REQUIRED; this separate theorem-scope approval is required before its mathematical critical review. Production coverage and recorded failures were reused.

Essential inputs are L005, L026 and the new L061. Reuse the
[approved production assessment](2026-10-14-first-kato-index-localization-criterion.md)
and its parent comparison; no changed arithmetic hypotheses or new source
search is proposed. This file now approves coverage; it does not perform
the mathematical audit.

Audit target: check global coefficient injectivity from residual
surjectivity, local coefficient injectivity at p only, preservation of
every other local Kummer condition, both transition directions, exact
Tate-module kernel matching and rationalized dimensions. Check the whole
system's nontriviality and first-index definition against the source,
including both strict/classical branches and the finite cyclic image case.
Do not infer integral Tate-module surjectivity from discrete surjectivity,
or infer k=1 from augmentation semisimplicity. Mathlib coverage remains
not checked, not asserted absent.

Continue only if all of these checks preserve the stated hypotheses.
Repair any actual error locally; otherwise retain the exact criterion
without reporting a point or branch-production theorem. Rational
membership of a strict class, auxiliary availability, selecting k=1,
uniform coefficient production and arbitrary complex-order comparison
remain unresolved. No cross-notebook input is required.

## Separate source-scope approval, 2026-10-14

The main gap remains rank E(Q)=m(E) for arbitrary m(E)>=2. The
intermediate target is the exact TARGET above. Its plausible downstream
use is a trustworthy criterion for the localization prerequisite of the
separately assessed generalized-Kato route. This criterion alone neither
selects an index nor identifies a strict class with a rational point.

The cited Kim version is unchanged. Theorem 2.1's local divisibility
condition and Section 2.4.1's residual working assumptions were inspected
alongside the statements already assessed. The collection comparison is
not componentwise. Both positive-corank proof cases were read through
their conclusions, including the bounded finite parts, large coefficient
depth and useful-prime step. These are imported source arguments; the
forthcoming audit must check their applicability without recreating them.
Wuthrich's diagram explicitly uses left exactness and retains a finite
index, so it cannot justify a general integral equality or surjectivity.

The local comparison reads L005's definitions and full coefficient-limit
argument, L026's hypotheses and existing source assembly, and all of
L061. Coverage distinguishes the two uses of localization: the classical
discrete map at p and a Kato component's singular localization. It also
distinguishes upward inclusions, downward multiplication maps, and point
quotient reductions. These distinctions are audit obligations, not
mathematical conclusions verified by this literature turn.

Duplicate and failure coverage is reused from the production assessment
and its parent. The targeted ATTEMPTS/031 read confirms that direct
ordinary-semisimplicity import is still parked. L014/L021 and L013/L019
remain contrasts under the parent's inspected comparison; no additional
proof reads or cross-notebook imports are needed. The present source
review is new audit-scope approval, not a repeat mathematical audit or a
claim of progress beyond the sources checked. No lemma, mathematical
script, DAG edge or main argument was changed.

Continue if the audit justifies every coefficient identification under
the retained hypotheses and preserves both corank alternatives and
finite discrete images. Repair a genuine error in the existing assembly;
stop downstream use if an essential identification fails or requires
finite Sha, point membership, integral right exactness or preselected
nonzero localization. Essential inputs are L005, L026 and L061; all
L026 arithmetic, residual, normalization, central-vanishing, sign and
coefficient premises remain supplied assumptions. Mathlib coverage of
the full result and supporting facts remains not checked.
