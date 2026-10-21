# L173 — The action-Hessian mixed branch has a finite cubic limit

## Hypotheses

Keep L158's exact SU(2) branch T_i for i=3,6, D=(-4,4)^4,
a=8/N through admitted even meshes, all-face relative boundary
conditions, straight direction-1 lower-rooted forest, the complete
compact displacement and actual L010 probes at tau=1/16. Take the
bare expansion at fixed mesh first. Use L018's ordinary-coordinate
full-link residual A, L156's h_k=R v_k and c_(i;kl), and L158's
vertex prefix covariance K and endpoint-sum matrix K^+=S K S^T.
Full-link gauge identities have already been applied in L158's
exact collapse. All action faces, upper jumps, constant modes and
both insertion subtractions retain their original conventions.

In particular the starting identity, including its color factor, is

    T_i=-6 sum_(e,f) A_ef U_(i,fe) K^+_fe,
    U_(i,fe)=sum_(k,l) c_(i;kl) (h_k)_f (h_l)_e.           (1)

The sums are over positive variable links; A has fixed range and
compact interior support. U_i in (1) is one-color. It is not the
color-extended matrix and supplies no further factor three.

## Conclusion

There is a finite real limit

    a^3 T_i -> K_(i,T),                                  (2)

given by the explicit finite-stencil/full-heat functional (8) below.
It retains the displacement derivative, exterior derivative, axial
prefix slope and both residual subtractions. The locally logarithmic
scalar correction is estimated before removal. The functional is
absolutely convergent, but its value, sign and vanishing are unproved.

This is a boundedness-to-existence improvement for this one branch,
not a complete-response limit. L159's V_i still requires a limit and
evaluation, and K_(i,T) itself requires evaluation. In combination
with L157 and L172, complete-response vanishing would require
lim a^3 V_i=6K_(i,R)-K_(i,T). No finer powers/logarithm, compensation
with other jets, interacting reflected error <=c_box/2, continuum
construction or finite positive mass is established. This is local
standard-method REPRODUCTION, without a novelty claim.

## Proof

### 1. Specify the coefficient without taking a limit of an unknown trace

For each output direction mu place a positive edge e at midpoint zero.
Let f run over the fixed union stencil of row e in A, with direction
nu(f) and midpoint offset r_f in lattice units. Enlarge the stencil
by zeros if necessary. All offsets are fixed integers or half-integers.
In this section the stencils are on the infinite grid; only finitely
many entries are used. Physical x denotes the midpoint of an actual
output edge and d(x)=x_1+4.

Use the unscaled incidence D_1, L=D_1^T D_1 and L028's exact centered
clover C and endpoint E maps. For a vertex displacement assignment v,
put

    k[v]=E M_v C D_1,
    (M_v F)_nu=sum_rho v_rho F_(rho nu),
    script A[v]=(L k[v]+k[v]^T L)/2.                     (3)

Here F is extended antisymmetrically from its six plane components,
as in L028. Transposition includes the variable coefficients. For
affine v, (3) means its finite row stencil, not an unbounded operator
claim. Define

    alpha_(mu f)(x)=script A[v_rho(z)=u_rho(x)]_(ef),
    beta_(mu f)(x)=script A[v_rho(z)=sum_j z_j partial_j u_rho(x)]_(ef)
                         -q_(mu f)(x).                  (4)

The coordinates z are vertex offsets from e's midpoint. q is the
row of Q_3+Q_6 in L018(2) with its strain coefficients frozen at x:
use precisely L028's D_1^T W_3 D_1 and D_1^T C^T S C D_1
compositions, with W_3 on plane rho nu equal to w_rho(x)+w_nu(x)
and S the symmetric matrix of the stated shear form. The four-vertex
averaging in W_3 and both clovers in the shear are retained; freezing
the coefficient does not change their incidence stencils. Thus (3)-(4)
specify the adjoint derivative and both subtractions with their signs.

Let g be L158(6)'s infinite three-dimensional scalar Green function.
For endpoints v of f and w of e, now regarded as offsets from zero,
define the two bounded finite-stencil arrays

    W_(mu f)=sum_(v in endpoints f,w in endpoints e) g(v_T-w_T),
    S_(mu f)=sum_(v,w) ((v_1+w_1)/2) g(v_T-w_T).          (5)

Both sums have four terms. The axial offsets in S are not discarded.

For clarity define the one-color physical exterior kernel directly:

    H_(i,nu mu)(x,y)=sum_(k,l) exp[-tau(lambda_k+lambda_l)]
                          b_(i,kl) ell_(k,nu)(x) ell_(l,mu)(y),
    ell_(k,1)=0,
    ell_(k,nu)(x)=lambda_k^(-1/2)
       [f_(k,nu)(x)-integral_(-4)^(x_1) partial_nu f_(k,1)(t,x_T) dt],
                     nu=2,3,4.                         (6)

Here f_k are the L2-normalized real relative modes and b_(i,kl) the
covariance-normalized continuum probe entries, exactly as in L152(5)-(6).
The constant axial cosine mode contributes its actual linear primitive.
L152 section 3 proves uniform C^2 convergence of the finite-mesh
counterpart H_(i,a) on compact two-point sets, with absolutely summable
polynomially weighted full heat bounds. Its use here is justified
because the columns and coefficients are precisely L156(8)'s same
R v_k and covariance-normalized probe, independently of which residual
polynomial is contracted against them. No quartic response theorem
is being assigned to this cubic branch.

Set

    H^0_(i,mu f)(x)=H_(i,nu(f) mu)(x,x),
    H^1_(i,mu f)(x)=sum_j r_(f,j)
                           partial_(x_j) H_(i,nu(f) mu)(x,y)|_(y=x).
                                                               (7)

Only the first argument is differentiated: the output edge e is the
chosen center. The promised answer is

    K_(i,T)=-6 integral_D sum_(mu=1)^4 sum_f [
         d beta_(mu f) W_(mu f) H^0_(i,mu f)
        +d alpha_(mu f) W_(mu f) H^1_(i,mu f)
        +alpha_(mu f) S_(mu f) H^0_(i,mu f)] dx.          (8)

Every row entry, direction, endpoint factor and subtraction in (8)
is specified by (3)-(7). We prove the local covariance comparison
needed to identify (8), rather than assuming convergence of the O(1)
remainder in L158(9).

### 2. The boundary correction to the scalar transverse Green kernel

Write G_N=Delta_0^(-1) on transverse interior vertices, and
b_N(y,z)=G_N(y,z)-g(y-z). On compact interior stencils,

    |b_N(y,z)|<=C/N,
    |b_N(y+one step,z)-b_N(y,z)|<=C/N^2,                 (9)

with the analogous second-argument bound. The first estimate is
L158(7). For the sharper difference we specialize L164 section 2's
heat-image argument to three vertex-Dirichlet coordinates, rather
than four relative edge coordinates. Here are the changed powers
and the boundary/tail details needed for this specialization.

For the infinite three-dimensional heat kernel p_t and j=0,1, its
Fourier symbol lambda=4 sum_(rho=2)^4 sin^2(theta_rho/2) gives

    |partial^j p_t(n)|<=C_m (1+t)^(-(3+j)/2)
                               (1+|n|/sqrt(1+t))^(-m).  (10)

The proof is the same Fourier derivative estimate in L164(6): each
difference contributes one power of theta, the Gaussian integral
now has dimension three, and m integrations by parts contribute
t^(m/2). The bounded-time torus derivatives are bounded. Thus the
dimension change supplies exactly (3+j)/2, with no new projection
or spectral assumption.

The three-dimensional Dirichlet heat kernel has the odd image sum
in all three coordinates. For compact observation and source rows,
each nonidentity image is at distance >=cN(1+|b|), after finitely
many nearest-image choices, b in Z^3. For 0<=t<=N^2 sum (10) over
these images with m>8. In the range 1<=t<=N^2 its integral is
bounded by

    C N^(-m) integral_1^(N^2) t^((m-3-j)/2) dt
      <=C N^(-1-j);

the range t<=1 is smaller. For t>=N^2 the complete Dirichlet mode
sum and its one-difference sum are bounded respectively by
C N^-3 exp(-ct/N^2) and C N^-4 exp(-ct/N^2). To see this, use
normalized sine entries <=C N^-3/2, a difference factor <=C|q|/N,
lambda_q>=4|q|^2/N^2, and the full Gaussian shell sum; every index
is positive. Their integrated tails are C/N and C/N^2. Infinite
tails from (10) have the same powers. Subtracting the identity heat
image proves (9); symmetry gives differences in either argument.
Every transverse boundary condition and low mode remains included.

Choose a reference vertex v_e within a bounded distance of e's
midpoint, and let y_e be its transverse part. All endpoints in a
row stencil are interior for sufficiently large N. Write j_e for
the axial lattice coordinate of e's midpoint and
b_e=b_N(y_e,y_e). A bounded path of single steps in both arguments
of (9) gives, uniformly on that stencil,

    min(s,t)G_N(y,z)
      =j_e g(y-z)+(min(s,t)-j_e)g(y-z)+j_e b_e+O(N^-1).
                                                               (11)

Here |min(s,t)-j_e| is bounded, |b_e|<=C/N and j_e<=N.
The spatially varying physical-boundary correction has become a
local scalar plus a vanishing error, not a discarded global kernel.

### 3. Local differences of the logarithmic prefix correction converge

L158(5) gives K(v,w)=min(s,t)G_N(y,z)-F_N(v,w), where
F_N=R_st(Delta_0)G_N. Its exact double heat representation is

    F_N((s,y),(t,z))=
       integral_0^infty integral_0^infty
           h^D_v(s,t) p^D_(v+w)(y,z) dw dv.              (12)

For each finite N the integrals converge by the positive Dirichlet
gaps. This is the commuting resolvent product, not a change of the
prefix endpoints or an omission of the axial edge constant mode
which was used in the exact identity for K.

The normalized finite sine expansions give, uniformly in all rows,

    |h^D_v|<=C(1+v)^(-1/2),
    |partial h^D_v|<=C(1+v)^(-1),
    |p^D_z|<=C(1+z)^(-3/2),
    |partial p^D_z|<=C(1+z)^(-2).                       (13)

For example the axial differentiated sum is bounded by
C N^-2 sum_(q>=1) q exp(-4v q^2/N^2); the transverse one by
C N^-4 sum_(r>=1) r^3 exp(-c z r^2/N^2). For times >=1 these
give the indicated powers, including times above N^2 by extracting
their positive gap exponential. For times <=1 the finite-range
difference and heat operator norms suffice. The undifferenced sums
are obtained by dropping the frequency factor. Infinite versions
follow from the corresponding Fourier integrals.

Changing one axial endpoint in the integrand of (12) is consequently
bounded by C(1+v)^-1(1+v+w)^(-3/2); changing one transverse endpoint
is bounded by C(1+v)^(-1/2)(1+v+w)^-2. Both are integrable on the
whole quadrant: integrate w first, obtaining C(1+v)^(-3/2).
These bounds are uniform in N. They also apply to either argument
and to the infinite kernels. Thus finite chains of bounded-offset
differences have a common integrable majorant.

Let h_v be the infinite one-dimensional heat kernel. Define for
each fixed integer displacement r=(r_1,r_T)

    f(r)=integral_0^infty integral_0^infty [
        h_v(r_1) p_(v+w)(r_T)-h_v(0) p_(v+w)(0)] dw dv. (14)

This is an absolutely convergent integral of the displayed difference;
neither unsubtracted term is assigned a finite double integral. A
bounded chain of coordinate steps and (13) proves convergence. It
also shows f(-r)=f(r), since both infinite heat kernels are even.

With alpha_e=F_N(v_e,v_e), we have uniformly for every supported
stencil and every endpoint pair

    F_N(v,w)-alpha_e=f(v-w)+o(1).                        (15)

To justify uniformity, join the two arguments to (v_e,v_e) by a fixed
bounded number of steps. On any compact rectangle in the two heat
times, each finite heat kernel converges uniformly to its infinite
kernel on these rows. This follows directly by approximating the
exponential of the bounded finite-range Laplacian with a polynomial:
any fixed-degree polynomial has exactly the infinite local entries
once the distance to all boundaries exceeds its range, and the
operator-norm Taylor tail is uniform in N and in bounded heat time.
Every center has distance >=delta N from the faces. Apply this to
each difference in the finite chain, then remove the time rectangle
using the two integrable majorants. The infinite differences telescope
to (14), including when v_e depends on the edge direction. This
proves (15), with no rate required. L158(8) retains
|alpha_e|<=C(1+log N).

### 4. Separate the scalar, even and slope pieces before cancellation

For endpoints v,w as offsets from e's midpoint, put

    E_(mu f)=sum_(v,w) [-|v_1-w_1| g(v_T-w_T)/2-f(v-w)],
    eta_e=j_e b_e-alpha_e.

Equations (11),(15) and min(s,t)-j_e=
(v_1+w_1)/2-|v_1-w_1|/2 give the local comparison

    K^+_fe=j_e W_(mu f)+4 eta_e+S_(mu f)+E_(mu f)+o(1),
    |eta_e|<=C(1+log N).                                (16)

The o(1) is uniform on all the stencils. W,S,E are fixed bounded
arrays. All four endpoint pairs have been summed. In particular
the logarithmic part is not being absorbed into the o(1).

The scalar contribution in (1) sums exactly in f as

    sum_f A_ef U_(i,fe)=sum_(k,l) c_(i;kl) (h_l)_e (A h_k)_e.

L156's smooth residual bound |A h_k|<=C a^5 p(k), the compact
interior bound |h_l|<=C a p(l), and the complete heat sum show that
its total contribution multiplied by eta_e is O(a^2 log(eN)).
Indeed there are O(a^-4) rows and each exterior product is O(a^6).
Multiplication by a^3 therefore makes it vanish. No eta_e is moved
through A; it may vary with every row. The uniform o(1) in (16)
likewise contributes o(a^-3), since |A_ef|<=C/a, |U_(i,fe)|<=C_i a^2
and each row has bounded size.

Next use the whole frozen principal row alpha from (4). L158(15)-(16)
prove that its centered Fourier symbol is imaginary and odd, with
every endpoint/clover filter retained. Equivalently its real row
coefficients change sign under f -> f^iota, inversion about the
midpoint of e, separately for each component nu(f). The simultaneous
positive-edge orientation changes introduce two minus signs in the
bilinear row and hence no extra sign. Both W and E are even under
this permutation: the endpoints of e are interchanged, those of f
are reflected, g and f are even, and |v_1-w_1| is unchanged. Therefore
for every constant component array H_(nu mu),

    sum_f alpha_(mu f) W_(mu f) H_(nu(f) mu)=0,
    sum_f alpha_(mu f) E_(mu f) H_(nu(f) mu)=0.           (17)

These are finite-stencil identities. The first is also precisely
L158's stationary cancellation. The second uses the convergent
subtracted potential (14), not a divergent Fourier principal value.
S is odd under inversion and is not removed by (17).

### 5. Keep all first-order terms and pass to the physical integral

For finite a define alpha_a by freezing u_a at x in (3). Let beta_a
use its first derivatives and the frozen w_a,s_a in (4). L028 proves
uniform C^r coefficient convergence with O(a^2) error, and the exact
finite-stencil generator is a^-1 k[u_a]. Taylor expansion on its
complete row and on the bounded insertion stencils gives uniformly

    A_ef=a^-1 alpha_(a,mu f)(x)+beta_(a,mu f)(x)+O(a),
    alpha_a -> alpha,             beta_a -> beta.         (18)

This expansion includes coefficient samples in the transposed
generator; replacing it by only the untransposed row would miss part
of beta. No strain derivative enters at order one from Q_3+Q_6:
their coefficient variation across a bounded stencil is O(a).

Use H_(i,a) from section 1 and set H_a^0,H_a^1 as in (7) with that
kernel. The actual link samples and uniform C^2 control in L152 give

    U_(i,fe)=a^2[H^0_(a,i,mu f)(x)+a H^1_(a,i,mu f)(x)+O_i(a^2)],
    H_a^0 -> H^0,                  H_a^1 -> H^1,          (19)

uniformly on the support. This preserves both component indices and
the actual lower primitive. There is no assumed first-order rate
for the probe matrix b_(i,kl,a).

Apply the first identity of (17) with alpha_a and H_a^0, so the
leading j_e=a^-1 d(x) contribution cancels exactly at every mesh.
Equations (18)-(19) leave in the stationary part, per row,

    a d(x) sum_f W_(mu f)
        [beta_(a,mu f) H^0_(a,i,mu f)
                        +alpha_(a,mu f) H^1_(a,i,mu f)]+O_i(a^2).
                                                               (20)

For the E part use the second identity of (17). Replacing A by its
principal row costs O(1) times O(a^2), and replacing U by its frozen
value costs O(a^-1) times O(a^3). Thus its remaining contribution is
O_i(a^2) per row. For the slope part no cancellation is asserted:
its per-row value is

    a sum_f alpha_(a,mu f) S_(mu f) H^0_(a,i,mu f)+O_i(a^2).
                                                               (21)

The scalar and uniform little-o errors have already been controlled
in section 4. There are O(a^-4) compact supported rows. Multiplying
(20)-(21) by a^3 turns their leading sums into a^4-weighted Riemann
sums and their O(a^2) errors into O(a). For each of the four output
directions there is one positive edge per shifted vertex cell; no
additional orientation, volume or color factor appears. Uniform
convergence in (18)-(19) and compact support therefore identify the
limit as (8), with the -6 in (1) applied once. This proves (2).

The heat sum and its differentiated versions are absolutely convergent
by L152's uniform polynomial/exponential majorants. All other sums
are finite and all coefficients have compact support. Consequently
the integral in (8) is finite, real and absolutely convergent. No
upper-face extension of the forest columns is assumed: the original
upper/action faces were retained in L158's exact collapse, and only
then did compact support restrict the two residual edge indices.

The checks for this analytic step are the exact residual/endpoint
normalizations, the two integrable double-heat majorants, finite-row
parity, and the error comparison o(a^-3)+O(a^-2)+O(a^2 log(eN))
against a^-3. There is no numerical coefficient or new certificate
claim. A signed evaluation of the three terms in (8), together with
an independent treatment of V_i, remains necessary to decide the
complete-response question.

## Mathlib

Full matching result and supporting scalar lattice heat/image coverage:
**not checked**; unknown is not absence. The finite spectral theorem,
Fourier heat representation, dominated convergence, Taylor expansion
and compact-support Riemann integration are standard methods. L164's
existing heat argument is specialized with the three-dimensional
Dirichlet powers explicitly verified in (9)-(10); it is not an imported
unread boundary theorem. L152's established exterior convergence is
reused with its exact normalization. The subtracted potential analysis
is needed because the undifferenced double integral is logarithmically
divergent and cannot be replaced by a bounded covariance correction.
The unchanged [assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md)
covers this isolated cubic-response attempt and supplies no ready
isolated-jet theorem in place of this specialization.
