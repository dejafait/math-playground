# 2026-09-25 — Consecutive growing-block compatibility

Step `collatz-2026-09-25-003-consecutive-growing-blocks` concluded NEGATIVE.
The primary source was rechecked and retains the universal positive-integer
target. Existing local changes and inactive branches were preserved; other
notebooks and shared infrastructure were left alone. The
[saved test](../drafts/2026-09-25-consecutive-growing-blocks.md) records the
gap, proposed intermediate target, downstream use, and stop test.

[L003](../lemmas/L003-consecutive-growing-blocks.md) proves the exact residue
condition for arbitrarily many consecutive growing (2,1) blocks, including
absence of descent inside them. Its q-scaled witnesses keep all endpoints in
one residue modulo q, with potential change greater than j log(9/8)>0
instead of the required negative change. The
[failed attempt](../ATTEMPTS/003-bounded-complete-block-descent.md) closes
the proposed fixed-block repair, including finite residue corrections at
endpoints. This is a new arithmetic compatibility result, not a repetition
of single-block feasibility, and establishes no universal convergence bound.

For each fixed positive start the repeated pattern has an exact finite
length. Its least possible starting size grows as 2^(3K+1)-5; this is a
size-dependent restriction, not forced compensation. The universal
eventual-descent gap remains. The loss of three valuation units in n+5
per growing block gives a specific reason to examine an unbounded arithmetic
correction next; other blocks' valuation increases remain uncontrolled.
No complete candidate exists. Consecutive exploration turns without an
advance or informative negative remain zero.

Validation: `python3 scripts/consecutive-blocks/check_prefix.py` passed
37,448 odd starts in full residue periods, 2,048 parameterized witnesses,
and 384,036 shortcut transitions. Its
[output](../scripts/consecutive-blocks/result.json) records the exact checks.
These are arithmetic and indexing checks, including the exit from each
predicted maximal repeated prefix, rather than convergence evidence.
L003 uses L002's exact block description; the new DAG row contains that
single genuine input. L001 is only a historical comparison. Mathlib coverage
is explicitly not checked.

Documentation validation: `python3 ../scripts/docs/check_structure.py --problem collatz`
passed with three nodes, one edge, complete lemma coverage, valid local
links, and compact overviews. The hypotheses, both directions of the residue
criterion, and the single new dependency were also reviewed mathematically;
the structure checker itself does not verify proofs.
