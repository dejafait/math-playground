# Lemma 114: bounded-generator payoff for separated mass pairs

**Hypotheses.** Let n_j be positive integers, j≥1, with
n_(j+1)≥4(n_j+1). Let M_j,N_j be nonnegative integers and suppose

A:=Σ_j (M_j+N_j)/n_j²<∞.

Set m_(n_j)=1+M_j, m_(n_j+1)=1+N_j, and m_k=1 at all other
positive integers. The pairs are disjoint by the separation hypothesis.

**Conclusion.** There is a positive strictly increasing unbounded
function F on the positive integers such that

D:=Σ_k m_k F(k)/k²<∞,
sup_k Σ_(l>k) m_l(F(l)−F(k))/(l−k)²≤4+2A+4D<∞.

For arbitrary clusters of m_k distinct points in [k,k+1/4], the forward
jump process of Lemma 107 is nonexplosive from every starting point.
Every strictly increasing positive bounded height sequence on the
increasing cluster union admits a subsequence with full upward
contribution tending to zero, in the sense of Lemma 107.

## Proof

Write e_j=n_j+1. Choose strictly increasing positive integers J_h,
h≥1, such that Σ_(j>J_h)(M_j+N_j)/n_j²≤2^(-h). Convergence permits
this recursive choice, also when A=0. Define

P(k)=1+Σ_(h≥1) 1_{e_(J_h)<k},
B(k)=1−1/(k+1), and F(k)=P(k)+B(k).

The endpoints satisfy e_(j+1)≥4e_j+1, hence in particular double.
The sum defining P is locally finite. Each selected endpoint eventually
lies below k, so P is unbounded. The positive strictly increasing B
makes F positive and strictly increasing. There are at most 1+log₂ k
endpoints at or below k; therefore F(k)≤3+log₂ k and the unit-baseline
sum Σ_k F(k)/k² converges by the integral test.

Put w_j=M_j/n_j²+N_j/(n_j+1)², so Σ_j w_j≤A. At both locations
of pair j, P has the same value, namely 1 plus the number of selected
indices J_h<j. Indeed the jump after e_j has not yet occurred at e_j,
and all earlier endpoints are below n_j. Interchanging nonnegative
sums gives

Σ_j [M_j P(n_j)/n_j²+N_j P(n_j+1)/(n_j+1)²]
 =Σ_j w_j+Σ_h Σ_(j>J_h) w_j≤A+1.

The B contribution from extra masses is at most A. This proves D<∞,
and also Σ_k m_k/k²<∞.

Fix k≥1 and first consider k<l<2k. There is at most one endpoint
in [k,l): two endpoints u<v there would have v≥2u≥2k, impossible.
Thus P(l)−P(k)≤1 and B(l)−B(k)≤1. The full unit-baseline
contribution in this range is at most

2Σ_(d≥1) d^(-2)≤4,

where Σ d^(-2)≤1+∫_1^∞ t^(-2)dt=2.

Now suppose l is a mass location in pair j and k<l<2k. If j>1,
its preceding endpoint satisfies

e_(j−1)≤n_j/4≤l/4<k.

All earlier endpoints are therefore below k. Its own endpoint e_j
is at least l; all later ones are larger. No endpoint lies in [k,l),
so P(l)=P(k). This reasoning applies separately to l=n_j and to
l=n_j+1, including k=n_j at the second location. For j=1 there
are no earlier endpoints and the same cancellation holds.

Write Q_l for the extra mass at l (M_j or N_j). Its contribution is

Q_l(B(l)−B(k))/(l−k)²
 =Q_l/[(k+1)(l+1)(l−k)]
 ≤(Q_l/l²) l/[(k+1)(l−k)]≤2Q_l/l²,

because l<2k and the integer difference l−k≥1. Summing over all
near mass locations gives at most 2Σ_j w_j≤2A. No bound on either
individual mass is needed.

For l≥2k, l−k≥l/2 and F(l)−F(k)≤F(l), hence the full far sum is
at most 4Σ_(l≥2k)m_l F(l)/l²≤4D. The boundary l=2k is assigned
only to this range; when k=1 the near range is empty. Combining the
ranges proves the claimed generator bound and convergence.

For the cluster consequence, assign payoff F(k) to every point in
cluster k. Reciprocal-square summability of the coordinates follows
from Σ m_k/k²<∞, so Lemma 107 defines the process. Payoff increments
inside a cluster are zero. For different clusters k<l the coordinate
distance is at least l−k−1/4≥3(l−k)/4. The full pointwise payoff
generator is consequently bounded by C=(16/9)(4+2A+4D).

Use the bounded-generator cutoff argument in Lemma 111: stop at the
first arrival in a cluster with label at least R, retain all exit
rates, and give that absorbing state payoff F(R). This cap decreases
generator increments. There are finitely many transient points, and
its finite-state expectation identity gives, from cluster k_0<R,

P(tau_R≤t)≤[F(k_0)+Ct]/F(R).

On the holding-time construction the exit times increase to the
lifetime, since every cluster is finite. Letting R tend to infinity
proves nonexplosion. Lemma 107 supplies the height-dependent upward
selection conclusion. ∎

## Qualifications

This proves the specified paired-location test. The mass amplitudes
are arbitrary subject to the displayed summability, but separation of
pairs remains an extra hypothesis. The construction follows the idea
of Lemma 113; its estimates have been proved here independently.
Only the bounded-generator cutoff portion of Lemma 111 is used, not
its linear count envelope. Arbitrary summable counts, general coordinate
selection, and RH remain unproved. The subsequence may depend on heights.

## Verification and formalization obligations

This proof is analytic and needs no numerical certificate. Audit tail
threshold existence, local finiteness and unboundedness, strict jumps
after second locations, nonnegative interchange, endpoint separation,
near cancellation at both locations, n_1=1, k=n_j and l=n_j+1,
and the l=2k far boundary. Formalization would require those elementary
estimates and the cutoff and process results invoked above.
