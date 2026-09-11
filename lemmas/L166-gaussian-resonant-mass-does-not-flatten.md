# Lemma 166: Gaussian resonant mass does not flatten on a dyadic interval

**Hypotheses.** Use the Gaussian amplitudes and excluded-pair mass W of
L165 in I=[N,2N], N=sqrt(T/(2π)), with T sufficiently large. Put
E_T f=T^(−1)∫_T^(2T)f(t)dt and bar W=E_T W. For the cutoff question,
let Q=|G_T|² as in L155 and let χ be C², constant zero below 1 and
constant one above 2. Fix M>0 and put h_T=χ''(Q/M).

**Conclusion.** There are constants c,C>0 independent of T such that

c (log T)^4 ≤ E_T|W−bar W| ≤ C (log T)^4.                (1)

In particular neither absolute nor relative L1 flattening occurs.
The exact replacement error is

E_T[h_T W]−bar W E_T h_T
 =bar W E_T[h_T(W/bar W−1)].                            (2)

It is o(1) if and only if the last normalized correlation is
 o((log T)^(−4)). Explicit amplitude variation alone gives an
O_χ((log T)^4) absolute bound, not the required decay. In fact

sup_(measurable |h|≤1) |E_T[h(W−bar W)]|
 =E_T|W−bar W| ≍ (log T)^4.                             (3)

This does not decide (2) for the particular h_T; that signed correlation
remains unproved.

**Proof.**

Let v=log(t/T) and x_j=n_j/N for the six indices of an allowed sextuple.
L165's Gaussian formula gives the exact ratio of each amplitude to its
value at T as exp(v log x_j−v²/4). Consequently

W(Te^v)/W(T)=exp(−3v²/2) Σ_α p_α exp(v L_α),            (4)

where p_α is the positive six-amplitude product at T divided by W(T),
Σ_α p_α=1, and L_α=Σ_(j=1)^6 log x_j∈[0,B], B=6 log 2.
There are finitely many allowed sextuples. L165 ensures W(T)>0.

We prove a uniform statement for every finite probability mixture in
(4), independent of its arithmetic origin. Write its profile as
f(u)=exp(−3(log u)²/2)Σ p_α exp(L_α log u), 1≤u≤2,
and μ_f=∫_1^2 f(u)du. There exists c_B>0 such that

∫_1^2 |f(u)−μ_f|du ≥ c_B.                              (5)

Suppose instead that a sequence of mixtures makes this integral tend
to zero. Its moments m_k=Σ p_α L_α^k satisfy m_0=1 and
0≤m_k≤B^k. Repeated Bolzano–Weierstrass selection followed by a
diagonal subsequence makes every moment converge to a_k. The entire
functions g(z)=Σ p_α exp(L_α z)=Σ_(k≥0)m_k z^k/k!
then converge uniformly on every compact complex disk to
G(z)=Σ_(k≥0)a_k z^k/k!: the series tails are uniformly bounded
by the tails of exp(B|z|), and each finite initial sum converges.
In particular f converges uniformly on [1,2] to
F(u)=exp(−3(log u)²/2)G(log u).

The assumed vanishing integrals imply ∫|F−∫F|=0. Continuity
makes F constant everywhere, and F(1)=a_0=1 makes that constant 1.
Hence G(v)=exp(3v²/2) for real 0≤v≤log 2. The identity theorem
for entire functions extends the equality to all complex v. But for
positive real v the moment bound gives |G(v)|≤exp(Bv), contradicting
exp(3v²/2)>exp(Bv) for v>2B/3. This proves (5).

Also on [1,2],

exp(−3(log 2)²/2) ≤ f(u) ≤ exp(B log 2).

Thus μ_f is bounded above and bounded away from zero uniformly, and
∫|f−μ_f|≤2 exp(B log 2). With t=Tu, (4) and (5) give

c_B W(T)≤E_T|W−bar W|≤2 exp(B log 2) W(T).

L165 supplies W(T)≍(log T)^4, proving (1), and the profile bounds
also give bar W≍(log T)^4. Formula (2) is finite integral algebra;
these two-sided bounds establish its stated little-o equivalence.
Since χ'' is continuous and zero outside [1,2], it is bounded, so
|E_T[h_T(W−bar W)]|≤||χ''||∞ E_T|W−bar W|.
Finally the upper bound in (3) is the triangle inequality, and equality
is attained by the measurable real function sign(W−bar W). This test
function is not asserted to be realizable as χ''(Q/M).

For comparison, differentiation of (4) gives
|W'(t)|≤(B+3 log 2)W(t)/t on [T,2T]. The pointwise factor 1/t
integrates over an interval of length T and therefore supplies only
O(W(T)) total variation. It does not contradict the lower bound (1). ∎

## Scope, verification, and formalization obligations

This resolves the amplitude-flattening route negatively, not the actual
cutoff replacement. The supremum in (3) permits T-dependent arbitrary
bounded tests, whereas h_T has a prescribed relation to Q and a fixed
cutoff. Cancellation using that relation could still make (2) o(1).
No tail estimate, nonvanishing result, or RH proof follows.

Verification is analytic: the six Gaussian exponent differences, the
probability normalization, the bounded moment subsequence, uniform
entire-series tails, the identity theorem, and the change of variables
t=Tu. No numerical computation is needed or claimed to prove (5).
Formalization would require these statements, elementary sequential
compactness of bounded real sequences, and the exact covariance identity.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
