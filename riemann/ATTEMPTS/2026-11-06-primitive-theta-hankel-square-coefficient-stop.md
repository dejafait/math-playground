# Fixed primitive-theta Hankel square — coefficient stop

The approved unshifted Lebesgue-half-line operator with kernel K(x+y),
A=H_K^*H_K, and the single normalization c=S_1/Tr(A) fails at z^4.
[L876](../lemmas/L876-fixed-primitive-theta-hankel-square-coefficient-mismatch.md)
contains the complete proof, precise standard operator citations and
qualifications; its certificate is
`scripts/primitive-hankel/coefficient-test-24.json`.

WHY IT FAILS: the normalized positive operator has too large a second
trace: c^2 Tr(A^2)-S_2 lies strictly between 0.00021317 and 0.00050451.
This is an all-half-line enclosure using the exact theta series with
bounded omissions, not a finite-sample fit. The first coefficient is
fixed correctly, so the nonzero residual disproves this determinant
identity already at the second coefficient. Stop this ansatz; no higher
coefficient sweep or fitted weights/shifts/prefactors/rank corrections.
The result is newly specialized and not independently audited. It does
not refute RH or positive-operator approaches with genuinely different
independent input. The arithmetic-to-logarithm interface remains open.
