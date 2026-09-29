# 2026-09-27 — Vanishing in the next fibre-degree range

STEP_ID: 2026-09-27-hodge-029-fibre-degree-three-ideal-vanishing.
Outcome: ADVANCE. Kind: RESEARCH. Classification: POTENTIALLY_NEW.

Reused the exact saved target's unchanged SPECIALIZE
[assessment](../drafts/literature/2026-09-27-higher-fibre-degree-ideal-cohomology.md).
Read the shared and local rules, whole overview and DAG, inspected
existing changes and relevant prior failures, and preserved unfinished
work. No fresh source search was needed for this approved specialization.
The calculation addresses the positive ideal-cohomology group in the
sufficient summand-recovery test for the ordering 0<m<n.

[L021](../lemmas/L021-fibre-degree-three-positive-ideal-vanishing.md)
proves vanishing for every positive r when the original ample L has
L.F=3. Translation and inversion preserving C reduce to two numerical
forms. The proof checks both resolved fibre components, complete global
section spaces, and the actual two-projection products. Their rank
is exactly the normalization dimension minus its three gluing conditions.
The odd-r calculation retains the coupled lower Weierstrass terms.
The [working draft](../drafts/2026-09-27-higher-fibre-degree-restriction-test.md)
preserves the checkpoints and the limits of this completion.

This reaches the required starting degree r=1 and proves the entire
positive tail in fibre degree three. It is a partial answer to the
saved target: L.F>=4 remains uncomputed. L020's degree-two nonzero
group remains unchanged. No actual inclusion obstruction, transverse
union lift or new cycle has been obtained. The 21-dimensional span,
three-versus-four direction gap and universal Hodge gap are unchanged;
STATUS remains IN_PROGRESS and there is no complete candidate.

The translation, vanishing and Riemann--Roch tools are imported known
results. The actual restriction calculation was not matched by the
saved source assessment; POTENTIALLY_NEW does not certify originality.
The nearest complete normal-generation theorems do not identify the
two projection spaces and global descent image. Mathlib coverage is
not checked. The DAG adds only L021's genuine inputs, and the overview
records this new partial parameter range without a revised lifting claim.

This mathematical input resets exploration turns used to zero. Further
numerical classification has lower priority than checking whether its
cohomological condition is needed for recovery. L018 first recovers a
lift of a direct sum. The Atiyah-obstruction criterion already cited in
L012 is a lead for recovering existence of a summand lift without
lifting its particular inclusion. Registered that distinct question as
[REVIEW_REQUIRED](../drafts/literature/2026-09-27-direct-summand-obstruction-recovery.md).
No theorem or calculation for the new target was derived. Its separate
source review must precede any revised union argument; the existing
degree restrictions remain in force meanwhile.

The new arithmetic checker passed five actual product matrices over
F_43: both forms in r=1,2 and the first form in r=3. Their image ranks
are respectively 83,75,341,309,775, equal to the corresponding
three-condition descent dimensions. It retains both polynomial
relations' lower terms. These finite checks support the formulas;
the proof supplies the all-r complex assertion and geometric checks.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 22 nodes and 51 edges. The shared literature validator
accepted the unchanged prior SPECIALIZE assessment, research
classification and exact new REVIEW_REQUIRED target. Reviewed the
new mathematical inputs in the DAG; downstream union recovery is
motivation, not a new input to L021. `git diff --check -- .` passed.
These structural and arithmetic checks are not verification of the
Hodge conjecture or a certification of originality.
