# Lemma 152: Gaussian fourth moment with two logarithms

**Hypotheses.** Let S(t) and b_n(t) be as in L149. Let T tend to infinity.

**Conclusion.**

∫_T^(2T)|S(t)|⁴dt = O(T^(−2)log(2T)²).

There are constants a,c>0 such that, for all sufficiently large T,

meas{t∈[T,2T]: |S(t)|≥a T^(−3/4)} ≥ c T/log(2T)².

The one-logarithm upper bound and a positive-proportion conclusion remain unproved.

**Proof.**

Put N=sqrt(T/(2π)) and assume N≥2. For fixed β>0 define

w_n(β)=n^(−2)exp(−β log(n/N)²),
A_k(β)=Σ_{mn=k}w_m(β)w_n(β),
D_β(N)=Σ_k A_k(β)².

Constants may depend on fixed β. All these sums converge absolutely.

### Gaussian energy at any fixed width

We first prove D_β(N)≤C_β N^(−6)log(2N). The unique coprime parametrization in L151 and the same Gaussian midpoint identity give

D_β(N)=Σ_{(r,s)=1}(rs)^(−4)exp(−β log(r/s)²) H_β(N/sqrt(rs))²,

where H_β(X)=Σ_{g≥1}g^(−4)exp(−2β log(g/X)²).

For X≥1, the integral of x^(−4)exp(−2β log(x/X)²) is C_β X^(−3), and the integral of its absolute derivative is C'_β X^(−4). This follows by x=X exp(y); the integrands are exponentials of negative quadratic polynomials times, for the derivative, an absolute linear factor. Comparison on each [g−1,g], as in L151, yields H_β(X)≤C_β X^(−3). For X<1 the inequality exp(−2β log(z)²)≤C_β z^(−2) yields H_β(X)≤C_β X²≤C_β X^(−1). Thus

H_β(X)≤C_β X^(−3)min(1,X²).

Dropping coprimality bounds D_β by

C_β N^(−6) Σ_{r,s≥1}(rs)^(−1) exp(−β log(r/s)²)min(1,N⁴/(rs)²).

On dyadic blocks r∈[2^j,2^(j+1)), s∈[2^h,2^(h+1)), each reciprocal sum is at most one, and the Gaussian is at most C_β exp(−c_β(j−h)²). Write d=|j−h| and v=min(j,h). The remaining factor is at most min(1,N⁴2^(−4v)); its sum over v≥0 is O(log(2N)). The sum over d converges. This proves the energy bound with all tails included.

### Moving envelope and weighted energy

For t∈[T,2T], write u=log(N_t/N)∈[0,log(2)/2]. Since (x−u)²≥x²/2−u², L149's weights satisfy

b_n(t)≤C w_n(1/2).                                      (1)

We also need

Σ_k k log(2k) A_k(β)² ≤ C_β N^(−4)log(2N)².             (2)

Expand A_k(β)² as the nonnegative sum over mn=pq=k. Put x_i=log(n_i/N) for the four indices (m,n,p,q), Q=Σ_i x_i², and z=log(k/N²)=x_1+x_2. Then |z|≤sqrt(2Q). With L=log(2N)≥1,

k log(2k)/(N² L) ≤ C exp(z)(1+|z|).

Indeed log(2k)=log 2+2log N+z is positive, and is at most 2L+|z|. The function exp(sqrt(2Q))(1+sqrt(2Q))exp(−β Q/2) is bounded for Q≥0. Multiplying each expanded summand by k log(2k) therefore gives at most C_β N²L times the corresponding summand with β replaced by β/2. Tonelli and the energy bound prove (2).

Finally Σ_n w_n(β)=O_β(N^(−1)). To verify this directly, the Gaussian bound gives w_n(β)≤C_β N^(−2)min((n/N)²,(n/N)^(−4)); elementary power sums give the claim. Hence Σ_k A_k(β)=O_β(N^(−2)).

### Integrated fourth power

Use L150's absolutely convergent fourth-power expansion, retaining envelope (1) instead of its divisor envelope. Its diagonal is at most

C T D_(1/2)(N)=O(T N^(−6)log(2N)).

For k≠l, integration by parts on each individual four-weight product gives the bound C A_k(1/2)A_l(1/2)/|log(k/l)|. The justification is exactly the product variation argument of L150: each product is unimodal in log N_t, its variation is at most twice its supremum, and both endpoint terms are retained. No unimodality of a sum is required.

Pairs l≥2k and their reverses contribute at most C(Σ_k A_k(1/2))²=O(N^(−4)). For k<l<2k, use log(l/k)≥(l−k)/(2k) and 2A_k A_l≤A_k²+A_l². Summing the harmonic denominators with each index fixed, as in L150, bounds this contribution and its reverse by

C Σ_k k log(2k) A_k(1/2)² = O(N^(−4)log(2N)²).

These finite bounds also justify absolute summation of the integrated off-diagonal estimates. Since N²=T/(2π), the claimed fourth-moment bound follows.

For the measure conclusion let K>0 be the constant in L149 and choose a²=K/4. For sufficiently large T, the second moment is at least (K/2)T^(−1/2). If E is the indicated large-value set, its complement contributes at most (K/4)T^(−1/2). Cauchy–Schwarz gives

(K/4)T^(−1/2)≤meas(E)^(1/2)(∫_T^(2T)|S(t)|⁴dt)^(1/2).

Squaring proves the assertion. ∎

## Scope, verification, and formalization obligations

This is a scoped improvement of L150. The extra logarithm in this upper bound comes from taking absolute values and summing reciprocal frequency gaps. Nothing here proves that the signed off diagonal requires that logarithm, or that the full fourth moment has a matching lower bound. The diagonal lower bound in L151 cannot be substituted for a lower bound on the full moment. No pointwise nonvanishing or RH assertion follows.

Analytic verification comprises the Gaussian midpoint identity at general width, all-scale H_β bound, dyadic tail summability, Gaussian absorption of k log(2k), moving-envelope inequality, product variation and endpoint terms, and the measure deduction. No numerical certificate is required. Formalization would require those estimates, Tonelli, absolute uniform convergence on the integration interval, and integration by parts. L149 supplies the representation and second moment; L150 supplies the integrated expansion and harmonic-sum argument; L151 supplies the coprime parametrization and energy proof method.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
