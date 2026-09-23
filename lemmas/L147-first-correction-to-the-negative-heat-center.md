# Lemma 147: first correction to the negative-heat center

**Hypotheses.** Use F, H, ℓ, S, A_1 and q_1 of L138, with real t tending to positive infinity and heat parameter −1. Put

d_n(t)=−π/4+i(log n−ℓ(t)),
P(d)=5d−i(d²+1/2),
S_1(t)=Σ_{n≥1}n^(−2+it)exp(d_n(t)²)P(d_n(t)),
W(t)=S(t)+S_1(t)/t.

**Conclusion.** The correction series converges absolutely, and with a constant independent of t,

F(−1,t+3i/2)/H(t)=W(t)+O(t^(−2)).                         (1)

In particular, if for some d>0 and 0≤δ<2 one could prove |W(t)|≥d t^(−δ) for all sufficiently large t, then q_1(t+3i/2)≥c_d t^(−δ) there. This additional hypothesis is unproved. An unspecified lower bound of order t^(−2) would not suffice to dominate the remainder constant. No lower bound for W, center nonvanishing, common heat-interval strip, or RH is asserted.

**Proof.**

Write b(t)=−π/4−iℓ(t) and g(v)=exp(−v²/4)/(2sqrt(π)). We first prove, uniformly for real |v|≤h=t^(1/4),

H(t+v)/H(t)=exp(b(t)v)[1+a(v)/t+O((1+|v|⁴)/t²)],
a(v)=5v/2−iv²/4.                                        (2)

Here is a derivative justification for the Stirling error. Set w(u)=1−iu/2 and use analytic logarithms on disks of radius a fixed small multiple of t around positive real u with |u−t|≤h. Their w-images lie in a fixed closed sector away from the negative real axis, have modulus comparable to t, and avoid the poles and zero of the polynomial factors of H. Logarithmic complex Stirling from the foundations expresses log H(u)=P_0(u)+R(u), where

P_0(u)=log(2−iu)+log(1−iu)−log 2−(2−iu)log π/2
       +(w(u)−1/2)Log w(u)−w(u)+log(2π)/2,

and R is analytic with |R(u)|≤C/t throughout slightly larger disks of the same type. Such a branch of log Γ is the analytic branch of Stirling in the sector; additive branch constants disappear in differences. Cauchy's derivative estimate on these disks gives |R'(u)|≤C/t² along the real segment. Thus R(t+v)−R(t)=O(|v|/t²); we have not differentiated a bare real-variable big-O estimate.

Direct differentiation of the explicit P_0 gives

P_0'(t)=−i/(2−it)−i/(1−it)+(i/2)log π
         −(i/2)(Log w(t)−1/(2w(t)))
       =b(t)+5/(2t)+O(t^(−2)),
P_0''(t)=−i/(2t)+O(t^(−2)),
P_0'''(u)=O(t^(−2))  for |u−t|≤h.

For the first coefficient, Log w(t)=log(t/2)−iπ/2+2i/t+O(t^(−2)) and 1/(2w(t))=i/t+O(t^(−2)). The gamma contribution to the real 1/t coefficient is 1/2, and the two polynomial factors contribute 2. The latter two derivative estimates follow by differentiating the displayed rational and logarithmic expression for P_0', not its asymptotic error.

Taylor's theorem and the bound for R' now give

log H(t+v)−log H(t)=b(t)v+a(v)/t+r(t,v),
|r(t,v)|≤C(|v|+v²+|v|³)/t².

Both a(v)/t and r(t,v) tend uniformly to zero on this range. The elementary exponential remainder bound gives

|exp(a(v)/t+r(t,v))−1−a(v)/t|
 ≤C(|r(t,v)|+|a(v)/t|²)≤C(1+|v|⁴)/t²,

proving (2).

The normalized convolution identity used in L138 is

F(−1,t+3i/2)/H(t)=∫_R g(v)[H(t+v)/H(t)]ζ(2−i(t+v))dv.

Since |ζ(2−iu)|≤ζ(2), the local replacement (2) costs at most

C t^(−2)ζ(2)∫_R g(v)exp(−πv/4)(1+|v|⁴)dv=O(t^(−2)).

We specify why the tails remain negligible at this sharper scale. The estimates in L138 bound the original normalized integrand on h<|v|≤t/2 by Cg(v)exp(π|v|/4), and its integral is O(exp(−c sqrt(t))). On |v|>t/2 the original convolution tail is bounded by C t^(−5/2)exp(πt/4−t²/32). Both are O(t^(−2)). The replacement tail for |v|>h is bounded by

C∫_(|v|>h)g(v)exp(π|v|/4)(1+v²)dv=O(exp(−c' sqrt(t))),

for some c'>0, since t≥1. Consequently we may replace the ratio and extend the replacement integral to the whole line with total error O(t^(−2)).

Expanding ζ is justified by the absolute majorant

ζ(2)∫_R g(v)exp(−πv/4)(1+|a(v)|/t)dv<∞.

The complex Gaussian identity and its first two derivatives give

∫g(v)exp(dv)dv=exp(d²),
∫g(v)v exp(dv)dv=2d exp(d²),
∫g(v)v² exp(dv)dv=(2+4d²)exp(d²).

Differentiation is dominated uniformly on compact complex d sets by a polynomial times a Gaussian. The integral of a(v)exp(dv) is therefore exp(d²)[5d−i(d²+1/2)]. Applying these identities term by term with d=d_n(t) proves (1). Absolute convergence also follows directly: for d=−π/4+ix, the function |exp(d²)P(d)| is bounded on real x, so the correction terms are dominated by Cn^(−2), uniformly in t.

Finally L138 gives c≤D(t)=A_1(t+3i/2)/|H(t)|≤C. Equation (1) gives the exact relation q_1=|W+E_2|/D with |E_2|≤K/t². Under the stated additional hypothesis, K/t²≤(d/2)t^(−δ) eventually, and the reverse triangle inequality yields q_1≥d t^(−δ)/(2C). This proves only the conditional implication. ∎

## Qualifications and verification

The correction changes the quantity whose cancellation must be controlled: a lower bound for S alone needs an additional comparison with S_1/t. The remainder is additive, so division by W is not justified without a lower bound. The result concerns only the fixed heat slice and large positive t.

Analytic validation checks the analytic Stirling branch and Cauchy disks, all derivative coefficients, the uniform exponential remainder, both original tail regions, the polynomial replacement tail, absolute Fubini, and the two Gaussian moments. No numerical certificate is required. No cancellation hypothesis has been promoted to an established input.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
