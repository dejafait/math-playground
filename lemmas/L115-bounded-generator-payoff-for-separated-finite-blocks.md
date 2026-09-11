# Lemma 115: bounded-generator payoff for separated finite blocks

**Hypotheses.** Let [a_j,b_j], j≥1, be finite integer intervals with
1≤a_j≤b_j and a_(j+1)≥4b_j. At each integer l in their union prescribe
a nonnegative integer M_l, and set M_l=0 outside the union. Suppose

A:=Σ_j w_j<∞, where w_j:=Σ_(l=a_j)^(b_j) M_l/l².

Put m_l=1+M_l for every positive integer l.

**Conclusion.** There is a positive strictly increasing unbounded
function F on the positive integers such that

D:=Σ_l m_l F(l)/l²<∞,
sup_k Σ_(l>k) m_l(F(l)−F(k))/(l−k)²≤4+2A+4D<∞.

For arbitrary clusters of m_k distinct points in [k,k+1/4], the forward
jump process of Lemma 107 is nonexplosive from every starting point.
Every strictly increasing positive bounded height sequence on the
increasing cluster union admits a subsequence with full upward
contribution tending to zero, in the sense of Lemma 107.

## Proof

Choose strictly increasing positive integers J_h such that
Σ_(j>J_h) w_j≤2^(-h), for h≥1. The convergent nonnegative series
allows this recursive choice, including when A=0. Define

P(k)=1+Σ_(h≥1) 1_{b_(J_h)<k},
B(k)=1−1/(k+1), and F(k)=P(k)+B(k).

Since b_(j+1)≥a_(j+1)≥4b_j, endpoints tend to infinity and the
sum defining P is locally finite. Every selected endpoint is eventually
passed, so P is unbounded. B is positive and strictly increasing;
therefore F is positive, strictly increasing and unbounded. At most
1+log₂ k endpoints are at or below k, giving F(k)≤3+log₂ k.
Thus the unit-baseline sum Σ_k F(k)/k² converges by the integral test.

For l in block j, precisely the selected endpoints of earlier blocks
are below l. In particular a jump strictly after b_j has not yet
occurred anywhere in block j. Consequently

P(l)=1+#{h:J_h<j}, for a_j≤l≤b_j.

Interchanging nonnegative sums yields

Σ_l M_l P(l)/l²
 =Σ_j w_j+Σ_h Σ_(j>J_h) w_j≤A+1.

Since 0<B(l)<1, its extra-mass weighted sum is at most A. This
proves D<∞. Also Σ_l m_l/l²<∞ directly from the hypothesis.

Fix k≥1 and first take k<l<2k. At most one endpoint lies in [k,l):
if u<v were two, v≥4u≥4k>l, a contradiction. Thus
P(l)−P(k)≤1 and B(l)−B(k)≤1. The unit-baseline contribution
in this near range is at most

2Σ_(d≥1) d^(-2)≤4,

using Σ d^(-2)≤1+∫_1^∞ t^(-2)dt=2.

Now let l be any location of extra mass in block j in this near
range. For j>1 every preceding endpoint is at most

b_(j−1)≤a_j/4≤l/4<k.

Its own endpoint is b_j≥l and every later endpoint is larger.
Hence no endpoint lies in [k,l), and P(l)=P(k). For j=1 the
same conclusion holds because there are no preceding endpoints.
The extra contribution at this location is therefore

M_l(B(l)−B(k))/(l−k)²
 =M_l/[(k+1)(l+1)(l−k)]
 ≤(M_l/l²) l/[(k+1)(l−k)]≤2M_l/l².

The last inequality uses l<2k and the integer spacing l−k≥1.
Summing over all near mass locations gives at most 2A. The number
of masses and the width of their block do not enter this estimate.

For l≥2k, l−k≥l/2 and F(l)−F(k)≤F(l), so the full far sum is
at most 4Σ_(l≥2k) m_l F(l)/l²≤4D. This range includes l=2k;
for k=1 the near range is empty. These estimates prove the generator
bound and convergence of its entire nonnegative series.

For the cluster consequence, assign payoff F(k) to every point of
cluster k. Coordinate reciprocal-square summability follows from
Σ m_k/k²<∞, so Lemma 107 defines the process and its finite rates.
Payoff increments inside a cluster vanish. Between clusters k<l the
coordinate distance is at least l−k−1/4≥3(l−k)/4, so the pointwise
payoff generator is bounded by C=(16/9)(4+2A+4D).

Apply the bounded-generator cutoff argument proved in Lemma 111:
stop at first arrival in a cluster with label at least R, keep the
full exit rates, and assign the absorbing state payoff F(R). There
are finitely many transient points. Capping the payoff decreases exit
increments, so the finite-state expectation identity gives, from
cluster k_0<R,

P(tau_R≤t)≤[F(k_0)+Ct]/F(R).

On the original holding-time construction tau_R increases to the
lifetime T, since the chain moves strictly forward and every cluster
is finite. In particular {T≤t} is contained in {tau_R≤t}. Letting
R tend to infinity proves P(T≤t)=0 for each finite t; a union over
integer t proves nonexplosion. Lemma 107 then gives the asserted
height-dependent upward subsequence. ∎

## Qualifications

This completes the finite-block test, including the requested subclass
b_j≤2a_j. That width condition is unnecessary: only the separation
between successive blocks is used. Arbitrary mass amplitudes and finite
block widths are permitted, subject to weighted summability. Separation
remains additional to summability; arbitrary counts, general coordinate
selection and RH remain unproved. The subsequence may depend on heights.
Lemma 114 motivates the construction but is not a mathematical input.
Only the bounded-generator cutoff argument of Lemma 111 is used, not
its linear count envelope.

## Verification and formalization obligations

The proof is analytic and needs no numerical certificate. Audit the
recursive thresholds, endpoint growth and local finiteness, unboundedness,
nonnegative interchange, constancy of P including both block endpoints,
near cancellation for all interior masses, singleton and arbitrarily
wide blocks, a_1=1, k=b_j, l=b_j, and the l=2k boundary. Check the
zero internal increments, retained exit rates, payoff-cap direction and
lifetime coupling. Formalization would require these elementary bounds
and the cutoff and process statements invoked above.
