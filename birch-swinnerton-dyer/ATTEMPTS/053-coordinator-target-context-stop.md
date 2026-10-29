# n=43–46 source construction: AST target context mismatch

2026-10-25, step 474. The sole fresh builder invocation exits one before
generated-source compilation or production. The complete
[attempt record](../drafts/2026-10-25-n43-46-role-selected-attempt.md)
locates the first failure and read-only diagnosis. No kernel or production
resource certificate exists; all stopped sources remain unchanged.

## WHY IT FAILS

The historical-loop selector compares the complete AST of a `for` target
with the AST of an evaluated expression. Both identifiers are `step`,
but their contexts are Store and Load respectively, so their AST dumps
differ. The unique-role guard reports zero matches after six unapplied
edit records. Complete owning-call pins had passed, but no full edit map
or generated source was emitted. This is an implementation error, not a
mathematical obstruction. Do not repair, retry or resume the stopped
builder. After stalled steps 472 and 474, park the coordinator-adaptation
route; a standalone n=43 certificate from fixed arithmetic sources is a
different, independently testable implementation target requiring separate
runner/source/preservation coverage. Existing analytic coverage is retained.
