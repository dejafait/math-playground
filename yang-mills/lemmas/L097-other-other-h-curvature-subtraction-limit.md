# L097 — A signed limit for the H diagonal's curvature subtraction

## Hypotheses

Use precisely L095's R_H,Q for SU(2), both actual L010 probes i=3,6,
L018's residual, the straight lower-rooted direction-1 forest, relative
all-face pinned box D=(-4,4)^4, admitted even N, a=8/N and tau=1/16.
Take the bare small-coupling coefficient at fixed mesh before refinement.
Coordinates and norms are ordinary dimensionless stored coordinates.
Keep every interior level, pinned transverse row, ordered plaquette pair
including coincidences and exterior heat mode. No generator term is
included in the curvature subtraction below.

Import L085/L091's K_g=M tensor P, M_st=min(s,t), K_h=R Qcal,
R=(L_D tensor I+I tensor Delta_T)^(-1), and L088's complete Omega_k
and real symmetric heat coefficients c_(i;kl,a). Here P is the full
relative transverse gradient projection and Qcal=I tensor (I-P).
In this file A_k=Pcal Omega_k Qcal is the unwhitened alternating block
of L095, not L091's whitened gradient/gradient block.

Let Cc=I tensor D_T denote transverse circulation; write D_T=D in the
transverse cochain notation. To avoid confusing this with the box D,
use D_T in formulas below. Define the level-diagonal rectangular map

    Zeta_k=M_(b_k) Bq-M_(q_k) Bb,
    S_T=D_T Delta_T^-1 D_T^T.                         (1)

Zeta_k maps transverse links to transverse plaquettes at each level.
S_T is the orthogonal projection onto im D_T. Use the actual stored
curvature multiplier M_0 from L008, so that

    Q_0=Q_3+Q_6=D_1^T M_0 D_1,
    ||M_0||<=C.                                      (2)

Thus the triplet retains its average of squares and the shear its two
clover factors. Let M_T(s) be M_0 restricted on both sides to transverse
curvatures at level s. These restrictions are level diagonal: the
clover of a transverse plane shifts only its two transverse coordinates.

## Conclusion

There is a finite real signed functional K_(i,Q) such that

    a^3 R_H,Q -> K_(i,Q),                             (3)

for both actual probes. A controlled finite-trace reduction is

    R_H,Q=sum_(k,l)c_(i;kl,a) sum_(s=1)^(N-1) s
        Tr_T[P Zeta_k(s)^T S_T M_T(s) S_T Zeta_l(s) P]
        +O_i(N^(27/10)).                             (4)

In particular the scaled error in (4) is O_i(N^(-3/10)). The full
min(s,t) is used to justify (4); it is not replaced by a local covariance
as an assumption. Both co-closed covariance factors and all strains
in the original subtraction are retained until that reduction.

Here is an explicit continuum formula for the limit. For a continuum
relative normalized mode f_k with physical eigenvalue nu_k, put, for
nu=2,3,4,

    v_(k,nu)(x)=[f_(k,nu)(x)
       -partial_nu integral_(-4)^(x_1) f_(k,1)(t,x_T) dt]/sqrt(nu_k).

Missing components of a component-labeled mode are zero. This is the
interior lower-rooted prefix limit; it does not redefine the pinned
upper-face potential. Put

    c_(i;kl)=exp[-tau(nu_k+nu_l)] (B_i^rel)_kl,

where B_i^rel is L008's bounded continuum whitened curvature form.
For theta in [-pi,pi]^3, indexed by 2,3,4, write

    d_j=2 sin(theta_j/2), eta_j=cos(theta_j/2),
    lambda=sum_(j=2)^4 d_j^2, P(theta)=d_T d_T^T/lambda,
    C_(mu nu)(theta)=i(-d_nu e_mu^T+d_mu e_nu^T),
    S(theta)=C(theta) C(theta)^*/lambda.

C has the three rows (23),(24),(34). At lambda=0 set P=S=0; this
measure-zero choice does not affect the integral. In each plane use
the exact two-edge path symbols

    b_(mu nu)=(eta_nu-i d_nu/2)e_mu^T
                              +(eta_mu+i d_mu/2)e_nu^T,
    q_(mu nu)=(-eta_nu-i d_nu/2)e_mu^T
                              +(eta_mu+i d_mu/2)e_nu^T.

Define the three-by-three row matrix z_v by

    (z_v)_(mu nu)=(v_mu+v_nu)q_(mu nu)
                                      -(v_nu-v_mu)b_(mu nu).

Let W_T(x) be diagonal with entries w_mu+w_nu, let C_T(theta) be
diagonal with entries eta_mu eta_nu, and define the real symmetric
S_6,T(x) by restricting L008's shear form to transverse curvatures:

    F^T S_6,T F=sum_(2<=mu<nu<=4) s_(mu nu)
                                  sum_(alpha=2)^4 F_(mu alpha)F_(nu alpha).

Antisymmetric extension of F and zero diagonal entries are understood.
The frozen multiplier is the actual stencil symbol

    m_T(x,theta)=W_T(x)+C_T(theta)^* S_6,T(x) C_T(theta).

Then

    K_(i,Q)=sum_(k,l)c_(i;kl) integral_D (x_1+4)
      integral_([-pi,pi]^3) Tr[P z_(v_k)^* S m_T S z_(v_l) P]
                                        dtheta/(2pi)^3 dx.             (5)

The series is absolutely convergent. Its value and sign are not
evaluated. R_H contains this term with a minus sign (L095); (3) is
the limit of the positive-definition subtraction R_H,Q itself. This
does not prove the limits of R_H,ax, R_H,tr, R_R or the other remaining
traces, nor their required joint value -4 gamma D_i before factor 3.
No complete other/other limit or compensation with -12 gamma D_i is
claimed. Other jets, N^2 remainders, slower powers/logarithm, matching,
interacting error <=c_box/2, continuum axioms, reflection positivity,
infrared control and finite positive mass remain open.

## Proof

### 1. Factor the actual subtraction through full curvature rows

In stored coordinates x=aA, the factors a^4 and the two physical
curvatures D_1 x/a^2 cancel. Thus L008's exact quadratic forms give
(2), with no extra power of a. Its boundedness is L008's polarization
and clover/Jensen bound. L090(3), on the full relative cochains, gives
Sigma E_h^T=I K_h, where I embeds the transverse interior links with
component 1 zero. Therefore L089's insertion is exactly

    V_curv=K_h I^T D_1^T M_0 D_1 I K_h.               (6)

Let G_st=1_(t<=s) P, for 1<=s,t<N. It is an exact (possibly redundant)
Brownian-increment factor: GG^T=K_g. Set

    X_k=D_1 I K_h A_k^T G.

Cyclicity of the finite trace gives

    R_H,Q=sum_(k,l)c_(i;kl,a) Tr(X_k^T M_0 X_l).       (7)

This factorization retains the actual signs, not a positive bound for
a signed probe. All row maps and projections are fixed after the tilt
derivatives; no base-law zero has been differentiated away.

L089's split Omega_k=F_k+Zeta_k^T Cc-Cc^T Zeta_k and Cc Pcal=0 imply

    A_k=Pcal F_k Qcal+Pcal Zeta_k^T Cc Qcal.

The second summand transposes to Qcal Cc^T Zeta_k Pcal. Consequently

    X_k=X_(k,F)+B Y_k,
    Y_k=Zeta_k G,
    B=D_1 I R (I tensor D_T^T).                       (8)

Here R D_T^T already lies in the co-closed space. All original
co-closed covariance factors survive (6)--(8).

L088/L090's complete exterior estimates give, for one fixed polynomial p,

    ||F_k||<=C a^2 p(k), ||Zeta_k(s)||<=C a p(k),
    ||Zeta_k(s+1)-Zeta_k(s)||<=C a^2 p(k).             (9)

The last estimate applies to existing neighboring levels, including
N-2,N-1. It follows from the actual prefix formula, not smoothness
across the upper pin. The finite selectors have bounded multiplicity.
L086's spectrum gives Tr K_h<=C N^4, and on its range
I^T D_1^T D_1 I=Delta_E=L_D+Delta_T. Hence

    ||D_1 I K_h||_HS^2=Tr K_h<=C N^4,
    ||G||<=C N,
    ||X_(k,F)||_HS<=C p(k) N.                         (10)

Thus the actual exterior-circulation terms are retained and estimated,
rather than omitted by freezing.

### 2. Differentiate the full prefix factor, including both endpoints

Let D_v be axial incidence from interior vertex levels to all N axial
edges, with zero values at levels 0,N, so D_v^T D_v=L_D. Since the
increments in G are orthogonal before P, the exact row-block traces are

    ||Y_k(s)||_HS^2=s ||Zeta_k(s)P||_HS^2,

and, for 1<=s<N-1,

    ||Y_k(s+1)-Y_k(s)||_HS^2
      =s ||[Zeta_k(s+1)-Zeta_k(s)]P||_HS^2
                                    +||Zeta_k(s+1)P||_HS^2.           (11)

These equalities directly use M_st=min(s,t). The two endpoint
differences have squared norms ||Y_k(1)||_HS^2 and ||Y_k(N-1)||_HS^2.
The second is allowed to be nonzero. With rank P=(N-1)^3 and (9),

    ||Y_k||_HS^2<=C p(k)^2 a^2 N^5<=C' p(k)^2 N^3,
    ||D_v Y_k||_HS^2
      <=C p(k)^2 [a^4 N^5+a^2 N^4]
      <=C' p(k)^2 N^2.                               (12)

The upper zero-extension jump contributes at most Ca^2 N^4, already
included in (12). It is not suppressed using an interior Taylor
estimate or replaced by a smooth upper boundary condition.

### 3. A uniform axial-static comparison with a singular-mode estimate

Let E_T embed transverse plaquettes into the full relative curvature
space and put B_0=E_T (I tensor S_T). By the relative cochain identity
D_T^T D_T=Delta_T(I-P), S_T^2=S_T=S_T^T, so ||B_0||<=1.

Here is the exact spectral comparison. Choose a transverse co-closed
edge eigenvector e with Delta_T eigenvalue lambda>0; the matching unit
curvature vector is D_T e/sqrt(lambda). On an axial L_D eigenvector
with eigenvalue mu, B has transverse-curvature component
lambda/(mu+lambda) and axial-curvature component of norm
sqrt(mu lambda)/(mu+lambda). These components are orthogonal. B_0
has transverse component 1 and axial component zero. Thus

    ||B||<=1, ||B-B_0||<=1,
    (B-B_0)^*(B-B_0)=mu/(mu+lambda)                    (13)

on this joint input mode. Both maps vanish on ker D_T^T. This argument
uses all axial Dirichlet modes and their endpoint edge differences.

Let Pi_eta select transverse curvature modes in im D_T with lambda<=eta.
The full transverse tensor spectrum in L086/L095 has lambda>=4|m|^2/N^2
and at most C r^2 labels in shell max_j m_j=r, including all component
multiplicities. Via D_T, this bounds the curvature-mode count as well:

    rank Pi_eta<=C N^3 eta^(3/2),                     (14)

for eta=N^(-2/5) and all sufficiently large N. More generally it holds
when N sqrt(eta)>=1, with a changed absolute constant. It follows from
(11)'s first equality and the rank bound, without commuting a multiplier,
that

    ||Pi_eta Y_k||_HS^2
      =sum_s s ||Pi_eta Zeta_k(s)P||_HS^2
      <=C p(k)^2 N^3 eta^(3/2).                       (15)

On lambda>eta, (13) bounds the squared error by mu/eta; transverse
spectral projections commute with D_v. Combining (12),(13),(15) gives

    ||(B-B_0)Y_k||_HS^2
       <=C p(k)^2 [N^3 eta^(3/2)+eta^-1 N^2]
       <=C' p(k)^2 N^(12/5),                          (16)

using eta=N^(-2/5). No low transverse covariance mode is discarded
from the original trace. This cutoff is solely an error estimate.

Set X_(k,0)=B_0 Y_k. Equations (8),(10),(12),(16) prove

    ||X_k-X_(k,0)||_HS<=C p(k) N^(6/5),
    ||X_k||_HS+||X_(k,0)||_HS<=C p(k) N^(3/2).        (17)

Bound the difference of the pairings in (7) using ||M_0||<=C and
Hilbert--Schmidt Cauchy--Schwarz. Its bound is
C p(k)p(l) N^(27/10). The full heat sum from L088/L090 makes this
O_i(N^(27/10)), with both exterior orientations retained.

Since X_(k,0) has only transverse curvature rows, M_0 restricts to M_T.
Every remaining map except G is level diagonal. Cycling GG^T=K_g in
the static pairing therefore selects its exact diagonal block sP.
This proves (4). The off-diagonal prefix has disappeared only after
the quantitative full-resolvent comparison (16)--(17).

### 4. Justify the transverse finite-trace limit before freezing

It suffices first to fix k,l. Write zeta_(k,a)=Zeta_k/a; its norm and
existing-neighbor coefficient differences are bounded by Cp(k) and
Ca p(k). Divide (4)'s static expression by a^-3 to obtain

    a^4 sum_s (a s) Tr_T[
       P zeta_(k,a)(s)^T S_T M_T(s) S_T zeta_(l,a)(s) P].              (18)

This normalization retains the physical lower-face distance a s=x_1+4.

For epsilon>0 regularize only the two transverse projections:

    P_epsilon=T(Delta_0+epsilon I)^-1 T^T,
    S_epsilon=D_T(Delta_T+epsilon I)^-1 D_T^T.

They are contractions. Their nonzero eigenvalues are lambda/(lambda+
epsilon). The same three-dimensional shell sum used in L095 gives
Tr Delta_0^-1+Tr Delta_T^-1<=C N^3. Since
[epsilon/(lambda+epsilon)]^2<=epsilon/lambda, their errors satisfy

    ||P-P_epsilon||_HS+||S_T-S_epsilon||_HS
                                               <=C N^(3/2) sqrt(epsilon).

In each product in (18), telescope all projection occurrences. The
other normalized factors have norm <=C p(k)p(l), and their ambient
dimension is O(N^3). Trace Cauchy--Schwarz therefore bounds the
per-level trace error by C p(k)p(l) N^3 sqrt(epsilon). Since
a^4 sum_s a s N^3<=C, the total error is
C p(k)p(l) sqrt(epsilon), uniformly in N. No variable strain or path
coefficient is commuted through either projection.

For fixed epsilon, approximate each inverse uniformly by a polynomial
on [0,12]. For t>0 an explicit degree-m choice for 1/(x+t) is

    p_(t,m)(x)=(1/(12+t)) sum_(j=0)^m [1-(x+t)/(12+t)]^j,
    sup_(0<=x<=12)|p_(t,m)(x)-1/(x+t)|
                                      <=(12/(12+t))^(m+1)/t.

Multiplying the geometric sum by x+t proves the error. The finite
spectral theorem and ||T||,||D_T||<=sqrt(12) give uniform operator
approximations to P_epsilon,S_epsilon. Telescoping (18) now bounds the
normalized trace error by C_(epsilon) p(k)p(l) times the inverse
approximation error, uniformly in N.

For fixed polynomial degrees the trace consists of a fixed finite
number of closed lattice walks. A collar of that fixed index width
has O(N^2) transverse rows per level. Bounded entries make its possible
contribution to (18) O(a^4 N^2 sum_s a s)=O(1/N); all such rows are
therefore controlled, not deleted from the actual trace. The strain
support is compact in the box, which also ensures that nonzero
multiplier stencils eventually use their interior formulas.

In the other rows, freeze all coefficients at a common cell point.
Their changes over any fixed-range walk are O(a p(k)p(l)); staggered
midpoint offsets have the same bound. L028's exact prefix formula
and relative mode normalization show, for each fixed k,
v_(k,a)/a -> v_k uniformly on the interior transverse rows. To verify
this convergence, divide its finite prefix differences by a, use the
smooth product modes and their physical eigenvalue convergence, and
apply the Riemann-sum theorem to the prefix integral. The same argument
gives the existing-neighbor bounds (9). It does not extend the interior
prefix through the pinned upper potential. The weights w_a,s_a tend
uniformly to the stated smooth strains. Thus the finite polynomial
trace in (18) converges by Riemann sums to the integral of its frozen
Fourier trace, with physical weight x_1+4.

Send polynomial degrees to infinity at fixed epsilon, using the uniform
trace errors just proved. Then send epsilon to zero. On the torus,
the projection symbols are d_T d_T^T/(lambda+epsilon) and
C C^*/(lambda+epsilon). They converge almost everywhere to P,S and
are uniformly bounded. The frozen path and strain factors are bounded,
so ordinary dominated convergence identifies the unregularized torus
integral. Together with the O(sqrt(epsilon)) finite-trace error, this
proves the fixed-k,l limit. This ordering proves the finite-to-frozen
passage; it is not an inference from a frozen value alone.

### 5. Identify the actual symbols and retain the full exterior sum

L088(11) gives exactly the stated b,q,C symbols. At a common frozen
point the signed exterior path sums divided by a are v_mu+v_nu and
v_nu-v_mu. Hence (1) has symbol z_v. Its imaginary parts are retained;
equivalently L088(12) gives z_v=2r_v+v_mu C plane by plane. In particular
C P=0, but there is no assumption that a variable zeta commutes with P.

For the triplet, frozen four-vertex averaging of its weight leaves
w_mu+w_nu on the curvature square. For the shear, its clover in each
plane is eta_mu eta_nu on both sides of its symmetric strain matrix.
Setting the axial curvature inputs to zero leaves exactly S_6,T as
defined above, even for strain terms involving index 1: those terms
vanish because they contain an axial curvature. This proves the
specified m_T, preserving the average-of-squares/clover distinction.
The frozen trace of (18) is therefore the k,l integrand of (5).

For every k,l both the normalized finite trace and its limiting
integral are bounded by C p(k)p(l). The exterior coefficients obey a
uniform summable majorant

    |c_(i;kl,a)| p(k)p(l)
      <=C p(k)p(l) exp[-(tau/16)(|k|^2+|l|^2)],

using L008's whitened form bound and the relative physical spectral
lower bound. Modes not admitted at a given mesh are extended by zero.
For each fixed pair their coefficients converge to c_(i;kl), by L008's
fixed-mode form convergence. Thus uniform heat tails, followed by
finite-pair convergence, justify passing the full sum through the limit.
They also justify (17)'s error sum and absolute convergence of (5).
The original traces are real and c is symmetric, so the limit is real;
no sign is inferred from this fact or from the indefinite strains.

This is one RESEARCH / REPRODUCTION attempt under the unchanged ready
EXPLORE assessment `drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The finite contraction and curvature forms are imported; the proof
specializes the existing spectral, prefix and finite-range trace methods
to the previously unevaluated curvature subtraction. It is local
progress without a claim of originality beyond the checked sources.
No numerical value or certificate is used. Any later comparison with
D_i retains L082's saved-table/IEEE qualifications through L084.

## Mathlib

Full matching limit theorem: **not checked**. Supporting finite spectral
decomposition, trace ideals, geometric sums, Riemann sums and dominated
convergence coverage: **not checked**. Unknown availability is not
absence. No continuum flow/Ward theorem assigns this isolated group's
cutoff coefficient.
