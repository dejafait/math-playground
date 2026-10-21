# L240 — Ordered massive boundary transfer for the local left crossed trace

## Hypotheses

Use exactly L239(1)--(3) on the relative all-face pinned SU(2) cube,
straight lower-rooted direction-1 forest, sufficiently large admitted
even N, a=8/N, tau=1/16, ordinary stored coordinates, bare-first
coefficient and actual probes i=3,6. All source/end rows, constant
component indices, endpoint/clover filters and heat labels are retained.
L237--L239 remain imported with their pending critical-audit qualifications.

Let E_f be the finite interior-level transverse-link space and Z_f
the transverse vertex space on those same axial levels. Their infinite
counterparts are E_b=l2(Z^4;R^3) and Z_b=l2(Z^4). Zero embeddings
are i_E and i_Z. On either space, superscript s=f,b, set

    R_s=(Delta_E,s+epsilon I)^(-1),
    P_s=T_s(I_ax tensor (Delta_0,s+delta I)^(-1))T_s*,
    Q_s=I-P_s,
    G_s=aG0_s,
    V_s=sum_(mu=2)^4 H_av,s U_mu,s C_mu,s,
    A_s=P_s G_s-T_s V_s.                              (1)

Here P_s,Q_s denote the positive-mass contractions throughout this
lemma, not the exact massless projections. In particular neither
P_s^2 nor Q_s^2 is replaced by a single factor. V_s maps E_s to Z_s;
T_s maps Z_s to E_s. The inverse in P_s acts independently on each
axial level, as in L100(11).

Use L228(1)'s compact Lipschitz extensions of the normalized actual
exterior columns to define z_k^b=a v_k^b, preserving all existing
finite samples before pinned zero extension. Define Omega_k^b by
the complete six-term formula L088(3), including f_k=Cc z_k,
b_k=Bb z_k and q_k=Bq z_k. Thus, on each space,

    Omega_k=Bb* M_f Bq-Bq* M_f Bb
             +Bq* M_b Cc-Cc* M_b Bq
             +Cc* M_q Bb-Bb* M_q Cc.                 (2)

No exterior-circulation term is deleted. On the whole grid use the
same local generator and averaging stencils and the compact original
displacement, extended by zero outside its interior support. All local
stencils agree with the finite ones away from the physical faces.
Define

    B_i^s(epsilon,delta)=a^-1 sum_(k,l)c_(i;kl,a)
      Tr_Es(R_s Q_s^2 Omega_k,s* P_s A_s
                                      R_s Q_s^2 Omega_l,s Q_s). (3)

In particular B_i^f is literally R_(loc,epsilon,delta) in L239(3).
The full finite-mesh heat coefficients are the same in both (3).
The infinite expression is a comparison trace, not a new covariance
law or a change of the physical boundary condition.

## Conclusion

At epsilon=N^-1 and delta=N^(-4/3),

    |B_i^f(epsilon,delta)-B_i^b(epsilon,delta)|
                                                  <=C_i N^-10. (4)

Consequently L239(5) gives

    |R_L-B_i^b(N^-1,N^(-4/3))|
                         <=C_i N^(5/2)sqrt(log(eN)).   (5)

This is a boundary/localization comparison only. The remaining
ordered whole-grid trace B_i^b still needs a quantitative coefficient
estimate transferring L100's frozen odd cancellation. No bound
O(N^(5/2)log(eN)^2) for B_i^b or complete R_L is established here.
Other L011 component rates and assembly, the interacting reflected
error <=c_box/2, continuum axioms, infrared control and finite positive
mass remain open. This partial reproduction awaits separate critical
audit; there is no complete-solution candidate.

## Proof

### 1. Locate the compact insertions without localizing a projection

L009's displacement has fixed physical clearance from every face.
L229(2) already checks both input and output support of G_s, with
its complete finite-range generator filters. L100(7) and L093(8)
give V_s in (1): U_mu is compact, and H_av and C_mu have fixed
range. Therefore V_s also has compact input and output support in
all four directions. The long axial prefix of E_pref is absent from
V_s; it was estimated separately in L238, not truncated here.

Choose diagonal selectors chi_E and chi_Z on fixed interior physical
neighborhoods of these supports, including a fixed stencil margin.
For sufficiently large N they have rank at most C N^4 and distance
at least cN from every physical face, with c>0 independent of N.
Writing G=G_b and V=V_b, one has exactly

    G=chi_E G chi_E=i_E G_f i_E*,
    V=chi_Z V chi_E=i_Z V_f i_E*,
    ||G||+||V||<=C.                                   (6)

The V norm follows from ||H_av||,||C_mu||<=1 and bounded
displacement; the G norm is L100's ||aG0||<=C. No assertion
of compactness is made for P_s G_s or A_s.

All inverses in (1) are bounded at positive mass. Finite-rank G,V
make the products in (3) trace class even on the infinite spaces.
For each k,l put, in the exact displayed order,

    W_G,s=R_s Q_s^2 Omega_l,s Q_s
                          R_s Q_s^2 Omega_k,s* P_s^2,
    W_V,s=R_s Q_s^2 Omega_l,s Q_s
                          R_s Q_s^2 Omega_k,s* P_s T_s. (7)

W_G,s maps E_s to E_s, while W_V,s maps Z_s to E_s. Cyclicity
with a finite-rank factor, including the rectangular trace identity,
gives exactly

    Tr_Es(R_s Q_s^2 Omega_k,s* P_s A_s
                                  R_s Q_s^2 Omega_l,s Q_s)
            =Tr_Es(G_s W_G,s)-Tr_Zs(V_s W_V,s).        (8)

For the second term, cycle T_s V_s to obtain the trace on Z_s;
do not identify Z_s with E_s. The first term retains the two adjacent
P_s factors from X and A_s. Equation (7) contains five Q_s factors
and two P_s factors in W_G, and five Q_s factors and one P_s factor
in W_V. Neither word uses a projection commutation or idempotence.

### 2. Uniform approximation of all nine inverse-bearing factors

Import L205(2),(9)--(10),(14)'s scalar Chebyshev residual, in the
precise finite/infinite specialization proved in L229(6)--(10).
For 0<mu<=1 and integer m>=1 it supplies a polynomial p_(m-1,mu)
of degree at most m-1 with

    ||(D+mu I)^(-1)-p_(m-1,mu)(D+mu I)||
            <=mu^-1 eta_mu,
    eta_mu=2 rho_mu^m<=2 exp(-m sqrt(mu)/3),
    rho_mu=(sqrt(16+mu)-sqrt(mu))
                               /(sqrt(16+mu)+sqrt(mu)). (9)

The applicability is unchanged: every finite relative scalar component
of Delta_E and every transverse slice Delta_0 has spectrum in [0,16],
as does its whole-grid counterpart. L229, proof sections 1 and 5,
checks the true relative interval end diagonals, including the constant
normal component, and the infinite Fourier symbols. Delta_0 has three
interval factors and an axial identity; no axial inverse is inserted.
The bounded self-adjoint spectral theorem gives (9) on the infinite
space as well. This imports the already proved scalar result; it does
not import L229's estimate for its different ordered trace.

Replace R_s by its polynomial Z_E,s, and define

    Z_0,s=p_(m-1,delta)(Delta_0,s+delta I),
    Ptilde_s=T_s(I_ax tensor Z_0,s)T_s*,
    Qtilde_s=I-Ptilde_s.                              (10)

Since ||T_s||^2<=12 and P_s,Q_s are contractions,

    ||R_s-Z_E,s||<=epsilon^-1 eta_epsilon,
    ||P_s-Ptilde_s||+||Q_s-Qtilde_s||
                                  <=24 delta^-1 eta_delta. (11)

If eta_epsilon<=1 and alpha=12 delta^-1 eta_delta<=1, each
polynomial P or Q has norm at most 2, and ||Z_E,s||<=2/epsilon.
The complete Omega, including both f terms, has

    ||Omega_k,s||<=C a p(k).                          (12)

For s=f this follows from L088(3),(5) and bounded stencil
multiplicity. For s=b the same multiplicity and ||z_k^b||_infinity
<=Ca p(k) suffice: all three f,b,q are fixed finite linear combinations
of these samples. Thus (12) does not need a smooth extension through
any pinned zero. L228's stronger neighboring bounds remain available
for the later coefficient problem but are not needed for (12).

Let Wtilde_G,s and Wtilde_V,s result from replacing every R,P,Q
in (7) by (10), retaining Omega and T unchanged. Telescope each
word one factor at a time, in its original order. In W_G there are
two R changes and seven P/Q changes; in W_V there are two R
changes and six P/Q changes. Two Omega factors contribute
C a^2 p(k)p(l); both inverse factors together contribute
C epsilon^-2, also when one of them is changed. All projection
norms are at most 2, and the extra T in W_V is bounded. Hence
both word errors satisfy the uniform finite inequality

    ||W_J,s-Wtilde_J,s||
       <=C p(k)p(l) a^2 epsilon^-2
                          (eta_epsilon+delta^-1 eta_delta),
                              J=G,V; s=f,b.           (13)

No derivative, coefficient freezing, heat cutoff or commutation of
a multiplier through an inverse is used in this estimate.

### 3. Polynomial paths from the two compact insertions

An edge inverse polynomial has range at most m-1. A slice vertex
polynomial also has range at most m-1, and its two incidences give
Ptilde,Qtilde range at most m+1. Let r_Omega bound the range of
the complete six-term stencil (2). Both polynomial words in (7),
and their adjoints, consequently have range at most

    L_m=9(m+1)+2r_Omega+2.                            (14)

This is a common upper bound: W_G has nine inverse-bearing
factors, W_V eight and one extra incidence. Fixed component staggering
is included in the range convention and the fixed support margins.

For L_m<cN, with a fixed extra local-stencil allowance, expand each
polynomial word into incidences, Laplacian powers, identities and
the actual Omega terms. Starting at an output row selected by chi_E,
every intermediate edge, vertex and plaquette index stays strictly
inside the box. All finite entries there, including mass diagonals
and actual exterior samples, equal the infinite entries. Every path
endpoint remains in the appropriate finite input space. Therefore
there are full row identities

    chi_E(i_E Wtilde_G,f i_E*-Wtilde_G,b)=0,
    chi_E(i_E Wtilde_V,f i_Z*-Wtilde_V,b)=0.           (15)

The second identity has vertex input columns; this does not alter
the path argument. Paths starting at chi_Z in the adjoint word also
give the corresponding full column comparison. In particular (15)
is not merely agreement after deleting external covariance columns.
The true finite normal end rows differ from scalar Dirichlet rows,
but no path in (15) reaches them. Every such row and every constant
mode remains in the global spectral errors (11)--(13).

Put F_G=i_E W_G,f i_E* and F_V=i_E W_V,f i_Z*. By (13),(15)
and the isometry of the embeddings, for J=G,V,

    ||chi_E(F_J-W_J,b)||
       <=C p(k)p(l) a^2 epsilon^-2
                          (eta_epsilon+delta^-1 eta_delta). (16)

There is no assumption that the actual inverse kernels have finite
propagation. Their entire tails are controlled by (13).

### 4. Trace comparison and full heat sum

Embedding preserves the finite traces in (8). The difference of
the G branch is Tr_Eb(G(F_G-W_G,b)); that of the V branch is
Tr_Zb(V(F_V-W_V,b)). By (6), G=G chi_E and V=V chi_E.
For a finite-rank operator K, |Tr K|<=rank(K)||K||, since its
trace norm is bounded by the number of nonzero singular values
times its norm. Using (6),(16), each branch difference is thus at most

    C p(k)p(l) N^4 a^2 epsilon^-2
                          (eta_epsilon+delta^-1 eta_delta). (17)

For the rectangular branch, V(F_V-W_V,b) is an operator on Z_b
with range contained in chi_Z, so the same rank bound applies.
At any fixed positive masses the same norms also show absolute
convergence of (3) after L088's complete envelope
sum|c_(i;kl,a)|p(k)p(l)<=C_i. Multiplying (17) by the original
a^-1 and summing gives, whenever the accuracy and range conditions
above hold,

    |B_i^f-B_i^b|<=C_i a N^4 epsilon^-2
                          (eta_epsilon+delta^-1 eta_delta). (18)

Only now choose

    epsilon=N^-1, delta=N^(-4/3),
    m=ceil(60 N^(2/3)log(eN)), eta=2(eN)^(-20).

Since delta<=epsilon, (9) gives eta_epsilon,eta_delta<=eta.
The accuracy conditions hold, and L_m/N=O(N^(-1/3)log(eN))
tends to zero, so (15) holds for sufficiently large admitted N.
Equation (18) is then at most

    C_i N^(19/3)eta<=C_i N^(-41/3)<=C_i N^-10.        (19)

This proves (4). The deliberately small comparison error is not an
optimized exponent. Combining it with L239(5) proves (5), without
changing the sign, normalization or single outside a^-1 in R_L.
Both exterior-circulation terms, both actual probes and the full heat
sum were retained throughout.

This is RESEARCH / REPRODUCTION under the unchanged EXPLORE
assessment for the quantitative R_L target. The scalar approximation,
bounded self-adjoint spectral theorem, polynomial propagation and
finite-rank trace inequalities are existing tools. The required new
applicability argument is the two ordered words (7), their rectangular
domains and complete projection counts, and compact insertions (6).
L229's co-closed-sector conclusion and L228's bulk trace bound do not
transfer to (3); neither was used. ATTEMPTS/029--032's stopped
commutation, fixed-mass substitution and absolute-moment mechanisms
are not used. There is no claim of progress beyond the sources checked,
no numerical certificate and no audit of the imported upstream inputs.

### 5. Separate critical audit of the literal boundary comparison

Audit dated 2026-10-19, STEP_ID YM-20261019-339-left-crossed-complete-rate-audit.
Accept (4)--(5) relative to the scalar approximation and finite local
stencil inputs stated above, and L239 as audited in this step. This
supersedes the original pending-audit qualification. The whole-grid
trace is bounded separately in L241, not in this comparison.

Directly expanding P_s A_s gives P_s^2 G_s-P_s T_s V_s.
Cyclically moving the compact insertion, rather than P_s A_s,
therefore gives exactly (7)--(8). The second trace is on Z_s,
because V_s:E_s->Z_s and W_V,s:Z_s->E_s. This verifies the
relative minus sign and the five Q factors in each branch, two P
factors in W_G and one P in W_V. Both resolvents remain. G and
V have compact input and output from the displacement and bounded
stencils, while A_s need not have compact output.

The dimensionless relative component Laplacian has interval end
diagonals 1 on its normal-edge interval and 2 on vertex intervals;
its spectrum is contained in [0,16]. The slice-vertex spectrum is
contained in [0,12]. These are the finite/infinite spaces checked
in L229's scalar specialization of L205. Positive mass makes its
uniform residual applicable even to a constant component mode.
Each replaced P or Q costs at most 12 delta^-1 eta_delta, and
the two R factors cost epsilon^-2 together. The bounded T in W_V
adds no mesh power. Telescoping nine, respectively eight, inverse-
bearing factors gives (13), with a^2 from the two actual Omegas.

The range bound (14) counts both incidences in every projection
polynomial, as well as the additional T and both Omega stencils.
Every elementary polynomial path starting at chi_E stays in the
interior when L_m<cN. Its endpoint can therefore be compared on
the entire appropriate input space, including the zero outside
embedding. Rows near physical faces occur only in the operator
approximation error, not in the exact polynomial identity. This
justifies (15)--(16) without deleting covariance sources.

The compact insertion ranks are O(N^4), and their norms are O(1).
After the original a^-1, the trace error is exactly the allowance
C_i a N^4 epsilon^-2(eta_epsilon+delta^-1 eta_delta).
At the stated schedule this is O(N^(19/3)eta), while eta is
O(N^-20). The propagation ratio is O(N^-1/3 log(eN)), tending
to zero. Hence (4)'s weaker N^-10 bound follows for sufficiently
large admitted N. The polynomial heat envelope applies before
choosing the schedule and gives (5) with L239. No fixed-degree
limiting theorem has received a mesh-dependent degree or mass.

## Mathlib

Full matching ordered left-crossed relative-boundary comparison:
**not checked**. Supporting bounded self-adjoint spectral calculus,
Chebyshev approximation, finite propagation and finite-rank rectangular
trace inequalities: **not checked**. Unknown coverage is not absence.
