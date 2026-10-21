# 2026-10-04 — Quadratic nonradial flow: longitudinal test

Reuse the ready SPECIALIZE assessment in
`drafts/literature/2026-09-26-current-target.md` for the unchanged full
combined-response coefficient. No new literature search is needed.
This is one bounded mathematical test within that target, preserving
the existing L019–L021 work.

The gap is the remaining nonradial flow contribution to L011's Gamma,
including its interactions with the higher probe and action jets. The
proposed intermediate test is whether Q_2 and the curvature of its
integrated jet z_2 depend only on linear curvature. A positive answer
would permit the forest-to-Hodge transfer used for the radial summand;
a counterexample requires retaining the forest law or explicit
nonlinear gauge-jet cancellations. Neither answer supplies the full
logarithm or the required interacting reflected error <= c_box/2.

L011 defines Q_2 but does not evaluate this test. L019 gives coordinate
change cancellations without evaluating an actual flow vertex. L020–L021
cover only a curvature-based cubic summand; their bounds do not apply
here. The failed global BRST representation is not reopened.

## Reasoning saved before verification

Let phi be a pinned site Lie-algebra field, and use oriented links v->w.
The exactly flat family exp(g phi_v) exp(-g phi_w) has coordinate jets
x_e=phi_v-phi_w and y_e=-[phi_v,phi_w]/2. With L=a^-2 D*D,
stationarity of this flat family under Wilson flow suggests
Q_2(x)=L y. Since D x=0, its linear flow is stationary, whereas the
quadratic flow jet from the straight initial coordinates g x should be
z_2(t)=(1-exp(-t L))y. Choosing two adjacent interior sites with
noncommuting phi leaves y on their shared edge, so D y is nonzero.

The inverse pinned gauge transformation should send the flowed straight
family to coordinates g^2(z_2-y)+O(g^3). Gauge invariance of each actual
probe numerator then gives its degree-four value on x as
j_(i,2)(exp(-t L)y). Comparing this with L011's probe composition
locates a cancellation between j_(i,2)(z_2), the cubic observable jet,
and the quartic observable jet. Signs and the actual Q_2 identity need
an independent degree-three Wilson-action check before recording a result.

## Completed test

[L022](../lemmas/L022-quadratic-flow-longitudinal-obstruction.md) proves
these identities and specializes them to the actual central triplet
stencil. For phi supported with noncommuting values on two adjacent
central sites, ||D y||^2=3/2 and j_(3,2)(y)=1. The isolated
j_(3,2)(z_2(tau)) is 1+O(a^2), whereas the full quartic probe coefficient
on this input is O(a^4) for both probes. The cubic observable derivative
and quartic observable jet supply the cancellation. Relative heat
diagonals prove the estimate without omitting boundary modes.

The exact rational script
`scripts/combined-ward-response/check_quadratic_flow_longitudinal.py`
checks the Wilson cubic-action gradient and inverse gauge signs on
complete relative N=4 and N=6 complexes. Those are local algebra tests;
the proof supplies the embedding into admitted fine meshes and the
cutoff bounds. No original-probe Wick covariance is evaluated.

Outcome: NEGATIVE for extending the radial term's curvature-only
transfer to the quadratic flow term. This supplies new explicit
evidence, rather than repeating the general warning about nonlinear
vertices. It is reproduction/specialization, with no claimed result
beyond checked literature. Keep the nonradial terms in the forest law
until their coordinate corrections can be included; the independently
testable radial action insertion remains within the same screened full
coefficient calculation. The logarithm and the interacting threshold
c_box/2 are unchanged. No new inconclusive exploration turn is used.
