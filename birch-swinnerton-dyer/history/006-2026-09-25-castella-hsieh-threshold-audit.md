# 2026-09-25 — Castella--Hsieh nonvanishing and the remaining Kummer defect

Preserved the existing changes and all inactive branches. Rechecked
Wiles's official rank statement; the scope is unchanged. The
[saved test](../drafts/2026-09-25-castella-hsieh-threshold-audit.md)
records the gap, threshold, redundancy comparison, and continuation test.

The [2022 source audit](../foundations/07-castella-hsieh-nonvanishing.md)
checks the published Theorems A/B, their Section 5 proofs, and the
added finite-Sha hypothesis before Theorem 5.5. Nonvanishing gives
Selmer dimension two, not a rational Kummer identification; neither
nonvanishing nor Kummer membership is supplied from m(E) = 2 alone.
This differs from the earlier 2016 audit: there is now an applicable
upper-bound theorem, but the proposed direct import still fails.

[L006](../lemmas/L006-generalised-kato-kummer-certificate.md) proves the
useful conditional consequence: a nonzero Kummer class in this setting
closes rank two without L004's cyclotomic coefficient. The theorem's
unconditional-in-nonvanishing output is r + dim V_p Sha = 2. With
Theorem B's extra positive-rank premise, only 1 <= r <= 2 follows;
the required lower bound remains r >= 2. No actual rank-one curve
with nonzero V_p Sha is asserted. The new DAG row has only L005 as
a direct lemma input; the imported upper bound lives in foundations.

Decision: stop the direct nonvanishing-to-points import, preserved in
[the failed attempt](../ATTEMPTS/004-analytic-rank-to-kato-kummer-import.md).
The two audits have isolated Kummer membership as a separate obstacle.
This motivates testing the actual diagonal-cycle specialization map
at weights (2,1,1), rather than another dimension-only criterion.
Nonvanishing, auxiliary choices, and the universal analytic comparison
remain unresolved; the restricted certificate is not a BSD candidate.

Mathematical review checked the direction of both Theorem A implications,
the strict local condition, the extra rank premise of Theorem B,
finite p-primary Sha in Section 5.7, and the distinction between theta
and cyclotomic variables. The new proof uses finite Sha only as a
conclusion after Kummer membership. No numerical computation or Mathlib
lookup was needed. The documentation checker initially caught an
overlong overview; the assembly was shortened without deleting branches.
`python3 ../scripts/docs/check_structure.py --problem birch-swinnerton-dyer`
then passed with six nodes and five direct edges, and
`git diff --check -- .` passed. The checker ran with bytecode writing
disabled, keeping shared infrastructure unchanged. These checks concern
structure and whitespace, not arithmetic correctness.

Completed step BSD-2026-09-25-006-castella-hsieh-threshold-audit is NEGATIVE:
new source evidence changes the direct-import decision. STATUS remains
IN_PROGRESS. Exploration turns without an advance or informative
negative result remain 0 of 3.
