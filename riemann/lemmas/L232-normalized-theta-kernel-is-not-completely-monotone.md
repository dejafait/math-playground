# Lemma 232: a normalized theta kernel is not completely monotone

**Hypotheses.** Let K be the actual theta kernel of L019. For x≥1 put

F(x)=x^(−5/4)K((log x)/2).

Complete monotonicity on (1,∞) means (−1)^k F^(k)(x)≥0 for every integer k≥0 and every x>1.

**Conclusion.** For every sufficiently large integer k,

(−1)^k F^(k)(k/π)<0.

Thus F is not completely monotone, even on any fixed terminal interval (a,∞). In particular it has no representation F(x)=∫_[0,∞) e^(−xt) dμ(t) there with μ a positive measure and the integrals finite. This conclusion concerns this normalization and variable only, not RH or all possible theta transforms.

**Proof.** The series in L019 gives

F(x)=Σ_{n≥1}(8π²n⁴x−12πn²)e^(−πn²x).

For each fixed derivative order, the series and its derivatives converge uniformly on compact subsets of x>0: each is bounded there by a fixed polynomial in n times e^(−πn²b), where b>0 is the compact interval's lower endpoint. Polynomial times Gaussian summability justifies termwise differentiation. Hence

(−1)^k F^(k)(x)=Σ_{n≥1}(πn²)^k[8π²n⁴x−(8k+12)πn²]e^(−πn²x).

At x=k/π, divide by the positive number 4π^(k+1)e^(−k). The result is

−3+R_k,   R_k=Σ_{n≥2} n^(2k+2)[2k(n²−1)−3]e^(−k(n²−1)).

For k≥4 the summands of R_k are positive and bounded above by

2k n⁴ exp(k[log(n²)−(n²−1)]).

For y≥4, log y≤(y−1)/2: the difference (y−1)/2−log y is increasing there and is positive at 4. To see the latter without a decimal approximation, e^(3/2)>1+3/2+(3/2)²/2+(3/2)³/6>4. Thus, with C=Σ_{n≥2}n⁴e^(−(n²−1))<∞,

0≤R_k≤2k Σ_{n≥2}n⁴e^(−k(n²−1)/2)
          ≤2k e^(−3k/4) Σ_{n≥2}n⁴e^(−(n²−1))
          =2Ck e^(−3k/4) → 0.

The second inequality splits k/2 into k/4+k/4, using n²−1≥3 and k/4≥1. Consequently −3+R_k<0 eventually, and k/π tends to infinity. This proves the sign failure on every terminal interval.

Finally, a positive Laplace representation finite on such an interval would imply all the signed derivative inequalities there. Indeed, at any interior x choose ε>0 with x−ε still in the interval. The bound t^j e^(−xt)≤C_(j,ε)e^(−(x−ε)t) supplies domination for each derivative (and, with a smaller ε, its neighborhood). Differentiation under the integral gives (−1)^j F^(j)(x)=∫t^j e^(−xt)dμ(t)≥0, a contradiction. ∎

The tested intermediate target was a positive Laplace measure for the exact theta expression, as a possible input to a future integral representation of the signed logarithmic forms. Even that target fails; no transfer from such a measure to L030 was assumed or proved. The achieved tail bound tends to zero relative to a strictly negative leading term. The required complete-monotonicity threshold was nonnegativity for every k and x, whereas the RH threshold remains every actual mixed form nonnegative.

**Mathlib.** Not checked for the full statement or its supporting differentiation and summability results. No matching library theorem is claimed. General documentation: https://leanprover-community.github.io/mathlib4_docs/
