# Mixed-cubic residual covariance test

STEP_ID: YM-20261007-076-mixed-residual-cross-covariance

Reuse `literature/2026-09-26-current-target.md` without changing its
SPECIALIZE target. Main gap: the complete ultraviolet Ward response and
interacting matching. The bounded intermediate test is whether the
upper-noise covariance with the conditionally centered transverse links
is localized uniformly in axial depth. Such a bound could control the
retained correction kappa(f,r,H-M)+E_mix before the logarithm is extracted.
Continue on a full-spectrum summable covariance estimate; abandon
uniform boundary localization if an actual spectral sector has a
nondecaying cross block. This is not a test of a signed-cumulant sign.

Read L026, L028, L048-L050, L054, L058-L059 and the latest local
continuation. L058 computes the covariance with transverse *curvature*,
not with each link entering its other cubic derivatives. L059 only
estimates the conditional quartic. ATTEMPTS/017's rough-defect obstruction
is preserved; neither conditional centering nor external heat damping
is a covariance estimate. No new external theorem is needed beyond the
already covered finite Gaussian regression and relative spectral calculus.

Working calculation, saved before verification: set t_s=s/N,
beta_s=sum_(ell<s) z_1(ell)-t_s u and
xi_s=z_T(s)+T beta_s=x_T(s)-t_s Tu. Then xi is independent of u.
The candidate exact cross block is
Cov(eta,xi_s)=-t_s P-g_N(s;Delta_T)(I-P).
The scalar identity needed is
lambda sum_(ell<s) (L_E+lambda)^(-1)_(N-1,ell)=g_N(s;lambda),
where L_E is the interval edge Neumann Laplacian. Its proof should use
the summed recurrence and its endpoint conditions. If correct, the
gradient block survives throughout the box; the curvature projection
in L058 deletes it, but the complete cubic derivative need not.

No a^2-scale bound for the actual correction has been obtained. Check
the scalar identity, gradient projection, all boundary rows, and the
distinction between link and curvature derivatives before recording a
result. Other cubic pairs, response jets, matching and the reflected
error <=c_box/2 remain independent gaps.

Completed test: L060 proves the candidate exact cross block and the
concatenated squared norm (N-1)(2N-1)/(6N). Its gradient sector alone
violates the proposed N-independent bound. The proof retains all modes
and end edges; the scalar identity follows from L_E=B^T B, L_D=BB^T
and the summed resolvent recurrence. A single transverse cubic has a
nonzero derivative along a gradient direction, so the curvature
projection alone cannot delete this block. The canonical proof and
qualifications are in L060; ATTEMPTS/018 records the stopped shortcut.

The result is an informative NEGATIVE for localization, not a scaled
bound for the retained correction. Continue under the unchanged target
and assessment by testing its signed gradient-sector contraction using
L011, L019, L028, L048-L050, L058-L060 and C057a. Keep both observable
derivatives and all plaquettes. No separate forest invariance, negligible
correction, or compensation is assumed. A cancellation must be proved
for the actual contraction; an operator norm or a single-vertex example
cannot decide it. The complete mixed scale and logarithm remain open.
