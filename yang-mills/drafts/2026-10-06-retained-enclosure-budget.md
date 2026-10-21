# Retained-value enclosure attempt

STEP_ID: YM-20261006-049-retained-enclosure-budget

The unchanged SPECIALIZE assessment in
`drafts/literature/2026-09-26-current-target.md` covers this bounded
substep of the combined Ward response. Main gap: ultraviolet-uniform
interacting control and eventually a nonzero physical continuum sector.
Intermediate target: enclose L033's cutoff-112 retained values, with
coefficient, inverse-weight, time-tail and arithmetic errors. A certified
sign would determine a selected upper-face power coefficient via L030;
L019 compensation, other contractions and the full logarithm remain open.

Saved before further work: test L033's full absolute heat-moment majorant
as an error propagator. Each weak-monomial product has eight Fourier
coefficient factors. Normalize their absolute errors by the elementary
L1 bounds 6 and 9. Propagate these errors and relative inverse-weight
errors before considering an expensive interval implementation. Bound
the finite time-window omission analytically. Exact rational evaluation
will compare the resulting sufficient error budgets to the same-cutoff
diagnostic sizes, without treating those diagnostics as lower bounds.
Continue only if a complete enclosure beats the sign threshold; stop this
particular majorant/binary64 certification method if its error budget
already exceeds that threshold under optimistic input-error assumptions.

Relevant duplicates/failures: L033 already bounds the omitted spectrum;
steps 047–048 only reproduce retained values. ATTEMPTS/011–015 exclude
raw forest-loop bounds, interior estimates at the pinned jump, low-mode
lattice global-norm certification and axial annihilation. The present
finite continuum error-propagation test does not reopen those methods.
No fresh general flow or matching theorem is needed; reuse the saved
source assessment. Full input requirements are L008, L030–L033 and the
two existing continuum evaluators. All numerical coefficient/weight
certifications and arithmetic residuals remain unproved until explicitly
enclosed; refinement differences cannot supply them.

## Completed bounded attempt

Outcome: NEGATIVE / RESEARCH / REPRODUCTION; actual task proof_attempt.
The canonical proof is L034. This specializes L033's existing absolute
expansion count with elementary product-error propagation; it does not
claim novelty beyond the inspected sources. The script
`scripts/combined-ward-response/check_retained_error_budget.py` uses exact
fractions and saves its complete certificate beside it as
`retained-error-budget-certificate.json`.

The rigorous ideal time-window tails are at most 0.00149112080440 and
0.00596448321757, below the selected 0.0015 and 0.006 thresholds. These
bounds concern the exact intended time endpoint. They do not certify
its binary64 realization or any finite-window quadrature rule.

The absolute expansion majorants are about (1.00753e30,4.03012e30).
At the illustrative input errors eta=epsilon_s=epsilon_r=2^-52 with
arithmetic residual E=0, the propagated allowances are about
(2.23716e15,8.94865e15), far above the same-cutoff diagnostic values
(453.073657044287,3352.593155019382). This is failure of the sufficient
scalar-budget test, not a proof of a large true error. Even these input
bounds have not been established for the numerical program. The
hypothetical combined budget first beats the diagnostic size at 95 bits
for probe 3 and 94 bits for probe 6, still assuming E=0; that comparison
alone validates no retained value. L034 gives every omitted hypothesis.

The certificate's complete ideal-time-tail values, failed-budget record,
comparison flags and first passing bit counts were inspected with
`python3 ../scripts/loop/inspect_json.py` on their selected pointers using
`--full`. The script proves its time-tail comparisons using exact
rational inequalities. It performs no new high-cutoff signed evaluation.

Stop the scalar-majorant/binary64-scale combination, preserving
ATTEMPTS/016. A materially different error estimator is the nonnegative
tensor sensitivity contraction retaining individual Fourier and mode
weights. Test its coefficient-error contribution for normalized absolute
uncertainty 1e-12 against budgets 100 and 1000; a failure requires higher
precision or another estimator, not another refinement-as-proof claim.
This stays within the unchanged combined-response assessment. All
coefficient input certification, time quadrature and arithmetic error,
I_i signs, L019 compensation, other response terms, finite matching and
the reflected-error threshold c_box/2 remain open. STATUS stays IN_PROGRESS.
This informative negative closes the current exploration test; prior
stopped branches and their evidence are retained. No supervisor state is
edited and no new ready literature assessment is self-approved.
