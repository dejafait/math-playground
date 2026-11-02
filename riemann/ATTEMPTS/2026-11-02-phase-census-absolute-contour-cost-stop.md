# Half-turn phase census: absolute contour estimate stopped

The exact census, rational kernel, full-polynomial contour and quantitative
cost comparison are canonical in
[L661](../lemmas/L661-phase-census-absolute-contour-endpoint-cost.md).
This tests the proposed nonuniform integer census, with phase mesh pi,
unit residues and the fixed rectangle of imaginary half-height 1/8.

WHY IT FAILS: The absolute contour cost already contains an endpoint
segment whose cost, divided by exp(-n/32)*sqrt(D), is at least
c*n^(-1/2)*exp(9n/100000). The denominator here uses an upper bound on
the actual squared-residue D, obtained from the improved full-family
envelope in L661. Thus this absolute-value estimate cannot certify the
census as an all-angle logarithmic countersequence. The statement is
about the cost of this contour representation, not a lower bound on the
signed response or H. It does not rule out the census, another phase
mesh or contour, or cancellation of the endpoint terms. Further work
must test that signed cancellation quantitatively, rather than repeat
the same absolute estimate. The paid criterion, Xi transfer and signs
remain open.
