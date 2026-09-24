# Lemma 247: complete monotonicity does not force real zeros

**Hypotheses.** Use the functions P and F and a=10+i/4 from L029. For H=P or H=F define A_H(x)=H(i√x), by its entire power series, and G_H=A_H′/A_H for x≥0. Complete monotonicity here means (-1)^k G_H^(k)(x)≥0 for every integer k≥0 and every x≥0, with right derivatives at zero.

**Conclusion.** Both G_P and G_F are strictly completely monotone, although both original entire functions have nonreal zeros. Neither G has a positive Stieltjes representation G(x)=∫_[0,∞)(x+s)^(−1)dν(s) with ∫(1+s)^(−1)dν(s)<∞. Thus even all translated scalar reciprocal-power signs do not imply the positive Stieltjes representation needed for mixed positivity. No positive Fourier-kernel representation for these examples is asserted.

**Proof.** Write A=1599/16, so a²=A+5i. Direct differentiation gives

G_P(x)=1/(x+25)+1/(x+A+5i)+1/(x+A−5i)
       =∫₀∞ e^(−xt) h_P(t)dt,

h_P(t)=e^(−25t)+2e^(−At)cos(5t).

The elementary exponential integrals converge absolutely for x≥0. We show h_P(t)>0 for every t≥0. If 0≤t≤1/5, then cos(5t)≥cos(1)>0. If t≥1/5, then

h_P(t)≥e^(−25t)[1−2e^(−(A−25)t)]
       ≥e^(−25t)[1−2e^(−1199/80)]>0.

The last inequality needs no decimal computation: 1199/80>1 and e>2. Every polynomial moment of |h_P| is integrable, so differentiating under the integral gives

(-1)^k G_P^(k)(x)=∫₀∞t^k e^(−xt)h_P(t)dt>0.

For the cosine factor put λ_n=10000π²(n+1/2)², n≥0. Euler's cosine product, after substitution z=i√x, is

cosh(√x/100)=Π_(n≥0)(1+x/λ_n).

Since Σ λ_n^(−1)<∞, logarithms of the tail converge uniformly on every compact complex set avoiding the finitely many head zeros, and their derivative series converge locally uniformly there. Consequently

G_F(x)=G_P(x)+Σ_(n≥0)1/(x+λ_n)
      =∫₀∞e^(−xt)[h_P(t)+Σ_(n≥0)e^(−λ_n t)]dt.

For t>0 the density sum converges by λ_n growing quadratically. Tonelli applies to this nonnegative sum; its t^k moment is k! Σ λ_n^(−k−1)<∞ for every k≥0. These bounds justify differentiation at every x≥0, including zero, and prove strict complete monotonicity of G_F. They also justify all translated scalar identities (-1)^k G_H^(k)(x)/k!=Σ_α(x+α²)^(−k−1), with one α per paired zero as in L029.

To exclude a positive Stieltjes representation, suppose one existed. Its integral defines a holomorphic function on D=C\(−∞,0]: on each compact subset of D, |z+s|≥c(1+s) for some c>0 uniformly in s≥0. The same bound, or local Cauchy estimates, justifies holomorphy under the integrable weight (1+s)^(−1). In contrast, the explicit G_P has a simple pole of residue 1 at z=−a², which lies in D. The same is true of G_F: the cosine logarithmic derivative has poles only at the negative real numbers −λ_n and is analytic at −a². The identity theorem on D with the two nonreal poles removed (a connected domain) would equate the integral to G_H there, contradicting its holomorphy at −a². This proves the claimed failure of the representation. L029 supplies the stated nonreal zeros and the retained entire-function properties. ∎

This is a generic obstruction, not a statement that actual theta G is completely monotone or fails a Stieltjes representation. The achieved property is all orders and all x≥0, not merely finitely many signs. The missing stronger threshold is positivity of mixed forms, which requires additional information beyond those scalar signs.

**Mathlib.** Not checked: coverage of the full counterexample, Euler's cosine product, holomorphy of Stieltjes integrals, and differentiation under these integrals was not checked. No matching or supporting theorem name in Mathlib is asserted. Reference portal: https://leanprover-community.github.io/mathlib4_docs/
