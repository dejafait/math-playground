# Current best argument — incomplete

STATUS: IN_PROGRESS

Updated: 2026-09-09. This write-up contains classical analytic partial results, explicit obstructions to insufficient proof strategies, and two finite interval certificates. It does not prove RH. The all-degree positivity condition in Corollary 32a is explicitly RH-equivalent and unproved.

## Starting theorems and definitions

For Re(s)>1, define ζ(s)=Σ_{n≥1} n^{-s}, where n^{-s}=exp(-s log n) with the real logarithm. Use the standard meromorphic continuation theorem for the Riemann zeta function: this extends to C with its only pole a simple pole at 1. Use Riemann's functional equation

ζ(s)=2(2π)^{s-1} sin(πs/2) Γ(1-s) ζ(1-s).

Reference: the standard named Riemann functional equation, also [NIST DLMF 25.4.2](https://dlmf.nist.gov/25.4.E2). Other starting tools are the identity theorem for meromorphic functions, the fundamental theorem of arithmetic, absolute convergence and rearrangement of series, and the standard theorem that Γ is holomorphic and nonzero on Re(s)>0. Further named inputs used below are the Weierstrass theorem for locally uniform holomorphic limits, the fundamental theorem of algebra, the Gaussian integral, Poisson summation for Schwartz functions, and Euler’s gamma integral Γ(z)=∫_0^∞e^{-u}u^{z-1}du for Re(z)>0. The standard named Hadamard factorization theorem is used in Lemma 24 only after proving its finite-order hypothesis. No RH-equivalent result is an input.

## Lemma DAG

Absolute convergence → reciprocal series → nonvanishing on Re(s)>1.

Dirichlet series + continuation → conjugation symmetry.

Functional equation + conjugation symmetry → zero orbits in the open strip.

Explicit polynomial → these symmetries do not imply RH.

Euler-product logarithm → nonnegative trigonometric sum → nonvanishing on Re(s)=1.

Boundary nonvanishing + functional equation + ζ(0)=-1/2 → all nontrivial zeros lie in the open strip.

Poisson summation → theta transformation → split Mellin integral → entire ξ and even real Ξ with exact zero correspondence.

Positive theta kernel → moment expansion and growth → unconditional paired Hadamard product → reciprocal-zero identities.

Theta tail → zero-free rectangle → six scalar signs and degree-two Jensen test.

Summable reciprocal nodes → mixed Hankel forms → explicit RH equivalence, with its positivity unproved.

Theta tail bounds + validated Taylor quadrature + outward arithmetic → finite positive definiteness of H_1 and H_2 only.

## Lemma 1: an absolutely convergent reciprocal

**Hypotheses.** Re(s)=σ>1. Define μ(1)=1, μ(n)=0 if a prime square divides n, and μ(n)=(-1)^k if n is a product of k distinct primes.

**Conclusion.** M(s)=Σ_{n≥1} μ(n)n^{-s} converges absolutely and ζ(s)M(s)=1. In particular ζ(s)≠0.

**Proof.** Since |μ(n)|≤1, both series are dominated by Σ n^{-σ}<∞, whose convergence follows from the integral test. The double series for their product has sum of absolute values at most (Σ n^{-σ})². It can therefore be grouped by the product of the indices, giving

ζ(s)M(s)=Σ_{k≥1} k^{-s} Σ_{d|k} μ(d).

For k>1 with r distinct prime factors, the inner sum is Σ_{j=0}^r binom(r,j)(-1)^j=(1-1)^r=0. For k=1 it is 1. This proves the claim. No continuation of this reciprocal series to σ≤1 is asserted. ∎

## Lemma 2: conjugation preserves zeros and multiplicities

**Hypotheses.** s∈C, with equality interpreted meromorphically at the pole.

**Conclusion.** ζ(conj(s))=conj(ζ(s)). A zero at ρ gives a zero of the same multiplicity at conj(ρ).

**Proof.** For Re(s)>1, conjugate the absolutely convergent defining series term by term. The function g(s)=conj(ζ(conj(s))) is meromorphic: conjugate the coefficients of each local Laurent expansion. It agrees with ζ on Re(s)>1 and hence everywhere by the meromorphic identity theorem. Conjugating a local Taylor series preserves the index of its first nonzero coefficient, proving the multiplicity claim. ∎

## Lemma 3: reflection orbits in the open critical strip

**Hypotheses.** ζ(ρ)=0 and 0<Re(ρ)<1.

**Conclusion.** The points ρ, conj(ρ), 1-ρ, and 1-conj(ρ) are zeros with equal multiplicities. Some points may coincide.

**Proof.** On this strip the prefactor in the functional equation is holomorphic and nonzero. Indeed, the exponential never vanishes, Γ(1-s) is holomorphic and nonzero since Re(1-s)>0, and sin(πs/2) vanishes only at even integers, none of which lie in the strip. Thus the functional equation preserves zero order under s↦1-s. Apply Lemma 2 for the other images. ∎

## Lemma 4: a counterexample to the symmetry-only inference

**Hypotheses.** Let a=1/4+i and

P(s)=(s-a)(s-conj(a))(s-(1-a))(s-(1-conj(a))).

**Conclusion.** P is an entire polynomial with P(1-s)=P(s) and P(conj(s))=conj(P(s)). It is positive on the real axis and on the critical line, but all four of its zeros lie off the critical line, inside the open strip.

**Proof.** Conjugation permutes its roots and leaves the leading coefficient real. Reflection also permutes the roots, and the four negative signs cancel. The roots have real parts 1/4 or 3/4 and imaginary parts ±1. For real x,

P(x)=((x-1/4)²+1)((x-3/4)²+1)>0.

Writing u=s-1/2 and d=1/4 gives P(s)=u⁴+2(1-d²)u²+(1+d²)². Thus, for real t,

P(1/2+it)=(t²-(1-d²))²+4d²>0.

All claims follow directly. ∎

## Lemma 5: the Euler-product logarithm on its actual domain

**Hypotheses.** Re(s)>1. The index p runs over primes and k over positive integers.

**Conclusion.** L(s)=Σ_p Σ_{k≥1} p^{-ks}/k converges absolutely, locally uniformly on Re(s)>1, and exp(L(s))=ζ(s). Consequently Re L(s)=log|ζ(s)|. For real σ>1, L(σ)=log ζ(σ).

**Proof.** On Re(s)≥1+δ, δ>0, the absolute sum is at most

Σ_p p^{-(1+δ)}/(1-p^{-(1+δ)}) ≤ (1-2^{-(1+δ)})^{-1} Σ_{n≥2} n^{-(1+δ)} < ∞.

This is a uniform majorant. For a finite set of primes p≤X, the power-series identity exp(Σ_{k≥1} z^k/k)=(1-z)^{-1}, |z|<1, gives exp(L_X(s))=Π_{p≤X}(1-p^{-s})^{-1}. Expanding the finitely many absolutely convergent geometric series and applying unique factorization identifies this product with the sum of n^{-s} over integers all of whose prime factors are ≤X. The difference from ζ(s) has absolute value at most Σ_{n>X} n^{-Re(s)}, since any omitted integer has a prime factor >X and hence is >X. This tends to zero, uniformly on Re(s)≥1+δ. Taking the limit proves exp L=ζ. Taking absolute values gives exp(Re L)=|ζ| and thus the real-logarithm identity, with no choice of a complex logarithm required. For real σ the positive Dirichlet series makes the final identity immediate. ∎

## Lemma 6: a nonnegative trigonometric polynomial gives a product inequality

**Hypotheses.** σ>1 and t∈R.

**Conclusion.** ζ(σ)³|ζ(σ+it)|⁴|ζ(σ+2it)|≥1.

**Proof.** All quantities inside the real logarithms below are positive by Lemmas 1 and 5. Lemma 5 and absolute convergence give

3 log ζ(σ)+4 log|ζ(σ+it)|+log|ζ(σ+2it)|
=Σ_p Σ_{k≥1} p^{-kσ}[3+4cos(kt log p)+cos(2kt log p)]/k.

For every real θ, the bracket is 2(1+cos θ)²≥0. The sum is nonnegative, and exponentiating yields the claim. The equality is asserted only for σ>1. ∎

## Lemma 7: nonvanishing on Re(s)=1

**Hypotheses.** t∈R and t≠0.

**Conclusion.** ζ(1+it)≠0.

**Proof.** Suppose ζ has a zero of order m≥1 at 1+it. Such an order is finite: ζ is holomorphic there, is not identically zero by Lemma 1, and the identity theorem applies. Put h=σ-1>0. The simple pole at 1 gives |ζ(1+h)|≤C_0/h for sufficiently small h. The Taylor factorization at 1+it gives |ζ(1+h+it)|≤C_1 h^m. Since t≠0 implies 1+2it≠1, holomorphicity at 1+2it gives |ζ(1+h+2it)|≤C_2. Choose a common sufficiently small interval of h on which all three bounds hold. Lemma 6 then yields

1 ≤ ζ(1+h)³|ζ(1+h+it)|⁴|ζ(1+h+2it)| ≤ C_0³C_1⁴C_2 h^{4m-3}.

The right side tends to zero, since 4m-3≥1, a contradiction. No boundary limit of the prime sum was taken: only the already-proved inequality for h>0 and finite local Taylor/Laurent estimates were used. ∎

## Lemma 8: residue at 1 and the value at 0

**Hypotheses.** ζ is the meromorphic continuation specified above; the pole at 1 is simple.

**Conclusion.** Res_{s=1} ζ(s)=1 and ζ(0)=-1/2.

**Proof.** For real h>0, the integral comparison for the decreasing function x^{-1-h} gives

1/h = ∫_1^∞ x^{-1-h} dx ≤ ζ(1+h) ≤ 1+∫_1^∞ x^{-1-h} dx = 1+1/h.

Thus hζ(1+h) tends to 1. By the assumed simple Laurent pole, this limit is its residue, so ζ(1-s)=-1/s+O(1) near s=0. In the functional equation, 2(2π)^{s-1}=1/π+O(s), sin(πs/2)=πs/2+O(s³), and Γ(1-s)=1+O(s), using Γ(1)=1 and its holomorphicity there. Multiplication gives ζ(s)=-1/2+O(s). Meromorphic continuation is holomorphic at 0, so ζ(0)=-1/2. ∎

## Lemma 9: complete classification outside the open strip

**Hypotheses.** s is outside 0<Re(s)<1, and s≠1 (the pole).

**Conclusion.** ζ(s)=0 if and only if s=-2n for a positive integer n. Each such zero is simple.

**Proof.** Lemmas 1 and 7 exclude zeros for Re(s)≥1. For Re(s)<0, the factor ζ(1-s) is holomorphic and nonzero by Lemma 1; Γ(1-s) is holomorphic and nonzero because Re(1-s)>1. The exponential prefactor is also holomorphic and nonzero. Thus the functional equation says that a zero occurs exactly when sin(πs/2)=0, namely at the negative even integers in this region. These zeros are simple: the sine derivative there is (π/2)cos(-nπ)≠0 and all other factors are nonzero. If Re(s)=0 and s=it with real t≠0, Lemma 7 makes ζ(1-it) nonzero, while the other factors are again holomorphic and nonzero. Finally s=0 is nonzero by Lemma 8. ∎

## Lemma 10: the positive prime-logarithm representation diverges at and left of 1

**Hypotheses.** 0<σ≤1 is real.

**Conclusion.** Σ_p1/p=∞, and Σ_pΣ_{k≥1}p^{-kσ}/k=∞. For complex s with 0<Re(s)≤1, the corresponding double series is not absolutely convergent.

**Proof.** Suppose Σ_p1/p were finite. For each prime p,

Σ_{k≥1}p^{-k}/k ≤ 1/(p-1) ≤ 2/p.

Hence the finite products Π_{p≤X}(1-1/p)^{-1} would be bounded independently of X by exp(2Σ_p1/p). Expanding each finite product as convergent geometric series shows it is at least Σ_{1≤n≤X}1/n: every such integer has all its prime factors ≤X. The harmonic sums are unbounded (by integral comparison), a contradiction. For 0<σ≤1 the k=1 terms satisfy p^{-σ}≥1/p, proving divergence of the nonnegative double sum. Absolute values of p^{-ks}/k equal p^{-k Re(s)}/k, proving the complex assertion. This makes no claim about conditional convergence at individual nonreal points. ∎

## Lemma 11: the continued product inequality is false

**Hypotheses.** Define F(σ,t)=|ζ(σ)|³|ζ(σ+it)|⁴|ζ(σ+2it)| for real σ,t sufficiently close to 0.

**Conclusion.** There is ε>0 such that F(σ,t)<1 whenever |σ|<ε and |t|<ε. In particular the absolute-value version of Lemma 6 fails at points with 0<σ<1 and t≠0. The original version with ζ(σ)³ also fails there for sufficiently small σ,t.

**Proof.** ζ is holomorphic near 0. Thus F is continuous near (0,0), and by Lemma 8, F(0,0)=(1/2)^8=1/256<1. Continuity gives the claimed neighborhood, which can be shrunk to ε<1. Also ζ(σ) is real for real σ by Lemma 2 and is negative near 0 since ζ(0)=-1/2. Replacing |ζ(σ)|³ by ζ(σ)³ therefore makes the original product nonpositive there, so it cannot be ≥1. ∎

## Lemma 12: a convergent alternating representation in Re(s)>0

**Hypotheses.** Re(s)>0. Set η_N(s)=Σ_{n=1}^N(-1)^{n-1}n^{-s}.

**Conclusion.** η_N converges locally uniformly to a holomorphic function η on Re(s)>0. On this half-plane η(s)=(1-2^{1-s})ζ(s), interpreted with a removable singularity at s=1.

**Proof.** Fix a compact subset with Re(s)≥δ>0 and |s|≤R. For M≥N, put a_n=(-1)^{n-1} and A_n=Σ_{k=N}^n a_k, so |A_n|≤1. Summation by parts gives

Σ_{n=N}^M a_n n^{-s}=A_M M^{-s}+Σ_{n=N}^{M-1}A_n(n^{-s}-(n+1)^{-s}).

By integrating the derivative of x^{-s} on [n,n+1], the absolute value is at most

M^{-δ}+R∫_N^M x^{-δ-1}dx ≤ (1+R/δ)N^{-δ}.

This uniform Cauchy bound proves local uniform convergence; the Weierstrass theorem on locally uniform limits of holomorphic functions gives holomorphicity. On Re(s)>1, absolute convergence permits separating the even terms and gives η(s)=ζ(s)-2·2^{-s}ζ(s). The multiplier q(s)=1-2^{1-s} vanishes at 1, with q'(1)=log 2. Lemma 8 shows that q(s)ζ(s) has removable value log 2 at 1 and is holomorphic throughout Re(s)>0 after filling it in. The identity theorem on that connected half-plane proves the identity everywhere there. No division at a zero of q is used. ∎

## Lemma 13: no real zeros in the open strip

**Hypotheses.** σ is real and 0<σ<1.

**Conclusion.** η(σ)>0 and ζ(σ)<0. In particular every nontrivial zero of ζ has nonzero imaginary part.

**Proof.** The even partial sums are

η_{2N}(σ)=Σ_{n=1}^N[(2n-1)^{-σ}-(2n)^{-σ}].

Every summand is positive, and the first is 1-2^{-σ}>0. Lemma 12 gives convergence, hence η(σ)≥1-2^{-σ}>0. Since 2^{1-σ}>1, the multiplier 1-2^{1-σ} is negative, so the identity in Lemma 12 gives ζ(σ)<0. Lemma 9 excludes all remaining nontrivial zeros outside the open strip. ∎

## Lemma 14: a positive-kernel Laplace representation

**Hypotheses.** Re(s)=σ>0. Let w(x) be 1 on the union of [2n-1,2n), n≥1, and 0 elsewhere on [1,∞).

**Conclusion.**

η(s)/s=∫_1^∞ w(x)x^{-s-1}dx=∫_0^∞w(e^u)e^{-su}du.

Both integrals converge absolutely and locally uniformly on Re(s)>0.

**Proof.** On each interval [2n-1,2n], integrating the derivative of x^{-s} gives

(2n-1)^{-s}-(2n)^{-s}=s∫_{2n-1}^{2n}x^{-s-1}dx.

Summing through n=N gives η_{2N}(s) on the left. On the right, absolute integrability follows from 0≤w≤1 and ∫_1^∞x^{-σ-1}dx=1/σ; the omitted integral is bounded by (2N+1)^{-σ}/σ. Pass to the limit using Lemma 12 and divide by s≠0. The substitution x=e^u proves the second identity. For Re(s)≥δ>0 the absolute tails are bounded by the corresponding tails of x^{-δ-1} or e^{-δu}; these bounds also give local uniform convergence. ∎

## Lemma 15: a nonnegative indicator kernel can have zeros inside the strip

**Hypotheses.** v(u) is the indicator of [0,1]∪[2,4], and H(s)=∫_0^∞v(u)e^{-su}du.

**Conclusion.** H is entire, is positive for every real s, and has a nonreal zero s with 0<Re(s)<(log 2)/2<1.

**Proof.** The compact support makes the integral entire (differentiate under the integral, bounded on every compact set), and its integrand is positive for real s on a set of positive measure. For s≠0, direct integration gives

H(s)=(1-e^{-s})(1+e^{-2s}+e^{-3s})/s.

Consider Q(z)=1+z²+z³. Its derivative is z(2+3z). Q(-2)=-3 and Q(-1)=1. Its stationary values are Q(-2/3)=31/27 and Q(0)=1. The derivative signs show that Q has exactly one real root r, lying in (-2,-1). By the fundamental theorem of algebra and real coefficients, the remaining roots z and conj(z) are nonreal. Vieta's formula gives r|z|²=-1, so 1/2<|z|²<1. Choose any complex logarithm of this individual nonzero number z and set s=-Log z. Then e^{-s}=z and

0<Re(s)=-log|z|=(log(-r))/2<(log 2)/2<1.

This s is nonreal and nonzero because z is nonreal. The displayed factorization gives H(s)=0. The elementary bound log 2<1 follows from ∫_1^2 dx/x<1. No numerical root estimates are used. ∎

## Lemma 16: theta transformation and exponential tails

**Hypotheses.** x>0 is real. Define θ(x)=Σ_{n∈Z}e^{-πn²x} and ψ(x)=Σ_{n≥1}e^{-πn²x}, so θ=1+2ψ.

**Conclusion.** θ(x)=x^{-1/2}θ(1/x). For x≥1 and each integer j≥0 there is a finite constant C_j such that |ψ^{(j)}(x)|≤C_j e^{-πx}.

**Proof.** Use the standard named Poisson summation theorem for Schwartz functions with Fourier transform f̂(y)=∫_R f(u)e^{-2πiuy}du. The Gaussian f_x(u)=e^{-πxu²} is Schwartz. Its Fourier transform is x^{-1/2}e^{-πy²/x}: the Gaussian integral gives f̂_x(0)=x^{-1/2}, while differentiation under the integral and integration by parts give f̂_x'(y)=-(2πy/x)f̂_x(y), which determines the transform. Both operations are justified by Gaussian integrability of polynomials times f_x. Poisson summation Σ_n f_x(n)=Σ_n f̂_x(n) proves the transformation; both sums converge absolutely.

For the tail estimate, termwise j-fold differentiation gives ψ^{(j)}(x)=Σ_{n≥1}(-πn²)^j e^{-πn²x}. On x≥1 its absolute sum is at most

e^{-πx} Σ_{n≥1}(πn²)^j e^{-π(n²-1)} = C_j e^{-πx}.

The constant is finite since exponential decay dominates every fixed polynomial. These bounds and the Weierstrass uniform convergence test also justify each termwise derivative (or apply the same bounds successively on compact x-intervals in (0,∞)). ∎

## Lemma 17: split Mellin integral with entire remainder

**Hypotheses.** ψ is as in Lemma 16. For s∈C put

I(s)=∫_1^∞ψ(x)(x^{s/2}+x^{(1-s)/2})dx/x,

where all powers use the real logarithm of x.

**Conclusion.** I is entire, I(s)=I(1-s), and for Re(s)>1,

π^{-s/2}Γ(s/2)ζ(s)=1/(s-1)-1/s+I(s).

**Proof.** For σ=Re(s)>1, the integral of the absolute values of the summands in ∫_0^∞Σ_{n≥1}e^{-πn²x}x^{s/2-1}dx is

Σ_{n≥1}∫_0^∞e^{-πn²x}x^{σ/2-1}dx=π^{-σ/2}Γ(σ/2)Σ_{n≥1}n^{-σ}<∞.

Thus Fubini's theorem permits termwise integration. The substitution u=πn²x and Euler's gamma integral give the left side in the conclusion. Split the x-integral at 1. Lemma 16 gives ψ(x)=(x^{-1/2}-1)/2+x^{-1/2}ψ(1/x) for 0<x<1. The elementary part integrates, for σ>1, to 1/(s-1)-1/s. Substituting y=1/x in the remaining part yields ∫_1^∞ψ(y)y^{(1-s)/2}dy/y, completing the identity.

On a compact set of s, both Re(s)/2 and (1-Re(s))/2 are bounded above by some finite A. Lemma 16 bounds the integrand in absolute value by 2C_0e^{-πx}x^{A-1}. Its k-th complex s derivative has the same bound times (log x/2)^k, also integrable for each fixed k. Dominated differentiation proves that I is entire. Reflection just interchanges its two summands, proving I(s)=I(1-s). ∎

## Lemma 18: entire completion and exact zero correspondence

**Hypotheses.** I is as in Lemma 17. Define ξ(s)=1/2+s(s-1)I(s)/2 and Ξ(z)=ξ(1/2+iz).

**Conclusion.** ξ is entire, ξ(1-s)=ξ(s), ξ(conj(s))=conj(ξ(s)), and ξ(0)=ξ(1)=1/2. On Re(s)>0, away from s=1,

ξ(s)=s(s-1)π^{-s/2}Γ(s/2)ζ(s)/2.

The zeros of ξ are exactly the nontrivial zeros of ζ, with the same multiplicities. Ξ is entire, even, and real on the real axis. RH is exactly the still-unproved assertion that all zeros of Ξ are real.

**Proof.** Entirety and reflection follow from Lemma 17 and s(s-1)=(1-s)((1-s)-1); endpoint values follow by substitution. Since ψ is real, conjugating the absolutely convergent integral shows I(conj(s))=conj(I(s)), and then the same holds for ξ. Multiply the identity of Lemma 17 by s(s-1)/2; the rational terms give exactly 1/2. This proves the product expression for Re(s)>1. Its right side is holomorphic on Re(s)>0 after removing the singularity at 1: Γ(s/2) is holomorphic there and (s-1) cancels the only ζ pole. The identity theorem gives the asserted extension.

In the open strip every prefactor in this expression is holomorphic and nonzero, so zero multiplicities agree. For Re(s)≥1 away from 1 the expression and Lemmas 1 and 7 make ξ nonzero; at 1 its value is 1/2. For Re(s)≤0 reflect to Re(1-s)≥1. Thus ξ has no zeros outside the open strip. By Lemma 9 this proves the exact zero correspondence. Composition makes Ξ entire, and reflection gives Ξ(-z)=Ξ(z). Moreover conjugation gives conj(Ξ(z))=Ξ(-conj(z))=Ξ(conj(z)), hence reality on R. Finally if s=β+iγ, its corresponding variable is z=(s-1/2)/i=γ+i(1/2-β), real exactly when β=1/2. The change of variable has nonzero derivative and preserves multiplicity. ∎

## Lemma 19: the theta boundary derivative and a positive kernel

**Hypotheses.** u≥0, A(u)=e^{u/2}ψ(e^{2u}), and K(u)=2A''(u)-A(u)/2.

**Conclusion.** A'(0)=-1/4, and

K(u)=Σ_{n≥1}[8π²n⁴e^{9u/2}-12πn²e^{5u/2}]e^{-πn²e^{2u}}>0.

A, A', A'', and K decay faster than e^{-Bu} for every fixed B>0 as u tends to infinity.

**Proof.** Differentiate θ(x)=x^{-1/2}θ(1/x) at x=1, justified by Lemma 16. This gives 2θ'(1)=-θ(1)/2, hence ψ'(1)=-(1+2ψ(1))/8. Therefore A'(0)=ψ(1)/2+2ψ'(1)=-1/4.

Put x=e^{2u}. Differentiating gives

A''(u)=e^{u/2}[ψ(x)/4+6xψ'(x)+4x²ψ''(x)],

so K(u)=e^{u/2}[12xψ'(x)+8x²ψ''(x)]. The differentiated series in Lemma 16 gives the displayed formula. Each summand equals 4v(2v-3)e^{u/2}e^{-v} with v=πn²e^{2u}≥π>3/2, so every summand is positive. The elementary bound π>3/2 is sufficient. Lemma 16 bounds |A|, |A'|, |A''|, and |K| by C e^{9u/2}e^{-πe^{2u}} on u≥0, with a suitable finite C. For any fixed B this bound times e^{Bu} tends to zero and is integrable: e^{2u} eventually dominates any linear multiple of u. ∎

## Lemma 20: entire Fourier cosine representation of Ξ

**Hypotheses.** z∈C and K is as in Lemma 19.

**Conclusion.** Ξ(z)=∫_0^∞K(u)cos(zu)du. This integral and its derivatives of every fixed order converge locally uniformly in z.

**Proof.** In I(1/2+iz), put x=e^{2u}; Lemma 17 gives I(1/2+iz)=4J(z), where J(z)=∫_0^∞A(u)cos(zu)du. Consequently Lemma 18 yields

Ξ(z)=1/2-2(z²+1/4)J(z).

For z in a compact set |z|≤R, |cos(zu)| and |sin(zu)| are at most e^{Ru}. Lemma 19 makes A, A', A'', and K times this bound integrable and makes all boundary terms at infinity vanish. The same holds after multiplying by any fixed power of u, so dominated differentiation proves local uniform convergence of every derivative.

Integrating twice by parts gives

∫_0^∞A''(u)cos(zu)du=-A'(0)+z∫_0^∞A'(u)sin(zu)du=-A'(0)-z²J(z).

At u=0 the first boundary term is -A'(0), while the second is zero because sin 0=0. It follows that

∫_0^∞K(u)cos(zu)du=-2A'(0)-2(z²+1/4)J(z)=Ξ(z),

using A'(0)=-1/4. All steps hold directly for complex z; no unsupported contour movement or extension of a real inequality occurs. ∎

## Lemma 21: imaginary-axis positivity and moment coefficients

**Hypotheses.** K is the kernel in Lemma 19. Define M_{2n}=∫_0^∞u^{2n}K(u)du for integers n≥0.

**Conclusion.** Every M_{2n} is finite and strictly positive,

Ξ(z)=Σ_{n≥0}(-1)^n M_{2n}z^{2n}/(2n)!,

with convergence on C, and Ξ(iy)>0 for every real y. Also M_{2n+2}²≤M_{2n}M_{2n+4} for every integer n≥0.

**Proof.** Finiteness follows from Lemma 19, and positivity follows because K(u)>0 on u>0. On |z|≤R, the sum of the absolute values of the cosine-series terms is at most cosh(Ru)≤e^{Ru}. The integrable majorant K(u)e^{Ru} permits exchanging the series and integral in Lemma 20 by dominated convergence (or absolute Fubini). Substitution z=iy gives Ξ(iy)=∫_0^∞K(u)cosh(yu)du>0. Finally apply Cauchy–Schwarz in the measure K(u)du to u^n and u^{n+2}. Their scalar product is M_{2n+2} and their squared norms are M_{2n} and M_{2n+4}. ∎

## Lemma 22: positive smooth superexponential kernels do not force real zeros

**Hypotheses.** On R let g(u)=exp(-cosh(2u)), h(u)=2g(u)+(g(u-4)+g(u+4))/2, and F(z)=∫_R h(u)e^{izu}du.

**Conclusion.** h is smooth, strictly positive, and even. It decays at least as fast as C exp(-c e^{2|u|}) for some C,c>0. F is entire and even, has positive imaginary-axis values and alternating even Taylor coefficients from positive moments, but has a zero z_0 with 0<Im(z_0)<1/2.

**Proof.** Positivity and smoothness are immediate, and evenness follows from that of g and the paired shifts. Since cosh(2v)≥e^{2|v|}/2 and |u±4|≥|u|-4, each shifted term is bounded by exp(-e^{-8}e^{2|u|}/2); one may take C=3 and c=e^{-8}/2. This majorant times e^{R|u|}|u|^k is integrable for every fixed R,k, so F is entire by dominated differentiation. The same is true for G(z)=∫_R g(u)e^{izu}du.

Real substitutions in absolutely convergent integrals give

F(z)=[2+(e^{4iz}+e^{-4iz})/2]G(z)=(2+cos(4z))G(z).

Let b=log(2+√3)>0. Since (2+√3)^{-1}=2-√3, cosh b=2. Also cosh 2>1+2=3>2 by its power series, so b<2 by strict monotonicity of cosh on (0,∞). Put z_0=(π+ib)/4. Then cos(4z_0)=cos(π+ib)=-cosh b=-2, so F(z_0)=0, and 0<Im(z_0)=b/4<1/2.

Evenness of h gives F(z)=2∫_0^∞h(u)cos(zu)du. The same dominated-series and cosh arguments as in Lemma 21 give the stated moment signs and positive imaginary-axis values. F is not identically zero because F(0)>0. This is a counterexample to the listed sufficient-condition guesses, not to RH or to a theorem using further arithmetic properties of K. ∎

## Lemma 23: an unconditional entire growth bound

**Hypotheses.** Ξ is defined in Lemma 18 and R≥1. Write B(R)=max_{|z|≤R}|Ξ(z)|.

**Conclusion.** log B(R)≤C+(R/2+4)log(R/2+4) for a fixed real constant C. In particular Ξ has entire order at most 1, meaning limsup_{R→∞} log log(max(e,B(R)))/log R≤1.

**Proof.** Lemmas 19–20 give, for a fixed C_1>0,

B(R)≤C_1∫_0^∞exp((R+9/2)u-πe^{2u})du
=(C_1/2)∫_1^∞x^{a-1}e^{-πx}dx,

where a=(R+9/2)/2. Put m=ceil(a). For x≥1, x^{a-1}≤x^m and e^{-πx}≤e^{-x}, so the last expression is at most (C_1/2)Γ(m+1)=(C_1/2)m!. The gamma recurrence, obtained by integration by parts in Euler's integral, gives Γ(m+1)=m!. Since m!≤m^m and m≤R/2+13/4<R/2+4, the asserted logarithmic bound follows after enlarging the constant. The displayed order bound follows by taking two logarithms and dividing by log R. No zero-location information was used. ∎

## Lemma 24: an unconditional paired Hadamard product

**Hypotheses.** Ξ is as above. Select one representative α_j from each pair {α,-α} of its zeros, repeating according to multiplicity.

**Conclusion.** No α_j is zero, Σ_j|α_j|^{-2}<∞, and

Ξ(z)=M_0 Π_j(1-z²/α_j²),

locally uniformly on C. The factors may involve nonreal α_j; their reality has not been assumed.

**Proof.** Use the standard named Hadamard factorization theorem in its order-at-most-one form: if f is entire of order at most 1 and f(0)≠0, its nonzero zeros ρ, with multiplicity, satisfy Σ_ρ|ρ|^{-2}<∞ and

f(z)=f(0)exp(bz)Π_ρ[(1-z/ρ)exp(z/ρ)], with b=f'(0)/f(0).

The product converges locally uniformly. A precise supporting reference is [Hadamard factorization, Theorem 7.7 in the UCL introductory analytic number theory notes](https://www.homepages.ucl.ac.uk/~ucahpet/IANTnotes2018.pdf); the named theorem is the input here.

For Ξ, Lemma 23 proves the order hypothesis, Lemma 21 gives Ξ(0)=M_0>0, and evenness gives Ξ'(0)=0. Thus b=0. The zero set is invariant under α↦-α with equal multiplicities by evenness and local Taylor series. Since 0 is not a zero, all these pairs have two distinct elements. For |z/ρ|≤1/2, the logarithm of (1-z/ρ)exp(z/ρ) is bounded in modulus by a constant times |z/ρ|², from its power series. The reciprocal-square summability therefore permits reordering the product and grouping into ± pairs on every compact set; finitely many nearby zeros cause no issue. Each pair becomes (1-z/α)(1+z/α)=1-z²/α². This also proves local uniform convergence of the paired product and the asserted square summability for the representatives. ∎

## Lemma 25: moment coefficients and reciprocal-zero power sums

**Hypotheses.** α_j are the representatives in Lemma 24, and M_{2n} are as in Lemma 21. Define S_k=Σ_jα_j^{-2k} for integers k≥1.

**Conclusion.** All S_k converge absolutely and are real. In particular

S_1=M_2/(2M_0),

S_2=(3M_2²-M_0M_4)/(12M_0²).

If RH holds, then S_k≥0 for every k≥1, so M_0M_4≤3M_2² is a necessary consequence of RH. No sufficiency is claimed.

**Proof.** Because Ξ(0)≠0 and its zeros are isolated, there is a zero-free disk around 0; hence |α_j| have a positive lower bound. Lemma 24 then gives absolute summability of every even reciprocal power. For |z| smaller than half that lower bound, expand the paired logarithms. The sum of the absolute values of the full double series is bounded by a constant times |z|²Σ|α_j|^{-2}, so

log(Ξ(z)/M_0)=-Σ_{k≥1}S_k z^{2k}/k,

using the local analytic logarithm that is zero at 0. Conjugation symmetry makes the left side's Taylor coefficients real, proving S_k real. The moment expansion gives Ξ(z)/M_0=1-a z²+b z⁴+O(z⁶), where a=M_2/(2M_0) and b=M_4/(24M_0). Its logarithm is -a z²+(b-a²/2)z⁴+O(z⁶). Comparing coefficients proves the formulas. Under RH every α_j is real and nonzero by Lemma 18, so every term of each S_k is positive. The asserted nonnegative sign and the necessary moment inequality follow conditionally.

The unconditional Cauchy–Schwarz inequality in Lemma 21 gives M_2²≤M_0M_4, which is a lower bound and does not give the needed upper bound M_0M_4≤3M_2². ∎

## Lemma 26: an elementary zero-free rectangle for Ξ

**Hypotheses.** z=x+iy with real x,y and |y|≤1/2. J(z) is as in Lemma 20.

**Conclusion.** |J(z)|<1/72. If also |x|≤4, then Ξ(z)≠0. Consequently every Ξ zero α satisfies |Re(α)|>4 and |Im(α)|<1/2.

**Proof.** For X≥1, n²≥n implies

ψ(X)≤Σ_{n≥1}e^{-πnX}=e^{-πX}/(1-e^{-πX})≤e^{-πX}/(1-e^{-π}).

Since |cos(zu)|≤e^{|y|u}≤e^{u/2}, the substitution X=e^{2u} gives

|J(z)|≤∫_0^∞e^uψ(e^{2u})du=(1/2)∫_1^∞X^{-1/2}ψ(X)dX
≤1/[2π(e^π-1)].

Use the elementary bounds π>3 and e³>1+3+9/2+27/6=13, so 2π(e^π-1)>72, proving the strict estimate. If |x|≤4, then |z²+1/4|≤|z|²+1/4≤16+1/4+1/4=33/2. Lemma 20 gives

|Ξ(z)-1/2|=2|z²+1/4||J(z)|<33/72=11/24<1/2.

Thus Ξ(z) cannot vanish in that rectangle. Lemma 18 and strip localization put every Ξ zero in |Im(α)|<1/2; applying the rectangle result proves the final assertion. ∎

## Lemma 27: six positive reciprocal-power sums and a strict moment inequality

**Hypotheses.** S_k and M_{2n} are as in Lemma 25.

**Conclusion.** Ξ has infinitely many zeros. S_k>0 for 1≤k≤6, and

M_2² < M_0M_4 < 3M_2².

These are unconditional finite tests, not RH.

**Proof.** By Lemma 21 every even Taylor coefficient of Ξ is nonzero, so Ξ is not a polynomial. If it had only finitely many zeros, Lemma 24 would make it a finite polynomial product, a contradiction. Thus there are infinitely many α_j. By Lemma 26 none is on the imaginary axis, so choose the representative of each ± pair with positive real part. It obeys Re(α_j)>4 and |Im(α_j)|<1/2. Its principal argument θ_j therefore satisfies

|θ_j|=arctan(|Im(α_j)|/Re(α_j))<1/8,

using arctan v≤v for v≥0, which follows by integrating 1/(1+v²)≤1. For 1≤k≤6, |2kθ_j|<k/4≤3/2<π/2. Hence Re(α_j^{-2k})=|α_j|^{-2k}cos(2kθ_j)>0. Absolute convergence and reality from Lemma 25 permit taking real parts term by term, proving S_k>0. The formula for S_2 gives M_0M_4<3M_2². The lower inequality is strict Cauchy–Schwarz for 1 and u² in K(u)du: equality would require u² to be constant almost everywhere for this measure, impossible since K is strictly positive on every interval in (0,∞). ∎

## Lemma 28: a degree-two Jensen polynomial is real-rooted

**Hypotheses.** Define γ_n=n!M_{2n}/(2n)! for n≥0 and J_2(X)=γ_0+2γ_1X+γ_2X². This definition is the degree-two Jensen polynomial of the entire series Σ_nγ_n X^n/n!=Σ_nM_{2n}X^n/(2n)!.

**Conclusion.** J_2 has two distinct negative real roots.

**Proof.** γ_0=M_0>0, γ_1=M_2/2>0, and γ_2=M_4/12>0. Its discriminant is

(2γ_1)²-4γ_0γ_2=M_2²-M_0M_4/3>0

by Lemma 27. Thus both roots are real and distinct. Their sum is -2γ_1/γ_2<0 and their product γ_0/γ_2>0, so both are negative. No assertion about any higher degree or shifted Jensen polynomial is made. ∎

## Lemma 29: even all positive scalar power sums do not force real zeros

**Hypotheses.** Let a=10+i/4 and

P(z)=(1-z²/25)(1-z²/a²)(1-z²/conj(a)²),  F(z)=P(z)cos(z/100).

For a nonzero even entire function, a paired reciprocal-power sum means one term α^{-2k} per ± zero pair, with multiplicity.

**Conclusion.** P and F are even and real on R. Both have nonreal zeros, all their zeros satisfy |Re(z)|>4 and |Im(z)|<1/2, and all their paired reciprocal-power sums are strictly positive. F has infinitely many zeros, has order at most 1, has alternating strictly nonzero even Taylor coefficients, and is positive on the imaginary axis.

**Proof.** Put b=1/25 and c=a^{-2}. Then Re(c)>0 since Re(a)²>Im(a)², and |c|=1/(100+1/16)<b/4. The paired sums for P are

T_k=b^k+c^k+conj(c)^k ≥ b^k-2|c|^k > b^k[1-2(1/4)^k]>0.

Its roots are ±5, ±a, and ±conj(a), giving the claimed locations. Its coefficients are 1,-e_1,e_2,-e_3 with

e_1=b+2Re(c)>0, e_2=2b Re(c)+|c|²>0, e_3=b|c|²>0.

Also P(iy)=(1+y²/25)|1+y²/a²|²>0 for real y: the second factor cannot vanish because a² is nonreal. The additional zeros of cos(z/100) are exactly z=100π(n+1/2), n∈Z, all real with absolute value ≥50π>4. Their paired reciprocal-power sums converge and are positive for every k≥1 by comparison with Σ_{n≥0}(n+1/2)^{-2k}. Thus adding them preserves strict positivity of all T_k. Multiplicities, if any roots coincided, would simply add; here the listed sets are disjoint.

Multiplying P's alternating coefficients by the alternating cosine series shows that every even coefficient of F has sign (-1)^n and nonzero magnitude: its coefficient after removing this sign is a sum of positive terms, including the constant-coefficient contribution from P. Moreover F(iy)=P(iy)cosh(y/100)>0. Finally |F(z)|≤C(1+|z|)^6e^{|z|/100}, proving order at most 1. This example does not assert a positive Fourier-kernel representation for F. ∎

## Lemma 30: convergent mixed quadratic forms

**Hypotheses.** β_j=α_j^{-2} as in Lemma 24 and q(X)=Σ_{m=0}^d c_mX^m has real coefficients. Define Q(q)=Σ_jβ_j²q(β_j)²; the square here is algebraic, not absolute-value squared.

**Conclusion.** Q(q) converges absolutely, is real, and

Q(q)=Σ_{m,n=0}^d c_mc_n S_{m+n+2}.

If RH holds, Q(q)≥0 for every real polynomial q. Thus RH implies positive semidefiniteness of every real Hankel matrix H_d=(S_{m+n+2})_{0≤m,n≤d}.

**Proof.** Lemma 24 gives Σ_j|β_j|<∞, hence the β_j are bounded and Σ_j|β_j|²<∞. Any fixed polynomial is bounded on a closed disk containing them, so Σ_j|β_j²q(β_j)²|<∞. Expand the finite polynomial square and interchange only a finite sum with this absolutely convergent series to obtain the identity. The S_k are real by Lemma 25, so Q(q) is real. Under RH all α_j are real and nonzero, hence β_j>0 and every β_j²q(β_j)² is nonnegative. The matrix assertion is precisely the definition of positive semidefiniteness, since cᵀH_dc=Q(q). Without RH, replacing q(β_j)² by |q(β_j)|² would change the expression and would not prove the stated sign. ∎

## Lemma 31: a mixed test detects the finite counterexample

**Hypotheses.** b=1/25, c=(10+i/4)^{-2}, and T_k=b^k+c^k+conj(c)^k, as in Lemma 29.

**Conclusion.** There is a real polynomial q of degree at most two such that

b²q(b)²+c²q(c)²+conj(c)²q(conj(c))²=-2.

Thus the 3-by-3 Hankel matrix (T_{m+n+2})_{0≤m,n≤2} is not positive semidefinite, although all T_k>0.

**Proof.** The three nodes b,c,conj(c) are distinct because b is real and c is nonreal. Define

L_c(X)=(X-b)(X-conj(c))/[(c-b)(c-conj(c))],

L_conj(c)(X)=(X-b)(X-c)/[(conj(c)-b)(conj(c)-c)],

q(X)=(i/c)L_c(X)-(i/conj(c))L_conj(c)(X).

The two Lagrange basis polynomials have conjugate coefficients, and the two scalar coefficients are conjugates, so q has real coefficients. Its values are q(b)=0, q(c)=i/c, and q(conj(c))=-i/conj(c). Substitution makes the three terms 0,-1,-1. The Hankel identity is the finite version of Lemma 30, proving the matrix claim. ∎

## Lemma 32: polynomial detection of a nonreal summable node

**Hypotheses.** (β_j) is a finite or countable sequence of nonzero complex numbers, invariant under conjugation including multiplicity, with Σ_j|β_j|<∞. Suppose a nonreal node w occurs.

**Conclusion.** There is a polynomial q with real coefficients for which Σ_jβ_j²q(β_j)²<0. Consequently all these real polynomial forms are nonnegative if and only if all nodes β_j are real.

**Proof.** Put r=|w|/2 and let E be the finite set of distinct nodes of modulus at least r. Finiteness follows from summability; conjugation invariance makes E conjugation-invariant. Both w and conj(w) belong to E and have the same finite multiplicity μ≥1. For v∈E let

L_v(X)=Π_{a∈E, a≠v}(X-a)/(v-a).

Then L_v(a) is 1 at a=v and 0 at the other nodes in E. The coefficients of L_conj(w) are conjugates of those of L_w. For each integer N≥1 define

q_N(X)=(i/w)(X/w)^N L_w(X) -(i/conj(w))(X/conj(w))^N L_conj(w)(X).

Its coefficients are real. It equals i/w at w, -i/conj(w) at conj(w), and 0 at every other node in E. Thus the contribution to the form from nodes in E, with multiplicity, is -2μ.

On |X|≤r, the fixed polynomials L_w and L_conj(w) are bounded. Therefore there is C independent of N such that |q_N(X)|≤C(r/|w|)^N=C2^{-N}. The remaining nodes have modulus <r and satisfy Σ|β_j|²<∞ (boundedness plus the original summability). The absolute value of their total contribution is at most C²4^{-N}Σ_{|β_j|<r}|β_j|², tending to zero. The whole form is real by conjugation and absolute convergence. For sufficiently large N it is negative. Conversely, if all β_j are real, each β_j²q(β_j)² is nonnegative, proving the final equivalence. ∎

## Corollary 32a: an explicit RH-equivalent condition, not a proof of it

For the actual Ξ nodes β_j=α_j^{-2}, RH holds if and only if every finite Hankel matrix H_d=(S_{m+n+2})_{0≤m,n≤d} is positive semidefinite.

**Proof.** The node summability is Lemma 24, and conjugation invariance follows from Lemma 18 (squaring reciprocals makes the ± representative choice irrelevant). Lemmas 30 and 32 identify matrix positivity with all β_j being real. A real β_j could be negative only if α_j were purely imaginary: writing α=x+iy, real α² forces xy=0, and negative α² forces x=0. Lemma 26 excludes such α_j. Thus all β_j real here means all α_j real, which is RH by Lemma 18. The forward implication is already Lemma 30. ∎

**Unresolved requirement.** No argument in this write-up proves H_d positive semidefinite for every d. Corollary 32a is openly RH-equivalent and cannot be used as an unconditional positivity input. Lemma 27 proves only the scalar cases S_2,S_4,S_6>0 among its diagonal entries, not the mixed forms.

## Lemma 33: the first mixed determinant in moment coordinates

**Hypotheses.** Put a=M_2/(2M_0), b=M_4/(24M_0), c=M_6/(720M_0), d=M_8/(40320M_0), all positive. The symbols here are normalized moment coefficients, not the counterexample nodes of Lemmas 29–31.

**Conclusion.**

S_3=a³-3ab+3c,

S_4=a⁴-4a²b+2b²+4ac-4d,

D:=det H_1=S_2S_4-S_3²
=a²b²-4b³-2a³c+10abc-9c²-4a²d+8bd.

For the actual Ξ, H_1 is positive semidefinite exactly when D≥0, since S_2>0 is already proved. The sign of D is not established by this lemma.

**Proof.** Set t=z². By Lemma 21, Ξ(z)/M_0=1-at+bt²-ct³+dt⁴+O(t⁵). Expand the local logarithm at t=0, justified on the zero-free disk used in Lemma 25:

log(Ξ(z)/M_0)=-at+(b-a²/2)t²+(-c+ab-a³/3)t³
+(d-ac-b²/2+a²b-a⁴/4)t⁴+O(t⁵).

Comparing with -Σ_{k≥1}S_k t^k/k gives the two new identities and S_2=a²-2b. Expanding (a²-2b)(a⁴-4a²b+2b²+4ac-4d)-(a³-3ab+3c)² gives the displayed expression for D. Finally, for real x,y,

S_2x²+2S_3xy+S_4y²=S_2(x+S_3y/S_2)²+(D/S_2)y².

Lemma 27 gives S_2>0, so this form is nonnegative for all x,y exactly when D≥0. ∎

## Lemma 34: small zero arguments do not ensure a mixed determinant sign

**Hypotheses.** α=10+i/4, c=α^{-2}, and T_k=c^k+conj(c)^k for integers k≥1.

**Conclusion.** T_k>0 for 1≤k≤6, but

T_2T_4-T_3²=-4|c|⁴(Im c)²<0.

The associated even real polynomial (1-z²/α²)(1-z²/conj(α)²) has all its zeros in |Re(z)|>4, |Im(z)|<1/2.

**Proof.** |arg α|<1/8 as in Lemma 27, so Re(α^{-2k})>0 for 1≤k≤6, giving the scalar signs. The zero locations are explicit. Expanding the determinant cancels c⁶ and conj(c)⁶ and yields

c²conj(c)⁴+conj(c)²c⁴-2c³conj(c)³
=|c|⁴(c-conj(c))²=-4|c|⁴(Im c)².

Since α² is nonreal, c is nonreal, making the result strictly negative. ∎

## Lemma 35: explicit uniform tails for the first five moments

**Hypotheses.** For n≥1 set K_n(u)=[8π²n⁴e^{9u/2}-12πn²e^{5u/2}]e^{-πn²e^{2u}}. For k∈{0,2,4,6,8} put B_k=∫_0²u^kΣ_{n=1}^4K_n(u)du.

**Conclusion.** 0≤M_k-B_k≤E, where the following explicit positive constant works for all five k:

E=128e^{-150}Σ_{j=0}^6 [6!/(6-j)!]50^{6-j}/3^{j+1} + 57,600,000e^{-74}.

**Proof.** Every K_n is positive on u≥0 by Lemma 19. Also u^k≤e^{8u} on u≥0 for the five stated k: for u≤1 use u^k≤1, and for u≥1 use log u≤u. For n≥1, n⁴≤16^{n-1} and n²≥1+3(n-1). Thus for X≥1,

Σ_{n≥1}n⁴e^{-πn²X}≤e^{-πX}/(1-16e^{-3πX})≤2e^{-πX},

using π>3 and e⁹>32. Dropping the negative term in each K_n and using π<4 gives u^kK(u)≤256e^{25u/2}e^{-3e^{2u}}. On u≥2 put X=e^{2u}; the resulting upper tail is at most 128∫_{e⁴}^∞X^{21/4}e^{-3X}dX. The exponential series through its seventh term gives e⁴>50. Since X^{21/4}≤X⁶ for X≥1, the tail is at most 128∫_{50}^∞X⁶e^{-3X}dX, which repeated integration by parts evaluates as the first term of E.

For the omitted n≥5 terms, integrate over all u≥0, an upper bound for their contribution on [0,2]. The same positive-term and π bounds give

Σ_{n≥5}∫_0^∞u^kK_n(u)du≤64Σ_{n≥5}n⁴∫_1^∞X⁶e^{-3n²X}dX
≤64·720Σ_{n≥5}n⁴e^{-(3n²-1)}.

The last inequality uses e^{-3n²X}≤e^{-(3n²-1)}e^{-X} for X≥1 and ∫_0^∞X⁶e^{-X}dX=720. Write n=5+j. Then n⁴≤625·16^j and n²≥25+11j for integers j≥0. Hence the last sum is at most 625e^{-74}/(1-16e^{-33})≤1250e^{-74}, giving the second term of E. The two upper bounds may overlap, which only enlarges their sum and is harmless. ∎

## Lemma 36: validated midpoint Taylor panels

**Hypotheses.** f is real C⁸ on [c-h,c+h], h>0. For j=0,…,7 write a_j=f^{(j)}(c)/j!, and suppose B≥sup_{u∈[c-h,c+h]}|f^{(8)}(u)|/8!.

**Conclusion.**

|∫_{c-h}^{c+h}f(u)du - 2Σ_{j=0}^3 a_{2j}h^{2j+1}/(2j+1)| ≤ 2Bh⁹/9.

Interval enclosures of the coefficients and B give an enclosure of the integral by interval addition and multiplication.

**Proof.** Taylor's theorem with integral remainder (or the Lagrange bound applied pointwise) gives |f(c+t)-Σ_{j=0}^7a_jt^j|≤B|t|⁸ for |t|≤h. Integrate this bound. Odd monomials integrate to zero, even monomials integrate to 2h^{j+1}/(j+1), and ∫_{-h}^h|t|⁸dt=2h⁹/9.

For implementation, normalized derivative coefficients of a product obey (fg)_n=Σ_{j=0}^n f_jg_{n-j}. If b=exp(a), its coefficients obey b_0=exp(a_0) and b_n=(1/n)Σ_{j=1}^n j a_jb_{n-j}, by differentiating b'=a'b and comparing coefficients. These identities hold at every point of a panel. Evaluating them by enclosing interval operations with the variable's constant coefficient equal to the full panel and its first coefficient equal to 1 therefore encloses f^{(8)}(u)/8! uniformly. Evaluating at the midpoint encloses the lower coefficients. The finite theta integrands are smooth by their explicit exponential formulas, so these operations apply. ∎

## Lemma 37: enclosures used by the finite certificate

**Hypotheses.** Real interval arithmetic uses downward rounding for lower endpoints, upward rounding for upper endpoints, and exact integer inputs. Decimal exp is correctly rounded to nearest, and each output is widened to its adjacent representable neighbors. Overflows, underflows, subnormals, invalid operations, and division by an interval containing zero are rejected. π is bounded by the rational alternating-series calculation described below.

**Conclusion.** The interval operations and Taylor recurrences in `certify_hankel.py` enclose the corresponding exact real quantities, subject to the stated arithmetic contracts. Summing the Lemma 36 panels and adding [0,E] from Lemma 35 encloses each actual moment.

**Proof.** Addition uses sums of the two lower and the two upper endpoints. Multiplication takes the minimum and maximum of the four endpoint products. Division multiplies by [1/upper,1/lower] for a divisor not containing zero. Directed rounding enlarges these exact interval operations. The exponential is increasing; correctly rounded endpoint exponentials lie between their adjacent representable neighbors, so widening encloses the exact endpoint values. Induction over expression evaluation and the finite derivative recurrences in Lemma 36 proves inclusion throughout. The implementation uses `copy_negate` and `copy_abs` for exact endpoint sign changes and rejects binary floating-point inputs.

For π, put A=arctan(1/5), B=arctan(1/239). The double-angle tangent identity gives tan(2A)=5/12 and tan(4A)=120/119, hence tan(4A-B)=1. The bounds A≥5/26 (integrate 1/(1+x²)≥25/26 on [0,1/5]), B<1/239, and A<1/5 place 4A-B strictly in (0,π/2). Thus 4A-B=π/4, giving π=16A-4B. For 0<x<1, integrating the finite geometric identity for 1/(1+x²) gives the alternating arctangent series and its next-term remainder bound. Ninety-six rational terms for each arctangent therefore provide exact rational lower and upper bounds for π, converted with directed rounding.

The arithmetic contract is Python's documented `decimal` contract: basic operations support directed rounding, `exp` is correctly rounded using ROUND_HALF_EVEN, and `next_minus`/`next_plus` return adjacent representable values. See the [official Decimal documentation](https://docs.python.org/3/library/decimal.html). This is a computer-assisted finite certificate, not an independently formalized verification of the Decimal implementation. ∎

## Lemma 38: a certified positive first mixed determinant

**Hypotheses.** The arithmetic contracts of Lemma 37 hold for the Python standard-library implementation. D and H_1 are as in Lemma 33.

**Conclusion.** The actual theta moments satisfy

3.38·10^{-15} < D < 4.34·10^{-15}.

In particular H_1 is positive definite. This is a computer-assisted finite partial result, not RH.

**Proof/certificate.** `certify_hankel.py` implements the explicit four-term theta integrands on [0,2], the eighth-order panel enclosure of Lemma 36, and the common tail of Lemma 35. It uses 70-digit outward arithmetic and the rational π enclosure of Lemma 37. The reproducible command is:

`python3 certify_hankel.py --panels 32 > hankel-certificate.json`

The saved output encloses S_2 in [0.0000371688839777867…, 0.0000371763145938135…] and D in [3.389399530870064…·10^{-15}, 4.331547435010644…·10^{-15}]. These ellipses abbreviate the exact rational decimal endpoints stored in `hankel-certificate.json`; the asserted looser bounds 3.38·10^{-15} and 4.34·10^{-15} contain those full endpoints strictly. The complete quadrature remainders and common tail enclosure are also saved there. The code propagates the full moment intervals through S_2,S_3,S_4 and then S_2S_4-S_3². By Lemmas 35–37, this interval contains the exact determinant. Its lower endpoint is positive, and S_2>0 is both analytically proved in Lemma 27 and enclosed positively here. Completing the square as in Lemma 33 proves positive definiteness.

Validation included exact rational containment checks for signed interval arithmetic, an exact exponential-derivative recurrence check at zero, and overlap with a separately evaluated expanded determinant expression. That second expression has a wider interval containing zero; the sign certificate uses the first, rigorously enclosing expression. No unvalidated decimal quadrature or zero computation enters the conclusion. ∎

## Lemma 39: moment tails through any fixed even degree

**Hypotheses.** m≥0 is an integer, p=m+2, and 0≤k≤2m is an even integer. Let B_k be the four-term integral on [0,2] in Lemma 35.

**Conclusion.** 0≤M_k-B_k≤E_m, where

E_m=128e^{-150}Σ_{j=0}^p [p!/(p-j)!]50^{p-j}/3^{j+1} + 80,000p!e^{-74}.

For moments through M_12, take m=6, p=8; the second coefficient is 3,225,600,000.

**Proof.** Repeat the bounds of Lemma 35 with u^k≤e^{2mu}. The substitution X=e^{2u} now gives the power X^{m+5/4}, bounded by X^{m+2}=X^p on X≥1. Thus the u≥2 tail is bounded by 128∫_{50}^∞X^p e^{-3X}dX, equal to the first displayed term by repeated integration by parts. The n≥5 bound becomes 64p!Σ_{n≥5}n⁴e^{-(3n²-1)}≤64p!·1250e^{-74}, equal to the second term. Both arguments are valid for each fixed m; the bound may become inefficient as m grows and no uniform-in-m sign conclusion is asserted. ∎

## Lemma 40: a justified finite Newton recurrence

**Hypotheses.** e_0=1 and e_j=M_{2j}/((2j)!M_0) for j≥1. S_k are as in Lemma 25.

**Conclusion.** For every fixed integer k≥1,

S_k=Σ_{j=1}^{k-1}(-1)^{j-1}e_jS_{k-j}+(-1)^{k-1}ke_k.

For H_2 the three leading principal minors are S_2, S_2S_4-S_3², and

D_2=S_2S_4S_6+2S_3S_4S_5-S_2S_5²-S_6S_3²-S_4³.

If all three are positive, H_2 is positive definite.

**Proof.** The even entire series makes F(t)=Σ_{j≥0}(-1)^j e_jt^j entire in t: its absolute series at |t| equals that of Ξ at |z|=sqrt(|t|). Near 0, Lemma 25 gives log F(t)=-Σ_{k≥1}S_kt^k/k. Therefore F'(t)=-F(t)Σ_{k≥1}S_kt^{k-1} there, with both series convergent. Comparing the coefficient of t^{k-1} gives (-1)^k ke_k=-Σ_{j=0}^{k-1}(-1)^j e_jS_{k-j}; isolate S_k to obtain the recurrence. The determinant formula is the direct 3-by-3 determinant expansion for [[S_2,S_3,S_4],[S_3,S_4,S_5],[S_4,S_5,S_6]]. Positive leading principal minors imply positive definiteness by the standard named Sylvester criterion for real symmetric matrices. Alternatively eliminate the first coordinate and then the second: the diagonal pivots are S_2, (S_2S_4-S_3²)/S_2, and D_2/(S_2S_4-S_3²), all positive. ∎

## Lemma 41: a certified positive H_2 test

**Hypotheses.** The arithmetic contracts of Lemma 37 hold. H_2=(S_{m+n+2})_{0≤m,n≤2} for the actual Ξ zeros.

**Conclusion.** H_2 is positive definite, and its determinant D_2 satisfies

3.10·10^{-31} < D_2 < 3.14·10^{-31}.

This is another finite computer-assisted partial result, not an all-degree positivity theorem.

**Proof/certificate.** The separate script `certify_hankel_next.py` imports the already inspected interval and Taylor operations from `certify_hankel.py`, integrates moments through M_12, uses E_6 from Lemma 39, and computes S_1,…,S_6 with the recurrence of Lemma 40. Run:

`python3 -B certify_hankel_next.py --panels 128 > hankel-h2-128.json`

The saved exact decimal interval endpoints give the following looser rational enclosures for the three leading principal minors:

- 0.00003717259927 < S_2 < 0.00003717259930;
- 3.86048·10^{-15} < S_2S_4-S_3² < 3.86050·10^{-15};
- 3.10·10^{-31} < D_2 < 3.14·10^{-31}.

Every lower endpoint is positive. The finite Taylor enclosure, the higher-moment tails, and the interval recurrence are justified by Lemmas 36–40. Thus the true three leading minors are positive and Lemma 40 proves positive definiteness. No extra panel refinement was needed at this degree. ∎

## Lemma 42: absolutely convergent Vandermonde expansion

**Hypotheses.** β_j=α_j^{-2} for Ξ as above, with indices counting multiplicity. Let d≥0 be fixed and H_d=(S_{m+n+2})_{0≤m,n≤d}.

**Conclusion.**

det H_d=Σ_{j_0<⋯<j_d}(Π_{r=0}^dβ_{j_r}²)Π_{0≤r<s≤d}(β_{j_s}-β_{j_r})²,

and the sum converges absolutely. These are algebraic squares, not modulus squares. Under RH every det H_d is strictly positive, but that unconditional sign has not been proved.

**Proof.** First keep only indices j≤N and define the (d+1)-by-N matrix V by V_{m,j}=β_j^{m+1}. The truncated Hankel matrix is VVᵀ, with transpose rather than conjugate transpose. The standard named Cauchy–Binet formula expresses det(VVᵀ) as the sum of squared determinants of its (d+1)-column submatrices. Factoring one β from each column leaves the standard Vandermonde determinant, giving exactly the finite version of the displayed formula.

Let R be a positive upper bound for all |β_j|, which exists by Σ|β_j|<∞. The absolute value of a summand is at most (2R)^{d(d+1)}Π_r|β_{j_r}|². The sum over increasing (d+1)-tuples of the latter products is at most (Σ_j|β_j|²)^{d+1}/(d+1)!, finite. Thus the infinite determinant expansion is absolutely convergent. Each entry of the truncated matrix converges absolutely to the corresponding S_{m+n+2}, and the determinant is a polynomial in finitely many entries, hence continuous. Passing N to infinity proves the identity. Repeated equal nodes contribute zero when both are selected, exactly as the Vandermonde factor prescribes; their other multiplicity contributions are counted by the indices.

Under RH all β_j are positive real. Lemma 27 gives infinitely many zeros, each of finite multiplicity, hence infinitely many distinct nodes. Every summand is nonnegative and at least one tuple of d+1 distinct nodes has strictly positive contribution. This proves strict positivity conditionally. For nonreal nodes, even one conjugate pair can make a square negative, as Lemma 34 demonstrates. ∎

## Lemma 43: ordinary moment matrices are strictly positive definite

**Hypotheses.** d≥0 is an integer and G_d=(M_{2m+2n})_{0≤m,n≤d}, with the theta moments of Lemma 21.

**Conclusion.** G_d is positive definite for every d. This is not the same matrix as H_d=(S_{m+n+2}).

**Proof.** For a real vector (c_0,…,c_d), let q(X)=Σ_{m=0}^d c_mX^m. Finite expansion under the moment integral gives

Σ_{m,n=0}^d c_mc_nM_{2m+2n}=∫_0^∞K(u)q(u²)²du.

It converges by the fixed moment bounds and is nonnegative. If the vector is nonzero, q is a nonzero polynomial and has only finitely many real roots. Thus q(u²)² is strictly positive on some open interval in (0,∞), where K is strictly positive, and the integral is strictly positive. This is a genuine modulus-free square of a real-valued function; unlike the reciprocal-node expressions, its arguments are real. ∎

## Lemma 44: ordinary Gram positivity does not survive the needed logarithm map

**Hypotheses.** On R set g(u)=exp(-cosh(2u)), h(u)=(9/10)g(u)+(g(u-8)+g(u+8))/20, and F(z)=∫_R h(u)e^{izu}du. Define normalized even moments μ_{2n}=∫_R u^{2n}h(u)du/∫_R h(u)du. Near z=0 define T_2 by

log(F(z)/F(0))=-(μ_2/2)z²-(T_2/2)z⁴+O(z⁶).

**Conclusion.** h is smooth, strictly positive, even, and superexponentially decaying; its ordinary even-moment Gram matrices are all positive definite. Nevertheless T_2<0, so the analogous 1-by-1 logarithmic Hankel matrix is already negative.

**Proof.** The regularity, decay, and all moment/entire-transform properties follow exactly as in Lemma 22, now with shifts 8 and positive weights summing to 1. Ordinary Gram positivity follows from the proof of Lemma 43 applied to this positive density. Write ν_2 and ν_4 for the normalized moments of g. Symmetry and real substitutions in the shifted integrals give

μ_2=ν_2+8²/10,

μ_4=ν_4+(6·8²/10)ν_2+8⁴/10.

It follows that μ_4-3μ_2²=(ν_4-3ν_2²)+(7/100)8⁴.

To bound ν_2, use cosh(2u)≥1+2u², so ∫_R u²g(u)du≤e^{-1}√π/(4√2) by the Gaussian second moment. On [-1/2,1/2], cosh(2u)≤cosh 1<2, so ∫_R g(u)du>e^{-2}. Here cosh 1<2 follows from e<3 and e^{-1}<1, and e<3 follows by comparing Σ_{n≥2}1/n! with Σ_{n≥2}2^{-(n-1)}, strictly at n≥3. Therefore ν_2<e√π/(4√2)<3/2, using π<4. As ν_4≥0,

μ_4-3μ_2² > -27/4+(7/100)4096=27997/100>0.

Expanding the local logarithm of 1-(μ_2/2)z²+(μ_4/24)z⁴+O(z⁶) gives T_2=(3μ_2²-μ_4)/12<0. This proves the failed preservation directly. Also the real shift formula gives F(z)=[9+cos(8z)]G(z)/10 for the entire transform G of g, so it has explicit nonreal zeros at (π+i log(9+√80))/8 and its symmetric images. No positivity of reciprocal-zero forms can be inferred merely from the ordinary moment Gram property. ∎

## Lemma 45: strict log-concavity of each theta-kernel summand

**Hypotheses.** n≥1, u≥0, v_n=πn²e^{2u}, and K_n is as in Lemma 35. Put ℓ_n(u)=log K_n(u), which is defined since K_n>0.

**Conclusion.**

ℓ_n'(u)=9/2-2v_n+6/(2v_n-3),

ℓ_n''(u)=-4v_n-24v_n/(2v_n-3)²<0.

Thus every individual K_n is strictly log-concave on [0,∞).

**Proof.** Factor K_n=4v_n(2v_n-3)e^{u/2}e^{-v_n}, with v_n≥π>3 and v_n'=2v_n. Its logarithm is log 4+log v_n+log(2v_n-3)+u/2-v_n. Differentiation gives 5/2+4v_n/(2v_n-3)-2v_n=9/2-2v_n+6/(2v_n-3). Differentiating once more gives the displayed negative expression. Every denominator is strictly positive on the stated domain, so both differentiations are valid. ∎

## Lemma 46: the variance obstruction in a sum of log-concave terms

**Hypotheses.** Positive C² functions f_n on a real interval have locally uniformly convergent sums of f_n, f_n', f_n'', and f_n'^2/f_n. Set f=Σ_n f_n>0, w_n=f_n/f, and ℓ_n=log f_n.

**Conclusion.**

(log f)''=Σ_nw_nℓ_n''+Σ_nw_n(ℓ_n'-Σ_jw_jℓ_j')².

These hypotheses hold for f_n=K_n on u≥0. Even if every ℓ_n'' is negative, (log f)'' need not be negative.

**Proof.** The convergence hypotheses justify f'=Σf_n' and f''=Σf_n''. Since f_n''=f_n(ℓ_n''+(ℓ_n')²), substitution into (log f)''=f''/f-(f'/f)² gives the mean-curvature plus variance identity. The squared sum is well-defined by the assumed convergence and Cauchy–Schwarz for the nonnegative weights. For K_n, Lemma 45 and the explicit K_n formula bound every relevant summand, on each compact u-interval, by a fixed polynomial in n times e^{-πn²}; the rational denominators are bounded away from zero. These bounds give all required local uniform convergence, including termwise derivatives.

For the failure example, f_1(u)=e^{-(u-2)²} and f_2(u)=e^{-(u+2)²} each have log second derivative -2. Their sum is 2e^{-u²-4}cosh(4u), whose log second derivative at u=0 is -2+16=14>0. Thus termwise log-concavity alone cannot remove the variance term. ∎

## Lemma 47: strict log-concavity of the full theta kernel

**Hypotheses.** u≥0, v=πe^{2u}, and K=Σ_{n≥1}K_n is the actual theta kernel.

**Conclusion.**

(log K(u))'' < -(68/125)v <0.

Thus K is strictly log-concave on [0,∞). This does not by itself assert real zeros for its Fourier transform.

**Proof.** Here v>3 and v_n=n²v. The explicit factors in Lemma 45 give

K_n/K_1=n²(2n²v-3)/(2v-3)·e^{-(n²-1)v}≤2n⁴e^{-(n²-1)v},

since 2v-3≥v and 2n²v-3≤2n²v. For n≥2, the slope difference from Lemma 45 is negative, with absolute value at most 2(n²-1)v+6/(2v-3)≤2(n²-1)v+2≤3(n²-1)v.

Variance is minimized by centering at the weighted mean, so it is bounded above by the mean square distance from the first slope. Using w_n≤K_n/K_1 gives

Var_w(ℓ_n')≤Σ_{n≥2}w_n(ℓ_n'-ℓ_1')²
≤18v²Σ_{n≥2}n⁴(n²-1)²e^{-(n²-1)v}
≤18v²Σ_{n≥2}n⁸e^{-(n²-1)v}.

Write n=2+j. Then n⁸≤256·256^j, because 2+j≤2(j+1) and j+1≤2^j. Also n²-1≥3+5j for integer j≥0. Therefore

Σ_{n≥2}n⁸e^{-(n²-1)v}≤256e^{-3v}/(1-256e^{-5v})<512e^{-3v}.

For the denominator bound, v>3 and e³>20 imply e^{5v}>e^{15}>20⁵>512. The elementary bound e³>20 follows by summing its exponential series from degree zero through eight (all later terms are positive). Thus the variance is <9216v²e^{-3v}.

The mean curvature in Lemma 46 is strictly less than -4Σw_n n²v≤-4v by Lemma 45. The function v e^{-3v} decreases for v≥3, so

2304v e^{-3v}≤6912e^{-9}<6912/8000=108/125,

again using e³>20. Combining the mean and variance bounds yields

(log K)''<-4v+9216v²e^{-3v}<-4v(1-108/125)=-(68/125)v.

All sums and derivatives are justified by Lemma 46. ∎

## Lemma 48: smooth even extension and monotonicity of K

**Hypotheses.** Define A(u)=e^{u/2}ψ(e^{2u}) for every real u and K(u)=2A''(u)-A(u)/2.

**Conclusion.** K is smooth, strictly positive, and even on R. K'(0)=0, K'(u)<0 for u>0, and log K is strictly concave on R. In fact (log K)''<-(68/125)πe^{2|u|}.

**Proof.** On each compact real u-interval, e^{2u} has a positive lower bound, so the differentiated theta series converges uniformly in every fixed derivative order. Thus A and K are smooth on R. The theta transformation gives ψ(e^{-2u})=(e^u-1)/2+e^uψ(e^{2u}); multiplying by e^{-u/2} yields

A(-u)=A(u)+sinh(u/2).

Differentiate this identity twice. Since (sinh(u/2))''=sinh(u/2)/4, applying 2D²-1/2 cancels the extra term and gives K(-u)=K(u). Positivity on u≥0 is Lemma 19 and extends by evenness; differentiating evenness at zero gives K'(0)=0. Lemma 47 gives the strict curvature estimate for u≥0. Evenness extends it to u≤0 with |u|. For u>0, integrate (log K)''<0 from 0 to u, using (log K)'(0)=0, to get (log K)'(u)<0 and hence K'(u)<0. ∎

## Lemma 49: strict log-concavity alone still does not force real zeros

**Hypotheses.** g(u)=e^{-u²}, h(u)=(9/10)g(u)+(g(u-1/2)+g(u+1/2))/20, and F(z)=∫_R h(u)e^{izu}du.

**Conclusion.** h is smooth, strictly positive, even, and strictly log-concave, with (log h)''≤-1. Nevertheless F has nonreal zeros and its local logarithmic quantity T_2, defined as in Lemma 44, is -7/19200<0. This example has Gaussian decay, not the theta kernel's superexponential decay scale.

**Proof.** Factor h(u)=e^{-u²}L(u), where L(u)=9/10+(e^{-1/4}/20)(e^u+e^{-u}). The three positive exponential terms in L have constant logarithmic slopes 0,1,-1 and zero logarithmic curvature. The finite version of Lemma 46 therefore gives (log L)'' equal to their weighted slope variance, at most their weighted second moment, which is ≤1. Thus (log h)''=-2+(log L)''≤-1. Positivity, evenness, and smoothness are immediate.

The Gaussian Fourier transform and real shifts give

F(z)=√πe^{-z²/4}[9+cos(z/2)]/10.

For b=log(9+√80)>0, cosh b=9, so z=2π+2ib is a nonreal zero. All transforms and their derivatives are entire by Gaussian exponential-moment domination on compact z-sets. Finally the normalized Gaussian has second moment 1/2 and fourth moment 3/4, so its fourth cumulant is zero. The shift calculation in Lemma 44, now with shift 1/2 and total shifted weight 1/10, gives fourth cumulant (7/100)(1/2)^4=7/1600. Hence T_2=-(7/1600)/12=-7/19200. This demonstrates that strict log-concavity is insufficient on its own; the example does not refute a theorem using the additional theta-scale decay or other specific theta identities. ∎

## Lemma 50: a small superexponential mixture remains strictly log-concave

**Hypotheses.** a=1/100, g(u)=exp(-cosh(2u)), and h_a(u)=(9/10)g(u)+(g(u-a)+g(u+a))/20 on R.

**Conclusion.** h_a is strictly log-concave on all R; more quantitatively,

(log h_a(u))''<-(1/4)cosh(2u).

Its entire Fourier transform still has nonreal zeros from its factor (9+cos(az))/10.

**Proof.** Regard the three terms as p_i exp(-V_i(u)), with shifts t_i∈{-a,0,a}, weights p_i∈{1/20,9/10,1/20}, and V_i(u)=cosh(2(u+t_i)). Write C=cosh(2u)≥1 and B=sinh(2a). The elementary exponential-series bound e^x≤1/(1-x) for 0<x<1 gives e^{2a}<2 and B<1/49<1/40. For every shift, V_i≥e^{-2a}C>C/2, so the mean logarithmic curvature is Σw_i(-4V_i)<-2C.

The three logarithmic slopes are -2sinh(2(u+t_i)). Their range is exactly 4CB. For any real variable in an interval of length L, its variance is ≤L²/4: expand the nonnegative product (X-min)(max-X), then bound (mean-min)(max-mean) by L²/4. Thus the slope variance is ≤4C²B²<C²/400. If C≤128, this is at most (8/25)C, giving total curvature <-(42/25)C.

For the remaining region use the identity Var_w(ℓ_i')=Σ_{i<j}w_iw_j(ℓ_i'-ℓ_j')². Put Δ=V_i-V_j. The ratio of any two weights p_i,p_j is at most 18, and the denominator of w_iw_j is at least either unnormalized term squared; hence w_iw_j≤18e^{-|Δ|}. The hyperbolic addition identities give

(V_i'-V_j')²=4Δ²+16sinh²(t_i-t_j)≤4Δ²+16B².

For x≥0, x²e^{-x}≤4/e²<1. Each pair therefore contributes <72+288/1600=3609/50 to the variance, so all three contribute <10827/50. If C≥128, combining this with mean curvature <-2C gives

(log h_a)''<[-2+10827/6400]C=-(1973/6400)C<-C/4.

This and the first region prove the uniform conclusion. Smoothness, evenness, positivity, and superexponential decay follow from the explicit positive shifts, as in Lemma 22. Real substitution in the entire Fourier integral gives F_a(z)=[9+cos(az)]G(z)/10; taking z=(π+i log(9+√80))/a makes the prefactor zero. This supplies a global small-shift proof rather than assuming log-concavity is stable under shifts. ∎

## Lemma 51: order at most one for superexponential Fourier kernels

**Hypotheses.** A real even measurable function h satisfies |h(u)|≤C exp(-c e^{2|u|}) for some C,c>0. Define F(z)=∫_R h(u)e^{izu}du.

**Conclusion.** F is entire and obeys log max_{|z|≤R}|F(z)|=O((R+1)log(R+2)) as an upper bound; in particular, if F is nonzero, its entire order is at most 1. This applies to g and all the finite positive shifts used above.

**Proof.** For every fixed derivative order k and compact |z|≤R, the absolute integrand after k derivatives is at most C|u|^k exp(R|u|-c e^{2|u|}), integrable. Hence dominated differentiation makes F entire. For R≥1,

max_{|z|≤R}|F(z)|≤2C∫_0^∞exp(Ru-c e^{2u})du=C∫_1^∞X^{R/2-1}e^{-cX}dX.

With m=ceil(R/2), bound X^{R/2-1}≤X^m and extend the integral to (0,∞), obtaining C m! c^{-(m+1)}. Taking logarithms and using m!≤m^m gives the asserted upper bound. A finite shift changes only C,c: e^{2|u-t|}≥e^{-2|t|}e^{2|u|}. No zero-location theorem is used. ∎

## Lemma 52: tuning the introduced zeros into the strip

**Hypotheses.** a=1/100, b=1/1000, c=cosh b, g(u)=exp(-cosh(2u)), and

h(u)=[c g(u)+(g(u-a)+g(u+a))/2]/(c+1).

Let G and F be the Fourier transforms of g and h.

**Conclusion.** h is positive, smooth, even, superexponentially decaying, and satisfies (log h)''<-cosh(2u)/4. F has order at most 1 and

F(z)=[c+cos(az)]G(z)/(c+1).

All zeros of the prefactor are exactly z=(2k+1)100π±i/10, k∈Z. Thus the introduced nonreal zeros satisfy |Re z|>4 and |Im z|<1/2. This lemma alone does not locate every zero of G.

**Proof.** Since 1<c<2, the ratio between any two of the three positive weights is at most 2c<4<18. The proof of Lemma 50 used the weights only through their positivity, normalization, and the ratio bound 18. The same curvature estimates therefore apply without change. The remaining kernel properties are immediate from the positive shifts, and Lemma 51 gives order at most 1.

The Fourier factorization follows by real substitution in absolutely convergent integrals. To solve cos(az)=-c, put w=e^{iaz}≠0. Then w²+2cw+1=0, whose roots are -e^b and -e^{-b} since c=cosh b. Taking all logarithms gives az=(2k+1)π±ib, exactly the listed zeros. There are no other prefactor zeros. Their real parts have absolute value at least 100π>4 and imaginary parts have absolute value 1/10<1/2. The product's other zeros are precisely zeros of G, which require a separate argument. ∎

## Lemma 53: a differential equation for the comparison base transform

**Hypotheses.** Fix z∈C, set ν=z/2, and for real x≥0 define

Y_z(x)=∫_0^∞exp(-e^x cosh t)cos(νt)dt.

G(z)=∫_R exp(-cosh(2u))e^{izu}du as in Lemma 52.

**Conclusion.** Y_z is smooth, Y_z(0)=G(z), and

-Y_z''(x)+e^{2x}Y_z(x)=(z²/4)Y_z(x).

With r=e^x tending to infinity, Y_z(x)=O_z(e^{-r}), Y_z'(x)=O_z(e^{-r/2}), and sqrt(r)e^rY_z(x) tends to sqrt(π/2)>0. In particular Y_z is not identically zero.

**Proof.** Evenness of the g integral and t=2u give Y_z(0)=G(z). Any fixed x-derivative introduces only a polynomial in e^x cosh t, while the exponential exp(-e^x cosh t) dominates that polynomial times |cos(νt)|≤e^{|Im ν|t} on compact x-intervals. This justifies smooth differentiation. Write k(t)=e^{-r cosh t}. Direct differentiation gives

k_{xx}=(r²cosh²t-r cosh t)k,  k_{tt}=(r²sinh²t-r cosh t)k,

so k_{xx}-r²k=k_{tt}. Twice integrating k_{tt}cos(νt) by parts gives -ν²Y_z: at infinity the exponential dominates all boundary factors; at zero k_t(0)=0 and sin 0=0. This yields the stated equation.

Let B=|Im ν|. Since cosh t≥1+t²/2 and r≥1,

|Y_z(x)|≤e^{-r}∫_0^∞e^{-t²/2+Bt}dt=O_z(e^{-r}).

For the derivative use y e^{-y}≤2e^{-y/2}, y≥0, with y=r cosh t. The same Gaussian comparison bounds |Y_z'(x)| by a constant times e^{-r/2}. Finally set t=v/sqrt(r):

sqrt(r)e^rY_z(x)=∫_0^∞exp[-r(cosh(v/sqrt(r))-1)]cos(νv/sqrt(r))dv.

The integrand tends pointwise to e^{-v²/2} and has absolute value at most e^{-v²/2+Bv}, integrable and independent of r≥1. Dominated convergence gives the asserted nonzero limit, using the Gaussian integral. ∎

## Lemma 54: every comparison-base zero is real and outside the small rectangle

**Hypotheses.** G(z)=0 and Y=Y_z is the nontrivial solution in Lemma 53.

**Conclusion.** z is real and |z|>2sqrt(7)>4.

**Proof.** Y(0)=0. Its smoothness gives Y(x)=O(x) near zero; the decay in Lemma 53 makes Y,Y',e^xY square integrable on [0,∞), and makes Y'(x)conj(Y(x)) tend to zero at infinity. Multiply the differential equation by conj(Y), integrate on [0,R], and integrate the second derivative by parts. Letting R tend to infinity gives

∫_0^∞(|Y'|²+e^{2x}|Y|²)dx=(z²/4)∫_0^∞|Y|²dx.

The right-hand norm is strictly positive by nontriviality. The left side is real and positive, hence z²/4 is positive real, which forces z real and nonzero.

For the sharper lower bound, put b(x)=1/x-2x for x>0. On [ε,R], expansion and integration by parts give

∫|Y'-bY|²dx=∫[|Y'|²+(b²+b')|Y|²]dx-[b|Y|²]_{ε}^{R}.

Here b²+b'=4x²-6. At zero, Y=O(x) makes b|Y|²=O(x) tend to zero and makes Y'-bY bounded. At infinity the proved decay kills both the boundary and all polynomial weights. Taking ε to zero and R to infinity proves

∫_0^∞(|Y'|²+4x²|Y|²)dx≥6∫_0^∞|Y|²dx.

For x>0, the exponential series gives

e^{2x}≥1+2x+2x²+(4/3)x³>1+4x²,

because the difference after the constant and 4x² is 2x(1-x+(2/3)x²)>0; its quadratic factor has negative discriminant and positive leading coefficient. Therefore the first energy integral is strictly greater than 7∫|Y|². Strictness holds because Y is nonzero on some interval with x>0. Thus z²/4>7, proving the stated bound. ∎

## Lemma 55: the combined generic conditions admit nonreal zeros

**Hypotheses.** Let 0<a≤1/100, c_a=cosh(a/10), and

h_a(u)=[c_a g(u)+(g(u-a)+g(u+a))/2]/(c_a+1),  g(u)=exp(-cosh(2u)).

Let F_a be the Fourier transform of h_a.

**Conclusion.** Every F_a has all of the following properties: entire order at most 1; evenness and reality on R; a smooth strictly positive even kernel with superexponential decay and (log h_a)''<-cosh(2u)/4; strictly alternating nonzero even Taylor coefficients; positive values on the imaginary axis; and every zero in |Re z|>4, |Im z|<1/2. Nonetheless it has nonreal zeros at (2k+1)π/a±i/10 for every integer k.

**Proof.** The proof of Lemma 50 is uniform when 0<a≤1/100: the bounds e^{2a}<2 and sinh(2a)<1/40 only improve as a decreases. The three normalized weights here have maximum ratio 2c_a<4<18, so the identical curvature proof applies. Lemma 51 supplies the entire order. Positivity and evenness of the kernel give imaginary-axis positivity and nonzero alternating even coefficients by the same dominated cosine expansion as Lemma 21, applied to 2h_a on [0,∞).

The shift formula gives F_a(z)=[c_a+cos(az)]G(z)/(c_a+1). As in Lemma 52, every prefactor zero is exactly (2k+1)π/a±i/10. Its real part has absolute value ≥100π>4 and its imaginary part has absolute value 1/10. Lemma 54 places every zero of G on the real axis with absolute value >4. Products of entire functions have precisely the union of their zero sets, with added multiplicities, so these two lists locate all F_a zeros. All the stated properties hold simultaneously, but the displayed prefactor zeros are nonreal. ∎

## Lemma 56: every finite comparison-base Hankel matrix is positive definite

**Hypotheses.** G(z)=∫_R exp(-cosh(2u))e^{izu}du. Select its positive zeros α_j with multiplicity, and define β_j=α_j^{-2}, T_k=Σ_jβ_j^k, and H_d(G)=(T_{m+n+2})_{0≤m,n≤d}.

**Conclusion.** G has infinitely many distinct real zeros, Σ_jβ_j<∞, and H_d(G) is positive definite for every fixed d≥0.

**Proof.** Lemma 51 gives order at most 1; G(0)>0 and G is even. Lemma 54 proves all zeros real and nonzero. The named Hadamard theorem and exactly the pairing argument of Lemma 24 give G(z)=G(0)Π_j(1-z²/α_j²), with Σ_j|α_j|^{-2}<∞. The positive density g has finite and strictly positive moments of every even order, so its cosine Taylor series has every even coefficient nonzero and G is not a polynomial. A finite zero set would make the paired product a polynomial; thus G has infinitely many zeros, and hence infinitely many distinct zeros since every zero of a nonzero entire function has finite multiplicity.

All β_j are now strictly positive. For any nonzero real polynomial q, the convergent sum Σ_jβ_j²q(β_j)² is strictly positive: every term is nonnegative and q can vanish at only finitely many distinct nodes. Its convergence follows from Σβ_j<∞ and boundedness of q on the node set, as in Lemma 30. This sum is the quadratic form of H_d(G) when deg q≤d, proving positive definiteness for every fixed d. ∎

## Lemma 57: any fixed number of Hankel tests can coexist with nonreal zeros

**Hypotheses.** N≥0 is a fixed integer. F_a is the family of Lemma 55, extended at a=0 by F_0=G. Define each H_d(F_a) from the paired reciprocal-zero power sums, equivalently from its local logarithmic coefficients.

**Conclusion.** There exists a_N∈(0,1/100] such that H_d(F_{a_N}) is positive definite for all 0≤d≤N, while F_{a_N} has nonreal zeros and every generic property in Lemma 55. The choice of a_N is allowed to depend on N; no single nonzero a is asserted to pass all degrees.

**Proof.** The entire-order, evenness, and positive-at-zero hypotheses needed for the paired product and local logarithmic identities hold for every F_a and for G by Lemmas 51, 55, and 56. Also F_a(0)=G(0)>0 exactly. The explicit factor

F_a(z)/G(z)=[cosh(a/10)+cos(az)]/[cosh(a/10)+1]

tends to 1 locally uniformly as a tends to zero. In particular each fixed Taylor coefficient of F_a tends to that of G. This also follows directly without differentiating a limit: integrate the finite binomial expansion for each shifted moment of g, whose coefficients are continuous functions of a and cosh(a/10).

For each fixed k, the normalized coefficients e_j and the finite Newton recurrence in Lemma 40 show that the reciprocal power sum T_k(F_a) tends to T_k(G). Hence every fixed finite determinant det H_d(F_a) is continuous at a=0. Lemma 56 makes det H_d(G)>0 for each d. For the finitely many d=0,…,N, choose a common sufficiently small positive a_N≤1/100 so that all those determinants stay positive. Sylvester's criterion, or successive completion of squares, then makes each H_d(F_{a_N}) positive definite. Yet Lemma 55 supplies its nonreal zeros (2k+1)π/a_N±i/10 and all the other stated properties. ∎

## Assembly and unresolved gap

The current main route begins with the classical zero localization and theta representation, proves the growth required for an unconditional Hadamard product, and translates that product into summable reciprocal-zero nodes. Lemmas 30–32 then prove that all mixed polynomial forms being nonnegative would force the nodes to be real and hence prove RH. This is a proved equivalence, not a proved positivity assertion.

For the actual theta moments, the analytical estimates prove six individual power-sum signs and a degree-two Jensen test. The interval certificates additionally prove H_1 and H_2 positive definite, under the explicit arithmetic contracts. No step extends these finite results to arbitrary degree. Proving that extension—or finding a different argument that excludes every off-line zero—is the unresolved gap.

Counterexamples retained in the lemma chain and archived in ATTEMPTS rule out the tested shortcuts: symmetry alone, continued prime positivity, positive Laplace/Fourier kernels alone, all scalar power-sum signs alone, and coarse strip geometry alone do not supply the missing mixed positivity. None is a counterexample to RH itself.

## Partial results

- ζ(s)≠0 when Re(s)>1, with an absolutely convergent reciprocal there.
- ζ(1+it)≠0 for every real t≠0, by Lemmas 5–7 (the classical boundary nonvanishing argument).
- Zeros in 0<Re(s)<1 occur in reflection/conjugation orbits with equal multiplicities and have nonzero imaginary part; ζ(σ)<0 for real 0<σ<1 (Lemma 13).
- The only zeros outside 0<Re(s)<1 are the simple zeros at -2,-4,-6,… (Lemma 9); ζ(0)=-1/2 (Lemma 8).
- The Euler-logarithm positive series fails absolute convergence for 0<Re(s)≤1, and its product inequality is false near the origin even with all factors replaced by moduli (Lemmas 10–11).
- A nonnegative bounded indicator Laplace kernel can have nonreal zeros within 0<Re(s)<1 (Lemma 15); the η integral alone gives no zero-free theorem.
- The theta integral constructs entire ξ and even real Ξ, with an exact multiplicity-preserving correspondence to the nontrivial ζ zeros (Lemma 18). No reality theorem for Ξ zeros has been proved.
- Ξ has a strictly positive theta cosine kernel, positive even moments, and Ξ(iy)>0. Smoothness, evenness, moment signs, and superexponential kernel decay still do not force real transform zeros (Lemmas 19–22).
- Ξ has order at most 1 and a justified paired Hadamard product. There are infinitely many nontrivial zeros, and none has |Im(s)|≤4 (Lemmas 23–27).
- S_k>0 for k=1,…,6, M_2²<M_0M_4<3M_2², and the degree-two Jensen polynomial has two distinct negative roots (Lemmas 27–28).
- H_1 and H_2 are positive definite by the reproducible finite interval certificates in Lemmas 38 and 41. These computations certify finite inequalities with remainder bounds; they do not certify RH.

No novelty or proof of RH is claimed for these baseline results and finite certificates. Excluding every off-line point inside the open strip remains unproved.

## Known traps checked

- No explicit-formula error estimate, prime-number-theorem error term, or unproved zero-free strip is used.
- No RH-equivalent positivity is assumed. Corollary 32a explicitly labels its all-degree condition as RH-equivalent and unproved; it is never used as a premise for an unconditional conclusion.
- Every infinite manipulation has a stated bound: Dirichlet/prime absolute sums, compact alternating-series tails, exponential theta tails, or summable reciprocal squares. The boundary proof uses local Taylor/Laurent bounds, not a boundary interchange of prime sums.
- There are no numerical zero computations or extrapolations from finitely many zeros. The finite determinant calculations use proved tails, proved quadrature remainders, and outward interval arithmetic, with their implementation contracts explicitly stated. An ordinary decimal value would not suffice.
- A positive kernel does not make its Fourier transform real-rooted. Reflection invariance of a set does not make every point fixed. Concrete counterexamples are retained.
- Algebraic squares in mixed forms are not replaced by modulus squares; that replacement would erase the very obstruction being tested.
- Finite positive scalar sums, a degree-two Jensen polynomial, and two finite positive Hankel matrices are not an all-degree theorem. No Li, Robin, Lagarias, or Nyman–Beurling criterion is claimed proved.

## What a Lean check would need

This is a future statement inventory only; no Lean is used or written.

1. The defining Dirichlet series, meromorphic continuation theorem, and functional equation for ζ with their precise domains.
2. For real σ>1, convergence of Σ n^{-σ}; |μ(n)|≤1; and Σ_{d|n}μ(d)=1 for n=1 and 0 otherwise.
3. Absolute summability of the double product and its regrouping by mn=k, giving ζ(s)M(s)=1 for Re(s)>1.
4. Meromorphicity of conjugate-reflected functions and the meromorphic identity theorem, yielding the conjugation identity and preservation of zero order.
5. Nonvanishing of the functional-equation prefactor on 0<Re(s)<1 and preservation of zero order under s↦1-s.
6. The polynomial's factorization, two symmetry identities, two positivity identities, and four off-line roots.

7. Uniform absolute convergence of the Euler-product logarithm on Re(s)≥1+δ, δ>0, and the finite-prime-product tail estimate proving exp L=ζ.
8. The identity 3+4cos θ+cos 2θ=2(1+cos θ)², its summed logarithmic inequality for σ>1, and exponentiation.
9. Local bounds at a simple pole, a zero of order m, and a regular point, giving the contradiction 1≤C h^{4m-3} as h decreases to zero for t≠0.

10. Integral comparison giving residue 1, the local functional-equation expansion giving ζ(0)=-1/2, and the classification and simplicity of zeros outside the open strip.

11. Divergence of reciprocal-prime sums via finite products and harmonic sums; the k=1 comparison; and the continuity counterexample F(0,0)=1/256 to the proposed continued inequality.

12. The alternating-series compact tail bound, removable product identity for η, paired positivity for real 0<σ<1, and the absolutely convergent indicator-kernel integral.
13. The elementary cubic root count and Vieta modulus bound in Lemma 15, the compact-support Laplace transform, and its zero obtained from an individual complex logarithm.

14. Poisson summation with the stated Fourier convention and Gaussian transform; theta transformation and its derivative tail bounds.
15. Absolute Fubini for the Mellin integral, the split identity, and the compact derivative majorants proving I entire.
16. Entirety, two symmetries, endpoint values, continued product formula, and exact zero/multiplicity correspondence for ξ and Ξ.

17. The differentiated theta identity, exact A and K derivative formulas, termwise K positivity, and superexponential majorants.
18. The change x=e^{2u}, both integration-by-parts boundary terms, and local uniform convergence of every complex derivative of the cosine integral.

19. Absolute cosine-series domination and moment Cauchy–Schwarz; the shifted superexponential counterexample, its Fourier factorization, and the exact off-real zero (π+i log(2+√3))/4.

20. The explicit entire-growth bound, the order-at-most-one Hadamard theorem, reciprocal-square summability, justified ± pairing, and local logarithm coefficient identities.
21. The analytic rectangle bound |J|<1/72, infinitude of zeros, positivity of S_1,…,S_6, strict moment inequalities, and the degree-two Jensen root calculation.
22. The scalar-sign counterexample including its cosine multiplier, convergent mixed forms, finite interpolation witness, and infinite interpolation witness with the C²4^{-N} tail bound.
23. Corollary 32a as an equivalence only, the moment determinant formulas, and the exact negative determinant for the conjugate-node example. Proving all actual Hankel matrices positive semidefinite would remain a separate missing theorem.
24. The explicit E and E_m truncation estimates, eighth-derivative Taylor panel bound, and normalized derivative recurrences.
25. Rational Machin bounds, verified interval-operation contracts (or an independent rational interval implementation), and rechecking the saved certificates' full rational endpoints against every intermediate enclosure. This would replace the current reliance on the documented Decimal implementation.
26. Newton's recurrence and the positive-principal-minor implication, yielding the finite conclusions H_1>0 and H_2>0 from their respective interval certificates.

Even checking every item would certify only the partial results and the stated equivalence, not the missing all-degree positivity or RH.

## Next lemma

Derive the absolutely convergent Cauchy–Binet/Vandermonde expansion for det H_d, keeping algebraic squares distinct from modulus squares. Use it to identify what further actual-theta structure could prove the missing sign; the finite H_1 and H_2 results provide no automatic extension. PROGRESS.md records the active next action and dated per-lemma history.
