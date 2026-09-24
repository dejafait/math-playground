# Lemma 235: modularly averaged truncations lose integral convergence

**Hypotheses.** For N≥1 and real u define

A_N(u)=e^(u/2) Σ_{n=1}^N exp(−πn²e^(2u)),
B_N(u)=(A_N(u)+A_N(−u))/2,
S_N(u)=2B_N''(u)−B_N(u)/2.

Let K be the smooth even actual theta kernel of L019, extended to R by the theta transformation of L016. Put C=Γ(1/4)/(4π^(1/4))>0, where Γ(a)=∫_0^∞ t^(a−1)e^(−t)dt for a>0.

**Conclusion.** S_N is smooth, even, and integrable with every absolute polynomial moment. For fixed N, at both ends,

S_N(u)=−6π(Σ_{n=1}^N n²)e^(−5|u|/2)+O_N(e^(−9|u|/2)).

S_N converges to K with all derivatives on every compact real interval, but

∫_R S_N(u)du=−C Σ_{n=1}^N n^(−1/2) → −∞.

Consequently S_N does not converge to K in L¹(R), nor do its Fourier transforms converge to the Fourier transform of K at frequency zero. Smoothness and individual integrability do not suffice for this approximation strategy.

**Proof.** Write D=d/du, v_n=πn²e^(2u), and T_N=(2D²−1/2)A_N. Direct differentiation gives

T_N(u)=Σ_{n=1}^N (8v_n²−12v_n)e^(u/2−v_n),
S_N(u)=(T_N(u)+T_N(−u))/2.

All these finite sums are smooth. As u→+∞, T_N(u) decays faster than every exponential. At the reflected argument v_n=πn²e^(−2u)→0. Taylor's formula e^(−v)=1−v+O(v²) gives

(8v²−12v)e^(−v)=−12v+20v²+O(v³).

Multiplying by e^(−u/2), summing finitely many terms, and dividing by two proves the stated positive-end expansion. Evenness proves the other end. The exponential tails prove all the asserted absolute moments; the coefficient is strictly negative.

For compact convergence, the Gaussian series defining A(u)=e^(u/2)ψ(e^(2u)) and each of its derivatives converges uniformly on every compact real interval. Indeed e^(2u) has a positive lower bound there, and each differentiated summand is bounded by a fixed polynomial in n times exp(−c n²) for c>0. L016's transformation gives

A(u)−A(−u)=−sinh(u/2).

The operator 2D²−1/2 annihilates the right side and commutes with reflection. Thus (2D²−1/2)A is even and agrees with K on u≥0 by L019, and applying the operator to the averaged infinite A also gives K. Uniform convergence of each required derivative proves compact convergence of S_N and all its derivatives.

For the integral, A_N and A_N' tend to zero at both ends: at +∞ they have superexponential decay, while at −∞ they are O_N(e^(u/2)). Their second derivatives are integrable by the same bounds. Hence integration of the second derivative gives zero boundary contribution, and reflection preserves the integral, so

∫_R S_N=−(1/2)∫_R B_N=−(1/2)∫_R A_N.

For each finite summand, substitute t=πn²e^(2u), du=dt/(2t), obtaining

∫_R e^(u/2)exp(−πn²e^(2u))du
= Γ(1/4)/(2π^(1/4) sqrt(n)).

This proves the integral identity without interchanging an infinite sum and an integral. The sum of n^(−1/2) diverges, for example because its first N terms sum to at least sqrt(N). In contrast K is positive and integrable by L019 and evenness, so its integral is finite and strictly positive. Thus

‖S_N−K‖_1 ≥ |∫_R(S_N−K)| = C Σ_{n=1}^N n^(−1/2)+∫_R K → ∞.

At frequency zero the Fourier integral is exactly the integral just computed. This proves its failure to converge as well. ∎

The modular identity can alternatively be imposed at the A level by setting A_N^*(u)=B_N(u)−sinh(u/2)/2. Then A_N^*(u)−A_N^*(−u)=−sinh(u/2) exactly, but applying 2D²−1/2 still gives S_N. This natural correction therefore does not repair the failed integral limit. The result concerns this averaging construction only, not every smooth approximation, the actual associated spectrum, or RH. It does not assert that a negative spatial tail alone refutes associated-kernel positive definiteness.

**Mathlib.** Not checked for the full statement or supporting results. The Gamma integral above is its defining convergent integral and is evaluated by an explicit substitution; no library theorem is assumed. Supporting theta-transformation references are retained in L016 and are not matches for this full statement. General documentation: https://leanprover-community.github.io/mathlib4_docs/
