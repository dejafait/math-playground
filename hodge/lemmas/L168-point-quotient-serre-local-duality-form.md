# L168 — Actual point-quotient Serre form in bracket coordinates

## Hypotheses

Retain the entire conditional family of L165 and L164, hence L071 and
L116 with their retained L108/L109/L111/L115 hypotheses. In particular
X=S_1 x B is the product of identical marked projective K3 surfaces,
with their original common metric, ordered hyperkähler triple, fixed
nonzero holomorphic forms sigma_1,sigma_B and actual connection. The
hypothetical locally free rank-two product-polystable F has integral
c_1(F)=0 and

\[
 \operatorname{ch}(F)=2-14e_1-21e_2-\tau_D+62P,
 \qquad P=e_1e_2,
\]

with the full prescribed mixed tensor. Set V=End_0(F), p:X -> B,
C=Rp_*V, M=R^1p_*V, W=R^2p_*V and D=RHom_B(-,O_B).
Use the actual normalized relative trace adjoint alpha:C[2] -> DC,
the actual arrows j:M[-1] -> C and a:C -> W[-2], and L116's
r=b^{-1}[-1] composed with (Dj)[-2]alpha[-2], with rj=id.
Here M is locally free,
b:M -> M^vee is the nondegenerate alternating form, and W is a sum
of length-one sheaves on the reduced finite, possibly empty split set Z.
Write W_z for its summand supported at z, W(z) for its residue line,
and W^dagger=Ext^2_B(W,O_B); thus DW=W^dagger[-2].

Use L109's actual gamma:W^dagger -> W, which is an isomorphism by
L111. Use L165's complex bilinear Serre form Q, its actual orthogonal
lift T:U=H^0(B,W) -> H^2(X,V), and Q_U(u,v)=Q(Tu,Tv).
The base trace is fixed by sigma_B. The same common nonzero relative
trace scalar is used in alpha,b,Q and gamma; it is not chosen separately
at different points. No Hermitian pairing is used.

Use L164's top derived-base-change isomorphism theta_z and its fixed
h_0=diag(1,-1) on each split fibre. Define the isomorphism of lines

\[
 \ell_z:W(z)\longrightarrow\mathbb C,\qquad
 \ell_z(w)=\frac{(2\pi i)^{-2}}2
   \int_{S_1}\sigma_1\wedge
        \operatorname{Tr}(h_0\theta_z(w)).                 \tag{1}
\]

No existence of F, value of t=h^0(B,M), section-image pairing,
integrability, multiplicative splitting or numerical residue constant
is assumed. No endpoint s=800,t=48 is required for this statement.

## Conclusion

The actual quotient adjoint, after identifying the orthogonal lift
with a derived morphism, is

\[
       \gamma^{-1}[-2]:W[-2]\longrightarrow
                  D(W[-2])[-2]=W^\dagger[-2].             \tag{2}
\]

Let ev_z:W_z^dagger x W(z) -> C be the perfect finite-support Serre
evaluation with the fixed base trace. Then

\[
 Q_U(u,v)=\sum_{z\in Z}
       \operatorname{ev}_z(\gamma_z^{-1}u(z),v(z)).        \tag{3}
\]

Here W_z^dagger means the residue space of the point-supported dual
summand. In particular different reduced points are Q_U-orthogonal.
Put n_z=ell_z^{-1}(1) and

\[
 \mu_z=\operatorname{ev}_z(\gamma_z^{-1}n_z,n_z)\ne0.
\]

In L164's fixed bracket coordinates, (3) is exactly

\[
 Q_U(u,v)=\sum_{z\in Z}\mu_z\ell_z(u(z))\ell_z(v(z)),
\]
\[
 Q_U(\beta(h,h),\beta(h,h))
   =\sum_{z\in Z}\mu_z
       B_z(\rho_z(h),\rho_z(h))^2.                       \tag{4}
\]

The weights are canonical with these choices, not arbitrary diagonal
matrix entries. A local Koszul expression for them is (10) below.
Multiplying the common relative trace by c multiplies all mu_z and
Q_U by c and leaves the orthogonal lift T unchanged. Z empty gives
the zero form on the zero space and an empty sum.

This is a conditional local ADVANCE / REPRODUCTION of the assessed
duality tools. It identifies the actual form but computes no actual
section quadrics or quartic coefficients. It provides no lower square
length, cardinality exclusion, F, transport or primitive Hodge
realization. The separate critical audit below preserves the formulas,
with outcome EXPLORATION / REPRODUCTION: no substantive error or stronger
conclusion was found.

## Proof

**Imported duality and its applicability.** Reuse the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-25-point-supported-quotient-serre-form.md`.
Import smooth proper relative duality from
[Stacks Lemma 48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT)
and its actual cup/evaluation/trace construction from
[Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81).
Import global Serre duality, functoriality and shift-compatible
evaluation followed by trace from
[Lemma 48.27.1(5),(7), Remarks 48.27.2–3 and Lemma 48.27.4,
0FVU](https://stacks.math.columbia.edu/tag/0FVU).
Here p is smooth proper of relative dimension two, B and X are smooth
projective, V is locally free and trace-self-dual, C is perfect, and
the fixed forms trivialize the canonical lines. These are precisely
the actual pairings retained in L109/L116/L165, not replacement forms.

For the point evaluation import finite-length duality from
[Lemma 57.11.2, 0G23](https://stacks.math.columbia.edu/tag/0G23),
the derived-Hom closed-immersion adjoint and its counit from
[Lemma 48.9.7, 0A9X](https://stacks.math.columbia.edu/tag/0A9X) and
[Example 48.9.8, 0B6M](https://stacks.math.columbia.edu/tag/0B6M),
and finite duality and evaluation at 1 from
[Lemma 48.11.4, 0AX2](https://stacks.math.columbia.edu/tag/0AX2) and
[Remark 48.20.12, 0AX4](https://stacks.math.columbia.edu/tag/0AX4).
Use composition of counits from
[Lemma 4.24.9, 0DV0](https://stacks.math.columbia.edu/tag/0DV0).
The inclusions of Z or a point into the Noetherian smooth surface B
are finite pseudo-coherent closed immersions; its local rings at Z
are regular of dimension two. All schemes are separated finite type
over C, with dualizing complexes normalized over that same field.
The fixed sigma_B identifies omega_B[2] with O_B[2]. Thus these
results apply without flatness of a point over B or local freeness
of W. They identify finite evaluation followed by the base trace
with the composite trace. No general duality theorem is reproved;
the specialization must still compare the actual arrows below.

**The actual derived lift and its adjoint.** Write q=alpha[-2], so
q:C -> DC[-2] is the flat map of the relative pairing. Form

\[
 \Lambda=\alpha^{-1}[-2]\circ(Da)[-2]:W^\dagger[-2]\to C.
\]

Indeed D(W[-2])=(DW)[2]=W^dagger. Since aj=0 and
f=(Dj)[-2]q=b[-1]r, composition gives

\[
 r\Lambda=b^{-1}[-1]D(aj)[-2]=0.                          \tag{5}
\]

The composite a Lambda is a morphism W^dagger[-2] -> W[-2], hence
is an ordinary sheaf morphism shifted by -2. At every stalk its
degree-two cohomology is exactly L109's gamma: that construction is
H^0(alpha^{-1}Da):W^dagger -> H^0(C[2])=W. The map a[2] induces
the identity on this H^0. Consequently, as global morphisms,

\[
 a\Lambda=\gamma[-2],\qquad
 \phi=\Lambda\gamma^{-1}[-2]:W[-2]\to C,\qquad
 a\phi=\mathrm{id},\quad r\phi=0.                        \tag{6}
\]

This is an identification in a sheaf Hom group, not an extension of
an arbitrary derived identity from B minus Z. L111 supplies the
invertibility of gamma, and L116 supplies all the actual global maps.
On H^2, (6) has image ker R and is a right inverse of A, so L165's
uniqueness proves H^2(phi)=T.

Pulling back the relative pairing through phi gives flat map

\[
 \begin{aligned}
 (D\phi)[-2]q\phi
   &=(D\phi)[-2]\circ(Da)[-2]\circ\gamma^{-1}[-2]\\
   &=D(a\phi)[-2]\gamma^{-1}[-2]
     =\gamma^{-1}[-2].                                   \tag{7}
 \end{aligned}
\]

Here q Lambda=(Da)[-2] follows directly from its definition. Dualizing
a composition reverses its arrows; no interchange of odd inputs is
made. This proves (2), and distinguishes gamma^{-1} from gamma and
from L116's zero transgression adjoint.

**Global trace, signs and the point decomposition.** For u,v in U,
gamma^{-1}u represents an element of
Ext^2_B(W,O_B)=H^0(B,W^dagger). Regarding v as O_B -> W, the
global Serre pairing furnished by (7) is

\[
 Q_U(u,v)=\operatorname{Tr}_B((\gamma^{-1}u)\circ v).
                                                               \tag{8}
\]

The composite is in Ext^2_B(O_B,O_B)=H^2(B,O_B).
There is no minus sign in (8): evaluation is ordered dual first,
as in L109's flat-map convention, and the identification
H^2(W[-2])=H^0(W) moves only the even shift -2. Unlike the
M[-1] contribution in L165, there are no two odd degree-one factors
to interchange. Functorial global cup/evaluation and the base trace
give precisely (8) from (7).

Decompose W=direct sum W_z. Duality gives the corresponding direct
sum for W^dagger, and gamma^{-1} is a sheaf morphism, so it preserves
these summands: a morphism between sheaves at distinct points has
every stalk zero. Derived evaluation of the dual of a direct sum
with that sum is the sum of the matching evaluations, with zero
off-diagonal components. This is the dual of the actual inclusions
and projections; it is not a matrix diagonalization of Q_U.

More explicitly set R=O_{B,z}, k=C. Finite-length duality gives

\[
 \operatorname{Ext}^2_R(W_z,R)
   =\operatorname{Hom}_{\mathbb C}(W(z),\mathbb C)
                \otimes_{\mathbb C}\operatorname{Ext}^2_R(k,R).
\]

Let tau_z:Ext^2_R(k,R) -> C be the isomorphism induced by
i_z^!O_B[2] -> C, using the fixed sigma_B and the normalized
dualizing complex over C. This is the finite evaluation trace, not
ordinary Hom_R(k,R). Define ev_z by contraction with W(z), followed
by tau_z. Composition of the closed-point counit with the base
counit is the composite counit, by the imported trace compatibility.
Thus (8) is the sum of these ev_z values. This proves (3), including
its normalization and orthogonality. Each ev_z is perfect; gamma_z
is invertible and both spaces are lines, so mu_z is nonzero.

**Transport into the bracket coordinate and a local weight formula.**
The map ell_z in (1) is invertible: theta_z is top base change, and
H^2(S_1,V_z)=H^2(S_1,O)h_0 is one-dimensional. Pairing with h_0
is nonzero since Tr(h_0^2)=2 and sigma_1 is nonzero. Hence (3) in
the basis n_z=ell_z^{-1}(1) is the first formula (4). L164 proves
ell_z(beta(h,h)(z))=B_z(rho_z(h),rho_z(h)); substituting proves
the second formula (4), with its full commutator normalization.

One can express mu_z by the actual local data of L111 without
assigning an analytic residue constant. Denote by kappa the common
relative trace scalar relative to L164's integral normalization.
In L111's actual orthogonal Koszul summand choose the degree-zero
generator reducing to h_0, a degree-two generator e_2, and middle
basis a_0,b_0. Write s_0 for the endpoint pairing, c_0 for the
middle pairing omega(a_0,b_0), and d=c_0/s_0. Both s_0,c_0 are
units in R. The summand has differentials

\[
 R\xrightarrow{(x,y)^t}R^2
      \xrightarrow{d(y,-x)}R,
\]

and represents W_z[-2]. Write w for the residue of e_2, so W(z)=Cw.
Its actual flat map sends e_2 to s_0 times the dual bottom generator.
This follows from the endpoint pairing s_0, with the same even
shift convention as L109/L111.

Define epsilon_{x,y} in Ext^2_R(k,R) by the functional 1 on the
leftmost module of the standard resolution

\[
 R\xrightarrow{(-y,x)^t}R^2\xrightarrow{(x,y)}R\to k.
\]

Identify W_z with k using w. The comparison from this resolution
to the preceding actual summand shifted by 2 has components, in
degrees -2,-1,0,

\[
 d^{-1},\qquad
 \begin{pmatrix}0&d^{-1}\\-d^{-1}&0\end{pmatrix},\qquad 1.
\]

For verification, multiplying the middle matrix by (-y,x)^t gives
(x/d,y/d)^t, while d(y,-x) times that matrix is (x,y). Its
degree-zero map is the identity and hence respects the augmentation.
Pulling the dual bottom generator back multiplies it by d^{-1}.
Thus the local Ext evaluation on (w,w) is

\[
 (\gamma_z^{-1}w)(w)
       =\frac{\bar s_0^{\,2}}{\bar c_0}\epsilon_{x,y}.
                                                               \tag{9}
\]

Bars mean reduction modulo the maximal ideal; it annihilates this
Ext line. The endpoint trace and (1) give
ell_z(w)=bar(s_0)/(2 kappa), with the factor 2 coming from h_0.
Scaling both entries of (9) to n_z therefore yields

\[
 \boxed{\displaystyle
  \mu_z=\frac{4\kappa^2}{\bar c_0}\tau_z(\epsilon_{x,y}).}
                                                               \tag{10}
\]

This retains the local evaluation functional and its orientation:
epsilon_{x,y} is specified by the displayed arrows, not a numerical
residue convention. Independence of the chosen parameters and free
generators follows from its identification with the canonical mu_z
in (3)–(4). No formula for tau_z(epsilon_{x,y}) in analytic coordinates
is asserted. Multiplying the common relative pairing by c scales
s_0,c_0,kappa by c, leaves d and phi unchanged (alpha^{-1} and
gamma^{-1} scale oppositely), and scales (10) by c, as required.

The continuation test is met at the level requested: (4) is usable
on the actual point-section quadrics, with weights given by genuine
local duality rather than an arbitrary normal form. Those section
quadrics and their interactions are still unknown. In particular,
nonzero mu_z do not make the complex bilinear quartic nonzero,
generic, or of any prescribed minimum square length. L167's actual
necessary identity remains compatible with (4), and no parked
vanishing or exclusion in ATTEMPTS/092–094 is reopened.

**Separate critical audit (2026-10-26, step 559).** Reuse the
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-25-point-quotient-serre-critical-audit.md`.
This audit checks (5)–(10), retaining every conditional hypothesis above.
It imports the previously inspected duality statements cited here; it
does not reprove them or certify all upstream results afresh. In
particular L111's actual paired complex, L116's actual global retraction
and L164's derived base-change comparison remain mathematical inputs.

First check domains and the inverse direction. Put A=W[-2]. Then
DA=W^dagger and q=alpha[-2]:C -> DC[-2]. The composite
Lambda=q^{-1}(Da)[-2] has domain DA[-2]. Because
r=b^{-1}[-1] composed with (Dj)[-2]q and aj=0, its composite with r is zero.
Moreover a Lambda lies in
Hom_D(W^dagger[-2],W[-2])=Hom_B(W^dagger,W). It is therefore
determined by its degree-two cohomology sheaf map, not by restriction
to the complement of Z. Its stalk map is
H^0(a[2]alpha^{-1}Da)=gamma: a[2] is the identity on H^0(C[2]).
Thus a Lambda=gamma[-2] globally. Since gamma is invertible by
L111, phi=Lambda gamma^{-1}[-2] has a phi=id and r phi=0.
On H^2, L165's exact sequence and actual orthogonal decomposition
identify H^2(phi) with the unique lift T. In particular an arbitrary
additive splitting has not entered the calculation.

Now q phi=(Da)[-2]gamma^{-1}[-2]. Applying (Dphi)[-2] on the
left gives D(a phi)[-2]gamma^{-1}[-2]=gamma^{-1}[-2]. This verifies
(7) with its domains; it could not give gamma, whose direction is
opposite. The comparison uses only reversal of compositions under D,
with degree-zero morphisms, so introduces no interchange sign.

For the global sign, use dual-first evaluation as specified in
[Stacks Example 20.50.7, 0FPC](https://stacks.math.columbia.edu/tag/0FPC)
and its use in [Lemma 48.27.4, 0FVU](https://stacks.math.columbia.edu/tag/0FVU).
Shifting the flat map for A back by two gives precisely the sheaf map
gamma^{-1}:W -> W^dagger. Its value on u corresponds to the class
W -> O_B[2]. Composing with the section v:O_B -> W and taking
Tr_B is (8). All tensor-shift interchanges in this identification
involve the even integer two; hence their signs are +1. There is no
analogue of the two odd factors in L165's M[-1] calculation. Global
Ext^2_B(W,O_B)=H^0(W^dagger) follows from DW=W^dagger[-2]
and finite support. This is a global Ext class: it is not evaluated
by falsely replacing it with Ext^2_R(R,R), which would vanish.

For each point, write W_z=i_{z*}W(z). The finite adjunction of
0A9X/0B6M and 0AX2 gives
DW_z=i_{z*}(W(z)^* tensor i_z^!O_B[2])[-2], where W(z)^*
is the vector-space dual and i_z^!O_B[2] is a line in degree zero.
The fixed base
form and normalization over Spec C give the stated tau_z on this
one-dimensional line. The trace in 0AX4 is evaluation at 1, and
the composition-of-counits identity 0DV0 identifies the closed-point
trace followed by the base trace with the trace to C. These hypotheses
hold for the finite closed immersions into the smooth proper surface;
no point is assumed flat over B. Thus their contraction is exactly
ev_z in (3). For different points, a sheaf map W_z -> W_{z'}^dagger
is zero stalkwise. Evaluation also pairs only matching summands under
the canonical finite direct-sum duality. This verifies orthogonality
without diagonalizing a global matrix. Perfect evaluation and the
invertible map between residue lines imply mu_z is nonzero.

Independently check the local adjoint's sign. In the actual Koszul
summand of L111 let u=(x,y)^t, v=d(y,-x), d=c_0/s_0, and
J=[[0,-1],[1,0]]. In degrees -2,-1,0 its adjoint K[2] -> DK has
components s_0,c_0 J,s_0 under L109's dual differential convention.
Indeed

\[
 (c_0J)u=(-c_0y,c_0x)^t=-v^t s_0,
 \qquad u^t(c_0J)=(c_0y,-c_0x)=s_0v.
\]

These check both nonzero chain equations. Endpoint symmetry gives
the same s_0 at both ends; the middle component implements
omega(a_0,b_0)=c_0. The orthogonal rank-fifty middle summand has
zero cross-pairing with this Koszul complex. Its inclusion therefore
computes the restriction of the actual pairing. Locally it is the
lift with a phi=id and r phi=0, so it computes the same quotient
adjoint as (7).

Let P resolve k with the displayed arrows (-y,x)^t and (x,y).
The comparison P -> K[2] is
(d^{-1},-d^{-1}J,1). Its chain equations are
(-d^{-1}J)(-y,x)^t=(x/d,y/d)^t=u d^{-1} and
v(-d^{-1}J)=(x,y). Its last component is 1, so its augmentation
is the specified identification by w, not a rescaling of that line.
The top generator e_2 maps under the flat map to s_0 times the dual
bottom generator. Pullback by this comparison multiplies that
functional by d^{-1}. Consequently the Ext coefficient evaluated
on (w,w) is bar(s_0/d)=bar(s_0)^2/bar(c_0), with precisely the
orientation epsilon_{x,y} in (9). No residue value is used.

Finally, the bottom generator reduces to the fixed h_0, while the
top generator reduces to theta_z(w). Actual base change of the trace
pairing gives
bar(s_0)=kappa (2 pi i)^{-2} integral sigma_1 wedge
Tr(h_0 theta_z(w))=2 kappa ell_z(w). Since bar(s_0) and kappa
are nonzero, n_z=(2 kappa/bar(s_0))w. Bilinearity supplies this
factor twice in (9), giving exactly (10). L164's polarized bracket
identity then yields (4), including its twice-Yoneda-square convention.
Changing a local generator or parameters cannot change (10)'s value:
for every such choice the preceding augmentation-preserving comparison
identifies it with the same ev_z(gamma_z^{-1}n_z,n_z). No numerical
orientation or independent pointwise rescaling has been introduced.

Under a common relative trace rescaling by c, alpha,b,q scale by c,
gamma and Lambda scale by c^{-1}, and gamma^{-1} scales by c.
Hence r and phi, and therefore T, are unchanged. The fixed bracket
coordinate ell_z and the fixed base functional tau_z are unchanged.
The quantities s_0,c_0,kappa scale by c, so (10) and Q_U scale
by c, not c^2 or c^{-1}. If Z is empty, W=U=0, the unique maps
on the zero object give the same identities, and every sum is empty.
No local generator or nonzero mu_z is asserted in that case.

All formulas (5)–(10) survive. This audit supplies neither numerical
tau_z values nor actual section quadrics, their minimum square length,
a compatible complementary operation or an exclusion of F. It leaves
ATTEMPTS/092–094 intact and is EXPLORATION / REPRODUCTION, not a
new mathematical advance beyond the imported framework.

## Mathlib

Full matching coverage of this derived actual-arrow comparison,
finite-support trace normalization and bracket-coordinate formula has
not been checked. No absence or formal verification is asserted. The
primary results above are imported; the separate informal critical
audit verifies the family-specific specialization (5)–(10) under its
retained conditional inputs, without certifying the unresolved main gap.
