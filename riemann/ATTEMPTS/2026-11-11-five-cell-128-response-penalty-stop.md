# Fixed five-cell response-penalty certificate stop

11 November 2026, step455. The completed bounded calculation is
[C744b](../lemmas/C744b-five-cell-128-response-penalty-certificate-obstruction.md),
with exact witness, derivation, source citations and full interval
certificate. The separate conceptual audit in step457 accepts that
fixed-certificate obstruction; its full reasoning is in C744b.

WHY IT FAILS: With precisely penalty 256, responses 0 through 127,
4096 retained modes per parity and covariance prefix ending at 16384,
an exact dyadic even vector in the first 64 modes has lower-comparison
energy below -2.288e-8. Both complete-complement floors are positive,
but the retained matrix itself has a negative direction, so no positive Schur
lower matrix can lie below it. This settles this fixed certificate
before covariance assembly. It does not refute the complete penalized
form, U_5 positivity or RH: the discarded physical responses j>=128
are nonnegative and unpaid, and the witness is not an exactly neutral
compact smooth test. Keep the source-certificate blockers parked.
Any later reopening needs a covered mechanism that recovers the lost
positive responses or a different signed comparison; unchanged reruns
and silent parameter changes are not continuations.

Step457 reproduced the original certificate byte for byte, checked
the full enclosure chain and accepted the lower-form/Schur implication.
The stop remains in force for the fixed truncated comparison. An
all-response evaluation of this same witness is a different proposed
diagnostic, requiring its own source/domain review; none was performed
in the audit.
