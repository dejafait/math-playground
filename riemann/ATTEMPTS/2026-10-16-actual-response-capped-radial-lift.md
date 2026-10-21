# Capped radial rare/bulk lift: incomplete cubic and bulk calibration

Step 152's exact partial construction and all bounds are canonical in
[L418](../lemmas/L418-prescribed-response-capped-rare-component.md).
Unlike L416's freely placed rare measure, every output response stays
at its actual height. Capping the conditional weight retains fiber mass
at most one and every quartic integrand exactly, with O(1) total rare
second-moment trace. The zero completion is a probability law, but is
explicitly not a law satisfying the full target list.

WHY IT DOES NOT COMPLETE THE TARGET: The maximal rare cubic contains
an actual magnitude-dependent multiplier. Existing signed moments do
not evaluate that integral. A bulk with critical norm O(sqrt(log H))
has cubic o(log^2 H) and cannot repair a missing leading coefficient.
Neither that coefficient nor a supported bulk with the required two
first means and six second moments was constructed. In particular O(1)
rare odd cross moments cannot simply be charged to the much smaller
allowed final errors. Removing the cap violates fiber probability where
the actual critical norm exceeds the proposed rare radius. L416's
response-amplitude and phase calibration remains unavailable.

This parks a direct transfer of L416's normalized-radius rare/bounded
bulk proof. It does not disprove this actual conditional feasibility
problem or exclude more flexible radial choices. The next implementation
should test a bulk supported on the negative discriminant cone at the
prescribed response, with integrated covariance calibration. Its possible
success would still leave the rare cubic and all actual/global/regulator
questions unresolved. L417 and all earlier failure scopes are preserved.

Step 153 continuation: [L419](../lemmas/L419-prescribed-response-negative-cone-bulk.md)
now supplies the independent supported bulk at the exact response,
including both first means and exact odd-second-moment cancellation.
This partial construction awaits critical review. It leaves the rare
cubic threshold above unchanged; the original zero-completion failure
and stopped direct transfer are preserved.
