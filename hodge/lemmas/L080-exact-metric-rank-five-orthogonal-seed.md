# L080 — An actual exact-metric seed for the rank-five orthogonal construction

## Hypotheses

Let S be the marked smooth projective complex K3 surface with the
actual real ample class h of L052. Use its integral Picard basis and

\[
\operatorname{NS}(S)\cap h^\perp=\mathbb Zk,
\qquad k=(-4,-2,1,2),\qquad k^2=-14.
\]

In particular k is primitive and is not twice an integral class.
Write eta for the integral point class. Stability below is strict
slope stability of torsion-free sheaves at the specified ample class.
No product kernel or image bundle is assumed to exist.

## Conclusion

There exists an algebraic locally free h-stable rank-two bundle E with

\[
c_1(E)=k,\qquad \operatorname{ch}_2(E)=-5\eta,
\qquad c_2(E)=-2\eta.
\]

It is spherical: its self-Ext dimensions are (1,0,1). Both E and
E^vee have cohomology dimensions (0,1,0). Consequently

\[
J_0=\mathcal O_S\oplus E\oplus E^\vee
\]

is an actual h-slope-zero polystable rank-five bundle with integral
c_1=0, c_2=10 eta, trivial determinant and a perfect symmetric
O_S-valued form. Its cohomology is (1,2,1). Its vector-bundle
automorphism group is (C^*)^3, hence linearly reductive; its
orientation-preserving form automorphism group is C^*.

This is a seed, not the requested stable acyclic J_5 of L079.
No deformation, formal or convergent, is asserted. It is a local
ADVANCE / REPRODUCTION of the assessed existence and chamber tools,
without a claim of progress beyond the checked general sources.

## Proof

**Imported inputs.** Use Yoshioka, *Irreducibility of moduli spaces
of vector bundles on K3 surfaces*,
[math/9907001v2, 7 February 2000](https://arxiv.org/pdf/math/9907001v2),
Theorem 0.1(1), p. 2, and the general-polarization convention in
Section 0.2, pp. 2--3. A primitive algebraic positive-rank Mukai
vector of square at least -2 has a nonempty stable torsion-free
moduli space at a general ample divisor. We use neither Lemma 1.5
(its positive-square bound fails here) nor the nonprimitive theorem.

For locally finite numerical walls use O'Grady, *Modular sheaves
on hyperkahler varieties*, Algebraic Geometry 9 (2022), 1--38,
[Definition 1.1, Definitions 3.1--3.3 and Section 3.2](https://content.algebraicgeometry.nl/2022-1/2022-1-001.pdf),
pp. 2,8--10. On a K3 surface every torsion-free sheaf is modular;
for rank two the wall parameter a equals the discriminant
4c_2-c_1^2. The hyperplanes orthogonal to integral xi with
-a<=xi^2<0 are locally finite in the real ample cone.

Use Greb--Toma, *Compact moduli spaces for slope-semistable sheaves*,
Algebraic Geometry 4 (2017), 40--78,
[Theorem 6.6 and Section 6.3.3](https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf#page=34),
pp. 73--74. For fixed topological invariants on a compact subset of
the real ample cone of a surface, a finite rational linear chamber
stratification preserves slope stability and semistability uniformly
over all torsion-free sheaves, including on lower-dimensional strata.
These general results are imported, not reproved. The remaining
argument checks their numerical and exact-real-polarization hypotheses.

**The vector and the small wall bound.** The required Mukai vector is

\[
v=(2,k,-3),\qquad v^2=k^2-2(2)(-3)=-2,
\qquad \Delta=4(-2)-(-14)=6.
\tag{1}
\]

It is primitive since k is primitive. Suppose a sheaf of these
invariants is slope-semistable at an ample class alpha and has a
rank-one equality-slope subsheaf. Saturation preserves equality:
a divisorial increase has positive alpha-degree and would violate
semistability. The saturated subsheaf and torsion-free quotient are
L tensor I_Z and L' tensor I_W for zero-dimensional Z,W. Put l=c_1(L),
so c_1(L')=k-l. Their second Chern identity gives

\[
-2=\operatorname{length}Z+\operatorname{length}W+l\cdot(k-l).
\]

For xi=2l-k, equality slopes give xi.alpha=0 and

\[
\xi^2=4(\operatorname{length}Z+\operatorname{length}W)-6.
\tag{2}
\]

The class xi is nonzero since k is not divisible by two. Hodge index
then gives -6<=xi^2<0. Thus the complete equality-slope obstruction
for these rank-two invariants lies among the numerical 6-walls.
There is no such wall through h: any nonzero xi perpendicular to h
is nk with square -14n^2<-6. Local finiteness therefore supplies an
open ball B about h, contained in the real ample cone, meeting no
6-wall. In particular, at every ample integral ray through B every
slope-semistable sheaf of vector v is slope-stable. Equation (2)
also rules out any Gieseker wall there: equality of reduced Hilbert
polynomials first requires equality of slopes. The zero first-class
difference is impossible. Such integral polarizations satisfy
Yoshioka's generality convention and condition (♮) of Section 0.2.

**An integral polarization in the same real stratum.** Choose a compact
convex neighborhood K of h contained in B. Apply Greb--Toma to the
fixed invariants (2,k,-2 eta). On a surface these are all the required
Chern classes. Among the resulting finite rational wall equations,
intersect the kernels of those vanishing at h, obtaining a rational
linear space W containing h. Rational points are dense in W. The
remaining equations have nonzero values at h, so a sufficiently close
rational alpha in W and in the interior of K has their same strict
signs. The segment from h to alpha stays in that relative stratum.

Clear denominators to choose an ample line bundle H with class a
positive integral multiple of alpha. Scaling preserves all slope
tests. The preceding 6-wall argument makes H a general polarization
for v. Yoshioka Theorem 0.1(1) and (1) give an H-Gieseker-stable
torsion-free E of vector v. Gieseker stability implies slope
semistability; (2) excludes equality and makes E H-slope-stable.
Greb--Toma now makes this same E stable at h, because alpha and h
are in the same stratum. There is no assumption that the finite
Greb--Toma stratification has no artificial wall through h, no
generic-polarization substitution for h, and no limiting assertion
about all subsheaves.

**Every point defect is impossible.** Let B_E=E**. A reflexive sheaf
on a smooth surface is locally free, and B_E/E has finite length t.
If a rank-one subsheaf A of B_E violated h-stability, A intersect E
would have the same rank and first class as A, since its quotient
is supported at points. It would violate E's stability. Hence B_E
is stable and simple. Its Mukai vector is (2,k,-3+t), so

\[
v(B_E)^2=-2-4t.
\]

For a simple bundle on a K3 surface, Serre duality gives Ext^0 and
Ext^2 dimensions one, and Mukai Riemann--Roch gives
dim Ext^1=2+v^2. Applied to B_E this is -4t, impossible for t>0.
Therefore t=0 and E is locally free. Applied to E the same identity
gives self-Ext dimensions (1,0,1). This checks freeness directly;
no primitive/nonprimitive freeness exception or defect dimension
estimate is being suppressed. Negative c_2 is consistent with the
positive discriminant six in (1).

**Cohomology, form and reductivity.** The slope of E at h is zero.
Dual stability makes E^vee stable of the same slope. The standard
stable-sheaf Hom lemma at equal slope gives Hom(O_S,E)=0 and
Hom(O_S,E^vee)=0, since their ranks differ. Serre duality then gives
H^2(E)=H^2(E^vee)=0. Surface Riemann--Roch gives
chi(E)=2 rank(E)+ch_2(E)=-1, and the same for E^vee, hence their
cohomology triples are (0,1,0). Dual stability and the equal-slope
Hom lemma apply to the real ample class by their slope inequalities;
alternatively apply the same real-stratum theorem to an integral
representative before these standard surface statements.

The three summands of J_0 are stable of slope zero, so J_0 is
polystable. Its Chern character is 5-10 eta. Its actual determinant
is canonically det(E) tensor det(E)^vee, hence trivial. For local
sections (a,e,phi) and (b,f,psi), set

\[
Q((a,e,\phi),(b,f,\psi))=ab+\phi(f)+\psi(e).
\]

Evaluation makes Q globally defined, symmetric and perfect. The
cohomology is (1,2,1), using the K3 triple (1,0,1) for O_S.
The stable summands are pairwise nonisomorphic: E and E^vee have
distinct first classes k and -k. Equal-slope Hom vanishing and
simplicity therefore give End(J_0)=C direct sum C direct sum C
as an algebra, and Aut(J_0)=(C^*)^3. A form-preserving automorphism
has scalars (a,b,c) with a^2=1 and bc=1. Its determinant is a,
so the orientation-preserving subgroup is exactly
{(1,b,b^(-1)): b in C^*}. In characteristic zero these tori are
linearly reductive. No formality or principal-bundle stability is
inferred merely from this reductivity.

**Scope.** The section of the trivial summand shows directly that
J_0 is not acyclic, and that summand has equal slope, so J_0 is not
stable. A form-preserving deformation with underlying-vector stability
and acyclicity is still required. The seed does not produce L079's
images, a common F, a transported cycle or new Hodge-class algebraicity.

## Mathlib

Full matching stable-seed existence, real-polarization chamber and
K3-sheaf formality coverage: not checked. The cited mathematical
sources supply supporting general results; no full matching Mathlib
declaration or absence is asserted. No formal verification is claimed.
