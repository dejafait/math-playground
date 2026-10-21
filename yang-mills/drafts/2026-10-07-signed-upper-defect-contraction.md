# Signed upper defect — bounded working record

STEP_ID: YM-20261007-066-signed-upper-defect-contraction

Approved target and coverage: the unchanged combined-response target in
`drafts/literature/2026-09-26-current-target.md` (SPECIALIZE).
The main local gap is the full power/log behavior of L011's response;
the construction and interacting reflected-error bound remain independent.

Intermediate test: contract L050's nonlocal defect against the actual
quadratic probes and residual in L049(9), separating any rigorously
subleading R contribution. This can narrow the compensation test against
L047. Continue on a complete finite contraction or a justified scaled
bound; abandon estimates that assign low-mode smallness to random Q,
discard E, or omit cross-edge and pinned-end contributions.

Inputs checked: L018's forest matrices, L025's two quartic pairing
classes, L029's Wick coefficient/exterior rates, L040–L041's companion
and signed d-line bound, and the full L049–L050 proofs. Local searches
found no existing contraction of the nonlocal defect. ATTEMPTS/017
rules out uniform-smallness; it does not rule out this signed test.
The ready source assessment is reused, with no new literature premise.

Working deduction, saved before further algebra: subtracting q_A from
L029's quartic removes l|H|^2/4, h|L|^2/4 and -b H.L/2 from its
quadratic Wick coefficient. The remaining HH coefficient is -f/3=O(1),
not O(N). L029's W rates then appear to give O(a^-1) for the sum of
one-pair R contractions. The no-internal-pair R contraction is exactly
L041's signed d-containing sum, also O(a^-1). Check all six coefficients
before asserting this reduction.

For Z, use a quadratic tilt of the full forest Gaussian, not conditioning
away the observable derivatives. Its upper-potential covariance has
first derivatives 2U, 2V and mixed derivative 4(W+W^T). Isserlis reduces
E[Q_e.Q_h] to a determinant of four covariance entries. Polarization
should retain all edge pairs of I-K. No scaled bound is yet proved;
L049's E remains present.

Completed: L051 gives the exact signed nonlocal defect contraction and
proves the complete R cumulant is O(a^-1), hence subleading at a^2
scale. All six one-pair coefficient bounds and the signed companion
were retained. Four rational checks, including two direct degree-eight
Gaussian cumulants, pass with no failures in
`scripts/combined-ward-response/signed-upper-defect-certificate.json`.
This is local REPRODUCTION progress, not a general renormalization
advance or a value for the requested logarithm.

Continuation within the unchanged approved target: use L051's two Phi
terms, L050's exact D and L049's complete E to test a^2-scaled
compensation against L047. Essential inputs are L018, L025, L029,
L040–L041 and L047–L051, with L011/L019 retaining the full-jet context.
No bound for either Phi term or E, no cancellation with other cubic
pairs, and no complete power/log asymptotic is assumed. R must be
restored for a logarithmic calculation; its O(a^-1) estimate does not
exclude slower powers or logarithms. The kernel's fixed-mode rate
cannot be applied to the rough internal covariance C or V.
