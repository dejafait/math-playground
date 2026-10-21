# 195 — 2026-10-13 First Hodge trace: upper action-column jump

STEP_ID: YM-20261013-195-cubic-residual-hodge-upper-jump

RESEARCH / REPRODUCTION / proof_attempt, reusing the unchanged prior-ready
EXPLORE assessment for the complete cubic residual/action target.
[L163](../lemmas/L163-cubic-residual-hodge-trace-upper-jump.md)
removes the upper action exterior jump from L161(3)'s first trace with
O(N^2) error. The exact action tensor pairs a normal source with a
tangential source. Specializing L041's two inverse columns separately
retains the extra tangential Dirichlet factor; applying its circulation
estimate indiscriminately would be incorrect. Both residual subtractions,
all action faces, constant modes and the complete heat sum remain.

The certificate at
`scripts/combined-ward-response/cubic-hodge-upper-jump-certificate.json`
passes 486 exact polarization entries, 18 additional fixed-link cases
and 24 full inverse-column recurrence cases, with maximum rational error
zero and no failures. These check algebra and boundary conventions;
the canonical proof supplies the uniform estimate. This is local
standard-method progress, with no novelty or complete-response claim.

Continue the same ready target with the first trace's interior part,
three other signed traces and the two retained mixed branches. The
new bound applies only to the first trace's action exterior split,
not to the prefix matrices in the other orders. Preserve the stops
in ATTEMPTS/009, /011, /036 and /037. Full compensation, finer scales,
interacting reflection and continuum/infrared construction stay open.
