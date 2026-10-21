# L086 — The complete other/other same-row class is subleading

## Hypotheses

Use L085's SU(2) Gaussian on the all-face pinned box, straight
lower-rooted direction-1 forest, admitted even N, a=8/N, both actual
L010 probes i=3,6 at tau=1/16 and the actual residual of L018.
Take the bare small-coupling coefficient at fixed mesh before refinement.
All norms use ordinary dimensionless stored coordinates. Retain every
transverse plaquette at each level 1<=s<N, all pinned end rows, all
colors and the complete exterior heat sums. Import L085's row selectors
J_alpha=(c_alpha,b_alpha,q_alpha), covariance S and blocks C,U,V,Z.
Here alpha=(s,p), beta=(t,q) range over the complete ordered pair set,
including coincident pairs. In particular

    Z_ab=J_alpha(S B S A S+S A S B S)J_beta^T.

Define, without the outside factor 3,

    T_Z=sum_(alpha,beta) sum_(j=1)^3 det C_ab[j:Z_ab],
    T_UV=sum_(alpha,beta) sum_(j!=k) det C_ab[j:U_ab,k:V_ab].

L085(5) is the exact complete response O_i=3(T_Z+T_UV), where
O_i=(1/2) kappa(f_(i,0),r0,Y,Y) and Y=S3-S3_top.
Constants may depend on the fixed probes, displacement, box and flow
time, but not on sufficiently fine admitted meshes.

## Conclusion

The complete same-row class, retaining both covariance path orders,
satisfies

    |T_Z| <= C_i N^(3/2),
    a^3 T_Z = O_i(a^(3/2)) -> 0.                         (1)

In fact the estimate bounds the sum of the absolute values of all its
cofactor monomials. The explicit two-gradient base term in L085(6)
separately satisfies

    sum_(alpha,beta) min(s,t)^2 |(Z_ab)_11|
                     |det (G_ab)_[2,3],[2,3]| <= C_i N.  (2)

Consequently the approved leading-scale question reduces exactly to
the six distinct-row terms:

    a^3 O_i - 3 a^3 T_UV -> 0.                           (3)

Thus cancellation of L084's coefficient by this group would require
lim a^3 T_UV=-4 gamma D_i for each i. Neither that limit, its existence,
its sign nor exclusion of stronger powers in T_UV is established.
No bound below is applied to its rough residual block V. No complete
response, logarithm, finite matching, interacting error <=c_box/2,
continuum construction or physical mass statement follows.

## Proof

### 1. Full two-level covariance norms

Use L085(2), with the entire transverse edge space E and axial
levels 1,...,N-1. Write M_st=min(s,t), let Pcal=I tensor P and set

    R=(L_D tensor I+I tensor Delta_T)^(-1),
    K=M tensor P+R(I-Pcal).                              (4)

The transverse projection commutes with Delta_T, hence with R.
This is the actual interior link covariance. It is not an upper-source
row or a tilted-law covariance identity. Let E_1=D be the transverse
circulation, and E_2,E_3 the two-edge signed path maps selecting b,q.
Their norms are bounded independently of N: each row has at most four
unit signed entries and each edge occurs in a bounded number of rows.
The same bound holds on all relative end rows, where fixed entries are
zero. The scalar-entry arrays of L085's blocks are therefore

    mathcal C_jb=(I tensor E_j) K (I tensor E_b)^T,       (5)

with rows and columns indexed by all alpha,beta. Norms below are norms
of these full arrays, not estimates at one axial level.

We first verify a complete spectral bound used for the resolvent part:

    Tr R <= C N^4,    ||R||_op <= C N^2,
    ||R||_HS <= C N^3.                                 (6)

Indeed L026(6)-(7)'s relative tensor spectrum, restricted to the
transverse components at interior axial vertices, gives eigenvalues

    rho_k=4 sum_(j=1)^4 sin^2(pi k_j/(2N))
          >=4 |k|^2/N^2.

Here k_1 is in 1,...,N-1; the transverse component's own index is in
0,...,N-1, and the other two transverse indices are in 1,...,N-1.
All three components are counted. There is no zero eigenvalue.
The shell max_j k_j=m contains at most C m^3 indices, so

    Tr R <= C N^2 sum_(m=1)^(N-1) m^3/m^2 <= C' N^4.

The same lower eigenvalue bound gives ||R||_op<=C N^2.
Positivity then gives Tr R^2<=||R||_op Tr R<=C N^6.
This proves (6); no logarithmic refinement of this deliberately coarse
Hilbert-Schmidt bound is needed. Restriction to ker Pcal only decreases
these positive spectral traces.

L085's cochain identities D P=0 and D^T D=Delta_T(I-P)
remove the gradient part whenever an endpoint is curvature. If mu_k
is an axial Dirichlet eigenvalue and lambda a transverse eigenvalue
on ker P, the nonzero curvature/curvature eigenvalues are
lambda/(mu_k+lambda). They are at most one and their number is O(N^4).
For curvature/link, the squared Hilbert-Schmidt norm is exactly

    ||(I tensor D) R(I-Pcal)||_HS^2
        =sum_(k,lambda in ker P) lambda/(mu_k+lambda)^2
        <=sum_(k,lambda in ker P) 1/(mu_k+lambda)
        <=Tr R <= C N^4.                               (7)

Using the bounded path maps, (7), and transposition of the full
covariance gives

    ||mathcal C_11||_HS <= C N^2,
    ||mathcal C_1b||_HS+||mathcal C_b1||_HS <= C N^2
                                      (b=2,3).         (8)

This N^2 curvature-array estimate respects L085's lower bound;
it does not reuse the false N^(3/2) full-array estimate.

For path/path, ||M||_HS^2=sum_(s,t) min(s,t)^2<=N^4 and
||P||_HS^2=rank P=(N-1)^3<=N^3. The Kronecker-product norm
and (6) consequently imply

    ||K||_HS <= N^(7/2)+C N^3 <= C' N^(7/2),
    ||mathcal C_jb||_HS <= C N^(7/2)  (j,b=2,3).        (9)

Both the Brownian-prefix part and the complete interior resolvent are
retained. There is no bulk-profile or physical-boundary replacement.

### 2. Actual exterior columns at both interior endpoints

Import L028, proof sections 1-3, for the centered residual consistency,
relative inverse, normalization and full heat expansion of S B S A S.
Import its transverse-row specialization proved in L062, proof
section 3, equation (11), including transverse end edges. Those rows
are precisely the present J_alpha at each 1<=s<N. Applying that
estimate independently to alpha and beta gives, with h=(a^2,a,a),

    |(J_alpha v_k)_j| <= h_j p(k),
    |(J_alpha z_k)_j| <= a^2 h_j p(k),                 (10)

and the same inequalities at beta. The polynomial p is mesh independent.
The columns v_k are covariance-square-root columns; z_k have the
actual residual on that smooth input. They are not rough columns of V.

The endpoint applicability is essential. Each transverse stored link
of a smooth relative one-form is a times its direct sample plus a
prefix of transverse differences. Its size is bounded by C a times
the C^1 norm because the prefix has physical length at most 8. A
transverse circulation cancels that prefix gradient exactly, leaving
size C a^2. Relative tangential zero values give the same statements
at transverse boundary endpoints, including plaquettes adjacent to a
fixed face. There is no transverse link at s=N in this group, so the
separately pinned upper-face jump is not used. L028's residual inverse
column has an additional uniform a^2 in its C^1 norm; this proves
the second line of (10) with the same endpoint reasoning.

For completeness the actual full expansion, with physical relative
eigenvalues nu_k and L028's uniformly bounded matrix B_i^rel, is

    (Z_ab)_jb=sum_(k,l) exp[-tau(nu_k+nu_l)] (B_i^rel)_kl
       [(J_alpha v_k)_j (J_beta z_l)_b
        +(J_alpha z_l)_j (J_beta v_k)_b].              (11)

Symmetry of B_i^rel identifies the second summand with the transpose
path order after swapping k,l. Both orders are retained. No residual
is commuted through the heat operators. The lower spectral bound
nu_k>=c|k|^2 and the uniform matrix bound make the sum of
exp[-tau(nu_k+nu_l)] p(k)p(l) mesh uniformly finite. Thus

    |(Z_ab)_jb| <= C_i a^2 h_j h_b                    (12)

uniformly over all ordered alpha,beta. In particular the entry orders
are a^6 for 11, a^5 for 1b or j1 with j,b>1, and a^4 for j,b>1.
Every exterior heat mode has been summed before this bound is used.

### 3. Exhaust the cofactors before taking the scale limit

For each fixed ordered pair, the sum of the three row replacements
is the first differential of the determinant:

    sum_j det C[j:Z]=sum_(j,b) Z_jb cof_jb(C).          (13)

Each cofactor has exactly two signed products of base entries.
For any such product the full pair sum is bounded by

    sum_(alpha,beta) |C_ru C_tv|
       <=||mathcal C_ru||_HS ||mathcal C_tv||_HS.       (14)

Combine (8)-(9), (12) and (14). The following table covers all nine
positions of Z and both monomials in each cofactor. Here j,b>1;
the table lists absolute upper bounds, not signed asymptotics.

| Z position | Product types in its cofactor | Bound after summation |
| --- | --- | --- |
| 11 | path/path times path/path | C a^6 N^7 = O(N) |
| 1b | path/curvature times path/path | C a^5 N^(11/2) = O(N^(1/2)) |
| j1 | curvature/path times path/path | C a^5 N^(11/2) = O(N^(1/2)) |
| jb | curvature/curvature times path/path, or curvature/path times path/curvature | C a^4 (N^(11/2)+N^4) = O(N^(3/2)+1) |

There are respectively 1,2,2,4 entries of the four types, with a
fixed factor two for cofactor products. Since a=8/N, their sum proves
(1), even before cancellation between monomials or ordered pairs.

For (2), repeat just the 11 cofactor estimate with both base factors
replaced by their gradient parts M tensor P. Each selected path/path
array then has Hilbert-Schmidt norm at most C N^(7/2).
Their product contains exactly min(s,t)^2 times the corresponding
product of G entries. The uniform a^6 bound on Z_11 and (14) prove
(2), including the absolute value of the difference defining the minor.
No estimate of the other terms in L085(6) is inferred from this alone.

Finally insert (1) into the imported complete identity O_i=3(T_Z+T_UV).
This proves (3). The factor 3 is applied once; the ordered-pair
normalization +1/2 has already been included by L085. Comparing with
L084's complete mixed coefficient 12 gamma D_i gives the necessary
value -4 gamma D_i for lim a^3 T_UV. This comparison adds no numerical
assumption to (1)-(3); any assertion about signs of D_i would retain
L082's saved-table and IEEE qualifications.

### 4. Scope of this attempt

The unchanged EXPLORE assessment is
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
L048/L085 supply the established complete contraction rather than a
new pairing enumeration. L028/L062 supply the smooth exterior columns.
The required additional specialization is their two-interior-endpoint
use with the full spectral array bounds (6)-(9). This proves a relevant
subleading bound within the approved complete-group question; it does
not approve a new target or claim a full a^3 limit.

This is local REPRODUCTION of the recorded finite spectral and Gaussian
methods, not a claim of a theorem beyond the sources checked. The proof
is analytic: its checks are the complete spectrum, all endpoint cases,
both residual orders, all cofactor positions and the original factor 3.
No mathematical script or numerical asymptotic evidence is needed.
The six distinct-row terms, including their actual rough V blocks,
remain. Other jets, finer powers and logarithms, nonlinear forest
compensation and all interacting continuum/mass gaps remain independent.

## Mathlib

Full matching coverage: **not checked**. Supporting finite spectral,
Hilbert-Schmidt, Kronecker-product and determinant-differential coverage:
**not checked**. Unknown availability is not absence. The finite
Gaussian contraction is imported from L048/L085, with the present
unchanged law and ordered region; no continuum Ward or flow finiteness
theorem is used to assign this group's coefficient.
