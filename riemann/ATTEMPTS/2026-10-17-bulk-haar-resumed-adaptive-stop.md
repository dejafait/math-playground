# Resumed direct adaptive enclosure: material-narrowing test fails

The exact step-190 enclosure, inclusion proof, complete budgets and
arithmetic qualifications are canonical in
[L426](../lemmas/L426-covariance-free-bulk-actual-height-phase-average.md),
in its resumed-adaptive section. Certificate:
`scripts/discriminant/bulk-haar-resumed-enclosure-190.json`.

WHY IT FAILS: Doubling the saved partition to 131072 leaves with 524288
additional candidate-child evaluations narrows I only to
[-0.194,0.114]. The exact width ratio to step 189 lies between .85 and
.86, missing the predeclared .75 threshold and still containing zero.
Joint strict-cell width about .288212 dominates branch width about
.0184495. Both include coefficient and full-response tail uncertainty;
neither is a measured irreducible floor. Stop further direct adaptive
subdivision of this implementation. A polynomial envelope of the
conditional angle average, integrated by exact Euler moments rather
than joint prime-angle ranges, is a materially different proposed test;
its source coverage and feasibility remain unassessed. This is no
nonvanishing or vanishing result, realization claim or RH conclusion.
