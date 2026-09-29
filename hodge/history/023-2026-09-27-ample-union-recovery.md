# 2026-09-27 — High-degree complete-intersection union recovery

STEP_ID: 2026-09-27-hodge-023-ample-union-recovery. Outcome: NEGATIVE.
Kind: RESEARCH. Classification: POTENTIALLY_NEW.

Reused the exact saved SPECIALIZE [assessment](../drafts/literature/2026-09-27-ample-complete-intersection-union.md)
without changing it. Read the shared and local instructions, complete
overview, DAG, existing changes and the relevant singular-support and
ideal-reconstruction proofs. Preserved prior unfinished work; saved
[interim reasoning](../drafts/2026-09-27-ample-union-lifting-test.md)
before completing the recovery.

[L018](../lemmas/L018-high-degree-complete-intersection-unions-retain-obstruction.md)
rules out a transverse lift whenever H^1(C,O_C(nH)) vanishes. Serre
vanishing and Bertini make this a nonempty high-degree regime with
smooth B and smooth ample intersection D. The proof recovers the
forgotten extension and summand by two global Ext vanishings, then
recovers the embedded ideal without dropping the three old singular
points. With one further positive ideal-cohomology vanishing, both
lifting implications hold and the kernel is exactly V_D.

The known basic-double-link construction, duality and Bertini tools
are imported; the relative recovery calculation was not matched in
the checked literature. POTENTIALLY_NEW records that limited source
comparison, not certified originality. Mathlib coverage is not checked.
This is an informative negative result for the specified regime,
not a resolution of the full existential target or a new Hodge class.

The achieved kernel remains three-dimensional against four required,
and the 21-dimensional span reaches no additional surface. The degree
threshold is qualitative: smaller n with nonzero H^1(C,O_C(nH)) are
not excluded. Stop the vanishing regime, and screen that remaining
cohomology through the new REVIEW_REQUIRED
[assessment](../drafts/literature/2026-09-27-positive-degree-normalization-cohomology.md).
No calculation on that new target was made. The informative negative
result resets the exploration count to zero. No complete candidate
exists and STATUS remains IN_PROGRESS.

Updated the narrative overview and added only the genuine inputs of
L018 to the ID-only DAG; preserved all older nodes and branches. The
mathematical checks are the exact cohomology sequences, derived
restriction for extension lifting, and flatness/determinant recovery
written out in the proof. No numerical experiment or new script is
needed for this step.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 19 nodes and 44 edges. The shared literature validator
accepted RESEARCH / POTENTIALLY_NEW against the unchanged prior
SPECIALIZE assessment and the exact new REVIEW_REQUIRED target. The
scoped whitespace check passed. These are process and documentation
checks, not independent verification of the mathematical proof.
