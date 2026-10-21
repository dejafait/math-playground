# 2026-10-05 — Nonradial quartic action: fixed-mesh contraction

The ready SPECIALIZE assessment is
`drafts/literature/2026-09-26-current-target.md`; its exact full-response
target is unchanged. This step selects only
`-kappa(f_(i,0), r_0, S4-S_(4,rad))`, for i=3,6, within that target.
The main gap is ultraviolet-uniform interacting control. An explicit
forest-covariance contraction can expose the still-required internal-loop
estimates without transferring nonlinear vertices to the Hodge law.
Continue if the two connected pairing classes can be specified exactly;
abandon a curvature-only transfer if the nonradial polynomial is nonzero
on a pinned zero-linear-curvature input. Neither test evaluates the full
logarithm or improves the reflected-error threshold c_box/2.

Preserved unfinished work and searched L011, L018–L019, L020, L022–L024,
the radial-action notes/history, and the isolated-Haar failure. Existing
results contract the radial action and locate cross-group cancellations;
none inspected gives this nonradial action contraction. Reuse the
assessment's imported bulk results and scope qualifications; no new
literature or general renormalizability reproof is needed here.

Work saved before the exact algebra checks: for a plaquette ordered
product of signed link exponentials, write its logarithm as
g w1 + g^2 w2 + g^3 w3 + O(g^4). The selected polynomial should be
q_p = |w2|^2/2 + <w1,w3>. Use its symmetric fourth-order tensor K_p
in local edge/color coordinates, and the exact forest covariance Sigma.
The two anticipated connected contractions are a fourth-chaos term
with 24 pairings and a quadratic Wick term with 48 after tracing two
action legs. Their signs, covariance ordering and BCH coefficients
require independent exact verification before promotion to a lemma.

Remaining assumptions: fixed mesh first, the actual full-link linear
Wilson flow in the leading probe, the actual free residual, and fixed
boundary links. No forest-group invariance, nonlinear curvature transfer,
uniform path estimate or bounded full remainder is assumed.

Completed: [L025](../lemmas/L025-nonradial-action-forest-contraction.md)
proves the ordered action decomposition and the exact 24/48 pairing
formula for both probes with all local color indices. The internal
loop is the signed plaquette-edge restriction of the exact forest
covariance. A pinned gradient makes the selected polynomial positive
while Dx=0, so the radial curvature-only transfer does not apply.
Ten exact checks passed: three ordered trace/BCH comparisons, one
zero-curvature test, and six two-class/full-cumulant comparisons.
The complete checks value in
`scripts/combined-ward-response/nonradial-action-certificate.json`
was inspected. These verify finite algebra, not the original-box
matrix entries or ultraviolet estimates. No cutoff bound is achieved.

The contraction threshold passes, and the direct-transfer test fails.
Continue with the exact forest law. Essential next inputs are L025's
local matrices, L018's path lift and forest covariance, L011's full
expansion, and L019's cancellation constraint. The next bounded
substep is to estimate C_p for compactly supported plaquettes in the
straight rooted forest, distinguishing uniform boundedness from path
growth before attempting to bound the selected contractions. Do not
infer the full response's growth from that local covariance alone.
