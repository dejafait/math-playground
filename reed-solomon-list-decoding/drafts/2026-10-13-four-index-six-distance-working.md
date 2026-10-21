# Four-index mixed-shell calculation — working checkpoint

Approved target: Test L056's fixed moments on every four-index union matrix anchored at D with half-distances (DE,DF,DG,EF,EG,FG)=(5,5,6,5,5,5).

The main gap is arbitrary-center 68-agreement safety, separately 67.
Use L053's positive rho and fixed pairs, L054's full region dictionary,
audited L056's 21 coefficients and represented unordered consistency,
and audited L057 as prior small-principal evidence. The unchanged
SPECIALIZE assessment is
`drafts/literature/2026-10-12-released-zero-four-index-six-distance.md`.
ATTEMPTS/035,038,039 do not decide this coupled matrix.

Plan: relative to D, write E,F,G using removed sets of sizes (5,5,6)
inside D and added sets of the same sizes outside. Enumerate all three
removed pair-intersection sizes and both removed/added triple sizes;
the required pair distances determine the three added pair sizes.
Nonnegative eight-region partitions on each side retain all 16 atoms.
Reconstruct full supports, check all six distances, compute DEF using D,
DEG using E and DFG using F, checking every eligible anchor.
Construct actual family-union entries and all exact principal minors;
retain singular matrices. A negative witness suffices to reject the
prescription; a pass requires complete enumeration and exact PSD evidence.

Completed: L058 exhausts 150 full atom vectors. All 2250 minors are
strictly positive; 2405 constructor and 7506 independent reconstruction
checks pass, including complete invertible positive-diagonal congruences.
The independent enumeration uses triple/four-way intersections and
Möbius inversion. One initial verifier set/frozenset method mismatch was
repaired; no inequality failed. Full evidence is in
`scripts/finite-support/released-zero-four-index-results.json` and
`scripts/finite-support/released-zero-four-index-verification.json`.
ATTEMPTS/040 parks this diagnostic. Separate critical review is pending.
Other triple coordinates, full SDP bounds, representing measures and
common-center RS realization remain open; no boundary change.
