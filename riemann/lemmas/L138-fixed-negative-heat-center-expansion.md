# Lemma 138: fixed negative-heat center expansion

**Hypotheses.** Let F be the theta heat deformation of L058, with the normalization of L137. Fix the negative heat parameter λ=−1. For real t>0 put

H(t)=((2−it)(1−it)/2)π^(−(2−it)/2)Γ(1−it/2),
ℓ(t)=½log(t/(2π)),
S(t)=Σ_{n≥1}n^(−2+it)exp((−π/4+i(log n−ℓ(t)))²).

**Conclusion.** The series is absolutely convergent, and there are constants C,T>0 such that for t≥T,

F(−1,t+3i/2)=H(t)(S(t)+E(t)),   |E(t)|≤C/t.                 (1)

For the absolute mass A_1 and cancellation factor q_1 defined in L137, there are constants 0<c<C' such that

c≤A_1(t+3i/2)/|H(t)|≤C'.                                  (2)

Consequently q_1(t+3i/2)=|S(t)+E(t)|/D(t), with c≤D(t)≤C'. This is an additive expansion, not a relative asymptotic or a lower bound. In particular, a bound |S(t)|≥d t^(−δ) for all sufficiently large t with d>0 and δ<1 would imply a polynomial lower bound for q_1. Such a bound for S is not proved here. No common zero strip or estimate on a heat interval is asserted.

**Proof.**

The completion and reflection identities used in L136 give, for every real u,

F(0,u+3i/2)=H(u)ζ(2−iu).

Here H extends by the displayed formula to all real u. Stirling as recorded in foundations/notation-and-inputs.md gives

|H(u)| asymp |u|^(5/2)exp(−π|u|/4)   (|u|≥1),             (3)

where both bounding constants are positive. Also 1/ζ(2)≤|ζ(2−iu)|≤ζ(2), by the reciprocal estimate in L136.

We first record a complex, rather than modulus-only, Stirling estimate. Set b(t)=−π/4−iℓ(t). Uniformly for real |v|≤t^(1/4),

H(t+v)/H(t)=exp(b(t)v)(1+O((1+v²)/t)).                    (4)

Here and below constants do not depend on t,v. To verify this without differentiating an unspecified error term, use complex Stirling in logarithmic form at w(u)=1−iu/2:

log Γ(w)=(w−½)Log w−w+½log(2π)+O(1/|w|).

A consistent logarithm exists along the relevant segment, which lies in the right half-plane and in a fixed sector away from the negative real axis. Include in the leading expression the two polynomial-factor logarithms and −(2−iu)log π/2. Call the resulting expression P(u). Direct differentiation gives

P'(t)=−π/4−(i/2)log(t/(2π))+O(1/t),
P''(u)=O(1/t) for |u−t|≤t^(1/4).

Indeed the gamma leading term has derivative (−i/2)(Log w−1/(2w)); the polynomial logarithms have derivatives O(1/t), and Log(1−it/2)=log(t/2)−iπ/2+O(1/t). Taylor's theorem along the real segment gives P(t+v)−P(t)=b(t)v+O((|v|+v²)/t). Subtracting the two Stirling remainders costs O(1/t). The resulting exponent error tends uniformly to zero on this segment, so exponentiating proves (4).

Write g(v)=(4π)^(-1/2)exp(−v²/4). By L137 the left side of (1), divided by H(t), is

∫_R g(v) [H(t+v)/H(t)] ζ(2−i(t+v))dv.                   (5)

Replacing the H ratio by exp(b(t)v) on |v|≤t^(1/4) changes (5) by at most

(C/t)∫_R g(v)exp(−πv/4)(1+v²)ζ(2)dv=O(1/t).            (6)

All remaining tails are negligible at this scale. Here are bounds that avoid applying a local expansion at an unbounded shift. On t^(1/4)<|v|≤t/2, (3) implies

|H(t+v)/H(t)|≤C exp(π|v|/4),

since t/2≤t+v≤3t/2. The integral of g(v) times this bound is O(exp(−c₀sqrt(t))) for some c₀>0. On |v|>t/2, L137's horizontal-strip bound |F(0,t+v+3i/2)|≤T_(3/2), together with (3), bounds the tail of (5) by

C t^(−5/2)exp(πt/4) ∫_{|v|>t/2}g(v)dv
 ≤ C t^(−5/2)exp(πt/4−t²/32),

for sufficiently large t. This is O(1/t). The tail of the replacement integrand exp(b(t)v)ζ(2−i(t+v)) outside |v|≤t^(1/4) is likewise O(exp(−c₀sqrt(t))), by its absolute bound ζ(2)exp(π|v|/4). Thus (5) equals

∫_R g(v)exp(b(t)v)ζ(2−i(t+v))dv+O(1/t).                 (7)

Expand ζ on Re s=2. The double sum/integral of absolute values is bounded by ζ(2)∫g(v)exp(−πv/4)dv<∞. Fubini therefore applies. For every complex d,

∫_R g(v)exp(dv)dv=exp(d²).

For real d this follows by completing the square; for complex d it follows by the identity theorem, since the Gaussian dominates uniformly on compact d sets. Applying this with d=b(t)+i log n proves that (7) equals S(t)+O(1/t). Absolute convergence of S follows also from

|exp((−π/4+i(log n−ℓ))²)|=exp(π²/16−(log n−ℓ)²)≤exp(π²/16).

To prove (2), use the same middle and far tail estimates on the absolute integrand. On |v|≤t/2, (3) bounds that integrand, after division by |H(t)|, by Cg(v)exp(π|v|/4); the far tail tends to zero. This proves the upper bound. For the lower bound restrict to |v|≤1. Equation (4) gives |H(t+v)/H(t)|≥½exp(−πv/4) for all sufficiently large t, while |ζ(2−i(t+v))|≥1/ζ(2). Integration on this fixed interval gives a strictly positive constant. The definition of q_1 now gives the exact claimed quotient. If the stated additional bound for S held with δ<1, then C/t≤(d/2)t^(−δ) eventually, and the reverse triangle inequality would give q_1≥(d/(2C'))t^(−δ). This implication does not establish its premise. ∎

## Scope and verification

The remaining cancellation is contained in an explicit t-dependent complex Dirichlet series. Absolute convergence and its termwise upper bounds supply no lower bound for its modulus. The additive error must not be divided by S without a proved lower estimate. Even this fixed-slice large-t expansion does not settle nonvanishing on the bounded portion of the center line, a heat-interval estimate, or RH.

Analytic validation covers the complex Stirling phase and logarithm branches, the uniform local error, all three Gaussian integration regions, absolute Fubini, the complex Gaussian identity, and the lower bound for the absolute mass. No numerical certificate is used or needed. The lower bound for S remains explicitly unproved.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
