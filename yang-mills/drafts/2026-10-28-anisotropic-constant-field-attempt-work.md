# Frozen anisotropic Wilson tensor — bounded attempt

STEP_ID: YM-20261028-539-frozen-anisotropic-bulk-cancellation

The prior EXPLORE assessment is
`literature/2026-10-28-anisotropic-constant-field-bulk-cancellation.md`.
Its exact target is the existence and vanishing of the complete
constant-field Wilson/density tensor for every independent constant
12-plaquette weight rho in [1/2,3/2], on the same transverse slice.

The main gap remains the interacting continuum theory with positive
mass. This intermediate test could support a later source-localization
argument for L297's remaining residues. It does not supply that argument,
a finite relative-cube transfer, the higher remainder or the mass gap.
A rigorously nonzero full component stops interval vanishing; a zero
first derivative is inconclusive. A full identity requires convergent
complete contractions and justified regulator passage.

The supplied literature assessment is reused without modification.
It has checked the relevant primary comparisons and ATTEMPTS/047--050;
ATTEMPTS/049 was reopened to retain its Wilson-specific locality
qualification. No cross-notebook input is used. Existing changes in
this notebook are preserved.

## Reasoning checkpoint before calculation

L280 fixes the own-slice ambient jets and full density. L282(6),(15)
fixes its bulk density. L283(13) is the complete single-plaquette
quartic contraction for a constant external field. L287(13) and
L289(4)--(8) fix the two cubic pairings and color normalization.
L297(6)--(8) fixes the requested covariance-removal tensor; it is not
assumed to be a self-energy or an effective action.

In midpoint Fourier coordinates put d_mu=2 sin(q_mu/2),
lambda=|d|^2, P=I-dd^T/lambda, v=d_1 e_2-d_2 e_1, and delta=rho-1.
The intended explicit covariance calculation starts from
lambda P+delta vv^T on d-perp. The projected inverse, all weighted
cubic terms and the weighted L283 quartic contraction will be compared
before any cancellation claim. Integrability and the meaning of the
complete constant-field row sum remain to be established.

No result is claimed at this checkpoint. The work below will preserve
any failed test or incomplete identity rather than approve it silently.

## Intermediate checkpoint

The inverse on d-perp is P/lambda-delta vv^T/(lambda kappa),
where kappa=lambda+delta(d_1^2+d_2^2). For a commuting external
field t u in a fixed color, the two charged Fourier sectors shift
q to q+/-t u. The exponential-coordinate derivative R and the
fixed-slice gauge overlap z=b(q)^*R^-1 b(q+/-t u) enter the
compressed Hessian determinant as

    det_H(R^* K(q+/-t u) R)
      = |det R|^2 pdet K(q+/-t u) |z|^2
          / (lambda(q) lambda(q+/-t u)).

The Haar and both gauge-density contributions must cancel the R,z
factors before integrating. Since pdet K=lambda^2 kappa, the proposed
complete coefficient is -1/2 integral (u dot partial_q)^2
log(lambda kappa). This is a finite-symbol Taylor calculation, not
an assumed effective-action identification or infinite determinant.
Its full proof and infrared passage are still being written.

The independent diagnostic
`scripts/anisotropic-bulk/check-symbol.py` compared the complete
L282/L283/L289 diagonal contraction formulas with this expression
at 80 exact-rational points, covering all directions and five rho
values including both endpoints. All differences were exactly zero;
the complete certificate is
`scripts/anisotropic-bulk/symbol-certificate.json`. These finite
samples are not a proof of the identity or convergence. SymPy was
unavailable; the diagnostic uses only Python's exact Fraction type.

The analytic obligations are uniform symbol derivative estimates,
absolute convergence of the complete cubic kernel including external
curls, and the vanishing small-sphere flux of log(lambda kappa).
No source localization or finite-cube conclusion will be inferred.

## Completed attempt

The complete proof is now canonical in
`lemmas/L299-frozen-anisotropic-constant-field-cancellation.md`.
It establishes the frozen identity throughout the approved interval,
with absolute complete-kernel row sums and the specified regulator
limits. The proof includes the external-curl placements and the
fixed-slice overlap factors; it does not assume a background-gauge
identification. No independent conceptual audit has yet occurred.
The source-localization and finite relative-cube obligations remain
open. The new audit assessment is REVIEW_REQUIRED and has not been
approved within this research turn. Existing failed routes are intact.
