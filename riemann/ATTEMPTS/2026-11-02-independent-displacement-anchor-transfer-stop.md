# Independent displacements: inherited-anchor and absolute-kernel transfer stopped

The full hypotheses and analytic proofs are canonical in
[L665](../lemmas/L665-independent-displacement-anchor-and-absolute-kernel-stop.md).
Both examples retain n=12q+3, delta=1/4, the fixed anchor, every
original unit residue, all n product factors and all M=n/3 moments.
They use displacements at most h/16 and remain L649-admissible.

WHY IT FAILS: Moving just one node gives a nonzero limiting error in
L664's inherited-anchor polynomial at u=-1, so that approximation is
not uniformly o(1) in the approved perturbed class. Separately, moving
each nonanchor node outward makes the absolute difference of the finite
node-polynomial kernels costly on the original rectangle: relative to
exp(-n/32)*sqrt(D), its full absolute contour cost is at least
c*n^(-3/2)*exp(981n/20000). The logarithmic localization charge does
not repair that exponential mismatch. This stops the small-error
anchor transfer and this fixed-contour absolute comparison. It does
not bound the signed error from below in the second example, exclude
every allowed arc, or refute the paid criterion. The first example
is actual response evidence; the second is an estimate-cost obstruction.

Preserve L664 and the earlier full-circle and endpoint stops. A further
attempt must allow an order-one change in the response and use signed
angular information. A finite nonharmonic sampling approach is nominated
for separate source comparison; no applicability or readiness is assumed.
