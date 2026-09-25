# 2026-09-25 — A second even-run length breaks inverse uniqueness

Step `collatz-2026-09-25-010-variable-even-run-branching` concluded
NEGATIVE. The [saved test](../drafts/2026-09-25-variable-even-run-branching.md)
states the main gap, intermediate target, downstream use, and decision
threshold. The primary [statement](https://mathprize.net/posts/collatz-conjecture/)
was rechecked and retains the recorded universal positive-integer target.
The active notebook had no unfinished changes; edits elsewhere were
preserved, and this step edited only Collatz files.

[L010](../lemmas/L010-variable-even-run-inverse-branching.md) proves that
adjoining (1,2) changes the allowed endpoint residues to all nonzero
classes modulo 3. Three inverse branches can then extend together on
infinite positive residue classes. It also proves the sharp depth-two
history bound five, with an explicit endpoint 661, exceeding the prior
bound three. The new exact congruences replace the old disjointness for
this alphabet; they do not invalidate the smaller-alphabet result.

The unique-decoder threshold fails, and its direct extension is stopped
in [Attempt 008](../ATTEMPTS/008-variable-even-run-unique-decoder.md).
The actual missing bound still concerns arbitrary future depth at each
fixed start; a depth-two count, unique decoding, or a density estimate
does not supply it. No complete candidate or infinite-branching claim
appeared. This single bounded test is an informative negative result,
leaving zero consecutive exploration turns without ADVANCE/NEGATIVE.

The reason for the next direction is that unrestricted incoming histories
can already have descended below their own starting values. Restricting
to histories satisfying the actual non-descent condition offers a distinct
test of which branching is relevant to a potential exceptional orbit.
The concrete bounded test is recorded only in PROGRESS.md.

Validation: `python3 scripts/variable-even-inverse/check_branches.py`
passed 729 odd endpoints over a complete period modulo 1458 against
independent forward iteration of 5,180 starts up to 10,359. The
[output](../scripts/variable-even-inverse/result.json) records all
extendibility classes, the sharp count, five positive-family lifts and
the fixed point. Mathematical review checked positive odd domains, exact
maximal runs, the changed endpoint union, both directions of each
congruence, and every valuation case in the bound five. L002 is the sole
earlier mathematical input in the new DAG row; Mathlib is not checked.

Documentation validation: `python3 ../scripts/docs/check_structure.py --problem collatz`
passed with ten nodes, eight edges, complete file coverage, valid local
links, and compact overviews. `git diff --check -- .` also passed.
Structural validation does not establish mathematical correctness.
