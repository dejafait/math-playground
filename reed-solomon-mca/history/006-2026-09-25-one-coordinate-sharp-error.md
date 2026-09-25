# 006 — 2026-09-25 — Sharp one-coordinate-omission cell

Completed one quotient-geometry step in the frozen affine-line model. The
[assessment](../drafts/2026-09-25-one-coordinate-quotient-geometry.md) records
the gap, intermediate target, relevance, redundancy check, and test. Reread
the [official statement](https://proximityprize.org/); the unread ABF26
correspondence remains a separate qualification. Existing work is preserved.

[L005](../lemmas/L005-one-coordinate-sharp-error.md) proves the exact error
2/q for 1/n<=delta<2/n and 1<=k<=n-3. Thus the prescribed 2^-128 budget is
met on this cell exactly when q>=2^129. At length 16 this improves the
previous counts 3,4,6,8 for the four listed rates to the sharp count two.
It does not extend L004's wider sufficient interval or determine the maximal
safe radius. The proof uses the root bound and elementary quotient geometry;
L004 is a comparison, not a mathematical input. The new DAG row has no lemma
inputs, and all previous rows are retained.

Outcome: ADVANCE; STATUS remains IN_PROGRESS, with exploration turns reset
to zero. The reason for the next direction is the successful removal of
global counting slack by realizable affine-line intersections. Two-coordinate
error subspaces are the next geometric test; the sole current action is in
PROGRESS.md. No complete challenge candidate is claimed.

Validation: `python3 scripts/one-coordinate/check.py` passed 528,620 input-pair
classes across five parameter sets using direct polynomial membership. This
includes characteristic two and an excluded codimension-two example with
four bad challenges. L005 supplies an algebraic check of that counterexample.
The proof was reviewed for zero quotient directions, lines through the origin,
both support sizes, same-support failure, attainment, and the strict endpoint.

`python3 ../scripts/docs/check_structure.py --problem reed-solomon-mca`
passed with 6 nodes and 2 edges; `git diff --check -- .` also passed.
These checks validate documentation structure, not mathematical correctness
or the paper-to-model correspondence. Mathlib coverage remains not checked.
