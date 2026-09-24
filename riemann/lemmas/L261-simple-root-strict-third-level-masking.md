# Lemma 261: a five-root split retains three strict Laguerre levels

**Hypotheses.** Let b>0 and 0<ε/b≤1/√20. Put P(z)=z(z²−ε²)(z²−4ε²)(z²+b²). For a real polynomial F, let D_n(F;x) denote the coefficient of y^(2n) in F(x+iy)F(x−iy), with D_0(F;x)=F(x)².

**Conclusion.** P has only simple zeros, retains the nonreal pair ±ib, and D_n(P;x)>0 for all real x and n=1,2,3. With b=1/4 the even polynomial E(z)=P(z−10)P(z+10) likewise has only simple zeros, including nonreal zeros, obeys |Re z|>4 and |Im z|<1/2 at every zero, and has D_n(E;x)>0 for every real x and n=1,2,3. This is a three-level assertion, not an all-level assertion.

**Proof.** Set q=(ε/b)², w=z/b, and p(w)=w(w²−q)(w²−4q)(w²+1), so P(z)=b⁷p(z/b). Consequently D_n(P;x)=b^(14−2n)D_n(p;x/b). It suffices to prove the signs for 0<q≤1/20. Write s=x² and expand p(x)=x⁷+(1−5q)x⁵+(4q²−5q)x³+4q²x. Coefficient extraction gives

D_1(p;x)=7s⁶+(8−40q)s⁵+(5−20q+101q²)s⁴+(−20q+4q²−80q³)s³+(35q²+80q³+48q⁴)s²+16q⁴,

D_2(p;x)=21s⁵+(10−50q)s⁴+(10+40q+138q²)s³+(35q²+80q³+48q⁴)s+40q³−32q⁴,

D_3(p;x)=35s⁴+(10+40q+138q²)s²+(20q−4q²+80q³)s+33q²−80q³+16q⁴.

For completeness these identities follow from the finite formula

D_n(p;x)=Σ_(j,k) a_j a_k x^(j+k−2n) Σ_r (−1)^(n+r) binom(j,r) binom(k,2n−r),

where a_7=1, a_5=1−5q, a_3=4q²−5q, a_1=4q², all other a_j vanish, and the inner sum is over 0≤r≤j and 0≤2n−r≤k. Thus all retained powers are nonnegative and no limiting operation is involved.

For D_1 the coefficient of s⁴ is at least 4, that of s³ is at least −21q (since 80q²≤1/5), and that of s² is at least 35q². Therefore their combined contribution is at least

s²(4s²−21qs+35q²)=s²[4(s−21q/8)²+119q²/16]≥0.

The remaining terms have nonnegative coefficients because 8−40q≥6, and the constant 16q⁴ is strictly positive. Thus D_1>0 for every s≥0. Every displayed nonzero coefficient of D_2 is positive: in particular 10−50q≥15/2 and 40q³−32q⁴=q³(40−32q)>0. The same holds for D_3 because 20−4q+80q²>0 and 33−80q+16q²≥29. Its constant is strictly positive as well. This proves all three global strict inequalities, including at real roots.

The roots 0, ±ε, ±2ε, ±ib of P are distinct. For the even construction use the coefficient convolution from L257:

D_n(UV;x)=Σ_(j=0)^n D_j(U;x)D_(n−j)(V;x).

Take U(z)=P(z−10), V(z)=P(z+10). All terms for n≤3 are nonnegative. For n=1, at least one of U(x)²,V(x)² is positive because their real root sets are disjoint, making the sum positive. For n=2 the j=1 term is positive; for n=3 the j=1 term is positive. Oddness of P gives evenness of E. Since 2ε≤1/(2√20)<1, the translated real roots are distinct and have absolute value greater than 9; the four nonreal roots are ±10±i/4. This verifies simplicity and the claimed localization.

At x=0 the local generating polynomial is t(t+q)²(t+4q)²(1−t)², where t=y². Its t⁶ coefficient is 10q−2<0 in the stated range. Thus a higher level explicitly detects the local nonreal pair; no claim about the sixth level of E is needed. ∎

The achieved threshold is three strict global levels with simple zeros and an even localized version. The required main threshold is all-degree mixed positivity for actual theta, or another sufficient condition excluding every off-line zero. Neither a positive Fourier kernel nor an actual-theta identity is asserted. This extends the two-level test of L260 but proves no arbitrary-finite-level simple-root theorem and is not a counterexample to RH.

**Mathlib.** Not checked for the full statement or supporting polynomial coefficient and binomial identities. No matching or supporting theorem name is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
