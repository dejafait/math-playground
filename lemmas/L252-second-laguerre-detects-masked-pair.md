# Lemma 252: the second Laguerre expression detects the masked pair

**Hypotheses.** Let H be the explicit real even entire function of L251:

H(z)=(1−z²/100)(1−z²/25)(1−z²/a²)(1−z²/conj(a)²)cos(z/100),    a=10+i/4.

For a real entire J define

D₂(J;t)=J″(t)²/4−J′(t)J‴(t)/3+J(t)J⁗(t)/12.

**Conclusion.** D₂(H;10)<−31 H′(10)²<0. Thus the second generalized Laguerre inequality detects this example's nonreal pair even though its first Laguerre expression is strictly positive on the entire real axis. This is a separation of these two tests, not a sufficient criterion for RH or for real zeros in general.

**Proof.** Set c=10 and b=1/4. Factoring off the real root c and the conjugate pair c±ib gives

H(z)=(z−c)((z−c)²+b²)R(z),

where for a nonzero real constant C,

R(z)=C(z+10)((z+10)²+b²)(z−5)(z+5)cos(z/100).

The constant is real because the two displayed real polynomials have exactly the roots, with multiplicities, of H's polynomial factor. In particular R(c) is real and nonzero. Taylor expansion at c, or three product differentiations, gives

H(c)=0,    H′(c)=b²R(c),    H″(c)=2b²R′(c),
H‴(c)=6R(c)+3b²R″(c).

Consequently, with S=−(R′/R)′(c),

D₂(H;c)=b⁴(R′(c)²−R(c)R″(c))−2b²R(c)²
         =H′(c)²(S−2/b²).

There is no logarithmic derivative of H at its zero in this calculation. R is nonvanishing on a neighborhood of c, so its logarithmic derivative there is legitimate. Differentiating its finite product yields exactly

S=1/400 + 2(400−b²)/(400+b²)² + 1/25 + 1/225
  + 10^(−4)sec²(1/10).

The conjugate-pair contribution is positive and less than 2/400. Also cos(1/10)≥1−1/200>1/2, so the final contribution is less than 1/2500. Hence

0<S<1/400+1/200+1/25+1/225+1/2500<1.

Since 2/b²=32 and H′(c)≠0, the claimed bound follows. All estimates are exact rational bounds; no numerical derivative or zero computation is used.

For clarity about normalization, multiplying the convergent Taylor series of J(t+iy) and J(t−iy) shows that the coefficient of y⁴ in |J(t+iy)|² is exactly D₂(J;t): the (0,4) and (4,0) terms give JJ⁗/12, the (1,3) and (3,1) terms give −J′J‴/3, and (2,2) gives J″²/4. This also independently identifies the tested level. L251 supplies the contrasting strict first-level positivity and the retained nonreal zeros. ∎

The attained bound separates two conditions on a comparison function. It proves no sign for actual Ξ, and even a proof of its second-level positivity alone would remain below the required all-degree mixed-positivity threshold. No positive Fourier-kernel representation for H is asserted.

**Mathlib.** Not checked: neither a full matching theorem nor supporting product/Taylor differentiation results were looked up. No theorem name is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
