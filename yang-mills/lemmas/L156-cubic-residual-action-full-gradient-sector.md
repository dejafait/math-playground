# L156 — The full-lift two-gradient sector is subleading

## Hypotheses

Keep L155's SU(2) box, admitted even meshes a=8/N, straight lower-rooted
forest, both actual L010 probes at tau=1/16, and fixed-mesh expansion
before refinement. Retain the complete compact displacement, both
insertion subtractions and every action plaquette. Use full variable
link coordinates, including forest links, until the contraction below.
Fixed boundary links are omitted and vertex potentials vanish on every
physical face. All transposes and norms are ordinary stored-coordinate
ones. The color bracket in t_c=i sigma_c/2 is minus the vector cross
product, with the inner product -2 Tr.

Write L=D_1^T D_1, Sigma=(L+D_0 D_0^T)^(-1), R=I-D_0 Phi as in
L018 and L026. Here (D_0 phi)_e=phi(head e)-phi(tail e), and Phi z
is the lower axial prefix, separately set to zero at boundary vertices.
Thus R includes the upper pinned jump. Let A be L018's full quadratic
residual matrix; A D_0=L D_0=0.

Let script R_3 and script S_3 be the degree-three Taylor polynomials
of L011's full gauge-invariant residual B(U) and full Wilson action,
before restricting to the forest. Their symmetric trilinear tensors
are T_R,T_S, normalized by script R_3(x)=T_R(x,x,x), and similarly
for S. Their restrictions are exactly r_1,S_3 in L155. Their quadratic
terms are sum_c (x^c)^T A x^c and (1/2) sum_c (x^c)^T L x^c.

Define the following one-color full-link matrices:

    C=R Sigma R^T,       U_i=R Sigma B_i Sigma R^T,
    K=Phi Sigma Phi^T,   C_g=D_0 K D_0^T,       E=C-C_g.       (1)

The matrix B_i is L018's actual flowed probe. For either matrix C or
C_g, put a hat on it to mean its three-color diagonal extension.
Define precisely one sector of the complete contraction:

    H_i^gg=-36 sum_(alpha,beta,gamma,delta,epsilon,zeta)
       (T_R)_(alpha beta gamma) (T_S)_(delta epsilon zeta)
       (hat U_i)_(alpha delta) (hat C_g)_(beta epsilon)
       (hat C_g)_(gamma zeta).                              (2)

Indices here combine full variable links and colors. In particular
this definition does NOT first discard tensor entries on forest links.
Those entries give zero with C but may not give zero with C_g.

## Conclusion

For each actual probe there is a constant independent of a such that

    |H_i^gg| <= C_i,       a^3 H_i^gg -> 0,       i=3,6.       (3)

This is a sector in the exact full-link expansion of L155, obtained by
replacing both direct rough covariance lines by C_g. The remaining
terms replace them by (C_g,E), (E,C_g) and (E,E). No bound or scaled
limit for that remaining signed sum, or for the complete response,
is proved here. E need not be positive and is not independent noise.
In particular (3) is not a projection statement for the surviving
forest-coordinate tensors, nor a termwise transfer of r_1 to a Hodge
Gaussian. No compensation coefficient, finer power/logarithm bound,
interacting reflected error <=c_box/2, continuum theory or mass follows.

The useful mechanism is a full gauge-jet identity followed by the
actual residual's smooth-column consistency, rather than an absolute
bound on growing raw link covariances. It specializes standard finite
Taylor and Gaussian matrix estimates; no originality beyond the
sources checked in the unchanged assessment is asserted.

## Proof

### 1. Full contraction and the exact gauge identity

L155's 36 connected pairings apply unchanged to the full-link tensors:
full-link forest covariance C has zero forest rows, and restricting its
Gaussian to the remaining coordinates gives precisely the original
law. Thus the complete H_i=-kappa(f_(i,0),r_1,S_3) is (2) with C in
place of C_g. The coefficient is -36 with the actual combined-color
Taylor tensors; L155's +3 instead factors their color and action
normalizations out. Multilinearity in its two direct covariance lines
makes (1)--(2) an exact four-term decomposition. This argument does
not differentiate a base-law zero or change the probe covariance.

Consider any smooth pinned-gauge-invariant scalar F with F_0=F_1=0,
F_2(x)=sum_c (x^c)^T A_F x^c and F_3(x)=T_F(x,x,x). Here A_F is
symmetric and annihilates D_0; this temporary notation is not L018's
restricted residual matrix. Apply the gauge transformation

    U_e -> exp(-t phi(tail e)) U_e exp(t phi(head e)).

The first two orders of the exponential-coordinate tangent are

    D_0 phi + (1/2)[x_e,phi(tail e)+phi(head e)] + O(x^2).

For example expand the two products and log through degree two; this
is the finite degree-two Baker--Campbell--Hausdorff identity. Taking
the homogeneous degree-two part of the exact gauge derivative gives

    3 T_F(x,x,D_0 phi)
       =-<A_F x,[x,phi_tail+phi_head]>.                     (4)

Brackets on links are taken edgewise; the inner product sums links
and colors. Polarize x=h+s D_0 psi in (4). The term with A_F D_0 psi
is zero, so

    6 T_F(h,D_0 phi,D_0 psi)
       =-<A_F h,[D_0 psi,phi_tail+phi_head]>.               (5)

The apparent asymmetry in phi,psi is harmless: the difference of the
two bracket fields is 2 D_0[psi,phi], annihilated in this pairing.
This also follows from the symmetric left side. Boundary vertices
have phi=psi=0, so the gauge transformation preserves all fixed links;
(4)--(5) retain every normal end edge with no boundary integration.

L011 supplies gauge invariance of both the full residual B and the
full action. Apply (5) with A_F=A and A_F=L/2 respectively. Both
residual insertion subtractions are already included in A. Neither
the force/vector summand separately nor a masked gradient is used.

### 2. Exact prefix-potential covariance, with all endpoints retained

Let G be the inverse of the unscaled three-dimensional scalar
Dirichlet Laplacian Delta_0 on transverse interior vertices. For
s,t=1,...,N-1, L026's component-1 Hodge spectrum and L085(7)--(8)'s
finite prefix calculation give the exact blocks

    K_st=[min(s,t) I-R_st(Delta_0)] G,
    R_st(lambda)=[(L_D+lambda I)^(-1)]_st.                 (6)

To check the specialization, Phi sums component-1 links below s;
these have the axial edge Neumann Laplacian L_E and transverse
scalar Dirichlet Laplacian Delta_0. The prefix vectors h_s satisfy
h_s^T h_t=min(s,t), B_0 h_s=-e_s, and
lambda(L_E+lambda I)^(-1)=I-B_0^T(L_D+lambda I)^(-1)B_0.
Sandwich this identity with h_s,h_t on each transverse eigenmode.
It yields (6), retaining the constant axial edge mode. Boundary
potential values are exactly zero; they are not extra rows of K.

Put M_st=min(s,t). The subtracted array in (6) is the positive
operator (L_D tensor I+I tensor Delta_0)^(-1)(I tensor G).
Its two factors commute. As K is a covariance,

    0 <= K <= M tensor G.

For positive finite matrices X<=Y, Tr X^2<=Tr Y^2: indeed
Tr(Y^2-X^2)=Tr((Y-X)(Y+X))>=0. Hence

    ||K||_HS^2 <= Tr(M^2) Tr(G^2) <= C N^8.               (7)

Here Tr M^2=sum_(s,t) min(s,t)^2<=N^4. The full transverse spectrum
has lambda_k>=4|k|^2/N^2 for k in {1,...,N-1}^3. Shells max k_j=m
have at most 3m^2 entries. Therefore

    Tr G^2 <= (N^4/16) sum_k |k|^(-4)
             <= (3N^4/16) sum_(m>=1) m^(-2) <= C N^4.

This is a full-spectrum bound. No bulk kernel replacement, boundary
collar deletion, or omission of a constant prefix occurs.

### 3. Keep the actual exterior heat columns

Use L149(9)'s exact exterior covariance expansion. In the physical
relative-mode convention let f_(k,a) be L2_a normalized with physical
eigenvalue lambda_k and stored orthonormal mode a^2 f_(k,a). Define

    v_k=a lambda_k^(-1/2) f_(k,a),       h_k=R v_k.

Then

    U_i=sum_(k,l) c_(i;kl) h_k h_l^T,
    c_(i;kl)=exp[-tau(lambda_k+lambda_l)]
              (mathcal B_i)_(kl),
    mathcal B_i=Delta_phys^(-1/2) Q_(i,a) Delta_phys^(-1/2).
                                                               (8)

L028 supplies uniform boundedness of mathcal B_i and the positive
physical gap lambda_k>=|k|^2/16. Consequently for any fixed polynomial
p, sum_(k,l) |c_(i;kl)|p(k)p(l)<=C_(i,p), uniformly over the complete
allowed spectrum. The color extension of (8) sums the same expression
with h_k t_c,h_l t_c for c=1,2,3. No restricted-Hessian flow is used.

Since A D_0=L D_0=0, exactly

    A h_k=A v_k,             L h_k=L v_k.

In dimensionless stored coordinates A=a^2 N_a, where N_a is L028's
physical residual operator. L028(5), including the adjoint coefficient
derivatives and both subtractions, gives

    ||A h_k||_infinity <= C a^5 p(k).                       (9)

Indeed A v_k=a^3 lambda_k^(-1/2) N_a f_(k,a) and
||N_a f_(k,a)||_infinity<=C a^2(1+|k|)^5. Its output support is in
a fixed compact interior region. This estimate is not applied to the
upper jump: gauge annihilation removes that part exactly first.

For the action one instead has

    ||L h_k||_infinity <= C a^3 p(k).                      (10)

Here L=a^2 d_a^*d_a. The relative sine/cosine modes remain closed under
each incidence map: a derivative contributes 2 sin(k_j pi/(2N))/a
with magnitude <=C k_j, interchanging the corresponding sine and
cosine factors. Thus d_a^*d_a f_(k,a) is a bounded number of product
modes with coefficients bounded by C(1+|k|)^2, also at normal end
edges. Zero derivative factors are retained for constant cosine modes.
Multiplying by a^3 lambda_k^(-1/2) proves (10). All action rows and
physical faces remain; no smooth continuation of h_k across its
pinned upper jump is asserted.

### 4. Contract and bound the entire two-gradient sector

Take independent three-color vertex Gaussians phi,psi with one-color
covariance K. These are auxiliary variables for the two multilinear
lines of (2), not independent pieces of the forest field. For a colored
link vector v define

    Z_v(phi,psi)=sum_e <v_e,
                   [(D_0 psi)_e,phi(tail e)+phi(head e)]>.

Each edge uses only its two endpoints, and every vertex has at most
eight incident links. Thus Z_v=psi^T M_v phi for a real matrix with

    ||M_v||_op <= C ||v||_infinity.                         (11)

For completeness, expand each bracket with the SU(2) structure constants
of magnitude at most one. Each row and each column has a bounded
number of entries, each at most C||v||_infinity; the row/column-sum
bound for operator norm proves (11). Pinned endpoints just give zero
terms, so this bound includes every end edge.

Set Khat=diag(K,K,K). Independence of phi and psi gives

    E[Z_v Z_w]=Tr(M_v Khat M_w^T Khat),
    |E[Z_v Z_w]|<=C ||v||_infinity ||w||_infinity ||K||_HS^2.
                                                               (12)

One direct matrix proof of the bound diagonalizes Khat. For any M,
sum_(j,k) lambda_j lambda_k |M_jk|^2 <=
||M||_op^2 sum_j lambda_j^2, by 2 lambda_j lambda_k<=lambda_j^2+
lambda_k^2 and the row/column squared-norm bounds. Cauchy--Schwarz
for the two weighted entry arrays gives (12), including its factor
3 from colors. No positivity of a probe or of A is assumed.

The independent copies select exactly the two direct lines in (2).
Using (5) twice in (2) and (8) yields the exact signed expression

    H_i^gg=-(1/2) sum_(k,l,c) c_(i;kl)
                 E[Z_(A h_k t_c) Z_(L h_l t_c)].          (13)

The normalization is -36 times (-1/6) times (-1/12)=-1/2.
There is no extra Isserlis pairing of phi with itself across a single
factor: phi and psi here represent two separately assigned lines.
The original 36 already counts their alternative assignments.

Combine (7),(9),(10),(12) and the complete heat sum after (8):

    |H_i^gg| <= C sum_(k,l,c) |c_(i;kl)| a^5 p(k) a^3 p(l) N^8
              <= C_i a^8 N^8 = C_i 8^8.

Absorb the fixed box-length factor in C_i. This proves (3). It is an
analytic bound; no finite mesh values or numerical cancellation are
used to infer the limit.

### 5. Scope, checks, and the remaining obstruction

The full tensors are essential. C_g can have nonzero axial forest
entries canceled by E in (1). Deleting those entries before the gauge
identity would invalidate (5) and this proof. The full response still
uses C, whose forest entries are exactly zero. This regrouping retains
all four terms; it does not assert that (2) is separately invariant
under forest changes or equals a transverse-gradient projection sector
of a previously restricted formula.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_cubic_gradient_ward.py`.
The certificate `scripts/combined-ward-response/cubic-gradient-ward-certificate.json`
checks the action specialization of (5) exactly on all 1728 basis
triples of one four-edge cycle, including its sign and factors. It
also checks (13)'s -1/2 factor as an exact rational product. These
finite algebra checks are not actual-probe or cutoff diagnostics;
gauge invariance of the complete residual and estimates (7)--(12)
are established above using the stated local inputs.

The mixed and E,E contractions still involve both the direct Hodge
field and its prefix correlations. Equations (9)--(10) cannot be
applied to them by simply calling E a gradient covariance. A proof
for that remaining complete signed sum, including any stronger powers,
is still required before determining the requested cubic-scale limit.

## Mathlib

Full matching result: **not checked**. Supporting finite gauge Taylor
identities, Gaussian bilinear moments, incidence spectra and matrix
norm estimates: **not checked**. Unknown availability is not absence.
The unchanged [target assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md)
is reused; no additional continuum theorem or external source is
imported. The standard finite identities are specialized explicitly
because the full-versus-restricted tensor order, pinned prefix and
actual residual scale determine whether this sector is below threshold.
