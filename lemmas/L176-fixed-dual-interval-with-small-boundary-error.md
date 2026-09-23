# Lemma 176: fixed dual interval with small boundary error

**Hypotheses.** Use T, N, h, B, E_B, a, e and D_T from L175. Define

Q_T(t)=Σ_(N≤k≤2N) (sqrt(a)/k)e(−a log(k/N)),

where k is an integer and endpoints are closed.

**Conclusion.** As T tends to infinity,

E_B|D_T−Q_T|²=O(sqrt(N)),
E_B|D_T−Q_T|=O(N^(1/4))=o(sqrt(N)).                 (1)

In particular |E_B|D_T|−E_B|Q_T||=O(N^(1/4)). Together with L175,
the full primal endpoint has first absolute moment o(sqrt(N)) if and
only if Q_T does. The amplitude sqrt(a)/k is retained exactly. This
proves a replacement estimate, not the asserted decay for either sum.

**Proof.**

Set δ=2N²−a. Since T=2πN² and t lies in [2T−h,2T],

δ=(2T−t)/(2π)+1/4,     1/4≤δ≤h/(2π)+1/4.

Thus the moving endpoints are N−δ/(2N) and 2N−δ/N.
Let W=(h/(2π)+1/4)/N. Then W=O(sqrt(N)) and W<N/2 for
large N, since h is comparable to N^(3/2). Define the two strips

S_−(t)=Σ_(a/(2N)≤k<N) (sqrt(a)/k)e(−a log(k/N)),
S_+(t)=Σ_(a/N<k≤2N) (sqrt(a)/k)e(−a log(k/N)).

The exact identity D_T−Q_T=S_−−S_+ follows from the overlap of
the intervals. It includes integral N or 2N: the lower strip excludes N,
and the upper strip excludes its moving left endpoint. Each strip is
contained in a fixed real interval of length at most W, respectively
[N−W/2,N) and (2N−W,2N]. Each contains at most K=ceil(W)+2
integers, all in [N/2,2N].

We bound either strip S by expanding its finite square. For an integer
k in its fixed supporting interval, its indicator is a threshold in t:
for S_− it is a(t)≤2Nk; for S_+ it is a(t)<Nk. Since a is increasing,
the product of any two such indicators restricts t to an interval J
(possibly empty) inside B. Strict endpoints change no integral.
The coefficient in a square term is b_(kl)(t)=a(t)/(kl). On B it
is positive, bounded by an absolute constant and monotone increasing,
so its total variation on every J is bounded by an absolute constant.
For k≠l the phase of this term is

exp(−i(t−π/2)log(k/l)).

Integration by parts on J therefore gives

|∫_J b_(kl)(t)exp(−i(t−π/2)log(k/l))dt|
 ≤ (2 sup_J b_(kl)+Var_J b_(kl))/|log(k/l)|
 ≤ C N/|k−l|.

Here the mean value theorem and k,l≤2N give
|log(k/l)|≥|k−l|/(2N). This argument accounts for the moving
cutoffs through J and does not differentiate an indicator as a smooth
function. A diagonal term contributes at most a constant after division
by h. For each positive integer difference d there are at most K pairs;
all differences are at most K. Summing both orders yields

E_B|S|²≤C[K+(NK/h)Σ_(1≤d≤K)1/d]
       ≤C[K+NK log(2K)/h].                                  (2)

Since K=O(sqrt(N)) and h is comparable to N^(3/2), the right side
is O(sqrt(N)+log(2N))=O(sqrt(N)). Apply
|S_−−S_+|²≤2|S_−|²+2|S_+|² to prove the first assertion in (1).
Cauchy–Schwarz for normalized integration proves its second assertion;
the reverse triangle inequality proves the comparison of absolute
moments. Finally apply L175's O(log(2N)) first-moment comparison.
Both errors are o(sqrt(N)), proving the equivalence. ∎

## Scope, verification

The proof controls both boundary strips, including all endpoint crossings,
without a pointwise small-error claim. It applies to the full endpoint;
a uniform assertion for all primal truncations has not been proved here.
No complete-sum first-moment decay, uniform integrability, cutoff covariance
or RH follows from this replacement alone.

Verification is analytic: the exact δ formula, interval subtraction,
strict endpoints, pairwise threshold intersections, amplitude variation,
frequency separation and normalized harmonic sum have all been checked.
No numerical certificate is used.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
