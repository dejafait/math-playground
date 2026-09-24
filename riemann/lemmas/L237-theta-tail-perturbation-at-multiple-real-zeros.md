# Lemma 237: theta tail concentration and a multiple-zero smoothing obstruction

**Hypotheses.** Use the finite transforms F_N and smoothing thresholds a_N^* of L236. Let F(x)=∫_R K(|u|)e^(ixu)du=2Ξ(x), with K from L019 and L020, and let

T_N(u)=K(u)−f_N(u) (u≥0), ε_N=2∫_0^∞T_N(u)du, E_N=F−F_N.

For the conditional conclusion only, suppose F has a real zero r of even multiplicity m≥2 with F(r+h)=−c h^m+O(h^(m+1)), c>0.

**Conclusion.** The numbers ε_N are positive and tend to zero. For each fixed integer j≥0,

2∫_0^∞u^j T_N(u)du ≤ C_j [π(N+1)²]^(−j) ε_N.

Uniformly on every fixed real compact interval, E_N/ε_N→1, E_N'/ε_N→0 and E_N''/ε_N→0. Under the additional multiple-zero hypothesis there is C>0 such that

a_N^* ≥ C ε_N^(−2/m) →+∞.

Thus vanishing smoothing widths require, among other things, the absence of negative-leading even-multiplicity real zeros. Such a zero is not asserted to exist. This restriction is stronger than anything about real-zero multiplicity supplied by RH alone.

**Proof.** Positivity and integrability of each theta summand follow from L019. Monotone convergence of the positive series gives ε_N>0 and ε_N→0. To obtain relative rather than merely absolute error estimates, write b=πn² and v=b e^(2u). The positive nth summand satisfies

K_n(u)du=2 b^(−1/4)(2v−3)v^(−3/4)e^(−v)dv, v≥b.

For b≥π>3, this density is bounded above and below by fixed positive constants times b^(−1/4)v^(1/4)e^(−v)dv. Set v=b+w. The integral without u^j is at least C e^(−b), by restricting w to [0,1]. Since u=(1/2)log(1+w/b)≤w/(2b), its jth moment is at most

C' (2b)^(−j)e^(−b)∫_0^∞w^j(1+w/π)^(1/4)e^(−w)dw.

The last integral is finite. Division proves that the jth moment of each summand is at most C_j b^(−j) times its mass. Summing n>N proves the stated inequality by Tonelli.

The cosine integral gives E_N(x)=2∫T_N(u)cos(xu)du. For |x|≤M, use |cos(xu)−1|≤M²u²/2, |sin(xu)|≤1, and |cos(xu)|≤1, and differentiate under the integral using these absolute moments. With B_N=π(N+1)² this yields

|E_N(x)/ε_N−1|≤C_M B_N^(−2),
|E_N'(x)|/ε_N≤C_1 B_N^(−1),
|E_N''(x)|/ε_N≤C_2 B_N^(−2).

These estimates prove the compact limits without an interchange of a supremum over all frequencies.

For the conditional obstruction put δ_N=ε_N^(1/m) and G_N(y)=ε_N^(−1)F_N(r+δ_N y). Analytic Taylor expansion at r gives convergence, with the first two y derivatives on bounded y intervals, of ε_N^(−1)F(r+δ_N y) to −c y^m. The estimates above show that ε_N^(−1)E_N(r+δ_N y) converges with those same derivatives to 1: differentiation introduces δ_N or δ_N², respectively. Consequently

G_N → G, G(y)=−(1+c y^m), in C² on bounded real intervals.

Choose a fixed y_0>0 with c y_0^m=(m−1)/2. The limit is nonzero there and

(log|G|)''(y_0)=c m y_0^(m−2)[(m−1)−c y_0^m]/(1+c y_0^m)² >0.

At x_N=r+δ_N y_0, F_N(x_N)≠0 for large N and the definition in L236 gives

δ_N² R_N(x_N)=[G_N(y_0)G_N''(y_0)−G_N'(y_0)²]/[2G_N(y_0)²]
→(log|G|)''(y_0)/2 >0.

Since a_N^*≥R_N(x_N), the claimed lower bound follows. All estimates here concern a shrinking neighborhood of one fixed real zero; no fixed-N Fourier-tail asymptotic is used. ∎

The achieved unconditional estimate is concentration of the omitted mass, not control of the logarithmic derivative. Even arbitrarily small absolute errors can produce a diverging smoothing threshold under the stated local zero geometry. The actual required bound remains a_N^*→0. Neither the multiple-zero hypothesis nor its negation has been proved here for actual theta. Simple zeros, other multiple-zero signs, nonzero compact regions, and N-dependent large frequencies require separate treatment. This result neither disproves the proposed theta limit nor proves any RH assertion.

**Mathlib.** Not checked for the full statement or supporting moment, Taylor, and differentiation-under-integral results. No full matching theorem is claimed. General documentation: https://leanprover-community.github.io/mathlib4_docs/
