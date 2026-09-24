# Lemma 291: refined strip envelope obstruction

**Hypotheses.** Use the theta kernel k, shifted integrand F, and parameters a,n,r,h,τ,δ,Φ_* of L269. Let a tend to positive infinity with n≥1 integer and h in a fixed compact interval [h₀,h₁] contained in (5,∞). In particular

n=r(h−9/2),  δ=(h/(2π))exp(−2r),
a=2πexp(2r)(1+h²/a²)^(−1/2).

For real y set q_y=πδexp(2|y|), and define the positive majorant without its constant multiplier by

U(s,x)=|s|^(2n)exp(−2aτ)
 · exp((9/2)(|s+x|+|s−x|))exp(−q_(s+x)−q_(s−x))
 · (1+q_(s+x)^(−5/2))(1+q_(s−x)^(−5/2)).

Let B_r={s=r/2+u, x=r/2+v: 0≤u≤1, 2≤v≤3}. Define H_*=9/2+5/(4 log 2).

**Conclusion.** The retained theta-series estimate gives |F|≤C U. There are constants c,C>0, uniform in the specified h-band, such that

c exp([5/2−2(h−9/2)log 2]r)
 ≤ (a/exp(Φ_*))∫_(B_r)U(s,x) ds dx
 ≤ C exp([5/2−2(h−9/2)log 2]r).

The box is strictly inside the mixed-sign argument sector |x|>|s| for sufficiently large r. Thus the integral of U over the complement of the positive-positive sector and its s-reflection cannot be o(exp(Φ_*)/a) when 5<h≤H_*. This failure also applies to every fixed positive sector cutoff. It concerns this majorant only: no lower bound on |F| or its signed integral, and no negative Laguerre sign, is asserted. No sufficiency for h>H_* is claimed.

**Proof.** L269 proves directly from the theta series, before replacing its argument-dependent factor by δ^(−5/2), that

|k(y±iτ)|≤C exp(9|y|/2)exp(−q_y)(1+q_y^(−5/2)).

Evenness and conjugation justify the same estimate for negative y. Multiplication and the contour multiplier prove |F|≤C U.

On B_r, s+x=r+u+v and s−x=u−v<0. Hence

|s+x|+|s−x|=r+2v,
q_(s+x)=(h/2)exp(2(u+v)),
q_(s−x)=(h/2)exp(−2r+2(v−u)).

The first q lies in a fixed positive compact interval depending only on h₀,h₁; the second is between positive constant multiples of exp(−2r). Consequently exp(−q_(s+x)−q_(s−x)) and 1+q_(s+x)^(−5/2) are bounded above and below by positive constants, whereas 1+q_(s−x)^(−5/2) is between positive constant multiples of exp(5r). These constants need not be numerically small; they are independent of a,n,u,v in the stated ranges.

Writing b=h−9/2, uniformly for 0≤u≤1,

2n log(s/r)=2rb log(1/2+u/r)
           =−2rb log 2+4bu+O(1/r).

The identity Φ_*=2n log r+9r−h−2aτ therefore gives the pointwise two-sided comparison on this unit-area box

U(s,x)/exp(Φ_*) ≍ exp([1/2−2b log 2]r).

Here the bounded terms include 9v+h+4bu+O(1/r); the coefficient 1/2 is exactly 9/2+5−9. Integrating and using a≍exp(2r) proves the displayed conclusion. The parameter identities also show r→∞, so all uniform estimates apply.

Since x−s=v−u≥1 and s>0, the box lies strictly in |x|>|s|. The two kernel real arguments have opposite signs there. It is consequently outside both same-sign sectors, regardless of any fixed positive cutoff on their arguments. If h≤H_*, the exponent 5/2−2(h−9/2)log 2 is nonnegative, so the normalized integral is bounded below by c>0. For a fixed limiting h<H_* it even diverges exponentially in r. Positivity of U extends this lower bound to any complement containing B_r. An upper certificate obtained by integrating U thus cannot yield the required little-o estimate in that range. This does not reverse the inequality |F|≤C U or preclude cancellation in F. ∎

**Mathlib.** Full statement: not checked. Supporting theta-series estimates, logarithm expansions, and integral comparisons: not checked. No full or supporting library match is claimed. The retained theta estimate and parameter definitions are supplied by L269; the box computation and the obstruction for this majorant are proved here.
