# Four-kernel audit: control loop overwrites the selected index

2026-10-23, step 419. The sole approved audit stops at the first report
comparison after n=3 replay; n=4,5,6 do not run. The complete canonical
audit qualification is in [L105](../lemmas/L105-four-fixed-rational-kernel-certificates.md).
Evidence remains in `scripts/four-rational-kernels/step-419/` and the
static diagnosis in `drafts/2026-10-23-four-kernel-audit-static-diagnosis.json`.

## WHY IT FAILS

The reused signed-control block is executed in the new worker's module
namespace. Its loop variable `n` ends at `2*D+1`, overwriting the index
read from the command line. The directory and replay module already
select n=3, so full arithmetic replay returns, but appending the overwritten
index to its report makes equality with the saved n=3 report fail.
This is a fresh harness error, not a mathematical contradiction or
certificate defect. The returned report is not persisted and later
audit comparisons do not run; no audit PASS may be inferred. Preserve
the stopped run without repair, retry or resumption. A function-scoped
control routine and immutable index contract are a specific changed
interface for separate review, not a retroactive repair of step 419.
