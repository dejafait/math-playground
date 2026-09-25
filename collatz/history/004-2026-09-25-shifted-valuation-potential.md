# 2026-09-25 — Shifted-valuation potential obstruction

Step `collatz-2026-09-25-004-shifted-valuation-potential` concluded NEGATIVE.
The [saved test](../drafts/2026-09-25-shifted-valuation-potential.md) records
the main gap, intermediate target, possible termination argument, and sign
test. The primary [source](https://mathprize.net/posts/collatz-conjecture/)
was rechecked and retains the universal positive-integer target. Existing
changes were preserved, and only this notebook was edited.

[L004](../lemmas/L004-shifted-valuation-potential-obstruction.md) proves
that an unbounded correction depending only on v_2(n+5) cannot decrease
at every complete block: arbitrarily large growing (3,1) blocks preserve
that valuation. Their potential increment is at least log(5/3)>0 instead
of the required negative value. Other growing (3,1) blocks increase the
valuation by arbitrarily large amounts. The
[failed attempt](../ATTEMPTS/004-shifted-valuation-potential.md) closes
this route, including arbitrary functions of that single valuation and
finite exception sets. Unlike the finite-residue obstructions, this new
result directly tests the unbounded correction proposed in the checkpoint.

The main eventual-descent gap remains. A reason to examine mixed growing
words is that L003's starting-size bound treats only one repeated block
type, while L004 defeats a valuation correction once another growing type
is admitted. A start-size bound growing uniformly with word length would
exclude infinite growth confined to the chosen alphabet; it would leave
other block types and later compensation unresolved. No such bound is
claimed here. No complete candidate exists, and the consecutive exploration
count remains zero after this informative negative result.

Validation: `python3 scripts/shifted-valuation/check_potential.py` passed
8,192 odd starts in complete residue periods, 568 parameterized witnesses,
and 35,038 shortcut transitions; the
[output](../scripts/shifted-valuation/result.json) retains the evidence.
These are exact block, valuation, and ratio checks, not convergence tests.
The proof was reviewed for maximality of the block, both valuations, sign
of each ratio bound, and arbitrarily large witnesses. L004 uses only L002
as a prior mathematical input; L003 motivates the test but is not used in
its proof. Mathlib coverage is explicitly not checked.

Documentation validation: `python3 ../scripts/docs/check_structure.py --problem collatz`
passed with four nodes, two edges, complete lemma coverage, valid local
links, and compact overviews. The added DAG row contains only the genuine
input L002; structural validation does not check mathematical correctness.
