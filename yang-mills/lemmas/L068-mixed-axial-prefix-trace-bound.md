# L068 — The actual right axial-prefix path/path trace is O(N²)

## Hypotheses

Keep L064's exact fixed-mesh SU(2) Gaussian coefficient, straight
lower-rooted forest, ordinary dimensionless coordinates, actual residual
A_0, both original probes, tau=1/16 and sufficiently fine admitted even
meshes a=8/N. Retain its complete exterior coefficients c_(i;kl),
alternating right path Q_l, upper endpoint sum E_+, and multiplier
g_k(e)=(Th_k)_e. Include all transverse plaquettes at levels 1<=s<N,
every upper transverse edge and every pinned end row. Take the
small-coupling coefficient at fixed mesh before mesh refinement.

Let I_1 insert all axial Hodge links, Sigma_1=I_1^T Sigma I_1,
G=(T^T T)^(-1) the three-dimensional pinned vertex inverse, and E_0
the normalized constant axial component-1 embedding. Let T_ax take
the transverse incidence of component-1 links at every axial edge
position r=0,...,N-1, with its sign chosen as in the actual forest
lift. Let J take its prefixes:

    (J z)_s=sum_(r=0)^(s-1) z_r, 1<=s<N.

Thus the right axial forest-lift summand is J T_ax I_1^T. This is
L026's root retraction, with its signed incidence; the separate
pinned top potential is never used as a level s=N prefix.
Let Delta_E be the transverse relative edge Laplacian, D the
transverse edge-to-plaquette incidence and P=TGT^T. All norms are
ordinary finite-coordinate norms. Constants may depend on the fixed
probe, displacement, flow time and box, but not on N.

## Conclusion

The actual right axial-path block and its contribution to L064(16) are

    W_X^ax=sqrt(N) G E_0^T A_0 I_1 Sigma_1 T_ax^T J^T,
    S_kl^ax=-Tr[K_1 Q_l (W_X^ax)^T E_+^T M_(g_k)].        (1)

For a fixed polynomial p, independent of N,

    |S_kl^ax|<=C N² p(k)p(l),
    |sum_(k,l) c_(i;kl) S_kl^ax|<=C_i N².                (2)

This meets the O(N²)=O(a^-2) threshold for this summand. It excludes
stronger powers here but gives neither o(N²) nor an a²-scaled limit,
sign, cancellation or logarithmic coefficient. The right axial
source is not assumed smooth or boundary localized. The first pair,
other endpoint monomials and all nine placements below a² scale
remain open, as do other cubic pairs, measure, insertion/flow jets,
nonlinear forest compensation, finite matching, reflected error
<=c_box/2, continuum fields, full reflection positivity, infrared
control and finite positive mass. This is local standard-method
specialization/reproduction, with no beyond-source originality claim.

## Proof

### 1. Keep the actual transfer and scalar residual in order

L018's quadratic transfer and L026's component-diagonal Hodge law give
the first identity in (1): the left lift is L_u=sqrt(N)E_0^T and
L_u Sigma=sqrt(N)G E_0^T, while the right lift is J T_ax I_1^T.
This transfers the quadratic covariance block with its actual rows;
it does not transfer unmodified cubic vertices to Hodge coordinates.
The second identity is L064(16) with this right summand selected.

Use precisely L065's bounded scalar operator

    R_01=G^(1/2) E_0^T A_0 I_1 Sigma_1^(1/2),
    ||R_01||<=C.                                        (3)

All right axial frequencies remain in (3). Factor the actual block as
W_X^ax=sqrt(N)G^(1/2)R_01 Sigma_1^(1/2)T_ax^T J^T.
Consequently, transposition and finite trace cyclicity give

    S_kl^ax=-sqrt(N) Tr[F_l H_k],
    F_l=K_1 Q_l J T_ax Sigma_1^(1/2),
    H_k=R_01^T G^(1/2) E_+^T M_(g_k).                   (4)

No path coefficient, endpoint multiplier or covariance is commuted
through another factor. In particular (3) is applied to the actual
component-1 input, not to the full-vector block obstructed by L066.

### 2. A summable full-spectrum bound at every axial level

L064 and L041's exact last-column inverse give

    (K_1)_s=-g_s(Delta_E)(I-P)D^T,
    g_s(lambda)=sinh(s eta)/sinh(N eta),
    eta=2 asinh(sqrt(lambda)/2).                         (5)

Since D^T D=Delta_E(I-P), with commuting factors, the complete
Hilbert–Schmidt norm at level s obeys

    ||(K_1)_s||_HS²
       =Tr[g_s(Delta_E)² Delta_E(I-P)]
       <=Tr[g_s(Delta_E)² Delta_E].                      (6)

The inequality follows from positivity and the commuting orthogonal
projection; it retains the entire pinned edge space as an upper bound.
Its three component spectra each have one cosine index in 0,...,N-1
and two sine indices in 1,...,N-1. For m=max_j q_j>=1, L026's
elementary sine bounds imply

    c m²/N²<=lambda_q<=C m²/N²,
    c' m/N<=eta_q<=C' m/N.

Each shell has at most C m² labels, including multiplicity across
the three components. In particular N eta_q>=c'>0. For d=N-s,
the exponential form of (5) gives

    0<=g_(N-d)(lambda_q)
       =exp(-d eta_q)
          [1-exp(-2(N-d)eta_q)]/[1-exp(-2N eta_q)]
       <=C exp(-c' d m/N).                              (7)

Thus, for every 1<=d<N,

    ||(K_1)_(N-d)||_HS²
       <=(C/N²) sum_(m=1)^(N-1) m⁴ exp(-c d m/N)
       <=C N³ d^-5.                                    (8)

Here is a uniform justification of the last shell sum. For alpha>0,
on t in [m-1,m], m⁴ exp(-alpha m)<=(t+1)⁴ exp(-alpha t).
Integrating and summing bounds the infinite sum by
24/alpha⁵+24/alpha⁴+12/alpha³+4/alpha²+1/alpha.
Since alpha=c d/N is bounded above by the fixed c, this is at most
C_c alpha^-5. Extending the finite sum to the infinite sum is
legitimate by nonnegativity. This proves (8), including the smallest
transverse eigenvalues and every pinned end edge, and in particular

    sum_(s=1)^(N-1) ||(K_1)_s||_HS<=C N^(3/2),           (9)

because sum_(d>=1) d^-5/2 is finite. The incidence D in K_1 is
essential to this bound. No smooth-source interpolation or truncation
to low physical modes is used.

### 3. Bound the exact adjoint prefix before taking its norm

Q_l is block diagonal in axial level s: each b_p,q_p path lies
in a transverse plaquette at that level. L062's two-link path
maps and L064(3) give, including end rows,

    ||Q_(l,s)||<=C a p(l).                               (10)

Indeed each selected path has two signed link entries, each link
belongs to a bounded number of transverse plaquettes, and the two
actual exterior path coefficients are bounded by a p(l). Deleting
fixed rows does not increase these bounds. No coefficient is taken
outside its actual local path map.

Set B_l=J^T Q_l^T K_1^T. Its exact block on axial edge position r is

    (B_l)_r=sum_(s=r+1)^(N-1) Q_(l,s)^T (K_1)_s^T,
    0<=r<=N-1,                                         (11)

with the empty last sum equal to zero. Triangle inequality in the
Hilbert–Schmidt norm, (9), and (10) give uniformly in r

    ||(B_l)_r||_HS<=C a p(l) N^(3/2).

The r blocks are disjoint coordinate blocks, so their squared
Hilbert–Schmidt norms add exactly. All N axial edge positions give

    ||B_l||_HS<=C a N² p(l).                             (12)

Equation (11) retains the near-top source and every prefix level.
Replacing J by its O(N) operator norm before using (9) would lose
the factor needed for the threshold; no source smoothness is inferred.

The full transverse incidence satisfies
T_ax^T T_ax=I_N tensor Delta_3=H_T. L026/L065's tensor covariance
is Sigma_1=(Delta_edge tensor I+H_T)^(-1); its commuting positive
factors give

    ||T_ax Sigma_1^(1/2)||<=1.                           (13)

This includes all three transverse directions jointly and all
axial modes and end edges. Applying the product inequality in
Hilbert–Schmidt norm to F_l in its exact order, (12)–(13) yield

    ||F_l||_HS<=||K_1 Q_l J||_HS
               =||B_l||_HS<=C a N² p(l).                (14)

### 4. Complete endpoint and heat sums

The pinned endpoint sum has uniformly bounded norm: each vertex
meets at most six retained edges and
||E_+z||²<=12||z||². A pinned endpoint contributes zero, so this
includes edges meeting a face. The vertex Green trace obeys
Tr G<=C N³. To see this directly from L026's three-dimensional
Dirichlet spectrum, shell m has at most C m² labels and inverse
eigenvalue at most C N²/m², so the sum of N-1 shells is O(N³).

Therefore, using |g_k(e)|<=a p(k) from L064(3),

    ||G^(1/2) E_+^T M_(g_k)||_HS²
       <=a² p(k)² Tr(E_+ G E_+^T)
       <=C a² p(k)² Tr G
       <=C a² N³ p(k)².

Together with (3), this gives

    ||H_k||_HS<=C a N^(3/2) p(k).                        (15)

For finite rectangular matrices, |Tr(FH)|<=||F||_HS||H||_HS,
by coordinate Cauchy–Schwarz (or the Hilbert–Schmidt pairing with
the transpose). Substituting (14)–(15) in (4) proves

    |S_kl^ax|<=C sqrt(N) a² N^(7/2) p(k)p(l)
              =C a² N⁴ p(k)p(l)
              <=C' N² p(k)p(l),                         (16)

since aN=8. L062/L064's complete heat coefficients obey
sum_(k,l) |c_(i;kl)| p(k)p(l)<=C_i for the fixed polynomial p.
Their positive physical gap, quadratic eigenvalue lower bound and
bounded relative probe form justify this summability for both probes.
Applying it to (16) proves (2), without dropping modes or signs.

The analytic checks are the right-lift sign defined by the actual
incidence, quadratic transfer, scalar compression, full shell sum,
exact adjoint prefix range, joint three-direction contraction,
pinned endpoint trace and complete heat sum. No finite numerical
diagnostic is needed or used as proof. The separate critical audit
below confirms this bound within its stated scope. The bound leaves
the whole N² scale available; it must not be recorded as a vanishing
scaled summand.
The general flow-renormalization and stress-matching statements are
reused from the saved primary-source assessment, not reproved here.

### 5. Separate critical audit, 2026-10-08

The audit YM-20261008-087-mixed-axial-prefix-trace-audit checked (1)–(16)
against the cited input formulas. No defect was found and no stronger
bound is claimed. This is an internal analytic audit in a separate
research step, not independent computer verification.

**Lift, sign and covariance normalization.** For an oriented transverse
edge e=(v,w), L026's retraction gives

    (x_T^ax)_(s,e)=sum_(r<s) [z_1(r,v)-z_1(r,w)].

Thus (T_ax f)_(r,e)=f_r(v)-f_r(w): this fixes the sign left implicit in
the hypotheses. Pinned endpoint evaluations are zero. The levels in
this formula are exactly 1<=s<N, so r=N-1 never contributes; no
prefix is substituted for the separately pinned top potential.
The upper axial link is the sum of all N axial entries, hence
L_u=sqrt(N)E_0^T. L026's component-diagonal inverse has eigenvalue
G on the constant axial mode, giving L_u Sigma=sqrt(N)G E_0^T.
There is no extra a or a^4 factor in these ordinary coordinates.

L018's quadratic invariance therefore gives the first identity of (1)
with both covariance factors retained. Since A_0 is symmetric, its
transpose is exactly

    (W_X^ax)^T=sqrt(N) J T_ax Sigma_1 I_1^T A_0 E_0 G.

Substitution in L064(16) yields (4). The overall minus is the minus
of that determinant minor, while the signed forest incidence is
already inside T_ax. Neither sign is inferred from a norm bound.
The dimensions also agree: F_l maps all axial links to upper edges,
H_k maps upper edges to axial links, and F_l H_k is an upper-edge
endomorphism. Its Hilbert–Schmidt trace bound uses the transpose
pairing, with no symmetry or positivity assumed for F_l H_k.

**Scalar restriction.** L065 proves a quadratic-form bound on the
entire component-1 space, not just its zero axial mode. Its polarized
form is A_11=H_T^(1/2) F H_T^(1/2), ||F||<=C. Substituting this
identity into R_01 gives e_0^T F H_T^(1/2) Sigma_1^(1/2), which is
bounded because H_T and Sigma_1 commute and H_T<=Sigma_1^(-1).
The right prefix does not preserve the zero mode and need not do so.
The axial coefficient-difference cancellation in L065(6) includes
both end edges; it assumes smooth coefficients, not smooth inputs.
Thus (3) uses precisely its proved all-axial scalar scope and never
the full-vector extension stopped by L066.

**Full level tail and adjoint.** At a transverse edge component the
two sine indices are positive even if its cosine index is zero.
Therefore m>=1 and N eta>=c>0 uniformly. This lower bound controls
the denominator of (7) also at the lowest physical modes. The
identity D^T D=Delta_E(I-P) retains the incidence factor lambda in
(6); dropping that factor would change the power of the level tail.
The three-component shell count is O(m²). For d=1 the bound in (8)
is O(N³), and for d=N-1 it is O(N^-2); the same integral comparison
proves every intervening case. It requires only 0<cd/N<=c, so its
constant is uniform as d/N tends to zero. No low- or high-frequency
sector has been omitted.

The two-link maps defining Q_l lie entirely in level s. Their
bounded row and column multiplicities and the actual exterior bound
give (10), including rows with fixed entries. Consequently taking
the adjoint gives exactly the range r<s<N in (11). The triangle
inequality is applied to each block before its norm is squared;
no orthogonality between different s is asserted. Only the final
disjoint r coordinate blocks have additive squared norms. There
are N such blocks, the last zero. This proves the sqrt(N) block
count in (12), without using a boundary-localization assertion.
The sign of T_ax disappears in T_ax^T T_ax=H_T, and the commuting
relative inverse proves (13) for all three directions jointly.

**Endpoints, heat sum and threshold.** Every vertex occurs in at
most six rows of E_+, including normal end edges; fixed tangential
rows vanish. Positivity justifies
Tr(M_g E_+ G E_+^T M_g)<=||g||_infinity² Tr(E_+ G E_+^T)
without commuting M_g and G. The three positive vertex indices in
G have shell multiplicity O(m²) and inverse eigenvalues O(N²/m²),
giving Tr G=O(N³) over all N-1 shells. This verifies (15).

The trace exponents in (16) are
sqrt(N) times aN² times aN^(3/2)=a²N⁴=64N².
The heat coefficients in L062/L064 use physical eigenvalues, whose
lower bound is c|k|², not the dimensionless lambda of (5)–(8).
For every fixed polynomial p, bounded B_i^rel gives the explicit
majorant C_i [sum_k p(k) exp(-tau c|k|²)]²<infinity. The finite
allowed mode sets embed in this full integer sum with bounded
component multiplicity. Hence no N-dependent number of exterior
modes is lost when passing from (16) to (2), for either probe.

The audit confirms O(N²) only. In particular (12) does not make
the prefix source smooth, and no bound above supplies an additional
vanishing factor. The first pair of L064(1), its other endpoint
monomials, and the complete logarithmic response remain unresolved.

## Mathlib

Coverage of the full axial-prefix trace statement: **not checked**.
Supporting finite trace inequalities, spectral calculus,
Hilbert–Schmidt norms, positive projections, finite incidence algebra
and series comparison: **not checked**. No matching theorem or absence
claim is made. The actual tensor spectra, prefix ranges and uniform
source bound needed for this specialization are justified above.
