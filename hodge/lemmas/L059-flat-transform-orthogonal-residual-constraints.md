# L059 — Orthogonal structure and bounded constraints on the flat residual

## Hypotheses

Retain the exact S,h,tau_D and the hypothetical bundle F of L058.
Thus S is the fixed smooth projective K3, X=S x S, and F is
locally free of rank two, slope-polystable for the simultaneous product
metric, with integral c_1(F)=0 and

\[
\operatorname{ch}(F)=2-6e_1-13e_2+\tau_D+26P.
\]

Use L058's actual, base-changing, zero-Einstein opposite transform
H=R^1p_1*F, with Rp_1*F=H[-1], and its holomorphic decomposition

\[
H=O_S^2\oplus K,\qquad
\operatorname{ch}(K)=7-14\eta,\qquad H^i(S,K)=0\quad(0\leq i\leq2).
\]

Use L052's exact zero-slope integral divisor lattice Zk, with
k=(-4,-2,1,2) and k^2=-14. No existence of F or K, spin lift,
vanishing of w_4, transform inverse, or stability of K is assumed.

## Conclusion

Determinant wedge and relative Serre duality give H a perfect
**symmetric** O_S-valued holomorphic pairing. Its restriction to K
is perfect and parallel for the induced zero-Einstein connection.
In particular K is the complexification of an oriented real rank-seven
bundle R, with

\[
p_1(R)=-14\eta,\qquad
\rho_4p_1(R)=\mathcal P(w_2(R))+i_*w_4(R).
\tag{1}
\]

Here P is the Pontryagin square and i_* is induced by Z/2 -> Z/4,
1 -> 2; P in (1) is not the product point class used in ch(F).
The necessary total characteristic constraint is compatible: the
inspected real-bundle theorem actually realizes rank-seven topology
with p_1=-14 eta, w_2=k mod 2, w_4=0. This constructs no holomorphic
or acyclic bundle.

The possible stable-summand patterns for K narrow to:

- a single stable symmetric rank-seven summand;
- distinct stable symmetric summands of ranks four and three;
- a stable symmetric rank-three summand plus E tensor C^2, where
  E is stable rank two with det(E)=O_S, c_2(E)=4 eta, and the
  symmetric pairing on this rank-four block is the product of the
  alternating determinant form on E and an alternating multiplicity
  form on C^2.

In particular L058's 5+2 pattern is impossible. The initially possible
pair of non-self-dual rank-two summands in 3+2+2 is also excluded;
no zero first Chern class on individual summands is assumed in doing so.

For every remaining pattern the adjoint bundle A=Lambda^2 K satisfies

\[
\operatorname{rank}A=21,\quad \operatorname{ch}_2(A)=-70\eta,
\quad\chi(A)=-28,\quad h^1(A)=28+2h^0(A).
\tag{2}
\]

The values (h^0,h^1,h^2)(A) are (0,28,0) for the first two
patterns and (3,34,3) for the third. Thus the total real characteristic
and adjoint-index tests do not exclude the flat exception: already
the single stable orthogonal rank-seven branch passes both. These
are consistency tests, not existence for any of the listed patterns,
nor a classification of their individual orthogonal topology.
Stop this bounded parity/index mechanism. This NEGATIVE is a
REPRODUCTION of the inspected tools, not a new general theorem,
flat-image rigidity, a new cycle, or a Hodge-conjecture resolution.

## Proof

**Trivialize the actual determinant and import coefficient duality.**
The integral first Chern class in the hypotheses is zero, not merely
its image in rational cohomology. This adds no restriction if L058's
character data are read rationally: integral Kunneth and torsion-free
K3 cohomology make H^2(X,Z) torsion-free, so rational vanishing of
an actual first Chern class already gives integral vanishing.
K3 cohomology and coherent Kunneth
give H^1(X,O_X)=0. The exponential exact sequence makes
Pic(X) -> H^2(X,Z) injective, so det(F)=O_X. Choose a trivialization;
the determinant wedge gives an alternating perfect bilinear form
b:F tensor F -> O_X. Choose also a nowhere-zero two-form on the
second K3, trivializing the relative canonical bundle of p_1.
Both choices can rescale the final pairing but cannot change its sign
or nondegeneracy.

Import [Stacks Section 48.19, (2) and (9), 0AU3](https://stacks.math.columbia.edu/tag/0AU3),
with [Lemma 48.3.6, 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q)
and [Lemma 48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT).
The proper smooth projection has relative dimension two and Noetherian
base, F is locally free coherent, and the duality coefficient is O_S.
The imported isomorphism, retaining its shift, is

\[
R p_{1*}(F^\vee)[2]\simeq R\mathcal Hom(Rp_{1*}F,O_S).
\]

Since Rp_1*F=H[-1] and F is identified with its dual by b, this
identifies H with H^dual. More explicitly the pairing on H is cup
product followed by b and the relative trace:

\[
R^1p_{1*}F\otimes R^1p_{1*}F
 \longrightarrow R^2p_{1*}O_X
 \longrightarrow O_S.
\tag{3}
\]

The last map uses the chosen relative canonical trivialization.
It is an isomorphism on R^2p_1*O_X; fibrewise it is the nonzero K3
Serre trace. Relative duality makes (3) perfect. Equivalently, base
change identifies it at every point with the perfect Serre pairing
on H^1 of the fibre, and a bundle map invertible at every fibre is
invertible. No generic-only cohomology argument is used.

The swap of two degree-one classes contributes (-1)^(1*1)=-1,
by the [complex commutativity constraint, Stacks 15.59, 0GWN](https://stacks.math.columbia.edu/tag/0GWN).
The coefficient wedge contributes another -1. Their product is +1,
so (3) is symmetric, not alternating. In Dolbeault representatives
alpha=a tensor u, beta=c tensor v with u,v of degree (0,1), the
pairing integrand is b(a,c)u wedge v. Swapping alpha,beta negates
both b and the wedge. This explicitly checks the sign in the actual
coefficient pairing; self-duality alone would not determine it.

**Descend to the residual and the connection.** Put T=O_S^2.
By acyclicity and K3 Serre duality,

\[
\operatorname{Hom}(T,K)=0,
\qquad\operatorname{Hom}(K,T)=0.
\]

Indeed these groups are copies of H^0(K) and H^0(K^dual), and
H^0(K^dual)=H^2(K)^dual=0. The same vanishings kill both off-diagonal
blocks of (3), viewed as H -> H^dual. As that map is invertible, its
restrictions on T and K are both invertible. Thus the restriction to
K is symmetric and perfect; an isotropic trivial part cannot be
discarded to force a spurious alternating residual.

Import Perego, *Kobayashi--Hitchin corrispondence for twisted vector
bundles*, Complex Manifolds 8 (2021), 1--95,
[Propositions 3.9--3.12 and 3.15, pp. 36--38](https://unige.iris.cineca.it/retrieve/e268c4cd-97f6-a6b7-e053-3a05fe0adea1/10.1515_coma-2020-0107.pdf#page=36).
Use its untwisted case. L058 supplies H's actual Chern connection
with Einstein function zero at h. Its dual has function zero by the
imported dual rule. The holomorphic pairing map H -> H^dual is
therefore parallel by Proposition 3.15; this conclusion requires no
stability of H. Holomorphic sections of H are likewise parallel by
the same proposition applied to O_S -> H. They span T. Hence its
Hermitian orthogonal complement is a parallel holomorphic summand;
it has the character and acyclicity of K. The off-diagonal Hom
vanishings identify it with the residual above. Its restricted
pairing is parallel for its zero-Einstein connection.

**Obtain a compact real orthogonal reduction, not just a complex form.**
At one fibre, let g be the parallel positive Hermitian metric, taken
linear in its first argument. Write the symmetric pairing as
q(u,v)=g(u,Jv), with J invertible antilinear. In a unitary basis,
write q(u,v)=u^t Bv with B=B^t. Then Jv=bar(B)bar(v), and
J^2=bar(B)B=B^*B is positive Hermitian. These operators are parallel;
J commutes with J^2 and its positive square root. The normalized
antilinear map j=J(J^2)^(-1/2) is an isometric involution. This can
also be checked by unitary Takagi diagonalization of B: J has the
form diag(s_i) times conjugation, s_i>0, and j is conjugation.
Its fixed spaces form a parallel real rank-seven bundle R with
K=R tensor_R C. This normalization proves a real reduction compatible
with the connection; an arbitrary complex symmetric form alone was
not being treated as a real metric.

A K3 has H^1(S,Z/2)=0, so w_1(R)=0 and R is oriented. By the
definition of Pontryagin classes, p_1(R)=-c_2(R tensor C)=-14 eta.
In particular it is not the Pontryagin class -28 eta of the real
bundle underlying the complex rank-seven K, which has real rank
fourteen. These are different real bundles.

Import Cadek--Vanzura, *On the classification of oriented vector
bundles over 5-complexes*, Czechoslovak Math. J. 43 (1993), 753--764,
[author manuscript, Section 2, p. 2, and Theorem 1(i), p. 5](https://www.math.muni.cz/~cadek/papers/so5.pdf).
The necessary relation for oriented real bundles is precisely (1).
For the compatibility test choose w_2=bar(k) and w_4=0. The defining
integral-lift property of Pontryagin square gives

\[
\mathcal P(\bar k)=\rho_4(k^2)=\rho_4(-14\eta)=2\bar\eta,
\]

which equals rho_4 p_1. Theorem 1(i) realizes such triples in real
rank five on a connected CW complex of dimension at most five.
The K3 has a finite real four-dimensional CW structure, so it supplies
an oriented rank-five R_5 with these classes. R_5 direct sum R^2
has rank seven and the same p_1,w_2,w_4. Its complexification has
c_1=0,c_2=14 eta. The theorem's extra hypotheses for injectivity are
irrelevant to this existence use. This is topological realization
only: neither the specified holomorphic structure nor an orthogonal
instanton, stability or acyclicity has been supplied. No w_2 or w_4
of the hypothetical actual K has been fixed by this witness.

**Retain all stable blocks before narrowing them.** L058 gives the
rank partitions 7, 5+2, 4+3 and 3+2+2, with each stable summand
E acyclic, of slope zero, and ch_2(E)=-2 rank(E) eta. Duals of
stable zero-slope bundles are stable. Holomorphic maps between these
summands are parallel by the imported morphism result. To use the
given metric here, first apply that result to the holomorphic idempotent
projections of K onto its stable summands: as endomorphisms of the
zero-Einstein K they are parallel. Their images inherit zero-Einstein
connections, so the morphism proposition applies to the summands too.
A nonzero
parallel map between stable bundles has zero kernel and full image:
a proper parallel subbundle would have degree zero, contradicting
stability. Thus it is an isomorphism. A stable endomorphism is
scalar, since an eigenspace of a non-scalar parallel endomorphism
would likewise give a proper parallel subbundle. These are the
usual simplicity/Schur consequences, with the real metric unchanged.

Consequently a perfect symmetric form pairs each stable isomorphism
type only with its dual. A type occurring once must be self-dual
with symmetric form. Its determinant has square O_S; torsion-free
Pic(S) makes its determinant O_S. Odd-rank self-dual types cannot
carry a perfect alternating form. A rank-two bundle with determinant
O_S has its perfect alternating wedge form. Simplicity makes every
map to its dual a scalar multiple of that form, so it cannot carry
a symmetric perfect form by itself. This excludes 5+2. In 4+3
the ranks differ, so both summands must be individually symmetric
self-dual, with c_1=0. The single rank-seven case must also be
symmetric self-dual.

In 3+2+2, the rank-three part must be symmetric self-dual. The
rank-two part could initially be a dual pair of non-isomorphic
types, or two copies of a self-dual type. Do not assign their c_1
in advance. For any stable acyclic rank-two summand E, L052's
lattice gives c_1(E)=t k with t integral, while L058 gives
ch_2(E)=-4 eta. Import K3 surface RR and Serre duality as in L052,
Huybrechts, *Lectures on K3 Surfaces*, author-hosted draft,
[Chapter 1, (2.5)--(2.6) and Proposition 2.4, pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11).
Tensor character multiplication yields

\[
\operatorname{ch}(\operatorname{End}E)
 =4+(-16+14t^2)\eta,\quad
\chi(\operatorname{End}E)=-8+14t^2.
\]

Simplicity and Serre duality give h^0=h^2=1 for End(E). Thus

\[
0\leq h^1(\operatorname{End}E)=10-14t^2,
\]

forcing t=0. Pic^0(S)=0 then gives det(E)=O_S, so E is self-dual
alternating and c_2(E)=4 eta. Two distinct such types cannot pair
with each other; each would have an alternating, rather than symmetric,
form on its single copy. The only possibility is E tensor M with
dim M=2. Schur's lemma writes its form as the alternating wedge
form of E times a bilinear form on M. Symmetry and perfectness
force that multiplicity form to be alternating and nondegenerate.
This establishes the stated exhaustive patterns without imposing
zero individual c_1 prematurely or constructing any summand.

**The adjoint index is compatible in every remaining pattern.**
For Chern roots x_i of a rank-n bundle, summing exp(x_i+x_j)
over i<j gives

\[
\operatorname{ch}_1(\Lambda^2 E)=(n-1)c_1(E),\qquad
\operatorname{ch}_2(\Lambda^2 E)
 =(n-2)\operatorname{ch}_2(E)+\tfrac12c_1(E)^2.
\]

These universal identities follow by summing the linear and quadratic
terms; they are needed here to specialize the inspected surface RR.
For K, c_1=0, n=7 and ch_2=-14 eta, so A has rank 21,
ch_1=0 and ch_2=-70 eta. K3 RR gives chi(A)=42-70=-28.
The symmetric form identifies A with the bundle of q-skew
endomorphisms, and induces A=A^dual. Hence Serre duality gives
h^2(A)=h^0(A), proving (2). The induced connection also has
Einstein function zero by the imported tensor rule, so all these
global skew endomorphisms are parallel.

For a single stable symmetric type the only endomorphisms are scalar,
and a scalar is q-skew only if it is zero. Distinct stable ranks four
and three give no cross morphisms and the same zero answer on both
diagonal blocks. Thus h^0(A)=0 in the first two patterns. In the
third, the rank-three part again contributes zero; on E tensor M,
all endomorphisms are id_E tensor End(M), and the q-skew ones
are precisely sp(M). For dim M=2 this Lie algebra has dimension
three (matrices [[a,b],[c,-a]] in a symplectic basis). There are
no cross morphisms to the rank-three part. Therefore h^0(A)=3
and h^1(A)=34 there. All required cohomology dimensions are
nonnegative. The induced symmetric form on A makes its degree-one
Serre pairing alternating, by the same cohomological swap sign, so
these even h^1 values also satisfy that parity condition.
No claim that such deformations or bundles actually
exist follows from the index.

The real rank-seven existence witness and these nonnegative adjoint
indices establish compatibility of the approved necessary tests.
They do not link that topology to any holomorphic stable branch,
prove existence of K or F, force the mixed tensor to vanish, or
address transport to the missing RM direction. Stronger block
topology, geometric existence, curvature coercivity and reconstruction
are outside this bounded test. The prior two-projection stop remains.

## Mathlib

Coverage of the full relative pairing, parallel residual, real reduction
and scoped orthogonal constraint result: **not checked**. No full
matching declaration or absence claim is made. The inspected Stacks
duality/sign statements, Perego connection-morphism proposition,
Cadek--Vanzura real existence theorem and Huybrechts K3 RR/duality
are the cited general inputs. Their determinant, sign, descent,
stable-block and index specializations above are the necessary local
proof; none is imported as a claimed literature theorem for this F.
