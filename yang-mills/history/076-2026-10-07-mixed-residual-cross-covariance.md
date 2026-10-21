# 2026-10-07 — Mixed residual cross covariance retains a bulk gradient block

STEP_ID: YM-20261007-076-mixed-residual-cross-covariance

[L060](../lemmas/L060-mixed-cubic-residual-cross-covariance.md) computes
the full upper-noise/conditional-link cross covariance and its exact
concatenated norm. This supplies a new negative test of uniform boundary
localization, recorded in [ATTEMPTS/018](../ATTEMPTS/018-mixed-residual-boundary-localization.md).
The surviving gradient sector is absent from L058's curvature projection;
a single cubic derivative does not generally annihilate it. Local
conditional variance bounds and the exact endpoint identity provide
additional analytic checks. No mathematical script was needed.

Outcome NEGATIVE, completed kind RESEARCH and classification REPRODUCTION
under unchanged SPECIALIZE coverage. This changes the estimate to pursue,
not the sign or size of either actual mixed response. The complete
correction kappa(f,r,H-M)+E_mix still has no a^2-scale bound. No result
beyond the checked sources or full logarithmic coefficient is claimed.

Continue by retaining and contracting the exact gradient cross block
jointly with both observable derivatives; do not repeat boundary
localization or conditional-centering shortcuts. L011, L019, L028,
L048-L050, L058-L060 and C057a fix the relevant response and comparisons.
Other/other cubic pairs, remaining jets, subleading powers/logarithms,
interacting reflected error <=c_box/2 and continuum/mass obligations
remain open. Existing changes and prior stop evidence were preserved.
