# 2026-10-26 — nonreal near-degree specialization

STEP_ID: 2026-10-26-c464b-nonreal-degree-convolution

Completed the single approved RESEARCH / REPRODUCTION proof attempt
under the unchanged [SPECIALIZE assessment](../drafts/literature/2026-10-26-nonreal-near-degree-threshold-coverage.md).
[C464b](../lemmas/C464b-nonreal-near-degree-xi-tail.md) proves the saved
threshold by separating the real near multiplier and applying L464 at
every finite convolution shift. The leading real coefficient preserves
strictness, including central zeros; n=0, M=0, repeated factors and
integer equality are explicit. The unchanged far sum is retained.
Only L464 is a direct mathematical input. The DAG and short overview
were updated accordingly; all pre-existing unfinished work is preserved.

Outcome ADVANCE means a relevant local parameter-sensitive bound was
established, not a discovery beyond the checked source mechanism. No
improved nonreal count or initial signs follow. It could make a future
bound on nearby nonreal zeros useful for a tail estimate, but all-height
initial signs and global mixed positivity remain the main gap. The
historical fixed-anchor, onset and masking stops remain intact. No
mathematical script or numerical certificate was needed: the test is a
finite symbolic argument covering all shifts, rather than a sample.
Mathlib and independent full-manuscript coverage remain unchecked.

The continuation is a separate critical audit, with its new
[scope assessment](../drafts/literature/2026-10-26-c464b-critical-audit-coverage.md)
marked REVIEW_REQUIRED for approval next turn. It is not performed in
this step. The compact checkpoint owns the sole current action.

Validation: `python3 ../scripts/docs/check_structure.py --problem riemann`
passes, as does notebook-scoped `git diff --check`. The new dependency
is mathematically L464 alone: its comparison and exact factorization
supply all non-elementary inputs. Structural checks do not constitute
the pending independent critical audit.
