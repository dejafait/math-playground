# Lemma 120: nonexplosion for unrestricted separated cluster counts

**Hypotheses.** For each integer k≥1 let C_k consist of m_k distinct
points in [k,k+1/4], where m_k is a positive integer and
Σ_k m_k/k²<∞. Enumerate their union as x_1<x_2<⋯. Use the forward
jump process of Lemma 107, with rates q_ij=(x_j−x_i)^(-2), total
rates K_i=Σ_(j>i)q_ij, and lifetime T.

**Conclusion.** For every starting index n, P_n(T=∞)=1. For every
strictly increasing positive bounded height sequence b_i, the full
upward contributions E_i defined in Lemma 107 satisfy liminf_i E_i=0.
In particular there are increasing indices i_r with E_(i_r)→0; they
may depend on the heights. No upper envelope on m_k beyond the stated
weighted summability is required.

## Proof

Every bounded interval contains only finitely many points, and
Σ_i x_i^(-2)≤Σ_k m_k/k²<∞. Lemma 107 therefore supplies finite
positive rates and the embedded chain Y_s with its independent
mean-one exponential variables Z_s. All probability statements below
refer to this holding-time construction, even before nonexplosion has
been established.

Apply Lemma 119 to obtain an increasing positive unbounded F with

B_F:=sup_k Σ_(l>k) m_l(F(l)−F(k))/(l−k)²<∞.

Let c(i) be the cluster label of x_i and set f(i)=F(c(i)). We apply
the finite-cluster cutoff argument of Lemma 111, now with this payoff.
Within one cluster the payoff increment is zero. Between clusters
k<l, the distance is at least l−k−1/4≥3(l−k)/4. Hence

Σ_(j>i) q_ij(f(j)−f(i))≤(16/9)B_F=:B<∞.          (1)

This estimate involves only nonnegative summands and allows arbitrarily
small distances inside any finite cluster.

Fix a starting index n, put k_0=c(n), and take an integer R>k_0.
Let M_R=min{s≥0:c(Y_s)≥R}, and let

τ_R=Σ_(s=0)^(M_R−1) Z_s/K_(Y_s).

Since the embedded chain strictly increases its index and only finitely
many points have cluster label less than R, M_R is finite. Each holding
time is finite almost surely, so τ_R is finite almost surely. Collapse
all destinations with cluster label at least R into one absorbing state
∂. The resulting chain has a finite set of transient states i≥n with
c(i)<R. Its rates to other transient states are q_ij, and its rate to
∂ is the full convergent sum Σ_(j:c(j)≥R)q_ij. Thus its total holding
rate is exactly K_i. This chain agrees in law with the original process
up to τ_R; retaining the full exit sum is essential.

Assign payoff g_R(i)=f(i) to transient states and g_R(∂)=F(R).
For every exit destination j, F(R)≤f(j), so replacing f(j) by F(R)
only decreases its nonnegative generator increment. Equation (1)
therefore bounds Q_R g_R by B on transient states; at ∂ it is zero.
The finite-state expectation identity justified in Lemma 108 gives,
for every finite t≥0,

E_n[g_R(X_t)]≤F(k_0)+Bt.

All payoffs here are nonnegative and the absorbing payoff is F(R).
Consequently

P_n(τ_R≤t)≤(F(k_0)+Bt)/F(R).                     (2)

No infinite-state expectation identity has been used.

On the original holding-time space, τ_R increases to T as R→∞.
Indeed M_R is nondecreasing; for each fixed s, all of Y_0,...,Y_s
have finite cluster labels, so M_R>s for sufficiently large R.
Thus the increasing partial sums defining τ_R eventually include each
holding-time term. In particular {T≤t}⊆{τ_R≤t}. Since F(R)→∞,
(2) implies P_n(T≤t)=0. Taking the union over positive integer t
proves P_n(T<∞)=0. The starting index was arbitrary.

The hypothesis of the final implication in Lemma 107 now holds from
every index. That implication proves the asserted height-dependent
vanishing subsequence and hence the zero lower limit. ∎

## Qualifications

This removes the count envelope from the separated-cluster result,
not the geometric separation hypothesis. For arbitrary coordinates
satisfying Σ_i x_i^(-2)<∞, unit-cell counts are finite and weighted
summable (after treating finitely many initial points), but points in
adjacent cells can be arbitrarily close. The distance comparison used
in (1) then fails: points at k+1−δ and k+1+δ have cell-label difference
one but distance 2δ. Taking δ arbitrarily small precludes any uniform
positive lower comparison constant. This observation is a gap in that
extension, not a counterexample to general nonexplosion. No assertion
is made here that a different partition or payoff cannot work.

No common subsequence for all heights, heat-parameter uniformity,
zero continuation, or RH conclusion follows from this result.

## Verification and formalization obligations

The proof is analytic and requires no numerical certificate. The audit
checks the hypotheses of Lemma 119, reciprocal-square summability,
zero internal increments, the 16/9 distance factor, finiteness of every
cutoff, retention of all exit rates, the direction of the payoff cap,
and convergence on the original holding-time space. Formalization
requires the payoff existence theorem, finite-state expectation identity,
finite exit coupling, monotone limits of nonnegative sums, and the
height-selection implication. All such earlier inputs are used only
with their stated hypotheses; no unrestricted-coordinate claim is
assumed in proving the cluster case.
