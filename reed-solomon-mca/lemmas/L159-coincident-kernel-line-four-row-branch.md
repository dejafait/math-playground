# L159 — At most two planes in the coincident-kernel-line branch

## Hypotheses

Let E be any field extension of F_97, including its algebraic closure.
Use L109's actual maps on W=E^S, with

    H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96},
    S={1,8,12,18,22,27,33}, J=H minus S.

An original label j=(I_j,K_j) has I_j in binom(S,2), K_j in
binom(J,2), and four-element support T_j=I_j union K_j. Set

    g_j(X)=product over y in J minus K_j of (X-y),
    z_j=min(S minus I_j),
    (Q_j w)_x=g_j(z_j)w_x-g_j(x)w_{z_j},
        x in (S minus I_j) minus {z_j}, in increasing order,
    V_j=ker Q_j=E^{I_j}+E (g_j(x))_{x in S}.

Here E^I denotes the coordinate subspace spanned by e_t, t in I;
the displayed kernel formula is L109's formula (3), used solely as
an identity for these maps, without its coding hypotheses.

Fix four distinct original labels a,b,c,d, with a<b and c<d in the
original 756-label lexicographic order. Assume T_a intersect T_b and
T_c intersect T_d are empty, and |T_i intersect T_j|<=1 for every
two distinct selected labels. No symmetry quotient is taken.

For a two-dimensional E-subspace L with rank(Q_j restricted to L)=1
for all four rows, write ell_j=L intersect V_j. Rank-nullity makes
each ell_j a line. The **coincident-line branch** consists of those
L for which at least two of these four lines coincide.
No coding, weight, chart, genericity or descent assumption is imposed.

## Conclusion

The coincident-line branch has at most two planes, over every E.
Its complete candidate list is the union of the following constructions
for the two groups of complementary cross pairs:

    ((a,c),(b,d)) and ((a,d),(b,c)).

For a group ((i,j),(r,s)):

1. If both I_i intersect I_j and I_r intersect I_s are empty,
   the group contributes no plane.
2. If both are nonempty, write these singletons as {t} and {u}.
   The group contributes exactly span(e_t,e_u).
3. If exactly one is nonempty, relabel the two pairs within this
   group so that I_i intersect I_j={t} and I_r intersect I_s is empty.
   The group contributes no plane unless e_t belongs to V_r+V_s.
   If it does, decompose uniquely e_t=v_r+v_s with v_r in V_r,
   v_s in V_s. Both components are nonzero, and the group contributes
   exactly span(v_r,v_s).

Each contributed plane has all four ranks exactly one. Duplicate
planes in the list are counted once. The sum-membership test in case
3 is an ordinary finite linear system for the actual kernel bases;
its value need not be assumed or enumerated to prove this bound.

This is a local REPRODUCTION of elementary interpolation and linear
algebra in the approved structural attempt. It establishes branch
finiteness, not universal four-row finiteness. Four pairwise distinct
ell_j, twelve-row exclusion, second-pair extraction, recovery gates
and the challenge radius remain unresolved. No source-level novelty
or independent critical audit is claimed.

## Proof

### Standard tools and the required local calculation

Use the arbitrary-field linear algebra in A. I. Kostrikin and
Yu. I. Manin, *Linear Algebra and Geometry*, Gordon and Breach,
1997 paperback, ISBN 90-5699-049-7, Chapter 1 Theorem 3.12,
pp. 20–21 and sections 6.2–6.9, pp. 44–46,
[primary book](https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf),
as recorded in the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-10-25-four-row-finiteness-review.md`.
Only rank-nullity, direct sums, uniqueness of decomposition and
linear-system consistency are imported. No projective-space
enumerative theorem or four-subspace classification is used.

The small polynomial calculation below is needed to control
intersecting cross pairs and a coordinate-vector sum obstruction,
which L155's disjoint-pair assertion does not cover. It also proves
the paired disjointness needed here directly, without invoking or
recomputing L153's finite census. This overlap is justified by the
stronger pair statements required for the branch; it is not a reproof
of a general finiteness theorem. For completeness, the sole root test
is the following explicit calculation: evaluation of a degree-at-most-two
polynomial at distinct u,v,w has coefficient matrix with rows
(1,u,u^2), (1,v,v^2), (1,w,w^2). Its determinant is
(v-u)(w-u)(w-v), nonzero in E. Thus three distinct zeros force all
three coefficients to be zero. This keeps the characteristic and
all denominators explicit.

### Every pairwise kernel intersection is a coordinate space

Put P(X)=product over y in J of (X-y), and
d_j(X)=product over y in K_j of (X-y), a monic quadratic. For x in S,
P(x) and every d_j(x) are nonzero, and

    g_j(x)=P(x)/d_j(x).                                      (1)

For distinct selected labels i,j, pairwise-linearity implies K_i!=K_j:
equality would already give two common elements of T_i and T_j.
The monic quadratics d_i,d_j are therefore distinct and linearly
independent. Indeed, alpha*d_j-beta*d_i=0 first gives alpha=beta
from the leading coefficient, then alpha=beta=0 since d_i!=d_j.
This uses distinct roots in J, so distinct K give distinct polynomials
also in characteristic 97 and after scalar extension.

If w belongs to V_i intersect V_j, write
w=s_i+alpha*g_i=s_j+beta*g_j, with s_i in E^{I_i} and
s_j in E^{I_j}. At every x outside I_i union I_j, (1) gives

    alpha*d_j(x)-beta*d_i(x)=0.

There are at least 7-4=3 such distinct x. The degree-two test makes
this the zero polynomial; independence gives alpha=beta=0.
Consequently, with the converse immediate from the coordinate vectors,

    V_i intersect V_j=E^{I_i intersect I_j}.                 (2)

In particular V_a intersect V_b=V_c intersect V_d=0. Every other
pair intersection is zero or the single coordinate line allowed by
pairwise-linearity. This conclusion is for the original maps over E,
not a support-disjointness heuristic.

### A coordinate vector cannot enter the sum of an overlapping pair

Suppose I_r intersect I_s={u} and t is outside I_r union I_s.
We claim

    e_t not in V_r+V_s.                                    (3)

If e_t=s_r+s_s+alpha*g_r+beta*g_s, look at x outside
I_r union I_s union {t}. Their number is 7-3-1=3.
At all three coordinates, multiplying by the nonzero denominators
and dividing by P(x) gives
alpha*d_s(x)+beta*d_r(x)=0. The degree-two test and the same
independence force alpha=beta=0. This would put e_t in
E^{I_r union I_s}, contrary to the choice of t. This proves (3),
including all possible K intersections permitted by the hypotheses.

### Exhausting the coincident-line branch

Let L be in that branch. A coincidence cannot be ell_a=ell_b or
ell_c=ell_d by (2). It must occur in one of the four cross pairs.
Choose such a pair i,j, and let r,s be its complementary pair.
Equation (2) implies I_i intersect I_j={t} and
ell_i=ell_j=E e_t. By disjointness of the two designated support
pairs, t lies in neither I_r nor I_s. Also e_t lies in neither V_r
nor V_s: one of i,j is the designated disjoint partner of r, and
the other is the designated disjoint partner of s, so (2) excludes
both memberships. These facts justify all nonzero components below.

If I_r intersect I_s is empty, (2) gives V_r intersect V_s=0.
The lines ell_r,ell_s are distinct, hence span L. Thus
e_t belongs to L subset V_r+V_s, and its decomposition e_t=v_r+v_s
in this direct sum is unique. Both components are nonzero. Since
L is spanned by a vector in V_r and a vector in V_s, its own
decomposition of e_t has those components, forcing
L=span(v_r,v_s). This is exactly case 3, with no further planes.

If I_r intersect I_s={u}, (3) shows e_t not in V_r+V_s. If ell_r
and ell_s were distinct, they would span L inside that sum, a
contradiction. Hence ell_r=ell_s=E e_u by (2), and
L=span(e_t,e_u). The labels t,u are distinct since t is outside
I_r union I_s. This is case 2. If both intersections in a group
are empty, (2) prevents either coincidence, giving case 1.

The four possible cross coincidences partition into the two displayed
groups. When both coordinate overlaps in a group exist, the two
possible initial choices give the same coordinate plane. When
exactly one exists, only that pair can be the initial coincidence
and the direct-sum decomposition gives at most one plane. Thus each
group contributes at most one, proving the bound two and exhaustiveness.

### Converse and exclusion of every rank-zero case

In case 2 the displayed coordinate plane meets each selected kernel
nontrivially: e_t lies in V_i and V_j, and e_u lies in V_r and V_s.
In case 3 its independent components v_r,v_s give a plane meeting
V_r and V_s, while e_t=v_r+v_s gives a nonzero vector in V_i and V_j.
Independence follows from V_r intersect V_s=0 and nonzero components.
So in either case each restricted Q_j has rank at most one.

For either designated disjoint pair h,k, (2) gives V_h intersect V_k=0.
If rank(Q_h restricted to this plane) were zero, the entire plane
would lie in V_h, contradicting its nonzero intersection with V_k.
The same argument with h,k exchanged excludes rank zero for k.
Apply it to both designated pairs. All four ranks are exactly one;
there is no empty, zero-image or extraneous plane retained by the list.
This proves the converse and the stated classification.

The remaining branch has four pairwise distinct ell_j. Neither (2)
nor (3) bounds that branch: it contains no common kernel line e_t
to which the complementary direct-sum argument can be applied.
No dimension count or sampled quadruple is being substituted for
its unresolved finiteness. The proof is valid over arbitrary E/F_97
and uses no finite-field count, genericity, characteristic transfer,
or coding realization.

## Mathlib

Full matching original-map coincident-branch classification: not checked.
General kernels, intersections and rank-nullity support the linear
steps; no exact Mathlib theorem names are asserted here. Unknown
coverage is not absence. No Lean verification or scheme-theoretic
claim is made.
