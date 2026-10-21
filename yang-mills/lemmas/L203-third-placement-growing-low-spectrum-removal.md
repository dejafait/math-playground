# L203 — Remove a growing low-spectrum corner from the signed third placement

## Hypotheses

Use L187 and L202's exact SU(2) setting: relative box (-4,4)^4,
sufficiently fine admitted even N, a=8/N, straight lower-rooted
direction-1 forest, full compact L008 displacement and both actual
L010 probes i=3,6 at tau=1/16. Take the bare expansion at fixed mesh
before refinement. Coordinates and adjoints are ordinary full variable-link
coordinates. Keep every physical face, normal end edge, constant
own-direction mode and complete exterior heat sum. Vertex potentials
are pinned on all physical boundary vertices.

Keep the co-closed projection P, covariance S=PSP, signed residual
A=PAP with both insertion subtractions, and M=2SAS. Set

    V=q Phi, H=I-D Phi/2, R=I-D Phi,
    Gamma_y=-(H^T diag(y)V-V^T diag(y)H)/2,
    J_y=P Gamma_y P,
    U_n=diag(Vn)H-diag(Hn)V.

Here Phi is the actual pinned lower prefix and q adds endpoint values.
Use L185/L187's full expansion

    SB_i=a^2 sum_(k,l)d_(i;kl)n_k e_l^T, n_k=S e_k,
    ||e_l||_infinity<=C a^2,
    sum_(k,l)|d_(i;kl)|p(k)p(l)<=C_(i,p)               (1)

for every fixed polynomial p. The e_j are the ordinary orthonormal
relative Hodge product modes, with component labels included. Define
E_K to be their orthogonal projection onto all allowed four-indices
max_mu j_mu<=K, for integers 1<=K<=N-1. Include every component
with such an index and every allowed zero own-direction index.

For any signed supported matrix X=PXP define the linear functional

    Q_(i,N)[X]=-6a^2 sum_(k,l)d_(i;kl)
                         Tr(J_(e_l) X U_(n_k)^T P).   (2)

L187's identity gives Q_(i,N)[M]=Q_(3,i,N), the entire third
quartic placement. In particular (2) is its original signed order.

## Conclusion

Put

    M_K^hi=(I-E_K)M(I-E_K),
    M_K^lo=M-M_K^hi=E_K M+(I-E_K)M E_K.              (3)

There is a constant independent of N,K such that

    |Q_(i,N)[M_K^lo]|<=C_i N^(-1/2)K^15.             (4)

For K_N=floor(N^(1/6)), and sufficiently large N, this yields

    Q_(3,i,N)=Q_(i,N)[M_(K_N)^hi]+O_i(N^2),
    a^3{Q_(3,i,N)-Q_(i,N)[M_(K_N)^hi]}=O_i(N^-1),   (5)
    G_(i,a)=-Q_(i,N)[M_(K_N)^hi]+o(N^3).             (6)

Here G is L202's original joint cubic probe-jet group. The retained
trace is O_i(N^3) by L202 and (5), but has no proved scaled limit
or coefficient. For each fixed K, (4) even tends to zero without
cubic scaling. It does not estimate the high/high corner uniformly
as K approaches N, or localize either moving prefix. No existence,
vanishing or sign of the complete cubic limit follows.

This is a local consequence of existing smooth-column consistency
and finite matrix estimates, not progress beyond the sources checked.
Independent f_(i,2),r_0, full compensation, finer asymptotics, finite
matching, reflected error <=c_box/2 and continuum/infrared construction
remain unresolved.

## Proof

### 1. The cutoff preserves covariance support without commuting with M

For each four-index the relative one-form product modes span a block
of at most four components. As recorded in L187, proof section 4,
P is the orthogonal projection I-dd^T/|d|^2 within the block when
all four indices are positive. If an index is zero, its sole allowed
own-direction component is already co-closed. E_K either retains
or removes each whole block. Thus E_K P=P E_K, and the two matrices
in (3) satisfy X=PXP. This does not assert E_K M=M E_K or any
commutation with A, a multiplier, H, V or Phi.

There are at most 4(K+1)^4 retained product modes. Write their index
set as I_K and put m_j=M e_j. L185(5), with Delta_phys denoting
the physical relative Hodge Laplacian, is the exact formula

    m_j=2 lambda_j^(-1) Delta_phys^(-1) N_a f_j,
    e_j=a^2 f_j.                                    (7)

The full inverse estimate L028(8) and its positive spectral gap give

    ||m_j||_infinity<=C a^2(1+|j|)^11,
    ||m_j||_2<=C(1+|j|)^11.                          (8)

The second bound follows because there are at most 4N^4 variable
links and N^2 a^2=64. L028's degree eleven estimate holds for every
allowed j, not just fixed j. No assumption about a rough column of M
is being made: (8) applies to its individual product-mode columns.

Symmetry of M and the exact identity (3) give the rank-one expansion

    M_K^lo=sum_(j in I_K)
       {e_j m_j^T+((I-E_K)m_j)e_j^T}.                (9)

Both mixed low/high corners are included, and the low/low corner
is counted once. Since ||I-E_K||<=1, the sum of the products of
the two vector norms in (9) is at most

    2 sum_(j in I_K)||m_j||_2<=C K^15.               (10)

Indeed |j|<=2K and the number of modes is at most 4(K+1)^4.
The individual e_j need not be co-closed; the whole matrix (9) is
supported by P, and the explicit projections in (2) remain.

### 2. Retain the upper jump in the projected deterministic factor

Let Pi select precisely the upper direction-1 normal variable links.
The full pinned product identity L187(3) gives, on every input,

    P U_(n_k)=P{diag(alpha_k)-diag(beta_k)V},
    alpha_k=Vn_k, beta_k=Rn_k.                        (11)

L187(15) supplies

    ||alpha_k||_infinity<=C N p(k),
    ||(I-Pi)beta_k||_infinity<=C p(k),
    ||Pi beta_k||_infinity<=C N p(k).                (12)

The raw prefix has ||Phi||_op<=N and q has bounded norm, so
||V||_op<=C N. On an upper normal edge, however, its V row is
exactly the sum of the N-1 lower axial links in that transverse
fiber. Its boundary endpoint contributes zero. Different transverse
fibers use disjoint source links. Therefore

    ||Pi V||_op=sqrt(N-1).                           (13)

This is a statement about the original raw prefix row, not about
Pi P V or a covariance restriction. Every source in that prefix
is retained. Combining (11)--(13) before taking norms gives

    ||P U_(n_k)||_op
       <=C p(k){N+N+N sqrt(N-1)}
       <=C' p(k)N^(3/2).                            (14)

In particular the upper jump is kept at its O(N) amplitude. No
selector has been moved through P.

### 3. Test the original signed trace against the complete low corner

The bounded incidence degree gives ||H||_op<=C N, while
||V||_op<=C N. Thus (1) and the exact definition of J give

    ||J_(e_l)||_op
       <=||H||_op ||e_l||_infinity ||V||_op<=C.       (15)

For any real vectors u,v, finite trace evaluation yields

    |Tr(J_(e_l) u v^T U_(n_k)^T P)|
       =|(P U_(n_k)v)^T J_(e_l)u|
       <=C p(k)N^(3/2)||u||_2||v||_2.              (16)

Apply (16) to every term of (9), then (10) and the full exterior
sum (1) in (2). This proves

    |Q_(i,N)[M_K^lo]|
       <=C_i a^2 N^(3/2)K^15
       =C_i' N^(-1/2)K^15,

as asserted. Positivity of M, entrywise covariance comparison and
commutation with M are absent from this estimate.

Finally K_N^15<=N^(5/2), so (4) is O_i(N^2) for that choice.
Equations (5) follow by linearity. L202's G=-Q_3+o(N^3) and
Q_3=O_i(N^3) give (6) and the retained cubic bound. These are
algebraic replacements with an explicit uniform error; no mesh/cutoff
limit has been interchanged and no high/high convergence is assumed.

All checks here are analytic. The rank-one expansion (9) retains
both mixed corners; its bound uses 11+4=15, and the response exponent
is -2+3/2=-1/2. The growing-cutoff exponent is -1/2+15/6=2,
strictly below the required cubic threshold. No mathematical script
or numerical preview is used as evidence.

The covariance-only obstruction in L197 is unchanged: the present
estimate uses the actual smooth-column cancellation in M=2SAS.
L076 removes a different left trace sector, and does not supply (4).
The high/high residual still carries all signed interactions and both
moving prefixes. The estimate does not imply its finite scaled limit.

## Mathlib

Full matching actual-probe low-corner estimate and remaining cubic
limit: **not checked**. Supporting spectral projections, rank-one
traces and operator ideal coverage: **not checked**; unknown coverage
is not absence. The smooth-column and projection inputs are imported
from L028, L185 and L187, and the joint reduction from L202. The
only additional specialization is the original upper-prefix row count
and the full rank-one low-corner test; no general Gaussian or flow
renormalization theorem is reproved. The unchanged
[approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers this partial estimate within its joint-group target. No
literature refresh or originality claim is made.
