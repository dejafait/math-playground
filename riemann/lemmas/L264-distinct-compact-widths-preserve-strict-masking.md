# Lemma 264: distinct compact widths preserve strict masking

**Hypotheses.** Use Q=−E and c_0,…,c_7 from L262. Write S_w(z)=sin(wz)/(wz), with its removable value at zero, and let D_n be the coefficient of y^(2n) in F(x+iy)F(x−iy).

**Conclusion.** There exist sixteen distinct widths 0<w_j<π/4 such that F(z)=Q(z)∏_(j=1)^16 S_(w_j)(z) is the Fourier transform of an even continuous compactly supported nonnegative kernel, positive throughout the support interior. F has order exactly one, all its zeros are simple and obey |Re z|>4 and |Im z|<1/2, including the nonreal zeros ±10±i/4. For every real x, D_n(F;x)>0 for n=1,2,3. These generic combined hypotheses do not imply real zeros; no actual-theta assertion follows.

**Proof.** First take all widths δ=3/4. Let B be the sixteen-fold convolution of the uniform density on [−1,1]. As in L263, the candidate kernel is K_δ=Σ_(k=0)^7 c_k B_δ^(2k), where B_δ(t)=δ^−1 B(t/δ). We certify its interior positivity at this particular width, replacing L263's unspecified large-width threshold.

On the interval u=−16+2j+2v, 0≤v≤1, j=0,…,7, the polynomial 2^16 δ K_δ(δu) has power coefficients

 a_(j,l)=Σ_(k:15−2k≥l) Σ_(h=0)^j c_k (4/3)^(2k) (−1)^h binom(16,h) binom(15−2k,l) 2^l [2(j−h)]^(15−2k−l)/(15−2k)!.

Here 0^0=1. This follows directly by differentiating the truncated-power formula in L263. Its degree-fifteen Bernstein coefficients are

 β_(j,i)=Σ_(l=0)^i a_(j,l) binom(i,l)/binom(15,l),  0≤i≤15.

Exact rational substitution gives β_(0,0)=0, β_(0,i)>0 for i≥1, and β_(j,i)>0 for j=1,…,7 and every i. These 128 finite rational sign checks are reproduced in `python3 scripts/laguerre/compact_width_check.py`, which constructs the c_k from their rational product and uses only integer arithmetic and fractions. This is an exact arithmetic certificate, not sampled positivity. The conversion identity follows by expanding v^l in the basis binom(15,i)v^i(1−v)^(15−i). Each basis element is nonnegative on [0,1]; hence K_δ is positive on the left support interior. Evenness proves the right half. The endpoint value is zero.

We next prove that this certificate survives sufficiently small changes of all sixteen widths. Put A=Σ_j w_j. The convolution B_w of the uniform densities on [−w_j,w_j] has the formula

 B_w(t)=[(∏_j 2w_j)15!]^−1 Σ_(J⊆{1,…,16}) (−1)^|J| (t+A−2Σ_(j∈J)w_j)_+^15.

Its derivatives through order fourteen are continuous jointly in t and the positive widths, by differentiating this finite formula. Set K_w=Σ_k c_k B_w^(2k). On a fixed compact interval this varies uniformly continuously with the widths. On the left edge, 0<t+A<2 min_j w_j, only the empty subset contributes, so all even derivatives used in K_w are nonnegative and its zeroth term is positive. Reflection gives the same assertion on the right edge.

For precision, restrict widths sufficiently close to 3/4 that |A−12|<1/4 and min w_j>1/2. Points inside the support whose distance to an endpoint is less than 1/2 have positive kernel by the preceding edge argument. Every remaining support point belongs to [−11.75,11.75], a fixed compact subset of the original support (−12,12). The original kernel has a positive minimum there. Uniform continuity therefore makes K_w positive there as well after shrinking the width neighborhood. Outside [−A,A] it vanishes. This proves positivity for an open neighborhood of the equal-width vector, not only for a sequence of widths.

Choose a vector in this neighborhood with each w_j<π/4, all ratios w_i/w_j irrational for i≠j, and w_j r/π not an integer for each real zero r of Q. Such a choice exists: the forbidden relations form countably many affine hyperplanes of measure zero in a nonempty open box. It gives no shared zeros among sinc factors or between them and Q. L262 gives simplicity of Q's zeros. All new zeros are real and have absolute value at least π/max w_j>4; the old zeros have the stated localization.

Integration by parts through order fourteen, with vanishing boundary derivatives, gives the Fourier transform of K_w as Q∏ S_(w_j). These steps are justified exactly as in L263: derivatives through order fourteen are continuous and piecewise polynomial. The support is compact. The sine products give nonnegative D_n for the multiplier M=∏ S_(w_j) at every level. If M(x)≠0, the summand D_n(Q;x)M(x)^2 is strictly positive for n=1,2,3 by L261 (as used in L262). If M(x)=0, its zero is simple and Q(x)≠0. Then D_1(M;x)=M′(x)^2>0. For n=1 use D_0(Q;x)D_1(M;x)>0; for n=2,3 use D_(n−1)(Q;x)D_1(M;x)>0. Every other summand in the coefficient convolution is nonnegative. Thus all three signs are strict everywhere.

Finally exponential type gives order at most one; on z=ir,

 log|F(ir)|=Ar−2 log r+O(1)

because Q has degree fourteen and there are sixteen sinc factors. Thus the order is exactly one. ∎

The attained bound is the concrete admissible width 3/4<π/4 with an open positivity neighborhood. The actual required RH threshold remains all-degree actual-theta positivity. The compact kernel is not claimed to satisfy theta's modular identity, strict log-concavity, or its exact growth and zero density.

**Mathlib.** Not checked for the full statement or supporting Bernstein conversion, convolution, or measure-zero facts. No matching theorem name is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
