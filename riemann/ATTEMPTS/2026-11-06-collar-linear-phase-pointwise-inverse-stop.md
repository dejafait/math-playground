# Relative linear phase: global pointwise inversion fails

2026-11-06. The canonical derivation, actual-G certificate and precise
scope are in [L850](../lemmas/L850-collar-linear-phase-flux-and-exterior-degeneracy.md),
pending a separate conceptual audit. This stops the inversion shortcut
for every L849(18) cutoff, not the full linear correction problem.

**WHY IT FAILS.** Pullback differentiation makes the linear equation
div(Mv)=Im q, with M=Re(F) I+Im(F) adj(Du). Teixeira's known theorem
supplies a supported ordinary flux, but recovering v by a global
pointwise inverse is unavailable. Every allowed cutoff is flat on the
antipodal line. The qualified exact bounds R_1<256 and G(-x)>1/100 on
[0,256] force Re F to vanish somewhere on that line, where M is the
zero matrix. This is not a full range obstruction: derivatives of Re F
still contribute to div((Re F)v), and a suitably chosen flux could
vanish to the required order. Smooth lifting, possible nodal-domain
compatibility and transition degeneracies remain unproved. No local
singularity, product-graph stop or failed extension is promoted to a
ban on the existential target. A renewed attempt must address that
smooth lifting problem, not repeat ordinary divergence plus inversion.
