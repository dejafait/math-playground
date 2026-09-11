# Lemma 124: upward selection for arbitrary bounded heights

**Hypotheses.** Let 0<x_1<x_2<⋯, Σ_i x_i^(-2)<∞, and
0<b_i≤H=sup_i b_i<∞. No ordering of the heights is assumed. Put
w_i=x_i+ib_i and form the paired product

F(z)=Π_i (1−z²/w_i²)(1−z²/conjugate(w_i)²).

Define its full upward contribution at w_i by

E_i=2Σ_(j:b_j>b_i)(b_j−b_i)
 [1/((x_j−x_i)²+(b_j−b_i)²)
  +1/((x_j+x_i)²+(b_j−b_i)²)].                       (1)

**Conclusion.** For every δ>0 and ε>0 there is an index i with
b_i>H−δ and E_i<ε. If H is not attained, indices i_r can be chosen
strictly increasing with b_(i_r)→H and E_(i_r)→0. If H is attained,
every zero at height H has upward contribution zero.

## Proof

The paired product converges locally uniformly since |w_i|≥x_i
and Σ_i |w_i|^(-2)<∞. The usual convergent-product argument (the
summable factor deviations give a nonzero tail away from the factors'
zeros) shows its zeros are exactly ±w_i, ±conjugate(w_i), all simple:
positive distinct x_i and positive b_i make these points distinct.
It is even and real entire, with F(0)=1. The only zeros higher than
w_i are w_j and −conjugate(w_j) for b_j>b_i, giving (1).

For j≠i set

q_ij=1/(x_j−x_i)²+1/(x_j+x_i)².

Each row Σ_(j≠i)q_ij is finite. Its finite prefix has no zero
denominators, and when x_j≥2x_i its terms are at most 5/x_j².
Consequently (1) is finite and nonnegative.

If H is attained, its assertion is immediate from the empty higher
set. Assume henceforth that H is not attained. Fix δ>0 and restrict
the state space to A={i:b_i>H−δ}. From state i∈A allow transitions
only to j with b_j>b_i, at rates q_ij. Every such j belongs to A.
The total rate K_i is finite and strictly positive, since some height
exceeds b_i. Construct the embedded chain Y_m by normalized rates,
and independent mean-one exponentials Z_m, with lifetime

T=Σ_(m≥0)Z_m/K_(Y_m).

This construction makes sense before any nonexplosion assertion.
Heights strictly increase at every jump, so no state is ever revisited.

By Lemma 122 there is a positive increasing unbounded f with
Σ_(j>i)(f(j)−f(i))/(x_j−x_i)²≤B for all i. Since
(x_j+x_i)^(-2)≤(x_j−x_i)^(-2), the positive part of the
height-directed generator satisfies

Σ_(j>i, b_j>b_i)q_ij(f(j)−f(i))≤2B.                (2)

The remaining terms have j<i, are finite in number, and are negative.
The full generator is thus well defined and at most 2B.

Here is the finite cutoff justification, extending the argument of
Lemma 123 to paths whose indices need not increase. Start at n∈A
and let R>n. Stop on the first visited index at least R, at time τ_R.
Before exit all states belong to the finite set A∩{1,…,R−1}.
There can be at most R−1 visits there since none repeats. Each holding
time is finite almost surely, so exit occurs after finitely many jumps.
Collapse all exit destinations to a single absorbing state ∂, retaining
the complete exit-rate sum. This is a finite-state chain agreeing with
the original construction until exit. Give it payoff f(i) at transient
states and f(R) at ∂. Capping each exit payoff decreases its generator,
because exit destinations j≥R have f(j)≥f(R). Equation (2), including
the negative backward terms, gives generator at most 2B everywhere.
The finite-state expectation identity used in Lemma 108 therefore gives

P_n(τ_R≤t)≤(f(n)+2Bt)/f(R), t≥0.                  (3)

Only a finite matrix and bounded finite-state payoff occur in this
identity; no infinite-state stopping formula is assumed.

On the original path let M_R=min{m:Y_m≥R}. These jump indices are
nondecreasing in R and tend to infinity: any fixed finite initial
segment of the path has a finite largest index. Each M_R is finite,
as infinitely many distinct states cannot stay below R. Thus
τ_R=Σ_(m<M_R)Z_m/K_(Y_m) increases to T pathwise. In particular
{T≤t}⊆{τ_R≤t}. Let R→∞ in (3), then take the countable union
over integer t, to conclude T=∞ almost surely from every n∈A.

Suppose now E_i≥ε>0 for all i∈A. Removing the nonnegative vertical
squares in (1) gives the finite height generator

L b(i)=Σ_(j:b_j>b_i)q_ij(b_j−b_i)≥E_i/2≥ε/2.

The normalized transition row has conditional expected height increase
L b(i)/K_i. For every integer M≥1 finite telescoping gives

(ε/2) E_n[Σ_(m<M)1/K_(Y_m)]
 ≤E_n[b_(Y_M)]−b_n≤H−b_n.

All increments are nonnegative and bounded; these inequalities also
establish the displayed integrability. Monotone convergence and the
independent unit means of Z_m yield E_n[T]≤2(H−b_n)/ε<∞.
This contradicts nonexplosion. Therefore inf_(i∈A) E_i=0, proving
the first assertion for nonattained H.

Finally, having selected i_(r−1), choose δ_r>0 less than 1/r and
less than H−max_(i≤i_(r−1))b_i, which is positive by nonattainment.
For the first choice use an empty excluded prefix. Apply the assertion
with this δ_r and ε=1/r. The resulting index exceeds the previous
one, its height tends to H, and its contribution tends to zero. ∎

## Qualifications and verification

The extension uses L123's finite cutoff argument, not an application
of its forward-only conclusion to an unordered height sequence. L122
provides the controlling payoff and L108 the finite-state expectation
identity. Reflected higher zeros are included directly in q_ij, so no
uniform reflected-tail estimate or omitted leftward contribution is
needed. This is a fixed-configuration theorem for distinct positive
horizontal coordinates. Repeated horizontal coordinates, multiplicities,
and uniform heat-parameter control are not addressed. No RH assertion
or derivative bound for a moving height supremum follows here.

Analytic verification checks row finiteness, the sign of backward
payoff increments, complete exit rates, absence of repeated states,
pathwise exit-time convergence, bounded height telescoping, and the
finite-prefix exclusion used for selection. No numerical certificate
is needed. Formalization would require convergent product zero sets,
countable transition sampling, finite-state expectation identities,
nonnegative monotone convergence, and the stated subsequence extraction.
