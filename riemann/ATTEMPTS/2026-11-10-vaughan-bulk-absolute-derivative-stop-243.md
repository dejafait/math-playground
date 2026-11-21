# Uncentered Vaughan bulk derivative payment — stop, step243

10 November 2026. The approved SPECIALIZE test is completed in
[L985](../lemmas/L985-vaughan-bulk-slow-phase-and-fixed-order-loss.md).
This is REPRODUCTION and an informative scoped negative, not a
new arithmetic bound beyond the checked tools or a disproof of RH.

WHY IT FAILS: the exact degree sum retains an exp(u/2) amplitude.
Its dyadic Type I phase has scale comparable to 1; coefficient-aware
Type II Cauchy yields differenced scale comparable to h/n, including
the diagonal and near diagonal. The approved derivative bounds give
no power saving. After amplitudes and all compensating pieces are
restored, the available absolute majorants have exponential rate 1,
including fixed-order errors; the target requires every positive
rate. This stops the specified uncentered absolute estimate chain.
A large upper bound is not evidence that the actual B_n or its
remainder is large or positive. Reopening needs a specific signed
compensation or arithmetic correlation input removing this loss.

The new source nomination asks about centering before these absolute
estimates. It is REVIEW_REQUIRED, with no centered decomposition or
estimate yet proved. Preserve the independent step233 lobe-sign,
step235 automatic-average and step240 criterion-only stops.
