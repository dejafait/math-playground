# Lemma 169: freezing Gaussian coefficients in cutoff blocks

**Hypotheses.** Use the amplitudes A_n, frequencies λ_n=log(n/N),
and Q from L156, on the fixed integer window I=[N,2N],
N=sqrt(T/(2π)). Use W and bar W from L166. Let T be sufficiently
large, L=log T, M>0, and χ∈C³(R) be real, zero on (−∞,1]
and one on [2,∞). Partition [T,2T] as in L168 into J=ceil(T/H)
equal blocks B_j of length h=T/J, with 1≤H≤T. Let c_j be the
midpoint, E_j normalized block integration, and W_j=E_j W. Define

S(t)=Σ_(n∈I) A_n(t) exp(i(t−π/2)λ_n),
S_j⁰(t)=Σ_(n∈I) A_n(c_j) exp(i(t−π/2)λ_n),
Q_j⁰(t)=|S_j⁰(t)|²,
f_j=E_j χ''(Q/M),    f_j⁰=E_j χ''(Q_j⁰/M),
K=1+sqrt(T)log T/h.

**Conclusion.** Uniformly in j,

E_j|S−S_j⁰|² ≤ C(h/T)² K,
E_j|Q−Q_j⁰| ≤ C(h/T)K,
|f_j−f_j⁰| ≤ C_χ hK/(TM).                              (1)

Consequently the error in the weighted block sum satisfies

|(1/J)Σ_j (W_j−bar W)(f_j−f_j⁰)|
 ≤ C_χ L⁴ hK/(TM).                                     (2)

The full covariance therefore obeys

E_T[χ''(Q/M)(W−bar W)]
 = (1/J)Σ_j (W_j−bar W)f_j⁰
   + O_χ(L⁴[h/T+hK/(TM)]).                             (3)

For H=T^(3/4), the remainder is
O_χ((1+1/M)T^(−1/4)(log T)^4), hence o(1) for fixed M.
Thus at fixed M the actual covariance is o(1) if and only if the
frozen weighted block sum in (3) is o(1). The latter remains unproved.

**Proof.**

All sums have the same finite index set. L156 gives
|A_n|≤CT^(−1/4), |A_n'|≤CT^(−5/4), and
Σ_(m≠n) |log(m/n)|^(−1)≤CN²log(2N).
For t∈B_j set d_n(t)=A_n(t)−A_n(c_j). The fundamental theorem
of calculus and |t−c_j|≤h/2 give

|d_n|≤ChT^(−5/4),    |d_n'|≤CT^(−5/4).

The diagonal contribution to E_j|S−S_j⁰|² is at most
CN h²T^(−5/2)≤C h²/T². For m≠n put p=d_m d_n and
ω=λ_m−λ_n=log(m/n). Then

sup_(B_j)|p|≤Ch²T^(−5/2),
∫_(B_j)|p'|≤∫_(B_j)(|d_m'||d_n|+|d_m||d_n'|)
 ≤Ch²T^(−5/2).

Integration by parts bounds the absolute value of
∫_(B_j) p exp(i(t−π/2)ω)dt by
(2 sup|p|+∫|p'|)/|ω|. This includes both block endpoints.
Summing over all ordered off-diagonal pairs and dividing by h gives

C h T^(−5/2) N²log(2N)
 ≤ C h T^(−3/2)log T
 = C(h/T)² sqrt(T)log T/h.

Together with the diagonal this proves the first bound in (1).

The same calculation for S uses sup|A_m A_n|≤CT^(−1/2)
and ∫_(B_j)|(A_m A_n)'|≤ChT^(−3/2)≤CT^(−1/2).
Its diagonal is O(1), giving E_j|S|²≤CK. For S_j⁰ the
coefficients are constant, so the product derivative vanishes;
the identical endpoint bound gives E_j|S_j⁰|²≤CK.
The elementary inequality

||S|²−|S_j⁰|²|≤|S−S_j⁰|(|S|+|S_j⁰|)

and normalized Cauchy–Schwarz now give
E_j|Q−Q_j⁰|≤C(h/T)K. Since χ''' is bounded (it vanishes
outside [1,2]), χ'' is globally Lipschitz with constant ||χ'''||∞.
Applying this bound with arguments Q/M and Q_j⁰/M proves the
last assertion in (1). No monotonicity of χ'' is assumed.

L166 supplies |W_j−bar W|≤CL⁴. The triangle inequality in the
normalized block sum proves (2). L168 gives the exact block
covariance decomposition with remainder O_χ(HL⁴/T). Since
H/2≤h≤H, this is O_χ(hL⁴/T), proving (3).

For H=T^(3/4), h lies between T^(3/4)/2 and T^(3/4), so
K=1+O(T^(−1/4)log T)=O(1). Substitution yields the displayed
remainder, which tends to zero for every fixed M>0. Subtracting
this remainder proves the equivalence. ∎

## Scope, verification

Freezing preserves the time-dependent phases, their arithmetic
relations, and the block location. It supplies no common value for the
f_j⁰ and no independence from W_j. The result controls only the error
of coefficient freezing; it proves neither the signed frozen estimate,
a tail theorem, nor RH. The explicit 1/M factor must be retained if M
is allowed to vary with T.

Verification is analytic: midpoint derivative bounds, the two product
rule terms, both integration endpoints, the ordered frequency sum,
division by h, normalized Cauchy–Schwarz, the cutoff Lipschitz bound,
and equal-block normalization are all exhibited above. No numerical
certificate is required.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
