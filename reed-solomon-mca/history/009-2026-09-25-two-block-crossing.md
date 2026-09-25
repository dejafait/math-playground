# 009 — 2026-09-25 — Ten challenges and a specific model crossing

Completed one bounded seven-challenge test at support cutoff twelve.
The [assessment](../drafts/2026-09-25-four-error-seven-challenge-test.md)
records the gap, continuation test, saved unfinished reasoning, and result.
The [official statement](https://proximityprize.org/) was reread; the
preliminary target and unresolved qualifications are unchanged. Existing
unfinished work and inactive branches were preserved.

A deterministic search found seven challenges at trial 47125, then its
support pattern suggested the simpler proof in
[L008](../lemmas/L008-two-block-witness-and-model-crossing.md). Two
coordinate blocks give 2r+2 bad parameters whenever n-k=2r and k>=2,
with full same-support failure over the stated field. Ten parameters
are therefore attained at cutoff twelve on the length-16, dimension-8
code over every F_(17^s). The count is a lower bound, not a sharp-error
assertion.

At q=17^32, ten exceeds the allowable count six. Together with L007
and monotonicity, this proves the exact safe set [0,1/4) for this frozen
model: largest safe grid radius 3/16, supremum 1/4, no attained real
maximum. The result is partial; STATUS remains IN_PROGRESS and no
complete challenge candidate is present. Outcome: ADVANCE, with zero
consecutive exploration turns.

The main general sharp-error gap and ABF26 correspondence remain.
The new construction gives only 130 at n=256,k=128,r=64, insufficient
for that example's q=257^32 budget. At length 16 and dimension 8 the
four-omission bounds are now 10/q and 69/q. The reason for the next
direction is that q=97^20 permits fifteen parameters on a smooth
order-16 subgroup, so a sixteen-parameter witness would decide a cell
where the new two-block construction alone does not. The current
next action is recorded only in PROGRESS.md.

The new DAG row uses L007 only for the safe side of the model crossing.
The construction and monotonicity are proved directly; L004 is a bound
comparison, not a mathematical input. Mathlib coverage is not checked,
and the supporting pinned ArkLib definition names and links are retained.

The auxiliary script checks the original event on every claimed support
of the seven-parameter discovery, the explicit ten witnesses, and all
17 parameters and 2517 admissible supports for the final pair over F_17.
It finds exactly {1,...,10} for that pair and checks exact budget
comparisons. The extension-field lower bound is algebraic; no finite
enumeration is presented as a uniform upper bound or a grand resolution.

Validation passed: `python3 scripts/four-error-search/check.py` and
`python3 ../scripts/docs/check_structure.py --problem reed-solomon-mca`.
The latter ran with bytecode writes disabled and reported 9 nodes,
3 edges, valid links, and compact overviews. `git diff --check -- .`
also passed. The generated search executable was removed; its source
and discovery output remain. Structural checks do not verify the proof
or identify the frozen event with ABF26.
