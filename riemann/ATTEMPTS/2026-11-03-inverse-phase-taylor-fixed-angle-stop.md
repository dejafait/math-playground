# Fixed-angle inverse-phase Taylor filter

The degree-floor(sqrt(n)) inverse-weight Taylor test has an exact
obstruction in [L688](../lemmas/L688-inverse-phase-taylor-fixed-angle-cancellation.md).
Its coefficient cost is exp(o(n)), but for every sufficiently large
admissible n a permitted conjugate pair of shifts makes the complete
weighted sum at u=-1 equal zero. The result is unaudited.

WHY IT FAILS: the central Taylor approximation does not control the
nodes at ordinate n^(-1/4). The last Taylor term dominates there and
amplifies their weighted contributions. The complete undisplaced sum
is nevertheless 1+o(1), by the paid contour estimate. Moving one
conjugate pair through allowed shifts changes the full real sum across
zero. Thus retaining every residue and paying a subexponential norm
do not ensure a fixed-angle signed lower bound. This stops this filter
at u=-1, not the joint maximum V; the constructed sparse vectors are
within the class covered by L686. Any continuation must use the angular
variation or a different joint-response mechanism, with every node
and observation cost retained.
