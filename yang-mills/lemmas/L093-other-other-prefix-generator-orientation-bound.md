# L093 — A cubic bound for one crossed generator orientation

## Hypotheses

Keep L091–L092's finite SU(2) forest Gaussian, actual L010 probes
i=3,6 and L018 residual, straight lower-rooted direction-1 forest,
relative all-face pinned box, sufficiently fine admitted even N,
a=8/N and tau=1/16. Take the bare small-coupling coefficient at
fixed mesh before refinement. Coordinates, transposes and norms
are ordinary stored-coordinate ones. Retain all interior levels,
transverse end rows, ordered plaquette pairs including coincidences,
both generator orientations and the complete exterior heat sum.

Use L092's spaces and maps I_T,I_1,Tcal,G_v,B,B0,C,H_g, and
L091's Pcal,Qcal,K_g,K_h,J_k,F,D_k. In particular

    C=Tcal G_v B,
    H_g=Pcal I_T^T+Tcal B I_1^T,
    Pcal V Qcal=C (I_1^T A_0 I_T) K_h.

Import L088's actual skew matrices Omega_k and symmetric real heat
coefficients c_(i;kl). Put

    Omega_(gh,k)=Pcal Omega_k Qcal,
    Omega_(hh,k)=Qcal Omega_k Qcal,
    G0=I_T^T K_a I_T,  G_T1=I_T^T K_a I_1,
    A_0=(L K_a+K_a^T L)/2-Q_0,  L=D_1^T D_1.

Here Q_0 is the sum of the actual triplet and shear curvature forms,
not the projection Qcal. K_a has L009's exact endpoint/clover filters
and compact displacement u_a. Its coefficients and first physical
differences are uniformly bounded, and vanish near the fixed faces.

## Conclusion

The full gradient row applied to the transverse generator obeys

    ||H_g K_a I_T|| <= C/a.                              (1)

This gains one prefix power over estimating B and K_a separately.
It is not a uniform whitened full-vector residual bound.

The co-closed-base crossed pair in L091(4) has the exact split

    R_hx=2 sum_(k,l)c_(i;kl) Tr(J_k^T F D_l)
        =R_L+R_R-R_Q,                                    (2)

where

    R_L=sum_(k,l)c_(i;kl)
      Tr(K_h Omega_(gh,k)^T H_g K_a I_T K_h Omega_(hh,l)),
    R_R=sum_(k,l)c_(i;kl)
      Tr(K_h Omega_(gh,k)^T C G_T1^T Qcal Omega_(hh,l)),
    R_Q=2 sum_(k,l)c_(i;kl) Tr(J_k^T F_Q D_l).             (3)

Here F_Q is the whitened gh block of the covariance insertion of
Q_0, with the same forest row maps as F. Uniformly,

    |R_L|<=C_i N^3,       |R_Q|<=C_i N^(5/2).             (4)

Thus the curvature subtraction is subleading at a^3 scale, and the
first actual generator orientation has bounded a^3-scaled values.
No scaled limit or sign for R_L is asserted. R_R is retained exactly;
no improvement of the prior O(N^(7/2)) bound for the complete R_hx
follows. The H diagonal crossed trace in L091(4) still lacks cubic
control. The two residual orientations in (2) have not been canceled
by transpose, and neither is identified with a scalar residual block.

The complete other/other limit and comparison with -12 gamma D_i
remain open. Other response jets, N^2 remainders, slower powers and
logarithm, matching, interacting error <=c_box/2, continuum axioms,
reflection positivity, infrared control and finite positive mass are
independent gaps. No Yang–Mills candidate is asserted.

## Proof

### 1. An exact axial prefix identity with its lower-end row retained

Work first on the axial interval. Let n=N-1, let x=(x_1,...,x_n)
have pinned values x_0=x_N=0, and let C_1 map the N axial edge
entries to averages at the n interior vertices. Write D_v=-B0^T
for the forward pinned vertex-to-edge difference. Then

    (T_1 x)_j:=(C_1 D_v x)_j=(x_(j+1)-x_(j-1))/2,
    S:=B C_1^T,   S_sj=1_(j<s)+delta_(s,j)/2.

Summing the centered differences, including s=1 and s=n, gives

    S T_1=H_av-(1/2) 1 e_1^T,
    (H_av x)_s=(x_(s-1)+2x_s+x_(s+1))/4.                (5)

Indeed the sum up to s-1 is
(x_s+x_(s-1)-x_1-x_0)/2 and the half-weighted last term is
(x_(s+1)-x_(s-1))/4. Combining them proves (5). The same
calculation for s=1 uses an empty first sum. For s=n it uses the
actual pinned upper value x_N=0; no upper edge is removed.
H_av=(2I+S_++S_-)/4 on pinned vertices has norm at most one.

Let U=M_u be multiplication by any real axial coefficient profile
with u_1=0 and |u_(j+1)-u_j|<=a L_u on neighboring interior
vertices. Compact support of the actual displacement implies u_1=0
for all sufficiently fine meshes. The exact commutator identity is

    S U T_1=H_av U+S[U,T_1].                            (6)

To verify it, use U T_1=T_1 U+[U,T_1] and (5); the retained
rank-one term is -(1/2) 1 e_1^T U=0. Without u_1=0 that term
would remain. The two nonzero off-diagonals of [U,T_1] are signed
adjacent differences of u divided by 2, so its maximum absolute
row sum and column sum are at most a L_u. The finite Schur bound
therefore gives ||[U,T_1]||<=a L_u. Also ||B||<=||B||_HS<=N
and ||C_1||<=1. Hence

    ||B C_1^T M_u T_1||
       <=||u||_infinity+Na L_u
       =||u||_infinity+8L_u.                            (7)

This is an operator bound on arbitrary rough inputs, not a
smooth-input consistency estimate. Tensor (5)–(7) over the pinned
transverse vertices. A coefficient can depend on all transverse
coordinates: the axial identity acts separately on each such column,
and the uniform coefficient and axial-difference bounds give the
same operator bound on their direct sum.

### 2. Apply the identity to the actual filtered generator

For a transverse input x=I_T y, L009(3) gives exactly

    I_1^T K_a I_T y
       =-a^(-1) C_1^T sum_(mu=2)^4
                         M_(u_(a,mu)) T_1 C_mu y_mu.     (8)

Here C_mu averages a transverse mu-edge onto its two vertex
endpoints and is a contraction on the relative interval. The
(mu,1) curvature of this input is -D_v y_mu/a. Its four-plaquette
clover average is -C_mu C_1 D_v y_mu/a, and the output endpoint
average is C_1^T. These are precisely the two axial filters in (8).
C_mu commutes with T_1 because they act in different coordinates;
it is not commuted through the variable coefficient. All nonzero
coefficient stencils are interior. On pinned transverse end rows,
the same incidence/average maps apply, with the fixed entries zero.
Thus (8) retains both endpoints and every actual clover factor.

Apply (7) to each term of (8) after the contraction C_mu. Uniform
smoothness of u_a gives

    ||B I_1^T K_a I_T||<=C/a.                            (9)

L090(2)'s bounded-multiplicity estimate gives ||G0||<=C/a.
Since ||Pcal||=1 and the dimensionless incidence Tcal has a uniform
operator norm, the exact row identity

    H_g K_a I_T=Pcal G0+Tcal B I_1^T K_a I_T

and (9) prove (1). In particular the transverse output of K_a is
retained alongside its component-1 output. This argument uses a
pinned summation of the latter's derivative, not the stopped uniform
full-vector residual extension or an axial bulk-profile replacement.

### 3. Split the crossed residual without dropping an orientation

L092's tensor incidence convention is

    mathscr D=I_T Tcal+I_1 B0^T,
    Delta=Sigma^(-1),   L=Delta-mathscr D mathscr D^T.

The component-1 block of Delta is L_E+H_T, where
L_E=B0^T B0 and H_T=I_N tensor Delta_0. Direct multiplication
therefore gives

    I_1^T L=H_T I_1^T-B0^T Tcal^T I_T^T.

Use L092's B B0^T=-I, G_v Delta_0=I, and
Tcal G_v Tcal^T=Pcal. Since axial and transverse constant
operators commute, but no coefficient is moved, this proves

    C I_1^T L=Tcal B I_1^T+Pcal I_T^T=H_g.              (10)

Also L I_T K_h=I_T Qcal. For verification I_T Qcal is fully
divergence-free, and the full Hodge Laplacian restricts to Delta_E
on I_T; hence L I_T K_h=Delta I_T K_h=I_T Qcal. This is
L090(3)'s co-closed row identity with all pinned rows retained.

Let A_gen=(L K_a+K_a^T L)/2. Both A_gen and Q_0 annihilate
full gauge gradients: L does so, L009 proves K_a mathscr D=0,
and Q_0 consists of curvature forms. Thus L092's covariance-row
identity applies to these two insertions separately. Define their
crossed blocks by V_gh^gen=C I_1^T A_gen I_T K_h and
V_gh^Q=C I_1^T Q_0 I_T K_h, so V_gh=V_gh^gen-V_gh^Q.
Equations (10) and the co-closed identity give the exact formula

    V_gh^gen=(H_g K_a I_T K_h+C G_T1^T Qcal)/2.         (11)

The second term is the transpose generator orientation of the
residual, not the transpose of the first displayed operator. There
is no assertion that it has the same bound or that the terms cancel.
Both expressions are still composed with their actual prefix and
relative covariance; no base-law identity has been differentiated.

From the definitions of J_k,F,D_l and cyclicity of a finite trace,

    Tr(J_k^T F D_l)
      =Tr(K_h Omega_(gh,k)^T V_gh Omega_(hh,l)).         (12)

Square roots cancel only on their positive subspaces. Substitute
V_gh=V_gh^gen-V_gh^Q and (11) into twice (12). The outside 2
cancels the 1/2 in (11), giving exactly (2)–(3). This is a split
inside L091's complete distinct-row class; it changes neither
L048's connected contractions nor L085's outside factor 3.

### 4. Bound the first trace and the bounded curvature subtraction

For clarity import the unsandwiched estimate needed here, rather
than infer it from a whitened norm. In L089 write Omega_k=F_k+H_k,
where F_k consists of the two actual exterior-circulation terms.
Their coefficient size is O(a^2 p(k)) and their paths have bounded
operator norms, so L089(6) gives

    ||F_k K_h||_HS<=C a^2 p(k)||K_h||_HS
                     <=C p(k) sqrt(log(eN)).

L090(11) gives ||H_k K_h||_HS<=C p(k)N. Its proof includes
the staggered boundary collars and every relative mode. Consequently

    ||Omega_k K_h||_HS<=C p(k)N,
    ||K_h Omega_(gh,k)^T||_HS<=C p(k)N,
    ||K_h Omega_(hh,k)||_HS<=C p(k)N.                   (13)

For the last two assertions use the fixed projections, their
commutation with K_h, and Omega_k^T=-Omega_k. No variable
multiplier is commuted through a resolvent or projection.

Finite Hilbert–Schmidt Cauchy–Schwarz in the exact order of R_L,
followed by (1) and (13), yields

    |Tr(K_h Omega_(gh,k)^T H_g K_a I_T K_h Omega_(hh,l))|
       <=C p(k)p(l) N^3.                               (14)

L088(5)'s full heat sum satisfies
sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i, after enlarging the fixed
polynomial as needed for L090. Summing (14) proves the first bound
in (4) for both actual probes. Every level and exterior orientation
was estimated, not selected at a convenient frequency.

For Q_0, L089(11) gives
||Sigma^(1/2) Q_0 Sigma^(1/2)||<=C. Apply the full row-map
argument in L091, proof section 1, to Q_0 in place of A_0: the
complete whitened forest insertion has norm at most C, so its
off-diagonal block F_Q has norm at most C. This does not require
positivity of Q_0. L091(11)–(12) therefore gives

    |Tr(J_k^T F_Q D_l)|
       <=||J_k||_HS ||F_Q|| ||D_l||_HS
       <=C p(k)p(l) N^(5/2).

The same complete heat sum proves the second bound in (4), including
its factor 2. Thus a^3 R_Q=O(N^(-1/2))->0.

### 5. Scope, continuation threshold and verification

This is local RESEARCH / REPRODUCTION under the unchanged EXPLORE
assessment `drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
It imports the finite contractions and L090's full-spectrum trace
estimate. The new specialization is the exact pinned prefix applied
to one generator orientation. The elementary interval computation is
needed to check the changed row composition and the boundary term;
no continuum Ward or flow theorem supplies that estimate. There is
no originality claim beyond the checked sources.

Equation (11)'s reverse orientation retains C G_T1^T Qcal; it has
no derivative immediately to the right of the prefix to which (6)
can be applied. Moving one there would require a separate exact
identity. Bound (1) therefore gives neither a bound on all of F nor
a resolution of R_R. The H diagonal, the E diagonal's limit and the
gradient-base crossed limit also remain. The joint remainder would
need a^3 limit -4 gamma D_i before the outside factor 3. Any numerical
comparison retains L082's saved-table/IEEE qualifications through
L091's reference comparison; no numerical value is used here.

Continue the same complete-group target only with actual control of
R_R or the H diagonal, or a signed joint leading identity. Abandon
this particular prefix gain if extending it requires deleting its
lower-end term without compact support, using a smooth rough input,
or transferring the derivative across a variable operator without
a commutator bound. No such extension is claimed in (4).

Supplemental exact interval verification is provided by
`scripts/combined-ward-response/check_other_other_prefix_generator.py`.
Run from the notebook with

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_other_other_prefix_generator.py

It checks both endpoint rows of (5), the coefficient commutator
identity with the lower-end term retained, and (10) in scalar
transverse-gradient coordinates. The full certificate is
`scripts/combined-ward-response/other-other-prefix-generator-certificate.json`.
All 16 cases N=2,4,6,10, with two coefficient profiles and two
transverse incidence values as applicable, have maximum entry error
0 against required error 0. Every exact Schur bound passes, with
no failures. Nonzero lower-end coefficient cases retain the rank-one
term; they do not assert (7) without its support hypothesis.
These finite normalization checks do not verify an asymptotic or
replace the analytical full-space argument above.

## Mathlib

Full matching prefix-generator and crossed-trace result: **not checked**.
Supporting interval incidence, finite Schur and Hilbert–Schmidt
inequalities: **not checked**. Unknown availability is not evidence
of absence. All mathematical inputs are the identified local results
and the displayed finite-matrix specialization, with its hypotheses
and unresolved reverse orientation retained.
