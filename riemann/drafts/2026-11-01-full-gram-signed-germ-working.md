# Full-Gram cancellation-preserving signed-germ test

1 November 2026. One RESEARCH attempt under the unchanged EXPLORE
assessment `literature/2026-11-01-full-gram-log-degree-energy.md`.
The target is the exact full-Gram relative half-budget at length
N=floor(T^(1/100)), with the common real unit observer and full tail.
The main gap remains pointwise initial signs at unbounded heights and
all-degree mixed positivity. A half-budget could give an averaged
detector margin after L623's reference and L622's transfer; it would
not give pointwise positivity. Continue only with a justified sharp
comparison, an informative obstruction, or a materially refined input;
an oversized upper bound proves no obstruction.

Read the used L623 Gram proof, L624 normalization/orientations and
six-term congruence, L627 rational basis and first-jet proof, and L628
full complex-shift proof. The damping estimate acts on the full tensor
space before its inverse is restricted to the finite input. It does
not truncate the output. The analytic C_N remains essential. Reused
the supplied source comparison and collective arithmetic assessment;
no essential new theorem is being imported. No cross-notebook input.
The freezing, prefix-o(1), and absolute-Cauchy stops remain in force.

## In-progress calculation

Use dimensionless z_j=i b_j. The six leading polar terms, after the
leading Hardy phase, have the common symmetric form

    sum_(|I|=2) exp(sum_(i in I)z_i - (sum_j z_j)/2)
        B_N((z_i)_(i in I),(-z_j)_(j outside I);a)/L-scaled
        / product_(i in I,j outside I)(z_i-z_j).

The notation `/L-scaled` means every argument of B_N is divided by L;
it is not an extra scalar denominator. The overall constant is
1/zeta(2). The exact finite-T phase and regular zeta factors still
need a uniform relative error justification before this leading germ
can be used for K_c.

The proposed bounded calculation multiplies the complete six-term sum
by the Vandermonde, performs its polynomial cancellation, and extracts
only the coefficients needed by Q and the common observer. Arithmetic
Taylor degrees through eight are retained. This is not an estimate of
the six singular terms separately. No signed coefficient or small
constant has yet been established. L628 can control analytic errors;
it does not by itself make the arithmetic Taylor remainder small.

## Completed attempt

The proof is canonical in
[L629](../lemmas/L629-full-gram-finite-signed-jet-reduction.md).
The earlier uncertainty is resolved as follows: L628 controls the
regular-zeta and exact-phase replacement by O(Gamma/log T), uniformly
in the coefficient vector and X. Arithmetic degrees above eight do
not contribute to the signed extraction at all. The complete six-term
polynomial cancellation yields 175 rational arithmetic-jet rows.
All rows were checked by an independent full polynomial construction,
exact division by the Vandermonde, and multiplication back. The
untwisted coefficients and pair-conjugation symmetry also pass.

The full certificate is
`scripts/full_gram/signed_germ_certificate.json`; reproduce it with
`python3 scripts/full_gram/signed_germ.py`. The proof states the finite
formulas independently of the program. No actual arithmetic coefficient
or signed eigenvalue was numerically estimated. Relevant complete checks
and first-degree weights were inspected using the shared JSON inspector.

The half-budget remains unresolved. L627's existing scalar first-jet
bound already costs 64/75+O(1/log T) for c=(0,1), compared with a
total allowance 1/2. This is only an upper-bound cost, not an obstruction;
the remaining degrees can cancel it. The norm-to-absolute-jet strategy
is parked. The materially refined input is the uniform finite-jet
reduction, with all degree-eight contributions and no analytic Taylor
remainder. A proposed next test uses the numerical radius of the
centered compressed multiplier, whose scalar quadratic form is exact
even though its output norm would discard components. Its proposed
2 log N+C bound is neither derived nor approved in this turn; its
separate REVIEW_REQUIRED assessment is recorded in PROGRESS.md.

No essential new source, cross-notebook theorem, external service,
delegation, API key, commit or shared-infrastructure edit was used.
The source and Mathlib qualifications are retained in L629. This is
a local uniform-reduction ADVANCE, not progress beyond checked source
theorems by a certified novelty standard, positivity or an RH candidate.
