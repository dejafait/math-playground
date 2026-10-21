# Residual-pair quadratic root-count test

Tested on 2026-10-04 under the saved correlated-cubic EXPLORE assessment.

## WHY IT FAILS

[L018](../lemmas/L018-residual-pair-elimination-and-root-count-limitation.md)
eliminates the residual roots from the signed energy exactly, including
the zero-difference branch and all cases with |S minus T|<=2. Fixing all
but one subset root gives a quadratic, but its generic two-root allowance
is too coarse: the resulting valid upper certificate necessarily exceeds
the sufficient energy threshold by more than 6.14e14, even before paying
for the unresolved degenerate configurations. This is a lower bound on
the method's upper allowance, not on actual energy or list size. The
remaining signed counts for larger symmetric differences have no effective estimate. Park
the energy route rather than repeat elimination or a different norm;
the degree-67 family's maximum remains open. A materially different
proposed witness mechanism uses a pole at zero and subset sum/product
constraints; it requires its own literature screening before mathematics.
