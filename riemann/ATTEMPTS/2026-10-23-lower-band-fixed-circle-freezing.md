# Closed lower-band fixed-circle freezing test

WHY IT FAILS: [L456](../lemmas/L456-lower-band-fixed-circle-freezing-obstruction.md)
shows that at m/r=7/8 the Euler-normalized concentric-disk interpolation
exponent is strictly greater than 1/2 for every fixed real center and
every admissible fixed collection of radii, including a reserved Cauchy
circle. The explicit valid full-band bound is O((log t)^(2/3)), giving
only M/sqrt(r)=O(r^(1/6)) against the sufficient o(1) threshold.
The non-Euler lower bound, both residues and all relative tails pass;
the central error does not receive a vanishing certificate. This parks
this fixed-circle relative-freezing implementation on the closed band,
not the arithmetic positivity target or every possible logarithmic
estimate. It neither proves an actual negative sum nor excludes a
moving-saddle comparison retaining the linear phase. L330's models and
the L323/L327 and fixed-r stops retain their original hypotheses.
