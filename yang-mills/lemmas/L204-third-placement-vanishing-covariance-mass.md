# L204 — A vanishing covariance mass has subcubic third-placement error

## Hypotheses

Use L187, L202 and L203's SU(2) setting: relative box (-4,4)^4,
sufficiently fine admitted even N, a=8/N, straight lower-rooted
direction-1 forest, complete compact L008 displacement and both
actual L010 probes i=3,6 at tau=1/16. The bare expansion is taken
at fixed mesh before refinement. Use ordinary full variable-link
coordinates and Euclidean adjoints. Retain all physical faces,
normal end edges, allowed constant own-direction modes and the
complete exterior heat sum. Vertex potentials are pinned on every
physical boundary vertex.

Let Delta be the dimensionless relative one-form Hodge Laplacian,
Delta_phys=a^(-2)Delta, P the co-closed orthogonal projection,
S=P Delta^(-1), A=PAP the complete signed symmetric residual with
both insertion subtractions, and M=2SAS. Keep L203's definitions

    V=q Phi, H=I-D Phi/2, R=I-D Phi,
    Gamma_y=-(H^T diag(y)V-V^T diag(y)H)/2,
    J_y=P Gamma_y P,
    U_n=diag(Vn)H-diag(Hn)V.

Phi is the original pinned lower prefix. For its complete heat expansion
and signed trace functional use

    SB_i=a^2 sum_(k,l)d_(i;kl)n_k e_l^T, n_k=S e_k,
    sum_(k,l)|d_(i;kl)|p(k)p(l)<=C_(i,p),
    Q_(i,N)[X]=-6a^2 sum_(k,l)d_(i;kl)
                          Tr(J_(e_l) X U_(n_k)^T P).       (1)

Here p is any fixed polynomial, e_j are all ordinary orthonormal
relative Hodge product modes, including component labels, and
Q_(i,N)[M]=Q_(3,i,N). For 1<=K<=N-1 let E_K be L203's
projection onto all complete component blocks with max_mu j_mu<=K.
In particular E_K commutes with P and Delta, but is not assumed
to commute with A, M, a prefix or a multiplier.

For epsilon>0 define the resolvent filter and massive covariance

    F_epsilon=Delta(Delta+epsilon I)^(-1),
    S_epsilon=P(Delta+epsilon I)^(-1),
    M_epsilon=2S_epsilon A S_epsilon.                       (2)

This F_epsilon is a resolvent filter, distinct from the square-root
filter in L201. No other factor in (1) is regularized.

## Conclusion

Uniformly in N, K and epsilon>0,

    |Q_(i,N)[M]-Q_(i,N)[M_epsilon]|
      <=C_i {N^(-1/2)K^7
           +N^(7/2) min(1,epsilon N^2/K^2)}.               (3)

The supporting improvement of L203's low-corner estimate is

    |Q_(i,N)[M-(I-E_K)M(I-E_K)]|
                                  <=C_i N^(-1/2)K^7.       (4)

In particular take epsilon_N=N^(-7/4) and K_N=floor(N^(7/16)).
Then

    Q_(3,i,N)=Q_(i,N)[M_(epsilon_N)]+O_i(N^(23/8)),
    a^3 |Q_(3,i,N)-Q_(i,N)[M_(epsilon_N)]|
                                              <=C_i N^(-1/8), (5)
    G_(i,a)=-Q_(i,N)[M_(epsilon_N)]+o(N^3).                 (6)

Here G is the original joint cubic probe-jet group from L202.
The massive trace is cubic-bounded, by L202 and (5). The mass
vanishes; its inverse square root N^(7/8) is o(N). These numerical
scales alone do not prove localization of the complete trace or
permit substitution into a fixed-mass limit theorem. Both prefixes,
their upper jump, every projection and the original exterior columns
remain in (1). No scaled limit, coefficient, sign, vanishing or full
compensation has been proved.

This is a local specialization of existing smooth consistency and
finite matrix estimates, not progress beyond the checked sources.
Independent f_(i,2),r_0, finer asymptotics, finite matching, interacting
reflected error <=c_box/2, continuum axioms and infrared finite
positive mass remain unresolved.

## Proof

### 1. Use a smooth column's L2 norm rather than its supremum

Write ||v||_a=a^2||v||_2 for the stored full-link norm; all component
weights are a^4. L185(5) gives, with e_j=a^2 f_j and physical
eigenvalue lambda_j,

    m_j:=M e_j=2 lambda_j^(-1) Delta_phys^(-1) N_a f_j.   (7)

L028(5) at r=0 bounds the compact smooth extension of N_a f_j by
C a^2(1+|j|)^5. The box volume and number of components are uniformly
bounded, so this is also a bound for its ||.||_a norm. The full
physical relative inverse has a uniform L2 operator bound by its
positive spectral gap. Consequently

    ||m_j||_2
      <=C a^(-2)lambda_j^(-1)||N_a f_j||_a
      <=C lambda_j^(-1)(1+|j|)^5
      <=C'(1+|j|)^3.                                   (8)

The last step uses L028's lambda_j>=|j|^2/16 and the absence of a
zero full one-form mode. An allowed zero own-direction index is
included and causes no exception. This holds for every admitted
mode j, not just fixed j. No supremum estimate on m_j is needed;
the six extra derivatives in L028(8) are therefore unnecessary here.
No smoothness is asserted for a general rough column of M.

Set Q_K=I-E_K and M_lo=M-Q_K M Q_K. Symmetry of M gives L203's
exact rank-one expansion

    M_lo=sum_(j in I_K){e_j m_j^T+(Q_K m_j)e_j^T}.        (9)

There are at most 4(K+1)^4 indices in I_K, each with |j|<=2K.
By (8), the sum of the products of vector norms in (9) is at most
C K^7. Both mixed corners remain and the low/low corner occurs once.

L203's original-order deterministic estimates are

    ||J_(e_l)||_op<=C,
    ||P U_(n_k)||_op<=C p(k)N^(3/2).                   (10)

The second retains the O(N) upper exterior jump and the upper raw
prefix row of norm sqrt(N-1). For arbitrary vectors u,v, they imply

    |Tr(J_(e_l)u v^T U_(n_k)^T P)|
       <=C p(k)N^(3/2)||u||_2||v||_2.                 (11)

The rank-one summands need not be individually co-closed; (11)
is an identity and inequality for all vectors, and their total is
supported by P. Apply (11) to (9), multiply by a^2 in (1), and
sum the complete heat coefficients. This proves (4), since
a^2 N^(3/2)=64 N^(-1/2).

### 2. The same low-corner bound survives the filter

By the finite-dimensional spectral theorem F_epsilon is a self-adjoint
contraction and commutes with S, P and E_K. In particular

    F_epsilon S=S_epsilon,
    F_epsilon M F_epsilon=M_epsilon.                   (12)

No commutation with A is used in the second equality: its two
covariance legs are changed in place. Applying F_epsilon on both
sides of each rank-one term in (9) only decreases its vector norm
product. Thus (11) proves, uniformly even for an N-dependent mass,

    |Q_(i,N)[M_lo]|+|Q_(i,N)[F_epsilon M_lo F_epsilon]|
                                      <=C_i N^(-1/2)K^7. (13)

This does not require a smooth filtered column or a positive M.

### 3. Bound both mass-difference placements in the high corner

Put E_A=S^(1/2) A S^(1/2); L186(12) gives ||E_A||_op<=C N,
with both residual subtractions retained. Since Q_K commutes with
S, the high corner has its exact whitened order

    M_hi=Q_K M Q_K
         =2S^(1/2) Q_K E_A Q_K S^(1/2).               (14)

On a removed product mode max_mu j_mu>K, the dimensionless
eigenvalue is a^2 lambda_j>=4(K+1)^2/N^2. Hence, writing
D_epsilon=I-F_epsilon,

    delta:=||D_epsilon Q_K||_op
         <=min(1,epsilon N^2/[4(K+1)^2]).              (15)

This follows directly from 1-t/(t+epsilon)=epsilon/(t+epsilon)
for t>0. It uses the full product spectrum, including the allowed
constant modes, rather than a scalar Dirichlet replacement.

In the original order,

    M_hi-F_epsilon M_hi F_epsilon
       =D_epsilon M_hi+F_epsilon M_hi D_epsilon.       (16)

For a fixed pair k,l, L187(16)--(17), with its repaired transpose
order, supplies

    ||J_(e_l)S^(1/2)||_HS<=C N^(3/2),
    ||P U_(n_k)S^(1/2)||_HS<=C p(k)N^3.               (17)

For the first term of (16), its trace in (1) is 2Tr(X E_A Y^T),
where

    X=J_(e_l)S^(1/2)D_epsilon Q_K,
    Y=P U_(n_k)S^(1/2)Q_K.

Equations (15),(17) give ||X||_HS<=C delta N^(3/2) and
||Y||_HS<=C p(k)N^3. For the second term, use instead

    X=J_(e_l)S^(1/2)F_epsilon Q_K,
    Y=P U_(n_k)S^(1/2)D_epsilon Q_K.

The factor delta now belongs to Y; the other filter is a contraction.
In both cases the signed finite trace inequality

    |Tr(X E_A Y^T)|<=||X||_HS ||E_A||_op ||Y||_HS

therefore gives C p(k)delta N^(11/2). The contractions occur at
the right ends of the factors in (17), never across a prefix,
multiplier or E_A. Multiplication by a^2 and the complete heat sum
prove

    |Q_(i,N)[M_hi-F_epsilon M_hi F_epsilon]|
                                        <=C_i delta N^(7/2). (18)

Combining (13),(16),(18) proves (3). Positivity of M, covariance
commutation, smoothing of the rough tilt and cyclic removal of
transport have not been used.

### 4. Choose a subcubic mass schedule and identify the remaining gap

For sufficiently large N, K_N=floor(N^(7/16)) lies in [1,N-1]
and is at least N^(7/16)/2. With epsilon_N=N^(-7/4), the two
terms on the right of (3) have bounds

    N^(-1/2)K_N^7 <=N^(41/16),
    N^(7/2)epsilon_N N^2/K_N^2 <=4N^(23/8).           (19)

Both powers are strictly below 3; 41/16<23/8=3-1/8.
Multiplying by a^3 gives (5). L202's Q_3=O_i(N^3) and
G=-Q_3+o(N^3) then give cubic boundedness of the massive trace
and (6), with the original subtraction sign.

The exact remaining matrix also equals

    M_(epsilon_N)
      =2(Delta+epsilon_N I)^(-1) A
                                 (Delta+epsilon_N I)^(-1), (20)

because A=PAP and P commutes with the resolvent. Equation (20)
removes only redundant projections adjacent to A; J, U, their
prefixes and every covariance source remain in (1). Its natural
mass length is epsilon_N^(-1/2)=N^(7/8), with physical length
a epsilon_N^(-1/2)=8N^(-1/8). This identifies a possible scale
for a future direct approximation, not a proved kernel-tail or
signed-trace localization estimate. Earlier fixed-mass convergence
arguments cannot be invoked with this varying mass merely because
(5) holds. The entire massive signed trace still needs a limit.

All checks here are analytic: weighted-to-ordinary norm conversion,
the degree 5 minus the eigenvalue's degree 2, the O(K^4) mode count,
both placements of (16), the upper-row bounds imported in (17),
and both exponents in (19). No numerical evidence or mathematical
script is used. The bound improves a route to the original joint
limit without determining that limit or any independent construction
requirement. The older stopped factorwise routes remain stopped.

## Mathlib

Full matching actual-probe mass estimate and cubic limit: **not checked**.
Supporting finite-dimensional spectral theorem, resolvent calculus,
rank-one traces and Hilbert--Schmidt ideal inequalities: **not checked**;
unknown coverage is not evidence of absence. The smooth consistency,
spectral gap and exact covariance-column formula are imported from
L028 and L185; the signed form and trace estimates from L186--L187;
the original low-corner decomposition and deterministic operator
bounds from L203; and the joint reduction from L202. Their L2
specialization and two ordered mass-difference placements are needed
here. No general Gaussian or renormalization theorem is reproved.
The unchanged [approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers this step within the exact joint-group target. No literature
refresh, novelty claim or completed joint-limit claim is made.
