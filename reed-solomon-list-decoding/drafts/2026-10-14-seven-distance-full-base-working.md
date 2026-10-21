# Approved distance-seven whole-base kernel attempt

Step 219 works only on the unchanged SPECIALIZE target in
`literature/2026-10-14-seven-distance-full-base-kernel-column.md`.
Main gap: arbitrary-center safety at 67/68 agreements, bracket 955–957.
Intermediate test: a nonnegative distance-seven column retaining the
complete L062 atom-key dictionary and annihilating the full L061 base.
An exact pass parks this diagnostic; an exact inconsistency excludes only
this fixed prescription. No energy, free-entry scalar upper bound or
retuning is authorized in this step.

Inputs: L021,L053,L056,L059,L060,L061,L062; foundations/09,10,12.
Preserve L064 and ATTEMPTS/041,043,046 and all prior unfinished work.
The base has positive rho and unchanged p7. Proposed exact reduction:
the stabilizer of D,G has region sizes 7,61,7,949. Its base orbits are
the anchor, 36 layer-five coordinates and 49 layer-six coordinates.
Construct the entire orbit action using intersection counts, with actual
orbit-size weights. Compute its exact full kernel and enforce weighted
orthogonality on the column; averaging will justify exhaustion of the
full kernel. Fix represented entries by the full six-permutation key,
forbidden entries to zero, and identify all other entries by that key.

Pending: check every entry, weighted self-adjointness, complete rank,
kernel basis, fixed lookup and rational nonnegative feasibility. A failed
ansatz or numerical status will not be reported as inconsistency.

Completed evidence: L065 and scripts/finite-support/seven-distance-full-base-kernel-{results,verification}.json. The full invariant quotient has rank 37 and kernel dimension 49; the fixed-entry system has rank 46 and three affine parameters. A rational column has 46 positive free coordinates and three zeros, with all original residuals zero. Constructor/independent reconstruction pass 4412/12638 checks. Initial decimal-basis extraction omitted nonbasic parameter-zero constraints; corrected extraction supplies the exact active set {4,27,33}, independently checked without an optimizer. The original exact system was consistent throughout. Energy and enlarged PSD were not evaluated. Separate critical review remains pending.
