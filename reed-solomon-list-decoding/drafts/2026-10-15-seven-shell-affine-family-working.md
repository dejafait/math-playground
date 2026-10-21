# Seven-shell affine family — step 232 working record

Approved target: test L067's unchanged 24-weight dual over the nonnegative
L065 three-parameter column family, retaining the complete L061/L062 base,
original positive rho and pairs, Boolean/forbidden rules and all unordered
presentations. Prior SPECIALIZE assessment:
`drafts/literature/2026-10-15-seven-shell-affine-family-fixed-dual.md`.

Main gap remains arbitrary-center safety at 67/68 agreements. A uniform
strict negative bound would widen the prescription excluded by this dual;
an exact admissible nonnegative value would stop only its uniform-family
claim. Other duals, base/pairs, global PSD, labels and RS realization remain
independent gaps. Preserve L061–L067 and ATTEMPTS/043,048,049.

Attempt in progress: recover every column coordinate as an affine vector
in (1,u,v,w), check all full-region presentations, derive the unchanged
dual's quadratic right side using the full anchored Schur reduction, and
check singular ranges coefficientwise. Try the unconstrained quadratic
maximum first as an upper bound; if that does not decide negativity, seek
an exact admissible point or a constrained global certificate. No numerical
proposal alone is evidence. Complete coefficients/certificates will be
saved under `scripts/finite-support/`.

Constructor result (pending independent substitution): all extra unordered
equalities are affine identities; all 64 singular ranges hold throughout
the family. The fixed dual quadratic depends only on w, has rank-one
negative curvature, and its global maximum is exactly zero at
u=v=0,w=M_03/(-M_33), with M the homogeneous objective matrix in the
constructor certificate. All 49 free entries there are nonnegative,
47 positive and precisely f_27=f_33=0. The initial curvature check
incorrectly stopped at a leading zero diagonal; its failed report is
preserved as `seven-shell-affine-fixed-dual-initial.json`. A positive
diagonal square decomposition fixes that check without changing any
mathematical input or objective. The final constructor passes 2077 checks.

The independent direct-subset presentation and determinant-form Schur
verification is now complete: all 7315 checks pass, including ten exact
quadratic evaluations, every original weighted kernel residual and the
direct exact weighted zero. Canonical proof, precise definitions,
qualifications and full certificate paths are in
`lemmas/L068-seven-shell-affine-family-fixed-dual-zero.md`; the route
stop is in ATTEMPTS/050. No other dual or completion search was attempted.
The initial verifier's field-name error stopped before any report and was
corrected to use the existing `kernel_basis` field. Separate critical
review remains pending under the REVIEW_REQUIRED continuation recorded
in PROGRESS.md.
