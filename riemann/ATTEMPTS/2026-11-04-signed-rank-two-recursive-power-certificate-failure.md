# Signed rank-two recursive rectangular Fourier powers

Step435, one fixed mathematical calculation; informative implementation
negative, with the requested sign/norm comparison inconclusive. The
canonical calculation, hypotheses, complete analytic bounds and evidence
are in [L779](../lemmas/L779-actual-rank-two-fredholm-inconclusive-certificate.md).

WHY IT FAILS: At (3,2048), both required count2 contours and true simple
grouping are certified, but recursive complex rectangular Fourier powers
make the high-mode coefficient errors enormous. The complete 512-mode
weighted error exceeds1.285e8, while its certified infinite-tail component
is below1.722e-17. The resulting trace-norm error cannot transfer the
positive finite determinant or finite norm>1 to the actual operator.
This is not a negative minor, a norm obstruction or a global signed-route
stop. No automatic refinement was made. Reopening requires a separately
assessed change to phase enclosure, with a full error certificate; merely
increasing precision or trying another radius is not the proposed next step.

The original unnecessary root-width assertion failure was retained and
resolved using the same fixed computation's wider strict bracket. A checker
adaptation typo was corrected; the final complete saved-data check passed.
Neither correction is claimed as mathematical progress beyond the sources.
