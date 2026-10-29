# L173 — Semiregularity detects the actual base-tangent obstruction

## Hypotheses

Retain the full conditional family of L116, L165 and L171. Thus
X=S_1 x B is the product of the identical marked projective K3
surfaces with the original common metric, ordered triple, holomorphic
forms sigma_1,sigma_B and actual connection. The hypothetical locally
free rank-two product-polystable F has integral c_1(F)=0 and

\[
 \operatorname{ch}(F)=2-14e_1-21e_2-\tau_D+62e_1e_2,
\]

with the full prescribed mixed tensor. Set p:X -> B,
V=End_0(F), C=Rp_*V, M=R^1p_*V and W=R^2p_*V. In particular
H^0(C)=0; M is locally free and carries L116's perfect alternating
relative Serre form b; W has length one at each point of the finite
reduced, possibly empty, split set Z. Write s=|Z| and
t=h^0(B,N), without assuming either value.

Write iota:T_B -> M for L108's specific extended family KS inclusion,
and retain its b-orthogonal splitting M=iota(T_B) direct sum N.
The letters iota and i below denote different maps. Use L116's actual
truncation and trace-adjoint arrows

\[
 M[-1]\xrightarrow{j}C\xrightarrow{a}W[-2]\longrightarrow M,
 \qquad r:C\longrightarrow M[-1],\qquad rj=1.
\]

Put H=H^0(B,M), K=H^1(B,M), E=H^2(X,V), U=H^0(B,W),
j_1=H^1(j), i=H^2(j), R=H^2(r), A=H^2(a). Use L165's
fixed symmetric complex bilinear Serre form Q on E and
S(v,w)=Q(iv,iw) on K. Let

\[
 K_T=H^1(B,T_B),\quad K_N=H^1(B,N),\quad I=H^1(\iota),
 \quad K=I(K_T)\oplus K_N,
\]

and let pi_T denote this fixed projection to K_T. All traces below
use the same nonzero relative normalization and base volume as Q.
Neither these forms nor the square expressions below are Hermitian.

Use the actual Yoneda commutator with no factor 1/2, as in L166/L167.
No existence of F, integrability of arbitrary section directions,
semiregularity injectivity, metric-star preservation, multiplicative
splitting or value of the point bracket is assumed.

## Conclusion

There is an actual base trace–Atiyah map

\[
 D_B:E\longrightarrow H^1(B,\Omega_B^1)
\]

of rank 20 whose kernel is exactly

\[
 \ker D_B=\{x:\pi_T R x=0\}=i(K_N)\oplus\ker R.       \tag{1}
\]

It is obtained from the base-cotangent component of degree-one
semiregularity, followed by the fixed fibre trace, with the single
universal Atiyah sign specified in the proof. Hence, for h,k in H,

\[
 \pi_T R[j_1h,j_1k]=0.                                  \tag{2}
\]

In particular the section evaluation of L166's actual complementary
operation takes values in K_N. No vanishing of its underlying global
Ext^1 morphism is asserted.

Let T=(A|_{ker R})^{-1}:U -> ker R be L165's actual orthogonal lift,
Q_U(u,v)=Q(Tu,Tv), and S_N=S|_{K_N}. Set

\[
 \beta_{\rm br}(h)=A[j_1h,j_1h],\qquad
 g_N(h)=R[j_1h,j_1h]\in K_N.
\]

Then

\[
 Q_U(\beta_{\rm br}(h),\beta_{\rm br}(h))
                  =-S_N(g_N(h),g_N(h)).                 \tag{3}
\]

Consequently the actual point quartic is an exact sum of at most
704-s+2t complex quadratic squares, allowing zero. At the formal
endpoint s=800,t=48, g_N=0 and the point quartic is identically zero.
This does not say that beta_br is zero, or that this endpoint exists
or survives independent constraints.

The original result is a conditional ADVANCE / REPRODUCTION: a
source-covered actual-map specialization that removes twenty complementary
directions, not a new general semiregularity theorem. The separate step
581 conceptual audit below preserves it, with EXPLORATION / REPRODUCTION
and no substantive error or stronger conclusion found.
It computes no actual section quadric, excludes no F or split
cardinality, and supplies no cycle, transport or primitive realization.

## Proof

**Imported inputs and applicability.** Reuse the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-26-semiregularity-base-tangent-detector.md`
and its completed parent source review. Import R.-O. Buchweitz and
H. Flenner, *A Semiregularity Map for Modules and Applications to
Deformations*, Compositio Math. **137** (2003), 135–210,
[arXiv:math/9912245v1, Corollary 4.8, printed p.32](https://arxiv.org/pdf/math/9912245v1#page=32):
semiregularity annihilates graded Yoneda commutators. Its q=1 component
on Ext^2 is c -> Tr((-At(F)) c) in H^3(X,Omega_X^1).
F is locally free, hence perfect, and X is smooth projective over C;
the theorem needs neither simple fibres nor semiregularity injectivity.
The theorem and the cited truncation triangle were spot-checked at
their original statements in this step. No fresh discovery assessment
or reproof of commutator annihilation is needed. The parent review's
stronger all-obstruction theorems are not needed for (2).

Reuse L171's all-family Atiyah/KS construction, including its universal
extension sign, from Huybrechts–Lehn, *The Geometry of Moduli Spaces
of Sheaves*, E31 (1997), 10.1.5, 10.1.7–9,
[pp.218–221](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=230),
and Kuhn, *The Atiyah class on algebraic stacks*, Forum Math. Sigma
**12** (2024), e100, [DOI 10.1017/fms.2024.109](https://doi.org/10.1017/fms.2024.109),
Lemma 4.4/Claim 4.5, Corollaries 4.6–4.7 and Lemmas 6.11–6.12.
Use the canonical truncation triangle from
[Stacks 13.12.4, 08J5](https://stacks.math.columbia.edu/tag/08J5).
For trace, projection formula and Serre transpose use the actual
evaluation/trace duality of
[Stacks 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81)
and [48.27.1–2, 0FVU](https://stacks.math.columbia.edu/tag/0FVU),
already specialized with shifts in L165. Here p is smooth proper,
V and the tangent/cotangent bundles are locally free, and the complexes
are perfect. W need not be locally free. The following comparison,
not those general constructions, is the work of this lemma.

**The global lift is forced by truncation.** Let a_B be the trace-free
base component of the Atiyah class, multiplied by L171's one global
sign so that its first-order family class is +[a] for
bar-partial_F+epsilon a. The product splitting of Omega_X^1 selects
this component. Derived adjunction gives L171's morphism

\[
 \alpha:T_B[-1]\longrightarrow C,
 \qquad H^1(\alpha)=\iota.                              \tag{4}
\]

We now compare these maps globally, without using a stalk-to-global
principle for derived morphisms. Apply Hom_D(B)(T_B[-1],-) to the
actual truncation triangle. The two groups flanking the map induced
by j are

\[
 \operatorname{Hom}(T_B[-1],W[-3])
       =\operatorname{Ext}^{-2}(T_B,W)=0,
\]
\[
 \operatorname{Hom}(T_B[-1],W[-2])
       =\operatorname{Ext}^{-1}(T_B,W)=0.
\]

Negative Ext between sheaves vanishes in the standard derived category;
these are global groups, not sheaf Exts. Exactness therefore gives

\[
 \operatorname{Hom}(T_B,M)
   \xrightarrow[\ j\circ(-)[-1]\ ]{\sim}
   \operatorname{Hom}_{D(B)}(T_B[-1],C).                 \tag{5}
\]

The inverse takes degree-one cohomology because H^1(j)=id_M.
Equation (4) hence implies the actual global identity

\[
                     \alpha=j\iota[-1].                \tag{6}
\]

H^0(C)=0 is essential to this truncation argument. It does not treat
T_B as a projective object in the global sheaf category or discard
W. In contrast, L166's complementary operation has positive global
Ext degree one; (5) does not make that operation vanish.

**The actual trace transpose.** Define

\[
 \theta_B(x)=\operatorname{Tr}_F(a_B\smile x)
                 \in H^3(X,p^*\Omega_B^1).
\]

The scalar part removed from At(F) makes no contribution for x in E:
Tr_F((id_F tensor c) cup x)=c cup Tr_F(x)=0. Thus theta_B is
the base projection of the q=1 semiregularity component, up to the
one universal sign comparing a_B with -At(F). In particular
theta_B annihilates the actual trace-free commutators. This argument
does not replace At(F) by c_1(F) or omit its non-scalar part.

Let tau_p:Rp_*O_X -> O_B[-2] be the relative Serre trace obtained
from sigma_1, with L165's same nonzero relative normalization.
The projection formula and tau_p tensor id_Omega induce

\[
 H^3(X,p^*\Omega_B^1)\longrightarrow H^1(B,\Omega_B^1).
\]

Define D_B as its composite with theta_B. Let

\[
 P_B(\eta,u)=\operatorname{Tr}_B
                  \operatorname{ev}(\eta\smile u)
\]

for eta in H^1(Omega_B^1), u in K_T. It is the perfect base Serre
pairing under the fixed sigma_B trivialization. The fibre and base
traces compose to the normalized fourfold trace used in Q.

To check the transpose, pull u back to H^1(X,p^*T_B). Under
adjunction, the action of (4) on this class is contraction of
a_B cup p^*u, in H^2(X,V); (6) identifies it with iIu. Trace
functoriality and the projection formula give

\[
 \begin{aligned}
 P_B(D_Bx,u)
 &=\operatorname{Tr}_X\operatorname{ev}
                   (\operatorname{Tr}_F(a_B\smile x)\smile p^*u)\\
 &=Q\bigl(x,\operatorname{ev}(a_B\smile p^*u)\bigr)\\
 &=Q(x,iIu)=S(Rx,Iu).                                  \tag{7}
 \end{aligned}
\]

Here the cohomological degrees of a_B,x,p^*u are 1,2,1.
Moving a_B past x in the traced expression has sign (-1)^2=+1;
the cotangent/tangent coefficients are sheaves in degree zero.
The fibre trace has even degree -2, and the chosen volume forms
have even exterior degree, so they introduce no additional interchange
sign in this projection formula. The shift H^2(alpha) has domain
H^1(T_B), exactly the total degree of a_B cup p^*u. This verifies
the transpose using the actual maps, not only a fibrewise KS identity.
Equation (7) uses the stated Yoneda order and common trace normalization.
Changing the universal Atiyah/shift convention or the trace normalization
throughout introduces only its fixed nonzero sign/scalar; it cannot
change the kernel or introduce point-dependent weights. The final
equality is precisely L165's already normalized adjoint identity,
including its S=-B_M tensor-shift sign.

**Detection and annihilation.** L108's splitting is b-orthogonal and
both coefficient forms are nondegenerate. Consequently

\[
 (K,S)=(I(K_T),S_T)\mathbin{\perp}(K_N,S_N)
\]

with perfect symmetric restrictions. Indeed Serre duality pairs
H^1 of each bundle with H^1 of its dual, and its alternating
coefficient form is an isomorphism to that dual. The base degree-one
sign and coefficient alternation combine to give symmetry as in L165.
Equation (7) becomes

\[
                 P_B(D_Bx,u)=S_T(\pi_T Rx,u).            \tag{8}
\]

Perfectness on both sides proves ker D_B=ker(pi_T R). On x=iIv,
the right side is S_T(v,u). Thus D_B restricted to iI(K_T) is an
isomorphism onto H^1(Omega_B^1); L116 gives dim K_T=20.
In particular this is an actual rank-20 detector. L165's decomposition
x=iRx+T(Ax) gives (1). The actual point lift T(Ax) is killed by
D_B because it lies in ker R: there is no unidentified cancellation
between the point quotient and tangent component.

Apply the imported commutator theorem to j_1h,j_1k, regarded in
Ext^1_X(F,F) through V -> End(F). The graded commutator remains
in V, and theta_B, hence D_B, vanishes on it. Equation (8) proves
(2), with no assumption that either direction integrates. It applies
in particular to the diagonal bracket, twice the Yoneda square.

**The remaining polynomial constraint.** L167's degree-four argument
applies for all s,t: it uses cyclicity and graded Jacobi for the actual
degree-one class v=j_1h to give Q([v,v],[v,v])=0. Its proof has no
endpoint assumption at that step. Reuse that identity, rather than
the endpoint-specific dimension statement or its formal witness.
By (2) and L165's actual orthogonal decomposition,

\[
 [j_1h,j_1h]=i g_N(h)+T\beta_{\rm br}(h).
\]

The two terms are Q-orthogonal. The cyclic identity is therefore
exactly (3). Both maps are homogeneous quadratic maps, since the
actual bracket is bilinear and A,R are linear. L116 gives

\[
             n:=\dim K_N=704-s+2t\ge0.
\]

Use the complex symmetric-form diagonalization already imported in
L165/L167 (Elman–Karpenko–Merkurjev, *The Algebraic and Geometric
Theory of Quadratic Forms*, AMS 56 (2008), Chapter I, Proposition
1.6 and Corollary 1.9,
[pp.13–15](https://www.math.ucla.edu/~rse/book/Kniga.pdf#page=23)).
Since S_N is nondegenerate, take a basis with S_N=diag(1,...,1).
Writing g_N=sum p_a e_a with homogeneous quadratic p_a, (3) gives
Q_U(beta_br,beta_br)=sum (sqrt(-1)p_a)^2, with at most n squares.
This is an exact polynomial identity, not a border-rank assertion
or a pointwise choice of square roots.

At s=800,t=48, n=0, so g_N=0 and this polynomial is zero. A
nonzero vector or quadratic map may be isotropic over C; the result
does not infer beta_br=0. L167's formal witness remains a formal
test, not an actual geometric map. If t=0 then H=0 and the bracket
statement is vacuous, although the rank-20 detector statement still
holds conditionally. If Z is empty then U=0 and (3) says only that
g_N has S_N-isotropic values, not that g_N vanishes. No assumption
of a nonempty split set, strict normal stability or generic bracket
was used. Independent normal and point operations, F's existence,
transport and primitive realization remain unresolved.

**Separate conceptual audit (2026-10-26, step 581).** The invocation-start
SPECIALIZE assessment is
`drafts/literature/2026-10-26-semiregularity-tangent-detector-critical-audit.md`.
This audit uses its already inspected primary statements and proof cases,
and the conditional results cited above. It neither reopens source
discovery nor independently audits their entire ancestry. Its scope is
the actual global lift, transpose, rank and polynomial consequence,
including empty Z and t=0. No substantive defect was found.

First check global uniqueness with the actual degrees. The preceding
term in the triangle is W[-3], not W[-1]. Thus the exact Hom sequence
has outer terms Ext^{-2}(T_B,W) and Ext^{-1}(T_B,W). Both are zero
for sheaves in the standard derived category, regardless of positive
global Ext groups. The intervening group is Hom(T_B,M), since source
and target both have shift -1. Consequently every map T_B[-1] -> C
has one and only one factor through j. Taking degree-one cohomology
identifies that factor with the map to M, because j induces id_M.
L171's H^1(alpha)=iota therefore proves (6) globally. No splitting
of W, projectivity in the global sheaf category or gluing of local
derived equalities is used. The absence of a degree-zero sheaf of C
is retained. This argument does not apply to L166's positive global
Ext^1 operation.

Next check the precise action of alpha on cohomology. A closed
Dolbeault representative a of a_B has degree one and coefficients
V tensor p^*Omega_B^1. Treat the cotangent factor as a coefficient
bundle in degree zero, as in the coherent cup product. Contraction
u -> ev(a cup u) is a map from the shifted Dolbeault complex of
p^*T_B[-1] to that of V: its compatibility with the differential
is d(a cup u)=-a cup du, matching the differential -d on the source.
After derived adjunction, its degree-one sheaf map on B is L171's
KS map with the already fixed first-order convention. On a closed
degree-one u it gives the degree-two class ev(a cup p^*u).
Thus the latter is H^2(alpha)(u)=iIu with
the stated shift convention, not a separately chosen lift of Iu.
This representative check fixes the action and sign of the imported
Atiyah construction; it is not a reproof of that construction.

With this convention the transpose calculation is exact. In
Tr_F(a cup x) cup p^*u, the degrees are 1,2,1. Graded cyclic trace
moves a past x with sign +1, and the degree-zero tangent/cotangent
evaluation gives Tr_F(x cup ev(a cup p^*u)). The total degree is
four. Projection formula and composition of the fixed fibre and base
traces give Q(x,iIu). The relative trace shift is -2, so its interchange
introduces no odd sign. The canonical trivializing forms have even
degree. The scalar part removed from the Atiyah class contributes
only its cup with Tr_F(x), which is zero for the actual V-valued x.
This verifies (7) on all of E, including the orthogonal point lift;
no pure-relative representatives or ordinary base change at Z have
been assumed. L165's actual mixed adjoint identity now gives
Q(x,iIu)=S(Rx,Iu). Its base-first sign S=-B_M is already part of S,
so no second minus sign should be introduced in this last equality.
A simultaneous different Atiyah or trace convention changes the
detector by the corresponding common nonzero scalar, not its kernel.

The two perfectness assertions in (8) are distinct and both hold.
P_B is the Serre pairing of H^1(Omega_B^1) with H^1(T_B), using
omega_B=O_B. For S_T and S_N, L108's alternating coefficient forms
are bundle isomorphisms to the respective duals. Applying H^1 and
base Serre duality makes their middle-cohomology pairings perfect.
The odd base cup and coefficient alternation cancel to make these
pairings symmetric; the common tensor-shift sign does not alter
their radicals. Coefficient orthogonality gives cohomological
orthogonality. Thus testing against every Iu detects precisely the
tangent projection of Rx, even if K_N is zero. Since Ri=id and
dim H^1(T_B)=20, this detector has rank exactly twenty. L165's
ker R=i(K)^{perp_Q} and its fixed lift T imply (1), including that
D_B T=0. A point component cannot cancel a nonzero tangent component.

The imported Buchweitz--Flenner commutator statement applies to the
actual Ext^1 classes of the locally free F on smooth projective X.
The trace of a graded commutator is zero, so those commutators are
indeed in the trace-free summand E. Projecting its q=1 identity to
the base cotangent component and then applying the fibre trace
preserves zero. Equation (8) consequently yields (2) without any
injectivity of full semiregularity or integrability of the inputs.
This controls section evaluations of L166's operation, not its
global Ext^1 class.

Finally check the dimension-free part used from L167. For the actual
degree-one v=j_1h, graded Jacobi gives -3[v,[v,v]]=0 over C and
the invariant trace pairing gives Q([v,v],[v,v])=0. The argument
uses only degrees 1,1,2 and 1,3; it has no s,t or endpoint assumption.
Using (2) in the actual orthogonal decomposition leaves exactly
i g_N(h)+T beta_br(h). There is no tangent term or mixed pairing,
so (3) follows with its minus sign. The bracket diagonal is twice
the Yoneda square in BOTH components; using squares instead would
multiply both sides of (3) by 1/4, not change the square count.
Each component of g_N in one fixed basis is a homogeneous quadratic
polynomial. Diagonalizing the fixed nondegenerate complex form S_N
therefore yields an exact polynomial expression with at most
n=704-s+2t squares. No pointwise square-root choice or border-rank
argument enters. The arithmetic agrees with
dim K=20+n=724-s+2t and dim E=20+n+s=724+2t.

At s=800,t=48, n=704-800+96=0, so g_N and the scalar point
quartic vanish. This does not make beta_br vanish over C. For empty
Z, U=0 and the identity allows isotropic values of g_N. For t=0,
H=H^0(M)=0 by L116 and the section bracket assertion is vacuous,
whereas the rank-twenty linear detector on E remains valid. Negative
n is incompatible with an actual family's cohomology dimension,
not an additional family allowed by the statement. No new bound on
t or s, actual section quadric, or exclusion of F follows. The audit
therefore preserves the conditional restriction and the recorded
limits of ATTEMPTS/004,/009,/068,/092--095; it is EXPLORATION /
REPRODUCTION, not new mathematical progress beyond the checked sources.

## Mathlib

Full matching coverage for trace–Atiyah semiregularity and this actual
global Leray/Serre comparison has not been checked; no absence is
claimed. The primary sources above supply the imported general
theorems. The family-specific proof and its separate conceptual audit
are informal; they are neither a formal verification nor a complete
candidate for the Hodge conjecture.
