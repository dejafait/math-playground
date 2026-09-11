# Lemma 108: nonexplosion under power gap lower bounds

**Hypotheses.** Let 0<x_1<x_2<⋯. Suppose constants a>1/2 and c>0
satisfy

x_j−x_i ≥ c(j^a−i^a), for every pair j>i≥1.             (1)

Use the forward jump process and lifetime T defined in Lemma 107,
with rates q_ij=(x_j−x_i)^(-2) and K_i=Σ_{j>i}q_ij.

**Conclusion.** From every starting index n, P_n(T=∞)=1. Consequently,
for every strictly increasing positive bounded height sequence, the
full upward contributions in Lemma 107 have a subsequence tending
to zero. This includes x_i=i^a for every a>1/2.

## Proof

Taking i=1 in (1) shows x_j≥(c/2)j^a for all sufficiently large j.
Thus Σ_j x_j^(-2)<∞, and Lemma 107 supplies finite positive K_i and
the embedded chain and independent holding-time construction.

Choose a real number p with 0<p<2a−1 and put f(i)=i^p. We first
prove a uniform bound

Σ_{j>i} q_ij(f(j)−f(i)) ≤ C, for every i≥1,             (2)

where C is finite and depends only on a,c,p. All summands are positive.
For i<j≤2i, the mean value theorem applied on [i,2i] gives

j^a−i^a ≥ A i^(a−1)(j−i),  A=a min(1,2^(a−1))>0,
j^p−i^p ≤ B i^(p−1)(j−i),  B=p max(1,2^(p−1)).

By (1), the sum over these j is at most

[B/(c²A²)] i^(p+1−2a) Σ_{k=1}^i 1/k
 ≤ [B/(c²A²)] i^(p+1−2a)(1+log i).                    (3)

For j>2i, j^a−i^a≥(1−2^(−a))j^a and j^p−i^p≤j^p.
Writing r=2a−p>1, the remaining sum is at most

[c²(1−2^(−a))²]^(-1) Σ_{j>2i} j^(−r)
 ≤ [c²(1−2^(−a))²(r−1)]^(-1) (2i)^(1−r).             (4)

The last inequality is the decreasing-function integral bound on
[2i,∞). Since p+1−2a<0, (3) and (4) are uniformly bounded for i≥1.
For example, with δ=2a−p−1>0, i^(−δ)≤1 and
i^(−δ)log i≤1/(eδ). This proves (2).

We now justify nonexplosion without applying a process identity past
an unknown explosion time. Fix integers R>n and let τ_R be the sum
of holding times up to the first embedded-chain index at least R.
There are at most R−n jumps before that exit since every jump strictly
increases the index. In particular τ_R is finite almost surely.
Collapse all exit destinations j≥R to a single absorbing state ∂.
Before exit this is a finite-state continuous-time chain on
{n,…,R−1,∂}; at i<R its total rate is K_i, with exit rate
Σ_{j≥R}q_ij. The holding-time and destination laws agree exactly with
the construction in Lemma 107 up to τ_R.

Set g_R(i)=i^p on transient states and g_R(∂)=R^p. Its finite-state
generator at i<R is

Q_R g_R(i)
 = Σ_{i<j<R} q_ij(j^p−i^p)
   + Σ_{j≥R} q_ij(R^p−i^p)
 ≤ Σ_{j>i} q_ij(j^p−i^p) ≤ C.                         (5)

At ∂ the generator is zero. The finite-state expectation identity gives

E_n[g_R(X_t)] = n^p + ∫_0^t E_n[Q_R g_R(X_s)] ds
 ≤ n^p+Ct.                                           (6)

For completeness, this identity only uses a finite rate matrix: each
state has an exponential holding time and fixed destination law, so
its transition matrix has expansion I+hQ_R+O(h²) uniformly over the
finite state set. Conditioning, taking the time derivative of the
expectation of the bounded g_R, and integrating gives (6). No assertion
about the infinite-state process after T is used.

On {τ_R≤t}, X_t=∂ and g_R(X_t)=R^p, while g_R is nonnegative elsewhere.
Therefore

P_n(τ_R≤t) ≤ (n^p+Ct)/R^p.                            (7)

On the original embedded-chain probability space, τ_R increases to T
as R→∞. Indeed, the chain indices strictly increase to infinity, and
every fixed holding-time term is included before exit once R exceeds
its associated visited index. In particular {T≤t} is contained in
{τ_R≤t} for every R. Letting R→∞ in (7) proves P_n(T≤t)=0 for every
finite t≥0. Taking the union over positive integer t proves T=∞ almost
surely. The subsequence conclusion follows from Lemma 107. ∎

## Qualifications

This resolves a scoped class of the universal nonexplosion question.
Reciprocal-square summability alone does not imply (1); coordinates
may have arbitrarily small successive gaps at widely separated places.
No conclusion about those general configurations is proved here.
The subsequence assertion for exact power coordinates has been obtained
by earlier averaging arguments; the new result is a lifetime theorem
and its extension to the gap-dominated class (1). Neither RH nor a
theta-specific zero assertion follows.

## Verification and formalization obligations

The proof is analytic and requires no numerical certificate. Check
both derivative constants for exponents below and above one, the
strict inequality p<2a−1 needed for the infinite tail, and the negative
exponent bounding the harmonic factor. The probabilistic audit uses
only finite-state chains, with the complete exit tail retained in the
rate matrix; suppressing that tail would describe a different process.
The capped payoff decreases the positive generator increments, which
is the direction needed in (5). Formalization would require the mean
value theorem, the power-tail integral estimate, the finite-state
expectation identity, the coupling at first exit, and increasing limits
of nonnegative holding-time sums. Lemma 107 supplies the process and
the final upward-selection implication.
