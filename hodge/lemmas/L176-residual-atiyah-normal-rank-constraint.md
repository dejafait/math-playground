# L176 — The residual Atiyah map forces at least fourteen normal directions

## Hypotheses

Retain the conditional family and all fixed conventions of L108,
L116, L165 and L173–L175. Thus X=S_1 x B is the product of the
identical marked projective K3 surfaces, with their original common
metric, ordered hyperkähler triple, holomorphic forms and actual
connection. The hypothetical locally free rank-two product-polystable
bundle F has integral c_1(F)=0 and

\[
 \operatorname{ch}(F)=2-14e_1-21e_2-\tau_D+62e_1e_2,
\]

with the full prescribed mixed tensor. No existence of F is asserted.
Put V=End_0(F), C=Rp_*V, M=R^1p_*V, W=R^2p_*V,
E=H^2(X,V), K=H^1(B,M) and U=H^0(B,W). Use the actual arrows
j,r,a and their maps i=H^2(j), R=H^2(r), A=H^2(a), not a chosen
additive splitting. In particular Ri=1 and ker A=i(K).

Keep the nondegenerate complex symmetric Serre form Q on E and
S(v,w)=Q(iv,iw). L108's specific orthogonal splitting gives

\[
 K=I(K_T)\mathbin{\perp_S}K_N,\qquad
 K_T=H^1(B,T_B),\quad K_N=H^1(B,N),
\]

where I is induced by the actual extended KS inclusion. Both
restrictions of S are nondegenerate. Write S_N=S|_{K_N}. Let
Z be the finite reduced split set, s=|Z|, and t=h^0(B,N), all as
in L116; Z may be empty. The retained conclusions are

\[
 \dim K_N=704-s+2t,\quad 0\le t\le48,\quad t\ne47,
 \quad t=48\Longrightarrow s=800.
                                                        \tag{1}
\]

Use L174's actual residual map f=mathfrak a_perp with domain
D_1=H^1(S_1,T_{S_1}), of dimension twenty, and L175's
ell(u)=q(phi(u),k). The forms below are bilinear over C, not
Hermitian. No metric preservation by j or r, section integrability,
value of a section bracket, or point self-pairing is assumed.

## Conclusion

The actual map Rf lands in K_N. Denote this normal map by g_N.
Let T=(A|_{ker R})^(-1):U -> ker R and Q_U(w,w')=Q(Tw,Tw'),
as fixed by L165. Then

\[
 f=i g_N+T A f,\qquad
 Q(fu,fv)=S_N(g_Nu,g_Nv)+Q_U(Afu,Afv).                  \tag{2}
\]

For nonempty Z, put

\[
 c=(-2\pi i)^2Q_U(w_k,w_k),
\]

where w_k is L175's actual point vector. This scalar is unknown,
and may be zero. With G=f^*Q, equation (2) becomes

\[
 g_N^*S_N=G-c\,\ell\otimes\ell,\qquad
 \operatorname{rank}G=15.                              \tag{3}
\]

Consequently

\[
 \begin{cases}
 \operatorname{rank}(g_N)\ge14,& Z\ne\varnothing,\\
 \operatorname{rank}(g_N)\ge15,& Z=\varnothing.
 \end{cases}                                           \tag{4}
\]

When Z is nonempty and c=0 the lower bound in (4) is also fifteen.
These are lower bounds for the actual map: no equality between
map rank and pulled-back Gram rank is asserted.

The dimension comparison therefore yields the uniform necessary
conditions

\[
 704-s+2t\ge14,\qquad s\le690+2t,\qquad
 t\le46,\qquad \boxed{0\le s\le782}.                   \tag{5}
\]

For empty Z the stronger inequality is 704+2t>=15, which adds no
restriction to t>=0. The endpoint s=800 and the range 783<=s<=796
previously left by L116 are excluded under the retained hypotheses;
797,798,799 were already excluded there. No existence or attainability
is asserted for s=782 or any other remaining value.

This is a conditional ADVANCE / REPRODUCTION of the assessed rank
tools and actual-arrow inputs. The separate step 592 conceptual audit
below preserves the conclusion (EXPLORATION / REPRODUCTION), with no
substantive correction or stronger bound.
It gives a cardinality constraint, not nonexistence of F, an actual
normal-map formula, a section-bracket value, a better square count,
transport, or primitive Hodge realization. No progress beyond the
checked general rank theorems is claimed.

## Proof

**Imported rank tools.** Reuse the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-27-residual-atiyah-normal-rank-constraint.md`.
Import rank subadditivity and composition bounds by the precise
theorem names `LinearMap.rank_add_le`,
`LinearMap.rank_comp_le_left` and `LinearMap.rank_comp_le_right`,
with the range/target bound `LinearMap.rank_le_range`:
[Mathlib, LinearAlgebra/Dimension/LinearMap, source revision
d79fa7b650321259f6f7257eec20974e91979f8d](https://github.com/leanprover-community/mathlib4/blob/d79fa7b650321259f6f7257eec20974e91979f8d/Mathlib/LinearAlgebra/Dimension/LinearMap.lean).
For the rank-one form use `Matrix.rank_vecMulVec_le`:
[Mathlib, LinearAlgebra/Matrix/Rank, source revision
2fbee2a0d2d8b7f09963e870ba493f5ac6ffc4af](https://github.com/leanprover-community/mathlib4/blob/2fbee2a0d2d8b7f09963e870ba493f5ac6ffc4af/Mathlib/LinearAlgebra/Matrix/Rank.lean).
The assessment inspected the complete relevant source proofs.
All spaces here are finite-dimensional over C; rank-nullity and
strong rank conditions hold, so these cardinal-rank statements
give ordinary integer-rank inequalities. Finite bases represent
the rank-one form by c times the outer product of ell's coordinate
vector with itself; a scalar multiplication cannot increase rank.
These general results need neither positivity nor a nonzero c.
They are imported, not reproved. What remains is their application
to the specified actual maps.

**Placement through the actual adjoint.** L174 proves
Q(fu,iIv)=0 for every u in D_1 and v in K_T, using L173's
identity mathfrak a_2=iI. L165's actual-adjoint identity gives

\[
 0=Q(fu,iIv)=S(Rfu,Iv).                                \tag{6}
\]

The orthogonal tangent/normal splitting in the hypotheses is
the cohomological splitting induced by L108's alternating
coefficient forms; L165's tensor-shift sign is the same on both
summands. Its tangent restriction is nondegenerate, so (6)
forces the tangent component of Rfu to vanish. Thus g_N=Rf
has target K_N. This uses orthogonality to the actual base image,
not a semiregularity vanishing assertion for f.

L165 supplies the actual Q-orthogonal decomposition

\[
 E=i(K)\mathbin{\perp_Q}\ker R,
 \qquad A|_{\ker R}:\ker R\xrightarrow{\sim}U.
\]

For every x in E its first component is iRx, since Ri=1.
The remaining component x-iRx is in ker R and has A-image Ax
because Ai=0. By the displayed isomorphism it is exactly T(Ax).
Apply this to x=fu. Since Rfu=g_Nu, both (2)'s decomposition
and its pairing identity follow, with no cross terms. In
particular g_N is the actual normal projection requested by the
target, rather than a normal component of an arbitrary lift.

**The point contribution retains its unknown norm.** For nonempty
Z, L175 gives Afu=-2pi i ell(u)w_k. Bilinearity, in the same
fixed normalization of Q, implies

\[
 Q_U(Afu,Afv)=(-2\pi i)^2\ell(u)\ell(v)Q_U(w_k,w_k)
             =c\ell(u)\ell(v).                         \tag{7}
\]

Even though w_k is nonzero, nondegeneracy of the complex bilinear
form Q_U does not imply Q_U(w_k,w_k) is nonzero. No such inference
is made. Combine (7) with (2) and L174's rank(G)=15 to obtain
(3). If Z is empty then W=U=0, Af=0, and (2) instead gives
g_N^*S_N=G exactly. This case requires no w_k or c.

**Ranks and dimension comparison.** Interpret each bilinear form
on D_1 as a map D_1 -> D_1^vee. Put H=g_N^*S_N and, for
nonempty Z, P=c ell tensor ell. Then G=H+P and rank(P)<=1
by the imported outer-product bound. Rank subadditivity gives

\[
 15=\operatorname{rank}G
       \le\operatorname{rank}H+\operatorname{rank}P
       \le\operatorname{rank}H+1.                      \tag{8}
\]

If b_N:K_N -> K_N^vee is the map associated with S_N, then
H=g_N^vee b_N g_N. The imported composition bounds imply

\[
 \operatorname{rank}H\le\operatorname{rank}g_N
                    \le\dim K_N.                     \tag{9}
\]

In particular (9) does not reverse the first inequality: a
nonzero image in an isotropic radical of the restricted form
can be invisible to H. Equations (8)–(9) prove the nonempty
case of (4). If c=0, H=G and its rank is fifteen. For empty Z
the same equality was already established, so (9) proves the
other case of (4). This checks every possible support case
without evaluating any point norm or radical image.

Equations (1), (4) and (9) give dim K_N>=14 uniformly and hence
s<=690+2t. If t=48, L116's conclusion in (1) forces s=800,
where dim K_N=704-800+96=0, contradicting this lower bound.
Therefore t!=48. Together with t<=48 and t!=47 from L116,
integrality gives t<=46. Substituting this upper bound gives

\[
                  s\le690+2(46)=782.
\]

For empty support the stronger normal bound reads 704+2t>=15
and is automatically satisfied. Thus it has not silently been
excluded, and no point of Z was assumed in the uniform conclusion.
The achieved threshold is fourteen normal directions versus the
previously available nonnegativity of 704-s+2t. It excludes the
formal endpoint with no normal cohomology but leaves every
existence, bracket and general primitive-realization question open.
Sharpening (3) requires additional evaluated data; this proof
neither assigns c a value nor claims its bound is optimal for F.

**Separate conceptual audit (2026-10-27, step 592).** The unchanged
invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-27-residual-atiyah-normal-rank-critical-audit.md`.
The audit imports the cited rank inequalities and reuses the assessed
duality coverage with its stated hypotheses. It checks this application
conditional on L108, L116, L165 and L173–L175; it is not a new audit of
the entire ancestry or an existence proof for the conditional family.

First distinguish three maps: L108's coefficient projection onto T_B,
L116's derived retraction r, and L174's Q-orthogonal projection P_2
onto the actual base Atiyah image. They are not interchangeable.
L108 extends the coefficient pairing, its inverse and the two splitting
maps across Z; their identities and cross-pairing zero extend as
bundle morphism identities. L111, retained in L116, identifies M with
that bundle. Thus b is block diagonal for this specific M=T_B direct
sum N, not merely for an abstract isomorphic bundle. Base Serre duality
and each invertible alternating coefficient form give perfect pairings
on H^1 of each summand. The common tensor-shift sign S=-B_M from
L165 affects both blocks identically. Therefore the splitting on K
is genuinely S-orthogonal, with perfect tangent and normal restrictions.
This does not assert metric preservation by j or r.

L173 identifies the actual base Atiyah map with iI globally, retaining
the finite top term. L174's definition of f=(1-P_2)mathfrak a_1
therefore gives Q(fu,iIv)=0 for all v in K_T. L165's mixed adjoint
identity holds for every x in E, including classes supported over Z:
Q(x,iv)=S(Rx,v). Write Rfu=I(v_T)+v_N in the fixed splitting.
Testing against every I(v) gives S_T(v_T,v)=0, whence v_T=0.
This checks the actual normal placement even if K_N is zero.
No semiregularity assertion about f is used; f is an Atiyah image,
not a section bracket to which bracket annihilation was applied.

Next, Ri=id and ker A=i(K) imply Ai=0. For any x in E, x-iRx
lies in ker R and has A-image Ax. The actual mixed adjoint gives
ker R=i(K)^{perp_Q}; since the restriction to i(K) is perfect,
this is an orthogonal direct sum. If y in ker R has Ay=0, then
y=iv and 0=Ry=v; conversely subtracting iRx from any lift of w
gives a lift in ker R. Hence A|ker R is bijective, and its inverse
T is exactly the lift used in Q_U. It follows that x=iRx+TAx
with zero cross-pairings. Applying this identity to f proves (2)
with the same Q, S_N and Q_U, not newly chosen forms or lifts.

For nonempty Z, L175 uses the actual top base-change isomorphisms
with the lower Tor terms retained, and one common line label k.
Its result is Af=-2pi i ell w_k, since the base-image correction
has zero A-image. Pulling Q_U back along this map yields precisely
c ell tensor ell with c=(-2pi i)^2 Q_U(w_k,w_k). The square is a
bilinear scalar square, not an absolute square. The point map has
rank one, but its pulled-back form may have rank zero: w_k nonzero
and Q_U nondegenerate do not rule out an isotropic w_k. The proof
uses only rank(P)<=1 and therefore covers that possibility. For
empty Z, U=0 and the point form is zero without defining w_k.

L174's rank fifteen concerns G=f^*Q, with the same normalization.
Writing H=g_N^*S_N gives G=H+P, so the imported rank inequalities
imply 15<=rank(H)+1. Moreover H, viewed as a map to D_1^vee,
is g_N^vee b_N g_N; hence rank(H)<=rank(g_N)<=dim K_N. No
converse is valid in general, since the restriction of S_N to the
image of g_N can have a radical. Thus the normal-map lower bound
is fourteen without evaluating any radical image. When P=0 it is
fifteen. In particular the empty-support case is retained, not
excluded by a point-map nonvanishing assertion. The argument needs
neither a positive form nor a known value of c.

Finally L116 computes dim K_N=704-s+2t for the actual bundle, and
its polystability argument makes t the full trivial multiplicity.
Its determinant argument excludes t=47; t=48 makes N trivial and
forces s=800. In that last case the normal dimension is
704-800+96=0, contrary to the uniform lower bound fourteen.
Consequently t<=46 and s<=704+2(46)-14=782. At s=782,t=46 the
dimension is fourteen, but this arithmetic does not establish
compatibility or attainment. For s=0 the stronger lower bound
fifteen reads 704+2t>=15 and is automatic. All integer endpoints
and both support cases therefore agree with (4)–(5).

The audit preserves every asserted conditional inequality and finds
no substantive error or stronger result. Its outcome is EXPLORATION /
REPRODUCTION, not a second advance for the original specialization.
The direct inputs already recorded in the DAG suffice and are unchanged.
Point norm, radical images, actual bracket values and existence of F
remain unresolved. No mathematical script, new lemma, square improvement
or claim of primitive Hodge realization is part of this audit.

## Mathlib

The general sum, composition, outer-product and target-dimension
rank inequalities are present under the precise theorem names and
source revisions cited above, with the finite-dimensional C
specialization justified here. Full matching coverage of these
actual Atiyah, truncation and normal-projection identities has
**not been checked**. No absence claim or local Lean verification
is made. The actual-map specialization and numerical consequence
have the separate informal conceptual audit above, not a formal
verification.
