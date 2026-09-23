# Lemma 143: all-positive-mode stationary phase

**Hypotheses.** Use I_k(t), N=sqrt(t/(2π)), and τ=t−π/2 from L140, with real t≥π. For every integer k≥1 put X_k=τ/(2πk), r_k=X_k/N, and

M_k(t)=X_k^(−1)sqrt(2π/τ)exp(−log² r_k)
        ·exp(iτ(log X_k−1)−iπ/4).

**Conclusion.** The leading-term series converges absolutely and

Σ_{k≥1}|I_k(t)−M_k(t)|=O(t^(−3/2)) as t→∞.                 (1)

The constant is independent of t and there is no mode cutoff. In particular this is o(t^(−1)). This is an additive expansion, not a nonvanishing or relative estimate.

**Proof.**

Write A=τ/(2πN), so r_k=A/k, X_k=NA/k and A/N=τ/t≤1. The exact substitution used in L141 gives

I_k=X_k^(−1+iτ)∫₀^∞ a_k(u)exp(iτφ(u))du,
a_k(u)=u^(−2)exp(−log²(Au/k)),  φ(u)=log u−u.              (2)

We retain the fixed cutoff χ and compact Morse coordinate v from L141. Unlike the compact parameter argument there, we will sum the derivative estimates over every k.

### A lattice estimate

For each nonnegative integer p there is a constant C_p such that, for every z>0,

Σ_{k≥1} k exp(−log²(z/k))(1+|log(z/k)|^p)≤C_p z².         (3)

Indeed the function exp(−w²)(1+|w|^p) is bounded on R, and is at most a constant times exp(3w) for w≤0. The terms k≤z therefore sum to O(z²), with an empty sum if z<1. For k>z they sum to at most C z³ Σ_{k>z}k^(−2). For z≥1 the last sum is O(1/z), by integral comparison (adjusting the constant for 1≤z<2); for z<1 it is bounded by Σ_{k≥1}k^(−2), and z³≤z². This proves (3), including arbitrarily small z.

By induction, for each fixed j≥0,

a_k^(j)(u)=u^(−2−j)exp(−log²(Au/k))P_j(log(Au/k)),

where P_j is a polynomial independent of A,k,u. Apply (3) with z=Au and a polynomial majorant for P_j. It yields the pointwise bound

Σ_{k≥1} X_k^(−1)|a_k^(j)(u)|≤C_j(A/N)u^(−j).             (4)

All sums here consist of nonnegative quantities; subsequent integration uses Tonelli.

### The stationary part

Under L141's smooth change of variable on the fixed support of χ, let

g_k(v)=χ(u(v))a_k(u(v))du/dv,

extended by zero to R. Its support is fixed and compact, g_k(0)=a_k(1), and every derivative through order four is a finite linear combination of a_k^(j)(u(v)), j≤4, with fixed smooth bounded coefficients. On this support u is bounded above and bounded away from zero. Consequently (4) gives

Σ_{k≥1}X_k^(−1)(||g_k||_1+||g_k^(4)||_1)≤C A/N.          (5)

The regularized Gaussian Fourier calculation proved in L141 gives, for each k, an error from replacing the stationary integral by

exp(−iτ−iπ/4)sqrt(2π/τ)a_k(1)

bounded by C τ^(−3/2)(||g_k||_1+||g_k^(4)||_1). Specifically its Fourier moment ∫ξ²|ĝ_k(ξ)|dξ has this bound by splitting at |ξ|=1 and integrating by parts four times on the outer region. Thus (5) bounds the absolute summed stationary errors in (2) by C(A/N)τ^(−3/2). No uniform compact range of r_k has been assumed.

### The nonstationary part

Put b_k=(1−χ)a_k and q=1/φ'=u/(1−u) away from 1. All products involving b_k are defined as zero on the neighborhood of 1 where it vanishes. For D b=(qb)', direct differentiation gives

D²b=q²b''+3qq'b'+((q')²+qq'')b.                           (6)

For each fixed k and t, the log Gaussian and its derivatives vanish faster than every required power at both endpoints. Hence b_k q and (Db_k)q vanish at zero and infinity, D²b_k is integrable, and the two integrations by parts in L141 are valid:

∫₀^∞ b_k exp(iτφ)du=(iτ)^(−2)∫₀^∞ D²b_k exp(iτφ)du.     (7)

We need an integrated summed bound, not just this per-mode assertion. Near zero, χ=0 and q=O(u), q'=O(1), q''=O(1). In (6), equation (4) bounds the weighted sums of the three terms respectively by O(A/N), O(A/N), and O(A/N). Near infinity, χ=0 and q=O(1), q'=O(u^(−2)), q''=O(u^(−3)); the corresponding bounds are O((A/N)u^(−2)), O((A/N)u^(−3)), and O((A/N)u^(−3)). On the remaining compact region outside the removed neighborhood of 1, all coefficients and cutoff derivatives are bounded, and (4) applies to the product derivatives of b_k. Therefore Tonelli and these integrable majorants prove

Σ_{k≥1}X_k^(−1)||D²b_k||_1≤C A/N.                       (8)

Equation (7) contributes at most C(A/N)τ^(−2) to the absolute summed errors. Together with the stationary estimate and |X_k^(iτ)|=1, this gives

Σ_{k≥1}|I_k−M_k|≤C(A/N)(τ^(−3/2)+τ^(−2)).                (9)

Since τ≥t/2 and A/N≤1 for t≥π, (1) follows. Finally (3) with z=A shows

Σ_{k≥1}|M_k|≤C sqrt(2π/τ)(NA)^(−1)A²
             =O((A/N)τ^(−1/2)),

proving absolute convergence of the leading-term series. ∎

## Scope, verification

This extends the expansion to every positive mode, with absolute summation of remainders justified by explicit nonnegative bounds. The absolute leading mass is only bounded above by O(t^(−1/2)); the complex leading sum has no lower bound here. Positive-mode cancellation, the theta center lower bound, a common heat-interval strip, and RH remain unresolved.

Analytic verification checks the lattice estimate for z<1 and z≥1, derivative scaling, compact coordinate derivative norms, the operator identity (6), both endpoint orders, individual integration-by-parts boundary terms, and Tonelli before summing remainders. No numerical certificate is needed. L140 supplies the mode definitions; L141 supplies the fixed cutoff, coordinate, and Fourier error argument. No unproved cancellation premise is used.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
