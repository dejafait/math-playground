# L095 — Cubic control of the H diagonal's axial transport

## Hypotheses

Use L091's finite SU(2) forest Gaussian, actual L010 probes i=3,6,
L018 residual, straight lower-rooted direction-1 forest, relative
all-face pinned box, sufficiently fine admitted even N, a=8/N and
tau=1/16. The bare small-coupling coefficient is taken at fixed mesh
before refinement. All coordinates, transposes and norms are ordinary
dimensionless stored ones. Keep every interior axial level, transverse
end row, ordered plaquette pair including coincidences and heat mode.

Import L085/L091's covariance blocks K_g=M tensor P, M_st=min(s,t),
and K_h=R Qcal, with R=(L_D tensor I+I tensor Delta_T)^(-1),
Pcal=I tensor P and Qcal=I-Pcal. Import the actual alternating
matrices Omega_k and symmetric real heat coefficients c_(i;kl)
from L088. Write

    A_k=Pcal Omega_k Qcal,
    R_H=sum_(k,l)c_(i;kl) Tr(J_k H J_l^T)
       =sum_(k,l)c_(i;kl) Tr(K_g A_k V_h A_l^T).       (1)

The second equality follows from L091's definitions of J_k,H;
square roots cancel only on their positive subspaces. A_k here is
the gh alternating block, not L091's gg block or a residual matrix.

Use L090(4)'s exact generator insertion and L089's curvature split:

    V_h=(Qcal G0 K_h+K_h G0^T Qcal)/2-V_curv,
    G0=I_T^T K_a I_T.                                  (2)

Split G0=G_ax+G_tr by selecting respectively the rho=1 and
rho=2,3,4 displacement terms of the actual generator L009(3).
This is a linear split of the already contracted insertion (2);
no separate nonlinear invariance is asserted.

## Conclusion

Define R_H,ax and R_H,tr by inserting, respectively,
(Qcal G_ax K_h+K_h G_ax^T Qcal)/2 and its G_tr counterpart
in (1), with the complete symmetric exterior sum. Let R_H,Q be
the trace (1) with V_curv. Then exactly

    R_H=R_H,ax+R_H,tr-R_H,Q,
    |R_H,ax|<=C_i N^3,       |R_H,Q|<=C_i N^3.          (3)

The axial transport bound keeps the full min(s,t) covariance and
both generator orientations. It is an actual finite-box bound, not
a frozen or low-frequency test. Neither bounded term is shown to
have a scaled limit or to vanish. R_H,tr retains the previous
O(N^4) upper bound only; no signed growth is established.

Thus the H diagonal still lacks a complete cubic bound. The reverse
crossed orientation R_R in L093 and the scaled limits of the other
bounded sectors remain unresolved. The joint remainder must have
limit -4 gamma D_i before the outside factor 3 to compensate L084;
(3) proves neither existence nor that value. All independent response
jets, finer powers/logarithm, matching, interacting error <=c_box/2,
continuum axioms, reflection positivity, infrared control and finite
positive mass remain open. There is no candidate solution.

## Proof

### 1. Retain the exact axial generator filters

Set n=N-1. On axial interior vertices let

    (T_1 x)_s=(x_(s+1)-x_(s-1))/2,  x_0=x_N=0.

This is L093's C_1 D_v with the actual pinned endpoints. For each
transverse component nu, let C_nu average a nu-edge onto its vertex
endpoints, using the relative transverse domains. These contractions
are those in L093(8). Define the level-diagonal transverse operator

    U_s=diag_(nu=2,3,4)
                  [C_nu^T M_(u_(a,1)(s,.)) C_nu].       (4)

For a transverse input with component 1 zero, its (1,nu) curvature
is D_v y_nu/a. Clover averaging maps it to C_nu C_1 D_v y_nu/a
on vertices, multiplication uses u_(a,1), and the output endpoint
average is C_nu^T. Operators C_nu and C_1 D_v act in different
coordinates. Consequently L009(3) gives exactly

    G_ax=a^(-1) U T_1.                                  (5)

No variable multiplier has been commuted with T_1 or a transverse
operator. The opposite sign in L093(8) concerned output component 1
and curvature (mu,1); here the curvature is (1,nu). Compact support
of u_a makes all nonzero stencils interior. The same incidence and
averaging maps retain every pinned transverse end row.

Smoothness and compact support of the specified u_a give

    ||U_s||<=C,  ||U_(s+1)-U_s||<=C a,                 (6)

and U_s=0 in fixed physical collars of both axial endpoints for all
sufficiently fine meshes. In particular U_1=U_n=0 then. Define
U_0=U_N=0 when using endpoint differences.

### 2. Control level differences of the actual alternating maps

Omega_k acts separately on each axial level: its paths and circulation
are transverse. Identify these identical transverse spaces and write
A_k(s)=P Omega_k(s) Q, Q=I-P. L088(3),(5) and L090(6) imply,
after enlarging the fixed mode polynomial p,

    ||A_k(s)||<=C a p(k),
    ||A_k(s+1)-A_k(s)||<=C a^2 p(k),
    sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i.                  (7)

For the second bound the four path/curvature terms use the axial
O(a^2 p(k)) differences of b_k,q_k in L090(6). Each of the two
exterior-circulation terms has norm O(a^2 p(k)) at either level,
so the triangle inequality alone bounds their difference at the
same order; no stronger difference estimate for f_k is needed.
All fixed selectors have bounded row and column multiplicity.
P,Q are fixed contractions, independent of axial level. Therefore
(7) requires no projection commutator or covariance approximation.
It includes the complete actual Omega, including its exterior
circulation and the transverse pinned rows.

Let W_k(t)=A_k(t)U_t for 1<=t<=n and W_k(0)=W_k(N)=0. Equations
(6),(7), with compact support at the endpoints, give

    ||W_k(t)||<=C a p(k),
    ||W_k(t+1)-W_k(t)||<=C a^2 p(k)                   (8)

for every t=0,...,n. No smooth extension across the upper forest
potential jump is used: this product is zero near that endpoint.

### 3. Sum the centered derivative against the full prefix weight

Transposition of the real scalar first-orientation trace in (1),(2)
gives the second orientation with k,l exchanged. Since the complete
heat coefficients are symmetric, both orientations have equal sums.
They add; the factor 1/2 in (2) is then used exactly once. Thus

    R_H,ax=a^(-1) sum_(k,l)c_(i;kl)
                  Tr(K_h A_l^T K_g A_k U T_1).         (9)

Here A_k Qcal=A_k and Qcal A_l^T=A_l^T justify the removed
adjacent projections. Neither orientation is asserted to vanish.

Put B_kl=A_l^T K_g A_k U. Its exact axial block is

    (B_kl)_st=min(s,t) A_l(s)^T P W_k(t).              (10)

Extend these blocks by zero at t=0,N, consistently with W_k there.
For each fixed s, |min(s,t+1)-min(s,t)|<=1 and min(s,t)<=N.
Using (7),(8) before taking any trace therefore yields

    ||(B_kl)_(s,t+1)-(B_kl)_st||
       <=C p(k)p(l) [a^2+N a^3]
       <=C' p(k)p(l) a^2.                             (11)

The endpoint estimates are valid because the relevant W_k products
vanish in their collars. In particular there is no uncanceled
min(s,N) upper-row jump. Right multiplication by the exact T_1 gives

    (B_kl T_1)_st=[(B_kl)_(s,t-1)-(B_kl)_(s,t+1)]/2,
    ||(B_kl T_1)_st||<=C p(k)p(l) a^2.                (12)

This is a block estimate with the entire transverse operator order
unchanged. It differentiates the full prefix kernel and the actual
level-dependent coefficients. Bounding T_1 and K_g separately would
lose this gain.

### 4. Bound the complete positive axial resolvent blocks

For lambda>0 let R_lambda=(L_D+lambda I)^(-1). Every entry is
nonnegative. One elementary verification is the discrete minimum
principle: if (L_D+lambda I)x has nonnegative entries and x has a
negative minimum, that row has negative image, using zero values at
the two pinned endpoints, a contradiction. Applying this to each
unit right-hand side proves entrywise nonnegativity of the inverse.
Moreover L_D 1>=0, so the same order preservation gives

    R_lambda 1<=lambda^(-1)1,
    sum_(s,t=1)^n (R_lambda)_st<=n/lambda.              (13)

Since Delta_T commutes with Q, each block
(K_h)_st=R_st(Delta_T)Q is positive semidefinite on the transverse
space: on a co-closed eigenvector its eigenvalue is the nonnegative
scalar (R_lambda)_st, and on gradients it is zero. This assertion
concerns each transverse block, not entrywise signs of P or Q.
Consequently its trace norm is its trace, and (13) implies

    sum_(s,t) ||(K_h)_st||_1
       <=n Tr_(ker P)(Delta_T^-1)<=C N^4.              (14)

For the final inequality use L086's exact relative tensor spectrum
with the axial factor omitted. For transverse component nu its own
index is in 0,...,N-1 and its other two indices in 1,...,N-1.
There is no zero mode, lambda>=4|m|^2/N^2, and the shell
max_j m_j=r contains at most C r^2 labels including all components.
Thus Tr Delta_T^-1<=C N^2 sum_(r=1)^(N-1) r^2/r^2<=C' N^3.
Restriction to ker P only decreases this positive trace. All modes
and all axial entries in (13)–(14) are included.

The trace of K_h B_kl T_1 is the sum of the transverse traces of
(K_h)_ts (B_kl T_1)_st. The finite trace-ideal inequality, (12)
and (14) give

    |Tr(K_h B_kl T_1)|<=C p(k)p(l) a^2 N^4.

Insert this in (9) and use the complete heat bound (7). It gives
|R_H,ax|<=C_i a N^4<=C'_i N^3, proving its part of (3).
Only cyclicity, exact axial differences and positive resolvent blocks
were used. No transverse multiplier was moved through P,Q or R.

### 5. Bound the curvature subtraction and state the remaining gap

L089(11)'s actual curvature insertion has whitened norm at most C.
The same row-map form inequality gives
V_curv=K_h^(1/2) H_Q K_h^(1/2), ||H_Q||<=C. L091(12) supplies
||J_k||_HS<=C p(k) N^(3/2), hence

    |Tr(J_k H_Q J_l^T)|<=C p(k)p(l) N^3.

The complete heat sum proves the curvature bound in (3). This bound
is at cubic scale, so this subtraction cannot be discarded when
seeking the limit. For R_H,tr, subtracting the two bounds in (3) from L091's
existing O(N^4) bound for the full R_H still gives only O(N^4). The axial argument
cannot be applied to transverse derivatives of P or its levelwise
kernel; such a gain requires a separate signed estimate.

This is a bounded RESEARCH / REPRODUCTION specialization under the
unchanged EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The finite contractions and generator insertion are imported. The
extra proof verifies the actual axial block order, endpoint terms and
resolvent sum needed for this different trace. It is local progress
using the recorded finite spectral and summation methods, not a claim
of mathematical novelty beyond the sources checked. No numerical
certificate or numerical value of D_i is used. Any later numerical
comparison retains L082's saved-table/IEEE qualifications via L084.

## Mathlib

Full matching finite-trace result: **not checked**. Supporting discrete
minimum principle, tensor spectrum, trace-ideal inequality and finite
summation coverage: **not checked**. Unknown availability is not
absence. No continuum flow or Ward theorem is used to assign this
isolated group's cutoff coefficient.
