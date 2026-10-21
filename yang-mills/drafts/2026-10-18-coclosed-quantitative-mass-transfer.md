# Co-closed quantitative transfer — bounded attempt

Approved target: Assess whether L090's complete co-closed/co-closed rough-sector trace T_hh is O(N^(5/2) log(eN)^2) for both actual probes.

Use the unchanged EXPLORE assessment
`drafts/literature/2026-10-17-coclosed-sector-quantitative-remainder.md`.
The main gap remains interacting cutoff removal with reflected error
<=c_box/2, followed by continuum axioms and finite positive mass.
A quantitative bound for this sector could enter the complete remainder
after L220's cubic cancellation; other component rates are independent.

The unfinished checkpoint is now completed in
[L225](../lemmas/L225-coclosed-uniform-resolvent-error.md). The full
weighted spectral sum and the resulting uniform mass-removal estimate
are proved there, including epsilon<N^-2, the complete boundary collar,
both covariance positions and both signed orientations. At epsilon=N^-1
the complete-sector comparison error is O(N^(5/2)sqrt(log(eN))), below
the requested threshold. This is local standard-method progress, not
a complete sector bound or a claim of progress beyond checked sources.

Continue the unchanged approved target by testing the remaining
T_(epsilon) with epsilon=N^-1 and its exact transverse projection.
The next discriminating test is whether retaining the derivative-weighted
covariance estimates through projection comparison avoids L090(16)'s
fixed-epsilon loss sufficiently for sublinear localization. Continue for
a uniform error at O(N^(5/2)log(eN)^2), or an explicit improved joint
error that narrows that gap; stop the particular transfer if its required
projection/localization parameters cannot meet that threshold. This
test is not assumed to succeed and selects no unproved parameter schedule.
The massive trace's coefficient-freezing and boundary errors also remain.
Do not infer a varying-mass limit from L090's fixed-mass limit.

Essential inputs: L088, L089, L090, L225, importing their analytic premises
L003 L009 L018 L026 L028 L085 L086. Keep i=3,6, both generator
orientations and covariance positions, all relative end rows and axial
levels, coincident plaquettes, constant component modes, both residual
subtractions through L089, and the complete exterior heat sum. No positive
residual, commuting coefficient or smooth upper extension is assumed.

L225's new specialization awaits a separate critical audit; its inputs
are imported, not recursively re-audited. Reuse the unchanged target
assessment; no additional source review or new ready assessment was
written in this research turn. Mathlib coverage remains not checked.
