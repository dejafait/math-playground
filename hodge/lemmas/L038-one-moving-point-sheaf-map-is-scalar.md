# L038 — The one-moving-point sheaf recipe has only scalar action

## Hypotheses

Let S be a smooth projective complex K3 surface, H an ample
polarization, B=S a second copy used as parameter space, and
X=B x S. Write a:X -> B and b:X -> S for the projections.
Choose distinct points p,q in S and three nonzero linear forms
l_0,l_p,l_q on C^2 with pairwise distinct kernels. Set

\[
Q=O_{Delta_S}\oplus O_{B\times\{p\}}
                    \oplus O_{B\times\{q\}},
\qquad
\epsilon:O_X^2\longrightarrow Q,
\]

where epsilon restricts l_0,l_p,l_q to the respective supports.
Let F=ker(epsilon), and let U=B minus {p,q}.

Use M=M_H(v) for the stable torsion-free sheaf moduli space,
where v=(2,0,-1) and H is v-generic when invoking its standard
moduli and Mukai-map properties. A universal sheaf exists for
this vector. In the action convention of Markman's equations
(32)--(33), t in H^2(S,Q) is represented by (0,t,0), whose dual
is (0,-t,0). The action of the geometric ch_2 class of a sheaf G
on X, from the sheaf surface to the parameter surface, means

\[
A_G(t)=a_*\bigl(b^*t\smile\operatorname{ch}_2(G)\bigr).
\]

For the intended application retain the rank-eighteen cubic-RM
T(S), with full endomorphism field
E=Q(zeta_7+zeta_7^{-1}). The construction and conclusions below
do not require that extra hypothesis.

## Conclusion

The map epsilon is surjective, and F is B-flat with torsion-free
rank-two fibres of Mukai vector v. Every fibre over U is
H-Gieseker stable, so F restricted to U x S defines an algebraic
map f_U:U -> M. Its two collision fibres F_p,F_q are unstable;
the displayed flat family therefore does not define the required
global stable map B -> M.

Its geometric action is nevertheless defined on all of B:

\[
\operatorname{ch}_2(F)
 =-[Delta_S]-[B\times\{p\}]-[B\times\{q\}],
\qquad A_F|_{T(S)}=-\mathrm{id}.
\tag{1}
\]

The geometric c_2 action is +id, since c_1(F)=0. With Markman's
dual convention the normalized Mukai action is also +id.

More precisely, **if** f_U extends to an algebraic map f:B -> M,
then, for any universal sheaf P on M x S,

\[
f^*\theta_v(0,t,0)=t \quad (t\in T(S)).
\tag{2}
\]

Thus changing only the two collision fibres, or changing the
base-line-bundle normalization, cannot give a non-scalar action.
No existence or impossibility of such a stable repair is asserted.
On the cubic-RM locus this recipe supplies only the
one-dimensional scalar subspace of the required three-dimensional
field E. It adds no residual class or transverse RM direction.
This conclusion does not classify other support families or maps
whose images lie in boundary strata.

## Proof

**Imported model and the specialization being tested.**
O'Grady, *Moduli of sheaves and the Chow group of K3 surfaces*,
[arXiv:1205.4119v2, Proposition 4.2 and Remark 4.3,
pp. 11--12](https://arxiv.org/pdf/1205.4119v2#page=11), gives
the generic three-distinct-point kernel model for this exact
vector and a birational Hilbert-cube model. It does not assert
that moving one point while fixing two extends to a stable
family. The universal-family criterion is Huybrechts--Lehn,
*The Geometry of Moduli Spaces of Sheaves*,
[Theorem 4.6.5 and Corollary 4.6.7, printed pp. 107--108,
PDF pp. 119--120](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=119).
Here chi(F)=r+s=1 gives the required Euler-pairing gcd one.
Import these results; the explicit family, its stability,
collision failure, and action are the specialization below.
The prior assessment inspected these exact statements before
this research step. No new moduli-existence proof is needed.

**Surjectivity, flatness, and vector.**
Away from intersections of the three supports, epsilon has only
one nonzero target summand locally, and its nonzero linear form
is surjective. The two constant supports are disjoint. The only
remaining intersections are (p,p) and (q,q), where the diagonal
meets a constant support. At (p,p), the rows l_0,l_p form an
invertible two-by-two matrix. After this constant change of
basis the local map is

\[
O_X^2\longrightarrow O_X/I_{Delta}\oplus O_X/I_{B\times\{p\}},
\qquad (s_1,s_2)\longmapsto(s_1,s_2),
\]

and is surjective. The same argument uses l_0,l_q at (q,q).

Each summand of Q is the structure sheaf of a section of a and
is B-flat. The source O_X^2 is B-flat because a is smooth.
The kernel of a surjection between flat modules is flat, and
flatness of Q preserves exactness on every fibre. Hence

\[
0\longrightarrow F_s\longrightarrow O_S^2
 \longrightarrow k(s)\oplus k(p)\oplus k(q)
 \longrightarrow0
\tag{3}
\]

is exact even when s=p or s=q; the repeated point then has two
separate skyscraper summands. Every F_s is torsion-free as a
subsheaf of O_S^2. The quotient has length three, so
c_1(F_s)=0, c_2(F_s)=3, chi(F_s)=4-3=1, and
v(F_s)=(2,0,-1). These use Riemann--Roch on a K3 surface,
where chi(O_S)=2. In particular, flatness has not been confused
with stability at a collision.

**Stability for three distinct points.**
Take s in U and a rank-one coherent subsheaf A of F_s.
It is torsion-free. Its double dual is a line bundle L, and its
inclusion in O_S^2 extends to L -> O_S^2: on the complement
of finitely many points this is the original map, and Hartogs
extension applies to the locally free Hom sheaf. A nonzero
component gives a section of L^{-1}. Thus L^{-1}=O_S(D)
for an effective divisor D, and c_1(A).H=-D.H<=0.

If D is nonzero, this slope is strictly negative. The coefficient
of n in the reduced Hilbert polynomial is then smaller than
that of F_s, so A cannot destabilize F_s. If D=0, then L=O_S,
A=I_Z for a zero-dimensional subscheme Z, and its map to O_S^2
is given by a nonzero constant vector w in C^2. For each of
s,p,q where the relevant l_i(w) is nonzero, containment in the
kernel (3) forces that reduced point to belong to Z. The three
kernel lines are distinct, so w is killed by at most one l_i.
Consequently length(Z)>=2 and

\[
\chi(A)=2-\operatorname{length}(Z)<=0
 <\frac{\chi(F_s)}{2}=\frac12.
\]

In this zero-slope case Riemann--Roch gives reduced polynomials
(H^2/2)n^2+chi(A) and (H^2/2)n^2+1/2, respectively.
Thus every rank-one subsheaf has strictly smaller reduced
Hilbert polynomial. Proper full-rank subsheaves also have
smaller polynomials because their nonzero torsion quotient has
positive Hilbert polynomial. There are no torsion subsheaves.
This proves Gieseker stability and hence the map f_U.

**The actual collision fibres fail stability.**
At s=p, choose a nonzero w in ker(l_q). Multiples of w by I_p
vanish in both skyscraper summands at p and in the summand at q.
They therefore give a rank-one subsheaf I_p w of F_p.
Its slope is zero and chi(I_p)=1>chi(F_p)/2=1/2, so it
destabilizes F_p. At s=q use a nonzero vector in ker(l_p).
These are tests of the actual fibres, rather than an inference
from the generic model or from a Hilbert-scheme collision.

**Chern-character and normalized actions.**
The exact sequence on X gives [F]=2[O_X]-[Q] in K-theory.
For the structure sheaf of a smooth codimension-two subvariety,
the components ch_0 and ch_1 vanish and ch_2 is its cycle class;
this is the leading-term consequence of Grothendieck--Riemann--Roch.
All three supports here are such subvarieties. Additivity gives
c_1(F)=0 and (1). The diagonal term acts as id under a_*(b^*t -).
The two constant-section terms have their degree-four class
entirely on the S factor; their product with b^*t vanishes on
that surface. Therefore A_F(t)=-t, including for t in T(S).

Markman, *On the monodromy of moduli spaces of sheaves on
K3 surfaces*, [arXiv:math/0305042v3, equations (32)--(33),
p. 23](https://arxiv.org/pdf/math/0305042v3#page=23), defines
theta_v by the degree-two part of the universal pushforward
with sqrt(td_S) and x^vee. For an untwisted universal family
the similitude is one. For x=(0,t,0), the dual is -t and
<v,x>=0. The degree-two pushforward is consequently

\[
-a_*\bigl(b^*t\smile\operatorname{ch}_2(G)\bigr).
\tag{4}
\]

The remaining possible term is rank(G) times b^*(t sqrt(td_S)_4),
which is zero because it has degree six on S. Formula (4) gives
+id for F. The raw ch_2 action, geometric c_2 action, and
Mukai action have therefore been distinguished, not identified
by an unspecified sign convention.

**A repair supported only at the collision parameters stays scalar.**
Suppose f extends f_U and let G=(f x id_S)^*P. A universal sheaf
is flat over M, so this pullback is a B-flat sheaf family.
On U x S it is isomorphic to F restricted there, tensored with
a line bundle from U, by the universal-family property for stable
sheaves. Every line bundle on U extends to B: B is regular and
the removed subset has codimension two, so taking closures of
Cartier divisors identifies Pic(B) with Pic(U). Let L be that
extension and put F_L=F tensor a^*L.

The Chern-character difference ch_2(G)-ch_2(F_L) restricts to
zero on U x S. Chow localization on the smooth fourfold X
therefore expresses it as a rational combination of the two
surface classes [{p} x S] and [{q} x S]: these are the only
dimension-two irreducible components of the removed set.
Each has zero action on H^2(S), since integrating a degree-two
class over the S fibre is zero. Moreover

\[
\operatorname{ch}_2(F_L)
 =\operatorname{ch}_2(F)+a^*c_1(L)^2,
\]

because F has rank two and c_1(F)=0. The additional pure
parameter class again has zero action on H^2(S). Thus A_G=A_F
there. Since P is flat over M, its ordinary pullback G agrees
with its derived pullback along f x id_S, so Chern characters
commute with this pullback. Integration along the fibres of
the smooth proper product projection commutes with base change.
Consequently f^*theta_v is computed by (4) with G, even though
f need not be flat. Formula (4) proves (2).

This argument controls arbitrary changes at the two parameter
points and all base-line-bundle normalizations, conditional on
the repaired family existing. It does not assume that an arbitrary
map to M has these three support sections, that its relative
double dual descends, or that boundary sheaves have the displayed
quotient. Those questions remain outside this specialization.

This is a reproduction and application of the inspected generic
model, named stability and Chern-character tools, and the Mukai
action convention. The source theorems are imported; the explicit
recipe is checked here. No originality or progress beyond the
checked literature is claimed.

## Mathlib

Coverage: **not checked** for the full statement, Gieseker
stability, the universal-family interpretation, or the Mukai map.
No matching library theorem or absence from checked Mathlib
sources is asserted. The directly linked O'Grady,
Huybrechts--Lehn and Markman results above are supporting inputs,
not matches for this full recipe and collision statement.
Riemann--Roch, Grothendieck--Riemann--Roch, Hartogs extension,
and Chow localization are the named supporting theorems used
in the proof; no Mathlib names for them have been checked.
