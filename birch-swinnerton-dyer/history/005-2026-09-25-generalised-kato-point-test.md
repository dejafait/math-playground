# 2026-09-25 — Generalised Kato classes and the rational-point threshold

Preserved the existing edits and inactive branches. Read the overview
and DAG before the relevant proofs, compared the proposed input with
both recorded failures, and rechecked the official Clay statement with
unchanged rank scope. The [saved test](../drafts/2026-09-25-generalised-kato-point-test.md)
records the gap, point threshold, and continuation criterion.

The [2016 source audit](../foundations/06-generalised-kato-scope.md)
distinguishes proved Theorem 3.1 and Corollary 3.6 from Conjectures 3.2
and 3.12. In particular, twisted-Selmer independence under an additional
triple-product nonvanishing condition does not supply L004's rational
points from m(E) = 2. Section 4.5.3 already assumes a Mordell--Weil
basis and predicts at most one line from the four stabilisations.
The achieved rational lower bound from the checked construction is
therefore still no improvement on r >= 0; the required bound is r >= 2.

[L005](../lemmas/L005-strict-kummer-rank-two-threshold.md) proves that
one nonzero strict class in the rational Kummer image would suffice
for that lower bound. It states the V_p Sha quotient and proves the
local-logarithm rank calculation using completed local points. The
conditional coefficient conclusion uses L004 directly; this is the
only new DAG edge. Neither conjectural point membership nor finite
Sha enters the proof as an established premise.

Decision: stop the direct two-point import, as recorded in
[the failed attempt](../ATTEMPTS/003-generalised-kato-independent-point-import.md).
The remaining useful test concerns one class's Kummer membership,
strictness, and nonvanishing. [Castella--Hsieh's later nonvanishing paper](https://arxiv.org/abs/1809.09066)
is a concrete lead for this requirement; its theorem hypotheses have
not been audited or imported here. Uniform certificate production,
the cyclotomic coefficient, and the universal analytic comparison
remain unresolved.

The mathematical review checked torsion in the local logarithm kernel,
completion before local tensoring, inverse-limit Kummer exactness,
the r = 0 and r = 1 boundary cases, and basis-change invariance of the
single line. Published HTML formulas and PDF text agree. No numerical
elliptic-curve computation or Mathlib search was required.

The documentation checker
`python3 ../scripts/docs/check_structure.py --problem birch-swinnerton-dyer`
passed with five nodes and four direct edges; `git diff --check -- .`
passed. Bytecode writing was disabled to keep shared infrastructure
unchanged. These checks validate structure, not arithmetic correctness.

Completed step BSD-2026-09-25-005-generalised-kato-point-test is NEGATIVE:
new source evidence changes the point-import decision. L005 records
a conditional threshold, not production of the missing arithmetic
input or a candidate BSD proof. STATUS remains IN_PROGRESS; exploration
turns without an advance or informative negative result remain 0 of 3.
