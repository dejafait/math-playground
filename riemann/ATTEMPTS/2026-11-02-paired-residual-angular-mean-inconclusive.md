# Paired residual angular mean: bounded test inconclusive

The exact mean and its qualifications are in
[C673d Section 5](../lemmas/C673d-angular-pair-real-crossing-stop.md),
specializing the existing C645o residue formula. The complete numerical
diagnostic is
`scripts/one-sided-hankel/positive-cone-angular-mean-screen.json`.

WHY IT DOES NOT DECIDE THE TARGET: the residue formula retains all
interior angular poles and gives a valid norm-one scalar observation,
but no signed asymptotic estimate was obtained. Decimal precision
agreement and agreement with small-size angular quadrature do not bound
roundoff or the unbounded-q tail. The observed means change sign, and
the tested values cannot establish decay on either side of rate 1/100.
Even a sufficiently large mean on one unbounded subsequence would only
exclude these coefficients as a countersequence on that subsequence;
other q and the infimum over all coefficients would remain open. A small
mean gives no upper bound for the residual norm.

Park the scalar test without declaring the witness or cone bound false.
The next proposed mechanism is a positive-real action on the entire
pole-parameter interval, with a paid angular representer. Its essential
representation-theorem coverage is missing and is nominated separately
as REVIEW_REQUIRED. The contour, polar-repair and Gram stops remain
unchanged; none is a global ban on angular separation.
