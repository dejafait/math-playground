# Robin even-quartic fixed-rectangle stop

Step 69 establishes the restricted obstruction in
[C681a](../lemmas/C681a-robin-quartic-fixed-rectangle-obstruction.md).
The complete exact certificate is
`scripts/one-sided-hankel/robin-quartic-three-point-certificate.json`.
The earlier finite-polynomial step-43 search remains inconclusive;
its different kernel and conclusions have not been changed.

WHY IT FAILS: on L681's fixed right edge, a positive combination of three
exact point costs cancels both even-quartic coefficients and exceeds
-0.007589. C681a transfers this to a finite-n lower bound for the uniform
absolute integrand, ruling out this sufficient estimate at rate above
1/100 even for n-dependent coefficients. Further coefficient tuning on
this fixed rectangle cannot repair it. This does not lower-bound the
complex contour integral or the full residual and does not exclude other
contours, other multipliers or arbitrary positive weights. Direct signed
residual estimates are an independently testable continuation.
