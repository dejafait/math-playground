# Lemma 140: Poisson representation with controlled tail

**Hypotheses.** Let S(t) be the series in L138, with real t>0. Put

N=sqrt(t/(2π)), τ=t−π/2, C(t)=exp(π²/16+iπ log(N)/2),

I_k(t)=∫₀^∞ x^(−2+iτ) exp(−log²(x/N)) exp(−2πikx) dx,   k∈Z.

All powers of positive real numbers use their real logarithms.

**Conclusion.** The following is an exact, absolutely convergent representation:

S(t)=C(t) Σ_{k∈Z} I_k(t).                                      (1)

The zero mode is

I_0(t)=sqrt(π) N^(−1+iτ) exp((−1+iτ)²/4).                       (2)

For every integer K≥1,

|S(t)−C(t)Σ_{|k|≤K}I_k(t)|
 ≤ e^(π²/16) sqrt(π)e^(9/4) N^(−3)
       [2(|τ|+3)²+24]/(2π²K).                                 (3)

In particular, K=ceil(t²) gives an O(t^(−3/2)) error as t→∞. This is smaller than the O(t^(−1)) normalized remainder in L138. No lower bound for S or for the finite sum in (3) is asserted.

**Proof.**

Define f(x)=x^(−2+iτ)exp(−log²(x/N)) for x>0, and f(x)=0 for x≤0. For fixed t, every derivative on x>0 is x^(−2−j+iτ) times exp(−log²(x/N)) times a polynomial in log(x/N). The factor exp(−y²) decays faster than exp(A|y|) for every fixed A. Thus every derivative tends to zero at x=0 from the right, and every derivative times any power of x tends to zero at positive infinity. Extending by zero makes f a Schwartz function on R. This assertion is for each fixed t; no uniform Schwartz bound in t is being assumed.

For completeness, Poisson summation here follows directly by periodization. The series P(u)=Σ_{n∈Z}f(u+n), together with its derivatives, converges uniformly for u∈[0,1] by Schwartz decay, and defines a smooth periodic function. Integrating over [0,1] and using absolute convergence gives its kth Fourier coefficient as I_k(t). Two integrations by parts, with zero boundary terms, give for k≠0

|I_k(t)|≤||f''||_1/(4π²k²).                                   (4)

Consequently its Fourier series converges absolutely and uniformly. It equals P: for example, the difference has every Fourier coefficient zero, and Fejér's theorem for continuous periodic functions forces that difference to vanish. Evaluating at u=0 gives Σ_{n≥1}f(n)=Σ_k I_k(t); f(0)=0 and all negative integer terms vanish. Expanding the square in L138 gives exactly S(t)=C(t)Σ_{n≥1}f(n), proving (1).

We now bound the norm in (4) explicitly. Write y=log(x/N), a=−2+iτ. Direct differentiation yields

f''(x)=x^(−4+iτ)e^(−y²)[(a−2y)(a−1−2y)−2].

Using |a−2y|≤|τ|+2+2|y| and |a−1−2y|≤|τ|+3+2|y| gives

|(a−2y)(a−1−2y)−2|
 ≤ (|τ|+3+2|y|)²+2
 ≤ 2(|τ|+3)²+8y²+2.

After x=N e^y, the measure x^(−4)dx becomes N^(−3)e^(−3y)dy. Completing the square gives

∫_R e^(−y²−3y)dy=sqrt(π)e^(9/4),
∫_R y²e^(−y²−3y)dy=(11/4)sqrt(π)e^(9/4).

Therefore

||f''||_1≤N^(−3)sqrt(π)e^(9/4)[2(|τ|+3)²+24].                  (5)

Summing (4) over |k|>K and using Σ_{k>K}k^(−2)≤1/K proves (3), since |C(t)|=e^(π²/16). As N^(−3)=O(t^(−3/2)) and the bracket is O(t²), choosing K=ceil(t²) gives the stated O(t^(−3/2)) bound. This proves an explicit truncation estimate even though K grows with t.

Finally, the same logarithmic substitution in I_0 gives

I_0=N^(−1+iτ)∫_R exp(−y²+(−1+iτ)y)dy.

The Gaussian identity ∫ exp(−y²+zy)dy=sqrt(π)exp(z²/4) holds for complex z: prove it by completing the square for real z and then use the identity theorem, with Gaussian domination on compact z sets. This proves (2). ∎

## Cancellation scope

The zero mode has modulus sqrt(π)e^(1/4)N^(−1)exp(−τ²/4), hence is o(t^(−1)). It cannot alone establish a lower bound dominating L138's remainder. For t>π/2, the phase of I_k is τ log x−2πkx. Its derivative is τ/x−2πk. Each positive k has one stationary point x_k=τ/(2πk); nonpositive k have none. In the amplitude coordinate,

x_k/N=τ/(2πkN)=(τ/t)(N/k).

Thus indices k comparable to N have stationary points at x comparable to N. This locates a relevant range; it is not a uniform stationary-phase expansion or an estimate of the sum over that range. The negative modes, remote positive modes, and combined positive-mode cancellation must still be controlled for any sharper conclusion. Neither absolute convergence nor the small truncation error bounds the retained sum away from zero.

## Verification and formalization obligations

Analytic validation covers smooth extension at zero, Schwartz decay, uniform periodization, Fourier uniqueness, boundary terms in both integrations by parts, the explicit second derivative and Gaussian moments, and the t-dependent cutoff bound. No numerical evidence or computational certificate is used. Formalization would require precisely these analytic facts, the complex Gaussian identity, and the elementary phase derivative calculation. The comparison to the theta center uses only L138's additive expansion; no RH-equivalent assertion is used as a premise.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
