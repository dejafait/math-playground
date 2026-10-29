# Complementary-covariance infrared attempt — working record

2026-10-28, step 532. The unchanged EXPLORE assessment is
`literature/2026-10-28-complementary-covariance-infrared-test.md`.
The interim notes below preserve the reasoning saved during the attempt.
The completed estimate is canonical in L297; this is not a checkpoint.

Target: Test whether the complete complementary-covariance tail
R_N(G)-R_N(G-H_r), differentiated in both sources, cancels L296's
leading infrared obstruction at r=r_N.

The main gap is quantitative full-box control of the uncut coefficient;
uniform higher remainder and the interacting/continuum/mass construction
remain independent. The bounded threshold is a controlled limit after
division by N^(1/2)(log N)^2. Zero would pass only a necessary first
test; a nonzero complete limit stops this leading-cancellation mechanism.
An uncontrolled mixed or high-spectrum remainder leaves it unfinished.

Startup inputs and failures inspected: L003 hypotheses, L279/L280's
source conventions and full polynomial, L282's exact bump/density
constant, L287's complete curl-energy proof, L296 sections 1--4,
and ATTEMPTS/047--050. Existing notebook changes are preserved.

Current avenue: expand the covariance polynomial about G, retaining
every mixed assignment. Its linear-in-H term contains the complete
one-line Wilson contraction together with the unchanged density.
The prospective cancellation concerns that operator on the four
ground modes. It requires separate uniform control of its source
derivatives, the heat high-spectrum part and the terms with two or
three H lines. No cancellation, asymptotic or effective-action identity
is assumed here. The finite Gaussian and matrix inputs are imported
from the precise citations in the saved assessment, not reproved.

Possible additional canonical inputs to inspect narrowly: L283's
quartic internal operator and L288--L289's cubic internal operator
limit. They concern the same all-link relative SU(2) tensors and may
evaluate the one-line contraction on smooth ground modes; their use
requires checking that applicability rather than importing L291's
uncut response cancellation as an estimate for this changed quantity.

## Saved derivation before completing the estimates

Write H=H_r and keep all source arguments implicit. Exact polynomial
expansion gives

R(G)-R(G-H) = Tr(W H) + U(U;H,H)/8
             - B(T,T;H,H,G)/4 + B(T,T;H,H,H)/12,

where W=D+E/4-A_U/4, E contracts the two cubic tensors against G,G,
and A_U contracts U against G. These are ambient all-link tensors,
then compressed to the fixed transverse space; colors remain included.
Real positive A(s,t) gives positive H and G-H on that space for r>0.

The newly inspected same-notebook inputs are L283(17), L289(12) and
L289(16), with their local proofs read through the boundary passage.
They apply directly to the same smooth sampled ground modes. Together
with L282(18) and the external-curl error in L287(12)--(13), they give
the prospective ground compression W -> (d_*-a_*/4+24 I_1/4)I = 0.
The equality uses I_1=Z_0/2-1/16. This uses neither L291's uncut
cancellation nor a one-face boundary approximation.

Remainder mechanism being checked: all zero/first/mixed derivatives
of W obey a uniform quadratic-form bound in J_N=I+log(eN)A. The
two internal G lines have uniformly bounded G-relative derivatives;
the L287 weighted-vertex tensor norm then retains every source term.
Quartic contractions have uniformly bounded local row sums.
Low-contour residues after removal of the three-ground-projector term
have bounded trace norm even with Ahat^(1/2) at both ends. Thus the
J_N form bound can avoid a spurious extra log N in that low remainder.
The high-contour trace estimate from L296 tolerates the O(log N)
operator norm of W. A second heat line should supply a further
G-relative exponential factor after one heat line is estimated in
trace norm; the crude N^4 cubic bound is insufficient for that term.
All these estimates, their multiplicities and source orders still need
to be written and checked before a completed conclusion is claimed.

## Completion

The saved avenue closes in
[L297](../lemmas/L297-complementary-covariance-infrared-cancellation.md).
Its complete polynomial identity, source-energy bounds, weighted low
residues, full high-spectrum trace estimate and mixed two-heat-line
bound prove tau_N(r_N)=o(N^(1/2)(log N)^2). The full proof, precise
citations and Mathlib qualification are canonical there. No script
or numerical evidence is used. L283 and L289 are additional direct
local inputs with their same-domain applicability explicitly checked;
L288 is only upstream of the imported L289 limit.

The result passes the approved necessary test without proving a
bounded tail or a rate, and preserves the separate bare all-tail stop.
A later conceptual audit must check the new weighted-residue and
signed mixed-contraction estimates; that continuation is registered
REVIEW_REQUIRED, without performing or approving it in this step.
