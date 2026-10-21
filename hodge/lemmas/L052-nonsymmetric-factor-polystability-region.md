# L052 — Necessary factor-polystability region for nonsymmetric corrections

## Hypotheses

Retain L044's final common hyperkahler metric on the very general
cubic RM K3 surface S, with real Kahler class h=omega_c and product
class Omega=p_1^*h+p_2^*h on X=S x S. Retain L048's full integral
mixed class tau_D, with operator D equal to 2A_c+4pi_K on divisors
and 2U on the transcendental space. L044 makes D self-adjoint,
scalar 2lambda on the positive three-plane, and preserves its
orthogonal complement. Set e_1=eta tensor 1, e_2=1 tensor eta,
where integral_S eta=1.

Take integers a,b in L050's topological region

\[
a+b\leq-13,\qquad (a+4)(b+4)\equiv6\pmod{12}.
\tag{1}
\]

A prospective F is a rank-two locally free holomorphic bundle,
slope-polystable at Omega, with cohomological Chern data

\[
c_1(F)=0,\qquad
\operatorname{ch}_2(F)=(a+4)e_1+(b+4)e_2+\tau_D.
\tag{2}
\]

No presentation, torsion-free replacement, or transport is assumed.
Write m=-a-4 and n=-b-4 for its factor second Chern numbers.

## Conclusion

Every F satisfying (2) must have

\[
\boxed{a,b\leq-9,\qquad (a+4)(b+4)\equiv6\pmod{12}.}
\tag{3}
\]

This is the exact non-exclusion set for the following necessary
tests combined with (1): exclude product line splitting, obtain
polystable factor restrictions by the hyperholomorphic connection,
and test their stable Euler characteristic or slope-zero line
splitting. It is not the holomorphic realization region. In particular,
passing the stable Euler test does not establish a stable factor bundle.

The least possible m+n in (3) is eleven, attained exactly by
(m,n)=(5,6),(6,5), equivalently (a,b)=(-9,-10),(-10,-9).
Thus a+b<=-19 is necessary, improving (1)'s cutoff -13.
These two factor restrictions would have to be stable, rather than
split. There are infinitely many pairs not excluded by the tests,
for example (-9,-10-12j) for every integer j>=0.

More precisely, at this metric a split polystable factor with
c_1=0 has second Chern number 14r^2 for an integer r. These
split factor bundles themselves exist; this does not construct F.
All other surviving factor values require the stable alternative.

This is an informative NEGATIVE filter, classified as REPRODUCTION
of covered tools, with no originality claim. It removes infinitely
many previously topologically realizable pairs but supplies no
holomorphic product bundle, new cycle or transverse surface.
The algebraic span remains 21 and attained RM directions three
against four required; the universal Hodge gap is unresolved.

## Proof

**Import the framework and reuse its coefficient-independent passage.**
Use Verbitsky, *Hyperholomorphic connections on coherent sheaves
and stability*, [arXiv:math/0107182v10, Theorem 3.9,
pp. 13--14](https://arxiv.org/pdf/math/0107182v10#page=13), and
[Proposition 3.7 and Lemma 3.8,
pp. 12--13](https://arxiv.org/pdf/math/0107182v10#page=12).
For stable bundles the invariant first two Chern classes supply a
hyperholomorphic Hermitian Yang--Mills connection; invariant
two-forms have zero Kahler contraction. Use Huybrechts, *Lectures
on K3 Surfaces*, author-hosted prepublication draft,
[Chapter 9, Section 3.1, pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175)
and [Theorem 4.9, p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182)
for real-class slope stability, dual stability and the
Hermite--Einstein/polystability correspondence. Import surface
and line Riemann--Roch and Serre duality from
[Chapter 1, equations (2.5)--(2.6) and Proposition 2.4,
pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11).
No general theorem is reproved. The parameter and exact-metric
application is needed because these sources do not classify (2).

L051's proof excluding product splitting depends only on the mixed
class: a line sum L direct sum L^{-1} has mixed character
2x tensor y for divisor classes x,y, so acts by zero on sigma,
whereas tau_D acts by 2lambda sigma. Thus F must be stable.
The full mixed class is rotation-invariant by L044, and the pure
point classes are invariant for all a,b. Hence c_1(F),c_2(F) are
invariant. The cited criterion and L051's curvature pullback
argument apply without a change: quaternionic-equivariant factor
embeddings pull the invariant curvature back to invariant surface
two-forms, whose Kahler contraction is zero. Therefore every
j_y^*F and k_x^*F is a locally free rank-two slope-polystable
bundle at h, with c_1=0 and second Chern numbers m,n respectively.
This uses curvature restriction, not an assertion that stability
is preserved under restriction. Total invariance is not assigned
to individual summands of an arbitrary polystable product bundle.

**Stable factor test, including its boundary.** Let E be a stable
rank-two locally free factor bundle with c_1(E)=0 and c_2(E)=c.
A nonzero section gives a rank-one subsheaf of nonnegative slope:
after saturation its determinant is an effective line bundle,
possibly trivial. This contradicts strict stability at slope zero.
Thus H^0(E)=0. Dual stability and Serre duality give H^2(E)=0.
Riemann--Roch consequently gives

\[
4-c=\chi(E)=-h^1(E)\leq0,\qquad c\geq4.
\tag{4}
\]

If c=4, the test gives h^1(E)=0 and no contradiction. For every
integer c>=4 it gives the nonnegative proposed value h^1(E)=c-4;
it is a necessary cohomological test, not a construction of E.
All negative values and c=0,1,2,3 fail the stable alternative.

**Split factor test at the actual metric.** A remaining polystable
rank-two locally free E is a sum of line bundles. Since a K3 has
Pic^0=0 and torsion-free Picard group, c_1(E)=0 makes these
L and L^{-1}. Their slopes are zero. For l=c_1(L), Whitney gives

\[
q(l,h)=0,\qquad c=-q(l,l).
\tag{5}
\]

We now compute the actual lattice of zero-slope lines, rather than
replace h by a nearby rational polarization. Use the divisor
classes (f_ell,O,E_exc,P) and their pairing G from L044's chamber
calculation, with G displayed in L025. They span the rational
Picard space and det(G)=-7. Their integral span has index e in
NS(S), with -7=e^2 det(NS(S)); integrality and squarefreeness
force e=1. Thus they are an integral basis. This also recovers
the integral-basis argument recorded in L020; no new lattice
classification is being assumed.

L044 gives h=(2lambda+2+d,d,1-d,0), with d=1+1/lambda,
lambda a root of the irreducible cubic z^3+z^2-2z-1. For an
integral l=(x,y,z,w), multiplication by G gives

\[
q(l,h)=2(y+w)\lambda+(x+y+3w)+(x-y+2z)/\lambda.
\tag{6}
\]

The numbers lambda,1,1/lambda are rationally independent:
any relation, multiplied by lambda, would be a polynomial of
degree at most two vanishing at the cubic algebraic number lambda.
Consequently (6) vanishes exactly when

\[
y=-w,\qquad x=-2w,\qquad z=w/2.
\]

Integrality forces w even, so l=r k, where r is an integer and
k=(-4,-2,1,2). Direct evaluation gives q(k,k)=-14. This proves
that the split alternative in (5) gives exactly c=14r^2.
Conversely each rk is the class of a line bundle by the definition
of NS(S); L(rk) direct sum L(-rk) is locally free polystable at
h and has that second Chern number. For r=0 it is O_S^2.
For r!=0 its second Chern number is at least fourteen.
In particular no negative value or value 1,2,3 can be split.
The earlier parity/effectivity obstruction in L051 is retained
and is strengthened here by the exact zero-slope lattice.

Combining (4) and (5), the numerical values not excluded for
one factor by these tests are exactly

\[
\{0\}\ \cup\ \{c\in\mathbb Z:c\geq4\}.
\tag{7}
\]

Only the zero and square values have actual split constructions
here. The whole tail in (7) means solely that the stable Euler
test supplies no contradiction; stable existence is unresolved
in this step. At c=5 or 6, a polystable factor would be stable
because these numbers are not 14r^2.

**Intersect with the full topological region.** Since p=a+4=-m
and t=b+4=-n, L050's congruence is mn=6 modulo 12.
It excludes m=0 or n=0. It also excludes m=4 or n=4, because
4 times an integer is divisible by four, whereas 6 modulo 12
is 2 modulo four. Thus (7) forces m,n>=5, exactly (3).
Conversely every pair satisfying (3) passes (4) on each factor
as a numerical necessary test and passes L050. Its sum is
already a+b<=-18, so (1)'s weaker inequality is automatic.
This proves exactness of the non-exclusion set for the stated
tests, without claiming stable existence or compatible gluing.

Squares modulo 12 are 0,1,4,9, so symmetry is impossible, as
already proved in L050. With m,n>=5, total ten would be (5,5)
and fails the congruence; total eleven is exactly (5,6) or (6,5)
and passes because 30=6 modulo 12. This gives a+b<=-19 with
the claimed equality pairs. The family (m,n)=(5,6+12j) proves
infinitude of the non-exclusion set. There are also infinitely
many new exclusions, for example (m,n)=(3,2+4j) for all j>=0:
they pass the old sum and congruence but violate (4) and (5).
This genuinely widens L051's one-pair obstruction; it does not
reclassify a stopped recipe as a success.

The exact verification command is
`python3 scripts/cubic-kahler/check_nonsymmetric_factor_region.py`.
It saves the metric polynomial, lattice, residue and boundary
certificates under `scripts/cubic-kahler/`; enumeration verifies
examples and residues, while (4)--(7) prove the infinite-region
claim. No existence source is needed for this necessary filter.
Compatible holomorphic F and its transverse transport remain
separate unresolved requirements.

## Mathlib

Coverage of the full fixed-metric variable-region statement:
**not checked**. No matching declaration or absence from checked
Mathlib sources is asserted. The directly linked Verbitsky and
Huybrechts results support the connection and surface tests;
they do not match the complete statement (3). L050 supplies
the exact topological region, while L044 and L051 supply the
fixed metric and coefficient-independent restriction argument.
This is a specialization and REPRODUCTION of inspected tools,
not a claim of progress beyond the checked literature.
