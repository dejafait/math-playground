# Lemma 281: uniform summation of positive-argument stationary patches

**Hypotheses.** Use the parameters and exact summands of L280, with a→∞ and log a≤h≤2 log a. Let ε=1/100. Allow j,k to depend on a, and let P_a be the finite set of positive integer pairs with jk>1 and

r−log j≥r/4,   r−log k≥r/4.

For each pair define J_jk over the full square |p|,|q|≤ε exactly as in L280. These squares have positive real kernel arguments for sufficiently large a, though a boundary square can extend slightly below r/4.

**Conclusion.** With an absolute constant C, uniformly in the stated range,

Σ_((j,k)∈P_a) |J_jk| ≤ C exp(Φ_*) a^(−1) h² exp(−(log 2−1/5)h)
                         =o(exp(Φ_*)/a).

The sum is over individual summands on their own patches, not the full theta kernel on the union of the patches. No disjointness is assumed and no complementary-region estimate is asserted.

**Proof.** Put b=log(jk)/2 and s₀=r−b. The index restrictions imply r/4≤s₀≤r. The exact algebraic identity in L280 holds also for these growing pairs: after removing (8π²)²exp(Φ_*)W_jk exp(ia log(k/j)), the integrand is

A_b(p,q) E(p,q) exp(if(p)−if(q)),

where v=(p+q)/√2, c=2√2,

S_b=log A_b=2n log(1+v/s₀)+9v−(h/2)(exp(cp)+exp(cq)−2),
f(y)=−(a/2)(exp(cy)−1−cy),
W_jk=(jk)^(−1/2)(1−b/r)^(2n).

The exact lower-degree factor E is

E=(1−3 exp(−cp)/(2V_+))(1−3 exp(−cq)/(2V_-)),
V_±=πexp(2r±2iτ),   |V_±|=sqrt(a²+h²)/2.

In particular E and its first derivatives and mixed derivative are bounded by an absolute constant on the fixed square, uniformly over all pairs. The cancellation of j,k inside these factors is essential.

We use a deliberately coarse amplitude bound instead of the fixed-pair Gaussian envelope. Since log(1+t)≤t and |v|≤√2ε, n=r(h−9/2)≤rh gives

S_b≤8√2ε h+9√2ε+h(1−exp(−2√2ε))
   ≤10√2ε h+9√2ε≤h/5

for sufficiently large h. The last inequality uses √2<3/2 and h→∞; its constants are independent of j,k. Also s₀+v≥r/4−√2ε≥r/5 eventually. Direct differentiation therefore gives

|S_b,p|+|S_b,q|≤Ch,   |S_b,pq|=n/(s₀+v)²≤Ch,

using r→∞. Hence A_b, its first derivatives, and its mixed derivative have absolute values at most C h² exp(h/5), for h≥1. The product H=A_b E has the same bounds. Its corner value, two edge derivative integrals, and mixed derivative area integral are consequently at most C h² exp(h/5), since the square has fixed size.

For completeness, on every subinterval of [−ε,ε] the primitive of exp(±if(y)) is O(a^(−1/2)), uniformly. Indeed f''=−4a exp(cy) has size comparable to a, f' is monotone, and its unique zero is zero. The portion |y|≤a^(−1/2) has this length bound. On either remaining portion integration by parts yields endpoint terms bounded by C/√a, while the integral of |f''|/|f'|² is a difference of reciprocal slopes and has the same bound. Splitting any interval into these three portions proves the assertion.

Apply the finite-rectangle fundamental-theorem-of-calculus identity proved in L275 to the complex amplitude H. It bounds the double oscillatory integral by the product of its two primitive bounds times the corner/edge/mixed variation just estimated. Thus

|J_jk|≤C exp(Φ_*) a^(−1) W_jk h² exp(h/5).             (1)

There is no absolute integration error from dropping E: it has been retained in the signed estimate.

Finally log(1−b/r)≤−b/r and n/r=h−9/2 give W_jk≤(jk)^(4−h). For t=h−4≥2, elementary integral comparison gives

q_t:=Σ_(m≥2)m^(−t)≤2^(−t)+∫_2^∞ x^(−t)dx≤3·2^(−t).

Consequently Σ_(j,k≥1,jk>1)(jk)^(−t)=2q_t+q_t²≤C2^(−t). The equality follows from multiplication of absolutely convergent positive series. Sum (1) over the finite set P_a and enlarge the weight sum to all pairs to prove the stated bound. Since log 2>1/5, h≥log a and h≤2 log a, its ratio to exp(Φ_*)/a is at most C(log a)² a^(−(log 2−1/5)), tending to zero. ∎

Overlapping patches create no double counting of an individual summand: each pair is integrated on its own assigned square. To use this in a full integral decomposition one must still control each summand outside its assigned square and justify the series/integral manipulation on the full domain. Pairs whose centers fall outside P_a, reflected sectors, and the remaining nonstationary regions are not bounded here. In particular this result does not extend L277's global sign range or complete L266's witness target.

**Mathlib.** Full statement: not checked. Supporting oscillatory integration by parts, finite-rectangle integration, and positive-series multiplication: not checked. No library match is claimed. L280 supplies the exact translated-summand algebra and parameter convention; L275 supplies the rectangle identity. The uniform amplitude and summation estimates are proved here.
