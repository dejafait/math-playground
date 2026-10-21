# 194 — 2026-10-13 Action double-gradient group is subcubic

STEP_ID: YM-20261013-194-cubic-residual-action-double-gradient-difference

RESEARCH / REPRODUCTION / proof_attempt on the unchanged prior-ready
complete cubic residual/action target. [L162](../lemmas/L162-cubic-residual-action-double-gradient-subcubic.md)
improves L161's entire action-two-gradient group from O(N^3) to
O(N^(5/2)), so it vanishes at cubic scale for both actual probes.
L159's co-closed transport supplies the difference missed by the
previous norm count. The full-prefix energy includes both end edges;
no signed E positivity, covariance commutation or jump smoothing is
used. This is standard-method local progress, not a novelty claim.

The full certificate
`scripts/combined-ward-response/cubic-action-double-gradient-difference-certificate.json`
passes 55 rational identities, nine signed trace cases and nine prefix
cases, with exact error zero and no failures. The non-co-closed
control retains its nonzero diagonal. Finite checks are algebraic;
the canonical analytical proof supplies the all-mesh bound.

Both same-vertex groups now vanish at cubic scale. Continue the
unchanged complete response target with L161's first four ordered
traces and the two retained mixed branches. Their bounds/limits and
all other jets, complete compensation, finer asymptotics, matching,
interacting reflection and continuum/infrared requirements remain.
Preserve ATTEMPTS/009, /011, /036 and /037. No candidate exists.
