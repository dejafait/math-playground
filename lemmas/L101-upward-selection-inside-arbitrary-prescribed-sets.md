# Lemma 101: upward selection inside arbitrary prescribed sets

**Hypotheses.** Let P, x_n, b_n, H, w_n, f and E_f be as in
Lemma 100. Thus P is an unbounded subset of the positive integers
containing 1, x_s=s^(3/4) for s∈P, and between consecutive s<t in P,

x_n=sqrt(n)t^(1/4)(1+(t−n)/(4t)),  s<n<t.

The heights increase strictly from b_1>0 to H<∞.

**Conclusion.** For every N∈P, let S_N=P∩[N,2N), and for s∈S_N let

d_s=min(t_s,2N)−s,

where t_s is the next element of P after s. Put q=1−2^(−3/4).
Then d_s are positive integers, Σ_{s∈S_N}d_s=N, and

(1/N)Σ_{s∈S_N}d_s E_f(w_s)
 ≤ H N^(−1/2)[512(1+log(3N+1))+18q^(−2)+4].          (1)

Consequently there is an increasing sequence s_k∈P tending to infinity
such that E_f(w_(s_k))→0. Selection may depend on the heights.

## Proof

Lemma 100 supplies the strict coordinate increase, product and exact
zero properties, convergence of all the upward sums, and separation

x_j−x_s ≥ (j^(3/4)−s^(3/4))/3,  j>s.                 (2)

The intervals [s,s+d_s], for s∈S_N in order, partition [N,2N]
with disjoint interiors. This proves positivity and the sum of lengths.

Fix s∈S_N and s<j≤4N. We first prove a bound that retains d_s.
If j<t_s, the interpolation gives

x_j≥sqrt(j)t_s^(1/4)≥sqrt(s)(s+d_s)^(1/4).

Since x_s=s^(3/4), the mean value integral for v^(1/4), with
s≥N and s+d_s≤2N, gives

x_j−x_s ≥ sqrt(s) d_s/[4(s+d_s)^(3/4)]
          ≥ d_s/[4·2^(3/4) N^(1/4)].                 (3)

If j≥t_s, then j≥s+d_s, so (2) and the derivative of v^(3/4)
on [s,s+d_s] instead give

x_j−x_s ≥ d_s/[4(2N)^(1/4)],

which implies (3) as well. This includes adjacent prescribed indices
and gaps that extend past 2N or 4N. Independently, (2) for j≤4N gives

x_j−x_s ≥ (j−s)/[4(4N)^(1/4)]
          ≥ (j−s)/[4·2^(3/4) N^(1/4)].

Taking half the sum of these two lower bounds, and using
8·2^(3/4)<16, yields

x_j−x_s ≥ (d_s+j−s)/(16 N^(1/4)).                   (4)

Write E_f(w_s)=A_s+B_s+V_s, where A_s is the right-hand contribution
from s<j≤4N, B_s is the right-hand contribution from j>4N, and V_s
is the full reflected contribution. By (4),

A_s≤512sqrt(N) Σ_{j=s+1}^{4N}(b_j−b_s)/(d_s+j−s)².   (5)

Put Δ_r=b_(r+1)−b_r. Expand b_j−b_s=Σ_{r=s}^{j−1}Δ_r
in the finite weighted sum of (5). For a fixed r≥s, the coefficient
from the sum over j is bounded by

Σ_{j=r+1}^{4N}1/(d_s+j−s)²
 ≤ ∫_{r−s}^∞ (d_s+v)^(−2)dv =1/(d_s+r−s).          (6)

The integral bound follows because the integrand is decreasing.
Thus the coefficient of Δ_r in the weighted kernel is at most

C_r=Σ_{s∈S_N, s≤r} d_s/(d_s+r−s),  N≤r<4N.

For intervals ending at or before r, d_s≥1 and u∈[s,s+d_s]
imply d_s+r−s≥r−u+1>0. Hence

d_s/(d_s+r−s) ≤ ∫_s^(s+d_s) du/(r−u+1).

These intervals have disjoint interiors and lie in [N,r], so their
total is at most log(r−N+1)≤log(3N+1). There is at most one
remaining interval with s≤r<s+d_s; its contribution is at most 1.
This also treats r=N, where the integral portion is empty. Therefore

C_r≤1+log(3N+1).

Every increment in (5) has N≤r<4N, so its total budget is
Σ_{r=N}^{4N−1}Δ_r=b_(4N)−b_N≤H. Equations (5)–(6) give

(1/N)Σ_{s∈S_N}d_s A_s
 ≤512H N^(−1/2)(1+log(3N+1)).                        (7)

For completeness, (2), j>4N and s<2N imply
x_j−x_s≥q j^(3/4)/3. Also x_j≥j^(3/4). Thus the right and
reflected tails obey the same bounds as in Lemma 100:

B_s≤18Hq^(−2)Σ_{j>4N}j^(−3/2)≤18Hq^(−2)N^(−1/2),
V_s≤2HΣ_{j>s}j^(−3/2)≤4H N^(−1/2).

These estimates follow first for finite sums and then for their
nonnegative increasing limits. Since the weights sum to N, combining
them with (7) proves (1).

Choose recursively N_k∈P with N_(k+1)>2N_k, possible by unboundedness.
Select a minimizing s_k∈S_(N_k) for E_f(w_s). Positive weighted
averaging bounds this minimum by (1), which tends to zero. The selected
indices satisfy s_k<2N_k<N_(k+1)≤s_(k+1), as required. ∎

## Qualifications and verification

This resolves selection inside P for the specified interpolation,
without a density assumption on P or a rate assumption on the heights.
The bound is uniform over P and heights with a common H. It does not
supply one fixed subsequence that works for every height sequence, or
an assertion for arbitrary coordinates, theta zeros, or RH.

The proof is analytic and needs no numerical certificate. Checks are
the clipped interval partition, both successor cases in (3), constants
in (4)–(5), the decreasing-integrand estimate, the single interval
crossing r, the finite height budget, and both infinite tails.
Formalization would require those inequalities and partitions,
Lemma 100's product and separation results, nonnegative sum limits,
and finite weighted minimum selection.
