# Lemma 612: microscopic blocks saturate the count-only charged-height test

## Hypotheses

All logarithms are natural. Put H0=3.0610046·10^10. For each real
T≥2H0, set

    L=log T, d=1/L, h=4/L, n=floor(T/h),
    γ_j=T+jh  (j=0,…,n).

Form the finite multiset Z_T consisting of γ_j+id, γ_j−id and
their negatives, each with multiplicity one. Thus every conjugate block
has the same positive integer multiplicity. Define, for real σ and H>0,

    N_T(σ,H)=#{j: 0<γ_j≤H and 1/2+d>σ}.

This counts one right-side representative β=1/2+d per positive-ordinate
block, with its multiplicity, not both members of that block. Under the
coordinate convention s=1/2+iz, that representative is z=γ_j−id.
Define the strict charged degree for real t by

    K_T(t)=2 #{j: |γ_j−t|<d}.

Since d<1/2<2, every charged block is inside the near window
|γ_j−t|<2. This is the charge rule of C464c, restated as a definition
for Z_T; its actual-Xi coefficient theorem is not applied to Z_T.

## Conclusion

For every T≥2H0, every H≥H0 and every 1/2≤σ≤0.831,

    N_T(σ,2H)−N_T(σ,H)
      ≤10395.2 H^(1−(σ−1/2)/4) log H
        +1.104 log² H+0.173 log H log log H+0.51 log H.       (1)

For every v≥0, the total number of positive-real-part members of Z_T
in the closed ordinate interval [v,v+1], counting both members of each
block with multiplicity, is at most log(v+2). In z-coordinates this
means counting members with Re(z) in [v,v+1]. Thus the model meets the
required closed-unit local-count condition with an absolute constant
independent of T and v.

Let r=T−nh, so 0≤r<h. With Lebesgue measure,

    meas{t∈[T,2T]: K_T(t)>0}
       =2nd+min(d,r)
       ≥T/2−1/log T ≥T/3.                                (2)

In particular the measure is T/2+O(1/log T), with an absolute constant.
The two specified count conditions, even with conjugation/reflection
symmetry and positive integer multiplicities, therefore do not imply
that this strict charge-presence union is o(T) for abstract block
families. The constant a in d=a/log T is here fixed as a=1; the lower
measure constant c=1/3 is separate from every density-source constant.

This is not a zero set of actual Xi, an actual-Xi measure lower bound,
a counterexample to RH, or an obstruction to arguments using additional
analytic/arithmetic information. No full zero-count asymptotic, Euler
product, explicit formula, source weighted-event bound or Xi product
normalization is imposed or verified. The family depends on T; the
nonimplication concerns the stated class of finite families, as in the
approved test, not a claimed construction of a single global zeta model.

## Proof

First T≥2H0>e^4, so L>4, 0<d<1/4 and n≥1. The ordinates γ_j
are distinct, lie in [T,2T], and have spacing h=4d. Reflection gives
the negative-real-part blocks; these are not positive-ordinate zeta
representatives and contribute to neither count in the conclusion.
All four points in a block are distinct, since γ_j>0 and d>0.

### Uniform dyadic density, including microscopic σ

Write δ=σ−1/2. If δ≥d, then N_T(σ,H)=0 for every H, including
δ=d, because the β cut is strict. Hence (1) holds. Suppose 0≤δ<d.
Then the left side of (1) counts the lattice ordinates in (H,2H],
with precisely that half-open convention. If this count is zero there
is nothing to prove. Otherwise some γ_j satisfies H<γ_j≤2H and
T≤γ_j≤2T, whence

    T/2≤H<2T.                                           (3)

This includes H=T/2 if the first ordinate is at 2H; H=2T itself
has no contribution. No wholly contained dyadic slab is assumed.

An interval of length H contains at most H/h+1 ordinates of a lattice
of spacing h. Indeed, k≥1 such ordinates have span (k−1)h≤H,
which implies k≤H/h+1; this also bounds the half-open count. As
H≥H0>2 and (3) holds,

    L≤log H+log 2≤2 log H,
    N_T(σ,2H)−N_T(σ,H)
      ≤HL/4+1≤(H log H)/2+1≤H log H.                  (4)

The final inequality uses H log H≥2. On the other hand (3), T≥2
and δ<1/L give

    δ log H/4≤log(2T)/(4 log T)≤1/2,
    H^(−δ/4)≥exp(−1/2)>1/2.                           (5)

For completeness exp(1/2)<2 follows by comparing its power series
Σ_(k≥0)(1/2)^k/k! with Σ_(k≥0)(1/2)^k=2, strictly at k=2.
Thus the leading term on the right of (1) alone is greater than
5197.6 H log H, which dominates (4). All its remaining displayed
terms are positive for H≥H0. This proves (1) for every allowed H
and σ, with no fixed-σ limit, omitted microscopic case, or endpoint
rounding assumption. In fact the argument also bounds any larger σ
with δ≥d by zero; it does not apply the source theorem outside its range.

### Closed unit intervals and multiplicities

If [v,v+1] contains k≥1 lattice ordinates, their span gives
k≤1/h+1, including the case when both endpoints are ordinates. Each
supplies two positive-real-part members, each of multiplicity one, so
the required local count is at most

    2k≤2/h+2=L/2+2≤L.                                 (6)

Nonemptiness also gives v+1≥T and hence v+2≥T+1>T. Consequently
L≤log(v+2), proving the stated bound. For empty intervals it holds
since log(v+2)>0 for v≥0. The negative blocks have real parts <0
and cannot enter [v,v+1]. This checks both members, the common integer
multiplicity and the closed endpoints, uniformly in v and T.

### Strict charge union and both clipped ends

Since K_T is a sum of nonnegative degree-two charges,

    {t∈[T,2T]: K_T(t)>0}
       =[T,2T] ∩ ⋃_(j=0)^n (γ_j−d,γ_j+d).              (7)

No block at equality |γ_j−t|=d is charged. The open intervals in
(7) are disjoint because their centers have distance 4d>2d.
Clipping affects their endpoints as follows. The first, centered at
T, has length d in the slab. For 1≤j≤n−1 the interval is wholly
inside the slab and has length 2d: the first such center is at least
4d from T and the last at least 4d from 2T. The last center is
γ_n=2T−r with 0≤r<4d. Its lower half is wholly retained since
n≥1, and its upper half has length min(d,r). Its clipped length
is therefore d+min(d,r). This also covers r=0, when the last
center is exactly 2T; n=1 simply has no interior intervals.
Open/closed boundary choices change none of these lengths.

Adding these disjoint lengths proves exactly

    d+2d(n−1)+d+min(d,r)=2nd+min(d,r).

Since T=4nd+r, this length equals

    T/2+min(d,r)−r/2.

For 0≤r≤d the correction is r/2, in [0,d/2]. For d≤r<4d
the correction is d−r/2, in (−d,d/2]. This includes r=0 and
r=d and proves the bounds T/2−d≤meas≤T/2+d/2 uniformly in T.
Here T log T>6, so d≤T/6, and the lower bound is at least T/3.
These bounds prove (2) and its asserted asymptotic, with the strict
charge threshold and both clipped endpoints retained.

If the two displayed count conditions implied a uniform o(T) union
bound for this class, applying it to this family for every T≥2H0
would contradict the ratio lower bound 1/3. This proves only the
specified nonimplication. No sign of a coefficient of Xi is deduced. ∎

### Independent audit and correction (2026-11-01)

The original exact expression was (2n+1)d+min(d,r). It exceeded
the sum of the stated clipped lengths by d, including when r=0;
that equality was false. The original floor-only justification of
the T/2−d lower bound also did not follow from the corrected sum.
The corrected equality and the two cases for r above repair both
claims; the T/3 conclusion and count-only nonimplication survive.
The original scratch calculation and dated history remain preserved.

The independent audit replayed all H≥H0, the strict σ cut including
δ=d, the two possible members and both closed-unit endpoints,
and every clipped interval, including r=0, 0<r<d and d≤r<4d.
The density estimate is checked directly for this finite family,
not imported as a theorem about it. No positivity theorem for actual
Xi, infinite-product interchange or full zero-count asymptotic is an
input. This audit accepts only the corrected finite-family result.

### Source comparison and justification of this calculation

The numerical condition (1) is the statement of Aleksander Simonic,
*Explicit zero density estimate for the Riemann zeta-function near
the critical line*, arXiv:1910.08274v2 (29 November 2019), Theorem 1,
pp. 1–2; boundary/multiplicity cases are discussed in Sections 4.2
and 4.5, especially (74). [Primary source](https://arxiv.org/pdf/1910.08274v2#page=2).
The local-count type is E. C. Titchmarsh, revised by D. R. Heath-Brown,
*The Theory of the Riemann Zeta-Function*, second edition (Oxford,
1986), Theorem 9.2, equation (9.2.1), printed p. 211:
N(u+1)−N(u)=O(log u), with multiplicities.
[Book scan](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=110).
For this model the stronger closed-unit version was proved directly
in (6); it is not inferred by discarding source endpoint issues.

These sources motivate the constraints and are not cited as proofs
of the constructed family or its measure. The saved EXPLORE assessment
records the prior primary-source comparison and lack of an inspected
matching model result; no novelty follows from that search. This
elementary calculation is necessary to distinguish the failure of
a direct source import from an actual logical nonimplication of the
specified inequalities. It does not reprove a zeta density theorem.
The proof is self-contained finite counting and interval length;
C464c and L018 are comparisons defining the intended interpretation,
not theorem hypotheses applied to the artificial points. In particular
the known source estimates are not claimed to exhaust zeta constraints.

## Mathlib

Full matching coverage and supporting formalizations were not checked.
No absence assertion or Lean verification is claimed. The proof above
is an informal exact argument; no numerical preview or computational
certificate is needed for its universal inequalities.
