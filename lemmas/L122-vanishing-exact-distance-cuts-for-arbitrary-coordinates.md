# Lemma 122: vanishing exact-distance cuts for arbitrary coordinates

**Hypotheses.** Let 0<x_1<x_2<⋯ and W=Σ_i x_i^(-2)<∞.
Let y_i≥0 with Y=Σ_i y_i<∞. Define

S_n=Σ_(i≤n<j)y_i/(x_j−x_i)².

**Conclusion.** liminf_(n→∞) S_n=0. In particular the cover alternative
of Lemma 121 never occurs under its stated hypotheses. Its capacities
tend to infinity, and there exists a positive strictly increasing
unbounded sequence f with

Σ_i f(i)/x_i²<∞,

sup_i Σ_(j>i)(f(j)−f(i))/(x_j−x_i)²<∞.

## Proof

Summability implies x_i→∞ and local finiteness. Every S_n is finite:
for each of its finitely many source indices the destination tail with
x_j≥2x_i is bounded by 4Σ_j x_j^(-2), and the rest is finite.

### A continuous maximal estimate

For a finite positive atomic measure μ on the real line define

Mμ(t)=sup_(r>0) μ([t−r,t+r])/(2r).

For u>0 its bad set has Lebesgue measure at most 3μ(ℝ)/u.
Here are details of the elementary covering argument. For any compact
subset K of the bad set choose at each point a centered interval with
mass strictly greater than u times its length. Slight enlargement
preserves the strict inequality and puts the center in its interior.
The interiors cover K; extract finitely many intervals. Repeatedly
select a longest remaining interval and discard all that intersect it.
Selected intervals are disjoint; each discarded interval is contained
in the concentric triple of the selected interval that discarded it.
Thus |K|≤3Σ_selected length<3μ(ℝ)/u. Inner regularity yields the
claim for the bad set. Measurability follows by taking the supremum over
positive rational radii: radii approaching any radius from above recover
its quotient, and each fixed-radius mass function is Borel measurable.
The zero measure has maximal function zero.

### Real cuts and distant pairs

For t≥x_1 define S(t)=Σ_(x_i≤t<x_j)y_i/(x_j−x_i)².
Pairs with x_i≤t/2 contribute at most

4Y Σ_(x_j>t)x_j^(-2).

Among the remaining pairs, those with x_j≥2t contribute at most

4W Σ_(x_i>t/2)y_i.

Their sum, denoted R(t), tends to zero as t→∞. The remaining pairs
satisfy t/2<x_i≤t<x_j<2t. These bounds concern disjoint classes;
all summands are nonnegative.

### Choosing a cut away from local atoms

Let q≥1, N=2^q and I_q=[N/2,4N]. Put

a_q=Σ_(x_i∈I_q)x_i^(-2),  b_q=Σ_(x_i∈I_q)y_i,
T_q=#{i:x_i∈I_q}.

Every positive coordinate belongs to at most four of these closed
windows. Consequently Σ_q a_q≤4W and Σ_q b_q≤4Y. Also
T_q≤16N²a_q≤16WN².

If T_q=0 or b_q=0, every cut t∈[N,2N] has zero remaining near
contribution. Otherwise write T=T_q, b=b_q and set δ=N/(8T).
In [N,2N], discard the closed δ-neighborhood of every local coordinate;
the total discarded length is at most 2δT=N/4. Apply the maximal
estimate to the finite measures

μ=Σ_(x_i∈I_q)y_i δ_(x_i),  ν=Σ_(x_i∈I_q)δ_(x_i).

Here δ_(x_i) denotes a unit point mass, distinct from the radius δ.
The sets where Mμ>24b/N or Mν>24T/N each have length at most N/8.
Their union with the discarded neighborhoods has length at most N/2.
There is thus a cut t_q∈[N,2N], strictly farther than δ from every
local coordinate, with

Mμ(t_q)≤24b/N,  Mν(t_q)≤24T/N.                 (1)

All remaining near pairs at this cut have endpoints in I_q and
distance d=x_j−x_i satisfying δ<d<4N. Split into shells

2^h δ≤d<2^(h+1)δ,  h=0,...,H_q−1,

where H_q=ceil(log_2(32T))+1. These shells cover the indicated range
since 4N/δ=32T. In a shell with s=2^h δ, both endpoints lie in
the interval centered at t_q of radius 2s. Enlarge to all source and
destination pairs in this interval. Its contribution is at most

s^(-2) μ([t_q−2s,t_q+2s]) ν([t_q−2s,t_q+2s])
 ≤16 Mμ(t_q) Mν(t_q).

Using (1) and T≤16N²a_q gives

S(t_q)≤R(t_q)+147456 H_q a_q b_q.               (2)

There is a finite constant C_W depending only on W such that
H_q≤C_W(q+1) whenever T_q≥1. Indeed
log_2(32T_q)≤2q+log_2(512W), and ceil(v)≤v+1;
one may take C_W=4+|log_2(512W)|. In the zero cases select any cut
and use zero for the near contribution, so in all cases

S(t_q)≤R(t_q)+147456 C_W(q+1)a_q b_q.           (3)

### Extracting the subsequence and payoff

Cauchy–Schwarz gives Σ_q sqrt(a_q b_q)≤4sqrt(WY)<∞.
It follows that liminf_q (q+1)a_q b_q=0. Otherwise some ε>0
would give sqrt(a_q b_q)≥sqrt(ε/(q+1)) eventually, contradicting
summability. Choose q tending to infinity along which that product
tends to zero. Then t_q≥2^q→∞, R(t_q)→0, and (3) gives S(t_q)→0.

For all sufficiently large such cuts, let n_q be the last index with
x_(n_q)≤t_q. It exists and is finite by local finiteness, tends to
infinity, and satisfies S_(n_q)=S(t_q), including if the chosen cut
in a zero case equals a coordinate. This proves the asserted liminf.

A cover in Lemma 121 would have S_n≥1 at every n, which is impossible.
That lemma's alternative now gives capacity divergence and the stated
payoff, including its strict increase and weighted summability. ∎

## Qualifications and verification

No minimum gap, count envelope, or fixed common cut subsequence is
assumed. The cuts may depend on y. The small excluded radius depends
on the local count, but its logarithmic shell cost is controlled by
reciprocal-square summability. The finite maximal argument, tail bounds,
window overlap, shell count, zero local masses, and conversion to index
cuts have been checked analytically; no numerical certificate is needed.
All series rearrangements use nonnegative terms.

The cut proof is self-contained; its maximal/shell strategy parallels
Lemma 119 but does not use that lemma as an input. Lemma 121 supplies
only the final capacity and payoff consequence. General stochastic
nonexplosion, uniform heat-parameter bounds, whole-plane continuation,
and RH are not conclusions here.

Formalization would require the finite atomic maximal estimate with
Lebesgue inner regularity, the good-cut measure bound, dyadic shell
estimates, nonnegative tail bounds, Cauchy–Schwarz and subsequence
extraction, and application of the exact-distance capacity alternative.
