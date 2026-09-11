# Lemma 156: smooth amplitude cutoff variation cost

**Hypotheses.** Fix 0<a<b<∞ and use G_T and N=sqrt(T/(2π))
from L155, on [T,2T], with expectation E_T f=T^(−1)∫f.
Let χ be a nondecreasing C¹ function on the real line, taking values in
[0,1], equal to zero on (−∞,1] and one on [2,∞).
For M>0 set Q=|G_T|² and w=χ(Q/M). Write V(w)=∫_T^(2T)|w'|dt.
Constants below may depend on a,b,χ, but not on T or M. Take T sufficiently
large in terms of a,b.

**Conclusion.** One has

E_T[Q 1_(Q>2M)] ≤ E_T(Qw)
 ≤ C/M + C (log(2T)/sqrt(T))(1+V(w)),                     (1)

V(w)≤CT/M.                                               (2)

In particular these estimates give only

E_T[Q 1_(Q>2M)] ≤ C/M + C log(2T)/sqrt(T)
                         + C sqrt(T)log(2T)/M.           (3)

For fixed M the last term does not tend to zero or remain bounded.
Thus this absolute variation estimate does not establish the fixed-cutoff
tail target of L155. This is a limitation of the estimate, not a lower
bound on the actual tail or on V(w).

**Proof.**

Put I={n∈N:aN≤n≤bN}, A_n(t)=T^(3/4)b_n(t), and
λ_n=log(n/N). Removing the common phase gives

H(t)=exp(−i(t−π/2)log N)G_T(t)
    =Σ_(n∈I) A_n(t)exp(i(t−π/2)λ_n),   Q=|H|².

The index set is fixed as t runs across the interval. For
ℓ_n=log(n/N_t), the exact coefficient derivatives are

A_n'=A_n ℓ_n/t,
A_n''=A_n(ℓ_n²−ℓ_n−1/2)/t².

Both ℓ_n and λ_n are bounded in terms of a,b. Hence

|A_n|≤CT^(−1/4), |A_n'|≤CT^(−5/4),
|A_n''|≤CT^(−9/4).                                      (4)

For distinct m,n in I, the mean value theorem gives
|log(m/n)|≥|m−n|/(bN). Since I has at most CN indices,
summing first over positive differences proves

Σ_(m≠n in I)1/|log(m/n)| ≤ CN²log(2N).                  (5)

For a product p=A_m A_n, (4) gives sup|p|≤CT^(−1/2)
and ∫|p'|≤CT^(−1/2). Integration by parts with
ω=log(m/n) yields the exact formula

∫ w p exp(i(t−π/2)ω)dt
 = [w p exp(i(t−π/2)ω)/(iω)]_T^(2T)
   − (1/(iω))∫(w p'+w' p)exp(i(t−π/2)ω)dt.              (6)

The additional term is the one containing w'. Its absolute bound,
together with the endpoints and p' term, is
CT^(−1/2)(1+V(w))/|ω|. Sum (6), divide by T, and use
N²=T/(2π) and (5). The off-diagonal part of E_T(Qw) has
absolute value at most C T^(−1/2)log(2T)(1+V(w)).
Every operation involves a finite sum and a C¹ integrand.

We also need E_T Q≤C and E_T|H'|²≤C. Here is a direct verification
that avoids introducing the large carrier frequency log N. For a finite
sum with coefficients d_n satisfying |d_n|≤CT^(−1/4) and
|d_n'|≤CT^(−5/4), its normalized diagonal square is O(1).
Integration by parts in each off-diagonal product d_m conjugate(d_n)
using (5) bounds their total by O(T^(−1/2)log(2T)). This argument
applies to complex coefficients as well: bound the product derivative by
the sum of the two absolute product terms. Apply it first to d_n=A_n,
and then to d_n=A_n'+iλ_n A_n, the coefficients of H'.
Their derivative is A_n''+iλ_n A_n', so (4) supplies precisely the
required bounds. This proves both asserted normalized L2 bounds.

The diagonal function D_T(t)=Σ A_n(t)² is bounded by C pointwise,
by (4) and |I|≤CN. Since w vanishes unless Q>M, Markov's inequality
gives E_T(D_T w)≤C P_T(Q>M)≤C E_T Q/M≤C/M.
Combining this with the off-diagonal estimate proves the upper bound in
(1). The lower bound follows from w=1 on Q≥2M and nonnegativity.

Finally Q'=2 Re(H' conjugate(H)), so the chain rule and
Cauchy–Schwarz give

V(w)≤(2||χ'||∞/M)∫|H'||H|dt
    ≤(2||χ'||∞ T/M)(E_T|H'|² E_T|H|²)^(1/2)≤CT/M.

Substitution proves (2) and (3). ∎

## Scope and verification

A smooth cutoff makes integration by parts legitimate but does not allow
its derivative to be omitted. Removing the carrier avoids a spurious
log T in the derivative norm; even the resulting estimate does not close.
The transition support M<Q<2M could contain useful additional information,
and cancellation in the sum of the w' terms has not been estimated here.
No impossibility theorem for such improvements, positive proportion,
pointwise nonvanishing, or RH is claimed.

Verification is analytic: differentiate ℓ_n using ℓ_n'=−1/(2t), check
both endpoint terms in (6), sum the harmonic differences in (5), and
normalize by T before applying the chain rule and Cauchy–Schwarz.
Formalization would require these finite-sum derivative and integration
identities, Markov's inequality, and the two L2 estimates. No numerical
certificate or external analytic input is needed.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
