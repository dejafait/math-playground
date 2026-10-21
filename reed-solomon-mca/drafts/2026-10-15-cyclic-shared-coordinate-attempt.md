# Cyclic shared-coordinate pass — step 227

2026-10-15. RESEARCH / proof_attempt under the unchanged EXPLORE
assessment `drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`.

The approved target is: Determine whether L087's full alternating moment
system has zero kernel for every bijective H-labeling.
The main target gap remains exclusion of sixteen actual errors; this
family-specific question leaves arbitrary-family and challenge gaps open.

Saved before completing the calculation: audited L089 reconstructs all
candidate intersection lines, and supplies three shared-coordinate gates
for each consecutive triangle. The proposed intermediate target is to
simplify those gates, keeping every denominator justified by distinct
labels, and obtain a restrictive label-only condition usable in a uniform
zero-kernel proof. Essential inputs are audited L089 and its L010/L087/L088
conventions; no actual errors, chart or parameters are assumed.

For the third gate at t, put a=h(t-1), b=h(t), c=h(t+4),
d=h(t+6), e=h(t+8), f=h(t+9). Sliding the nine-label circuit window
appears to reduce that gate to

    (d-e)(c-a)/((d-a)(c-e))
      + (d-b)(e-f)/((d-f)(e-b)) = 1.

Prospective consequence, still to check: the three pairs (a,b), (c,f),
(d,e) are fibers of one degree-two rational function and are swapped
by a projective involution. This is not yet a uniform contradiction.
The test is to prove the exact reduction and determine whether the
remaining gates couple these local restrictions into a stronger condition.
Continue for a useful proved residual restriction or uniform exclusion;
abandon zero kernel only on an independently verified deficient labeling.
No positive rank samples, label sweep or family census are proposed.

Local comparison: the earlier reconstruction and audit do not simplify
the shared gates. L036 uses a quadratic involution for a different
actual-error branch; inspect that elementary calculation before duplicating
machinery. ATTEMPTS/020,029,031 remain preserved. No literature refresh,
cross-notebook input or mathematical script has been used at this point.

## Completed pass

[L090](../lemmas/L090-cyclic-six-label-involution-reconstruction.md)
proves the displayed simplification and its exact determinant and
involution forms, including invertibility, uniqueness and finite poles.
An explicit eight-step reconstruction determines every possible labeling
from its values at J={0,1,4,6,7,8,11,15}. This uses eight of the sixteen
necessary six-label determinants, with no label enumeration. The full
algebra and every reconstruction row are canonical in L090, whose only
direct mathematical input is audited L089. L036 was a comparison for
elementary algebra, not an imported actual-error theorem or dependency.

This is a useful lower-locality restriction on the residual labeling
problem, not a determination of rank R or an assertion of progress beyond
the inspected literature. POTENTIALLY_NEW has only its policy meaning.
The required uniform threshold remains rank R>=3; only rank R>=2 is
known uniformly. None of the reconstruction's partial assignments was
tested for existence. A reconstructed value at infinity, outside H or
already used invalidates that seed assignment. Passing reconstruction
still leaves the eight unused determinant equations and the first two
shared-coordinate gates for all sixteen triangles. The restriction has
not received a separate critical audit.

All proof checks were analytic: the six-label numerator identity was
expanded explicitly, the two-pair kernel and its discriminant were checked
with both A=0 and A!=0 retained, and each of the eight table rows was
checked against the cyclic pair formula and previously known indices.
There was no mathematical script, rank sample, label sweep, source search
or cross-notebook input. Existing changes and failed routes are preserved.

Continue the unchanged approved target with one analytic elimination pass
on the remaining shared gates, checking L090's new identities wherever
load-bearing. The plausible use is a uniform label contradiction; actual
error applicability, arbitrary-family coverage, triangle twelve and source
qualifications remain independent gaps. Continue for a uniform
contradiction or useful further proved restriction; a deficient bijection
requires independent full-kernel verification before abandoning uniform
zero kernel. If the pass yields neither, record EXPLORATION and reassess
the mechanism. The unchanged ready assessment covers this target; no new
continuation assessment or literature approval is asserted.
