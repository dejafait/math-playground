# Upper-face cubic conditioning — bounded working record

Approved scope: the unchanged SPECIALIZE combined-response assessment
`literature/2026-09-26-current-target.md`; actual task: proof_attempt.
Essential inputs: L011, L018, L026, L029, L048. L019 remains the
full-response interpretation constraint, and L047 supplies the selected
power comparison without being a premise of the proposed identity.

Main gap: complete cutoff response and interacting matching remain open.
Intermediate target: condition the upper-face cubic pair on its axial-zero
potentials, obtain a uniform covariance bound for the remaining curvature
noise, and retain the corrections caused by both quadratic observables.
Downstream use: expose an exact compensation mechanism against the
upper-face quartic before attempting its scaled response. Continue if
conditioning yields a complete identity with boundary rows and derivative
terms; abandon replacing the conditional observable by its unconditional
mean or claiming compensation from an action-only square completion.

Checked for duplicates/failures: L048 contracts the full cubic sum but does
not condition it; L029 gives local Cov(H,d)=Cov(H,L)/N, not the global
conditional contraction. Relevant upper-face drafts and ATTEMPTS/011,
013 preserve raw-loop growth and the pinned-jump obstruction. No new
source premise is required: this is finite Gaussian specialization under
the ready assessment, not a reproof of bulk renormalization.

Saved before completing the proof: write u(v) for the upper axial path,
ell_e=u(v)-u(v'), d_e=ell_e-T_e, eta_e=d_e-ell_e/N.
The zero-axial-mode identity suggests eta is independent of the whole u
field and Cov(eta)=Cov(d)-(1/N) T G3 T^T, between zero and identity.
For Q_e=u(v) cross u(v'), S3_top=(1/2) sum eta_e dot Q_e.
Conditional averaging of S3_top^2/2 gives Q^T Cov(eta) Q/8; this
alone cannot replace the two-cubic cumulant, since f and r depend on eta.
The required second Gaussian integration-by-parts corrections are being
retained. No cutoff limit or cancellation is assumed.

Completed: L049 proves the global regression, 0<=K<=I, the pointwise
quartic defect bound and the exact top/top cumulant identity with both
observable derivative terms. All ten exact finite surrogate checks pass
in `scripts/combined-ward-response/upper-cubic-conditioning-certificate.json`;
the complete checks and failures were inspected. These check algebra,
not actual-box values or asymptotics. This is local standard Gaussian
reproduction, no originality claim. No a^2-scaled estimate was obtained.

Continuation under the unchanged approved target: use L049's exact
-Kappa(f,r,Z+R)+E identity to test the scaled upper-face action group
against L047, retaining all covariance directions and derivative terms.
Essential mathematical inputs are L011, L018, L026, L029, L048, L049;
L030/L047 supply the selected comparison and L019 constrains the
full-response interpretation. Unresolved assumptions: no small identity
deficit, vanishing derivative correction, scaled limit or top/non-top
pair bound is available. Continue on a proved bound or limiting class;
abandon action-only conditioning if it drops R, E or cross plaquettes.
Measure, insertion/flow jets and the full logarithm remain unresolved.
