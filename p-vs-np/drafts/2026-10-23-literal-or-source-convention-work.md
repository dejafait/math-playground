# Step 420 — completed source-convention review

Literature-only target: compare L097/L098's literal-OR source presentation
with LTW and primary completeness references; no lemma or script changes.
Main gap: unrestricted SAT decision/separation. Intermediate target: settle
the exact language/rules supported by the completeness citation. Downstream
use: decide whether L106's exact source compiler has an adequate basis, before
any changed extraction or implementation. Continue only with explicit source
coverage or a separately reviewed discriminating test; abandon the unchanged
completeness import if its hypotheses do not cover the serialized language.

Inspected L097 §§3–4, L098 hypotheses, L106's finite-template passage and
step-419 qualification, the exact parser/pattern/MP branches of
`scripts/parity-source/checker.py`, Attempt 036, and the complete selected
endpoint/row diagnostics using the shared JSON inspector. Existing changes
and finite archives are preserved. Reused earlier scope assessments only
for their recorded coverage; they did not resolve this changed hypothesis.

Primary LTW author manuscript is accessible. Printed p.2 explicitly expands
implication as negation/disjunction, displays three schemes, and gives exact
MP. Definition 2.1, printed p.11, has ordered OR/AND/NOT trees and constants;
Definitions 2.2–2.4 require sound rules and implicational completeness.
Lemma 3.3, printed pp.13–14, explicitly treats those three schemes and MP.
No extra OR bridge has been found in those load-bearing passages. This is
textual scope evidence, not a proof that such a bridge cannot be derived.

The primary scan of Shoenfield, *Mathematical Logic* (1967), was read at
§2.6 pp.21–23 and §3.1 pp.27–30, including the complete connective cases
of the Tautology Theorem proof. Its four propositional rules differ from
the local checker. This supplies new negative source-coverage evidence,
not a proof of source nonderivability. The completed citations/comparison
are in `drafts/literature/2026-10-23-literal-or-source-convention-review.md`.
The opaque-OR universal soundness test is a proposed next target with a
separate REVIEW_REQUIRED assessment; no obstruction or repair is approved
here. No mathematical script or lemma was changed. Mathlib is unchecked.
