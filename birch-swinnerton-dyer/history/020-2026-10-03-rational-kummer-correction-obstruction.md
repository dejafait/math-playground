# 2026-10-03 — Rational corrections cannot remove the auxiliary p-singular value

Completed the exact preapproved correction test with the unchanged
SPECIALIZE assessment. No new literature search was performed; the
already inspected Kim sections and theorem statements were retrieved
only to apply their coefficient, local-condition and normalization
conventions precisely.

[L014](../lemmas/L014-rational-kummer-corrections-of-kato-systems.md)
records the result. Global rational Kummer corrections are finite at
p, so they leave the singular quotient unchanged. Under E(Q_p)[p] = 0,
Kim's torsion reciprocity makes the assumed nonzero mod-p Kurihara value
an obstruction already at the selected two-prime component. For the
complete ordinary family, subtracting the preserved finite-singular
relations and transverse conditions puts the correction in the zero
classical system module of Theorem 2.5(1). This is an applicability
argument for known results, not a new theorem beyond the checked
literature.

The correction mechanism stops in
[ATTEMPTS/016](../ATTEMPTS/016-rational-kummer-correction-of-kato-family.md).
The required lower bound r >= 2 is unchanged: no rational class or
rational determinant is produced. Nonvanishing at a minimal two-prime
index is an explicit extra premise and is not inferred from m(E) = 2.
L013 remains a formal model with no asserted full arithmetic realization.
STATUS remains IN_PROGRESS and no candidate appears.

The changed direction retains finiteness at p but adds a distinguished
relaxed auxiliary prime and different rank-zero relations. It avoids
repeating the same classical-system correction and has a primary lead
already recorded in the previous assessment. Its exact arithmetic
transfer and local hypotheses require assessment; the new
[REVIEW_REQUIRED file](../drafts/literature/2026-10-03-rank-zero-extra-relaxed-prime.md)
records that source need. Even a nonzero p-finite family would leave
rational Kummer membership as a separate requirement.

Step BSD-2026-10-03-020-rational-kummer-correction-obstruction has outcome
NEGATIVE, kind RESEARCH and classification REPRODUCTION. This informative
negative uses no mathematical exploration budget; the counter remains
0 of 3. The named theorems are imported by citation, and the correction
applicability is reproduced. Existing unfinished work is retained.

Validation: `python3 ../scripts/docs/check_structure.py --problem birch-swinnerton-dyer`
passed with 14 nodes, 11 unique edges, an acyclic graph and valid local
links. The literature validator accepted the unchanged prior SPECIALIZE
assessment, exact covered target, RESEARCH/REPRODUCTION classification
and the new REVIEW_REQUIRED target. The dependency row for L014 has no
lemma inputs: its arithmetic theorems are cited directly, and L013 is
only the contrasting unresolved model. The proof audit checked the
coefficient reduction in (3), every local condition on the difference,
the distinction between ordinary and completed systems, and the t = 0
reduction of the actual singular quotient. No numerical or model test
was needed. All 89 entry files are retained; only DAG.md, PROOF.md and
PROGRESS.md are changed among them, and the prior assessment, foundations,
mathematical scripts and existing lemma files are unchanged. The local
diff whitespace check passed. Shared infrastructure and other notebooks
were not edited.
