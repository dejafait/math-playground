# L155 — Complete cubic residual/action connected contraction

## Hypotheses

Keep L011's SU(2) fixed-mesh expansion in the relative box (-4,4)^4,
a=8/N through sufficiently fine admitted even meshes, with L008's full
compact displacement and both actual L010 probes at tau=1/16. Use
L026's straight direction-1 lower-rooted forest, including the omitted
upper axial edge and all physical-boundary conditions. The bare
small-coupling coefficient is taken at fixed mesh before refinement.

In dimensionless exponential coordinates theta=g x, write Sigma_F and
B_(i,F) exactly as in L018(3). Thus the three colors have covariance
Sigma_F independently and f_(i,0)=sum_c (x^c)^T B_(i,F) x^c up to a
constant. The probe uses full-link linear Wilson flow started on the
slice, not the restricted forest Hessian's flow. Select only

\[
 H_{i,a}=-\kappa_0(f_{i,0},r_1,S_3),\qquad i=3,6.                 \tag{1}
\]

Use L149(4)–(6)'s ordered word coefficients W_(w,m), clover coefficients
C_(rho nu,m), left-frame generator coefficients X_(e,m), and force
coefficients G_(e,m). These are polynomials in full link coordinates
Theta_e=theta_e^c t_c, with t_c=i sigma_c/2 and
<Y,Z>=-2 Tr(YZ). Fixed links are identity. Forest coordinates are set
to zero only after forming the full action variation.

## Conclusion

The complete cubic residual is the following finite local polynomial:

\[
\begin{split}
 r_1={}&\left\{\sum_e\bigl(
       \langle G_{e,1},X_{e,2}\rangle
       +\langle G_{e,2},X_{e,1}\rangle\bigr)
       +4\sum_p\widetilde b_p\operatorname{Tr}W_{w_p,3}\right.\\
 &\left.\quad+2\sum_{z,\mu<\nu}s_{a,\mu\nu}(z)\sum_\alpha
       \operatorname{Tr}\bigl(
       C_{\mu\alpha,1}(z)C_{\nu\alpha,2}(z)
       +C_{\mu\alpha,2}(z)C_{\nu\alpha,1}(z)\bigr)
       \right\}\circ I_F .                                    \tag{2}
\end{split}
\]

The edge sum is over full variable links, including forest links
before restriction. The plaquette and vertex sums here have the actual
compact insertion weights. In contrast, S_3 contains every action
plaquette in the box, including physical-boundary plaquettes.

Separate (2) into local summands q_lambda, one per edge, weighted
plaquette, or supported vertex/plane. In each stencil list its distinct
positive link variables y_1,...,y_m. A repeated word occurrence uses
the same variable. There are real coefficients h_(lambda,rst),
alternating in r,s,t and zero on repeated indices, such that

\[
 q_\lambda(y)=\sum_{r<s<t}h_{\lambda,rst}\,
                    y_r\cdot(y_s\times y_t).                    \tag{3}
\]

These coefficients are explicitly specified by (2) and L149's finite
word formulas: for r<s<t, extract the coefficient of
y_r^1 y_s^2 y_t^3 in q_lambda, and extend alternatingly. Let P_lambda
map the one-color forest coordinates to this stencil, putting zero
on forest/fixed rows. Let J_p be L048's four-row signed-edge selection
in traversal order for any action plaquette p. Define rectangular blocks

\[
 C_{\lambda p}=P_\lambda\Sigma_F J_p^T,\qquad
 U_{i,\lambda p}=P_\lambda\Sigma_F B_{i,F}\Sigma_F J_p^T.          \tag{4}
\]

With omega_(uvw) equal to +1 on increasing triples in {1,2,3,4},
alternatingly extended and zero on repetitions, the exact complete
response (1) is

\[
 \boxed{H_{i,a}=3\sum_{\lambda,p}\sum_{r,s,t=1}^{m_\lambda}
       \sum_{u,v,w=1}^{4}
       h_{\lambda,rst}\omega_{uvw}
       (U_{i,\lambda p})_{ru}
       (C_{\lambda p})_{sv}(C_{\lambda p})_{tw}.}                \tag{5}
\]

In particular, either product of the last two entries may be replaced
jointly by its alternating minor with coefficient 3/2:

\[
 H_{i,a}=\tfrac32\sum_{\lambda,p,r,s,t,u,v,w}
 h_{\lambda,rst}\omega_{uvw}(U_{i,\lambda p})_{ru}
 \bigl[(C_{\lambda p})_{sv}(C_{\lambda p})_{tw}
       -(C_{\lambda p})_{sw}(C_{\lambda p})_{tv}\bigr].           \tag{6}
\]

There are no surviving internal cubic pairs. Each surviving connected
pairing has one path through the quadratic probe and two direct,
undamped cross-covariances between the residual and action stencils.
All colors, both residual chain-rule terms, both insertion subtractions
and the connected subtraction are retained. The outside minus sign
in (1) is included in +3; there is no outside 1/2 from L011's different
two-action summand.

This finite reduction supplies no mesh-uniform bound, a^3-scaled
limit, actual-probe sign, or compensation coefficient. In particular
neither o(a^-3) nor O(a^-3) is established. It does not bound the full
response, any finer power/logarithm, the interacting reflected error
<=c_box/2, or the continuum/infrared construction. No separate forest
invariance is asserted. It is a specialization of finite Taylor and
Gaussian pairing identities, not a claim of a discovery beyond the
sources checked in the approved assessment.

## Proof

### 1. Full-coordinate residual before forest restriction

L149(4)–(6) gives the exact Taylor coefficients of the ordered group
words, endpoint transports and left-frame force. Its force identity is

\[
 D\mathcal S(\Theta)[v]=\sum_e\langle G_e(\Theta),X_e(\Theta)\rangle,
 \qquad \dot U_e=X_e U_e,quad \dot\Theta_e=v_e.                 \tag{7}
\]

Neither G_e nor X_e has a constant coefficient. Its degree-three
part is therefore precisely the first sum in (2). This is the full
action derivative: evaluating on the slice does not delete forest
edges from that derivative.

For the coordinate check, the exact differential of the exponential
is dot U U^-1 = integral_0^1 exp(t Theta) v exp(-t Theta) dt. Its
first two homogeneous orders give the already established L149(8)
identity v_1=X_1 and v_2=X_2-[Theta,X_1]/2. Thus the same degree-three
part of (7) is D s_2 v_2+D s_3 v_1. This verifies the coordinate
correction required by L011(13); X_2 has not been substituted for v_2.

For the triplet, L010 gives j_3=8 sum_p tilde b_p P_p and
P_[3]=-Tr W_3/2. Hence -j_(3,3)=4 sum_p tilde b_p Tr W_3.
For the shear, j_6=-2 sum s Tr(C C), and C_0=0. Its degree-three
coefficient has exactly the two splittings (1,2) and (2,1), with
the plus sign in (2) after subtraction. L011(13) now proves (2).
All these identities hold as finite Taylor identities before restriction;
no nonlinear Gaussian quotient transfer is made.

### 2. The residual's color tensor, including its subtractions

Each local summand in (2) is unchanged by simultaneous SU(2)
conjugation of all its link variables. Indeed, word and clover matrices
conjugate, the transported endpoint clover conjugates as well, and both
Tr and < , > are invariant. Restricting a link variable to zero
preserves this property. The corresponding color action is every
rotation in SO(3).

Here is a finite tensor argument for the consequence at degree three.
Let R_(rc,sd,te) be the symmetric combined edge/color coefficient of
one q_lambda, namely its third derivative divided by 3!. For fixed
edge indices r,s,t, invariance under the rotations by pi about each
color axis forces a possibly nonzero component to contain each of
the three colors once: its three color multiplicities must have the
same parity, and their sum is three. A rotation by pi/2 about the
remaining color axis exchanges any other two colors with one minus
sign. Consequently these components are alternating in the color
indices. Thus R_(rc,sd,te)=k_rst epsilon_cde. Symmetry of R under
exchange of combined slots forces k to be alternating in r,s,t.
It vanishes when two edge indices coincide. Expansion over the six
edge permutations gives k_rst=h_rst/6 and exactly (3).

This argument applies separately to the full force/vector summand and
each insertion subtraction; it does not presume L048's action-specific
zeros for an unexamined residual. For any one-color covariance matrix
D, contraction of two slots of R against D_rs delta_cd is zero because
epsilon_cc e=0. Thus each q_lambda is pure third Gaussian chaos for
the exact color-diagonal forest law, including zero or coincident
selection rows. No claim about smallness of its coefficients is used.

### 3. Complete connected contraction and sign

Import L048(4)–(5)'s ordered action cubic, with its established sign:

\[
 S_3=\sum_p q_{3,p},\qquad
 q_{3,p}=-\tfrac12\sum_{u<v<w}y_{p,u}\cdot(y_{p,v}\times y_{p,w}),
 \quad T_{(uc)(vd)(we)}=-\tfrac1{12}\omega_{uvw}\epsilon_{cde}.    \tag{8}
\]

Use the standard Isserlis Gaussian pairing theorem as in L048,
and L011's finite partition definition of cumulants. No exponential
moment of a cubic is assumed. The cubics have zero expectation and
their products with f have odd degree, so for fixed lambda,p the
third cumulant is exactly E[f q_lambda q_(3,p)]-E[f]E[q_lambda q_(3,p)].

Label the vertices F,R,P with degrees 2,3,3. An internal pair at F
disconnects it and is removed by this subtraction. Every internal
pair at R or P vanishes by their respective epsilon tensors. For a
remaining pairing let n_FR,n_FP,n_RP count the three types of edge.
The degree equations give n_FR+n_FP=2, n_FR+n_RP=3 and
n_FP+n_RP=3. Hence n_FR=n_FP=1 and n_RP=2. There are 2 choices
for the F leg attached to R, 3 for its R endpoint, 3 for the P
endpoint of the other F leg, and 2 ways to pair the remaining R,P
legs: 36 labeled pairings. These exhaust the surviving graphs.
Coincident physical selections do not identify the labeled vertices.

Symmetry of the combined tensors and of B_(i,F) makes these 36
contractions equal after summing indices. The probe path is exactly
U_(i,lambda p) in (4), and the other two are C_(lambda p). Their
color factor is sum_(c,d,e) epsilon_cde^2=6. The residual tensor
normalization is 1/6 and the action tensor normalization is -1/12.
Finally (1) contributes its outside minus sign. The coefficient is

\[
 (-1)\,36\,6\,(1/6)(-1/12)=3.
\]

This proves (5), with every action plaquette included. Interchange
v and w in the second term of (6). Omega changes sign while the
scalar entries commute, giving twice the product in (5); this proves
(6). In particular antisymmetry is a minor contraction, not a reason
to delete two arbitrary undamped lines.

### 4. Exact checks and their limits

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_cubic_residual_action.py`.
The full certificate is
`scripts/combined-ward-response/cubic-residual-action-certificate.json`.
All 14 checks pass with no failures. Enumeration of all 105 eight-leg
pairings gives 90 connected pairings, 54 with an internal cubic pair,
and 36 survivors. Twelve rational comparisons independently expand
the signed normalized cumulant and (5), each with exactly zero error.
They use two positive covariance matrices (one nondiagonal), two
symmetric probe matrices (one indefinite), and three pairs of stencil
maps, including signed, zero and repeated rows and coincident maps.
The residual coefficients are unequal signed rational numbers, rather
than a second copy of the action tensor.

A separate sign control uses three independent standard color
vectors, q=det(y_1,y_2,y_3), action=-q/2, and the sum of squares as
probe. It gives -kappa(f,q,-q/2)=18, both by exact moments and (5).
This is a synthetic algebraic control, not either actual L010 probe
and not a signed lower bound in the pinned box. The checks verify
the pairing implementation and normalizations; the actual local-jet
identification rests on sections 1–2, not on those finite examples.

No replacement of Sigma_F, boundary truncation, prefix approximation,
or restriction of the exterior heat spectrum occurs in (4)–(6).
L026's growing raw forest covariance is therefore retained, including
the upper pinned condition in its exact matrix. Estimating the complete
signed sum at cubic scale requires additional work; the finite pairing
identity alone provides no cutoff decay. Other jets can still change
the full coefficient in L011(6).

## Mathlib

Full matching theorem: **not checked**. Supporting Gaussian moments,
finite cumulants, SU(2) Taylor words and invariant tensors: **not checked**.
Unknown coverage is not asserted absence. The reused
[target assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md)
records the inspected primary Ward/flow/power-counting results and
their scope limitations. The standard input here is the named Isserlis
Gaussian pairing theorem, with its connected specialization explicitly
proved above; no uninspected continuum theorem is imported.
