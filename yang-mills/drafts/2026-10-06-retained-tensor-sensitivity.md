# Retained Fourier tensor sensitivity — working record

STEP_ID: YM-20261006-050-retained-tensor-sensitivity

The main gap remains the complete interacting Ward response and, downstream,
an ultraviolet-uniform reflected error <= c_box/2. This bounded calculation
stays within the unchanged SPECIALIZE combined-response target. Its
intermediate target is the cutoff-112 nonnegative coefficient-uncertainty
contraction at eta=1e-12, compared with budgets 100 and 1000 for probes 3
and 6. Passing licenses validation of inputs, inverse weights and arithmetic;
failure calls for higher precision or another estimator. Neither outcome
evaluates the full response or proves its logarithm.

Essential inputs: L008, L030–L034 and the existing pure-sector and tensor
evaluators. ATTEMPTS/011–016 are preserved. The scalar full-spectrum
majorant in ATTEMPTS/016 failed; actual modewise propagation has not been
tested. No additional literature is needed for these unchanged elementary
finite-product and separable-weight applicability differences. The saved
source assessment imports the general flow/matching results by citation;
none certifies this numerical specialization.

For each one-dimensional weak integral, let b be the absolute approximate
value and let d=eta times its absolute Fourier multiplier sum with H_0=6,
H_1=9. Exact parity exclusions are imposed before the expansion. A product
of two integrals has baseline B=b_1 b_2 and allowance
D=d_1 b_2+b_1 d_2+d_1 d_2. For each pair of operator monomials, form four
nonnegative coordinate sums with the heat factors. Propagate their product
allowance by E_new=E(B+D)+P D, P_new=P B, starting at (P,E)=(1,0).
Integrate against the two positive inverse-weight measures and sum with
absolute combined rational monomial coefficients and factor 8. This retains
all allowed components and frequencies, avoiding subtraction of nearby
products. The precise conditional statement and proof will be canonical.

Unresolved assumptions: no certified Fourier input error, time-rule error,
phase/heat/derivative rounding error or total arithmetic enclosure; L019
compensation, other action classes/pairings and other jets are not premises.
First cross-check the small-cutoff sensitivity against a dense contraction,
then measure cutoff 112 with the previously tested positive time rule.

## Completed bounded calculation

The canonical conditional statement and proof are in
[L035](../lemmas/L035-retained-tensor-fourier-sensitivity.md). The script
`scripts/combined-ward-response/check_retained_tensor_sensitivity.py`
stores its complete diagnostic evidence in
`scripts/combined-ward-response/retained-tensor-sensitivity-certificate.json`.
The full small-cutoff arrays, refined totals, inverse-weight discrepancies,
refinement differences and failures were inspected, not merely previewed.

At eta=1e-12 and M=112, the degree-12 time-rule allowances are
(5.042079728032214e-7,1.8312544018601046e-6), against budgets (100,1000).
Baseline diagnostics are (8495.60481190369,30374.13867740209).
The independent dense/subset contraction at M=2 agrees to relative
1.793e-14 against 1e-11. Time degrees 8/12 agree to relative 4.283e-16
against 1e-9; the finite-spectrum inverse-rule diagnostics pass 1e-11.
No check failed. These are binary64 observations and no input or arithmetic
error is thereby proved.

Outcome EXPLORATION: the requested bounded estimator test passes
diagnostically and supports continuing, while no retained value or sign is
enclosed. This is elementary reproduction/specialization, with no claim of
progress beyond the inspected literature. The scalar-majorant failure is
preserved in ATTEMPTS/016. A narrower actual coefficient-input bound is
now justified as the next test. Reuse the unchanged approved response
assessment; no new literature assessment is written or self-approved.

Continuation: prove the uniform exact quadrature error <=1e-12 H_h for
h=0,1 and |n|<=224 for the degree-144, four-panel coefficient rule with
L008's exact rho. Essential inputs are L008, L033–L035 and the
Integrals implementation. Arithmetic of the stored nodes, phases,
transforms and tensor contraction is separate and still unvalidated.
Passing this input test would supply only one hypothesis of L035;
the time/weight and arithmetic allowances, compensated response and
interacting reflected threshold remain unresolved.
