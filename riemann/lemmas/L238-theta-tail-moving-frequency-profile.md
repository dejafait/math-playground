# Lemma 238: the omitted theta tail on a moving Fourier scale

**Hypotheses.** Use the positive summands K_n of L019 and the omitted tail T_N, its mass ε_N, and transform E_N of L237. Put m=N+1, B=πm² and P_N(t)=E_N(Bt)/ε_N, for integers N≥1. Derivatives of P_N below are with respect to t.

**Conclusion.** For every fixed T>0 and j=0,1,2 there is a constant C_T independent of N such that

sup_{|t|≤T} |P_N^(j)(t)−p^(j)(t)| ≤ C_T/B,
where p(t)=4/(4+t²).

Also ε_N=8 exp(−B)(1+O(B^(−1))). In particular E_N(Bt)>0 on each fixed bounded t interval for all sufficiently large N. On such intervals,

B² {E_N E_N''−E_N'²}(Bt)/(2E_N(Bt)²)
= (t²−4)/(t²+4)² + O_T(B^(−1)),

where the primes on E_N are derivatives with respect to its original frequency. This is a statement about the omitted tail, not about F_N or its smoothing threshold.

**Proof.** Write b=πn², v=b exp(2u), and w=v−b. The change of variables used in L237 gives exactly

K_n(u)du=4 exp(−b) exp(−w) q_b(w)dw,
q_b(w)=(1+w/b)^(1/4)−{3/(2b)}(1+w/b)^(−3/4),
u=log(1+w/b)/2.

For b≥π and w≥0, concavity of the fourth root and positivity give

1−3/(2b) ≤ q_b(w) ≤ (1+w/b)^(1/4),
|q_b(w)−1| ≤ (w/4+3/2)/b.

Consequently, with M_n=∫_0^∞K_n(u)du and Q_b=∫_0^∞exp(−w)q_b(w)dw,

M_n=4 exp(−b)Q_b,  Q_b=1+O(b^(−1)),  c≤Q_b≤C,

for absolute positive c,C. All the estimates remain valid after integration against any fixed nonnegative integer power of w, since its exponential moment is finite.

For n=m set b=B and y_B(w)=B log(1+w/B)/2. The elementary inequalities log(1+s)≤s and log(1+s)≥s−s²/2 for s≥0 imply

0≤y_B(w)≤w/2,  |y_B(w)−w/2|≤w²/(4B).

For j=0,1,2 write h_j(t,y)=y^j cos(ty+jπ/2), the jth t derivative of cos(ty). On |t|≤T and 0≤y≤w/2 its derivative with respect to y is bounded by T when j=0, and by j(w/2)^(j−1)+T(w/2)^j when j≥1. The mean value theorem therefore bounds

|h_j(t,y_B(w))−h_j(t,w/2)|
≤ C_T B^(−1)(1+w^(j+2)).

Integrating this bound with exp(−w), and using the preceding weighted bound for |q_B−1| and |h_j(t,y_B)|≤(w/2)^j (interpreted as 1 for j=0), yields

∫_0^∞ exp(−w)q_B(w)h_j(t,y_B(w))dw
= ∫_0^∞ exp(−w)h_j(t,w/2)dw + O_T(B^(−1)).

The derivative integrals are justified by these same integrable polynomial bounds. Division by Q_B=1+O(B^(−1)) proves the asserted C² estimate for the normalized transform of the first omitted summand. The limiting integral is

∫_0^∞ exp(−w)cos(tw/2)dw
= Re[1/(1−it/2)]=4/(4+t²),

and its first two derivatives are the displayed limiting integrals by domination.

It remains to bound all later summands uniformly, including derivatives. The single-summand moment estimate proved in L237 gives, for j=0,1,2,

∫_0^∞ (Bu)^j K_n(u)du ≤ C_j (B/b)^j M_n ≤ C_j M_n  (n≥m).

Hence the absolute value of each jth t derivative of ∫K_n(u)cos(Btu)du is at most C_j M_n. For n=m+k, k≥1, we have

π[(m+k)²−m²]≥π(2m+1)k.

The mass bounds above and a geometric series show

Σ_{n>m} M_n/M_m ≤ C exp(−π(2m+1))/(1−exp(−π(2m+1))).

This quantity is O(B^(−1)), with an absolute constant for all m≥2. Uniform absolute convergence of the derivative series follows from the same estimates. Normalizing the whole tail by its total mass therefore changes the first-summand profile and its first two derivatives by O(B^(−1)). The factor 2 in both E_N and ε_N cancels. It also gives ε_N=2Σ_{n≥m}M_n=8 exp(−B)(1+O(B^(−1))).

Finally p(t)≥4/(4+T²)>0 on the fixed interval. The C² estimate permits division by P_N² for sufficiently large N, with a uniform error O_T(B^(−1)). The chain rule gives

B² {E_N E_N''−E_N'²}(Bt)/(2E_N(Bt)²)
= [P_N P_N''−P_N'²]/(2P_N²)
= (log p)''/2+O_T(B^(−1)).

Direct differentiation of log p=log 4−log(4+t²) gives (log p)''/2=(t²−4)/(t²+4)². This proves the conclusion. ∎

The achieved estimate resolves the omitted tail on bounded scaled-frequency intervals. Its positive logarithmic curvature for fixed |t|>2 has size B^(−2), tending to zero; it is not a nonvanishing obstruction to smoothing. Nor can it be inserted into the definition of a_N^*, whose denominator is F_N² rather than E_N². The required global estimate remains a_N^*→0. Comparing F and E_N with two derivatives, controlling frequencies outside bounded t intervals, and resolving local zero geometry are still missing. Even a vanishing threshold would supply only first-level positivity, not the all-degree premise for RH.

**Mathlib.** Not checked for the full statement or supporting Laplace-integral, differentiation-under-integral, and uniform convergence results. No full matching theorem is claimed. General documentation: https://leanprover-community.github.io/mathlib4_docs/
