# Finite-obstacle top escape: working checkpoint

Approved target: the exact J_H in
`literature/2026-10-30-finite-obstacle-top-escape-test.md`.
Main gap: actual-Xi all-degree positivity; this tests only a proposed
outer-boundary majorant for the L504 positive-class cost route.

Candidate calculation, pending complete write-up: fix R,T, take
W=1/R and k=pi/W=pi R. Use the right-hand corridor
(a+W,a+2W) times (b/4,H). Its separated harmonic function is
sin(k(x-a-W))*sinh(k(y-b/4))/sinh(k(H-b/4)).
When X_H/2>=a+2W its top datum is <=chi_H. Nonnegativity of
h_H elsewhere should give h_H>=this function in the corridor.
At p=(a+3W/2,b/2), this gives a fixed positive multiple of
exp(-pi R H). A fixed Harnack chain below y=b transfers it to
(a,y), b/3<=y<=2b/3. Therefore the candidate J_H lower bound
is a positive fixed multiple of exp(pi R H).

The initial pending checks above are now resolved in
[canonical L506](../lemmas/L506-finite-obstacle-top-envelope-divergence.md).
It supplies an explicit H_0, step length b/24 (disk radius b/12), at most
ceil(36/(Rb)+4) Harnack steps and a positive fixed lower constant.
The first separate critical audit remains pending. No actual H_a
function or negative-part lower bound is asserted. No script or
numerical experiment was required; the earlier candidate reasoning
is preserved here as a working checkpoint, not a second proof.
