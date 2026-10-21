# L053 — Stable locally free factors for the minimum surviving pair

## Hypotheses

Let S be the smooth projective complex K3 surface of L044's final
ample chamber. Take precisely its real ample class

\[
h=(2\lambda+2+d,d,1-d,0),\qquad d=1+1/\lambda,
\]

in the integral divisor basis of L052. Here lambda is the positive
root of z^3+z^2-2z-1. Use L052's conclusion

\[
\{l\in\operatorname{NS}(S):l\cdot h=0\}=\mathbb Zk,
\qquad k=(-4,-2,1,2),\qquad k^2=-14.
\tag{1}
\]

Stability means strict slope stability for coherent torsion-free
sheaves, at the indicated ample class. A second Chern number is the
integral of c_2 over S. No global bundle on S x S is assumed.

## Conclusion

For each c in {5,6}, there exists an algebraic locally free rank-two
bundle E_c on S with determinant O_S, second Chern number c, and
slope-stable at the exact real class h. The bundles can first be
chosen stable at one common integral ample polarization H approaching
h from an adjacent chamber.

This supplies the necessary individual factor bundles for L052's
minimum pair (-9,-10), and its reversal. It does not realize the
prescribed mixed tensor on S x S, prove product stability, or transport
any bundle or cycle transversely. The universal primitive-Hodge gap,
the known span 21, and three attained RM directions against four
required are unchanged. This is a REPRODUCTION and specialization of
the sources below, without a claim of progress beyond known results.

## Proof

**Imported results and scope.** Use Yoshioka, *Irreducibility of moduli
spaces of vector bundles on K3 surfaces*,
[math/9907001v2, 7 February 2000](https://arxiv.org/pdf/math/9907001v2),
Theorem 0.1(1), Corollary 0.3 (p. 2), and Lemma 1.5 (pp. 5–6),
with the general-polarization condition (♮) in Sections 0.2 and 1.1.
The first result gives primitive nonemptiness; the corollary covers
multiples; the lemma applies to arbitrary positive-rank vectors and
gives slope-stable existence from slope-semistable existence if
v^2/2>=ell(v)^2. Its rank-one-factor proof case is included in the
approved assessment; we import the lemma, not its abbreviated generic
filtration estimate as an independent proof.

Use Ellingsrud–Lehn, *Irreducibility of the Punctual Quotient Scheme
of a Surface*, [alg-geom/9704016v1](https://arxiv.org/pdf/alg-geom/9704016v1),
Theorem 1 (p. 1): for a locally free rank-r sheaf B on a smooth
projective surface, the length-t Quot scheme has dimension (r+1)t.
The global statement includes all support collisions; we do not
reprove its irreducibility or punctual assertions.

Use O'Grady, *Modular sheaves on hyperkähler varieties*, Algebraic
Geometry 9 (2022), 1–38,
[Definitions 1.1 and 3.1–3.3, Proposition 3.4 and its proof](https://content.algebraicgeometry.nl/2022-1/2022-1-001.pdf),
pp. 2 and 8–10. On a K3 surface every torsion-free sheaf is modular,
q is the intersection form and c_S=1. For rank two with c_1=0 and
c_2=c, its discriminant number is 4c and a(E)=4c. The a-walls
are orthogonal to integral divisor classes xi with -a<=xi^2<0,
are locally finite in the real ample cone, and slope stability at
integral polarizations is constant in each open a-chamber.
Proposition 3.10 bounds an equality-slope class
2c_1(A)-rank(A)c_1(E) between -a(E) and zero; square zero
forces that class to be zero. We use these statements only at
integral polarizations. The real endpoint is checked separately.

**Choice of an admissible integral polarization.** Use the common
24-wall set, sufficient for c=5 and 6. By (1), a wall through h must
be represented by rk with integer r!=0 and 14r^2<=24. Thus its only
hyperplane is k^perp. It really is in this larger wall set: h is
not in an open 24-chamber. By local finiteness choose a small convex
ball B about h contained in the real ample cone and meeting no
24-wall except k^perp. Either component B_+ of B minus k^perp lies
in a single open 24-chamber. Rational ample classes are dense there.
Choose a rational ray in B_+ and scale it to an integral ample H.
Positive scaling does not change slopes or chambers.

We verify the generality needed above, rather than selecting a
rational point outside an unspecified countable exceptional set.
For a slope-semistable torsion-free rank-two sheaf F with c_1=0
and c_2=c, an equal-slope rank-one subsheaf can be saturated without
introducing a divisor: any nonzero divisorial saturation would have
positive H-degree and contradict semistability. Write its saturated
sequence as

\[
0\longrightarrow L\otimes I_Z\longrightarrow F
 \longrightarrow L^{-1}\otimes I_W\longrightarrow0,
\qquad c=\operatorname{length}Z+\operatorname{length}W-l^2,
\tag{2}
\]

where l=c_1(L). Rank-one torsion-free sheaves on a smooth surface
have precisely this line-bundle/point-ideal form. If l is nonzero
and l.H=0, Hodge index and (2) give -c<=l^2<0. Consequently
xi=2l is a nonzero class with -4c<=xi^2<0 and xi.H=0, which
would put H on a 24-wall. Hence l=0. This proves (♮) for both
vectors. The same argument shows that changes of slope ordering
and hence of Gieseker stability for these vectors cannot introduce
an additional wall within B_+: equal normalized first Chern
classes have a polarization-independent remaining reduced Hilbert
polynomial comparison. Thus H is a general polarization in the
wall sense used by Yoshioka. The persistent equal reduced Hilbert
polynomials for a divisible vector are allowed; they are not
removed by the word general.

More explicitly, once l=0, the reduced constant terms of the
rank-one factors in (2) are the integers 2-length(Z) and
2-length(W), whereas that of F is (4-c)/2. For c=5 equality
is impossible. For c=6 it requires both lengths to be three;
this equality persists for every polarization and is compatible
with the nonprimitive semistable theorem. Thus the same H works
for both vectors without imposing a nonexistent generic removal
of the latter equality.

**Nonempty slope-stable loci, including the nonprimitive vector.**
The vectors and dimensions are

\[
v_c=(2,0,2-c),\qquad v_c^2=4c-8,\qquad
\ell(v_c)=\gcd(2,0)=2.
\tag{3}
\]

For c=5, v_5=(2,0,-3) is primitive with square 12, so
Theorem 0.1(1) gives a Gieseker-stable torsion-free sheaf at H.
It is slope-semistable. For c=6, v_6=(2,0,-4)=2(1,0,-2)
is nonprimitive, with square 16. Its primitive constituent has
square 4, so Corollary 0.3 gives Gieseker-semistable existence.
One can also see this nonemptiness directly from I_Z direct sum
I_Z for a length-three subscheme Z: I_Z is rank-one stable and
has vector (1,0,-2). This is not a slope-stable bundle and is used
only to establish nonemptiness.

For both vectors v_c^2/2 is respectively 6 or 8, at least
ell(v_c)^2=4. Lemma 1.5 now gives a nonempty slope-stable locus.
Its properly slope-semistable codimension lower bound is
v_c^2/(2ell(v_c))-ell(v_c)+1=c-3, namely 2 or 3.
We do not apply the primitive-only Proposition 0.5 to v_6, and
we do not assume irreducibility in this branch.

**Removing every point-defect stratum.** Let E be any H-slope-stable
torsion-free sheaf with vector v_c and let B_E=E**. On a smooth
surface B_E is locally free and B_E/E has finite length t. If a
rank-one subsheaf A of B_E had slope at least zero, A intersect E
would have the same rank and first Chern class as A because the
quotient is supported at points; this would contradict stability
of E. Thus B_E is H-slope-stable, with determinant O_S and
second Chern number c'=c-t.

The stable Euler test of L052 applies also at H: a nonzero section
of B_E gives a saturated rank-one subsheaf of effective determinant
and nonnegative slope; the same applies to B_E^* by dual stability.
Therefore H^0(B_E)=H^2(B_E)=0 by Serre duality. Surface Riemann–Roch
gives 4-c'=-h^1(B_E)<=0, so c'>=4. Hence a nonzero defect can
only have t=1 for c=5, or t=1,2 for c=6.

We count consistently in the stack of stable sheaves without a
chosen determinant trivialization. The standard named Mukai
smoothness theorem for simple sheaves on a K3 surface (Mukai,
*Symplectic structure of the moduli space of sheaves on an abelian
or K3 surface*, Invent. Math. 77 (1984), 101–116; the dimension
formula is also stated in Yoshioka's Introduction) applies without
primitivity. For a stable sheaf G, Hom(G,G)=C and by Serre duality
Ext^2(G,G)=C. The trace Ext^2(G,G) to H^2(O_S) is an isomorphism:
its dual sends 1 to id_G. The trace-free obstruction therefore
vanishes: the trace of a sheaf obstruction is the obstruction to
deforming its determinant, and the fixed determinant O_S lifts
over every small extension on the fixed surface. Riemann–Roch
gives Ext^1 dimension v(G)^2+2.
Pic^0(S)=0 introduces no determinant deformations. Thus coarse
stable moduli are smooth of dimension v(G)^2+2; their stacks
have dimension one less, since the scalar automorphisms have
dimension one. No smoothness of the strictly semistable coarse
compactification is asserted.

This argument applies at each stable point, including nonprimitive
vectors; it supplies purity, not merely the largest component
dimension. Yoshioka Section 1.1 (p. 4) gives the bounded quotient
stack setting, and Lemma 1.7 (p. 6) explicitly treats positive-square
nonprimitive vectors. Its total semistable dimension agrees with
this count but is not being used to infer purity. The determinant
is not equipped with a trivialization, so its scalar stabilizer
remains G_m rather than the finite determinant-one subgroup.

In particular, the nonempty stable stack at c has pure dimension
4c-7. The stack of stable locally free possible hulls at c'
has dimension 4c'-7 if nonempty. Over that stack there is a
tautological bundle; its relative length-t Quot space has fibres
of dimension 3t by Ellingsrud–Lehn. This can equivalently be
formed on a smooth atlas and its atlas relative dimension subtracted.
The kernel of the universal quotient is flat over the parameter
space because both the bundle and its quotient are flat. Restrict
to its open stable locus. Every length-t defect E occurs in this
space through its canonical quotient B_E to B_E/E. Kernels have
double dual equal to the given bundle: the quotient is supported
at points and both double duals are reflexive. Scalar automorphisms
preserve each Quot point, so source and target both have the same
one-dimensional scalar stabilizer. More precisely, a scalar on
the hull restricts to that same scalar on its kernel. This is an
isomorphism of the stabilizer groups, in particular injective;
the stack map is therefore representable. Alternatively rigidify
both scalar actions and make the same dimension count on local
coarse charts. There is no extra automorphism dimension from the
quotient: Quot already identifies isomorphic quotient maps.

The defect image therefore has dimension at most

\[
(4(c-t)-7)+3t=4c-7-t<4c-7.
\tag{4}
\]

Equivalently the coarse dimensions are bounded by 4c-6-t.
For c=5 the single defect bound is 13 against stable dimension
14. For c=6 the bounds are 17 and 16 against stable dimension
18. The complete coarse-dimension check is

| c | t | c' | Hull dimension | Quot dimension | Defect bound | Stable dimension |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | 1 | 4 | 10 | 3 | 13 | 14 |
| 6 | 1 | 5 | 14 | 3 | 17 | 18 |
| 6 | 2 | 4 | 10 | 6 | 16 | 18 |

These are upper bounds if the indicated hull locus is empty.
Empty hull loci only improve the bounds. The hull stacks
and the relative Quot spaces are of finite type (stable hulls
lie in bounded Gieseker moduli at H), so their images are
constructible. A finite union of these lower-dimensional images
cannot exhaust a nonempty pure-dimensional stable locus. Thus
there is an H-stable locally free E_c for each c=5,6. This does
not assume that separate nonempty open loci intersect, or that
the nonprimitive moduli is irreducible.

**Strict stability at the exact real endpoint.** For each E_c,
choose rational ample classes alpha_j in B_+ converging to h.
After positive scaling they are integral ample divisor classes.
Their rays and H lie in one open 24-chamber, hence also one
open 4c-chamber. O'Grady Proposition 3.4(ii) makes the fixed
E_c stable at every alpha_j. For any fixed rank-one subsheaf A,
c_1(A).alpha_j<0. Continuity gives c_1(A).h<=0. Since A was
arbitrary, E_c is h-slope-semistable; no uniform bound on all
subsheaves or interchange of limits is used in this inference.

If E_c were not h-stable, a rank-one subsheaf of slope zero
would exist. Saturation retains slope zero: any divisorial
increase is positive against h and would violate the just-proved
semistability. Formula (2) applies again, now with l.h=0.
By (1), l=rk, so

\[
c=\operatorname{length}Z+\operatorname{length}W+14r^2.
\tag{5}
\]

For c=5,6 this forces r=0. But a subsheaf with l=0 has
slope zero also at H, contradicting the H-stability of E_c.
Thus E_c is strictly stable at h. Because Pic^0(S)=0 and the
integral Picard group is torsion-free, c_1(E_c)=0 identifies its
determinant with O_S. The proof is complete.

**Qualifications.** The numerical ample-wall set really contains
a wall at h; only the actual equality-slope possibilities have
been excluded. All defects, including collisions, are counted.
Local freeness is established before using these bundles as factor
candidates. Nothing identifies the two independent bundles with
restrictions of a common product bundle, and no Hodge solution or
complete solution candidate is claimed.

## Mathlib

Full stable locally free existence, moduli-stack dimension, relative
Quot and real-chamber coverage: **not checked**. No matching theorem
or absence is asserted. The proof imports named complex-algebraic
and sheaf-moduli results; it supplies no Lean formalization.
