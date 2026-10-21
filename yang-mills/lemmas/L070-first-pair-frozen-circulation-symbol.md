# L070 — The first pair has a nonzero frozen circulation symbol

## Hypotheses

Keep L064's first pair and L069 section 4's skew operator, with
Tz(v,w)=z(v)-z(w), and retain both original endpoint placements.
The direct right block is L067's

    W_X=sqrt(N) G E_0^T A_0 I_T Sigma_T.

Here Sigma_T is the full four-dimensional Hodge component covariance.
Let B_2,B_3 be the actual two-link transverse path maps, D their
circulation map, and S the upper-vertex-to-all-level-link map
(Sz)_s=sTz, 1<=s<N. Thus the unchanged base row is H_X=G S^T.
All these are the complete finite pinned maps until the explicitly
defined frozen test below.

For that test only, freeze the upper coefficient r at a real
three-vector R, the smooth right lifted field at a real vector v,
and the displacement at u. On each oriented transverse plane mu<nu,
freeze the exterior path coefficients to

    t_2=a(v_mu+v_nu), t_3=a(v_nu-v_mu), t_1=0.

These are the exact paths of a constant transverse stored link field
av. They define a local constant-coefficient test, not a substitution
for either actual probe. Use infinite-grid cell-center symbols at
four-dimensional frequency (0,theta), theta in [-pi,pi]^3, theta!=0.
In A_0 keep only the frozen generator part of order 1/a. L066 gives
its exact symbol. Coefficient derivatives, Q_3,Q_6, physical boundaries,
axial profiles and the full signed heat sum are outside this symbol
test. In particular evaluating a four-dimensional symbol at zero
axial frequency does not replace Sigma_T in the finite trace by G.

## Conclusion

The exact circulation/path part of the finite direct first pair, for
one exterior product, is

    F_circ= sqrt(N) Tr[G C_r G E_0^T A_0 I_T
                              Sigma_T D^T Q_l S],             (1)
    Q_l=M_(t_l,2) B_3-M_(t_l,3) B_2,
    C_r=E_v^T M_r T-T^T M_r E_v.

No axial levels, end rows, covariance weights or heat coefficients
are removed in (1). After the stated freezing, remove the scalar
level factor s and the axial embedding normalization from the formal
local symbol of (1). The resulting symbol is

    m(theta;R,v,u_1)
      =2u_1 [(R . (d c)) (beta . (c v))]/H²,
    d_j=2 sin(theta_j/2), c_j=cos(theta_j/2), H=sum_j d_j²,
    beta=(H I-d d^T) diag(c_j²) d.                          (2)

Products dc and cv in (2) are componentwise. Its normalized full
transverse angular mean is

    integral m(theta) dtheta/(2pi)^3 =2u_1 gamma (R . v),
    gamma=(1/3) integral [H sum_j d_j² c_j^4
                               -(sum_j d_j² c_j²)²]/H²
                                      dtheta/(2pi)^3 > 0.   (3)

Thus neither summing all transverse planes nor angular averaging
annihilates this frozen composition identically. At the retained
carrier theta=(pi/2,pi,0), with R=v=(1,0,0), its value is u_1/9.

This is a negative test of an automatic frozen-symbol cancellation,
not a lower bound, asymptotic expansion or sign for either actual
probe. It establishes neither failure nor success of the required
O(N²) bound. It gives no N³ coefficient of the pinned trace. The
actual exterior contraction, variable coefficients, axial covariance,
boundaries and remainder must still be controlled. No logarithm,
finite matching or interacting reflected-error improvement follows.
This is a local REPRODUCTION under the unchanged SPECIALIZE response
assessment, not a claim of progress beyond the sources assessed.

## Proof

### 1. Compress the two placements with their signs unchanged

Use L069's exact expression sum_(a,b,c) epsilon_(abc) t_a
W_b^T C_r H_c. Since H_1=0, its terms involving t_2,t_3 are

    -sum_p t_2(p) W_1(p)^T C_r H_3(p)
     +sum_p t_3(p) W_1(p)^T C_r H_2(p)
      =-Tr[D W_X^T C_r H_X Q_l^T].                        (4)

Transposing this real scalar trace and using C_r^T=-C_r changes
the minus sign to plus:

    (4)=Tr[Q_l H_X^T C_r W_X D^T].

Substitute H_X^T=SG, L067's direct W_X, and cycle the finite
rectangular trace. This proves (1). The other two monomials have
t_1 and two right paths; they have not been declared zero in the
actual problem. They vanish only in the constant-exterior test where
t_1=0 by definition. Both endpoint placements and all transverse
planes remain in (1).

### 2. Compute the right paths at their actual staggered positions

Center each transverse plaquette. In plane mu<nu its four signed
edge symbols, in order, are

    exp(-i theta_nu/2) X_mu,
    exp( i theta_mu/2) X_nu,
   -exp( i theta_nu/2) X_mu,
   -exp(-i theta_mu/2) X_nu.

Their sum is D X=-i d_nu X_mu+i d_mu X_nu. On a vertex mode,
T has symbol -i d, so their first-two and middle-two sums give

    B_2 T=-i(d_mu c_nu+d_nu c_mu),
    B_3 T= i(d_mu c_nu-d_nu c_mu).

The real cross terms cancel exactly because
d_mu sin(theta_nu/2)=d_nu sin(theta_mu/2). Consequently the actual
alternating minor with the frozen coefficients is

    Q T=2ia(v_nu d_mu c_nu-v_mu d_nu c_mu).

Multiplying by D^* in this plane gives component mu equal to
2a(d_nu² c_mu v_mu-d_mu d_nu c_nu v_nu), and component nu
equal to 2a(d_mu² c_nu v_nu-d_mu d_nu c_mu v_mu). Summing all
three transverse planes therefore yields the exact symbol

    D^* Q T=2a L diag(c_j) v,  L=H I-d d^T.                (5)

This uses the alternating paths jointly. Replacing Q by an arbitrary
bounded path map would lose the factors in (5).

### 3. Retain the two left Green weights and the direct covariance

For constant upper coefficient R the diagonal terms in C_R cancel.
In direction j its action on vertices is
R_j[z(v-e_j)-z(v+e_j)]. Hence

    C_R(theta)=-2i sum_j R_j sin(theta_j)
              =-2i R . (dc).                             (6)

At four-dimensional frequency (0,theta), the full Hodge transverse
component symbol is H I, so its inverse symbol is H^(-1)I.
The upper vertex Green symbol is separately H^(-1).

L066 proof section 2 gives K_(T,1)=-(iu_1/a) diag(c_j²)d.
At this frequency K_(1,T)=0, the curl-energy cross blocks with
component 1 vanish, and its transverse block is L. Thus the order
1/a part of the actual residual has symbols

    (A_0)_(T,1)=-(iu_1/(2a)) beta,
    (A_0)_(1,T)= (iu_1/(2a)) beta^T.                       (7)

The factor 1/2 is the symmetrization of L_0 K+K^* L_0. The bounded
curvature forms and shifted-coefficient derivatives are excluded
only by the explicit definition of the principal frozen test, not
by a claim that their trace remainders are small.

Insert (5)–(7) in the precise order G C_R G A_(1,T)
Sigma_T D^* Q T from (1). Since L beta=H beta, its scalar value is

    H^(-1)[-2i R.(dc)] H^(-1)
        [iu_1 beta^T/(2a)] H^(-1)[2a L diag(c)v]
       =2u_1 (R.(dc))(beta.(cv))/H².

This proves (2), including its sign. No variable multiplier has
been commuted with a covariance in deriving the finite identity.
The commutation in this displayed scalar calculation is permissible
only for the explicitly frozen symbols.

### 4. The complete angular mean survives

Put S_0=sum_j d_j² c_j². Then
beta_j=d_j(H c_j²-S_0). The coefficient of R_j v_k in (2),
apart from 2u_1, is

    d_j c_j d_k c_k (H c_k²-S_0)/H².

For j!=k this is odd in theta_j and integrates to zero. All its
diagonal integrals are equal by permutation of the three coordinates.
Their sum is the integral of

    V(theta)=[H sum_j d_j² c_j^4-S_0²]/H².                (8)

For H>0, (8) is the variance of the three values c_j² under weights
d_j²/H. It is nonnegative and bounded by 1. At
theta=(pi/2,pi,0), H=6, S_0=1 and sum d_j² c_j^4=1/2,
so V=1/18>0. Continuity gives a positive-measure neighborhood
inside the integration cube on which it is positive. This remains
true though the displayed carrier lies on one cube face. Thus its
integral is strictly positive, proving (3).

The integrals used here are genuine integrals, with no singular
principal-value prescription: |beta_k|<=2H|d_k| and
|d_j d_k|<=H imply that each tensor entry above is bounded near
H=0. Assign any value at the single zero point. Finite measure,
parity and permutation symmetry therefore apply directly.

At the same carrier beta=(2sqrt(2),-2,0), dc=(1,0,0) and
cv=(1/sqrt(2),0,0) for R=v=(1,0,0). Formula (2) is u_1/9,
as claimed. This checks the nonzero symbol without numerical
quadrature or a mathematical script.

### 5. What the test does and does not decide

The frozen angular tensor is a positive scalar times R.v, multiplied
by u_1. Thus an argument that declares the direct first pair zero
from skew-symmetry, summing transverse directions, or odd-frequency
integration cannot be used without additional actual-probe structure.
The remaining question is the actual signed exterior/axial contraction
and a justified approximation of the pinned trace, not whether the
local tensor in (3) is identically zero.

The test uses an infinite-grid symbol at zero axial frequency; it is
not a theorem approximating the complete four-dimensional covariance
on the variable-coefficient finite box. In particular neither a
nonzero symbol nor a nonzero angular mean proves a nonzero leading
coefficient after summing the actual exterior heat expansion. We do
not assign the frozen R,v to a specific probe or infer a scale from
phase-space counting. All finite trace estimates from L064 and L069
remain unchanged. The O(N²) direct bound is unresolved.

L011/L019's other response and forest jets, other/other cubics,
measure, insertion/flow terms, all nine mixed placements for the
logarithm, finite matching, reflected error <=c_box/2, continuum
fields, full reflection positivity, infrared control and finite
positive mass remain open. Conditional signs stay conditional; the
shared quartic must still be subtracted only once.

### 6. A separate actual-column exterior/axial diagnostic, 2026-10-08

This subsection defines and tests a surrogate suggested by (3), not
an approximation theorem for (1). Keep the actual two probes,
tau=1/16, all relative modes and the straight forest at an admitted
even mesh. Let Q_i, Sigma and H be the stored-coordinate operators
of L018, so H=exp(-tau Delta/a²), Sigma=Delta^(-1), and i=3,6.
Let e_k be the ordinary orthonormal Hodge modes and lambda_k their
physical eigenvalues. L028/L062/L064's columns and coefficients are

    v_k=R_F Sigma^(1/2)e_k,
    c_(i;kl)=exp[-tau(lambda_k+lambda_l)]
                      e_k^T Sigma^(1/2)Q_i Sigma^(1/2)e_l.

Here R_F is L026's exact lift, with the upper potential separately
pinned. For a full Hodge input x, define U_mu x on transverse interior
vertices by averaging the positive upper (1,mu) curvature row
(D_1 x)_(N-1,mu) across its two transverse endpoints and dividing by
a². Equivalently this is the same average of L064's r_k when x is
Sigma^(1/2)e_k: D_1 R_F=D_1. Define V_mu x(s,y) by averaging the
mu-link component of R_F x across that direction to the transverse
vertex y at level s and dividing by a. Normal end edges are retained;
all fixed tangential links and boundary vertex evaluations are zero.
These are exact finite maps, with mu=2,3,4 and 1<=s<N.

For two full inputs define the bilinear diagnostic

    P_a(x,z)=a^4 sum_(s,y) u_(a,1)(s,y) (sa)
                           sum_mu (U_mu x)(y)(V_mu z)(s,y).
    D_(i,a)=sum_(k,l)c_(i;kl)
                 P_a(Sigma^(1/2)e_k,Sigma^(1/2)e_l).       (9)

In (9), sa is the physical lower-face-to-level distance. The centering,
the physical distance factor and the normalizations are part of this
diagnostic's definition. In particular the actual two-link paths
are replaced here by averages of their underlying lifted link columns;
we have not bounded that replacement in (1). No angular constant
gamma, color multiplicity, sign or power of N from (1) is assigned to
D_(i,a). Identifying (9) with a leading coefficient would additionally
require the axial embedding normalization, covariance composition,
variable-coefficient and pinned-boundary remainder analysis. L066's
norm obstruction remains; Sigma is still four-dimensional.

Here is an exact finite way to evaluate the full heat sum in (9).
Write P_a(x,z)=x^T M_a z in ordinary coordinates and
M_a^sym=(M_a+M_a^T)/2. Since the coefficient matrix c is symmetric,
substituting its definition and summing the complete mode basis gives

    D_(i,a)=Tr[M_a^sym Sigma H Q_i H Sigma].              (10)

Indeed Sigma^(1/2) commutes with H, and the two exterior factors
Sigma^(1/2), together with those in c, give Sigma on both sides.
All sums are finite. This identity neither changes the regulator nor
transfers a nonlinear polynomial to the Hodge law.

Let xi have independent real Rademacher entries on all stored Hodge
coordinates, so E[xi xi^T]=I exactly. Set

    z=H^(1/2)xi,
    x_R=Sigma z,
    x_L=Sigma H Q_i z.

Then E[x_L x_R^T]=Sigma H Q_i H Sigma. Consequently

    E[(P_a(x_L,x_R)+P_a(x_R,x_L))/2]=D_(i,a).             (11)

This follows directly from finite matrix multiplication and the
second-moment identity; no Gaussian approximation, mode truncation
or interchange of limits is used. Each sample uses both actual Q_i
and the original full relative spectrum. An empirical average of (11)
is still a sample estimate, not an exact evaluation of (10).

The implementation is
`scripts/combined-ward-response/check_first_pair_exterior_heat.py`.
Reproduce with

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_first_pair_exterior_heat.py --samples 16

Its full certificate is
`scripts/combined-ward-response/first-pair-exterior-heat-certificate.json`.
An N=4 one-site geometry (not the admitted displacement) assembles
the incidence Hodge inverse and dense heat operators independently
of the spectral routine. Summing every coordinate column checks
(10) against (11); both probe trace errors are below 5e-18, against
2e-11, and the tested spectral factor errors are below 2e-15, against
2e-11. The bilinear row/matrix check has error below 5e-15 against
9.89e-11. These are floating implementation checks, not interval
certificates or a proof of a sign at an admitted mesh.

For N=24 and 32, all 16 paired samples for each probe are saved, with
seeds 900024 and 900032. Their means (triplet,shear) are respectively
(-180.3972,-24.5679) and (-271.1691,99.3451); estimated sample
standard errors are (60.5287,57.8138) and (69.5446,100.6373).
The triplet samples suggest a negative diagnostic; the shear is
unresolved and changes sampled sign. Standard errors supply no
rigorous probability, sign, zero or continuum-limit statement here.
No asymptotic coefficient, O(N²) bound or logarithm is established.
The completed step is EXPLORATION / RESEARCH / REPRODUCTION: a
defined actual-column diagnostic and a full-spectrum exploratory test,
with no claimed advance beyond the assessed sources or closure of
the direct first pair. The original frozen-symbol result is unchanged.

## Mathlib

Coverage of this full frozen-symbol test: **not checked**. Supporting
finite trace algebra, trigonometric identities, bounded torus
integration, coordinate parity and weighted variance positivity:
**not checked**. No matching theorem or absence claim is asserted.
Coverage of the added finite diagnostic representation and independent
Rademacher second-moment identity: **not checked**.
The ready source assessment is reused. General flow renormalizability
and stress matching are not reproved; the calculation concerns only
the exact endpoint and path specialization not evaluated there.
