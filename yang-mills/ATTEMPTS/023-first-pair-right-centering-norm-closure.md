# Rough right-row centering with the generic first-pair norm

WHY IT FAILS: [L074, proof section 5](../lemmas/L074-first-pair-exterior-centering-defect.md)
applies the determinant-one shear to the actual exterior and both
rough right rows, with all pinned endpoints and both placements.
The first pair is exactly invariant: the exterior O(N²) defect moves
between the circulation/path and path/path terms with opposite signs.
The rough gradient paths are unchanged. The retained joint ordered
trace still contains the centered antisymmetric path minor, and the
available full-array bounds give O(N³), above the O(N²) threshold.
This parks this shear-plus-generic-norm closure; it does not prove
signed growth or exclude a sharper joint cancellation. A distinct
test is the exact axial covariance transfer of the s-weighted base
row before the residual, rather than another path centering or norm
rearrangement. ATTEMPTS/019–022 and the exterior defect estimate remain.
