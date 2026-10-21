# 2026-10-06 — Retained tensor Fourier sensitivity

STEP_ID: YM-20261006-050-retained-tensor-sensitivity

RESEARCH / REPRODUCTION / EXPLORATION; actual task calculation. Reused
the unchanged SPECIALIZE assessment for the combined Ward response.
[L035](../lemmas/L035-retained-tensor-fourier-sensitivity.md) records a
conditional nonnegative modewise error contraction, replacing the failed
scalar majorant of ATTEMPTS/016 without discarding its evidence.

At cutoff 112 and illustrative normalized Fourier uncertainty 1e-12,
the diagnostic allowances are about (5.04e-7,1.83e-6), below budgets
(100,1000). A small-cutoff dense/subset check and time refinement pass.
Complete evidence is saved in
`scripts/combined-ward-response/retained-tensor-sensitivity-certificate.json`.
These passing diagnostics license validation, not a certified sign, input
error or full coefficient. The result is elementary specialization, with
no claim beyond the checked literature. One exploration turn is used.

Continue by proving a uniform exact coefficient-quadrature error
<=1e-12 H_h for h=0,1 and |n|<=224 at degree 144. The exact rho and
four-panel rule are retained. Essential inputs: L008, L033–L035 and
the existing Fourier integrator. Stored-node/transform rounding, weights,
tensor arithmetic, L019 compensation, other jets and the reflected
threshold <=c_box/2 remain unresolved, not premises. The existing
assessment stays unchanged and reusable for the same saved target.
