# 2026-09-27 — An exact positive ideal-cohomology exception

STEP_ID: 2026-09-27-hodge-027-fibre-degree-two-ideal-cohomology.
Outcome: ADVANCE. Kind: RESEARCH. Classification: POTENTIALLY_NEW.

Reused the unchanged, ready SPECIALIZE
[assessment](../drafts/literature/2026-09-27-positive-ideal-cohomology.md)
for the exact saved target. Read the shared and local instructions,
whole overview and DAG, inspected existing changes, and preserved prior
and unfinished work. The gap addressed was the positive ideal-cohomology
group that can prevent L018's sufficient summand recovery when 0<m<n.
No deformation of a new representative was calculated in this turn.

[L020](../lemmas/L020-fibre-degree-two-positive-ideal-cohomology.md)
proves that every original ample L with L.F=2 has
h^1(I_C(H))=L^2-4>=4, while all r>=2 vanish. The original class is
transported by an automorphism preserving C. The explicit section spaces
on S and W and the actual two-projection products give the exact image;
the normalization count retains all three gluing conditions. This is
an exact exceptional degree and a full tail in the stated range, not
an inference from total dimensions or eventual Serre vanishing alone.

The result is partial because the original L was numerically unspecified.
No answer is asserted for L.F>=3. The positive group makes the possible
failure of sufficient recovery real at n-m=1 in fibre degree two.
It does not compute the obstruction of an actual inclusion, cancel the
rank-one transverse obstruction, or produce a transverse cycle. The
m>n>0 exclusion is retained. The 21-dimensional cycle span and the set
of surfaces covered are unchanged, and the universal Hodge gap remains
open. STATUS stays IN_PROGRESS without a complete candidate.

The supporting translation theorem was read in Schuett--Shioda,
[arXiv:0907.0298v3, section 7.6, pp. 33--34](https://arxiv.org/pdf/0907.0298v3#page=33).
It is imported, as are the named vanishing and Riemann--Roch inputs.
The actual restriction calculation was not matched by the saved source
comparison; POTENTIALLY_NEW does not certify originality. Mathlib
coverage is not checked. The prior assessment itself was not rewritten.

The [working draft](../drafts/2026-09-27-positive-ideal-restriction-test.md)
preserves the intermediate reasoning and the bounded scope of its
completion. The new DAG row uses L008's correspondence geometry and
L019's divisor and normalization results. Its mathematical inputs were
reviewed; L018 is downstream motivation, not a premise of this rank
calculation. The overview and sole current checkpoint record the result.

The source assessment and this calculation used two turns; the new
mathematical input resets exploration turns used to zero. The remaining
numerical range is a concrete unfinished part of the same cohomological
question. Registered its exact target as
[REVIEW_REQUIRED](../drafts/literature/2026-09-27-higher-fibre-degree-ideal-cohomology.md),
with no calculation or source search on that new target. Its review must
precede any further specialization. No stopped representative is reopened.

The supporting coefficient checker passed seven (b,r) cases over F_43,
including r=1,2,3 and parameter degrees crossing seven. It also checked
the individual extreme-coefficient relations. These finite computations
do not verify the geometry or replace the all-degree complex proof.
Validation: `python3 ../scripts/docs/check_structure.py --problem hodge`
passed with 21 nodes and 48 edges. The shared assessment parser accepted
the prior SPECIALIZE target and the exact new REVIEW_REQUIRED target;
the research outcome and classification fields were checked. The prior
assessment was preserved. `git diff --check -- .` passed. These are
record and arithmetic checks, not a verification of the Hodge conjecture.
