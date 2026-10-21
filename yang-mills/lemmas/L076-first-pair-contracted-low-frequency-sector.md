# L076 — A growing low-frequency sector of the centered circulation trace vanishes

## Hypotheses

Keep L064's actual two probes i=3,6, SU(2) straight-forest Gaussian,
tau=1/16, ordinary dimensionless coordinates, relative fixed-link box,
and sufficiently fine admitted even meshes a=8/N. Take the coupling
coefficient at each fixed mesh before refining the mesh. Keep the
actual symmetric residual A_0, including both insertion subtractions.

Use L070's pinned vertex incidence T, G=(T^T T)^(-1), upper skew
matrix C_(r_k), and (Sz)_s=sTz, 1<=s<N. Use the exact centered path
operator bar Q_l in L074 section 5, and the complete transverse
covariance Sigma_T and normalized axial embedding E_0 in L075.
All transverse end edges and axial levels are included. Define

    X_l=Sigma_T D^T bar Q_l S,
    F_(i,N)^circ=sum_(k,l)c_(i;kl) sqrt(N)
           Tr[G C_(r_k) G E_0^T A_0 I_T X_l].             (1)

This is only the centered circulation/path contribution. It is the
Z_l=D^T bar Q_l instance of L075(11). It is not the centered path/path
term, the exterior centering defect, or the whole first pair.

Let e_q be the ordinary orthonormal transverse pinned vertex modes,
q=(q_2,q_3,q_4) in {1,...,N-1}^3, and let P_K project onto
max_j q_j<=K, where 1<=K<=N-1 is an integer. Define F_(i,N,K)^low
by inserting P_K at the far left of the trace in (1). This is a
projection on the left trace space, not on the internal transverse
spectral resolution of Sigma_T. No projection is moved through C,
bar Q_l, A_0 or the other variable-coefficient maps.

## Conclusion

There are constants independent of N,K such that

    |F_(i,N,K)^low| <= C_i a² K^12.                       (2)

In particular K_N=floor(N^(1/12)) gives

    F_(i,N)^circ=F_(i,N,K_N)^high+O_i(N^-1),             (3)

where the high trace has I-P_(K_N) at the far left of (1), with
every other factor unchanged. The low sector vanishes even without
a² scaling and contributes no unsuppressed cutoff logarithm.

This is not an O(N²) bound or a scaled coefficient for the high
sector or for (1). Its available complete bound remains O(N³).
In particular (2) does not justify dropping L075's low internal-mode
upper-face correction: the two spectral placements are different.
The full response, all other first-pair terms, logarithmic coefficient,
and interacting reflected-error threshold c_box/2 remain unresolved.
This is a local REPRODUCTION of the assessed finite covariance and
consistency methods, with no beyond-source novelty claim.

## Proof

### 1. Preserve the full kernel and put the residual on the left

The right column in (1) is exactly

    (X_l z)_s=sum_alpha P_alpha sum_(t=1)^(N-1)
       R_(lambda_alpha)(s,t) t D^T bar Q_l(t) Tz,          (4)

with R and P_alpha as in L075. The transverse circulation D is
levelwise. All coefficients remain inside the kernel in (4).
We will use an operator bound on this complete inverse, never a
bulk-distance replacement or a zero-axial-frequency substitution.

For one trace mode set

    g_(k,q)=G C_(r_k)^T G e_q,
    y_(k,q)=E_0 g_(k,q),  x_(l,q)=X_l e_q.

Transposing only the left factors in its scalar diagonal entry, and
then using the symmetry of the actual A_0, gives the exact identity

    <e_q,G C_(r_k) G E_0^T A_0 I_T X_l e_q>
                         =<A_0 y_(k,q),I_T x_(l,q)>.    (5)

In particular C^T=-C stays in g with its sign; (5) does not assert
positivity or cancellation of the trace. Moving the residual by
symmetry is legitimate for these finite matrices and does not commute
it with any coefficient. All heat indices k,l remain unrestricted.

### 2. The actual upper coefficient supplies a smooth left forcing

For every fixed derivative order m the edge coefficients r_k have
smooth staggered extensions satisfying

    ||r_k||_(C^m) <= C_m a² p_m(k).                      (6)

Here and below p_m denotes a polynomial independent of the mesh.
To verify the higher-derivative form of L062's curvature estimate,
use that the forest lift preserves curvature exactly. Before that
lift, its covariance-square-root mode is a times a physical
sine/cosine one-form divided by its positive physical eigenvalue's
square root, as in L067 section 2. An upper (1,mu) plaquette row
is a signed pair of unscaled differences of that field. For a smooth
mode b, each difference equals a times an integral of its physical
derivative over a unit interval. The exterior stored-link factor
provides the other a. Differentiating this integral in transverse
coordinates gives (6) for every fixed m. The relative sine/cosine
extensions reproduce the fixed tangential zero rows and normal end
edges exactly, including the last axial interval. There is no
interpolation of a forest potential across its upper-face jump.

The vertex mode and its dimensionless eigenvalue are

    e_q(v)=(2/N)^(3/2) product_(j=2)^4 sin(pi q_j v_j/N),
    lambda_q=4 sum_(j=2)^4 sin²(pi q_j/(2N)).

They obey lambda_q>=c a² |q|² and
||e_q||_(C^m)<=C_m a^(3/2)(1+|q|)^m on their exact trigonometric
extensions. Thus z=G e_q=lambda_q^(-1)e_q obeys the convenient,
deliberately nonsharp bound

    ||z||_(C^m)<=C_m a^(-1/2)(1+|q|)^m.                 (7)

Consider C_r=E_v^T M_r T-T^T M_r E_v with Tz(v,w)=z(v)-z(w).
For each direction j its action at a retained vertex is exactly

    (C_r z)(v)=sum_j [r_j(v-e_j)z(v-e_j)
                                      -r_j(v)z(v+e_j)]. (8)

The edge coefficient r_j(v) labels the edge from v to v+e_j.
At a pinned endpoint the adjacent value of z is zero, exactly as
in its sine extension. Both end edges occur in (8), with no missing
boundary term. Rewrite a summand as

    r_j(v-e_j)[z(v-e_j)-z(v+e_j)]
                      +[r_j(v-e_j)-r_j(v)]z(v+e_j).

Every bracket is a difference over physical distance at most 2a.
Using (6), (7), their integral difference formulas, and the product
rule, the forcing f_(k,q)=C_(r_k)^T G e_q therefore has an exact
sampled smooth extension with

    ||f_(k,q)||_(C^m)
       <=C_m a^(5/2) p_m(k)(1+|q|)^(m+1).              (9)

The transpose only changes the sign. This bound holds up to the
transverse boundary and for all q, with polynomial rather than
uniform control of large q. Counting at most N³ vertices also gives

    ||f_(k,q)||_2<=C a p(k)(1+|q|).                     (10)

### 3. Interior regularity before residual consistency

The global pinned spectral gap gives ||G||<=C a^-2. Since g=G f,
(10) and the three-dimensional physical norm
||h||_(L²_(a,3))=a^(3/2)||h||_2 imply

    ||g||_(L²_(a,3))<=C a^(1/2) p(k)(1+|q|).            (11)

On any fixed interior region, g satisfies

    a^-2 Delta_V g=a^-2 f.

Equation (9) bounds physical forward differences of its right-hand
side through order seven by
C a^(1/2) p(k)(1+|q|)^8. No boundary smoothness theorem for the
Dirichlet inverse is needed. Apply the interior estimate of L067
section 3 in three dimensions as follows. Choose finitely many fixed
nested neighborhoods containing the transverse projection of every
input stencil of A_0, all separated from the transverse faces.
For a cutoff chi the same edgewise identity used there is

    sum_j ||partial_(j,a)(chi w)||²_(L²_(a,3))
      =<chi²w,a^-2 Delta_V w>_(L²_(a,3))
       +a³ sum_(j,v)|partial_(j,a)chi(v)|² w(v)w(v+e_j).

It holds on the cutoff support, with no physical-face term. Bounding
adjacent products and applying Cauchy–Schwarz controls first
differences by the L² norms of w and its forcing on the larger
neighborhood. Commute physical forward differences with the interior
constant-coefficient Laplacian and iterate on the nested neighborhoods.
The eighth iteration uses forcing differences only through order
seven. Consequently

    sum_(|alpha|<=8)||partial_a^alpha g||_(L²_(a,3),inner)
       <= C a^(1/2) p(k)(1+|q|)^8.                     (12)

This is the same finite energy argument as L067; its change of
dimension and volume weight are explicit here. Multiply by another
cutoff equal to one on the needed stencils, and extend by zero on
the infinite vertex grid. The product-difference identity preserves
(12). The inverse continuous Fourier integral of its lattice
transform interpolates the grid values exactly. On the Brillouin
cube the inequality

    |(exp(i a xi_j)-1)/a| >= (2/pi)|xi_j|

and discrete Plancherel bound that interpolant's H^8 norm by (12).
Cauchy–Schwarz in the inverse integral controls its derivatives
through order five, since
integral_R³ |xi|^10(1+|xi|²)^(-8) dxi is finite.
After a final fixed cutoff, this supplies an exact local C^5
extension of g of norm at most the right side of (12).

E_0 inserts the normalized constant axial edge mode, so its values
are g/sqrt(N), with no axial variation. Multiplication by a smooth
axial cutoff equal to one on all A_0 input stencils gives an exact
compact extension of y on those stencils. Since N^-1/2=O(a^1/2),

    ||y_(k,q)||_(C^5,stencils)
                  <=C a p(k)(1+|q|)^8.                 (13)

L028's actual residual consistency states A_0=a² N_a and
||N_a Y||_infinity<=C a²||Y||_(C^5) for such smooth inputs.
It includes the adjoint coefficient derivatives and both curvature
forms. Apply it to (13), rather than to the rough right column:

    ||A_0 y_(k,q)||_infinity<=C a^5 p(k)(1+|q|)^8,
    ||A_0 y_(k,q)||_2<=C a³ p(k)(1+|q|)^8.              (14)

The second inequality counts O(a^-4) full-link rows, not O(a^-3).
All other output rows vanish because the residual coefficients and
their stencils are compactly supported. This argument never asserts
that g has smooth boundary traces or that the rough residual has a
uniform full-vector norm.

### 4. Bound the complete right inverse without simplifying its profile

The transverse incidence obeys the pinned Hodge form inequality

    D^T D <= I_ax tensor Delta_E <= Sigma_T^(-1).

This is the full four-dimensional covariance from L075, with every
axial Dirichlet eigenvalue included. Thus
||Sigma_T^(1/2) D^T||<=1 and, by its full spectral gap,

    ||Sigma_T D^T||<=C a^-1.                            (15)

L062's coefficient bounds and L074's bounded centered path maps give
||bar Q_l||<=C a p(l) on the full levelwise array. Also

    ||S e_q||²=sum_(s=1)^(N-1) s² ||T e_q||²
             =sum_s s² lambda_q <= C a^-1 |q|²,

using the upper sine bound lambda_q<=C a² |q|². Combining this
identity with (15), in the stated order, yields

    ||x_(l,q)||_2<=C a^(-1/2) p(l)|q|.                  (16)

This includes the upper correction in (4), the variable path
coefficients, all transverse frequencies created by them, every
level and every end row. No modewise localization estimate or
unjustified commutation is part of (16).

### 5. Sum the actual exterior modes and the selected trace modes

By (5), (14), (16), the isometry I_T and sqrt(N)=O(a^-1/2),
each selected trace entry is bounded by

    sqrt(N)|<A_0 y_(k,q),I_T x_(l,q)>|
       <=C a² p(k)p(l)(1+|q|)^9.                       (17)

Enlarge p once to absorb the finitely many derivatives above.
L064's complete coefficients satisfy
sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i for this polynomial, as explicitly
justified in L067: the relative probe form is uniformly bounded
and the fixed positive flow time gives Gaussian summability over
all allowed external indices. There is no exterior mode cutoff.

There are K³ selected q and (1+|q|)^9<=C K^9 for them.
Summing (17) proves (2). For K_N=floor(N^(1/12)),
a² K_N^12<=64/N; splitting the finite trace by P_K+(I-P_K)=I
then proves (3). In particular the bound is below the required
O(N²) scale for this sector and tends to zero before scaling.

The proof does not extend to the full q range at a useful rate:
substituting K=N-1 into (2) gives only O(N^10), worse than the
existing complete O(N³) bound. The remaining contraction is exactly
(1) with I-P_(K_N) on the far left. Its high trace frequencies still
mix through C and bar Q_l with the complete axial inverse. L070's
nonzero frozen symbol is relevant to that unresolved sector, but
supplies neither a signed growth estimate nor an original coefficient.

The centered path/path term, scaled exterior centering defect,
diagnostic identification, all nine mixed placements and remaining
action/measure/insertion/flow/forest jets are independent open tasks.
No continuum field construction, reflection positivity, infrared
control or finite positive mass follows. The proof uses finite
matrix identities, the existing local consistency result and the
specified energy estimate; no mathematical script or numerical
certificate is needed or used.

## Mathlib

Coverage of the full specialized trace-sector statement: **not
checked**. Supporting finite spectral projections, matrix norm
inequalities, finite-difference interior estimates and interpolation:
**not checked**. No matching theorem or absence claim is made.
The unchanged source assessment's general flow and stress results
are not reproved and are not used to assign a coefficient to this
finite-box trace. The proof specializes only the retained covariance,
path and residual operators not evaluated by those sources.
