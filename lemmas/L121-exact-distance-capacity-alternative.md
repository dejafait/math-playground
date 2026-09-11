# Lemma 121: exact-distance capacity alternative

**Hypotheses and definitions.** Let 0<x_1<x_2<⋯ with
W=Σ_j x_j^(-2)<∞. For i≤n put

A_in=Σ_(j>n)(x_j−x_i)^(-2),

and set A_in=0 for i>n. Define

C_N=max{Σ_(n≤N)d_n : d_n≥0, Σ_(n=i)^N A_in d_n≤1 for i≤N}.

A cover is a sequence y_i≥0 with Σ_i y_i<∞ and
Σ_(i≤n)y_i A_in≥1 for every n.

**Conclusion.** Exactly one of the following holds:

- C_N→∞, and there is a positive strictly increasing unbounded sequence
  f(i) with Σ_i f(i)/x_i²<∞ and
  sup_i Σ_(j>i)(f(j)−f(i))/(x_j−x_i)²<∞.
- The capacities are bounded, and a cover exists. Its minimum total
  mass equals lim_N C_N. No payoff as in the first alternative exists.

All coefficients use actual distances, including arbitrarily close
points across any chosen cell boundary. No claim is made here that
summability of reciprocal squares determines which alternative holds.

## Proof

We adapt the finite-capacity argument of Lemma 118 and give the details
needed when its integer-distance diagonal bound is unavailable.
The summability hypothesis implies x_j→∞ and finitely many points in
each bounded interval. For fixed i, terms with x_j<2x_i are finite in
number and have positive denominators; the rest are bounded by 4/x_j².
Thus every A_in is finite, and A_nn≥(x_(n+1)−x_n)^(-2)>0.

Each feasible coordinate satisfies 0≤d_n≤1/A_nn. The finite feasible
set is compact and nonempty, so the maximum exists and is finite.
Extension by zero is feasible for every additional row, hence C_N is
nondecreasing. For arbitrary nonnegative increments, Tonelli gives

Σ_(j>i) [Σ_(n=i)^(j−1)d_n]/(x_j−x_i)²
 =Σ_(n≥i) A_in d_n.                                      (1)

If C_N→∞, choose finite feasible vectors v^(r), extended by zero,
with total mass at least 2^r. Set d_n=Σ_(r≥1)2^(-r)v_n^(r).
Each coordinate is finite by the diagonal bound. Every row is at most
one, while Σ_n d_n=∞, by nonnegative interchange. Conversely any
infinite feasible d with divergent total mass has feasible truncations
and therefore forces C_N→∞.

Finite-dimensional linear-programming strong duality identifies C_N
with the attained minimum of Σ_(i≤N)y_i under y_i≥0 and
Σ_(i≤n)y_i A_in≥1 for n≤N. Feasibility follows by taking
 y_i=1/A_ii for i≤N: each column's diagonal term alone equals one.
If C=lim C_N<∞, optimal dual vectors, extended by zero, have each
coordinate in [0,C]. Diagonal subsequence extraction gives coordinatewise
limits y_i≥0. Each finite partial sum is at most C, so Σ_i y_i≤C.
For fixed n the cover inequality is a finite sum of finite coefficients,
and survives this limit. Thus y is a cover. For any cover and any
feasible d, Tonelli gives

Σ_n d_n≤Σ_n d_n Σ_(i≤n)y_i A_in
       =Σ_i y_i Σ_(n≥i)A_in d_n≤Σ_i y_i.                  (2)

Applying this to finite optimizers shows C_N≤Σ_i y_i. The constructed
cover has mass exactly C, proves minimum attainment, and precludes
divergent feasible increments. This establishes the capacity alternative.

It remains to justify the payoff formulation, especially strict increase.
For a divergent feasible d, set f_0(i)=1+Σ_(n<i)d_n. Equation (1)
bounds its generator by one. Its weighted sum is finite because

Σ_j f_0(j)/x_j²
 ≤W+Σ_(j>1)(f_0(j)−1)/(x_j−x_1)²≤W+1.                 (3)

Here 0<x_j−x_1<x_j, and the last sum is the first generator row.
Define finite M_n=max_(1≤i≤n)A_in and positive increments

e_n=2^(-n)/(1+M_n),   h(i)=Σ_(n<i)e_n.

Then 0≤h(i)≤1, h is strictly increasing, and for each i,

Σ_(n≥i)A_in e_n≤Σ_(n≥i)2^(-n)≤1.

Equation (1) makes this a generator bound for h even when some gaps
are arbitrarily small. Thus f=f_0+h is positive, strictly increasing,
unbounded, has generator at most two, and weighted sum at most 2W+1.
No distance comparison across cells has been used.

Conversely let f have the claimed properties and generator bounded by
B<∞. Strict increase gives B>0 from the first positive term in row one.
Its increments d_n=(f(n+1)−f(n))/B are feasible by (1), with divergent
total mass because f is unbounded. Hence C_N→∞. This completes all
assertions. ∎

## Qualifications and verification

This resolves a precisely scoped part of the arbitrary-coordinate task:
it provides an exact alternative and a gap-sensitive strict correction.
It does not exclude summable covers, prove general nonexplosion, or prove
RH. Small gaps are retained in A_in and M_n; no uniform positive minimum
gap or rate bound is assumed. The earlier integer-coordinate vanishing-cut
estimate is not an input to this result and is not asserted to extend.

The verification is analytic; no numerical certificate is needed. The
audit checks full destination tails in finite programs, individual diagonal
positivity, dual feasibility without a uniform diagonal bound, zero
extension, finite-column limits, and both directions of the payoff
criterion. All infinite rearrangements involve nonnegative terms.
Formalization would require finite linear-programming strong duality,
compactness and diagonal extraction, Tonelli, the exact increment identity,
and the bounded strict-correction construction. Lemma 118 supplies the
reused proof argument; its specialized hypotheses are not assumed here.
