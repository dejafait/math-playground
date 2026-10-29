# Full reflected coefficient: signed-contraction work record

STEP_ID: YM-20261025-482-exact-reflected-signed-contraction-test

The approved target is the full logarithmic bound in the unchanged
assessment `literature/2026-10-25-exact-reflected-coefficient-log-growth.md`
(EXPLORE before this invocation). Essential inputs are L279 and L003.
L011 supplies the already audited method, not its different Ward
coefficient. Existing notebook changes are preserved.

The main gap is a mesh-uniform interacting comparison, followed by the
continuum and infinite-volume construction. This attempt tests
|kappa_a| <= C log(eN) for the actual reflected pair. Success could
control its first perturbative correction; it would not control the
higher remainder or specify a physical trajectory. The stopping test
is the requested bound or a complete signed family with a precise
remaining estimate, without deleting faces, tensor channels or Haar
terms. Prior scalar-only, bulk-only and uniform-error import failures
remain in L004 and ATTEMPTS/005 and /046. No new source theorem is used.

Checkpoint before calculation: introduce two weights on the original
plaquette action, one for each supported insertion. Keep the exact
forest quadratic form and all cubic, quartic and Haar terms. Try to
organize their mixed source derivative before estimating. No new
coefficient extraction or nonlinear Hodge substitution is intended.

Completed bounded attempt: the full calculation is canonical in
[L279 section 6](../lemmas/L279-fixed-mesh-exact-reflected-coefficient.md).
The source-weighted expression (22) reproduces all seven original
terms. Cubic internal pairings vanish by their alternating SU(2)
color tensor, leaving the complete signed cubic/quartic/Haar family
(27). The normalized mixed covariance response has the uniform
Hilbert--Schmidt bound (29), using L003's bounded q_a. Neither this
bound nor the tensor organization estimates the full coefficient.

The estimate stops at the internal contractions in the entire signed
family (27). The Haar-only upper estimate (30) retains an uncontrolled
forest covariance norm, and the distinct-line terms still need joint
control. No growth or divergence is inferred from an individual term.
All boundaries, oriented tensor components, moving means and density
terms remain present. No new source hypothesis or nonlinear Hodge
transfer was used; no numerical fit or mathematical script was needed.

Outcome: EXPLORATION / RESEARCH / REPRODUCTION. This is a finite
Gaussian organization, not a beyond-source discovery or a bound on
kappa_a. One mathematical exploration turn has been used. The same
prior EXPLORE assessment continues to cover the unchanged full-sum
target; no new target was derived and approved. A further attempt must
test cancellation in (27), not merely re-expand the coefficient or
repeat (29). If it cannot obtain a controlled signed contraction, the
mechanism must be reassessed after that second unproductive attempt.
