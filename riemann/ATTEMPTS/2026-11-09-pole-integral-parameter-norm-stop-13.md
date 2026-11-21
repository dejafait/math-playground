# Coupled pole integral: parameter-norm estimate stopped

9 November 2026, step13. The full derivation and finite bounds are in
[L930](../lemmas/L930-pole-integral-regular-residual-and-norm-floor.md),
awaiting a separate conceptual audit. The exact pole integral and the
O(1/log T) full-metric regular residual are retained partial inputs.

## WHY IT FAILS

After combining the two pole endpoints into one entire-family derivative,
the proposed triangle estimate integrates its pointwise operator norms.
Even exact norms at every parameter have a certificate floor
1-O(1/log T), by L930(14), so this estimate cannot establish <=1-eta
for fixed eta>0. This loss is not an uncontrolled regular-zeta residual:
L930(12) bounds that residual in both complete energy metrics. It is the
loss of cancellation between interpolation parameters. The actual pole
operator has only the displayed lower and loose upper bounds; no norm
counterexample, joint-gap impossibility or sufficient weaker margin is
proved. Stop this specific integral-norm estimate. Reopening requires a
materially different estimate retaining parameter cancellation or new
input; more parameter samples or Schur weights do not remove its floor.
L929's distinct termwise stop and the step226/approval-loop stops retain
their scopes. Joint projection, signed realization/transfer and Xi signs
remain open.

Subsequent review, 9 November 2026 step15: the separate conceptual
audit in the same canonical L930 validates the residual and this
certificate-only stop without correction. The step13 pending-review
wording above is retained as historical context; the true operator's
fixed or sufficient shrinking gap remains unresolved.
