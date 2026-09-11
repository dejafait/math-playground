# Lemma 174: derivative-test limit for last-block first moments

**Hypotheses.** Let T tend to infinity, N=sqrt(T/(2π)),
h=T/ceil(T^(1/4)), B=[2T−h,2T], and E_B denote normalized integration.
For N≤y≤2N let

P_y(t)=Σ_(N≤n≤y) exp(i(t−π/2)log(n/N)),
M_y=#{n integer: N≤n≤y}.

**Conclusion.** Uniformly for t in B and all these y,

|P_y(t)| ≤ C[1+M_y N^(−1/6)+M_y^(1/2)N^(1/6)]
          ≤ C' N^(5/6).                                      (1)

For the full endpoint one has

E_B|P_(2N)|²=N+O(1+N²log(2N)/h),                              (2)
c N^(1/6) ≤ E_B|P_(2N)| ≤ C sqrt(N).                         (3)

Thus the direct second- and third-derivative estimates do not establish
sup_y E_B|P_y|=o(sqrt(N)), the sufficient condition in L173.
This is a limitation of the displayed estimates, not a proof that the
condition is false or that stronger oscillatory methods cannot prove it.

**Proof.**

Put a=(t−π/2)/(2π) and f(x)=a log(x/N). For sufficiently large T,
N²/2≤a≤2N² uniformly on B. On [N,2N],

f'(x)=a/x, f''(x)=−a/x², f'''(x)=2a/x³.

In particular 1/8≤|f''|≤2 and
1/(8N)≤f'''≤4/N. The second-derivative test from foundations gives
only O(M_y+1). The third-derivative test there, with λ=1/(8N)
and fixed ratio A=32, gives the first bound in (1). Translation to
consecutive integer indices preserves all derivative bounds. Empty and
singleton sums obey the added constant, so no short-endpoint restriction
is needed. Since M_y≤N+1, (1) follows for every truncation.

For clarity, the averaged square can be checked directly without any
phase distribution hypothesis. Its diagonal is M_(2N)=N+O(1).
For m≠n the absolute value of the averaged phase integral is at most
2/(h|log(m/n)|); the constant shift π/2 only supplies a unit factor.
The mean value theorem gives 1/|log(m/n)|≤2N/|m−n|.
For each positive difference there are O(N) pairs, so the sum over
both orders is O(N²log(2N)/h). This proves (2).

Here h is comparable to N^(3/2), so that the error in (2) is o(N).
Consequently E_B|P_(2N)|²≥N/2 for large N. Applying the pointwise
inequality |P|²≤(sup_B|P|)|P| and (1) gives the lower bound in (3).
Cauchy–Schwarz and (2) give its upper bound. The same calculation for
a truncated sum gives uniformly E_B|P_y|²≤C N.

Averaging (1) and dividing by sqrt(N) gives O(N^(1/3)); using the
averaged square instead gives O(1). The lower bound in (3), divided
by sqrt(N), is only c N^(−1/3), which tends to zero. Neither upper
bound is little-o, and the lower bound does not rule out little-o.
For example, at the level of these bounds alone a nonnegative variable
of size N^(5/6) on a set of normalized measure N^(−2/3) has square
mean N and mean N^(1/6). This example is solely a logical check of
the inequalities, not a model for the actual phases. ∎

## Scope and verification

This audits the classical second- and third-derivative route only.
It supplies no first-moment asymptotic, uniform integrability, cutoff
covariance estimate or RH proof. In particular an estimate saving a
power over the trivial O(N) sum is not enough for L173.

Verification is analytic: exact derivatives, uniform constants over the
moving block and all truncations, both oscillatory endpoints, integer
counts, harmonic summation, and the direction of the first-moment lower
bound have been checked. Formalization would need the two named finite
sum derivative tests, the explicit finite square integration and these
inequalities. No numerical certificate is used.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
