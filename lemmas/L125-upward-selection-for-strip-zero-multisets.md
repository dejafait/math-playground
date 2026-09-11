# Lemma 125: upward selection for strip zero multisets

**Hypotheses.** Let (z_i) be a nonempty finite or countable multiset of
points z_i=a_i+ib_i with a_i real and 0<b_i≤H=sup_i b_i<∞. Count
all multiplicities in the assumption

Σ_i (1+|z_i|²)^(-1)<∞.

Define the upward contribution, also counting destination multiplicity, by

E_i=2Σ_(j:b_j>b_i) (b_j−b_i)/|z_j−z_i|².                 (1)

**Conclusion.** Every E_i is finite. For every δ,ε>0 there is a copy i
with b_i>H−δ and E_i<ε. If H is attained, E_i=0 at every copy at
height H. If H is not attained, one can select copies with |z_i|→∞,
b_i→H, and E_i→0. Repeated real parts and repeated points are allowed.

## Proof

The summability assumption implies that every bounded disk contains
only finitely many copies: each copy in the disk of radius R contributes
at least (1+R²)^(-1). In particular every multiplicity is finite and
each distinct location is isolated. For fixed i, all sufficiently large
|z_j| satisfy |z_j−z_i|≥|z_j|/2, so their inverse squared distances
are summable. The remaining strictly higher destinations are finite
in number and distinct from z_i. Thus their exact rates

q_ij=1/|z_j−z_i|², for b_j>b_i,

have a finite row sum K_i. This also proves E_i≤2H K_i<∞.
The attained-supremum conclusion is immediate. Henceforth suppose H
is not attained; there must be infinitely many distinct locations.

### Distinct auxiliary coordinates

For each copy let d_i be the distance from z_i to the nearest distinct
location, or equivalently the infimum over those locations. This is
strictly positive: locations in a fixed neighborhood are finite, and
locations outside that neighborhood have a positive distance bound.
Choose, successively in any enumeration, numbers

0<η_i<min(1,d_i/4),    t_i=1+|z_i|+η_i,

so that all t_i are distinct. At each stage only finitely many values
are forbidden in a nonempty open interval. Copies at one location
receive distinct t_i as well. For distinct locations i,j, the reverse
triangle inequality and d_i,d_j≤|z_i−z_j| give

|t_i−t_j|≤||z_i|−|z_j||+η_i+η_j
         ≤(3/2)|z_i−z_j|.

Consequently every strictly upward rate satisfies

q_ij≤(9/4)/(t_i−t_j)².                              (2)

No inequality is needed between copies at the same location, since
there is no strictly upward transition between them. Also

Σ_i t_i^(-2)≤Σ_i (1+|z_i|²)^(-1)<∞.

The t_i are locally finite and unbounded, so relabel the copies in
strictly increasing t order. Lemma 122 supplies a positive increasing
unbounded f(i) and a finite B with

Σ_(j>i)(f(j)−f(i))/(t_j−t_i)²≤B.                    (3)

### Height-directed nonexplosion

Fix δ>0 and restrict states to A={i:b_i>H−δ}. From each i in A jump
only to strictly higher destinations, with the exact rates q_ij above.
All destinations remain in A. Nonattainment makes 0<K_i<∞ at every
state. Construct the embedded chain Y_m with probabilities q_ij/K_i,
and independent mean-one exponential variables Z_m. Its lifetime is

T=Σ_(m≥0) Z_m/K_(Y_m).

Heights strictly increase, so no copy is revisited. From (2) and (3)
the positive part of the generator applied to f is at most C=9B/4.
All negative terms have j<i and are finite in number. The full
generator is therefore well defined and bounded above by C.

We give the finite cutoff justification, as in Lemma 124. Start at
n in A. For R>n stop at the first visited index at least R, at time
τ_R. Collapse all these exit destinations to a single absorbing state,
retaining the complete exit-rate sum at each transient state. Before
exit this is a finite-state chain on A∩{1,…,R−1}. Give transient
state i payoff f(i) and the absorbing state payoff f(R). Since every
exit destination j≥R has f(j)≥f(R), this capping can only decrease
the generator. Its upper bound remains C. The finite-state expectation
identity justified in Lemma 108 yields

P_n(τ_R≤t)≤(f(n)+Ct)/f(R).                          (4)

All these finite chains couple to the embedded construction until exit.
Exit takes finitely many jumps almost surely, since states cannot
repeat and there are only finitely many below R. Let M_R be the first
jump index with Y_(M_R)≥R. The M_R increase to infinity as R→∞:
every finite path prefix has a finite largest index. Thus
τ_R=Σ_(m<M_R)Z_m/K_(Y_m) increases to T, and {T≤t} is contained
in {τ_R≤t}. Let R→∞ in (4) and then take the union over positive
integer t. This proves T=∞ almost surely without assuming an
infinite-state stopping identity.

### Bounded-height contradiction and selection

If E_i≥ε for all i in A, the exact height generator satisfies

Σ_(j:b_j>b_i)q_ij(b_j−b_i)=E_i/2≥ε/2.

Conditional expected height increments in the embedded chain equal
this generator divided by K_i. Finite telescoping consequently gives

(ε/2) E_n[Σ_(m<M)1/K_(Y_m)]
 ≤ E_n[b_(Y_M)]−b_n ≤ H−b_n.

Nonnegative monotone convergence, followed by the independent unit
means of Z_m, implies E_n[T]≤2(H−b_n)/ε<∞, contradicting
nonexplosion. Therefore some i in A has E_i<ε, as claimed.

For the last assertion, exclude the finitely many copies in the disk
|z|≤r. Their maximum height is strictly below H. Choose δ_r<1/r
also smaller than the difference between H and that maximum whenever
the excluded set is nonempty. Apply the assertion with δ_r and ε=1/r.
The selected copy lies outside the disk, has height tending to H, and
has contribution tending to zero. ∎

## Qualifications and verification

This is a fixed-configuration statement, not an assertion that all
points are simple zeros or that a multiple zero has a differentiable
trajectory. Coincident copies have equal height and are excluded from
(1); no division by zero is performed. Both signs of the real part and
the imaginary axis are included directly, without symmetry assumptions.
For a symmetric zero multiset the reflected upper zeros are simply
additional destinations in (1). In a bounded strip the stated weight
is equivalent to (1+a_i²)^(-1), since
1+a_i²≤1+|z_i|²≤(1+H²)(1+a_i²).

Analytic verification checks finite disk counts including multiplicity,
isolation, the recursive perturbation, the direction and factor 9/4
in (2), auxiliary-coordinate summability and sorting, complete rate
tails, negative backward increments, finite-state capping, lifetime
limits, and the exact height-generator identity. No numerical
certificate is required. L122 supplies the payoff; L124 supplies the
adapted cutoff argument; L108 supplies its finite-state identity.

Formalization would require countable multiset enumeration, discrete
location distances, recursive avoidance of finitely many coordinates,
the payoff application, and the finite-chain and monotone-convergence
steps displayed above. Uniformity in a heat parameter, control of
multiple-zero splitting, differentiation of a moving supremum, and
RH remain unproved.
