# L063 — Mixed residual derivatives on the upper-curvature row

## Hypotheses

Use L062's actual SU(2) straight-forest Gaussian, covariance S, residual
A, and both original quadratic probes B=B_i, i=3,6, with tau=1/16,
a=8/N through admitted even meshes. The small-coupling coefficient is
taken at fixed mesh first. Retain every upper transverse edge e and
every transverse plaquette p at levels 1<=s<=N-1, including pinned
end edges and zero fixed rows. Use exactly its row maps
R'_e=(d_e,u(v),(Tu)_e), J'_p=(c_p,b_p,q_p), and blocks C',U',V',Z'.
All norms below are ordinary dimensionless-coordinate norms. Constants
may depend on the fixed box, displacement, probe and flow time.

## Conclusion

Define the two terms whose residual derivative occupies row 1 by

    D_i(a) = sum_(e,p) [det C'[2:U',1:V']
                       + det C'[3:U',1:V']].                 (1)

Then

    |D_i(a)| <= C_i a^(-3/2),     a² D_i(a) -> 0.             (2)

In particular L062's exact complete mixed response can be written

    M_i = 6 (T_Z + D_i + T_rem),
    T_rem = sum_(e,p) sum_((j,k) in I) det C'[j:U',k:V'],
    I = {(1,2),(1,3),(2,3),(3,2)}.                            (3)

Thus a²(M_i-6 T_rem)->0 by L062 and (2). No bound or limit for
T_rem is asserted. Neither this reduction nor conditional centering
assigns L059's conditional coefficient to M_i. The five removed terms
must be restored when studying subleading powers and logarithms.
Other cubic pairs, measure and insertion/flow jets, nonlinear forest
compensation, finite matching, the reflected-error threshold c_box/2,
continuum axioms, infrared control and finite positive mass remain open.

## Proof

### 1. Bound the actual transverse-link covariance columns

Write Sigma for the full Hodge covariance in dimensionless coordinates,
and A_0 for the full Hodge residual. For a linear forest row t, denote
its lifted full-link row transpose by r_t and put x_t=Sigma r_t.
L018's exact linear quotient transfer and free gauge invariance of
the quadratic residual give

    V'_(1b) = x_(d_e)^T A_0 x_(J'_p,b).                      (4)

This transfers the specified quadratic covariance product with its
lifted rows; it makes no transfer claim for unmodified higher vertices.
In particular d_e and c_p are actual relative plaquette circulations,
since D_1 R_F=D_1. The Hodge projection identity gives

    r_(c_p)^T Sigma r_(c_p) <= 1,
    ||Sigma|| <= C N²,
    ||x_(c_p)|| <= C N.                                      (5)

The norm inequality follows from Sigma²<=||Sigma|| Sigma. It also
holds for a zero or degenerate fixed-boundary plaquette row.

For the other two right rows we need a variance bound for every
transverse forest link at every level s<N, including end edges.
L026 proves Var(x_mu(s,v))<=s+8 when both endpoints are interior.
Its upper-bound argument extends as follows, without extending its
lower bound. The exact lift is a direct component-mu Hodge link minus
the difference of the two length-s axial root sums. At a pinned
transverse endpoint the corresponding component-1 coordinates are
absent and have value zero. Let T_mu be the transverse relative
difference on component-1 links. The root difference still has
coefficient row T_mu^T b, where b has one unit entry at each of the
s plaquettes along this strip, so ||b||²=s. The relative inequality

    T_mu^T T_mu <= Delta_1

holds with these pinned rows as well, by the componentwise relative
Laplacian decomposition. Hence

    b^T T_mu Sigma_1 T_mu^T b <= ||b||²=s.                    (6)

L026's full tensor-spectrum diagonal bound gives direct-link variance
at most 8. That link and the axial root difference belong to different
Hodge components and have zero covariance. A link contained in a
boundary face is zero; for an end edge normal to that face the same
strip with the missing endpoint is precisely (6). Thus, uniformly
over all right-hand links used here,

    Var(x_mu(s,v)) <= s+8 <= N+8.                            (7)

Both b_p and q_p are sums of two signed links. The covariance form of
Cauchy–Schwarz, without any independence assumption between these
links, bounds each variance by 4(N+8). Combining with the Hodge gap
as in (5) yields

    ||x_(b_p)|| + ||x_(q_p)|| <= C N^(3/2).                  (8)

The gap and projection in (5) are the same full-spectrum identities
used in L041. Equations (6)–(8) do not assume localization in s, omit
the gradient sector of a link, or truncate a transverse mode.

### 2. Apply the residual only to the separated source

L041, proof section 2, equation (10), proves

    ||A_0 x_(d_e)||_2 <= C a^5                               (9)

uniformly over all upper edges, including transverse end edges. Its
hypothesis is separation of the upper circulation source from the
fixed compact coefficient support. It does not require separation
of the second row in (4). A_0 is symmetric. Applying Cauchy–Schwarz
to (4), with (5), (8) and N=8/a, gives the actual mixed-block bounds

    |V'_11| <= C a^4,
    |V'_12| + |V'_13| <= C a^(7/2).                          (10)

This is the only small rough-residual estimate used. In particular
there is no assertion that all of V' obeys L054's upper/upper form
bound, and no smooth-input estimate is applied to x_(b_p) or x_(q_p).

### 3. Retain the heat column and count all pair indices

L028's exterior covariance/probe identity without its residual factor
gives, in L062's row coordinates,

    U' = sum_(k,m) exp[-tau(lambda_k+lambda_m)] B^rel_(i;km)
                      (R' v_k)(J' v_m)^T.                   (11)

L062(10)–(11) give |R'v_k|<=(a²,1,a)p(k) and
|J'v_m|<=(a²,a,a)p(m), including every pinned row. The uniform
bound on B^rel and complete heat-weighted polynomial summability
therefore imply

    |U'_21|<=C_i a²,   |U'_22|+|U'_23|<=C_i a,
    |U'_31|<=C_i a³,   |U'_32|+|U'_33|<=C_i a².               (12)

Only the probe block is estimated with heat columns.

At the base law L062(5) writes rows 2 and 3 of C' as
(0,H_2,H_3) and (0,J_2,J_3). Its equation (9) bounds the complete
arrays H_b,J_b, b=2,3, in Hilbert–Schmidt norm by C N³. There are
O(N³) upper edges and O(N⁴) transverse plaquettes over all levels,
hence O(N⁷) pairs. Ordinary finite-array Cauchy–Schwarz consequently
gives

    sum_(e,p) (|H_2|+|H_3|+|J_2|+|J_3|) <= C N^(13/2).     (13)

The count includes all levels, orientations, collars and end edges.
It uses no decay profile in the axial direction.

### 4. Expand both determinants with all curvature derivatives intact

For the first term in (1), the three rows are V'_1,U'_2,C'_3.
Its determinant is

    V'_11(U'_22 J_3-U'_23 J_2)
      - U'_21(V'_12 J_3-V'_13 J_2).                          (14)

For the second they are V'_1,C'_2,U'_3, giving

    V'_11(H_2 U'_33-H_3 U'_32)
      + U'_31(V'_12 H_3-V'_13 H_2).                          (15)

These expansions use only the zeros in the undifferentiated base
row. They keep U'_21,U'_31 and V'_11; none is differentiated away
using a base-law zero. Applying (10), (12), (13) to every monomial
in (14)–(15) bounds their absolute sums respectively by

    C_i (a^5+a^(11/2)) N^(13/2)
       = O_i(a^(-3/2)+a^(-1)),
    C_i (a^6+a^(13/2)) N^(13/2)
       = O_i(a^(-1/2)+1).                                   (16)

Their sum proves (2). Removing precisely these two ordered placements
from L062's six gives the four pairs in (3); the normalization +6
is unchanged. All bounds are absolute, so no unproved signed
cancellation is used.

The analytic checks cover the mixed lift (4), both kinds of pinned
right edge, the untruncated Hodge gap, uniformity of (9) in the upper
source, the full pair count, and all monomials in (14)–(15). No
numerical check is needed for these estimates. This is local
REPRODUCTION using finite spectral inequalities and Cauchy–Schwarz
under the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`. The specialization
is the mixed upper/interior row and its retained boundary cases;
general flow finiteness and stress matching are not reproved.
No progress beyond the inspected source methods is claimed.

## Mathlib

Coverage of this full mixed residual-row bound: **not checked**.
Supporting positive-matrix inequalities, finite spectral calculus,
Cauchy–Schwarz and determinant expansions: **not checked**. No
matching theorem or absence claim is made. The regulator-specific
hypotheses and estimates are justified above and in the cited local
proofs.
