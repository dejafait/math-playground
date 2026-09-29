# L023 — Ramified complete-intersection unions retain the cubic obstruction

## Hypotheses

Retain the very general cubic surface S, X=S x S, reduced support C,
and marked tangent spaces V_D contained in V_RM contained in V_N of
L008. In particular the Dickson family has differential of rank three.
Use the fixed-product rigidity of C proved in L016. Fix an ample L
on S, put H=p_1^*L tensor p_2^*L, and write Q(k)=Q tensor H^k.

Let m,n>0 and choose an admissible union as in L022:

\[
I=I_C,\qquad f\in H^0(X,I(n)),\quad
g\in H^0(X,O_X(m)),\qquad Y=C\cup V(f,g).
\]

Here (f,g) is a regular sequence defining a smooth surface, and g
is a nonzerodivisor on O_C. No ordering of m,n or existence of such
sections for every pair is assumed. Set

\[
J=I_Y,\quad F=I(-m),\quad G=O_X(-n),\quad
E=F\oplus G,\quad M=O_X(-m-n).
\]

For r=0,1,2 put A_r=C[tau]/(tau^(r+1)). Let S_2 be an NS-fixed
deformation over A_2 with a specified identification S_1=S x Spec A_1.
Its order-tau^2 coefficient is kappa in V_N, and X_2=S_2 x_(A_2) S_2.
The NS-fixed condition extends H to H_2. An allowed lift Y_2 is any
A_2-flat closed subscheme of X_2 with special fibre Y. Its first-order
motion, components, defining sections and linkage presentation are
not prescribed. Subscripts on sheaves below denote restriction to X_r.

## Conclusion

Every allowed Y_2 produces an embedded flat lift C_2 of C in X_2.
The recovered C_1 is constant. Consequently

\[
Y_2\text{ exists}\quad\Longrightarrow\quad\kappa\in V_D.
\tag{1}
\]

Thus no admissible positive-degree union has the required ramified
lift with kappa in V_RM outside V_D, even with arbitrary earlier motion.
If additionally H^1(X,I(n))=0, existence is equivalent to kappa in V_D;
this asserts existence of a lift, not extension of every specified Y_1.

The permitted coefficient space is contained in the three-dimensional
V_D, against four RM directions required, and equals it under that
extra hypothesis. The cycle still acts by U, because L022 gives
[Y]=[C]+mn c_1(H)^2. No transverse surface or new algebraic Hodge span
is obtained. Higher ramification orders, other representatives, and
the universal rational Hodge conjecture are not settled here.

## Proof

**The difference from the central obstruction argument.** L022 recovers
some ideal lift from the obstruction of the central direct sum; it does
not preserve a chosen earlier sheaf. Here we recover an actual inclusion
or projection on the given middle lift, compatibly through both small
extensions. The relevant Ext^1 vanishes in at least one of these two
directions for every degree pair. This is the specialization needed
beyond the saved obstruction-theory assessment.

Use Serre duality for perfect complexes on the smooth projective
fourfold X, whose dualizing complex is O_X[4]; a supporting reference is
[Stacks Lemma 57.4.1, tag 0FY7](https://stacks.math.columbia.edu/tag/0FY7).
Derived restriction adjunction, Kodaira vanishing and Kunneth are the
same standard inputs as in L022. The nilpotent-base criteria used below
are [Stacks Lemma 15.80.4, tag 07LU](https://stacks.math.columbia.edu/tag/07LU),
[Lemma 15.68.20, tag 0H75](https://stacks.math.columbia.edu/tag/0H75), and
[Lemma 15.68.3, tag 0654](https://stacks.math.columbia.edu/tag/0654).
These are supporting results, not statements of (1).

**Positive top cohomology on C vanishes.** Write nu:W -> C for the
smooth normalization in L008 and P=g_0^*L tensor g_1^*L. For every d>0,

\[
H^2(C,O_C(dH))=0.                                    \tag{2}
\]

Indeed the exact normalization sequence is

\[
0\longrightarrow O_C(dH)\longrightarrow\nu_*P^d
\longrightarrow T\longrightarrow0,
\]

where T has length three, one at each double point. This follows from
L008's local ring: pairs of functions on the two smooth branches must
have equal constant term. Finite pushforward and the absence of higher
cohomology for T give H^2(C,O_C(dH))=H^2(W,P^d).

Let F_W be a general complete elliptic fibre of W. It is nef, since
its line bundle comes from O_(P^1)(1). L008 gives K_W=2F_W, and each
g_i maps a general such fibre isomorphically onto a fibre of S. If
F_S is the elliptic fibre class on S, then

\[
(K_W-dP)\cdot F_W=-2d(L\cdot F_S)<0.
\]

An effective divisor has nonnegative intersection with a nef class.
Thus K_W tensor P^(-d) has no nonzero section. Serre duality on W
proves (2). All three singular points have been retained by the
normalization sequence; no duality or vanishing theorem on singular
C itself is being assumed. This top-cohomology argument is separate
from L022's use of positive H^1 vanishing.

**One central map has zero lifting obstruction.** Put d=n-m. If d<=0,

\[
\operatorname{Ext}^1_X(G,E)
=H^1(X,I(d))\oplus H^1(X,O_X)=0.                    \tag{3}
\]

For d<0, H^0(C,O_C(dH))=0 by antiampleness (or pullback to W), and
H^1(X,O_X(d))=0 by Kunneth and Serre duality on the two K3 factors.
The ideal sequence gives H^1(X,I(d))=0. For d=0, the map
H^0(X,O_X) -> H^0(C,O_C) is an isomorphism: C is connected, reduced
and projective, as the image of the connected W. Together with
H^1(X,O_X)=0 this gives the same vanishing.

If d>0, use the opposite direction. Serre duality gives

\[
\begin{aligned}
\operatorname{Ext}^1_X(E,G)
&=\operatorname{Ext}^1_X(I(-m),O_X(-n))
       \oplus H^1(X,O_X)\\
&\simeq H^3(X,I(d))^*=0.                            \tag{4}
\end{aligned}
\]

The last equality follows from (2) and the ideal sequence, since
H^2(X,O_X(d))=H^3(X,O_X(d))=0. Formula (4) uses global Ext and
perfect-complex duality, not the false replacement of I by a line
bundle at its singular points. It does not require H^1(X,I(d))=0.
Thus the known positive ideal-cohomology exceptions do not obstruct
the projection used in this degree range.

**Recover the linkage extension through both stages.** L022 proves,
for precisely these admissibility and positivity hypotheses,

\[
0\longrightarrow M\xrightarrow{a\mapsto(-af,ag)}
E\xrightarrow{(v,w)\mapsto gv+fw}J\longrightarrow0,
\qquad\operatorname{Ext}^2_X(J,M)=0.                \tag{5}
\]

Now assume Y_2 exists and let J_2 be its ideal. It is A_2-flat because
both the ambient structure sheaf and its quotient O_(Y_2) are flat.
Put M_r=H_r^(-m-n). For r=1,2 let i_r:X -> X_r and
j_r:X_(r-1) -> X_r be the closed immersions. Flatness over A_r gives
Li_r^*J_r=J and Lj_r^*J_r=J_(r-1). Locally this follows from

\[
J_r\otimes^{\mathbf L}_{O_{X_r}}O_{X_s}
\simeq J_r\otimes^{\mathbf L}_{A_r}A_s=J_s
\quad(s=0,r-1).
\tag{6}
\]

Apply RHom_(X_r)(J_r,-) to
0 -> i_(r*)M -> M_r -> j_(r*)M_(r-1) -> 0. Derived adjunction
identifies the relevant exact segment as

\[
\operatorname{Ext}^1_{X_r}(J_r,M_r)
\longrightarrow
\operatorname{Ext}^1_{X_{r-1}}(J_{r-1},M_{r-1})
\longrightarrow\operatorname{Ext}^2_X(J,M)=0.
\tag{7}
\]

Starting with (5), lift its class first to r=1 and then to r=2.
The resulting sequence

\[
0\longrightarrow M_2\longrightarrow E_2
\longrightarrow J_2\longrightarrow0                 \tag{8}
\]

has flat middle term, because both ends are A_2-flat, and has central
fibre E. The reduction maps in (7) are reduction of extensions: flatness
of their ends makes ordinary restriction exact and agrees with (6).
This construction applies to the actual arbitrary J_1 obtained from
Y_2. It imposes no constancy or splitting on E_1.

**Recover an ideal sheaf from the actual E_2.** When d<=0, begin with
the central summand inclusion G -> E. Apply Hom_(X_r)(G_r,-) to
0 -> i_(r*)E -> E_r -> j_(r*)E_(r-1) -> 0. By adjunction the
obstruction to lifting a map G_(r-1) -> E_(r-1) lies in
Ext^1_X(G,E), which is zero by (3). Hence the inclusion lifts first
to G_1 -> E_1 and then to G_2 -> E_2.

A map of A_r-flat sheaves whose central reduction is injective is
injective with A_r-flat cokernel. To check this over the nonreduced
base using the cited criteria, form its cone with source in degree -1
and target in degree 0. Its derived tensor with C is the central
cokernel in degree 0. Tags 0H75 and 0654 therefore make the cone an
A_r-flat sheaf in degree 0. Its degree -1 cohomology is zero, proving
injectivity, and its degree 0 sheaf is the flat cokernel. Applying this
to G_2 -> E_2 produces a flat Q_2 with central fibre F.

When d>0, begin instead with the central projection E -> G. Apply
Hom_(X_r)(E_r,-) to the reduction sequence for G_r. Since E_r is
A_r-flat, adjunction identifies the obstruction group with
Ext^1_X(E,G)=0 by (4). Thus that projection lifts through both stages
to E_2 -> G_2. Its central reduction is surjective, so nilpotent
Nakayama gives surjectivity. Its kernel Q_2 is A_2-flat because both
E_2 and G_2 are flat, and exact restriction gives its central fibre F.

In both cases P_2=Q_2 tensor H_2^m is a coherent A_2-flat lift of I.
We have lifted one selected map on the actual E_2; a splitting and the
other map are unnecessary. No mixed extension data of E_1 have been
discarded or required to vanish.

**Reconstruct an embedded ideal over the three-layer base.** Extend
L012's determinant/Hartogs reconstruction as follows. P_2 is perfect
over X_2: its derived reduction is the perfect ideal I on the smooth
X, so tag 07LU applies to the nilpotent reduction of each affine
ambient ring. This is perfectness over O_(X_2); the flatness already
proved is over A_2. Hence its determinant D_2 is a line bundle.

On U_2 with underlying open U=X minus C, the sheaf P_2 is locally free
of rank one: lift a central basis, apply nilpotent Nakayama, and use
base flatness to make the kernel zero. There it identifies canonically
with D_2. The central determinant is det(I)=O_X, with its standard
trivialization off C. For each r=1,2 the kernel of
Pic(X_r) -> Pic(X_(r-1)) is a quotient of H^1(X,O_X), from the
unit-sheaf sequence with kernel 1+tau^r O_X. That group is zero.
Therefore D_2 is trivial, compatibly with its central trivialization.

For u:U_2 -> X_2 one has u_*O_(U_2)=O_(X_2). Indeed, on a smooth
affine chart the deformation is trivial over A_2, with trivialization
compatible with the given lower one by formal smoothness. Each of
its three O_X-module coefficients has Hartogs extension across the
codimension-two C. The natural restriction map glues these local
equalities. The central Hartogs input is the one used in L012,
[Stacks Lemma 15.24.18, tag 0AVB](https://stacks.math.columbia.edu/tag/0AVB).
Adjunction now gives

\[
P_2\longrightarrow u_*(P_2|_{U_2})
\simeq O_{X_2}.                                    \tag{9}
\]

Its central reduction is I -> O_X: equality holds on U, hence on X
because O_X is torsion-free. The flat-map criterion proved after (8)
makes (9) injective with A_2-flat quotient. Its image defines C_2.
This treats the entire ideal, including all three non-lci points;
no flatness assertion about a residual component of Y_2 is needed.

**Rigidity eliminates the earlier motion of the recovered C.** L016
proves H^0(C,N_C)=0 from L008's full coefficient classification and
the rank-three Dickson parameter map. Its argument for the first
rotation uses only the current generic hypotheses. In the fixed
product X_1, embedded first-order lifts of C have tangent space
H^0(C,N_C). Consequently C_1 is the constant embedded C x Spec A_1.
This is a rigidity input, not a consequence of the equality of
ambient obstruction kernels alone.

Both C_2 and X_2 are now constant modulo tau^2. In compatible local
ambient trivializations the remaining changes of ideal generators
and transition maps are tau^2 times central ones. Their flatness and
gluing equations are exactly the ordinary first-order equations with
epsilon replaced by tau^2, since tau annihilates this coefficient.
This is the recovered-support argument at the end of L016; it depends
only on the constancy just proved. Thus ob_C(kappa)=0. L008 identifies
its kernel with V_D, proving (1) for every permitted earlier Y motion.

**The conditional converse and scope.** Suppose H^1(X,I(n))=0 and
kappa belongs to V_D. L022 supplies a first-order flat Y lift in the
product deformation with class kappa. Pull it back by epsilon -> tau^2.
Flatness is preserved by base change. The resulting ambient deformation
is isomorphic to the prescribed X_2 with its lower trivialization:
deformations of S with that trivial lower term over this small extension
are classified by their coefficient in H^1(S,T_S). This produces the
claimed lift, constant modulo tau^2. It does not say that every earlier
motion of Y extends. The dimension and cycle comparisons are those
already established in L008 and L022.

This is a reproduction and application of known duality, Ext and
nilpotent-base techniques. The new notebook conclusion is the uniform
order-two exclusion, obtained by the opposite map when n>m and by
retaining the actual earlier extension data. The saved assessment did
not supply this specialized recovery conclusion, and no originality
claim is made. Neither a nonzero positive ideal-cohomology group nor
arbitrary first-order motion escapes the exclusion. The 21-dimensional
span on the known family and the universal Hodge gap remain unchanged.

## Mathlib

Coverage of the full statement and its supporting deformation, duality
and nilpotent-base inputs: **not checked**. No full matching Mathlib
theorem or library absence is asserted. The linked Stacks statements
support Serre duality, perfectness, Tor amplitude, flatness and Hartogs;
none states (1) for this union. The saved prior SPECIALIZE assessment
also records the corrected Huybrechts--Thomas obstruction criterion and
the fixed-ambient sheaf/morphism framework. Here explicit Ext vanishings
recover the actual maps, so no unproved quadratic obstruction formula,
preserved splitting, or relative use of the uncorrected criterion is
needed. The normalization, sign-dependent map recovery, three-layer
reconstruction and precise use of rigidity are proved above.
