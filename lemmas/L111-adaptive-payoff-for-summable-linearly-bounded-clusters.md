# Lemma 111: adaptive payoff for summable linearly bounded clusters

**Hypotheses.** Let m_k be positive integers, indexed by k≥1, with

A=Σ_{k≥1} m_k/k²<∞, and m_k≤Ck for some finite C>0.

**Conclusion.** There is a strictly increasing unbounded function
F on the positive integers, with F(k)≥1, such that

Σ_k m_k F(k)/k²<∞,
sup_{k≥1} Σ_{l>k} m_l(F(l)−F(k))/(l−k)²<∞.             (1)

Consequently, for arbitrary clusters C_k of m_k distinct points in
[k,k+1/4], the forward jump process of Lemma 107 on their increasing
union has infinite lifetime almost surely from every starting point.
Every strictly increasing positive bounded height sequence on that
union admits a subsequence with full upward contribution tending to zero.

## Proof

Put G(t)=log(log(t+e)) for real t≥1. It is strictly increasing,
unbounded and positive, and its positive derivative

G'(t)=1/((t+e)log(t+e))

is decreasing. For each j≥1 choose a real threshold R_j≥0 such that
R_{j+1}≥R_j+2 and

Σ_{l:G(l)>R_j} m_l/l²≤2^(−j).                       (2)

This is possible recursively because the convergent positive series
has tails tending to zero, and G(l) tends to infinity. Define for s≥0

phi_j(s)=min(1,max(0,s−R_j)),
h(s)=1−exp(−s)+Σ_{j≥1} phi_j(s),
F(k)=1+h(G(k)).

The sum defining h is locally finite because R_j→∞. Its ramp
intervals (R_j,R_j+1) are disjoint. On each compact interval h is
piecewise continuously differentiable with derivative between 0 and 2:
the exponential term has derivative exp(−s)≤1 and at most one ramp
has derivative 1. Integrating across the finitely many breakpoints gives

0<h(v)−h(u)≤2(v−u), for 0≤u<v.                      (3)

Strict positivity follows already from the exponential term. For any
integer J≥1, if s≥R_J+1 then the first J ramps equal 1, so h(s)≥J.
Thus F is positive, strictly increasing, and unbounded. Moreover,
0≤phi_j(G(l))≤1 whenever G(l)>R_j and it is zero otherwise. Interchanging
only nonnegative sums and applying (2) gives

D:=Σ_l m_l F(l)/l²≤2A+Σ_j 2^(−j)=2A+1<∞.            (4)

We estimate the generator in two ranges. When k<l≤2k, (3) and the
decreasing derivative of G imply

F(l)−F(k)≤2(l−k)/((k+e)log(k+e)), and m_l≤2Ck.

Consequently the near sum in (1) is at most

4C k/((k+e)log(k+e)) Σ_{d=1}^k 1/d
 ≤4C(1+log k)/log(k+e)≤8C.                          (5)

For the last inequality, log(k+e)≥1 and log(k+e)≥log k, also at k=1.
For l>2k, l−k≥l/2 and F(l)−F(k)≤F(l), so the far sum is at most

4Σ_{l>2k} m_l F(l)/l²≤4D.                           (6)

This proves (1), with bound 8C+4D, including convergence of its full
nonnegative series. The thresholds adapt to the actual summable
sequence; no uniform rate of decay of its tails was assumed.

For the consequence, enumerate the cluster union as x_1<x_2<⋯.
Each cluster is finite, and Σ_i x_i^(−2)≤A, so Lemma 107 defines its
finite positive rates q_ij=(x_j−x_i)^(−2), embedded chain, and lifetime T.
Write c(i) for the cluster label and f(i)=F(c(i)). Internal cluster
increments of f are exactly zero. If c(i)=k<l=c(j), then
x_j−x_i≥l−k−1/4≥3(l−k)/4. It follows from (5)–(6) that

Σ_{j>i}q_ij(f(j)−f(i))≤B:=(16/9)(8C+4D).             (7)

Here arbitrarily small internal gaps do not affect this bound.
Fix an initial cluster k_0 and an integer R>k_0. Stop at the first
arrival in a cluster at least R, at time tau_R. Collapse all destinations
in those clusters into one absorbing state, retaining their full summed
exit rates. Only finitely many points precede this exit. Strictly
increasing indices ensure that it takes finitely many holding times
almost surely. The finite-state chain is coupled to the original
construction through this exit, without presupposing nonexplosion.

Give transient states payoff f(i), and the absorbing state payoff F(R).
Since F is increasing, this cap only decreases the generator increments
for exits. The generator is therefore at most B by (7). The finite-state
expectation identity established in Lemma 108 yields

P(tau_R≤t) F(R)≤E[g_R(X_t)]≤F(k_0)+Bt.

The first inequality uses nonnegative payoffs and absorption at exit.
On the original holding-time probability space tau_R increases to T:
indices tend to infinity, every cluster is finite, and each fixed holding
time is included for sufficiently large R. In particular {T≤t} is
contained in {tau_R≤t}. Letting R→∞ and using F(R)→∞ gives
P(T≤t)=0 for every finite t. A union over integer t proves nonexplosion.
The height-dependent subsequence conclusion is now Lemma 107. ∎

## Qualifications

This completes a scoped part of the summability-only payoff question.
The additional linear envelope need not follow from summability: for
example, m_(2^j)=1+floor(4^j/j²) for j≥1 and m_k=1 elsewhere has
Σ m_k/k²<∞ but unbounded m_k/k. The proof above makes no assertion
about such sequences, nor does their failure of the envelope disprove
existence of an alternative payoff. General coordinate selection and RH
remain unproved. The subsequence here can depend on the heights.

## Verification and formalization obligations

This is an analytic proof; no numerical certificate is required.
The audit covers recursive thresholds, locally finite disjoint ramps,
strict increase, nonnegative series interchange, the near harmonic
estimate including k=1, and the weighted infinite tail. It also checks
zero internal increments, intercluster separation, retention of all
exit rates, the payoff-cap direction, and lifetime coupling before any
nonexplosion conclusion. Formalization would require those elementary
facts, the finite-state expectation identity from Lemma 108, and the
process and selection implication from Lemma 107.
