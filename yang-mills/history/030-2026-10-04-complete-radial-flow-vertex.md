# 2026-10-04 — Complete selected radial flow summand controlled

Reused the existing SPECIALIZE assessment for the exact combined-response
target; no literature work was needed. Preserved prior unfinished work.
[L021](../lemmas/L021-complete-radial-flow-vertex-bound.md) computes the
previously excluded connected pairings of L020's radial cubic flow
vertex and bounds them by O(a). With L020 this bounds all pairings of
that selected flow summand, for both original probes. The
[working note](../drafts/2026-10-04-radial-flow-remaining-pairings.md)
records the test and normalization. Exact enumeration in
`scripts/combined-ward-response/check_radial_remaining_pairings.py`
passes 24 rational cases for both pairing classes separately.

Outcome: ADVANCE, a local specialization/reproduction of Wick and
heat/trace estimates; no discovery beyond checked literature is claimed.
The bound includes flow times near zero and relative boundary modes.
It excludes this entire selected flow summand as an unsuppressed
logarithmic source, without bounding the radial action's separate
insertions elsewhere or the complete Gamma. The reflected-error
threshold c_box/2, continuum construction and mass gap remain unresolved.

Continue the screened combined-response calculation with the remaining
nonradial and two-quadratic flow terms. Their forest law must be retained
unless free gauge invariance justifies a transfer. The new estimate
keeps the inconclusive exploration counter at zero; historical route
stops are preserved. STATUS remains IN_PROGRESS, with no candidate.
