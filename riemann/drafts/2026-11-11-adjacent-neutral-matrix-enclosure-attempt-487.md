# Matrix enclosure attempt, step487

Approved target and assessment are unchanged from step486/step483.
The main gap is L030-L032/C032a actual-Xi positivity. A positive common
margin for the complete neutral E+/-2X forms could pay nearest-neighbor
interactions through C744i(6); remote, non-neutral, odd and global signs
remain independent gaps. Existing degree128 failures are preserved.

This bounded implementation attempt uses C744j(1)-(9), C744k(1)-(12)
and C744l(1)-(9). First enclose an actual principal Schur block with
indices 2,3,256, including all257 projection rows and the complete L2
Gram product. These columns test both low parities and the worst-degree
power-basis cancellation. The sought full certificate is still both
255-dimensional matrices >=I/25. A positive principal block alone
cannot establish it; failed sufficient lower bounds alone do not
refute the fixed target. Save all coefficient and matrix enclosures.

Continue on a reproducible certified block calculation with explicit
rounding/error charges; otherwise save the failed arithmetic budget.
The unchanged ready target permits further implementation, not a new
analytic mechanism or an assertion that C744i/j/k/l have been audited.
No literature turn, cross-notebook input or changed hypotheses are used.

## Completed bounded attempt

C744l Section6 contains the canonical arithmetic proof, qualifications
and reproduction commands. The implementation constructed enclosed
P/Q coefficient arrays for all three pieces and both signs on columns
2,3,256. It evaluated all257 projection rows and complete Gram products
for this principal block, retaining all mixed terms and subtracting
the full projection covariance. Exact integer convolution and rational
power-log integration retain cancellation before rounding; explicit
coefficient L2 errors and interval operations pay all arithmetic here.

All7 computation checks pass. The principal Gershgorin lower bounds
exceed0.5879 and1.1655, with maximum matrix widths<1.046e-236 versus
the requested1e-30. All13 saved-matrix replay checks pass. Full operands
and failures are in `scripts/adjacent-neutral/matrix-enclosure-487.json`
and `scripts/adjacent-neutral/matrix-replay-487.json`; the coefficient
archive is `scripts/adjacent-neutral/matrix-coefficients-487.json.gz`.
The first slower run stopped after saving coefficients; the completed
run uses a common Legendre recurrence for projection polynomials and
has no unpaid numerical quadrature or hardware-rounding assumption.

This is local implementation progress using known tools, not progress
beyond the compared general sources. C744i/j/k/l remain independently
unaudited. A positive principal block is insufficient for the complete
finite matrix: all omitted columns4,...,255 and their interactions are
still unpaid. No full neutral mu, strict-half ratio, smooth witness or
RH conclusion has been established. PROOF.md and DAG.md are unchanged.

Continue the same exact ready target with the remaining columns and
complete finite matrix enclosure. Use the current selected-column
evidence as an arithmetic check, never as a bound on the omitted
directions. The original1/25 sufficient threshold and every prior
failure remain in force. A new creative mechanism is not selected
merely to meet a scheduling target while this specific certificate
remains independently testable and incomplete.
