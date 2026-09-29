# 2026-10-03 — Global degree-three support/action specialization

STEP_ID: 2026-10-03-hodge-069-global-degree-three-support-action.
Outcome: ADVANCE. Kind: RESEARCH. Classification: REPRODUCTION.

Read the shared goal and prompt, local goal, checkpoint, whole
proof overview and ID-only DAG; inspected and preserved existing
changes. Reused the ready SPECIALIZE assessment for the exact
saved global reduction target, leaving its bytes unchanged.
The step addressed the missing actual family and mixed Chern
comparison, with stable non-scalar-map construction explicitly later.

The full scoped proof is
[L039](../lemmas/L039-global-degree-three-support-action.md).
Stability and chi(F)=1 supply a map to O_X with image of
colength at most one. Ext vanishing excludes the only possible
nontrivial bundle-hull image. This proves that every stable
fibre has actual hull O_X^2. Constant relative Hom and Ext
dimensions then construct the parameter bundle and its
base-changing evaluation inclusion. The quotient is flat
of length three. Its leading Chern character computes the
normalized Mukai action as the positive weighted-support action.
This works for families entirely in collision strata.

The saved continuation test passed: the missing all-fibre
family/action input is established, without a boundary exception.
The critical family, injection, multiplicity and sign checks
are retained in the
[working record](../drafts/2026-10-03-global-support-reduction.md).
The base-change and perfect-complex local-normal-form statements
were read in Stacks Tags 0DJT, 0BCD and 0BDI as supporting tools.
Huybrechts--Lehn's flatness criterion and Markman's convention
were checked directly; the other ready source evidence was reused.
No full-statement match or originality is asserted.

This is local progress through an application of known theorems,
not a new non-scalar cycle or a general Hodge resolution.
The 21-dimensional span on the Dickson family and three RM
directions against four required remain unchanged. L038's
specific scalar/collision obstruction is preserved. An existing
stable family now has a precise support/action description,
but an arbitrary support map has no proved stable lift.

The next direction is the converse lifting issue, including
collision strata, to make a later non-scalar-family construction
testable. Its exact changed target is recorded as
[REVIEW_REQUIRED](../drafts/literature/2026-10-03-degree-three-support-stable-lifts.md).
No search or calculation on that target was performed here;
the next turn is literature-only. Exploration use is zero
consecutive after this mathematical input. No runner research-stop
state was edited, and no complete informal candidate is present.

Added only L039 to the ID-only DAG, with no earlier lemma as a
direct mathematical input: the proof uses named standard theorems
and source imports. Updated the relevant overview passage,
known-traps qualification, compact checkpoint and working record.
Mathlib coverage remains not checked. Earlier files and inactive
branches were preserved.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 40 nodes and 83 unique edges; bytecode writes were
disabled. `git diff --check -- .` and the new-artifact whitespace
check passed. The literature validator accepted RESEARCH /
REPRODUCTION under the unchanged prior SPECIALIZE assessment,
with the new target REVIEW_REQUIRED. Entry-hash comparison found
exactly the three overview/checkpoint/DAG updates and four new
artifacts; every earlier lemma, script, assessment and other file
was unchanged, and no file was removed. No numerical computation
was needed for this proof step. The checks validate documentation
and process fields, not mathematical correctness.
