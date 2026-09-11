# Averaging the uniform progression-error budget

Attempt: sum L220's progression-error bound over the actual interior
a,m box, improving the divisor factor by short-interval averaging,
to establish E_box=o(M_box).

WHY IT FAILS: [L222](../lemmas/L222-interior-averaged-progression-error-budget.md)
proves that the resulting uniform budget exceeds the real main term
by at least a factor cN/log N. Divisor pairing does control the
average divisor count, but the bound still charges a constant
endpoint error where the real cell integral is of order 1/N.
This is a failure of the proposed bound, not a lower bound for
the actual signed error. Cancellation of those errors remains open.
