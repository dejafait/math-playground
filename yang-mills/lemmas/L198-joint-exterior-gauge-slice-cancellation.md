# L198 — Joint exterior gauge slices cancel the explicit multiplier

## Hypotheses

Use L194's exact SU(2) setting: relative box (-4,4)^4, admitted even
N, a=8/N, straight lower-rooted direction-1 forest, complete compact
L008 displacement, both actual L010 probes i=3,6 at tau=1/16, and
bare expansion at fixed mesh before refinement. Use ordinary full
variable-link coordinates and retain every normal end edge, physical
face, constant own-direction mode and heat mode. Vertex potentials
are pinned on every boundary vertex.

Use L183's L=D_1^T D_1, orthogonal co-closed projection P, covariance
S=PSP with LS=SL=P, and signed residual A=PAP, including both
insertion subtractions. Keep L194's full alternating spatial tensors
r,s of the residual and action cubics, with quadratic matrices A and
L/2 respectively. For a deterministic link vector v their slices are
(r_v)_bc=sum_a v_a r_abc, and likewise s_v. These full tensors are
formed before forest restriction; v need not be co-closed.

Set T=2SA, M=2SAS, V=q Phi, R=I-D Phi, and let J_y=P Gamma_y P
be L194's skew matrix. For each rank-one input SB=n y^T define

    phi=Phi n, alpha=Vn, beta=Rn, m=Tn,
    D_alpha=diag(alpha), D_beta=diag(beta).

The letter D without a subscript remains the vertex incidence.
Use the complete actual-probe expansion from L194(10),

    SB_i=a^2 sum_(k,l) d_(i;kl) n_k e_l^T, n_k=S e_k,
    sum_(k,l)|d_(i;kl)|p(k)p(l)<=C_(i,p)                 (1)

for every fixed polynomial p. Let Pi select the upper direction-1
normal links only, and put beta_k^t=Pi Rn_k and
beta_k^b=(I-Pi)Rn_k. These selectors act only on deterministic
exterior vectors, never on covariance inputs or across P.

## Conclusion

L194(5)'s whole rank-one joint trace has the exact identity

    Z(n,y)=-6 Tr(J_y S(r_beta-s_m)S)
             +12 Tr(J_y M s_beta S)
             -6 Tr(J_y M V^T D_beta).                  (2)

The explicit multiplier D_alpha has canceled between the residual
gradient slice, both rough action placements and the quartic. This
is an exact all-face gauge identity, not a small covariance commutator.
The retracted exterior beta retains its O(N) upper jump.

Define the following two full exterior sums:

    B_(i,N)=a^2 sum_(k,l)d_(i;kl)
       {-6 Tr(J_(e_l) S r_(beta_k^b) S)
          +12 Tr(J_(e_l) M s_(beta_k^b) S)},
    H_(i,N)=12a^2 sum_(k,l)d_(i;kl)
                         Tr(J_(e_l) M s_(beta_k^t) S). (3)

For sufficiently fine admitted meshes the original joint group is

    G_(i,a)=B_(i,N)+H_(i,N)-Q_(tr,i,N)+E_(i,N),
    |B_(i,N)|<=C_i N^3 sqrt(log(eN)),
    |Q_(tr,i,N)|<=C_i N^3,  a^3 E_(i,N)->0.            (4)

Here Q_tr is exactly L196(2), with its positive sign there, and is
subtracted once in (4). Thus only the upper-exterior action trace H
remains outside the displayed O(N^3 sqrt(log(eN))) control. Its
inherited bound is still only O(N^(7/2)). H is not an upper-output
partition of Q_3, so L196's subcubic upper-output estimate cannot be
assigned to it.

No improved complete-group power bound, cubic boundedness, finite
scaled limit, sign or coefficient is established. In particular the
bulk logarithmic allowance and the transport coefficient remain.
This finite cancellation and localization of the excess power are
local progress by specialization of existing gauge identities, not
progress beyond the checked sources. Independent f_(i,2),r_0, full
compensation, finer asymptotics, finite matching, interacting reflected
error <=c_box/2, continuum axioms and infrared finite positive mass
remain unresolved.

## Proof

### 1. Check the full gradient-slice sign

Import L156(4), the degree-two gauge-jet identity for a full invariant
cubic C with quadratic matrix K=PKP:

    dC(z)[D eta]=-<Kz,[z,q eta]>.

The bracket is minus the color cross product. It applies to the
complete residual with K=A and the full action with K=L/2, including
all boundary plaquettes and both residual subtractions. Take eta to
have only color 1 with spatial vector phi, and take z to have colors
2 and 3 with arbitrary spatial vectors x,w. Then

    [z,q eta]^2=-D_alpha w,
    [z,q eta]^3= D_alpha x.

The right side of the gauge identity is therefore

    (Kx)^T D_alpha w-(Kw)^T D_alpha x
       =x^T(K D_alpha-D_alpha K)w.

In L194(2)'s alternating convention the left side is precisely
x^T c_(D phi) w. There is no extra factor of 3: the color-ordered
polynomial is sum_abc c_abc z_a^1 z_b^2 z_c^3. Since x,w are
arbitrary, the full matrix identities are

    r_(D phi)=[A,D_alpha],
    s_(D phi)=[L,D_alpha]/2.                            (5)

No projection of the two rough arguments was used to establish (5).
The potential phi is pinned, so the gauge identity includes the
upper normal rows even though its normal derivative jumps there.

### 2. Cancel in the original trace order

Write n=beta+D phi. L187's full pinned product identity gives

    U_n^T P=(D_alpha-V^T D_beta)P.                     (6)

Inside the trace with J_y=P J_y P and M=PMP, equations (5),(6)
give

    2s_n S+U_n^T P
      =2s_beta S+L D_alpha S-D_alpha P
                            +D_alpha P-V^T D_beta P
      =2s_beta S+L D_alpha S-V^T D_beta P.             (7)

L194(5) may use (7), since a terminal P can be inserted by cyclicity
against J_y. Its residual is r_n=r_beta+[A,D_alpha]. Also

    M L=2SASL=2SA,
    Tr(J_y S D_alpha A S)=-Tr(J_y S A D_alpha S).       (8)

The second identity follows by taking a transpose, using J_y skew
and S,A,D_alpha symmetric, then cycling the finite trace. Thus the
terms involving D_alpha in L194(5) sum to

    -6 Tr(J_y S[A,D_alpha]S)
         +6 Tr(J_y M L D_alpha S)
      =-12 Tr(J_y S A D_alpha S)
         +12 Tr(J_y S A D_alpha S)=0.

The remaining terms are exactly (2). This computation retains both
rough action placements, whose equality by transpose supplied the
factor 12 in L194. Keeping only one would fail to cancel. Neither A
nor S has been commuted through a variable multiplier, and the false
identity PH^T=P is never used.

### 3. Isolate the deterministic upper exterior and the exact error

By L155's full local residual formula and compact displacement and
insertion supports, every link in every nonzero residual stencil is
separated from the physical boundary for all sufficiently fine meshes.
The radius is a fixed number of lattice steps. Therefore

    r_(beta_k^t)=0,   r_(beta_k)=r_(beta_k^b).           (9)

This is a tensor support statement, not a covariance localization.
The action has no such support property and keeps
s_(beta_k)=s_(beta_k^b)+s_(beta_k^t), including all action faces.

L196 proof section 3 identifies its transport sum exactly as
6a^2 sum_kl d_(i;kl) Tr(J_(e_l) M V^T diag(beta_k)). Hence the last
term of (2) sums to -Q_tr, with its entire pinned jump retained.
L194(4) subtracts Q_1+Q_2. L183 and L193 identify the remaining
co-closed response G^H_(i,N)=E[F_(i,3)(z)rho_F(z)] and prove
G^H_(i,N)=o(N^3). Consequently the error in (4) is exactly

    E_(i,N)=G^H_(i,N)-Q_1-Q_2
       +6a^2 sum_(k,l)d_(i;kl) Tr(J_(e_l) S s_(Tn_k) S). (10)

L194 proves Q_1+Q_2=O(N^(5/2)) from L185–L186, and bounds the
last term by O(sqrt(log(eN))). Its smooth-tilt direction is Tn_k,
not an assumed smooth rough Tz. These facts prove a^3 E_(i,N)->0.

### 4. Bound the entire remaining bulk-exterior sum

L187(15) gives ||beta_k^b||_infinity<=C p(k) on every link. This
vector can jump at the selected layer; no derivative estimate for
it is needed here. L194(8)'s local quadratic estimate applies to
any deterministic direction of bounded amplitude, with every action
face retained. For one fixed color c it gives

    ||d script R_3[ (beta_k^b)^(c) ]||_2
        <=C p(k) N^3 sqrt(log(eN)),
    ||d script S_3[ (beta_k^b)^(c) ]||_2
        <=C p(k) N^2 sqrt(log(eN)).                    (11)

For the rough tilt acting on both remaining action slots, L194(13)'s
whitened tensor argument depends only on the quadratic coefficient
tensor and ||2S^(1/2)AS^(1/2)||<=CN. It therefore also gives

    ||d^2 script S_3[(beta_k^b)^(c),Tz]||_2
        <=C p(k) N^3 sqrt(log(eN)).                    (12)

The direction beta_k^b is deterministic and held fixed in (12).
There is no derivative of beta_k^b or extra T beta_k^b term in the
two rough-slot placements being estimated.

L194(9),(11) give ||<e_l,b^c>||_2<=C N^2 (a polynomial in l
could equally be absorbed in (1)). Its exact two-color contraction
(15),(16) identifies the expression in braces in (3) with

    2 sum_(c=1)^3 E[<e_l,b^c>
       {d script R_3[(beta_k^b)^(c)]
             -d^2 script S_3[(beta_k^b)^(c),Tz]}].      (13)

This is the same finite Isserlis identity for any deterministic
exterior direction; beta_k^b need not be a covariance column.
Cauchy–Schwarz, (11),(12) bound (13) by
C p(k) N^5 sqrt(log(eN)). Multiplying by a^2=64/N^2 and summing
the complete coefficients (1) proves the bulk bound in (4).
L196 supplies its transport bound. Finally L194's complete
O(N^(7/2)) bound and (4) imply H=O(N^(7/2)); no improvement is
inferred by subtracting these upper bounds.

### 5. Verification and stopping qualification

The checks are analytic: the two explicit color components fix the
sign in (5); expanding (7),(8) checks every multiplier term and its
factor; (9) uses compact support only for the residual; (10) retains
the smooth-tilt and all removed placements with their signs. No
numerical fixture or mathematical script is used as evidence.

L197's nonzero covariance-commutator matrix element is unaffected.
It forbids a factorwise shortcut, whereas (5)–(8) combine actual
residual and action tensors before estimates. This does not prove
that H is nonzero, that the bulk logarithm occurs, or that either
probe diverges. L196's upper-output partition selects a different
index from the deterministic action exterior in H. The remaining
test must estimate H in its actual trace order and remove the bulk
logarithmic allowance or control the full signed sum; even cubic
boundedness would still leave convergence unproved.

## Mathlib

Full matching joint cancellation, upper-exterior decomposition and
scaled limit: **not checked**. Supporting finite trace, Gaussian
pairing and gauge-jet coverage: **not checked**; unknown coverage is
not an absence claim. L156(4)'s already established full gauge-jet
identity and L194's finite Isserlis contractions are imported, with
only their new actual-slice specialization and signs proved here.
No general gauge or flow-renormalization theorem is reproved. Reuse
the unchanged [approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md);
its scope covers this finite reduction of the same joint group.
