# 2026-10-04 — An internal radial Wilson-flow contraction

The saved target and its SPECIALIZE assessment in
`drafts/literature/2026-09-26-current-target.md` are unchanged. No new
literature is needed. Existing L019 work is preserved. The shared/local
instructions, entire overview, DAG, and L008–L011 definitions were read.

The gap is the complete original-probe coefficient Gamma_(i,a), including
its possible logarithm and faster cutoff terms. A useful bounded test is
to contract the radial quartic Wilson-action contribution inside the
third flow jet, with the flow time integrated all the way to zero. This
tests an actual internal loop rather than another coordinate-change
identity. If the contraction is uniformly small, remove it from the
list of possible logarithmic sources; if it grows, retain it in the
required cancellations. Neither outcome settles the other vertices or
the interacting reflected-error threshold c_box/2.

## Working argument saved before completion

Write the local plaquette logarithm as w = D theta + w_2 + w_3 + ... .
The radial part of the Wilson numerator at fourth order is
`-sum_p |D theta|^4/96`. Its contribution to the cubic coordinate flow
is `D* (|D theta|^2 D theta)/(24 a^2)`. Coordinate-metric and BCH terms
are separate contributions, not discarded terms of the full flow.

For three independent colors, internal pairing of two fields in
`|Y|^2 Y` gives `5 v Y`, where v is one color's coincident curvature
variance. Here Y = D z_1(s), so v is a diagonal of the exact-curvature
projector times the relative two-form heat operator. Thus v <= 1 and
v <= C a^4/s^2 at positive s. The integrated bound is O(a^2), not a
logarithm. It includes the physical faces through the relative modes.

The remaining issue is to bound this subgraph after contraction with
the actual unsmoothed quadratic residual. Its covariance-normalized
operator has the crude bound O(1/a). Split the flow integral at tau/2:
in the first half the output propagator controls two derivatives; in
the second half v = O(a^4), which absorbs their cutoff bound O(a^-2).
The normalized probe correction has trace norm O(a^2), suggesting an
O(a) bound for both residual responses. Only these free-gauge-invariant
polynomials may be moved from the forest to the Hodge Gaussian.

## Completed result

The full proof and precise selected-pairing definition are in
[L020](../lemmas/L020-radial-wilson-flow-tadpole-bound.md). The selected
contribution to each original probe's Gamma_(i,a) is O(a), so it has no
unsuppressed cutoff logarithm. This is a local mathematical advance by
specializing elementary Wick and relative heat-kernel estimates, not a
claim beyond the checked renormalization literature. It does not bound
the whole radial-vertex contribution: Wick pairings to the outer probe
leg and the residual, rather than internally in the cubic vertex, remain.
The nonradial cubic flow, two quadratic-flow vertices, action, measure,
and insertion terms also remain. No complete coefficient is assigned.

The continuation is the same screened combined-response target, with
this selected contraction removed from the unknown terms. The required
reflected error <= c_box/2 and all continuum/mass-gap gaps are unchanged.
