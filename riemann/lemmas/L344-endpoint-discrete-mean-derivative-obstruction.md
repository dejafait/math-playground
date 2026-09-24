# Lemma 344: a derivative-certificate obstruction for the discrete endpoint mean

**Hypotheses.** For real r≥2 use the functions and constant C>0
from L333:

S_r(a)=Σ_(j,k≥1)(jk)^(−1/2)(1−log(jk)/(2r))_+^r exp(ia log(k/j)),
B_r(a)=|ζ(1+1/r+ia)|²,  R_r(a)=S_r(a)/B_r(a)−1,
M_r=C/r²+O(r^(−3)).

Here M_r is the long-height mean of |R_r|². The denominator is
nonzero. Let g_r(k,l) be L333's absolutely summable coefficients in

|R_r(a)|²=Σ_(k,l≥1)g_r(k,l)exp(ia log(k/l)).

For coprime positive integers p,q define the fully grouped coefficients

h_r(p,q)=Σ_(d≥1)g_r(dp,dq),  ω_(p,q)=log(p/q).

These real coefficients need not be nonnegative. For integer N≥1 put

a(x)=sqrt(4π²exp(8x)−25),  a_n=a(n),
D_N=(1/N)Σ_(n=N)^(2N−1)|R_(2n)(a_n)|²,
δ_N=exp(−2N).

The tested certificate first treats the distinct frequencies separately,
uses the standard classical or Heath-Brown fixed-order derivative
estimates on f_ω(x)=ω a(x)/(2π), caps them by the trivial bound,
then uses absolute Abel summation for the moving weights h_(2n)(p,q).
Any fixed finite collection of derivative orders and fixed derivative
comparison constants is allowed, as are partitions into consecutive
integer intervals. This specifies a method to test, not a hypothesis
about the actual cancellation.

**Conclusion.** Every equal-frequency collision can be retained before
the discrete average, giving the exact absolutely convergent identity

D_N=Δ_N+Σ_((p,q)=1,p≠q)(1/N)
          Σ_(n=N)^(2N−1)h_(2n)(p,q)exp(ia_n ω_(p,q)),
Δ_N=(1/N)Σ_(n=N)^(2N−1)M_(2n)
   =C/(8N²)+O(N^(−3)).                                  (1)

The very small nonzero frequencies are harmless in absolute mass:

(1/N)Σ_(n=N)^(2N−1)
 Σ_((p,q)=1,0<|ω_(p,q)|<δ_N)|h_(2n)(p,q)|
 ≤K N^17 exp(−2N).                                      (2)

The remaining absolute coefficient budget satisfies

A_N:=(1/N)Σ_(n=N)^(2N−1)
 Σ_((p,q)=1,|ω_(p,q)|≥δ_N)|h_(2n)(p,q)|
 ≥1−K/N−K N^17 exp(−2N).                                (3)

Here and below K can be enlarged to a fixed absolute constant. On
every frequency in (3), the tested derivative bounds are eventually
no better than the trivial bound, including on partial intervals.
The resulting absolute Abel certificate is at least A_N, even after
partitioning the n interval. Thus its liminf is at least one, against
the sufficient target D_N=o(1). It also cannot certify D_N<1/4.

This lower bound concerns an upper-bound certificate, not D_N or its
signed off-diagonal part. No positive lower bound for D_N, failure of
the discrete o(1) assertion, endpoint sign, or zero-exclusion extension
is asserted. The leading term in Δ_N does not by itself describe D_N.

**Proof.** We first record exactly which coefficient estimates are
available before sampling. L333 constructs real coefficients

c_r(m,n)=(mn)^(−σ)H_r(m,n),  σ=1+1/r,
|H_r(m,n)|≤(e+1)τ(m)τ(n),
g_r(k,l)=Σ_(v|k,u|l)c_r(u,v)c_r(k/v,l/u),

where τ is the divisor function. Absolute convergence permits the
product expansion in the hypotheses, and L333 proves

Σ_k g_r(k,k)=M_r,
Σ_(k≠l)|g_r(k,l)|/|log(k/l)|≤K(r+1)^17.                 (4)

For the second assertion its proof bounds |g_r(k,l)| by
(e+1)²d_4(k)d_4(l)/(kl)^σ and sums the inverse logarithmic gap.
It does not assume a minimum gap for infinitely many frequencies.
We use this proved bound, rather than infer it from a finite-interval
mean estimate by reversing an inequality.

Every positive rational k/l has a unique reduced form p/q. Absolute
convergence therefore justifies the definition of h_r and gives

|R_r(a)|²=Σ_((p,q)=1)h_r(p,q)exp(ia log(p/q)),
h_r(1,1)=M_r,
Σ_((p,q)=1,p≠q)|h_r(p,q)|/|ω_(p,q)|≤K(r+1)^17.          (5)

All nonzero frequencies in (5) are distinct. The last estimate follows
by the triangle inequality within each d sum in (4). In particular,
for any δ>0,

Σ_((p,q)=1,0<|ω_(p,q)|<δ)|h_r(p,q)|≤Kδ(r+1)^17.        (6)

This grouping retains cancellations between all equal nonzero
frequencies as well as the constant frequency.

For each fixed N there are only N different r values. Hence the sum
of their absolute coefficient norms is finite. We may average (5)
at a=a_n without freezing any coefficient or exchanging an infinite
N limit with an infinite sum. This proves the identity in (1).
By the decreasing integral comparison for x^(−2),

Σ_(n=N)^(2N−1)n^(−2)=∫_N^(2N)x^(−2)dx+O(N^(−2))
                    =1/(2N)+O(N^(−2)).

Also Σ_(n=N)^(2N−1)n^(−3)=O(N^(−2)). Substituting
M_(2n)=C/(4n²)+O(n^(−3)) proves the formula for Δ_N.
Using r=2n≤4N in (6) proves (2).

To prove that the remaining mass matters, evaluate the fully grouped
series at zero. The actual-function estimate in L334 gives

1≤S_r(0)≤1+2sqrt(2πr)+4r,  B_r(0)≥r².

Consequently S_r(0)/B_r(0)=O(1/r),
R_r(0)=−1+O(1/r), and |R_r(0)|²=1+O(1/r). No recurrence
or equidistribution assertion is used here. From (5),

Σ_((p,q)=1,p≠q)h_r(p,q)=|R_r(0)|²−M_r=1+O(1/r).        (7)

Subtract the small-frequency sum, whose absolute value is bounded
by (6), from (7). The absolute sum over the remaining frequencies
is at least their signed sum. For 2N≤r<4N and δ=δ_N this gives

Σ_((p,q)=1,|ω_(p,q)|≥δ_N)|h_r(p,q)|
 ≥1−K/N−K N^17 exp(−2N).

Averaging proves (3). In particular this obstruction survives full
ratio grouping; it is not an artifact of assigning separate absolute
values to repeated frequencies.

We next check the actual sampled phase, including its square-root
correction. Put b=25/(4π²)<1. On x≥1 its binomial expansion is

a(x)/(2π)=exp(4x)
 +Σ_(j≥1)binom(1/2,j)(−b)^j exp((4−8j)x).

For each fixed derivative order d the series of derivatives converges
uniformly on x≥1: the absolute terms are bounded by a constant times
j^d b^j exp((4−8j)x), and the geometric factor dominates j^d.
After removing the first term the differentiated tail is
O_d(exp(−4x)), uniformly on x≥1. Thus

a^(d)(x)/(2π)=4^d exp(4x)+O_d(exp(−4x)),
|f_ω^(d)(x)|≥(4^d/2)|ω|exp(4x)                         (8)

for x≥N and N sufficiently large depending on fixed d. For
|ω|≥δ_N the last expression is at least (4^d/2)exp(2N),
uniformly in x≥N and in that frequency. Its sign is the sign of ω;
conjugating the exponential treats negative ω.

Here are the precise standard bounds being tested. If an interval
contains m consecutive integers and
0<λ≤|f^(d)|≤Aλ there, the classical estimate has scale

m λ^(1/(2^d−2))
 +m^(1−2^(2−d))λ^(−1/(2^d−2)),  d≥2.                   (9)

For fixed d≥3 and ε>0 Heath-Brown's estimate has scale

m^(1+ε)[λ^(1/(d(d−1)))+m^(−1/(d(d−1)))
         +m^(−2/(d(d−1)))λ^(−2/(d²(d−1)))].             (10)

Constants depend only on the fixed displayed parameters. These are
the classical restatement in D. R. Heath-Brown, *A New k-th Derivative
Estimate for Exponential Sums via Vinogradov's Mean Value*,
[equation (1), p. 1](https://arxiv.org/pdf/1601.04493#page=1), and
[Theorem 1, p. 3](https://arxiv.org/pdf/1601.04493#page=3), respectively.
Their hypotheses and all their terms were checked in that primary
source. They are supporting estimates, not a theorem about D_N.

Whenever a bounded-A application on a subinterval is permissible,
the upper derivative hypothesis and (8) force
λ≥(4^d/(2A))exp(2N). The first term in either (9) or (10),
divided by m, therefore tends to infinity uniformly in the frequency
and the subinterval. Fixed implicit constants cannot change this
comparison. Capping these estimates by |Σ exp(ia_nω)|≤m leaves
only m. Empty and singleton sums also have their trivial bounds.
The derivative ratio over the full dyadic interval grows with N;
we do not apply a theorem with fixed A there without checking its
hypotheses. Allowing arbitrary partitions into subintervals where
the hypotheses do hold does not help, since (8) holds on each one.
Choosing a much smaller λ while retaining fixed A is not permitted.
No term in (9) or (10) has been dropped to obtain a purported saving.

It remains to check that moving weights cannot improve this specific
certificate. Fix a frequency and an integer interval I=[u,v]. Set
w_n=h_(2n)(p,q) and P_t=Σ_(n=u)^t exp(ia_nω). Finite Abel
summation is the exact identity

Σ_(n=u)^v w_n exp(ia_nω)
 =w_v P_v+Σ_(t=u)^(v−1)(w_t−w_(t+1))P_t.

Using only |P_t|≤t−u+1 yields the absolute budget

Q_I=(v−u+1)|w_v|
      +Σ_(t=u)^(v−1)(t−u+1)|w_t−w_(t+1)|.

For each n∈I the telescoping identity
w_n=w_v+Σ_(t=n)^(v−1)(w_t−w_(t+1)) implies, by the triangle
inequality and summation over n,

Σ_(n=u)^v|w_n|≤Q_I.                                    (11)

Thus neither this Abel estimate nor replacing it by the direct
triangle bound improves on Σ_I|w_n|. The same is true after any
partition into consecutive intervals. Sum (11) over all retained
frequencies and divide by N. These budgets converge if used on the
whole interval, since N is finite and each h_(2n) is absolutely
summable; any larger divergent budget would also fail the target.
Equations (3) and (11) prove the asserted certificate lower bound.

For clarity, (7) evaluated phases at zero only to measure coefficient
mass. It is not an evaluation at a_n. Frequencies of large derivative
can cancel on integers, and signs of different frequency contributions
can compensate each other. The tested estimates retain neither kind
of information. The exact discrete mean in (1) could still tend to
zero; the proof supplies no nonvanishing lower bound for it. A method
using information about fractional parts of the actual phases, or
signed summation across distinct frequencies, is outside this test.
No uniform or actual-height sign conclusion follows. ∎

**Mathlib.** Full statement: not checked. Coverage for the discrete
mean identity, grouped inverse-frequency budget, derivative-certificate
comparison and moving-weight lower bound is not checked; their proofs
are above. L333–L334 retain the supporting results recorded as present
through L001:
[`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius),
[`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff),
and [`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re).
Those library links were not rechecked. They support the original
series and denominator, not a match for (1)–(3). The checked paper
supports only (9)–(10). No full library match or absence is asserted.
