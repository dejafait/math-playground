# Co-closed weighted projection transfer — completed attempt

Approved target: Assess whether L090's complete co-closed/co-closed rough-sector trace T_hh is O(N^(5/2) log(eN)^2) for both actual probes.

Reuse `literature/2026-10-17-coclosed-sector-quantitative-remainder.md`.
The main gap remains interacting cutoff removal with reflected error
<=c_box/2, then continuum axioms and finite positive mass. A quantitative
sector remainder could support the complete coefficient remainder;
other component rates and interacting control remain independent gaps.

The preliminary reasoning saved here is now completed in
[L226](../lemmas/L226-coclosed-weighted-projection-error.md). Its proof
retains the projection difference's exact gradient range, controls both
projection placements in each alternating operator, and telescopes all
eight changes across the two generator orientations. With L225,
epsilon=N^-1 and delta=N^(-4/3) reduce the approved sector bound to the
same bound on the exact regularized trace, with comparison error below
the threshold. This is local standard-method specialization, not a
complete sector estimate or originality claim. Both new comparison
lemmas await separate critical audits.

Continue the unchanged approved target by testing joint localization
and coefficient freezing in T_(N^-1,N^(-4/3)). The concrete test is to
retain the derivative and resolvent factors in the closed trace while
bounding its spatially weighted kernel products, including the physical
boundary comparison, at O(N^(5/2)log(eN)^2). L090's frozen two-orientation
cancellation remains the endpoint; no growing-range remainder estimate
is imported from its fixed-degree argument. A claimed approximation
must bound its actual trace error, not merely its operator error or
propagation range. No sublinear range has been proved here.

Continue for a uniform trace error at that threshold or a specific
joint estimate narrowing the gap. Abandon a chosen absolute-kernel
transfer if its explicit parameter requirements cannot meet the
threshold; preserve the loss and distinguish it from signed growth.
The existing geometric polynomial estimate has no established adequate
localization/freezing bound at these masses. Exact projection removal
or a materially different signed regrouping remains possible within
the approved trace, but a changed target or hypotheses needs review.

Essential inputs: L088 L089 L090 L225 L226 and inherited L003 L009
L018 L026 L028 L085 L086. Retain i=3,6, both generator orientations,
both covariance positions, every axial level and normal end row,
coincident plaquettes, constant component modes and the full heat sum.
L089 retains both residual subtractions. No positive residual, commuting
multiplier, smooth upper extension, or varying-mass application of a
fixed-mass limit is assumed. Localization, coefficient freezing and
boundary comparison of the regularized trace remain unproved.
Mathlib coverage is not checked. Reuse the unchanged ready assessment;
no new assessment, literature turn or scheduler change is made.
