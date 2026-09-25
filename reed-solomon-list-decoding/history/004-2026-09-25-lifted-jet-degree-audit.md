# 2026-09-25 — Nonsingular lifted-jet degree review

Read the shared rules, local goal/checkpoint, complete overview, DAG,
existing changes, and relevant prior work. All unfinished work was preserved.
The prize page and September 5 version of TR26-169 were inspected; the
pinned source qualifications remain in place.

The [focused audit](../drafts/2026-09-25-lifted-jet-degree-audit.md) passes its
test. [L003](../lemmas/L003-linear-degree-lifted-jets.md) proves an explicit
linear numerator and residual degree estimate for a nonsingular Taylor
chart, improving the quadratic estimate in the reviewed local passage.
Simultaneous numerator/denominator accounting is the substantive input.
The chart still requires H!=0 and the base coefficient equation.

This is ADVANCE, with exploration turns 0/3, as a local input toward the
cover required by L002. It supplies no new unconditional safe radius.
The local degree calculation is no longer the missing step; degree control
after taking the graph closure is now the relevant direction, with singular
coverage still outstanding. The full threshold, field scope, and ABF
comparison remain open. STATUS stays IN_PROGRESS; no complete candidate
for the challenge appeared.

Validation: the general induction and residual equivalence were reviewed,
and `python3 scripts/lifted-jets/verify.py` passed five exact symbolic charts
and 120 finite-field samples. The
[saved results](../scripts/lifted-jets/results.json) are supporting checks,
not the proof. L003 uses no earlier local lemma as a mathematical input,
so its DAG row has no edge. The required
`python3 ../scripts/docs/check_structure.py --problem reed-solomon-list-decoding`
passed; it checks documentation structure, not mathematical correctness.
