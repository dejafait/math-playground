# L101 — A finite signed cubic limit for the E diagonal

## Hypotheses

Use L092's exact R_E for SU(2), both actual L010 probes i=3,6,
L018's residual, the straight lower-rooted direction-1 forest,
relative all-face fixed-link box D=(-4,4)^4, admitted even N,
a=8/N and tau=1/16. Take the bare small-coupling coefficient at
fixed mesh before refinement. All transposes, coordinates and norms
are ordinary dimensionless stored ones. Keep all interior levels,
transverse end rows, ordered pairs including coincidences and the
complete exterior heat sum.

Import L085/L091's K_g=M tensor P, M_st=min(s,t), and
K_h=(L_D+Delta_T)^(-1) Qcal. Use L088's actual Omega_k and real
symmetric coefficients c_(i;kl,a). Put Delta=Delta_0=T^T T,
G=Delta^-1, U=T G^(1/2), and B_(s,r)=1_(r<s), where
1<=s<N and 0<=r<N. Axial tensor identities are implicit.
Thus UU^T=P and (UB)(UB)^T=K_g. Define

    A_11=I_1^T A_0 I_1,
    F_11=H_T^(-1/2) A_11 H_T^(-1/2), H_T=I_N tensor Delta,
    A_<s=B_s A_11 B_s^T, B_s f=sum_(r=0)^(s-1) f_r,
    Zeta_k=M_(b_k) Bq-M_(q_k) Bb,
    S_T=D_T Delta_T^-1 D_T^T.                         (1)

Here B_s acts on component-1 axial edges, not on forest link
components. Zeta_k is level diagonal and is exactly L097's map.
The common residual is A_0=(L_0 K_a+K_a^T L_0)/2-Q_3-Q_6.
The triplet retains its average of squares; the shear retains its
clover factors. All projections below are fixed after differentiation.

## Conclusion

For both probes there is a finite real functional K_(i,E) with

    a^3 R_E -> K_(i,E).                              (2)

A controlled finite-trace reduction, before any coefficient freezing,
is

    R_E=sum_(k,l)c_(i;kl,a) sum_(s=1)^(N-1)
       Tr_T[T G A_<s G T^T Zeta_k(s)^T S_T Zeta_l(s)]
       +O_i(N^(27/10)).                              (3)

In particular its scaled error is O_i(N^(-3/10)). The scalar
insertion in (3) is cumulative along the entire prefix. It is not
the local H-curvature insertion times s.

Here is an explicit formula. Use L097's continuum exterior columns
v_k, coefficients c_(i;kl), exact plane path matrix z_v, torus
projection P(theta) and curvature projection S(theta). For
theta in [-pi,pi]^3, indexed by 2,3,4, put

    d_mu=2 sin(theta_mu/2), lambda=sum_mu d_mu^2,
    t_mu=sin(theta_mu),
    W_mu(x)=integral_(-4)^(x_1) w_mu(t,x_T) dt,
    m_E(x,theta)=sum_mu W_mu(x)(t_mu^2-d_mu^2)
       -(lambda/2) sum_mu W_mu(x) cos(theta_mu)
       +u_1(x)[(1/2) sum_mu t_mu^2-lambda].            (4)

Then

    K_(i,E)=sum_(k,l)c_(i;kl) integral_D
      integral_([-pi,pi]^3) [m_E(x,theta)/lambda]
          Tr[P z_(v_k)^* S z_(v_l) P]
                                     dtheta/(2pi)^3 dx.             (5)

Set the integrand to zero at lambda=0. The series is absolutely
convergent. Its value and sign are not evaluated. No compensation
with L084 or complete other/other limit follows: R_R and R_H,tr
still lack cubic control, the gradient-base crossed limit remains
open, and the H axial/curvature functionals remain unevaluated.
Finer powers, the logarithm, other jets, finite matching, interacting
error <=c_box/2, continuum axioms, reflection positivity, infrared
control and finite positive mass remain unresolved. No candidate exists.

## Proof

### 1. Factor the actual E insertion before changing its covariance

L092(8)--(9) gives V_g=C A_11 C^T and C H_T^(1/2)=UB.
L065's scalar form theorem gives ||F_11||<=C with every axial
frequency and endpoint retained. Hence

    V_g=UB F_11 B^T U^T.

Unwhitening the actual L091 trace, and using K_h Qcal=K_h, gives

    R_E=sum_(k,l)c_(i;kl,a) Tr(Y_k F_11 Y_l^T),
    Y_k=K_h^(1/2) Omega_k^T UB.                      (6)

This is the exact gradient-residual/co-closed-base diagonal trace,
with no outside factor 3. L085 supplies that factor only when the
complete other/other contribution is assembled. No positivity or
block-diagonal full residual is assumed.

Write Omega_k=F_k+Zeta_k^T Cc-Cc^T Zeta_k, as in L097's
factorization; here F_k is the two exterior-circulation terms, and
Cc=I tensor D_T. Since Cc U=0 exactly,

    Y_k=K_h^(1/2) Cc^T H_k-K_h^(1/2) F_k UB,
    H_k=Zeta_k UB.                                   (7)

L088/L097 gives, with one fixed mode polynomial p,

    ||F_k||<=C a^2 p(k), ||Zeta_k(s)||<=C a p(k),
    ||Zeta_k(s+1)-Zeta_k(s)||<=C a^2 p(k),
    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.              (8)

These neighboring-level estimates do not extend a potential through
the upper pin. The full prefix remains in UB, whose norm is at most
CN. L086's full spectrum, used in L097, gives Tr K_h<=CN^4.
Therefore the second term of (7) has Hilbert–Schmidt norm at most
CN^2 a^2 p(k) N<=C' p(k)N. It is retained as an error.

### 2. Static replacement controlled by the full prefix energy

Let L_*=I tensor (Delta_T^(-1/2) D_T^T), a contraction from
transverse curvature to transverse links, with zero action on
ker D_T^T. The static replacement in (7) is

    Y_(k,*)=L_* H_k.

On an axial eigenmode mu of L_D and a transverse curvature mode
corresponding to a co-closed edge eigenvalue lambda>0,
K_h^(1/2) Cc^T has multiplier sqrt(lambda/(mu+lambda)); L_*
has multiplier 1 with the same partial isometry. Consequently

    ||K_h^(1/2) Cc^T-L_*||<=1,
    (1-sqrt(lambda/(mu+lambda)))^2
                                      <=mu/(mu+lambda).             (9)

Both maps vanish on ker D_T^T. This uses the complete axial
Dirichlet spectrum and all transverse rows.

The prefix-energy count from L097 applies to H_k without changing
its covariance: UB has mutually orthogonal increments with row
overlap min(s,t)P. Directly,

    ||H_k(s)||_HS^2=s ||Zeta_k(s)U||_HS^2,
    ||H_k(s+1)-H_k(s)||_HS^2
       =s ||[Zeta_k(s+1)-Zeta_k(s)]U||_HS^2
                                    +||Zeta_k(s+1)U||_HS^2.

Here UU^T=P, so these are precisely the row norms counted in
L097(11). Include the differences to zero at both levels 0,N.
In particular the upper jump contributes
(N-1)||Zeta_k(N-1)U||_HS^2 and is not assumed small by smoothness.
Using (8) and rank P=(N-1)^3 gives

    ||H_k||_HS^2<=C p(k)^2 N^3,
    ||D_v H_k||_HS^2<=C p(k)^2 N^2.                 (10)

Let Pi_eta select transverse curvature eigenvalues lambda<=eta.
The three-dimensional relative tensor shell count of L097 gives
rank Pi_eta<=C N^3 eta^(3/2) when N sqrt(eta)>=1. Since each
H_k(s)=Zeta_k(s)U B_s,

    ||Pi_eta H_k||_HS^2
       =sum_s s ||Pi_eta Zeta_k(s)U||_HS^2
       <=C p(k)^2 N^3 eta^(3/2).                    (11)

This estimate does not commute a multiplier with a projection. On
the complementary transverse spectrum (9) bounds the squared
error by mu/eta. Equations (10)--(11) therefore imply

    ||[K_h^(1/2) Cc^T-L_*]H_k||_HS^2
       <=C p(k)^2[N^3 eta^(3/2)+eta^-1 N^2].         (12)

Choose eta=N^(-2/5). Combining (7)--(12), including its F_k term,

    ||Y_k-Y_(k,*)||_HS<=C p(k)N^(6/5),
    ||Y_k||_HS+||Y_(k,*)||_HS<=C p(k)N^(3/2).

Trace Cauchy–Schwarz with ||F_11||<=C bounds the difference
between (6) and its static pairing by
Cp(k)p(l)N^(27/10). Equation (8) sums this error over every heat
mode. This proves a uniform cubic-scale approximation, rather than
a fixed-mass approximation with an N-dependent scaled error.

Since L_*^T L_*=S_T, cycling the static pairing through the
level-diagonal Zeta_k and S_T selects the diagonal block

    (B F_11 B^T)_ss=G^(1/2) A_<s G^(1/2).

Use U=T G^(1/2). Exchanging k,l in the complete real symmetric
exterior sum now gives exactly (3). Neither min(s,t) nor the
residual is declared level diagonal. The cumulative block appears
only after the quantitative covariance replacement.

### 3. Keep the exact cumulative scalar insertion, including its cut

This step identifies the local stencil whose limit is needed in (3).
Use L065's forward differences D_mu, centered averages C_mu and
T_mu=C_mu D_mu on transverse vertices. The incidence T in (1)
has tail-minus-head orientation; the signs of D_mu here are those
of L065. The quadratic forms below contain paired differences, so
this distinction does not change their scalar symbols.

At axial vertex j set

    k_j=a^-1 sum_(mu=2)^4 M_(u_(a,mu)(j)) T_mu,
    Q_(6,j)=(1/2) sum_(mu<nu)
       [T_mu^T M_(s_(a,mu nu)(j)) T_nu
                          +T_nu^T M_(s_(a,mu nu)(j)) T_mu],
    L_j=(Delta k_j+k_j^T Delta)/2-Q_(6,j).

Let W_(mu,r) be the exact triplet weight on a (1,mu) plaquette
at axial edge r: it is the transverse endpoint average of the
axial endpoint average of w_(a,1)+w_(a,mu). Explicitly,

    W_(mu,r)=C_mu^T[(w_(a,1)(r)+w_(a,mu)(r)
                         +w_(a,1)(r+1)+w_(a,mu)(r+1))/2],

with coefficient values zero at axial boundary vertices. For
1<=s<N the exact scalar matrix is

    A_<s=sum_(j=1)^(s-1) L_j+(1/4)L_s
       +(1/(2a)) sum_mu T_mu^T M_(u_(a,1)(s)) T_mu
       -sum_(r=0)^(s-1) sum_mu D_mu^T M_(W_(mu,r)) D_mu.             (13)

To verify (13), test the quadratic form on any transverse vertex
field phi. The input B_s^T phi equals phi on axial edges r<s and
zero elsewhere. Its C_1 average equals phi at vertices j<s,
phi/2 at j=s and zero at j>s. Thus the transverse generator and
clover shear terms in L065 give the first two terms of (13),
including the quarter weight. L065(6) gives for the other generator
outputs, for each mu,

    (1/(2a)) sum_(r<s)
      <T_mu phi,M_(u_(a,1)(r+1)-u_(a,1)(r)) T_mu phi>
       =(1/(2a))<T_mu phi,M_(u_(a,1)(s)) T_mu phi>.

The lower coefficient is zero. This is the endpoint term in (13),
not zero at the moving prefix cut. Finally L008's average of
squares yields the last term of (13); no axial clover averaging
of that square is introduced. Polarization proves the matrix
identity. The calculation retains the other generator components
on this pure component-1 input exactly as L065 requires.

The same scalar form bound, applied to B_s^T phi, gives

    |phi^T A_<s phi|<=C s phi^T Delta phi.             (14)

In particular a A_<s is a uniformly bounded finite-range stencil
and is bounded in form by C' Delta, since a s<=8. Its range in
the transverse index is fixed independently of s,N. Coefficients
in (13) have compact transverse support, with all neighboring
stencils inside the physical boundary on sufficiently fine meshes.

### 4. Derive the normalized stencil limit

Use zero extension to the transverse infinite grid wherever a
coefficient is nonzero; compact support makes all products there
the exact finite-grid products. With shifts S_mu, write
T_mu=(S_mu-S_mu^-1)/2 and
Delta=sum_mu(2I-S_mu-S_mu^-1). For one transport summand the
exact local identity is

    (Delta M_u T_mu-T_mu M_u Delta)/(2a)
       =([Delta,M_u]T_mu-[T_mu,M_u]Delta)/(2a).       (15)

There is no global assertion that pinned shifts commute at the
physical boundary: (15) is used only on the coefficient-supported
stencils, where zero extension agrees with the finite product.
The coefficient differences in each commutator are O(a). All
coefficients and their needed physical differences converge
uniformly to the smooth L008 displacement and derivatives, as
in L028's coefficient construction.

At a common cell point and fixed torus frequency, the limiting
symbols of these divided commutators are

    [Delta,M_u]/a ->-2 sum_j (partial_j u) i sin(theta_j),
    [T_mu,M_u]/a ->(partial_mu u) cos(theta_mu).

Consequently the frozen normalized single-layer generator symbol
is

    g_T=sum_(j,mu=2)^4 (partial_j u_mu)t_j t_mu
                       -(lambda/2) sum_mu w_mu cos(theta_mu).

The shear symbol is sum_(mu<nu)s_mu nu t_mu t_nu. Since
s_mu nu=partial_mu u_nu+partial_nu u_mu, it cancels precisely
the off-diagonal part of g_T. The triplet symbol at layer t is
sum_mu(w_1+w_mu)d_mu^2; its axial and transverse endpoint
averages converge to that same weight. These statements preserve
the actual scalar shear and average-of-squares normalization.

Multiply (13) by a. The quarter layer term vanishes uniformly,
since ||L_s||<=C by the commutator energy calculation and bounded
shear. The complete axial sums are uniform Riemann sums of their
bounded smooth coefficients. The endpoint term tends to
(u_1(x)/2)sum_mu t_mu^2. Thus the limiting frozen symbol is

    integral_(-4)^(x_1) [sum_mu w_mu(t)(t_mu^2-d_mu^2)
       -(lambda/2)sum_mu w_mu(t)cos(theta_mu)-w_1(t)lambda] dt
       +(u_1(x)/2)sum_mu t_mu^2.

The coefficient u_1 vanishes at the lower face and
integral_(-4)^(x_1) w_1 dt=u_1(x). This is (4). The stencil
coefficient convergence is uniform in the axial cut s and in
transverse position: the Taylor errors in (15) are uniform, and
an axial sum has at most N terms multiplied by a. Staggered
cell offsets change these smooth coefficients by O(a).

In particular |m_E|<=C lambda. This follows either from (4),
using t_mu^2<=d_mu^2 and bounded W_mu,u_1, or from (14).
There is no singular uncanceled transport symbol in this scalar
insertion and no claim that m_E is zero or has a fixed sign.

### 5. Control the transverse inverse before the finite-range limit

Set zeta_(k,a)=Zeta_k/a and

    L_s=T G (a A_<s) G T^T.

Equation (14) gives -C P<=L_s<=C P, uniformly in s,N. In
particular ||L_s||<=C and L_s=P L_s P. The static expression
in (3), multiplied by a^3, is

    a^4 sum_(k,l)c_(i;kl,a) sum_s
                       Tr_T[L_s zeta_k(s)^T S_T zeta_l(s)].        (16)

For epsilon>0 let G_epsilon=(Delta+epsilon I)^-1,
L_(s,epsilon)=T G_epsilon (a A_<s) G_epsilon T^T and
S_epsilon=D_T(Delta_T+epsilon I)^-1 D_T^T.
The relative intertwining in L085/L092 shows exactly

    L_(s,epsilon)=f_epsilon(Delta_T) L_s f_epsilon(Delta_T),
    f_epsilon(lambda)=lambda/(lambda+epsilon).

No variable coefficient is commuted through an inverse. The
three-dimensional shell sum from L097 gives
Tr Delta^-1+Tr Delta_T^-1<=C N^3. Using
[epsilon/(lambda+epsilon)]^2<=epsilon/lambda therefore gives

    ||(I-f_epsilon(Delta_T))P||_HS
       +||S_T-S_epsilon||_HS<=C N^(3/2)sqrt(epsilon),
    ||L_s-L_(s,epsilon)||_HS<=C N^(3/2)sqrt(epsilon).

The last line follows by telescoping the exact two-sided identity
and using L_s=P L_s P and its uniform norm bound. Other factors
in (16) have norm <=Cp(k)p(l); their transverse dimension is
O(N^3). Trace Cauchy–Schwarz bounds each per-level replacement
error by Cp(k)p(l)N^3 sqrt(epsilon). Since a^4 N^4 is bounded,
the complete normalized error is <=C_i sqrt(epsilon), uniformly
in N. This controls all singular transverse modes before freezing.

At fixed epsilon approximate both inverse functions uniformly by
polynomials on [0,12], for example the geometric polynomial and
explicit error in L097 section 4. The normalized stencil a A_<s
has fixed range and uniform norm by (14). Telescoping the finite
product thus bounds its normalized trace error by a constant
depending on epsilon times the inverse approximation errors,
uniformly in s,N and after the full heat sum.

For fixed polynomial degrees every trace is a finite sum of
closed walks of fixed index range. Each transverse boundary
collar has O(N^2) rows per level. Their contribution to (16)
is at most C a^4 N^3=O(1/N), with all coefficients bounded.
Elsewhere the stencil coefficient convergence in section 4,
and L097's proved v_(k,a)/a ->v_k and neighboring coefficient
control, permit freezing on each walk with error tending uniformly
to zero for fixed k,l. The normalized sum is a four-dimensional
Riemann sum. The frozen symbol of L_(s,epsilon) is

    [m_E lambda/(lambda+epsilon)^2] P;

the frozen Zeta/a symbol is the actual z_v, and that of
S_epsilon is C C^*/(lambda+epsilon). It follows that the
regularized version of (16) converges to the corresponding torus
and spatial integral for each fixed exterior pair. Send polynomial
degrees to infinity at fixed epsilon using their uniform errors.
Then send epsilon to zero: |m_E|<=C lambda bounds the displayed
symbol uniformly, the curvature projection factors are contractions,
and the z_v are bounded. Dominated convergence identifies (5).
The uniform O(sqrt(epsilon)) finite-trace error makes this passage
valid for the original trace, rather than just the frozen model.

### 6. Retain all exterior heat modes and the scope of the result

All finite normalized traces above and their limits are bounded
by Cp(k)p(l), using (8), (14) and the bounded torus symbols.
L097's complete exterior heat majorant and fixed-mode coefficient
convergence apply without changing the modes or probes:

    |c_(i;kl,a)|p(k)p(l)
       <=C p(k)p(l) exp[-(tau/16)(|k|^2+|l|^2)].

Extend nonadmitted modes by zero. Uniform heat tails followed by
finite-pair convergence prove absolute convergence of (5) and
passage of the full sum through the limit. Combining this with
(3)'s scaled error proves (2). Reality follows from the original
real symmetric trace sum, or from its paired torus expression.

This is one bounded RESEARCH / REPRODUCTION attempt under the
unchanged assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The finite contraction, pure-component covariance identity and
scalar form bound are imported from L091/L092/L065. The proof
justifies the new static specialization and cumulative scalar
symbol; it does not reprove those imported results or assume a
general Ward/flow-finiteness theorem for this isolated group.
This is local standard-method progress, with no originality
claim beyond the checked sources. No numerical certificate or
IEEE assumption is needed for (2)--(5). Any future comparison
with D_i retains L082's qualifications through L084.

## Mathlib

Full matching limit theorem: **not checked**. Supporting finite
spectral calculus, symmetric form bounds, trace ideals, discrete
product rules, Riemann sums and dominated convergence: **not
checked**. Unknown availability is not evidence of absence.
