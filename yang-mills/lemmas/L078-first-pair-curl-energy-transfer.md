# L078 — Exact curl-energy transfer isolates the actual leading circulation trace

## Hypotheses

Keep L076's actual SU(2) probes i=3,6, straight-forest exterior columns,
a=8/N, tau=1/16, fixed relative box, and coupling coefficient at fixed
mesh before refinement. In ordinary dimensionless coordinates write

    Delta=Sigma^(-1)=L_0+D_0 D_0^T,  L_0=D_1^T D_1,
    A_0=(L_0 K_a+K_a^T L_0)/2-Q_3-Q_6.

D_0,D_1 are full relative incidences; K_a is L009's actual generator
and Q_3,Q_6 are the actual insertion forms. Use L075's full Sigma_T,
I_T,E_0 and Delta_V=T^T T=G^(-1). Reserve D for the transverse curl
at each level, as in L074. All normal end edges and axial rows remain.
For each exterior heat index l set

    Z_l=D^T bar Q_l S,  X_l=Sigma_T Z_l,
    bar Q_l=M_(bar t_l,2)bar B_3-M_(bar t_l,3)bar B_2,
    (Sz)_s=sTz.

Every coefficient has its actual level dependence and every k,l is
retained with c_(i;kl). At transverse vertices C_mu averages adjacent
mu edges and T_mu=C_mu D_mu is the centered signed difference, with
D_mu oriented as in L065. T in S retains L070's stated convention.
Define the finite pinned transverse-edge map

    (V_s z)_mu=C_mu^T M_(u_(a,1)(s)) T_mu z, mu=2,3,4.       (1)

In particular u_(a,1) stays between the two displayed maps.

## Conclusion

The actual signed finite transverse trace

    J_(i,N)=-(1/(2a)) sum_(k,l)c_(i;kl) sum_(s=1)^(N-1) s
          Tr[G C_(r_k) G V_s^T D^T bar Q_l(s) T]             (2)

satisfies, for L076(1)'s centered circulation/path contribution,

    F_(i,N)^circ=J_(i,N)+O_i(N²).                           (3)

Equation (2) is exactly its K_a^T L_0/2 placement after eliminating
the right covariance. The L_0 K_a/2 placement and both curvature
subtractions together are O_i(N²). L076's high left trace consequently
also equals J_(i,N)+O_i(N²). If N^(-3)J_(i,N) has a limit, it is
the N^(-3) limit of those actual traces; existence and value are open.

This reduces an actual trace, rather than L077's frozen diagnostic.
It does not identify (2) with L070(9), evaluate its sign, bound F^circ
by O(N²), or determine an N²-scale coefficient or logarithm. Both left
pinned Green factors remain. The remainder may contribute at a² scale
and may contain a logarithm. This is local REPRODUCTION under the
saved SPECIALIZE assessment, without a beyond-source novelty claim.

## Proof

### 1. Cancel the right inverse on its exact co-closed range

The finite relative identity T^T D^T=0 includes transverse end edges.
Thus Z_l is transversely co-closed on every level. The intertwining
Delta_V T^T=T^T Delta_E and L075's exact inverse

    Sigma_T=(L_V tensor I+I tensor Delta_E)^(-1)

show that X_l has the same property: applying T^T to its defining
equation gives a positive definite axial-vertex/transverse-vertex
Hodge matrix times T^T X_l equal to zero. Hence T^T X_l=0. This
uses the complete inverse, not a bulk profile approximation.

The full divergence of I_T X_l is its transverse divergence because
component 1 is zero. The full Hodge matrix is component diagonal.
Consequently

    L_0 I_T X_l=Delta I_T X_l=I_T Z_l.                      (4)

Also D_0^T E_0=0: the axial incidence adjoint kills the constant edge
mode at every interior vertex. The tensor Hodge identity gives

    L_0 E_0=E_0 Delta_V.                                   (5)

These include the physical faces; scalar Dirichlet conditions are
not imposed on component 1. Split the actual residual exactly:

    A_0=K_a^T L_0/2+A_rem,
    A_rem=L_0 K_a/2-Q_3-Q_6.                               (6)

Using (4), its first placement in L076's trace is

    (sqrt(N)/2) Tr[G C_(r_k) G E_0^T K_a^T I_T Z_l].        (7)

L065(2) retains the axial input average and gives exactly

    (I_T^T K_a E_0 z)_s=-(1/(a sqrt(N))) V_s z.             (8)

Indeed C_1 takes the normalized constant edge mode to the same
constant at every axial vertex. Substitute (8) and Z_l into (7)
to obtain (2), including its sign and 1/2. The other displacement
components remain in A_rem. No symmetry of A_rem is assumed.

### 2. Bound the reverse generator placement by axial summation by parts

Put B=E_0^T K_a I_T. We prove

    ||G^(-1/2) B Sigma_T^(1/2)||<=C.                        (9)

Use L028's uniform smooth, compact coefficient extensions through
physical derivative order two. Let D_v map pinned axial vertices to
edges, C_1 average edges to vertices, and T_1=C_1 D_v. Its exact
finite matrix is skew-symmetric:
(T_1 f)_s=(f_(s+1)-f_(s-1))/2, with f_0=f_N=0.
L009's clover and endpoint formula gives on transverse-only x

    (K_a I_T x)_1
       =-a^(-1) C_1^T sum_mu M_(u_(a,mu)) T_1 C_mu x_mu.

This is the -partial_1 x_mu part of F_(mu,1); x_1=0 removes its
other part. Both clover averages and the output endpoint average
are present. Since E_0^T C_1^T=N^(-1/2) sum_s, finite skew-adjoint
summation by parts gives

    Bx=N^(-1/2) sum_(s,mu) M_(b_mu(s)) C_mu x_mu(s),
    b_mu(s)=(T_1 u_(a,mu))(s)/a.                           (10)

The pinned zeros and compact coefficient support leave no endpoint
term. The coefficient and its transverse differences satisfy

    ||b_mu||_infinity<=C,
    ||b_mu(.+a e_j)-b_mu||_infinity<=C a,                  (11)

including their zero extensions. For fixed s put
Y_s=sum_mu M_(b_mu(s)) C_mu x_mu(s). The product-difference identity
then gives

    ||T Y_s||<=C (||Delta_E^(1/2)x_s||+a||x_s||).           (12)

To justify this at all rows, every nonzero coefficient stencil lies
in the fixed interior collar. A difference of b times an average
is a shifted b times the difference of that average plus a difference
of b times a shifted average. The latter is bounded by C a||x_s||.
For j different from mu, differences commute with C_mu and are
controlled by the j derivative of component mu in its Hodge energy.
For j=mu, the derivative of C_mu x_mu is an average of adjacent
own-direction edge-to-vertex derivatives of x_mu, also controlled
by that energy. The averages have norm at most one. The same
identities hold on zero-extended coefficient supports; no physical
face is crossed by a nonzero coefficient stencil. Taking T of the
result retains all actual pinned end rows. This proves (12) without
assuming boundary regularity of x.

Axial Cauchy–Schwarz in (10), with (N-1)/N<=1, gives

    ||T Bx||²<=C sum_s (||Delta_E^(1/2)x_s||²+a²||x_s||²)
                <=C ||Sigma_T^(-1/2)x||².                 (13)

The transverse energy is part of the full Hodge energy; its full
spectral gap is at least c a², so it also controls a²||x||².
Since ||Tz||=||G^(-1/2)z||, this proves (9). By (5),

    G^(1/2) E_0^T (L_0 K_a/2) I_T Sigma_T^(1/2)
                =(1/2)G^(-1/2) B Sigma_T^(1/2)             (14)

is uniformly bounded. This controls only that placement, consistently
with L066's growing full mixed residual block.

### 3. Retain the two actual curvature subtractions

The actual bounded weights and finite curvature averages give
|z^T Q_j z|<=C||D_1 z||² for j=3,6, by the form argument of
L065/L066. For mixed curvature products use 2|vw|<=v²+w².
For the triplet keep the vertex average of squares. No replacement
by a square of averages occurs. Since Q_j is symmetric and L_0<=Delta,

    ||Sigma^(1/2) Q_j Sigma^(1/2)||<=C.

The tensor identities Sigma^(1/2)E_0=E_0 G^(1/2) and
Sigma^(1/2)I_T=I_T Sigma_T^(1/2) give the corresponding mixed
bound. With (14), the triangle inequality proves

    R_rem=G^(1/2) E_0^T A_rem I_T Sigma_T^(1/2),
    ||R_rem||<=C.                                         (15)

No symmetry of A_rem is needed for this norm inequality.

### 4. Sum the complete pinned trace and every exterior heat mode

Set

    W_1=sqrt(N) G E_0^T A_rem I_T Sigma_T D^T,
    H_b=G S^T bar B_b^T, b=2,3.

The relative form inequality D^T D<=Sigma_T^(-1) and (15) imply

    ||W_1||_HS<=sqrt(N) ||G^(1/2)||_HS ||R_rem||
                                ||Sigma_T^(1/2)D^T||
               <=C sqrt(N Tr G)=O(N²).                    (16)

Here Tr G=O(N³): the positive three-dimensional sine eigenvalues
satisfy lambda_q>=c |q|²/N²; each shell of radius m contains O(m²)
indices. Summing N²/m² over the shells up to O(N) proves the bound.
Also, exactly,

    ||S G||_HS²=sum_(s=1)^(N-1) s² Tr(G T^T T G)
                 =sum_s s² Tr G=O(N^6).

The centered rough paths have bounded operator norm, so
||H_b||_HS=O(N³). Upper endpoint pullbacks and T change these
complete-array bounds by only fixed constants. All levels and
edges have already been counted.

The finite skew-trace expansion in L070 applies to arbitrary W_1.
Thus the remainder trace equals

    -sum_p bar t_l,2(p) W_1(p)^T C_(r_k) H_3(p)
     +sum_p bar t_l,3(p) W_1(p)^T C_(r_k) H_2(p).           (17)

Expand C_r=E_v^T M_r T-T^T M_r E_v. Every endpoint map has bounded
norm. Complete-array Cauchy–Schwarz and the actual coefficient bounds
from L062/L064/L074 give

    |(17)|<=C ||r_k||_infinity max_b||bar t_l,b||_infinity
                            ||W_1||_HS sum_b||H_b||_HS
             <=C a³ p(k)p(l) N² N³
             <=C N² p(k)p(l).                             (18)

Finally L064(3) gives sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i, proving
(3) with the complete heat sum. L076's removed low left sector is
O(N^(-1)); subtracting that actual sector proves the high-sector
consequence. No projection moved through a coefficient or restricted
an internal covariance frequency. In particular this consequence
uses the full unprojected J_(i,N) in (2).

### 5. Remaining scope

Equation (2) is an actual finite trace with O(N²) difference, not yet
a continuum integral or an evaluated coefficient. The pinned transverse
inverses and variable exterior coefficients still need signed asymptotic
analysis. L077 is a contrast, not an input. Its angular mean and L070(9)
have no proved identification with (2). Centered path/path, the scaled
exterior defect, all nine placements and remaining response jets remain;
the shared quartic must be subtracted once. No logarithm, reflected-error
bound <=c_box/2, continuum field axioms, reflection positivity, infrared
limit or finite positive mass follows. No script or numerical evidence
is used. General perturbative renormalization theorems are not reproved.

## Mathlib

Coverage of the full specialized reduction: **not checked**. Supporting
relative cochain Hodge identities, matrix norms and summation by parts:
**not checked**. No matching theorem or absence assertion is made.
The primary results in `drafts/literature/2026-09-26-current-target.md`
are reused within their stated scope, not used to assign a coefficient.
