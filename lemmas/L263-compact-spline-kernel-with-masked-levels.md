# Lemma 263: compact spline kernels retain three nonnegative masked levels

**Hypotheses.** Let E and the strictly positive coefficients c_0,…,c_7 be as in L262, so Q(z)=−E(z)=Σ_(k=0)^7 (−1)^k c_k z^(2k). Fix an integer m≥8, put N=2m, and define S_δ(z)=sin(δz)/(δz), with its removable value at zero. Define D_n by coefficient extraction from F(x+iy)F(x−iy).

**Conclusion.** For all sufficiently large δ>0, F_δ=Q S_δ^N is the Fourier transform of an even continuous nonnegative compactly supported kernel, strictly positive in the interior of its support. It is entire of order exactly one, retains the nonreal zeros ±10±i/4, and satisfies D_n(F_δ;x)≥0 for every real x and n=1,2,3. These inequalities are not strict: all three vanish at every nonzero sinc zero. Simplicity and the coarse localization of L262 are not preserved. This does not settle the generic criterion with those extra hypotheses or any actual-theta sign.

**Proof.** Let B be the convolution of N copies of (1/2)1_[−1,1]. Elementary repeated integration gives

B(t)=[2^N(N−1)!]^(−1) Σ_(j=0)^N (−1)^j binom(N,j)(t+N−2j)_+^(N−1).

One can derive this formula by writing each uniform density as one half the difference of two translated Heaviside functions, then convolving N times; integrating a Heaviside N−1 times gives t_+^(N−1)/(N−1)!. In particular B is even, supported on [−N,N], is C^(N−2), and is strictly positive inside: for |t|<N there is an open set of choices of the first N−1 summands in (−1,1) whose remaining summand also lies in (−1,1). Its convolution integral is positive on that set.

On the rightmost unit interval N−1≤t≤N, reflection of the first polynomial piece gives B(t)=(N−t)^(N−1)/[2^N(N−1)!]. Thus every even derivative B^(2k), 0≤k≤7, is nonnegative there, and the same holds on the reflected interval. All fourteen derivatives used are continuous, including at the endpoints, since N≥16.

On I=[−N+1,N−1] put β=min_I B>0, M_k=max_I |B^(2k)|, and A=Σ_(k=1)^7 c_k M_k. These are finite constants determined by finitely many polynomial pieces. For

δ≥max(1, sqrt(2A/(c_0 β))),

set B_δ(t)=δ^(−1)B(t/δ) and K_δ=Σ_(k=0)^7 c_k B_δ^(2k). On t/δ∈I,

δ K_δ(t)≥c_0 β−Σ_(k=1)^7 c_k δ^(−2k) M_k≥c_0 β/2>0.

On either remaining interior edge interval every summand is nonnegative and c_0 B_δ>0. Outside the support the kernel is zero. This proves the claimed sign, including the boundary value zero. This is an explicit sufficient threshold in terms of finite polynomial extrema; no numerical sign extrapolation is needed.

The transform of B_δ is S_δ^N, by the elementary integral of a uniform density and Fubini for compact integrable functions. Repeated integration by parts gives the transform of B_δ^(2k) as (−1)^k z^(2k)S_δ(z)^N. There are no endpoint terms: derivatives through order thirteen vanish at the support endpoints. The derivative of order thirteen is absolutely continuous, and the derivative of order fourteen is continuous and piecewise polynomial, so these integrations remain legitimate even at knots. All integrals converge for every complex z. This proves the transform identity for K_δ.

The classical Euler sine product S_δ(z)=∏_(j≥1)(1−δ²z²/(j²π²)) converges locally uniformly. For a real root pair ±a, the corresponding product at x±iy is

(1−x²/a²)² + 2(a²+x²)y²/a⁴ + y⁴/a⁴.

Its coefficients are nonnegative. Finite products and then locally uniform convergence (hence coefficient convergence in y) imply D_n(S_δ^N;x)≥0 for every n. Multiplication convolves these coefficients. L261 gives D_0(E;x)≥0 and D_n(E;x)>0 for n=1,2,3, proving the stated nonnegativity for F_δ.

At each a=jπ/δ, j≠0, the factor S_δ^N has a zero of multiplicity N. The multiplicity of F_δ there is at least N, so F_δ(a+iy)F_δ(a−iy) vanishes to order at least 2N in y. Therefore D_n(F_δ;a)=0 for n<N, including the three tested levels. The multiplier has only real zeros, so it cannot remove any nonreal zero of Q. The exponential-type upper bound follows from |sin(δz)|≤exp(δ|z|) and polynomial growth. Along z=ir, log|F_δ(ir)|=Nδr+(14−N)log r+O(1), proving order exactly one. For arbitrarily large allowed δ, the new roots ±π/δ also violate |Re z|>4. ∎

The attained threshold is order one and a nonnegative compact Fourier kernel together with three global nonnegative levels. The required main threshold remains actual-theta all-degree positivity. The loss of strictness is unavoidable for this power multiplier, while the sufficient large-width estimate provides no compatibility certificate for keeping all new roots outside the known zero-free rectangle.

**Mathlib.** Not checked for the full statement or supporting convolution, spline, integration-by-parts, and Euler sine-product results. No matching theorem name is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
