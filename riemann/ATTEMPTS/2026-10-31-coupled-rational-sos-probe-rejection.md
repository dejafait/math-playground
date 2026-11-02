# Coupled rational SOS probe: one candidate rejected, family unresolved

The approved P4/q family retains the exact denominator, all quartic
coefficients, both global branches, full K and closed-I cone condition.
The bounded sufficient SOS search used the stricter cost 1/300, two
40-by-40 Gram matrices, and one numerical refinement.

WHY IT FAILS: [L594 Section 5](../lemmas/L594-coupled-rational-global-certificate-reduction.md)
records the surviving coefficient/PSD defects and an exact rational
counterexample to one explicitly rounded iterate. Its full trace cost
is below 1/288, but the first global branch is less than -1/200 at the
recorded point. This refutes that candidate; neither the projection
residual, this point, nor failure at the stricter trial cost excludes
the SOS subclass or the P4/q family. Preserve the exact evidence and
do not count further iterations of the same projection as a new idea.
The ready unchanged target can receive a refined acceleration-Schur
and covariance-scaled test. General clipping and Xi transfer remain open.
