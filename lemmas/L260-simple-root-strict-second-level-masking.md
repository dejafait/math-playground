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

yields the two asserted polynomial identities. Their displayed coefficients are positive except for absent terms: 3A²−10B>0, B²>0, and −2AB>0. Since each power of x is even, both expressions are strictly positive at every real x, including all three real roots. The roots 0, ±ε, ±ib are distinct.

At x=0 the generating polynomial is t(t+ε²)²(b²−t)² with t=y². Its t⁴ coefficient is 2ε²−2b², proving the last assertion without invoking any real-zero criterion.

The coefficient convolution from L257 gives, with U(x)=P(x−10), V(x)=P(x+10),

D_1(UV;x)=D_1(U;x)V(x)²+U(x)²D_1(V;x),
D_2(UV;x)=D_2(U;x)V(x)²+D_1(U;x)D_1(V;x)+U(x)²D_2(V;x).

Both factors have strictly positive first and second expressions by translation. They have no common real zero, so the first sum is strictly positive; the middle term in the second sum is strictly positive. All remaining terms are nonnegative. Since P is odd, E is even. Its real zeros are 10, 10±ε, −10, −10±ε, and its nonreal zeros are 10±ib and −10±ib. For the specified parameters these ten zeros are distinct and satisfy the stated localization. ∎

This removes the repeated-root and non-strict-sign qualifications for the first two levels of L257. It does not remove them for arbitrary finite K. The actual required threshold is an all-degree criterion or a separately sufficient theta-specific condition, not these two inequalities, even with simple zeros. No positive Fourier-kernel representation, theta identity, or counterexample to RH is claimed.

**Mathlib.** Not checked for the full statement or supporting polynomial coefficient and differentiation identities. No matching or supporting theorem name is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
