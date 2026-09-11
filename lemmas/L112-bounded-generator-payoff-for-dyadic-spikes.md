# Lemma 112: bounded-generator payoff for dyadic spikes

**Hypotheses.** For positive integers k, let m_k=1 except that
m_(2^j)=1+floor(4^j/j²) for every integer j≥1.

**Conclusion.** The explicit function

P(k)=1+Σ_{j≥1:2^j<k}1/j,
F(k)=P(k)+1−1/(k+1)

is positive, strictly increasing and unbounded, and satisfies

D:=Σ_{k≥1}m_k F(k)/k²<∞,
sup_{k≥1}Σ_{l>k}m_l(F(l)−F(k))/(l−k)²≤8+4D<∞.       (1)

For arbitrary clusters of m_k distinct points in [k,k+1/4], the
forward jump process of Lemma 107 on their increasing union is
nonexplosive from every starting point. Every strictly increasing
positive bounded height sequence on that union has a subsequence
whose full upward contribution tends to zero.

## Proof

All sums defining P at a fixed k are finite. P is nondecreasing,
and the harmonic series shows P(k)→∞. The correction
B(k)=1−1/(k+1) is positive and strictly increasing, so F has all
the asserted monotonicity properties.

Split m into its unit baseline and its extra masses at powers of two.
For k≥1, F(k)≤2+log₂ k, since the number of indices with 2^j<k
is at most log₂ k and every 1/j≤1. Thus the baseline contribution
to D is finite by the integral test. At a spike,

F(2^j)=2+H_(j−1)−1/(2^j+1)≤3+log j,                 (2)

where H_0=0 and H_r=Σ_{h=1}^r1/h. For j≥2 this follows from
H_(j−1)≤1+log(j−1)≤1+log j, and j=1 is immediate.
The extra contribution to D is at most
Σ_{j≥1}(3+log j)/j², again finite by the integral test. This proves
weighted integrability without discarding any spike. In particular
Σ m_k/k²<∞ because F≥1.

Fix k≥1. Split the generator into k<l<2k and l≥2k. For the latter,
l−k≥l/2 and F(l)−F(k)≤F(l), so the entire far sum is at most 4D.
The equality l=2k belongs to this far range; that boundary matters.

For the baseline in the near range, the increment P(l)−P(k) is the
sum of 1/j over powers 2^j in [k,l). Such an interval, with l<2k,
contains at most one power of two, so the
increment is at most 1, and in particular at most 2. Also 0≤B(l)−B(k)≤1. Consequently the
near baseline sum is at most

3Σ_{d≥1}d^(−2)≤6,                                  (3)

using 1+∫_1^∞t^(−2)dt=2 as an upper bound for the series.
This also covers k=1, whose near range is empty.

There is at most one power of two l=2^j in (k,2k). For such a
power, l/2<k<l. Every power of two strictly below l is at most l/2
and is therefore already strictly below k. It follows that P(l)=P(k).
Thus only the correction contributes for this extra mass. Its exact
increment is

B(l)−B(k)=(l−k)/((k+1)(l+1)).

Since floor(l²/j²)≤l²/j², its generator contribution is at most

l²/[j²(k+1)(l+1)(l−k)]
 ≤l/[j²(k+1)(l−k)]≤2.                              (4)

Here l<2k, j≥1, and the integer l−k≥1. Combining (3), (4), and
the full far estimate proves (1). Every series estimate was for
nonnegative terms and establishes convergence of the full series.

For the cluster consequence, use the process of Lemma 107, whose
coordinate summability follows from Σ m_k/k²<∞. Give each point in
cluster k the payoff F(k). Internal increments are zero. Points in
clusters k<l have separation at least 3(l−k)/4, so (1) bounds their
full payoff generator by (16/9)(8+4D). Each cluster is finite and
F tends to infinity. The finite-cluster cutoff argument proved in
Lemma 111 now applies verbatim: at the first exit to cluster label
at least R, cap the absorbing payoff at F(R), retain all exit rates,
and obtain

P(tau_R≤t)≤[F(k_0)+(16/9)(8+4D)t]/F(R).

The linear count envelope in Lemma 111 was used to construct its
payoff, not in this cutoff argument. Here (1) supplies the needed
generator bound directly. The exit times increase to the full lifetime;
letting R→∞ proves nonexplosion. Lemma 107 supplies the stated
height-dependent selection conclusion. ∎

## Qualifications

The counts satisfy Σ m_k/k²<∞ but m_(2^j)/2^j≥2^j/j²→∞.
Thus this example lies beyond the linear envelope of Lemma 111.
The payoff anticipates the isolated large destination masses by placing
its jumps immediately after them. This proves existence for this specific
sequence; it does not establish a payoff for all summable counts.
General coordinate selection and RH remain unproved.

## Verification and formalization obligations

The proof is analytic; no numerical certificate is required. Audit the
strict inequality in the definition of P, the assignment of l=2k to
the far range, the empty near range at k=1, and the exact correction
increment. Formalization would require harmonic divergence, integral
bounds for logarithmically weighted reciprocal squares, dyadic spacing,
the nonnegative series decomposition, and the finite-cluster cutoff
argument of Lemma 111 and selection implication of Lemma 107.
