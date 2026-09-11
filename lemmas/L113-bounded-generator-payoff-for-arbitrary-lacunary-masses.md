# Lemma 113: bounded-generator payoff for arbitrary lacunary masses

**Hypotheses.** Let n_j be positive integers with n_(j+1)≥2n_j.
Let M_j be nonnegative integers satisfying A:=Σ_j M_j/n_j²<∞.
Set m_k=1+M_j when k=n_j, and m_k=1 otherwise.

**Conclusion.** There is a positive, strictly increasing unbounded
function F on the positive integers such that

D:=Σ_k m_k F(k)/k²<∞,
sup_k Σ_(l>k) m_l(F(l)−F(k))/(l−k)²≤4+2A+4D<∞.

For any clusters of m_k distinct points in [k,k+1/4], the forward
jump process of Lemma 107 is nonexplosive from every starting point.
Every strictly increasing positive bounded height sequence on the
cluster union admits a subsequence with full upward contribution
tending to zero.

## Proof

Choose strictly increasing positive integers J_h, h≥1, such that

Σ_(j>J_h) M_j/n_j²≤2^(-h).

Convergence of the nonnegative series permits this recursive choice,
including when A=0. Define

P(k)=1+Σ_(h≥1) 1_{n_(J_h)<k},
B(k)=1−1/(k+1), and F(k)=P(k)+B(k).

These sums are finite for each k, because n_j≥2^(j−1).
The function P is nondecreasing and unbounded: at k>n_(J_H)
at least H jumps have occurred. The function B is positive and
strictly increasing, so F is positive, strictly increasing and unbounded.

There are at most 1+log₂ k spike locations at or below k. Consequently
F(k)≤3+log₂ k, and Σ_k F(k)/k² converges by the integral test.
For the extra masses, nonnegative sum interchange gives exactly

Σ_j (M_j/n_j²)P(n_j)
 =A+Σ_h Σ_(j>J_h) M_j/n_j²≤A+1.

The strict inequality in the definition of P is essential here: the
mass at n_(J_h) does not pay for the jump immediately after itself.
Since B≤1, the extra contribution to D is at most 2A+1.
This proves D<∞, and also Σ_k m_k/k²<∞.

Fix k≥1. First consider k<l<2k. The interval [k,l) contains at
most one spike location: two such locations u<v would satisfy
v≥2u≥2k, a contradiction. Thus P(l)−P(k)≤1 and
B(l)−B(k)≤1. The full unit-baseline contribution in this near range
is at most

2Σ_(d≥1) d^(-2)≤4.

There is at most one spike location l=n_j in (k,2k). All earlier
spikes are at most l/2<k. All selected jumps before l have therefore
already occurred at k, while the jump after l has not occurred at l.
Hence P(l)=P(k). The extra contribution of this spike is exactly

M_j(B(l)−B(k))/(l−k)²
 =M_j/[(k+1)(l+1)(l−k)]
 ≤(M_j/l²) l/[(k+1)(l−k)]≤2A,

using l<2k and the integer spacing l−k≥1. If there is no such
spike the extra near contribution is zero. For k=1 the near range
is empty, so these bounds still hold.

For l≥2k, use l−k≥l/2, positivity of F, and monotonicity to obtain

Σ_(l≥2k) m_l(F(l)−F(k))/(l−k)²
 ≤4Σ_(l≥2k) m_l F(l)/l²≤4D.

In particular l=2k belongs to the far range. This proves the stated
bound on the complete nonnegative generator series.

For the consequence, give each point in cluster k payoff F(k).
Coordinate reciprocal-square summability follows from Σ m_k/k²<∞,
so Lemma 107 defines the process. Internal cluster payoff increments
are zero. Between clusters k<l the distance is at least
l−k−1/4≥3(l−k)/4. Thus the full pointwise payoff generator is bounded
by C=(16/9)(4+2A+4D).

Apply the finite-cluster cutoff argument proved in Lemma 111: stop
at the first arrival in a cluster with label at least R, retaining
all exit rates and assigning the absorbing state payoff F(R).
This cap decreases generator increments. The finite-state expectation
identity gives, from starting cluster k_0<R,

P(tau_R≤t)≤[F(k_0)+Ct]/F(R).

Each cluster is finite, so the exit times increase to the full
lifetime, on the holding-time construction before assuming nonexplosion.
Letting R tend to infinity proves infinite lifetime almost surely.
Lemma 107 then gives the height-dependent selection conclusion. ∎

## Qualifications

No bound on individual M_j other than weighted summability is imposed,
and no decay rate of the tails is assumed. The spike locations need
not be powers of two. The separation condition is additional to
summability; the proof does not cover arbitrary count sequences.
This extends the explicit example in Lemma 112, which is a comparison,
not an input to this proof. General coordinate selection and RH remain
unproved. The selected upward subsequence may depend on the heights.

## Verification and formalization obligations

The proof is analytic and requires no numerical certificate. Audit
recursive tail thresholds, local finiteness, divergence of P, the strict
jump convention, nonnegative interchange, the location count bound,
the empty near range at k=1, and the far boundary l=2k. The cluster
application uses only the bounded-generator cutoff portion of Lemma
111, not its count envelope. Formalization would require these elementary
estimates, that cutoff argument, and the process and selection statement
of Lemma 107.
