# Rotation-uniform Chebyshev ellipse envelope — bounded method stop

The target was the saved common-pole angular root-mean-square Hankel
bound at exponent 1/32. One attempted countersequence reused C645l's
Chebyshev poles for every angle and tried to extend its global ellipse
quadrature estimate uniformly. The exact obstruction is proved in
[C645m](../lemmas/C645m-rotation-uniform-chebyshev-ellipse-envelope-stop.md);
its proof has not yet received an independent audit.

WHY IT FAILS: At theta=pi/2 the grid is the real segment of points -j/n.
The rightmost point of every allowed ellipse makes the inverse-grid
weight grow faster than the Chebyshev denominator suppresses it. The
specific quadrature majorant is > (8/11)exp(s*n/12) for n>=39, including
any positive shrinking choice s=s_n<=1/10. A lower bound on this upper
bound supplies no lower bound on the actual error. Neither the initial
finite endpoint screen nor the old fixed-angle arc gain controls that
cost. Therefore this envelope cannot certify an angular countersequence.

The angular target, the Chebyshev family itself and the actual error
remain open. A refined test can use exact angular Laurent coefficients
or residue cancellation; the common interior angular poles must be
retained. This stop does not prohibit those mechanisms and does not
alter the fixed-angle counterfamily or the RH gap.
