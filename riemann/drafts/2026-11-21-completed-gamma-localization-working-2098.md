# Localization2098: saved reasoning

Approved target: review2096's exact O_h(X^(-1)) tail beyond 4 log X,
with C034r's fixed input and C034v's least joint cap at T=ceil(X^3).
This is a REPRODUCTION under SPECIALIZE, not a new signed estimate.

Proof plan saved before final documentation: after J, the source has
multiplier Xi(u-i/4) times the transform of Jh times the finite sum
of mu(n)log(X/n)n^(-1/2)(n/X)^(1/4)exp(iu log(n/X)).
The finite sum has modulus at most 2(log 2)sqrt(X), without a sign
estimate. DLMF25.2.8 at N=1 bounds zeta(3/4+iu) by O(1+|u|);
DLMF5.11.9 bounds its gamma factor by
O(|u|^(-1/8)exp(-pi|u|/4)). Thus the source tail integral is bounded
by a constant times X(1+H)^(23/4)exp(-pi H/2) for H>=1.
At H=4 log X this is O_h(X^(-1)). C034v(4) gives whole-vector norm
error O(X^(-1/2)); orthogonal projection and the triangle inequality
then pay the requested completed-vector tail. Both ends and every
boundary term must remain. Full details will be canonical in C034w;
this working note alone is not verification. The complete proof is now
saved in lemmas/C034w-completed-gamma-logarithmic-frequency-tail.md;
its independent audit is the nominated continuation. No signed core bound,
cumulative upper or RH implication is claimed.
