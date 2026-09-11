# Lemma 110: nonexplosion for logarithmic cluster counts

**Hypotheses.** For each integer k≥1 let C_k consist of m_k≥1 distinct
real points in [k,k+1/4]. Suppose M>0 and

m_k≤M k/log(k+1)^2 for all k≥1.

Enumerate the union increasingly as x_1,x_2,… and use the forward jump
process of Lemma 107, with rates q_ij=(x_j−x_i)^(-2) for j>i
and lifetime T. Internal cluster gaps have no positive uniform lower bound.

**Conclusion.** From every starting index, T=∞ almost surely. For every
strictly increasing positive bounded height sequence on these coordinates,
the full upward contributions of Lemma 107 have a subsequence tending
to zero. In particular these assertions hold for
m_k=max(1,floor(k/log(k+1)^2)).

## Proof

Reciprocal-square summability follows from
Σ_i x_i^(-2)≤M Σ_k 1/(k log(k+1)^2)<∞, using the integral test
on k≥2. Thus Lemma 107 defines finite positive total rates and a
forward embedded chain with independent exponential holding times.
Let c(i) be the cluster label of x_i, and put

F(t)=sqrt(log(t+1)), t≥1, and f(i)=F(c(i)).

F is increasing and unbounded, and
F'(t)=1/(2(t+1)sqrt(log(t+1))) is positive and decreasing.
In particular F is concave. The nonnegative generator sum has zero
terms within clusters. Between labels k<l,
x_j−x_i≥l−k−1/4≥3(l−k)/4, so

L f(i)≤(16/9) Σ_{l>k} m_l(F(l)−F(k))/(l−k)^2, k=c(i). (1)

For k<l≤2k, the count bound and concavity give

m_l≤2Mk/log(k+1)^2,
F(l)−F(k)≤(l−k)/(2(k+1)sqrt(log(k+1))).

Hence the near sum on the right of (1), before its factor 16/9, is at most

M(1+log k)/log(k+1)^(5/2)
 ≤ M(1+1/log 2)/(log 2)^(3/2).                       (2)

Here Σ_{d=1}^k 1/d≤1+log k, k/(k+1)≤1, and
1+log k≤(1+1/log 2)log(k+1). These estimates include k=1.
For l>2k, use l−k≥l/2 and F(l)−F(k)≤F(l). The far sum is at most

4M Σ_{l>2k} 1/(l log(l+1)^(3/2))
 ≤4M ∫_{2k}^∞ dt/(t(log t)^(3/2))
 =8M/sqrt(log(2k))≤8M/sqrt(log 2).                  (3)

The integral comparison uses log(l+1)≥log l and the decreasing positive
function 1/(t(log t)^(3/2)) for t≥2. In particular the full infinite
generator sum converges, and (1)–(3) give L f(i)≤B for all i, where

B=(16M/9)((1+1/log 2)/(log 2)^(3/2)+8/sqrt(log 2)).

For clarity, apply the finite-state expectation argument of Lemma 108
with a cluster cutoff, retaining every rate. Start in cluster k_0 and
fix an integer R>k_0. Stop at the first point with cluster label at least
R, and call its arrival time tau_R. There are finitely many points below
R, and indices strictly increase. Thus the exit uses finitely many
holding times and occurs almost surely. Collapse all exit destinations
to one absorbing state partial, with their full summed rate at each
transient state. This finite-state chain agrees with the original
holding-time construction through tau_R, even if internal rates are large.

Give a transient point i payoff g_R(i)=F(c(i)), and give partial payoff
F(R). Replacing an exit destination payoff F(c(j)) by F(R) only decreases
the increment. Therefore Q_R g_R≤B on transient states, and it is zero
at partial. The finite-state expectation identity proved in Lemma 108
implies

E[g_R(X_t)]≤F(k_0)+Bt,
P(tau_R≤t)≤(F(k_0)+Bt)/F(R).                         (4)

The second inequality uses nonnegative payoffs and absorption at exit.
On the original probability space tau_R increases to T: the embedded
indices tend to infinity, every cluster is finite, and every visited
holding time is included for all sufficiently large R. In particular
{T≤t} is contained in {tau_R≤t}. Since F(R)→∞, (4) yields
P(T≤t)=0 for every finite t≥0. Taking a union over positive integer t
proves nonexplosion. Lemma 107 now gives the height-dependent selection
conclusion.

Finally log(k+1)≤sqrt(k) for k≥1: the difference sqrt(t)−log(t+1)
is positive at t=1 and has derivative
(t+1−2sqrt(t))/(2sqrt(t)(t+1))≥0. Thus k/log(k+1)^2≥1,
and max(1,floor(k/log(k+1)^2))≤k/log(k+1)^2. The stated example
satisfies the hypotheses with M=1. ∎

## Qualifications

The logarithmic count example exceeds every fixed sublinear power
bound, so this extends the polynomial-count regime. It does not prove
nonexplosion for arbitrary counts with Σ_k m_k/k²<∞. The selected
subsequence may depend on the heights; no common subsequence, general
coordinate theorem, theta-specific zero assertion, or RH proof follows.

## Verification and formalization obligations

This is an analytic proof; no numerical certificate is required. The
checks are the exact zero internal increments, intercluster distance,
concavity, harmonic bound including k=1, convergent logarithmic tail,
and the direction of payoff capping. All internal and exit rates remain
in the finite matrix. The lifetime coupling precedes any nonexplosion
claim. Formalization would require these elementary estimates, cluster
enumeration, the finite-state identity and coupling from Lemma 108,
and the selection implication from Lemma 107.
