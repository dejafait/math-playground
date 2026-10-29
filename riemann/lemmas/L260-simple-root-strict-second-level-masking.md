# Lemma 260: simple roots retain strict first- and second-level masking

**Hypotheses.** Let 0<ε<b and put P(z)=z(z²−ε²)(z²+b²). Define D_n(F;x) as the coefficient of y^(2n) in F(x+iy)F(x−iy), including D_0(F;x)=F(x)². Set A=b²−ε²>0 and B=−ε²b²<0.

**Conclusion.** Every zero of P is simple, including the nonreal pair ±ib, but D_1(P;x)>0 and D_2(P;x)>0 for every real x. More precisely,

D_1(P;x)=5x⁸+4Ax⁶+(3A²−10B)x⁴+B²,
D_2(P;x)=10x⁶+(3A²−10B)x²−2AB.

For b=1/4 and any 0<ε<b, the even polynomial E(z)=P(z−10)P(z+10) has only simple zeros, all obeying |Re z|>4 and |Im z|<1/2, retains nonreal zeros, and satisfies D_1(E;x)>0 and D_2(E;x)>0 everywhere on the real axis. The local factor still has D_4(P;0)=2(ε²−b²)<0.

**Proof.** Expand P(z)=z⁵+Az³+Bz. Multiplication of its Taylor polynomials gives

D_1(P;x)=P′(x)²−P(x)P″(x),
D_2(P;x)=P″(x)²/4−P′(x)P‴(x)/3+P(x)P⁗(x)/12.

Indeed the coefficient of y² consists of the two (0,2) terms and the (1,1) term, and that of y⁴ consists of the (0,4), (1,3), (2,2), (3,1), (4,0) terms. Substitution of

P′=5x⁴+3Ax²+B, P″=20x³+6Ax, P‴=60x²+6A, P⁗=120x

yields the two asserted polynomial identities. For an explicit normalization and cancellation check, the first identity subtracts

P′²=25x⁸+30Ax⁶+(9A²+10B)x⁴+6ABx²+B²,
PP″=20x⁸+26Ax⁶+(6A²+20B)x⁴+6ABx².

The three terms in the second identity are

P″²/4=100x⁶+60Ax⁴+9A²x²,
P′P‴/3=100x⁶+70Ax⁴+(6A²+20B)x²+2AB,
PP⁗/12=10x⁶+10Ax⁴+10Bx².

Subtracting the second line from the first and adding the third gives exactly the asserted D_2, including cancellation of x⁴. This is the coefficient convention in Csordas, *Fourier transforms of positive definite kernels and the Riemann ξ-Function*, [arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2), Remarks 2.5, equation (2.11), p. 4; no all-order converse from that source is needed here.

Since A>0 and B<0, all displayed nonzero coefficients of D_1 and D_2 are positive. In particular, D_1(P;x)≥B²>0 and D_2(P;x)≥−2AB>0 for every real x. These polynomial bounds include all real roots and arbitrarily large |x|; no division by P or compactness argument is used. The factorization gives all five roots 0, ±ε, ±ib, which are pairwise distinct because ε,b>0. Each linear factor occurs once, so simplicity is over C, not just on the real axis.

At x=0 the generating polynomial is t(t+ε²)²(b²−t)² with t=y². Its t⁴ coefficient is 2ε²−2b², proving the last assertion without invoking any real-zero criterion.

The coefficient convolution from L257 gives, with U(x)=P(x−10), V(x)=P(x+10),

D_1(UV;x)=D_1(U;x)V(x)²+U(x)²D_1(V;x),
D_2(UV;x)=D_2(U;x)V(x)²+D_1(U;x)D_1(V;x)+U(x)²D_2(V;x).

Both factors have strictly positive first and second expressions by translation. For b=1/4, each translated root lies in the closed disk of radius b about its translation center, 10 or −10. Those disks are disjoint: their centers have distance 20>2b. Each factor has five distinct simple roots, and there is no common complex root. Thus the degree-ten product has precisely ten simple roots, in particular no common real zero of its factors. Consequently

D_1(E;x)≥B²(V(x)²+U(x)²)>0,
D_2(E;x)≥D_1(U;x)D_1(V;x)≥B⁴>0

for every real x. All omitted terms are nonnegative. These inequalities also handle a real zero of either factor, without dividing by that factor.

Since P is odd, E(−z)=P(−z−10)P(−z+10)=P(z+10)P(z−10)=E(z). Its real zeros are 10, 10±ε, −10, −10±ε, and its nonreal zeros are 10±ib and −10±ib. The quartet has distinct real or imaginary coordinates, since 10 and b are positive. Every root obeys |Re z|≥10−b=39/4>4 and |Im z|≤b=1/4<1/2. ∎

Critical audit completed 2026-10-25: the finite coefficient identities, parameter signs, all-real-center strictness, full complex-root list and convolution transfer above were checked independently. This verifies the existing certificate, not a new construction. The negative fourth-level value asserted here concerns P at zero; it is not asserted for E at zero.

This removes the repeated-root and non-strict-sign qualifications for the first two levels of L257. It does not remove them for arbitrary finite K. The actual required threshold is an all-degree criterion or a separately sufficient theta-specific condition, not these two inequalities, even with simple zeros. No positive Fourier-kernel representation, theta identity, or counterexample to RH is claimed.

**Mathlib.** Not checked for the full statement or supporting polynomial coefficient and differentiation identities. No matching or supporting theorem name is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
