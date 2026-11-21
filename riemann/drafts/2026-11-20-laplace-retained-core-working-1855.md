# Retained-core contour attempt1855 — working checkpoint

Approved target: assessment1854, unchanged EXPLORE. Research/development;
no new source scope, no quantitative residual claim. Inputs C034d/e,
C032n; C034c/b supply the future threshold and inherited qualifications.
Main gap: L030-L032/C032a actual-Xi all-degree positivity.

For a signed translate index nu=(rho,epsilon), epsilon=+/-1, set
c_nu=epsilon*gamma_rho, b_nu=-epsilon*delta_rho. Then
G_sigma(v-epsilon*z_rho)=G_sigma(v-c_nu-i*b_nu). On v=x+i*b_nu
this is the positive real G_sigma(x-c_nu). Use cutoff a=13.

Finite rectangle candidate (orientation checked): for rational F holomorphic
in Re v>=a, real integral from a to M equals shifted horizontal integral
plus the connector from a to a+i*b_nu minus the far connector from M
to M+i*b_nu. This applies to F=Q_j and Q_j'', hence separately in
each variable of K. No origin contour is taken.

Pending proof obligations: one uniform majorant on I=[1/2,3] for every
horizontal and connector side, all independent product terms, and the
summed far-side limit. The tentative bounds are |F(x+i*t)|<=C*x^-4
(Q) or C*x^-6 (Q''), with Gaussian envelope exp(-(x-c_nu)^2/24).
C032n(9) should pay horizontal integration; C032n(13)'s counting proof
should pay the far side by O(M log M)*M^-4, before taking limits.
Finite connectors should have summable exp(-(13-c_nu)^2/24) envelopes.

Cutoff relocation must be exact: U_j^1=U_j^13+L_j,
W_j^1=W_j^13+M_j, where L_j=int_1^13 p Q_j and
M_j=int_1^13 p Q_j''. The six product corrections remain. Alternatively
use alpha_j^13=int_0^13(p-p(0))Q_j-p(0)int_13^infinity Q_j,
beta_j^13=int_0^13(p''-p''(0))Q_j-p''(0)int_13^infinity Q_j
-p'(13)Q_j(13)+p(13)Q_j'(13). Do not split an origin-divergent term.

Proposed final form is C=HH[K]+HV[K]+VH[K]+VV[K]+R_13,
with factor1/4 in each two-translate sum and both signs of epsilon.
Only HH is signed by C034e. Preserve all other terms as explicit residual.
Success requires rigorous absolute full-divisor exchanges and a real
nonpositive HH; an identity alone cannot pay C034c(20), S4^3/5.
No closure, ECT, conditioning, weights, signed-height or Xi claim.

Completed1855: the pending estimates and bookkeeping above are now
proved in canonical C034f(47)-(60), pending independent conceptual
audit. In particular the full summed far-side bounds are
O(M^-3 log M) and O(M^-5 log M); all nine finite side products and
the exact R_13=R_1+J_13 relocation are retained. No residual bound at
S4^3/5 is asserted. This draft preserves the pre-derivation checkpoint;
the full proof and citations reside only in C034f.
