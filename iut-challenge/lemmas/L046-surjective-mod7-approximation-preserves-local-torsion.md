# L046 — Surjective mod-7 approximation preserving local torsion

## Hypotheses

Retain L044's fixed algebraic closure Omega of Q_3, embedded
H=Q_3(zeta_60), standard Tate curve E_q over Q_3 with q=3^30,
and embedded N=Q_3(zeta_420,3^(1/7)). In the notation of its proof,
put

f(x)=x^3+(1/4)x^2-b_2(q)x-b_3(q) in Z_3[x].

Fix any sufficient precision M>=1 from L044's application of
Bisatt–Dokchitser Theorem 2.2 at m=210, including its squarefree
neighborhood. This precision stays fixed throughout the counting
argument. Global mod-7 image means the image on all geometric
7-torsion, in any F_7-basis, over Q. Coordinate fields use both
coordinates of every torsion point.

## Conclusion

There exists a monic integer cubic g congruent to f modulo 3^M
whose nonsingular pointed curve E_0/Q, given by y^2=g(x), satisfies

rho_(E_0,7)(G_Q)=GL_2(F_7),

and E_0[210] is isomorphic to E_q[210] as a G_Q_3-module.
Consequently, with E'=E_0 tensor_Q Q(zeta_60),

E'_H[30] is entirely H-rational, and H(E'_H[7])=N

inside Omega. Thus L044's choice can be reselected to satisfy this
global-image prerequisite while retaining its full local module.
The construction is existential; no effective M or coefficients,
image after restriction to L045's field F, sufficient initial theta
data or original finite B>=A comparison is asserted. This is a
known-method specialization. The separate 2026-10-11 critical audit
below validates this unchanged existential conclusion.

## Proof

### Imported results and why a specialization is needed

Use David Zywina, *Elliptic curves with maximal Galois action on
their torsion points*, Bull. London Math. Soc. 42 (2010), 811–826,
[DOI](https://doi.org/10.1112/blms/bdq039),
[author-hosted 15-page version](https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf),
retrieved 2026-10-11. Page and theorem numbers below refer to that
author version. Definition 5.1, p.6, defines B_(k,m)(X) as the
nonsingular integral short models in B_k(X) whose m-torsion image
does not contain SL_2(Z/mZ). Proposition 5.7, p.8, gives, for fixed
k, coefficient norm and m,

|B_(k,m)(X)| / |B_k(X)| << log(X)/X^([k:Q]/2).

Apply only k=Q, m=7, with the maximum norm on the two real
coefficients. There is no minimal-model, good-reduction or non-CM
hypothesis. Lemma 2.4's proof, p.5, identifies containment of
SL_2(F_7) with full GL_2(F_7) image over Q, using the cyclotomic
determinant. Import these results without reproving their sieve or
group-theoretic inputs. The exclusion of Q in Theorem 1.3 is not a
hypothesis of Proposition 5.7.

For pointed coordinate changes use J.S. Milne, *Elliptic Curves*,
second edition (2021), [II.2, pp.50–53](https://www.jmilne.org/math/Books/EC2.pdf),
the characteristic-not-2-or-3 changes preceding Theorem 2.1,
Theorems 2.1(b) and 2.4(b); II.1 Proposition 1.5, p.49, states
that pointed isomorphisms preserve the elliptic group law.
The maps below are checked explicitly because an arbitrary short
model need not belong to L044's original cubic neighborhood.
L044 supplies the integral squarefree f and its finite-torsion
constancy theorem, with the full hypotheses, precise citation and
separate audit recorded there. No new constancy theorem is used.
The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-11-mod7-surjective-local-approximation.md`.

### Original congruences and the pointed rational maps

Let h=3^M. Choose integers c,d_0,e_0 representing respectively
1/4,-b_2(q),-b_3(q) modulo h in Z_3. Fix c once and for all, and
for arbitrary s,t in Z set

d=d_0+h s, e=e_0+h t,
g_(s,t)(x)=x^3+c x^2+d x+e.

Every one of these cubics is monic and congruent to f modulo h.
L044's sufficient precision ensures squarefreeness over Q_3,
hence over Q, and gives the complete G_Q_3-module isomorphism at
level 210 for its nonsingular pointed curve.

For the affine equation y^2=g_(s,t)(x), set

X=9x+3c, Y=27y,
A=81d-27c^2,
B=729e-243cd+54c^3.

Then Y^2=X^3+A X+B. Indeed expanding its right side at
X=9x+3c gives

729x^3+729c x^2+729d x+729e,

which equals 729y^2. The inverse is
x=(X-3c)/9, y=Y/27. Thus both maps are defined over Q; although
the usual depression x+c/3 divides by 3, the displayed scaling
makes A and B integers for all the permitted d,e.

On projective cubics the map is

[x:y:z] -> [9x+3c z:27y:z],

with inverse [X:Y:Z] -> [(X-3c Z)/9:Y/27:Z].
The homogeneous equation transforms by the same factor 729.
The transformation is invertible over Q and sends [0:1:0] to
[0:1:0]. Therefore it is a pointed Q-isomorphism to the integral
short model E_(A,B), and preserves the elliptic group law. Its
restriction to 7-torsion is F_7-linear and G_Q-equivariant,
so the two global representations have conjugate images.

### The full-rank affine lattice and its exact leading count

Write
A_0=81d_0-27c^2 and B_0=729e_0-243cd_0+54c^3.
The permitted short coefficients form the affine lattice

Lambda=(A_0,B_0)+{(81h s,-243c h s+729h t):s,t in Z}.

The integer parameter matrix has determinant
(81h)(729h)=3^10 h^2, which is nonzero. Thus Lambda is a translate
of a full-rank subgroup of Z^2, of index
D=3^(2M+10). Injectivity also follows directly from its first
coordinate and then its second. D is fixed, independently of the
growing real coefficient bound R.

For |A|,|B|<=R, the first-coordinate condition admits

2R/(81h)+O(1)

integers s. For each such s, the second-coordinate condition is an
interval in t of length 2R/(729h), hence admits
2R/(729h)+O(1) integers t. The latter error is uniformly bounded
over s: an interval's integer count differs from its length by at
most two, regardless of its center. Summing gives

|Lambda intersect [-R,R]^2|=4R^2/D+O_(h)(R+1).

This proves a positive leading constant without asserting a density
theorem for an unspecified subfamily. For completeness, the singular
short equation is 4A^3+27B^2=0. For each integer A it admits at most
two integers B, so at most 2(2 floor(R)+1)=O(R+1) integer pairs in
the box are singular. Removing these from Lambda therefore retains
4R^2/D+O_(h)(R+1) nonsingular pairs. In fact the local squarefree
neighborhood already excludes singular pairs in Lambda, but the
count comparison does not require relying on that redundancy.

### Domination of the exceptional set

The same elementary box and singular count give
|B_Q(R)|=4R^2+O(R+1). Zywina Proposition 5.7 therefore bounds the
exceptional models at m=7 by

|B_(Q,7)(R)|=O(R^(3/2) log R).

This is a bound for the entire box, so it also bounds exceptions
inside Lambda. For fixed h and hence fixed D,

|B_(Q,7)(R)| / (4R^2/D) = O(D log R/sqrt(R)) -> 0.

The error in the permitted nonsingular count divided by its leading
term also tends to zero. Hence for sufficiently large R there is a
nonsingular pair in Lambda outside B_(Q,7)(R). Its image contains
SL_2(F_7), and the cited Q-case criterion gives GL_2(F_7).
Its unique integer parameters s,t recover an original cubic still
congruent to f modulo 3^M. The pointed Q-isomorphism transfers the
full global image to that E_0. There is no uniformity claim as M
varies and no effective coefficient-size estimate.

### Complete local torsion and embedded fields

Apply L044's finite-torsion argument to this original monic cubic,
at the same fixed precision M. Its leading coefficient and all
three nonleading congruences are unchanged, so it yields an
isomorphism phi:E_0[210] -> E_q[210] of G_Q_3-modules in Omega.
This is a conclusion about all 210-torsion; the global surjectivity
condition has not substituted a point or cyclic subgroup for it.

Restrict phi to the actual subgroup G_H and to the subgroups killed
by 30 and by 7. Since both divide 210, these are precisely the full
30-torsion and full 7-torsion modules. By L044 the first target
module has trivial G_H action and the second has full coordinate
field N. Equivariance and bijectivity imply trivial action on
E_0[30] and equality of the two pointwise-fixing kernels on
7-torsion. Each kernel fixes exactly the embedded field generated
by both coordinates of every torsion point; the finite separable
fixed-field correspondence therefore gives H(E'_H[7])=N.
The completion of the embedded Q(zeta_60) is H as in L044.
The pointed Q coordinate change would also preserve these modules;
using the original cubic makes their local constancy explicit.

This specialization passes the declared count/congruence test and
supplies local progress by applying known sources. It establishes
no theorem beyond the source methods checked, no image statement
over F, and no global initial theta-data instance. L043's
exact-curve stop is preserved: only the finite module is retained.
The distinct packet stops ATTEMPTS/022,025,026 also remain intact.
Geometric-parameter/full initial-data conditions, native/input/action
identification, marked pilot transport, essentiality and the original
finite B>=A gap remain unresolved. L045 is downstream, not an input.

### Separate critical audit — 2026-10-11

The verdict is a pass within the stated existential scope. Use the
pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-11-mod7-approximation-critical-audit.md`.
No changed hypothesis, new theorem or additional lemma input is
required. Audited L044 supplies the full local constancy premise;
its L042 packet is retained, not independently reconstructed here.

**Coordinate algebra and congruences.** Put
F_g=y^2 z-x^3-c x^2 z-d x z^2-e z^3 and
F_s=Y^2 Z-X^3-A X Z^2-B Z^3. Substitution of the displayed map gives
F_s(9x+3cz,27y,z)=729 F_g(x,y,z). In particular the xz^2 terms
243c^2 and -243c^2 cancel, and the constant-in-x cubic terms are
27c^3-81c^3+54c^3=0 and 243cd-243cd=0.
The projective matrix has determinant 243, nonzero in Q; composing
with the displayed inverse in either order gives the identity matrix.
Neither map has a projective base point, and both fix [0:1:0].
Thus this is a Q-defined pointed isomorphism, not just an affine
substitution or a geometric twist. Milne II.1 Proposition 1.5 applies.
All three original nonleading coefficients remain in their prescribed
3^M-classes. The short coefficients need not remain in that original
neighborhood: local constancy is applied before the coordinate change.
The determinant being divisible by 3 creates no obstruction over Q
or Q_3; an integral isomorphism of reduction models is not required.

**Index, errors and nonsingularity.** Write a=81h and b=729h.
The parameter matrix is triangular with diagonal a,b; its integer
lattice index is ab=3^(2M+10). Its injectivity follows by first
recovering s from A and then t from B. Set u=2R/a and v=2R/b.
If S is the number of permitted s, then |S-u|<=2. Each of their
t-intervals has count T_s with |T_s-v|<=2, uniformly in its center,
even though that center depends on s and c. Hence the total P obeys

|P-uv| <= 2v+2S <= 2v+2u+4
          =4R/b+4R/a+4.

This verifies the asserted error independently of the lattice's
translation and shear. At most 4 floor(R)+2 pairs in the whole box
are singular, because each integer A allows at most two B. Removing
them can therefore subtract at most 4R+2 from this lower bound.
In fact L044 already excludes them from this family: its sufficient
fixed precision makes every original cubic squarefree, and the
pointed isomorphism retains nonsingularity. The redundant removal
estimate is valid without using this stronger fact.

**Source bound and global transport.** The primary author version of
Zywina was directly rechecked at section 1.1, Definition 5.1,
Proposition 5.7 with its complete proof, and the first assertion of
Lemma 2.4's proof. They cover exactly the fixed maximum-norm box over
Q and level 7 used here; import the bound and Q-case criterion as
cited above. No all-level Serre-curve assertion is invoked.
For some fixed C and all sufficiently large R the number of exceptions
is at most C R^(3/2) log R. The number of surviving good pairs is
therefore bounded below by

4R^2/D-(4R/a+4R/b+4)-(4R+2)-C R^(3/2) log R.

Dividing by 4R^2/D gives a quantity tending to 1, because M, a, b
and D were fixed first. The lower bound is eventually positive.
This uses exceptions in the whole box and needs no equidistribution
inside the permitted family, uniformity in M, minimal models or
distinct isomorphism classes. The resulting pointed Q-isomorphism
induces an F_7-linear G_Q-equivariant bijection on the entire
7-torsion. Its conjugacy of representations transfers the full image
to the original cubic, to which the local theorem applies.

**Full local modules and embedded fields.** L044's same-degree monic
neighborhood gives an isomorphism phi on all 210-torsion for every
permitted original cubic. For n=30,7 the subgroup annihilated by n
inside E[210] equals E[n]; an abelian-group isomorphism carries it
bijectively to the corresponding subgroup. Restricting to the actual
G_H in Omega therefore gives full G_H-equivariant bijections at both
levels, including the 3-primary part. For every sigma in G_H,
injectivity and equivariance imply that sigma fixes all source points
if and only if it fixes all target points. At level 30 the target
action is trivial, so all source points are H-rational. At level 7
the identical pointwise-fixing subgroups fix the identical embedded
coordinate fields: each field is generated by both coordinates of
all the finitely many torsion points, and finite separable Galois
correspondence applies inside Omega. L044 identifies that field with
N and the actual completion of Q(zeta_60) with H. No abstract field
isomorphism, degree match or compatibility of chosen torsion bases
is needed. The isomorphism phi need not arise from a curve isomorphism.

All four approved checks pass. L044 remains the only direct lemma
input; L045 is a downstream use. There is no mathematical correction
to the proof or change to the dependency row. This audit validates
an application of known methods, not progress beyond the checked
sources or an essential IUT flaw. Image over F, effective coefficients,
geometric-parameter and full initial-data conditions, native/input/action,
pilot transport, essentiality and original finite B>=A remain open.
The exact-curve and other-packet stops remain intact. Full matching
Mathlib coverage remains unchecked; no numerical evidence is used.

## Mathlib

Full matching coverage of the fixed-level exceptional-model bound,
prescribed local finite-torsion approximation and combined existence
statement has not been checked in Mathlib. No absence claim is made.
The cited primary results are the mathematical inputs; the displayed
coordinate identities, full-rank lattice count and module transport
are their explicit specialization, not a claimed new large-image or
local-constancy theorem. No mathematical script or numerical evidence
is used.
