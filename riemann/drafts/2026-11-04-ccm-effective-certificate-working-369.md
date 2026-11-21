# Step369 — fixed-cell effective prolate certificate working record

Approved target and unchanged assessment: construct the residual/tail
certificate for modes 0 and 4 at lambda=sqrt(13), with all 241 translated
L759 coefficients. This is a SPECIALIZE research attempt, not source work.
The parent assessment and recorded finite-row failure were checked;
L759/L760 supply the basis and later observable definitions. No existing
trial certificate was found in those scoped inputs. Earlier files remain.

Main gap: actual-Xi positivity; downstream purpose is the saved projected
ground/trial observable, still requiring a nonzero boundary denominator.
The bounded test is explicit infinite-mode errors and all coefficient
errors, or an exact unpaid inequality. No limiting result is sought.

Planned certificate: on the even Legendre basis use the first 96 modes
(degrees 0 through 190). The omitted diagonal begins at 192*193.
Because c^2 x^2 is bounded and nonnegative, the omitted compression has
that lower bound. At a threshold t below it, compare finite Schur forms
A-t and A-t-beta^2/(192*193-t) e_last e_last^T. Matching interval LDL
inertias will give the infinite count; a finite Ritz gap alone is unused.
Point numpy eigenvalues suggest isolators (80,82) and (723,726), but
these are candidates only. Certify every pivot and the omitted coupling.

Refine rational polynomial candidates with point Decimal solves; certify
their normalized residuals including beta times their last coordinate.
Once infinite counts isolate the selected modes, apply the spectral
theorem for L2 error, with the corresponding sign choices. Construct the
zero-integral combination using the actual additive integrals, preserving
independent scaling covariance. Transport its errors through the finite
sum r<=13 and the exact du/u coefficient functionals. Integrate polynomial
approximants termwise on each support interval [1/lambda,lambda/r],
paying all transcendental and arithmetic error. No inversion parity.

Unpaid at this checkpoint: every stated interval count, residual, mode
identification, transport bound and coefficient enclosure. No lemma or
mathematical result is claimed yet. The future denominator and 1/10
comparison are outside this step. Arithmetic will use directed Decimal
intervals; complete certificates will be stored under scripts/spectral-triples/.

Completed: the 96-mode cutoff passed all infinite counts but missed the
chosen mode-4 error threshold: 3.8313723e-70 versus required <1e-70.
Both failed script/certificate versions are preserved. Refining the same
mechanism to112 even modes (degrees0,...,222, omitted floor50400) gives
mode errors <2.645e-97 and <4.034e-93, and all241 coefficient component
radii <1.276e-91, versus required <1e-65. Full proofs and software
qualifications are canonical in L761; the full certificate and complete
evidence check are in scripts/spectral-triples/ccm-trial-*-369.json.
The second check inspected every saved pivot/residual/rectangle and used
an alternate determinant recurrence plus separately grouped support
integrals. It is a consistency check, not the deferred conceptual audit.

No denominator division, ground/trial observable, new source assessment,
family assertion or RH candidate was produced. The main argument in
PROOF.md is unchanged; this finite prerequisite is not assembled into
an actual-Xi proof. The exact next audit is newly nominated with
REVIEW_REQUIRED coverage. Existing source assessments were not rewritten.
