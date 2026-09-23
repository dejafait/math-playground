# Lemma 185: square-displacement short-sum reduction

**Hypotheses.** Use L184 with rho=N^(−1/2), including its real product
weights W and contribution A_rho. Let M be the integers in
[a−−rho,a++rho]. For m∈M define the exact finite set

R_m={r∈Z: r≠0, a−²≤m²+r≤a+²,
                      (m−rho)²≤m²+r≤(m+rho)²}.

Set S0(m)=Σ_(r∈R_m) W(m²+r) and
S1(m)=Σ_(r∈R_m) r W(m²+r).
Use L182's coordinate formula at the positive real root q=m to define
Z±(m), even if m lies just outside [a−,a+], and put

C_m=∫_(Z−(m))^(Z+(m)) cos(z²) dz,
G_m=∫_(Z−(m))^(Z+(m)) sin(z²) dz.

**Conclusion.** For every epsilon>0,

Re A_rho=(N²h)^(−1) Σ_(m∈M) sqrt(2πm)
              [G_m S0(m)−(2π/m) C_m S1(m)]
             +O_epsilon(N^(−1/2+epsilon)).                    (1)

This is a reduction to signed short sums, not a decay estimate for them.
In particular, decay of the displayed normalized expression is equivalent
to Re A_rho=o(1). Its two terms need not decay separately.

**Proof.**

All bounds below are uniform in m∈M and r∈R_m. Write
q=sqrt(m²+r)=m+d. The exact identity r=2md+d² gives

|r|≤2m rho+rho²=O(N^(3/2)),
d=r/(2m)+O(N^(−3)),
sqrt(2πq)=sqrt(2πm)[1+O(N^(−5/2))].                          (2)

There is no Taylor expansion of W(m²+r): it remains exact.

We justify freezing the Fresnel factors also for m outside the stationary
root interval. For fixed s=s± and root q between m and sqrt(m²+r),
put x=s/(2πq)−1 and

v(x)=x sqrt(2[(1+x)log(1+x)−x]/x²).

The quotient is continued smoothly at zero with value 1, as proved in
L182. Thus v and v' are bounded in the neighborhood in use, and

Z_s(q)=sqrt(2πq)v(x),
Z_s'(q)=sqrt(2πq)/q [v(x)/2−(1+x)v'(x)]=O(N^(−1)).           (3)

Indeed q≍N² and |s−2πq|≤h+2πrho, so |x|=O(N^(−1/2)).
This argument crosses x=0 smoothly and does not require the saddle to
lie inside the block. The mean value theorem now gives the uniform
zero-order expansions in the square displacement

z±(m²+r)=Z±(m)+O(|r|/N³),
C_(m²+r)=C_m+O(|r|/N³),
G_(m²+r)=G_m+O(|r|/N³).                                     (4)

For the first line use |d|≤C|r|/N², from r=d(2m+d).
For the last two use that the integrands have modulus at most one:
changing integration endpoints costs at most the sum of their shifts.
The finite Fresnel bound in L182 holds for arbitrary real endpoints,
so |C_m|+|G_m|≤C, even outside the stationary interval.

Combining (2) and (4) yields the signed analytic-amplitude expansion

sqrt(2πq)[G_(m²+r)−4πd C_(m²+r)]
 =sqrt(2πm)[G_m−(2πr/m)C_m+O(N^(−3/2))].                   (5)

For clarity, the errors inside the brackets are O(N^(−3/2)) from
freezing G, O(N^(−2)) from freezing C multiplied by d,
O(N^(−3)) from replacing d, and O(N^(−5/2)) from the relative
square-root amplitude. All coefficients are uniformly bounded as used;
no cancellation in W is assumed in these estimates.

The uniqueness of the nearest integer in L184 makes (m,r)↦m²+r
a bijection from the indicated pairs to Q_rho. The exact sets R_m
retain both stationary endpoints and the asymmetric displacement bounds
−2m rho+rho²≤r≤2m rho+rho². No symmetric integer cutoff is substituted.
L184's absolute weight count gives

Σ_(m∈M) Σ_(r∈R_m) |W(m²+r)|
 ≤C_epsilon h N^(3/2+epsilon).

Consequently the total error in (5), after normalization by N²h,
is O_epsilon(N^(−1+epsilon)): multiply the count by
O(N)N^(−3/2)/(N²h). Applying (5) to L184 (3) and grouping the
remaining finite sums proves (1); L184's O_epsilon(N^(−1/2+epsilon))
error dominates. Choose epsilon<1/2 to make the remainder o(1). ∎

## Scope, verification

The two short sums have lengths O(N^(3/2)). The inherited divisor bound
alone gives |S0(m)|≤C_epsilon N^(3/2+epsilon) and
|S1(m)|≤C_epsilon N^(3+epsilon). Their contributions in (1) therefore
have only the absolute bounds O_epsilon(N^(1/2+epsilon)) and
O_epsilon(N^epsilon), respectively. Cancellation of their displayed
combination remains unproved. Neither the other stationary products nor
the full mixed moment nor RH is settled by this reduction.

Verification is analytic: the exact displacement identity, smooth
coordinate differentiation at zero, Lipschitz bounds for moving integration
endpoints, preservation of integer cutoffs, and absolute accumulation of
all remainders. No numerical or external theorem is needed.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
