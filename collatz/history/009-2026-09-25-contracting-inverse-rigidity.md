# 2026-09-25 — Backward rigidity with a contracting block

Step `collatz-2026-09-25-009-contracting-inverse-rigidity` concluded
ADVANCE for an intermediate arithmetic constraint. The
[saved test](../drafts/2026-09-25-contracting-inverse-branch.md) records
the gap, relevance and continuation threshold. The primary
[statement](https://mathprize.net/posts/collatz-conjecture/) was rechecked
and retains the recorded universal positive-integer target. Existing
unfinished work and inactive branches were preserved; edits were confined
to this notebook.

[L009](../lemmas/L009-contracting-block-inverse-rigidity.md) proves that
adding (1,1) to the earlier two-letter alphabet preserves uniqueness of
the extendible inverse branch. It gives exact congruences, a valuation
decoder and a sharp bound of three histories at any endpoint at each
depth. This extends the arithmetic constraint to histories containing
both growth and contraction. It also retains the fixed point 1 and
exhibits inverse growth on an extendible branch greater than 1.

The proposed intermediate uniqueness threshold is met. The actual
forward escape or universal eventual-descent bound is not: the inverse
map no longer decreases in size, and bounded multiplicity alone gives
no time or least-start bound. No complete candidate appeared. The proof
still fixes every even-run length to 1, so testing the effect of allowing
a second even-run length is a concrete gate to broader use. This does not
reopen the stopped density-only or valuation-potential inferences.
Consecutive exploration turns without an advance or informative negative
remain zero.

Validation: `python3 scripts/contracting-inverse/check_branches.py` passed
81 odd endpoints over a complete period modulo 162 against independent
forward iteration of 143 starts, then 6,558 constructed endpoints from
3,279 words and 42,648 backward history levels. The
[output](../scripts/contracting-inverse/result.json) checks the sharp
depth-two example and fixed-point exception. Mathematical review checked
positivity, parity, exact maximal runs, both directions of the congruences,
the valuation boundary cases, induction on depth and the loss of inverse
contraction. L002 is the sole earlier mathematical input; the new DAG row
records it. Mathlib coverage is not checked.

Documentation validation: `python3 ../scripts/docs/check_structure.py --problem collatz`
passed with nine nodes, seven edges, complete lemma coverage, valid local
links and compact overviews. `git diff --check -- .` also passed.
Structural checks do not establish mathematical correctness.
