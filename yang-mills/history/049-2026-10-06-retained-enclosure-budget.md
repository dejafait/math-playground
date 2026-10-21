# 2026-10-06 — Retained enclosure budget

STEP_ID: YM-20261006-049-retained-enclosure-budget

RESEARCH / REPRODUCTION / NEGATIVE; actual task proof_attempt. Reused the
unchanged SPECIALIZE combined-response assessment. One bounded enclosure
attempt yielded [L034](../lemmas/L034-retained-fourier-error-budget.md):
a conditional coefficient/weight/arithmetic error budget and rigorous
ideal-window tails below 0.0015 and 0.006. The exact rational certificate
is `scripts/combined-ward-response/retained-error-budget-certificate.json`.
No actual retained-value enclosure was completed.

The scalar majorant at illustrative 2^-52 input error gives allowances
above 10^15, exceeding the same-cutoff diagnostic sizes. Record this
method's failure in [ATTEMPTS/016](../ATTEMPTS/016-scalar-binary64-retained-enclosure.md).
It does not establish large actual error or stop all sign certification.
The precision test first passes its hypothetical budget at 95/94 bits,
with arithmetic error artificially set to zero; those assumptions remain
undischarged. This is elementary propagation of L033, not claimed progress
beyond the inspected literature or on the complete logarithm.

Reassess using a different error estimator: a nonnegative tensor
sensitivity contraction retaining actual Fourier and mode weights.
The selected test is its coefficient-error contribution at normalized
uncertainty 1e-12, compared with budgets 100 and 1000. Success only
licenses subsequent rigorous input/weight/rounding validation. Essential
inputs remain L008, L030–L034 and the two continuum evaluators; L019
compensation and the full response remain open. This informative negative
resolves the current exploration test; prior stopped routes are preserved.
