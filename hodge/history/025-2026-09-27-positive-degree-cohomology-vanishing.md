# 2026-09-27 — All-positive-degree vanishing closes the tested unions

STEP_ID: 2026-09-27-hodge-025-positive-degree-cohomology-vanishing.
Outcome: NEGATIVE. Kind: RESEARCH. Classification: POTENTIALLY_NEW.

Reused the unchanged, previously saved SPECIALIZE
[assessment](../drafts/literature/2026-09-27-positive-degree-normalization-cohomology.md).
Read the shared and local instructions, entire overview and DAG,
inspected existing changes, and preserved all unfinished work. The
approved question was whether the positive support cohomology vanished
for every n>0 with the fixed ample product polarization. Large-degree
vanishing was already known and would not have met this threshold.

[L019](../lemmas/L019-positive-degree-cubic-support-vanishing.md) proves
the required vanishing for every n>0. A visible constant-coordinate
section and the Picard-rank-four input give a rational divisor basis.
Intersections with its elliptic multiples give a uniform inequality:
no irreducible (-2)-curve has fibre degree greater than one, and
L^2>2L.F for every ample L. Thus L-F is nef and big. The normalization
calculation checks the full canonical correction and independently
prescribes the six values above the three double points, retaining
the length-two tangencies of both type-III fibres. This treats the
actual product bundle without identifying its two factors.

The normalization sequence, Kawamata--Viehweg vanishing and gluing tools
are imported from the inspected sources. The full lattice and gluing
specialization was not matched by that bounded review; POTENTIALLY_NEW
does not certify originality. Mathlib coverage remains not checked.
The full proof is in the lemma; [the working draft](../drafts/2026-09-27-positive-degree-cohomology-test.md)
preserves the initially incomplete argument and its resolution.

Through L018, every admissible smooth union with m>n>0 now recovers C
from any first-order lift. This supplies new evidence closing the
former small-degree exception, rather than repeating the high-degree
stop. Its permitted directions are contained in the three-dimensional
V_D, against four RM directions required. Equality retains the separate
ideal-cohomology hypothesis. No additional surface, transverse lift or
algebraic Hodge class was obtained; the 21-dimensional span and universal
gap remain unchanged. STATUS remains IN_PROGRESS, with no complete
candidate. Exploration turns used reset to zero on this informative
negative result.

The reason for the next direction is the explicit degree inequality
in L018's second recovery step: the reversed ordering requires positive
ideal cohomology, a different group from the support cohomology settled
here. Registered the exact new target as
[REVIEW_REQUIRED](../drafts/literature/2026-09-27-positive-ideal-cohomology.md).
No calculation or source search on that new target was performed. A
nonzero group would only indicate a possible failure of recovery;
actual obstruction cancellation would remain unproved.

Updated the narrative overview, checkpoint and prior attempt's scope.
The new DAG row records only L008's geometric input and L018's recovery
implication. Earlier lemmas, assessments, scripts and inactive branches
are preserved. Exact rational checks passed for the determinant -7,
the orthogonal vector's square -7/2, and the section identities for
integers -25 through 25. The written generic-fibre argument and uniform
inequality prove the assertions for all integers; the finite check is
only supporting algebra.

Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 20 nodes and 46 edges. The literature validator accepted
the saved SPECIALIZE target, research classification and exact new
REVIEW_REQUIRED target. `git diff --check -- .` passed. The direct
mathematical inputs of the new DAG row were reviewed. These checks
validate the records and supporting algebra, not the universal Hodge
conjecture or the correctness of every prior notebook lemma.
