# Lemma 242: a signed integral for the theta logarithmic derivative

**Hypotheses.** Let K be the actual positive theta kernel of L019, and set
F(x)=Ξ(i√x)=∫₀∞K(u)cosh(√x u)du for x≥0. Define G(x)=F′(x)/F(x) and the probability density p_x(u)=K(u)cosh(√x u)/F(x). For x>0 put

a_x(u)=u tanh(√x u)/(2√x),

b_x(u)=u² sech²(√x u)/(4x)−u tanh(√x u)/(4x^(3/2)),

D_x(u,v)=b_x(u)+b_x(v)+(a_x(u)−a_x(v))².

At x=0 use a_0(u)=u²/2 and b_0(u)=−u⁴/6.

**Conclusion.** All the following integrals converge absolutely, and

G′(x)=E_x[b_x]+Var_x(a_x)=½∫₀∞∫₀∞p_x(u)p_x(v)D_x(u,v)du dv.

For every fixed x≥0, D_x has both positive and negative values on open subsets of (0,∞)², each of positive p_x⊗p_x measure. In particular this exact representation does not prove G′≤0 by a pointwise sign, even for the actual theta kernel.

Near zero the reciprocal-node expansion is

G(x)=Σ_{k≥0}(−1)^k S_{k+1}x^k.

Under RH, G(x)=Σ_j β_j/(1+xβ_j) is a positive Stieltjes representation, equivalently ∫(x+t)^(−1)dν(t) with ν=Σ_jδ_{1/β_j}. This is a conditional representation, not an assertion of RH or an unconditional sign for G′.

**Proof.** L020 gives the integral for F, and L019 gives positivity and the superexponential bound on K. On every compact x interval, derivatives through order two of cosh(√x u), including at zero by its power series, are bounded by a fixed polynomial in u times e^{C u}. L019 makes these bounds integrable. Thus F is twice differentiable under the integral and strictly positive. The functions a and b are respectively the first and second x derivatives of log cosh(√x u); the displayed zero limits follow from log cosh y=y²/2−y⁴/12+O(y⁶). Their needed products also have integrable polynomial bounds on compact x intervals. Differentiating the normalized expectation gives G=E_x[a_x] and G′=E_x[b_x]+E_x[a_x²]−E_x[a_x]². Expanding the square of the difference of two independent copies proves the double integral and absolute convergence.

For x>0 and u>0, put y=√x u. The sign of b_x(u) is that of y sech²y−tanh y, which is strictly negative: h(y)=tanh y−y sech²y has h(0)=0 and h′(y)=2y sech²y tanh y>0. Therefore D_x(u,u)=2b_x(u)<0. For any fixed v>0, as u→∞,

a_x(u)=u/(2√x)+o(1),   b_x(u)=−u/(4x^(3/2))+o(1).

Consequently D_x(u,v)/u²→1/(4x)>0. This supplies positive values as well. At zero direct substitution gives

D_0(u,v)=(u⁴+v⁴−6u²v²)/12,

which is negative on the positive diagonal and positive for fixed v and sufficiently large u. Continuity extends each strict sign to an open rectangle about a suitable point. Since K is strictly positive on (0,∞), both rectangles have positive product probability. The positive regions can have very small weight; no sign of the whole integral follows from their existence.

For the expansion, L024 gives the paired product F(x)/F(0)=Π_j(1+xβ_j), with Σ|β_j|<∞. If |x| sup_j|β_j|<1, the logarithms and their derivative series converge absolutely locally uniformly, bounded by geometric series times Σ|β_j|. Hence G=Σ_jβ_j/(1+xβ_j), and geometric expansion gives the stated Taylor series (the empty product is harmless). Under RH all β_j>0, and on x≥0 the same derivative formula follows locally uniformly, using Σβ_j<∞ and denominators bounded away from zero. The positive measure ν is locally finite because only finitely many β_j exceed any positive threshold; ∫(1+t)^(−1)dν=Σβ_j/(1+β_j)<∞. This proves the conditional Stieltjes formula. ∎

The required first-derivative threshold is E_x[b_x]+Var_x(a_x)≤0, an integrated comparison, not merely b_x<0. The attained result is an exact signed representation and a failure of its pointwise-sign test; it supplies no new actual S_k or Hankel sign. A full positive Stieltjes measure with the appropriate finite inverse moments would give S_{k+1}=∫t^(−k−1)dν near zero and hence Q(q)=∫t^(−2)q(1/t)²dν≥0. Such a measure has not been constructed. Even proving G′≤0 for all x would leave that stronger representation and the all-degree condition unresolved. L044 already disproves generic logarithm preservation, and L046 records the general variance obstruction; the new test here is the explicit signed kernel on actual theta support in the squared imaginary-axis variable.

**Mathlib.** Not checked: coverage of the full statement and of supporting integral-differentiation and variance identities was not checked. No matching library theorem is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
