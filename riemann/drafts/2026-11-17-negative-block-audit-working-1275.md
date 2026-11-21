# Negative-block audit working record1275

Approved scope: assessment1274, SPECIALIZE; classification REPRODUCTION.
This saved intermediate reasoning is now superseded by the complete
[canonical audit1275 in L559](../lemmas/L559-paired-tail-retained-endpoint-audit.md).
The preliminary notes below are preserved; they are not a second proof.

Actual Phi=K/4. L559 gives smooth evenness and both transverse endpoints;
L019 supplies positive Phi(0). For P(q)=32q^3-224q^2+330q-75,
Phi''(0)=sum q_n P(q_n)e^(-q_n)/4. On [3,22/7], P decreases
and P(3)=-237. Thus the first term is less than -79/36 using
e<3 and pi<4. The positive tail is less than
204800*100/(18^4*99)<2 using pi^4<100, e^3>18, and the
successive majorant ratio <26/18^5<1/100. Hence Phi''(0)<-7/36.
This checks the required sign, not the source's sharper decimals.

For c0=Phi(0), c2=Phi''(0), direct moving-limit differentiation gives
Q_y'=-(16/3)y*c0*c2*a^3+O_y(a^5); do not differentiate an
uncontrolled remainder. An increasing compact interval therefore exists.

Set k=2x, h=2pi/k. Four inner IBPs retain g1=-W A(a,a),
g2=W A_b(a,a), g3=W A_bb(a,a), g4=-W A_bbb(a,a), plus
k^-4 W integral_0^a A_bbbb sin(kb) db. Lower endpoints vanish
by oddness of A or sin(0). Uniformly on a fixed compact triangle,
C_eps=2pi(g1''-g2')/k^4+O(k^-5). For the source's stated
O(k^-6) contributions from g3/g4, also keep ||g3''|| and ||g4'||,
and include the triangle size and ||W|| in the integral remainder bound.
All are finite by smoothness. The first two moments give
C_Q=-2pi Q'/k^2-2pi^2 Q''/k^3+O(k^-4).
Absorb the uniform lower-order terms into pi*delta/k^2 to reach
C_tot<=-pi*delta/k^2=-pi*delta/(4x^2).

The canonical audit supplies the complete argument and corrected
constant dependence. Its rational-arithmetic replay passes all nine checks.
No global sum, small-y uniformity, Schur sign, or RH assertion is obtained.
