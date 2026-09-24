# Lemma 139: absolute series mass and dominance obstruction

**Hypotheses.** Let S(t) be the explicit series in L138, for real t>0. Put N=sqrt(t/(2π)), c₀=exp(π²/16), and write S(t)=Σ a_n(t) using exactly the summands in that lemma. Let M(t)=Σ |a_n(t)|.

**Conclusion.** As t tends to positive infinity,

M(t)=c₀ sqrt(π) exp(1/4)/N+O(N^(-2)),                     (1)

with the explicit error bound 2c₀e/N². Every term satisfies

|a_n(t)|≤c₀e/N².                                        (2)

Consequently |S(t)|=O(t^(-1/2)). In particular, no bound |S(t)|≥d t^(-δ) with fixed d>0 and δ<1/2 can hold for all sufficiently large t. This does not exclude any such lower bound with 1/2≤δ<1, which would still dominate L138's O(1/t) remainder.

More precisely, for any family of finite subsets A(t) of the positive integers with cardinality k(t)=o(N),

Σ_{n∈A(t)}|a_n(t)|/M(t) → 0.                             (3)

Thus isolating o(sqrt(t)) terms and bounding the entire complementary sum by its absolute term mass cannot prove a positive lower bound for |S(t)|, even if the isolated sum is evaluated exactly. This is an obstruction to that particular triangle-inequality argument, not an obstruction to a lower bound using cancellation in the complement.

**Proof.**

The real part of the square in L138's exponential gives

|a_n(t)|=c₀ f_N(n),   f_N(x)=x^(-2) exp(-(log(x/N))²), x>0.

Set f_N(0)=0. This extension is continuously differentiable at zero, and f_N and its derivative decay at infinity sufficiently for the following integrals. Indeed, on writing y=log(x/N),

f_N(x)=N^(-2) exp(1-(y+1)²).

It increases from zero to e/N² at x=N/e and then decreases to zero. Therefore

∫₀^∞ |f_N'(x)| dx=2e/N².                                (4)

The substitution x=N exp(y), dx=N exp(y)dy gives

∫₀^∞ f_N(x)dx=N^(-1)∫_R exp(-y²-y)dy
                  =sqrt(π) exp(1/4)/N.                  (5)

The Gaussian integral in the last equality follows by completing the square.

For each integer n≥1, the fundamental theorem of calculus bounds

|f_N(n)-∫_{n-1}^n f_N(x)dx|
 ≤∫_{n-1}^n |f_N(n)-f_N(x)|dx
 ≤∫_{n-1}^n |f_N'(u)|du.

Sum up to a finite integer m and pass to infinity. The integrable derivative makes the total error absolutely summable, and (5) is finite. This proves convergence of the series and bounds its discrepancy from (5) by (4). Multiplying by c₀ proves (1); the maximum calculation proves (2). The triangle inequality now gives the claimed upper bound for |S|. If δ<1/2, then t^δ |S(t)| tends to zero, contradicting a fixed positive d.

For an arbitrary finite A(t), (2) bounds its mass by c₀e k(t)/N². Divide by (1), whose leading constant is positive, to obtain (3). Denote that selected mass by B(t), and its actual complex sum by P(t). The proposed reverse triangle estimate is

|S(t)|≥|P(t)|-(M(t)-B(t)).

Its right side is at most 2B(t)-M(t), which is strictly negative for all sufficiently large t when k(t)=o(N). This proves the stated obstruction even for a t-dependent, optimally selected collection of terms. It does not estimate the actual modulus of the complementary complex sum. ∎

## Scope, verification

The absolute mass is of order t^(-1/2), while the largest term is at most of order t^(-1), the same order as L138's available additive remainder. These facts do not imply that |S| is of either order: cancellation remains unestimated. No zero or small-value sequence for S has been proved here, and no lower bound for the theta center or RH follows.

Analytic verification consists of the exact modulus identity, completing the square in the integral and maximum, the integrable-variation quadrature estimate, and the subset triangle bound. No numerical certificate is needed. No interchange of oscillatory limits is used.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
