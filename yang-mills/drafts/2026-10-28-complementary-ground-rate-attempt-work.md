# Full relative-cube ground compression — bounded attempt

Step YM-20261028-536-complementary-ground-rate-attempt. Initial checkpoint;
the target and hypotheses are exactly those of the saved EXPLORE
assessment `literature/2026-10-28-complementary-ground-compression-rate.md`.
Existing notebook changes are preserved. No source refresh is needed.

The main gap is the interacting continuum construction with positive
infinite-volume mass. The intermediate test is
`||P_N W_N^(0) P_N|| = O(N^-1 log(eN)^2)` for L297's exact operator.
Its possible use is the largest low-pole coefficient at L297's infrared
test scale; other residues and the higher remainder remain independent.

The supplied assessment and ATTEMPTS/047--050 were checked. Neither
the one-face results nor the qualitative fixed-polynomial limits give
the target. L297(17) already bounds the external-curl difference by
`O(N^-1 sqrt(log(eN)))`; the present quantitative work concerns the
complete density, local quartic and internal-curl bilinear forms.

Proposed discriminating calculation: use L003's exact tensor grids to
compare finite-box heat kernels with the infinite-lattice kernel up to
time N^2, then use the relative spectral gap above that time. Seek
pointwise covariance/curl bounds of orders distance^-2, distance^-3,
distance^-4 and a boundary-depth comparison, without replacing the
transverse projection by a scalar covariance. Products in the complete
internal-curl operator should then have a summable first spatial moment;
their boundary row defect must be summed over every face and intersection.
This is a proposal, not an established estimate.

Continue on a full uniform rate or a rigorous weaker explicit modulus.
If the complete internal-pair or boundary sum cannot be controlled, save
the exact residual. An inadequate upper bound does not refute the rate.
No conclusion about a bounded complete tail or continuum theory is made.

## Completed attempt

The complete proof is now canonical in
[L298](../lemmas/L298-full-cube-ground-compression-rate.md).
The exact tensor image formulas, short/long heat-time split and
transverse identities give full-cube kernel and boundary-depth bounds.
The complete internal-curl products have a summable first spatial
moment; their boundary row defect is O(log(ed)/d^2), summable over
all depth layers. Density and local quartic defects are O(d^-2).
Consequently all three ground bilinear errors are O(N^-1).
Retaining L297(17)'s external-curl term gives the stronger bound
O(N^-1 sqrt(log(eN))) and hence the registered threshold.

Outcome ADVANCE is local quantitative progress, pending a separate
conceptual audit; no originality beyond the checked sources is claimed.
The exact registered rate target and saved EXPLORE assessment remain
unchanged for that audit. The new proof uses no additional external
theorem: its heat calculation supplies the mixed-grid specialization
missing from the assessed scalar results. The ordinary finite Gaussian
input is cited, and the recorded Wilson constants are reused.
No mathematical script or numerical verification was needed.
