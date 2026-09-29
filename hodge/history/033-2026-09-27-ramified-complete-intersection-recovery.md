# 2026-09-27 — Ramified complete-intersection recovery

STEP_ID: 2026-09-27-hodge-033-ramified-complete-intersection-recovery.
Outcome: NEGATIVE. Kind: RESEARCH. Classification: REPRODUCTION.

Read the shared and local rules, whole overview, DAG, saved checkpoint
and its prior SPECIALIZE assessment; inspected and preserved unfinished
changes. Worked only on the exact reviewed ramified-union target.
Provisional reasoning was saved before completing the proof in the
[recovery draft](../drafts/2026-09-27-ramified-complete-intersection-recovery-test.md).

[L023](../lemmas/L023-ramified-complete-intersection-unions-retain-obstruction.md)
excludes the transverse order-tau^2 lift for every admissible m,n>0,
allowing all earlier union motions. Positive top cohomology on the
support vanishes. Consequently one of the middle sheaf's central
inclusion/projection maps lifts through both small extensions on the
actual earlier sheaves. The recovered ideal gives an embedded C, whose
known fixed-product rigidity reduces its later equation to L008.
This resolves the prior review's missing compatibility; it is not just
the already known exclusion of constant earlier union motion.

The necessary bound is still at most three ambient RM coefficients
against four required. Equality retains H^1(I_C(nH))=0 and asserts
existence of some lift, not extension of every chosen Y_1. The action
U, attained 21-dimensional span and set of surfaces covered do not
change. Higher ramification orders, other representatives, actual
transverse families and the universal Hodge target remain unresolved.
STATUS stays IN_PROGRESS; no complete Hodge candidate was obtained.

The proof reproduces/applies standard Ext, duality, perfectness and
flatness tools, with full singular-point and base-reduction checks.
The saved assessment was sufficient and left no essential unread
source. The previously inspected Stacks criteria were consulted again
for exact applicability. Fujino's already cited Corollary 1.7 was also
checked for its higher-cohomology scope; the final top-cohomology proof
uses the shorter nef-fibre/Serre-duality argument instead. No new
literature gate or claim of originality is introduced. L022's earlier
proof and all prior cohomology work remain intact.

Stop the prescribed ramified complete-intersection escape. Changing
the positive degree ordering cannot remove the recovered map, so a
further such cohomology classification is not a useful continuation.
The selected different test allows both mixed first-order motions
between two rotation structure sheaves; their compositions could
enter a later diagonal obstruction. L017 computed a nearby directed
Ext group but did not evaluate these two-way products. This is a
reason to screen that possibility, not evidence of a cancellation.
Created a [REVIEW_REQUIRED assessment](../drafts/literature/2026-09-27-two-way-rotation-yoneda-products.md)
for the exact new target. No calculations for it were performed.
The informative exclusion resets exploration turns used to zero.

Updated the overview, the stopped-attempt record, and the sole compact
checkpoint. Added only L023's genuine mathematical inputs to the DAG:
the geometry/obstruction calculation, ideal reconstruction, fixed-product
rigidity, and all-degree linkage-extension recovery. No second graph
or lemma index was created.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 24 nodes and 59 edges. The step fields, prior SPECIALIZE
decision, exact new target match and REVIEW_REQUIRED gate were checked;
`git diff --check -- .` and new-file whitespace checks passed. An entry
hash comparison found only the four intended existing-file updates and
four new artifacts, with no deletions; all older lemmas, scripts and
literature assessments were unchanged. The mathematical audit checked
both signs of n-m, the d=0 boundary, reduction of extensions/maps, flat
kernel/cokernel recovery, singular-point reconstruction and the separate
rigidity input. No numerical calculation or new script was needed.
Structural validation does not verify the informal proof or the Hodge
conjecture.
