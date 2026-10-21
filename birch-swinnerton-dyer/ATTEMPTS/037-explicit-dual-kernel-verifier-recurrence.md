# Explicit dual kernel — first independent replay stopped

2026-10-16, step 262. This is an implementation failure in the fixed
BMSS dual-kernel attempt, not a mathematical obstruction to dual kernels
and not a reopening of ATTEMPTS/035--036.

## WHY IT FAILS

Production wrote a whole-field candidate but the independent replay failed
`dual_after_quotient_division_degrees` before constructing either composite.
The new verifier transcribes psi8/Y with factor 8 instead of the factor 2
required by the standard division-polynomial recurrence already used in
L068. The precise diagnosis, source citation, limitations, timings and
preserved evidence are in
[the attempt record](../drafts/2026-10-16-explicit-dual-kernel-attempt.md).
The one production and one replay stage each stayed below 180 seconds;
the first failure ended this invocation's arithmetic. The original script
and candidate coefficients remain unmodified. No actual dual identification,
whole affine-line presentation, Selmer enclosure or BSD advance is claimed.
A fresh bounded replay after fixing this transcription, with the same
ready target and independently checked normalization, is justified; no
new mathematics or algorithm approval is inferred from this diagnosis.
