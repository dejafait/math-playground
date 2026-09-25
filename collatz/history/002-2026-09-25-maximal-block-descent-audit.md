# 2026-09-25 — Maximal odd-even block descent test

Step `collatz-2026-09-25-002-maximal-block-descent` concluded NEGATIVE. The
source target was rechecked and is unchanged. Existing local work, including
the inactive fixed-window branch, was preserved; other notebooks were left
alone. The [saved audit](../drafts/2026-09-25-maximal-block-descent-audit.md)
records the gap, intermediate target, and discriminating test.

[L002](../lemmas/L002-maximal-odd-even-block-descent.md) proves the exact
maximal-block formula and descent inequality. The necessary compensation
threshold b>a log_2(3/2) is not forced: every positive pair (a,b) occurs
infinitely often, including b=1 for arbitrarily large a. The explicit family
16t+11 has endpoint 18t+13 and hence positive change 2t+2 instead of the
required negative change. The [failed attempt](../ATTEMPTS/002-first-maximal-block-descent.md)
records why neither completing the first even run nor adding a finite
exception set fixes this route.

This narrows a sufficient strategy without resolving universal eventual
descent. Single-block feasibility says nothing about how later blocks
compensate. The reason to examine successive growing blocks is that their
arithmetic compatibility determines whether a bounded number of complete
blocks could repair this failure. The (2,1) affine map gives a concrete test,
without assuming independence or an infinite positive orbit. No complete
candidate exists. Consecutive exploration turns without an advance or
informative negative remain zero.

Validation: `python3 scripts/maximal-block/check_block.py` passed 21,482
parameter cases and 703,428 shortcut transitions; the
[exact output](../scripts/maximal-block/result.json) is retained. This is an
algebra and indexing check, not a density or convergence argument. L002 is
proved directly, with L001 used only for historical comparison; its new DAG
row has no inputs. Mathlib coverage is explicitly not checked.

Documentation validation: `python3 ../scripts/docs/check_structure.py --problem collatz`
passed with two nodes, no edges, complete lemma coverage, valid local links,
and compact overviews. This validates storage structure, not the proof.
