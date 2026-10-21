# Quantitative L079 comparison — working record

Approved target: determine whether
|a^3 J_(i,N)-2 gamma D_(i,a)| <= C_i N^(-1/2) log(eN)^2,
for both actual probes, under the unchanged 2026-10-17 first-pair
quantitative EXPLORE assessment.

The main construction gap is ultraviolet-uniform interacting matching
with reflected error <=c_box/2, continuum axioms and finite positive
infrared mass. This step addresses only one quantitative input to the
mixed component; L080, L101 and the other component rates are independent.

Saved before completing the argument: use the inspected Lawler–Limic
Theorem 4.3.1 to obtain |g(x)|<=C/(1+|x|) and fixed-offset
|g(x+e)-g(x)|<=C/(1+|x|)^2 for Delta=6(I-P). Its remainder
O(|x|^-3) suffices for this difference bound without differentiating
the remainder. Proposition 4.6.2(a), applied linearly to a finite
zero-mass source, makes the interior harmonic correction O(N^-2).
Together with the exterior dipole l2 tail this should give an
O(N^-1/2) zero-extended right-source comparison. A radius-cN cutoff
of the monopole has squared energy error O(N^-1), so L045's energy
projection should yield the same left derivative error. Finally
the weighted derivative sum
sum_x min(|x|/N,1)^2 (1+|x|)^(-4) is O(N^-1) in dimension three.
It should control the variable upper coefficient before the full heat
sum. These are proof obligations at this checkpoint, not yet results.

Continuation test: prove all these estimates uniformly for source y
in L079's fixed K and with polynomial exterior-mode constants; then
use L079(18). Abandon a factorwise estimate if its actual boundary or
source structure violates the asserted power, and do not infer signed
response growth from that failure. No upper axial profile is deleted.

Essential input IDs: L045 L070 L076 L078 L079, with the actual probe,
smooth coefficient and heat-tail hypotheses imported through L079.
No monopole l2 norm or bounded infinite inverse on all l2 is assumed.

Completed: [L221](../lemmas/L221-first-pair-pinned-trace-quantitative-rate.md)
proves the stronger rate C_i N^(-1/2), without logarithmic loss, by
carrying out these estimates in the original trace order. The scalar
theorems are imported by precise citation; the variable-coefficient
trace specialization is written out. No mathematical script or
numerical evidence is used. The result meets this bounded target;
it does not establish the complete coefficient's rate, an O(N^2)
selected remainder or interacting matching. Separate critical audit
of L221 is proposed and requires its own coverage approval.
