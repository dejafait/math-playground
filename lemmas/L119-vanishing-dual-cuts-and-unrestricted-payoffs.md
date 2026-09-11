# Lemma 119: vanishing dual cuts and unrestricted payoffs

**Hypotheses.** Let m_l be positive integers with
W=Σ_(l≥1)m_l/l²<∞. Let y_k≥0 with Y=Σ_(k≥1)y_k<∞. Define

S_n=Σ_(k≤n) y_k Σ_(l>n) m_l/(l−k)².

**Conclusion.** liminf_(n→∞) S_n=0. Consequently no summable cover
in the sense of Lemma 118 exists for these counts. The finite capacities
there tend to infinity, and there is a positive strictly increasing
unbounded function F on the positive integers such that

Σ_l m_l F(l)/l²<∞,

sup_k Σ_(l>k) m_l(F(l)−F(k))/(l−k)²<∞.

## Proof

Every S_n is finite: for each fixed k≤n the finite part l<2k
is finite and the remaining summands are at most 4m_l/l².
We first prove the liminf assertion without using any payoff theorem.

### An elementary maximal estimate

For a finitely supported nonnegative sequence f on the integers, put

M f(n)=sup_(r≥0 integer) [Σ_(|t−n|≤r)f(t)]/(2r+1).

For any finite set E of integers and threshold u>0,

#{n∈E:M f(n)>u}≤3(Σ_t f(t))/u.                    (1)

Indeed, for each such n choose a centered integer interval with average
strictly above u. This is a finite collection. Select an interval of
largest length, discard all intervals intersecting it, and repeat.
The selected intervals are disjoint. Every discarded interval has radius
at most that of the selected interval it meets, so is contained in its
concentric interval of triple radius. The latter has cardinality at
most three times the original cardinality, also for radius zero.
The union of these enlarged intervals covers all the bad centers.
The sum of cardinalities of the selected intervals is less than
(Σ_t f(t))/u, by disjointness and their strict average inequalities.
This proves (1). No bound on the witnessing radii is needed.

### Separating distant pairs

Pairs with k≤n/2 contribute at most

4Y Σ_(l>n)m_l/l²,

since l−k≥l/2. Among remaining pairs, those with l≥2n contribute
at most 4W Σ_(k>n/2)y_k, by the same denominator inequality.
Thus the total contribution of these two disjoint classes is at most

R_n=4Y Σ_(l>n)m_l/l² + 4W Σ_(k>n/2)y_k →0.         (2)

All remaining pairs satisfy n/2<k≤n<l<2n.

### Selecting a cut in each dyadic interval

For j≥1 let N=2^j and I_j=[N/2,4N]∩ℕ. Set

a_j=Σ_(l∈I_j)m_l/l²,   b_j=Σ_(k∈I_j)y_k,

T_j=Σ_(l∈I_j)m_l≤16N²a_j.

Each fixed positive integer belongs to at most four of these windows.
Nonnegative summation therefore gives Σ_j a_j≤4W and Σ_j b_j≤4Y.

Restrict m and y to I_j and extend them by zero to all integers,
calling the resulting sequences g and f respectively. Suppose b_j>0.
Apply (1) on E_j={N,...,2N−1}, with thresholds 24b_j/N for f
and 24T_j/N for g. Each bad set has cardinality at most N/8.
There is consequently an n_j∈E_j where both inequalities hold:

M f(n_j)≤24b_j/N,   M g(n_j)≤24T_j/N.              (3)

If b_j=0, take any n_j∈E_j; the remaining near contribution is zero.
The thresholds for g are positive since m_l are positive.

Fix a good cut n=n_j with b_j>0. All its remaining pairs lie in I_j.
Split them into shells 2^h≤l−k<2^(h+1). As l−k<2n≤4N,
all shells are covered by 0≤h≤j+2 (allowing empty shells).
For one shell put r=2^(h+1). Both endpoints are within distance r
of n. Bounding the denominator below by 2^(2h) and enlarging to
all pairs in the centered interval gives a shell contribution at most

2^(−2h) [Σ_(|k−n|≤r)f(k)] [Σ_(|l−n|≤r)g(l)]
 ≤25 M f(n) M g(n),

because 2r+1≤5·2^h. There are at most j+3 shells. Combining this
with (2), (3), and T_j≤16N²a_j yields

S_(n_j)≤R_(n_j)+230400(j+3)a_j b_j.                (4)

This also holds when b_j=0.

By Cauchy–Schwarz, Σ_j sqrt(a_j b_j)<∞. It follows that

liminf_(j→∞)(j+3)a_j b_j=0:                        (5)

otherwise some ε>0 would give sqrt(a_j b_j)≥sqrt(ε/(j+3))
for every sufficiently large j, contradicting that summability.
Choose an increasing subsequence of j along which the expression in
(5) tends to zero. Its cuts tend to infinity since n_j≥2^j.
Equation (2) makes R_(n_j) tend to zero, and (4) proves the claimed
liminf. This does not assert convergence along all cuts.

Finally a summable cover from Lemma 118 would satisfy S_n≥1 for
every n, contrary to the liminf just proved. The alternative and payoff
equivalence in that lemma give capacity divergence and all the stated
properties of F. ∎

## Qualifications and verification

The cut estimate itself uses only nonnegative finite counts and weighted
summability, not their integrality or a positive lower bound. Positive
integer counts are retained to apply Lemma 118 as stated. The selected
cuts may depend on both m and y; no common subsequence is asserted.
This proves unrestricted payoff existence, but does not here establish
its stochastic consequences, uniform control in a heat parameter,
whole-plane zero continuation, or RH.

The proof is analytic and requires no numerical certificate. Its audit
checks finite series, disjoint far classes, closed dyadic windows and
fourfold overlap, the finite covering argument including radius zero,
zero local y mass, shell endpoints, the constant in (4), and the
subsequence consequence of summability. All infinite rearrangements use
nonnegative terms. The only earlier mathematical input is the final
application of Lemma 118; the cut estimate is proved independently.

Formalization would require the finite greedy interval selection,
nonnegative-series estimates, Cauchy–Schwarz for summable sequences,
subsequence extraction from a zero liminf, and the stated finite-capacity
alternative. No RH-equivalent positivity is used.
