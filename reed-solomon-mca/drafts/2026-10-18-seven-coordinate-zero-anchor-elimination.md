# Seven-coordinate t=0 parameter elimination — completed bounded attempt

STEP_ID: 2026-10-18-mca-297-zero-anchor-support-elimination

The approved target is unchanged: assess the seven-coordinate fifteen
bound under the ready October 17 assessment. Main gap: exclude sixteen
original bad parameters. Intermediate target: eliminate the unknown
parameters from L104's t=0 simultaneous system, where r=12+n_0.
Potential use: a support-only obstruction before any extension-field
parameter search. Continue only on a nonvacuous compatibility reduction;
abandon if it merely repackages the moment equations without a test.

Read L104's full reduction and audit, L010's full event/equality proof,
L103's hypotheses and smaller-class application, and the relevant L107
statement. Reuse the ready Hall/shortening source assessment. L105/L107
require equal-lift anchors and cannot be applied at t=0. ATTEMPTS/036 and
037 stop different triangle coefficient eliminations: their automatic
minors and unresolved rank drops must not be recycled as contradictions.

Proposed calculation, not yet a proved input: represent the lift plane by
an alternating tensor p in exterior-square F^7. For each two-overlap row
(I,K), project onto the five coordinates S minus I and impose
g_K wedge projected(p)=0. These are linear equations in 21 entries,
with coefficients depending only on support labels. Need to prove
necessity, retain projected ranks zero and one, distinguish arbitrary
kernel tensors from decomposable ones, and restore finite-chart and
full-weight gates. A full-rank matrix would be a genuine exclusion over
all extensions; no rank or t=0 exclusion is assumed.

Independent gaps remain: other profiles and seven-sets, universal
representation, uniform triangle count and challenge qualifications.
No rational descent or all-support confinement is assumed.

## Completed result

The canonical proof and all gates are in
`lemmas/L109-seven-coordinate-parameter-free-support-filter.md`.
The quotient presentation gives six independent equations per support
row in 21 alternating coordinates, with no row parameters. At t=0 the
12–14 rows require rank at most twenty. The specified four-row test has
rank twenty-one and minor residue 28; independent modular and integer
determinant paths agree. The known two-row local construction passes
every matrix and eight-moment check. The full certificate is
`scripts/seven-coordinate/zero-anchor-support-filter.json`.

Read L026's alternating construction and L027's quotient interpretation
for duplicate comparison; their family-specific rank conclusions are
not inputs. This is a reproduction/specialization of that method, with
new local seven-coordinate applicability and no originality claim.
The selected continuation test is met by a nonvacuous support-only
obstruction. No complete t=0 family was enumerated or excluded; no
sixteen-event witness was constructed. Separate critical audit remains.
