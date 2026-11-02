# Individual finite-residue recovery: coefficient/Mahler transfer stop

The exact family, complete proof, source imports and qualifications are
canonical in [L667](../lemmas/L667-finite-residue-recovery-mahler-cost-stop.md).
The test used the approved full-spatial fixed-angle assessment, all M
moments, actual complex weights and actual spatial degree. It supplies
new quantitative negative evidence and no counterexample to the target.

WHY IT FAILS: the constant coefficient of every exact finite inverse
row already has an exponential norm cost. Complete-product magnitudes
cannot compensate for it. Even the best individual row followed by
the degree-indexed coefficient inequality and triangle inequality
produces a lower value with a loss exceeding the allowed rate; positive
mixing of these row inequalities does not help. This bounds the value
certified by the transfer, not the true logarithmic mean. Signed row
combinations before taking absolute values, sparsity-sensitive bounds,
and full-root arguments are not ruled out. Repeating an individual row
or a looser inverse-norm estimate cannot repair this diagnosed loss.

The proposed continuation tests one prescribed signed combination,
interpolation of the actual inverse weights with degree at most M-1.
Its uniform coefficient cost is unproved and its changed exact target
has REVIEW_REQUIRED coverage. No new cancellation mechanism has yet
been derived. The older ambient/scalar/anchor stops remain intact.
