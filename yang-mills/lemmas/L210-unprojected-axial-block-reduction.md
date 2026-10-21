# L210 — Subcubic axial diagonal and the remaining single-prefix trace

## Hypotheses

Use L209's complete setting: SU(2), relative box (-4,4)^4, admitted
even N, a=8/N, straight lower-rooted direction-1 forest, full compact
displacement, both actual L010 probes i=3,6 at tau=1/16, and the
fixed-mesh bare expansion before refinement. Use ordinary stored-link
coordinates and transposes. All boundary vertex values are pinned;
all variable normal end edges, allowed constant modes, both residual
subtractions and the full external heat expansion are retained.

In L209's notation set Sigma=Delta^(-1), S=P Sigma, A=PAP=A^T,
Z=p(Delta+epsilon I) with precisely L205's mass/degree schedule,
V=q Phi, H=I-D Phi/2, R=I-D Phi. For each heat pair put

    n=S e_k, y=P e_l, alpha=Vn, nu=Rn,
    Y=diag(alpha)-diag(nu)V,
    Bcal=H^T diag(y)V-V^T diag(y)H, C=Y^T Bcal.       (1)

The letters Bcal and C in this lemma are modal maps, not the probe
matrix B_i. In particular Bcal^T=-Bcal. L209 gives

    Qhat_i=6a^2 sum_(k,l) d_(i;kl) Tr(A Z C Z),
    G_(i,a)=-Qhat_i+o(N^3), Qhat_i=O(N^3),           (2)

where G is the original joint cubic probe-jet group. Its heat weights
obey L209(2)'s polynomial summability.

Split the link space orthogonally into direction-1 links and the three
transverse components. Let I_1,I_T be their coordinate insertions,
A_ab=I_a^T A I_b, Z_a=I_a^T Z I_a, Sigma_a=I_a^T Sigma I_a,
q_a=I_a^T q and Phi_1=Phi I_1. Subscripts on vectors denote the
same component restrictions. Delta, Sigma and Z are componentwise;
P and A are not assumed componentwise. In particular Phi I_T=0.

## Conclusion

The complete transverse block is identically zero:

    C_TT=0.                                         (3)

The whole axial diagonal contribution, with no sign assumption, obeys

    D_(i,N)=6a^2 sum_(k,l)d_(i;kl)
                       Tr(A_11 Z_1 C_11 Z_1),
    |D_(i,N)|<=C_i N^(5/2)=o(N^3).                  (4)

The two mixed blocks combine exactly as

    C_T1+C_1T^T
      =diag(y_T)[diag(alpha_T)q_T Phi_1
                            -q_T Phi_1 diag(alpha_1)]. (5)

Thus define the retained trace

    R_(i,N)=6a^2 sum_(k,l)d_(i;kl) Tr(
       A_1T Z_T diag(y_T)
       [diag(alpha_T)q_T Phi_1-q_T Phi_1 diag(alpha_1)] Z_1).
                                                        (6)

Its sign and normalization are fixed by

    Qhat_i=D_(i,N)+R_(i,N),
    G_(i,a)=-R_(i,N)+o(N^3), R_(i,N)=O(N^3).         (7)

There is no proved limit or coefficient for R_(i,N). Formula (6)
retains the complete mixed residual A_1T; the scalar estimate used
in (4) is not transferred to that block. Only one rough prefix occurs
in (6), while alpha=q Phi n retains the actual external prefix.
Neither the long plateau nor the near-diagonal prefix transition has
been estimated away. In matrix entries, the bracket after multiplication
by diag(y_T) is exactly

    y_e (q_T Phi_1)_(e,h) (alpha_e-alpha_h),          (8)

for transverse edge e and axial edge h. This difference is not
declared small across a long prefix or smooth through an upper pin.

This is local standard-method progress toward the approved joint-group
limit, not a result beyond the checked sources or a compensation claim.
The independent f_(i,2),r_0 contribution, full compensation, finer
asymptotics, finite matching, interacting reflected error <=c_box/2,
continuum axioms and infrared finite positive mass remain unresolved.

## Proof

### 1. Compute the component blocks without moving a projection

All this algebra takes place in L209's already justified Qhat. It
does not remove a projection from any individual original covariance
block. Since Phi=(Phi_1,0), the definitions give

    H=[ Id_1-D_1 Phi_1/2       0
                   -D_T Phi_1/2       Id_T ],
    V=[q_1 Phi_1  0; q_T Phi_1  0],
    Y=[diag(alpha_1)-diag(nu_1)q_1 Phi_1       0
                 -diag(nu_T)q_T Phi_1       diag(alpha_T)]. (9)

Here Id_1,Id_T are component identity maps and D_a=I_a^T D.
Direct multiplication in Bcal yields

    Bcal_TT=0,
    Bcal_T1=diag(y_T)q_T Phi_1,
    Bcal_1T=-Phi_1^T q_T^T diag(y_T).                (10)

Consequently C_TT=0 and

    C_T1=diag(alpha_T)diag(y_T)q_T Phi_1,
    C_1T=[diag(alpha_1)-Phi_1^T q_1^T diag(nu_1)]
                                      [-Phi_1^T q_T^T diag(y_T)]. (11)

The second term in the square bracket must be checked at the upper
pin, rather than bounded as though nu_1 were smooth.

### 2. The upper jump cancels in this mixed block exactly

On an axial fiber label its edges r=0,...,N-1 and its interior
vertices s=1,...,N-1. The actual prefix is

    (Phi_1 w)_s=sum_(r=0)^(s-1) w_r,
    (Phi_1 w)_0=(Phi_1 w)_N=0.

Thus (D_1 Phi_1 w)_r=w_r for 0<=r<=N-2, while its last
entry is -sum_(r=0)^(N-2)w_r. It follows that nu_1=Rn has
zero entries except possibly on the upper axial normal edges, where
its entry is sum_(r=0)^(N-1)n_r. No bound or cancellation of that
sum is assumed. The column of Phi_1 at r=N-1 is exactly zero,
because the prefix has no unpinned vertex above that edge. Hence

    diag(nu_1) Phi_1^T=0.                           (12)

This removes the extra term in C_1T in (11), proving

    C_1T=-diag(alpha_1)Phi_1^T q_T^T diag(y_T).

Transposition and (11) now give (5). Every transverse endpoint in
q_T uses its pinned vertex value; (12) includes the actual upper
normal source edge rather than omitting it. No statement is made
about the axial diagonal's upper contribution by this cancellation.

### 3. The scalar residual energy bound applies to A_11 only

L065(1) and its proof sections 1–4 concern precisely the full residual
A=(L K_a+K_a^T L)/2-Q_3-Q_6 used here, with L the action curl
Laplacian and the same endpoint/clover generator and two insertion
forms. Its A_0 notation denotes this same A, not a residual frozen
at zero axial frequency. Its scalar quadratic-form conclusion holds
for every axial component field, with all axial frequencies retained:

    |f^T A_11 f|<=C f^T H_T f,
    H_T=I_N tensor Delta_T.                          (13)

The companion zero-mode assertion in L065 is not needed. To apply
(13), note that the axial relative Hodge block is

    Sigma_1=(L_edge tensor I+H_T)^(-1).

L_edge is nonnegative and commutes with H_T, so
Sigma_1^(1/2) H_T Sigma_1^(1/2)<=I. Substitute
f=Sigma_1^(1/2)v into (13), then use the finite-dimensional spectral
theorem for its symmetric form. This proves

    ||E_11||<=C, E_11=Sigma_1^(1/2)A_11 Sigma_1^(1/2). (14)

In particular the generic O(N) full residual estimate is unnecessary
in this diagonal block. Formula (13) includes all cross-component
generator outputs before the scalar pairing and both subtractions;
no term of A_11 has been omitted. It supplies no bound of this strength
for A_1T or the full A.

### 4. Unprojected covariance counts with every normal end row

We need the analogues of L187's positive trace counts for Sigma,
not an unjustified deletion of P in a norm bound. Let

    Ktilde=Phi Sigma Phi^T, U_st=min(s,t),
    G_T=Delta_T^(-1), 1<=s,t<=N-1.

Since Sigma_1<=I_N tensor G_T and the actual prefix satisfies
Phi_1 Phi_1^T=U tensor I, positive sandwiching gives

    0<=Ktilde<=U tensor G_T.                         (15)

The product spectrum gives Tr G_T=O(N^3): a three-dimensional
shell max k_j=r has O(r^2) modes and inverse eigenvalues at most
N^2/(4r^2). The analogous four-dimensional count, including all
allowed constant own-direction modes, gives Tr Sigma=O(N^4).
Also Tr U=O(N^2), so Tr Ktilde=O(N^5). For the full vertex
Dirichlet incidence,

    D^T D=L_D tensor I+I tensor Delta_T,
    Tr(U L_D)=2(N-1).

The last equality follows either from its tridiagonal entries or
the squared norms of all axial differences of the prefix, including
the last jump. Taking the positive trace in (15) therefore yields

    Tr(D Ktilde D^T)
      <=2(N-1)Tr G_T+Tr U Tr(Delta_T G_T)=O(N^5).

The endpoint sum q has bounded norm. Consequently

    ||Sigma^(1/2)||_HS<=C N^2,
    ||V Sigma^(1/2)||_HS+||H Sigma^(1/2)||_HS<=C N^(5/2). (16)

If Pi_top selects the upper axial normal edges, their V rows are
the last rows of Phi, giving separately

    ||Pi_top V Sigma^(1/2)||_HS^2
                            <=(N-1)Tr G_T=O(N^4).   (17)

L187(14)–(15) apply to the actual exterior n=S e_k:
alpha is O(p(k)N) everywhere, nu is O(p(k)) off that upper
layer and O(p(k)N) on it. Equations (16)–(17) thus prove

    ||Y Sigma^(1/2)||_HS<=C p(k)N^3.                 (18)

Indeed its three bounds are N*N^2, N^(5/2) and N*N^2,
respectively. This explicitly retains the largest upper-layer term.

The finite prefix has ||Phi||<=N, hence ||H^T||+||V^T||<=C N.
L209(8) gives ||y||_infinity<=C a^2 p(l). Use the original order
in Bcal and (16), obtaining

    ||Bcal Sigma^(1/2)||_HS
      <=||H^T|| ||diag(y)|| ||V Sigma^(1/2)||_HS
          +||V^T|| ||diag(y)|| ||H Sigma^(1/2)||_HS
      <=C p(l)N^(3/2).                              (19)

These are full-domain counts. In particular neither S nor Sigma has
been treated as componentwise equal to the forest covariance.

### 5. The diagonal estimate and the remaining signed order

Let F_1=Delta_1 Z_1. L205's relative polynomial estimate gives
||F_1||<=1+eta uniformly, and F_1 commutes with Sigma_1. Keeping
the two filters on their original sides of the residual,

    Z_1 A_11 Z_1
      =Sigma_1^(1/2) F_1 E_11 F_1 Sigma_1^(1/2).

The modal diagonal trace in (4) is thus Tr(E_11 U_k^T W_l), where

    U_k=Y I_1 Sigma_1^(1/2)F_1,
    W_l=Bcal I_1 Sigma_1^(1/2)F_1.

Because Sigma is componentwise, restricting its columns cannot
increase either Hilbert–Schmidt norm in (18)–(19). Thus (14)
and matrix Cauchy–Schwarz give

    |Tr(E_11 U_k^T W_l)|<=C p(k)p(l)N^(9/2).

Multiply by 6a^2 and sum all heat weights using L209(2). This proves
(4). The cubic-scaled allowance is C_i N^(-1/2), tending to zero.
No positivity of A_11 or E_11 has been used.

Finally expand the full finite trace in (2) into its four component
blocks. The transverse block is zero by (3). Since A_T1=A_1T^T
and both Z blocks are symmetric, transposing the second mixed
trace combines the two as

    Tr(A_1T Z_T [C_T1+C_1T^T] Z_1).

Formula (5) proves (6) and the exact first equality in (7). There
is no additional factor 2: the two orientations have already been
included in their displayed sum. Equations (2) and (4) prove the
remaining claims in (7). In particular the minus sign from the
original joint group is retained. The identity (8) is just the
entrywise formula for the two diagonal multipliers in (5).

The remaining trace is cubic-bounded only by the complete preceding
bound and the subcubic subtraction. Neither its coefficient
difference, its plateau/transition split, nor its mixed residual
has a proved cubic-scale limit here. L207 cannot be applied without
its actual energy and coefficient hypotheses. No fixed-degree limit
is used at the varying degree. All checks in this step are analytic
block multiplication, finite positive trace counts and ordered matrix
inequalities; no numerical fixture or mathematical script is evidence.

## Mathlib

Full matching actual-probe block reduction and cubic limit: **not
checked**. Supporting finite block-matrix algebra, positive sandwich
inequalities and Hilbert–Schmidt trace estimates: **not checked**;
unknown coverage is not absence. The finite-dimensional spectral
theorem and matrix Cauchy–Schwarz are used in their standard forms.
L065 supplies the scalar residual form theorem, and the unprojected
trace counts are justified here because the change from S to Sigma
and the retained upper normal edge matter. No general flow or
renormalization result is reproved. Reuse the unchanged
[approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
within its joint-group scope. No originality claim is made.
