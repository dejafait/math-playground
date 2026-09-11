# Lemma 219: single-factor slice and real-measure obstruction

**Hypotheses.** Use Q_N, the exact normalized length e, fixed boxes,
and scales of L218. Write v=cd and fix integers a,c,d in those boxes.
For each m in M_in define the closed real interval

I_m=[(m²-R+1)/(a(v+1)), (m²+R)/(av)] intersect [N,2N].

For integer b define e_m(b) to be max(t_0-b_0,0)/R using L191's
exact endpoints with u=ab, without imposing the gcd condition.

**Conclusion.** The exact slice contribution is

q(a,c,d)=sum_(m in M_in) sum_(b in I_m intersect Z)
       [phi(ab)/(ab)] e_m(b) 1_{gcd(m,ab)=1}.                 (1)

The nonempty intervals I_m are pairwise disjoint for sufficiently
large N. Their union has real length O(h/N). The integer slice has
q(a,c,d)=O(h/N+1)=O(sqrt(N)), giving only Q_N=O(N^(7/2)).

For a precise limitation of the real-length approach, suppose this
slice has at least eta h distinct m in M_in satisfying

N+1 <= m²/(av) <= 2N-1,                                  (2)

where eta>0 is fixed. Then the real length of the union is also
bounded below by a positive constant times h/N. This is a statement
about a relaxed real support, not about the integer sum (1). No
O(N³) bound or contrary lower bound for Q_N follows.

**Proof.**

The necessary inequalities for a nonempty cell are

abv-R <= m² <= ab(v+1)+R-1.

As a,v are positive, solving these inequalities for b gives exactly
b in I_m. Conversely b in I_m need not satisfy all exact cutoffs;
that is why e_m(b) remains in (1). An exact positive length implies
membership, and L218 identifies the only possible integer m for
any integer b. Exchanging finite sums and retaining the gcd gives
(1). In particular square products still contribute zero by L218.

The same uniqueness proof applies to real b in [N,2N]: the possible
m interval has width at most 5/8+O(N^(-1/2))<1. It uses only the
bounds on ab and cd, not integrality of b. Thus two distinct integer
m cannot have intersecting I_m.

Before intersecting with [N,2N], the length of I_m is exactly

D_m=m²/[av(v+1)] + R/(av) + (R-1)/[a(v+1)].              (3)

Uniformly for m in M_in, m is comparable to N², a to N, and
v to N². Hence D_m is comparable to 1/N; the two R terms are
O(N^(-3/2)). There are O(h+1)=O(h) integers in M_in because
its enclosing interval [a−,a+] has length h/(2 pi). Summing
(3) proves the real-length upper bound.

For (2), put z=m²/(av). The upper endpoint before clipping is
z+R/(av), and the lower is z-z/(v+1)-(R-1)/(a(v+1)).
Both differ from z by O(1/N), so neither is clipped when (2)
holds, eventually. Each of the stipulated eta h intervals therefore
has length at least c/N. Disjointness proves the conditional lower
bound. This does not assert that (2) holds for every slice.

For the integer upper bound it is better to use the enclosing support
than sum one rounding error for each of O(h) intervals. L213's
necessary product interval J_v has length O(h). Thus all eligible
integer b belong to (J_v/a) intersect [N,2N], an interval of length
O(h/N) with at most O(h/N+1) integers. Since e_m(b)<=2,
phi(ab)/(ab)<=1, and each b belongs to at most one I_m, (1)
gives the stated bound. There are O(N³) triples a,c,d, proving
the aggregate bound.

## Qualifications, verification, and formalization

The exact sum retains all stationary cutoffs, normalized lengths,
and gcd(m,ab)=1. The intervals are only a necessary-support
relaxation. In particular neither their real lengths nor a count of
nonsquare products replaces these weights. Summing real lengths
in a slice satisfying (2) is already of order sqrt(N); a real-volume
upper bound of order one in such a slice is false. Even that fact
does not establish a lower bound on its integer population. The
remaining saving must control the arithmetic sum, on average over
triples; a uniform O(1) slice estimate is not claimed necessary.

Verification is analytic: inversion of two linear inequalities,
the exact subtraction (3), real-variable uniqueness, and the integer
count in an enclosing interval. Formalization requires these finite
identities, uniform scale bounds, and the conditional disjoint-length
sum. Q_N=O(N³), the signed comparison, and RH remain unproved.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
