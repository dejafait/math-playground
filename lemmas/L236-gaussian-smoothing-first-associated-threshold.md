# Lemma 236: Gaussian smoothing repairs the finite first associated spectrum

**Hypotheses.** Use k_N, F_N and d_N from L234, with integer N≥1. For a>0 set

g_a(u)=(4πa)^(−1/2)exp(−u²/(4a)), k_{N,a}=g_a*k_N,

F_{N,a}(x)=∫_R k_{N,a}(u)e^(ixu)du,
A_{N,a}(t)=∫_R s²k_{N,a}(s+t)k_{N,a}(s−t)ds.

Define, wherever F_N(x)≠0,

R_N(x)=[F_N(x)F_N''(x)−F_N'(x)²]/[2F_N(x)²].

**Conclusion.** There is a finite strictly positive number a_N^*=sup_{F_N(x)≠0} R_N(x). For every a>0,

Â_{N,a}(2x)=e^(−2ax²)[F_N'(x)²−F_N(x)F_N''(x)+2aF_N(x)²]/4.

This spectrum is nonnegative for every real x if and only if a≥a_N^*. Every fixed a>0 removes the eventual negative tail:

Â_{N,a}(2x)=e^(−2ax²)[2a d_N² x^(−4)+O_{N,a}(x^(−6))]>0

for all sufficiently large x. Moreover F_{N,a}(z)=e^(−az²)F_N(z) on C, so smoothing preserves every complex zero and its multiplicity. No bound tending to zero for a_N^* as N→∞ is asserted.

**Proof.** The finite kernel has all exponentially weighted absolute moments by L234. Convolution with g_a retains this property and the pointwise decay hypothesis of L233: for each B>0,

|k_{N,a}(u)|≤C_B∫g_a(v)e^(−B|u−v|)dv
≤C_B e^(−B|u|)∫g_a(v)e^(B|v|)dv.

It is real, even and continuous, by dominated convergence in the convolution, using boundedness of k_N. Thus L233 applies. Exponential moments also justify the entire Fourier transforms and all their derivatives, locally uniformly in z. Fubini for the convolution at complex z is dominated by the product of the two exponentially weighted L¹ norms. The normalized Gaussian integral gives its transform e^(−az²): on the real axis this follows by differentiating the integral and integrating by parts to obtain J'(x)=−2axJ(x), J(0)=1; the identity theorem extends it to C. Hence F_{N,a}=e^(−az²)F_N. Differentiating this product twice and applying L233 yields the spectrum identity. The exponential factor never vanishes, proving the zero statement.

L234 gives, with d_N>0,

F_N²=4d_N²x^(−4)+O_N(x^(−6)),
F_N'²−F_N F_N''=−8d_N²x^(−6)+O_N(x^(−8)).

Inserting these proves the stated positive tail for every fixed a>0. Dividing the same estimates yields

R_N(x)=x^(−2)+O_N(x^(−4))

for large |x|, where evenness handles negative x. In particular F_N is nonzero outside a compact interval and R_N is positive sufficiently far out, tending to zero.

The function F_N is entire and not identically zero, as its nonzero tail already proves. It therefore has only finitely many real zeros in that compact interval. At a real zero r of multiplicity m≥1, write F_N(x)=(x−r)^m h(x) with real analytic h nonzero near r. On the punctured neighborhood,

R_N(x)=(log|F_N(x)|)''/2
=−m/[2(x−r)²]+(log|h(x)|)''/2 →−∞.

Away from these finitely many neighborhoods and the tails, R_N is continuous on a compact set and is bounded above. Its supremum is therefore finite, and its positive tail proves a_N^*>0. (It is also attained: choose a positive value, discard tails below half that value and zero neighborhoods with negative values, then maximize on the remaining compact set.) At nonzeros the bracket in the spectrum identity equals 2F_N²(a−R_N). At zeros it equals F_N'²≥0, including multiple zeros. This proves both directions of the threshold assertion. ∎

The achieved bound is an all-real-frequency first-level inequality for each finite N at a sufficiently large N-dependent smoothing width. To use these particular approximants in a limit to the actual theta transform, a sufficient additional target is a_N^*→0, allowing a_N≥a_N^* with a_N→0. No such estimate follows from fixed-N asymptotics: their constants and onset frequencies depend on N. Even that limit would establish only first associated-spectrum positivity, leaving higher-order conditions and the all-degree mixed forms unresolved. Zero preservation also prevents interpreting convolution as a general cure for nonreal zeros.

**Mathlib.** Not checked for the full statement or supporting Gaussian Fourier, analytic zero factorization, convolution, and compactness results. No full matching theorem is claimed. General documentation: https://leanprover-community.github.io/mathlib4_docs/
