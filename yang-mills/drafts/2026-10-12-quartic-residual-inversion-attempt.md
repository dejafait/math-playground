# Quartic residual: local inversion bound and unfinished first order

The unchanged approved target is the complete L011 quartic residual
covariance for both actual L010 probes in the straight lower-rooted
forest. This attempt establishes a signed O(a^-3) bound but does not
reach the required o(a^-3). It uses the unchanged saved EXPLORE assessment
`literature/2026-10-12-quartic-residual-insertion-cubic-scale.md`.

The full proof is canonical in
[L150](../lemmas/L150-quartic-residual-cubic-bound-by-local-inversion.md).
The exact covariance, single-row projection comparison, full external
heat-mode neighbor estimate and complete nonlinear midpoint inversion
identity are justified there. All 104 exact word-geometry checks pass
in `../scripts/combined-ward-response/quartic-residual-inversion-certificate.json`.
The check does not numerically evaluate either actual response.

Unfinished obligations: retain the signed first-order contraction of
K-K^0, U-U^0 and C-C^0 in L150(11), together with both insertion
subtractions. Each has only an O(a^-3) bound after summation. The
complete normalized sum is Z=O(a); its order-a coefficient must vanish
with a controlled remainder to obtain Z=o(a). No existence of that
coefficient, covariance derivative expansion, actual-probe cancellation
or uniform limit interchange is assumed. The exact covariance in
L085 retains min(s,t), its local kink and every pinned transverse row.
The upper-face condition remains encoded in the actual external prefix
and covariance; do not replace the local comparison by a global one.

Essential inputs are L149 L150 L028 L085 L114; L009 L010 L011 L017
L018 L026 retain the generator/probe/forest conventions.
L019 remains the separate forest-compensation constraint. No nonlinear
Hodge transfer, internal heat damping, isolated forest invariance,
covariance asymptotic or vanishing first-order coefficient is assumed.
Continue if a controlled signed estimate reaches o(a), a nonzero
actual-probe coefficient is justified, or a discriminating obstruction
changes the mechanism. Abandon a repetition that only yields O(a),
or invokes the frozen cancellation to discard its first-order errors;
do not repeat ATTEMPTS/036's entrywise count or ATTEMPTS/011's false
bounded-loop hypothesis. The unchanged assessment covers the exact
same target; no additional source review is needed merely because this
bound is now available. All other jets, full compensation, finer
asymptotics and the interacting/continuum/infrared gaps remain open.
