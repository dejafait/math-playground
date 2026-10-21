# L072 — A deterministic tensor integral for the surviving diagnostic

## Hypotheses

Keep L070 section 6's diagnostic at an admitted even mesh N, a=8/N,
tau=1/16, with all its row averages, axial levels, normal end edges,
zero boundary evaluations and straight lower-rooted pinned forest.
Use ordinary stored coordinates and L018's full four-dimensional
operators Delta, Sigma=Delta^(-1), H=exp(-tau Delta/a²).
Use L071's split of L008's actual probe matrices into Q_i^A+Q_i^B,
i=3,6. Only Psi_13 and its antisymmetric partner occur in Q_i^A;
the diagnostic's u_1 already depends only on that sector.

The conclusion concerns this finite Gaussian diagnostic only. No
approximation of the original circulation/path trace is assumed.

## Conclusion

There is an explicit finite tensor construction of matrices M and
Q_i^A from one-dimensional matrices of order at most N, given below,
such that, with t_0=tau/a² and E(t)=exp(-t Delta),

    D_(i,a)= integral_(t_0)^infinity integral_(t_0)^infinity
                         Tr[M E(t) Q_i^A E(s)] ds dt.       (1)

If their component blocks are expanded by that construction as

    M_(alpha,beta)=sum_r m_r tensor_(j=1)^4 M_(r,j),
    (Q_i^A)_(beta,alpha)=sum_l q_l tensor_(j=1)^4 Q_(l,j),

then the complete integrand in (1) is the finite scalar expression

    sum_(alpha,beta,r,l) m_r q_l product_(j=1)^4
      tr[M_(r,j) E_(beta,j)(t) Q_(l,j) E_(alpha,j)(s)].  (2)

The index sets r,l refer to the blocks indicated in each summand;
no mode, component, axial level or transition weight is truncated.
E_(alpha,j) is the one-dimensional edge heat when j=alpha and
the vertex heat otherwise. In particular the edge zero mode is kept.

Put d=4N(N-1)^3, lambda_*=12 sin²(pi/(2N)),

    W_* = max_(s,y) |(sa) u_1(s,y)|,
    W_3 = max_(mu<nu,x) |w_mu^A(x)+w_nu^A(x)|,
    S_6 = max_(mu<nu,x) |s_mu nu^A(x)|,
    B_M = 12 a sqrt(N-1)(1+4N) W_*,
    B_3 = 16 W_3,                 B_6 = 192 S_6.

All maxima are over the actual finite coefficient arrays, including
their transitions. For every T>=t_0, omitting the part of (1) outside
the square with t_0<=t,s<=T has absolute error at most

    d B_M B_i / lambda_*²
       [2 exp(-lambda_*(T+t_0))-exp(-2 lambda_* T)].       (3)

Thus these two infinite integration tails can be made smaller than
any prescribed positive error, with an explicit threshold. This does
not enclose the retained integral, its quadrature or its arithmetic.
No sign or zero of D_(i,a), mesh limit, original-trace coefficient,
O(N²) direct first-pair bound or response logarithm is established.

## Proof

### 1. One-dimensional spaces and the full relative heat

Let V=R^(N-1) have entries at interior vertices j=1,...,N-1,
and E=R^N have entries at edge tails ell=0,...,N-1. Define the
unscaled pinned incidence G:V->E and average A:E->V by

    (Gv)_ell=v_(ell+1)-v_ell, with v_0=v_N=0,
    (Ae)_j=(e_(j-1)+e_j)/2.

Let C:V->V be the central physical difference
(Cv)_j=(v_(j+1)-v_(j-1))/(2a), with the same zero endpoints.
Let P:E->V be the actual prefix matrix

    (Pe)_j=sum_(ell=0)^(j-1) e_ell,

and let r_top^T:E->R select ell=N-1. These definitions retain
both end edges. They introduce no periodic extension. Tensor
coordinates below are always ordered 1,2,3,4.

The component-alpha one-form space is

    X_alpha=tensor_(j=1)^4 X_(alpha,j),
    X_(alpha,j)=E if j=alpha, and V otherwise.

The stored relative one-form space is the orthogonal direct sum of
these four spaces. On V put L_V=G^T G, and on E put L_E=G G^T.
The relative tensor-complex identity used in L008 and L018 gives

    Delta|X_alpha=sum_(j=1)^4 L_(alpha,j),
    E(t)|X_alpha=tensor_(j=1)^4 E_(alpha,j)(t),           (4)

where L_(alpha,j) acts in coordinate j as L_E or L_V respectively,
and E_(alpha,j)(t) is its exponential. For clarity, the cancellation
behind (4) is at the operator level: in D_1^T D_1 the cross block
between components alpha,beta is the negative product of their two
incidences, and in D_0 D_0^T it is the positive same product. They
cancel because incidences in different tensor coordinates commute.
The remaining diagonal blocks are G G^T in the component coordinate
and G^T G in each other coordinate. This includes boundary rows of G.

The eigenvalues of L_V are 4 sin²(pi k/(2N)), 1<=k<N;
those of L_E have the same positive eigenvalues and one zero
eigenvalue. The former follows by applying the tridiagonal matrix
with diagonal 2 and off-diagonal -1 to the pinned sine vectors;
the latter follows from the nonzero singular values of G and its
one-dimensional orthogonal complement, the constant edge vector.
Every X_alpha has three vertex coordinates. Consequently Delta is
positive and its least eigenvalue is exactly lambda_* above. There
is no removal of the constant edge mode and no use of a transverse
covariance in place of the four-dimensional Sigma.

### 2. Exact coefficient and probe construction

On interior vertices put h_j=ja, r_j=rho(-4+ja),
f_j=(-4+ja)r_j, with L008's exact rho. Their boundary values are
zero wherever a central difference uses them. The displacement of
the A sector is exactly

    u_1^A=f tensor r tensor (Cf) tensor r,
    u_3^A=-(Cf) tensor r tensor f tensor r,
    u_2^A=u_4^A=0.                                     (5)

Use C in coordinate mu to form w_mu^A=C_mu u_mu^A and
s_mu nu^A=C_mu u_nu^A+C_nu u_mu^A. Each array is thus an explicit
finite signed sum of products of four one-dimensional vectors.
The supported-stencil assumption makes these exactly L008's zero-
extended central differences. No derivative of rho is substituted
for a mesh difference.

For mu<nu define the stored circulation map

    C_(mu nu) x=G_mu x_nu-G_nu x_mu.

Its output space has E in coordinates mu,nu and V in the other two.
Every nonzero component block is a tensor product of one G and
three identities, with the displayed sign. Write
B_(mu nu)=A_mu A_nu C_(mu nu), a map to V^tensor4, and set
B_(nu mu)=-B_(mu nu), B_(mu mu)=0. These are exactly the vertex
clover rows in stored coordinates.

Set the plaquette weight array

    z_(mu nu)=A_mu^T A_nu^T (w_mu^A+w_nu^A).

Here the adjoints act on coefficient vectors, not on a diagonal
matrix. Each vertex contributes weight 1/4 to its four plaquettes.
The exact stored quadratic matrices are

    Q_3^A=sum_(mu<nu) C_(mu nu)^T diag(z_(mu nu)) C_(mu nu),

    Q_6^A=(1/2) sum_(mu<nu, alpha not in {mu,nu})
      [B_(mu alpha)^T diag(s_mu nu^A) B_(nu alpha)
       + B_(nu alpha)^T diag(s_mu nu^A) B_(mu alpha)].    (6)

Indeed physical curvature on input x/a is C_(mu nu)x/a².
The factor a^4 in L008's forms cancels the two factors a^(-2).
The first formula retains its average of squares. The second
retains its oriented clover products and polarization factor 1/2;
on the quadratic diagonal it is precisely the unsymmetrized product
in L008. There are two alpha values in each of the six shear pairs.

Equations (5)-(6) give a finite tensor expansion of every block of
Q_i^A: diagonal multiplication by a product vector is the tensor
product of the four diagonal matrices; distribution over each
finite signed coefficient sum and over the two circulation blocks
specifies all summands. All operations are sums, transposes and
compositions of the stated one-dimensional maps. This is an exact
construction, not a separability assertion about the nonlinear
Wilson-flow probes or a low-mode approximation to them.

### 3. Exact upper and lifted rows, including their axial factors

Use mu in {2,3,4}. Let bar U_mu be a map from full one-forms to
V^tensor4: it is a² times L070's U_mu, replicated unchanged over
every interior axial level. Let bar V_mu be a times L070's V_mu.
Their only nonzero input-component blocks are the following.
On input component mu, bar U_mu has axial factor
1_V (r_top^T G), transverse factor A in coordinate mu, and identities
in the other two coordinates. On input component 1 its axial
factor is -1_V r_top^T, its coordinate-mu factor is A G, and the
other two factors are identities. The minus sign is the -G_mu x_1
part of the positive (1,mu) circulation. Here 1_V is the column of
N-1 ones, so these formulas replicate rather than normalize the row.

On input component mu, bar V_mu has axial identity on V, factor A
in coordinate mu, and the other identities. On input component 1
it has axial factor -P, coordinate-mu factor A G, and the other
identities. This is exactly the transverse component of
R_F x=x-D_0 phi_x, with phi_x=P_1 x_1 on all interior vertices.
The boundary values of phi are zero, including at the upper face;
the incidence G in the transverse factor therefore includes the
normal end edges. There is no use of an unpinned upper prefix or
an axial-frequency projection.

Let

    W=diag(h f) tensor diag(r) tensor diag(Cf) tensor diag(r).

This is multiplication by (sa)u_1(s,y) on the complete vertex array,
with h=sa the physical distance from the lower face, as required by
the definition of the diagnostic. In particular h is not x_1.
Equations (5) and the row normalizations now give

    P_a(x,z)=x^T M z,
    M=a sum_(mu=2)^4 bar U_mu^T W bar V_mu.              (7)

The coefficient a is a^4/(a² a). Formula (7) is a finite tensor
construction of all blocks of the unsymmetrized diagnostic matrix.
It keeps the four component combinations {1,mu} on both sides,
including the prefix contribution; there is no omission based on a
base-law zero covariance. It also shows explicitly that each block
is a finite sum of products of four matrices of order at most N.

### 4. Resolve both Green factors without truncating the spectrum

L070's finite identity and L071 give

    D_(i,a)=Tr[M^sym Sigma H Q_i^A H Sigma]
           =Tr[M F Q_i^A F],          F=Sigma H.          (8)

The second equality holds because F Q_i^A F is symmetric: the
trace of its product with the skew part of M is zero. Use the scalar
single-inverse Laplace identity recorded in L033 section 4 on each
side; its earlier squared inverse weight is not present here. The
specialization to the finite positive matrix Delta is

    F= integral_(t_0)^infinity exp(-t Delta) dt.         (9)

For an eigenvalue lambda>0 the integral is exp(-t_0 lambda)/lambda,
which is exactly the eigenvalue of Sigma H. Bounds by
exp(-lambda_* t) make (9) absolutely convergent in operator norm.
The trace in (8) is finite dimensional and its double integrand is
absolutely integrable, as quantified below. Substitution proves (1).
No infinite-volume or mesh limit is being interchanged.

Since E is component diagonal, the trace of the full product is
the sum over alpha,beta of the trace on X_alpha of

    M_(alpha,beta) E_beta(t) (Q_i^A)_(beta,alpha) E_alpha(s).

Insert the finite tensor constructions of sections 2-3 and (4).
Composition of tensor maps is coordinatewise, and the trace of a
tensor product of four square matrices is the product of their four
traces (expand its diagonal in the tensor basis). Intermediate maps
may be rectangular; the product in each coordinate starts and ends
in X_(alpha,j), so the traced product is square. This proves (2),
with both component heat orders and both inverse weights retained.

### 5. A complete bound for the two integration tails

The following bounds use ordinary Euclidean operator norms. The
incidence G has norm at most 2, and A has norm at most 1: apply
the inequality |b+c|²/4<= (|b|²+|c|²)/2 and count each edge
in at most two adjacent averages. The prefix has norm at most N,
for instance by its Frobenius norm, whose square is N(N-1)/2.
The full D_0 has norm at most 4, by summing its four squared
incidence bounds. Thus ||R_F||<=1+4N. Each transverse component of
the lifted-link average has norm at most (1+4N)/a.

Each upper curvature row has norm at most 4/a²: its two incidence
blocks have norms at most 2, their combined row has norm at most
sqrt(8)<4, and neither the transverse average nor upper evaluation
increases the norm. Replication over all levels has norm sqrt(N-1).
Multiplication by the diagnostic weight has norm W_*. From the
original a^4 normalized row formula in (7), the triangle inequality
therefore gives ||M||<=B_M.

For the triplet, the nonnegative adjoint averaging sends any vertex
coefficient bounded by W_3 to a plaquette coefficient bounded by
W_3: each plaquette gets at most four contributions of size W_3/4.
Also ||D_1||²<=||Delta||<=16, from (4) and the norm bound on G.
The first formula in (6) consequently gives ||Q_3^A||<=16 W_3.

For the shear, each B_(mu alpha) is a contraction of one component
of D_1. For any x, each of the twelve scalar products in its
quadratic form is bounded in magnitude by
S_6 ||D_1 x||², using Cauchy-Schwarz and the clover contractions.
Summing gives |x^T Q_6^A x|<=12 S_6 ||D_1 x||².
Self-adjointness in (6) then gives ||Q_6^A||<=192 S_6.
These bounds intentionally keep signed weights through their
absolute maxima; they do not supply a positivity claim.

For d-dimensional matrices, |Tr Z|<=d||Z||, by bounding each
diagonal matrix element. Positivity of Delta and the spectral gap
therefore yield, for both probes,

    |Tr[M E(t) Q_i^A E(s)]|
       <=d B_M B_i exp[-lambda_*(t+s)].                 (10)

Integrating this bound over the positive quadrant t,s>=t_0 minus
the square t,s<=T gives exactly (3): its exponential integral is

    lambda_*^(-2) [exp(-2 lambda_* t_0)
               -(exp(-lambda_* t_0)-exp(-lambda_* T))²].

In particular it is at most
2d B_M B_i exp[-lambda_*(T+t_0)]/lambda_*² after including the
prefactor. When B_M B_i>0, an error epsilon>0 is ensured by any

    T>=max(t_0, lambda_*^(-1)
                   log(2d B_M B_i/(lambda_*² epsilon))-t_0).

If either bound is zero, (10) gives D_(i,a)=0 directly. The
threshold otherwise addresses only the two infinite integration
tails. A retained quadrature, coefficient evaluation, matrix
exponential and arithmetic enclosure is still required. Tensor
trace factors can have either sign, and multiplying norm bounds
cannot determine the diagnostic's sign.

### 6. Scope of the completed attempt

The finite algebra is a deterministic evaluation route for the
defined diagnostic, with a rigorous tail threshold. It is not a
sign certificate. No sampled sign is used, and no positive Gram
interpretation is assigned to the signed trace. All axial levels,
transition coefficients, edge zero modes and boundary rows were
kept in the construction before separating the heat factors.

L070's centering/path replacement, axial normalization, variable-
coefficient and physical-boundary trace remainders remain unresolved.
Neither (1) nor (3) relates this surrogate to the original first
pair. The other mixed placements, response jets, cutoff logarithm,
finite matching, reflected error <=c_box/2, continuum fields,
reflection positivity, infrared limit and finite positive mass are
still open. The shared quartic is not added again.

## Mathlib

Coverage of the full specialized diagnostic tensor integral and its
tail threshold: **not checked**. Supporting finite matrix spectral
calculus, tensor-product traces, norm bounds and exponential
integration: **not checked**. No matching theorem or absence claim
is asserted. This is finite algebra and the scalar resolvent integral
specialized to the recorded rows under the ready SPECIALIZE response
assessment. General flow renormalizability and bulk stress matching
are reused in their assessed scope and are not reproved or extended
to this physical-boundary response.
