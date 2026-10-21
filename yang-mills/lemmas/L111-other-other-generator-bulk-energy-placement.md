# L111 — Generator multipliers can cross the bulk energy kernel at cubic cost

## Hypotheses

Use exactly L099/L110's transverse H trace for SU(2), both actual
L010 probes i=3,6, straight lower-rooted direction-1 forest, all-face
relative fixed-link box (-4,4)^4, admitted even N, a=8/N and tau=1/16.
Take the bare small-coupling coefficient at fixed mesh before refinement.
Coordinates and norms are ordinary stored ones. Keep all interior axial
levels, pinned transverse rows, both generator orientations and every
exterior heat mode. Import L110's exact D,D core and its separately
cubic-bounded exterior-circulation remainder; that remainder is retained.

At each transverse level let D be the dimensionless relative incidence
from transverse links to the three transverse plaquette components.
Let J extend this finite plaquette array by zero into the three-component
array on Z^3, indexed by the plaquette's lower vertex. Thus this uses
L110's periodic unshifted phases. Physical component-center offsets
remain in the actual finite stencils, rather than being identified.
Let E_j be L110's infinite-grid energy convolution. It is not the
pinned energy covariance.

L009(3) and L028's endpoint/clover factorization give exactly

    G_tr(t)=a^-1 H_t D,
    H_t=sum_r T_r M_(b_(r,t)) C_r.                         (1)

Here r is a fixed finite list of ordered transverse component/plane
choices, with their signs; T_r is the endpoint average/injection from
vertex scalars to the output link component, C_r is the clover
average/selector from plaquettes to vertex scalars, and
b_(r,t)(x)=u_(a,rho)(at,ax), with the box origin included in the physical
coordinates. The operators T_r,C_r are fixed translation-invariant
finite stencils on the infinite grid. Equation (1) on the finite box
means their relative restrictions. All nonzero displacement coefficients
are in a fixed physical interior set, so every nonzero stencil is
interior at sufficiently fine mesh. Extend b by the same globally
smooth compactly supported u_a of L028. Uniformly in r,t,

    |b_(r,t)(x)-b_(r,t)(y)|<=C a |x-y|.                  (2)

These are scalar multipliers at vertex indices. When acting on
plaquette arrays below, the same scalar multiplies all three components
at the same integer index. No actual component-center coefficient has
been substituted for it. Shifts in T_r,C_r remain exact.

## Conclusion

Put

    E^pin_ts=D (K_h)_ts D^T,
    B_ts=E^pin_ts-J^* E_(t-s) J,
    Z_(kl;st)=F_l(s)^T P F_k(t),                         (3)

where the F operators are exactly those of L110, including their
actual staggered exterior coefficients. Then the finite core has the
exact decomposition

    R_H,tr^D=R_bulk+R_pin,
    R_bulk=a^-1 sum_(k,l,s,t)c_(i;kl,a) min(s,t)
               Tr[J^* D H_t E_(t-s) J Z_(kl;st)],
    R_pin=a^-1 sum_(k,l,s,t)c_(i;kl,a) min(s,t)
               Tr[D H_t B_ts Z_(kl;st)].                (4)

The D,H in R_pin are finite operators; the D,H in R_bulk are their
infinite-grid stencils before compression. Define just the moved bulk
expression by replacing D H_t E_j in (4) with

    D sum_r T_r C_r E_j M_(b_(r,t)).                    (5)

Call the resulting real scalar R_bulk,moved. For both actual probes,

    |R_bulk-R_bulk,moved|<=C_i N^3.                     (6)

This is the complete error for moving the generator's displacement
coefficients across the bulk joint covariance, summed over all levels,
all r and all heat modes. It retains the middle finite P, min(s,t),
both exterior coefficient levels and every staggered stencil. It does
not move either F coefficient through P or freeze them.

Neither R_pin nor R_bulk,moved is cubic-controlled here. No total
coefficient-freezing error, pinned-transfer estimate, O(N^3) bound
for R_H,tr, a^3 limit, coefficient value or compensation follows.
The error in (6), like L110's exterior-circulation remainder, is
cubic-bounded and cannot be discarded in a coefficient calculation.
Other jets, finer powers/logarithm, matching, interacting error
<=c_box/2, continuum axioms, reflection positivity, infrared control
and finite positive mass remain unresolved.

## Proof

### 1. Keep the generator in its curvature-input order

For a transverse input with component 1 zero, the displacement terms
rho=2,3,4 in L009(3) use exactly the transverse curvatures D/a.
Endpoint averaging, scalar vertex multiplication and clover averaging
occur in that order after this input. L028's factorization justifies
(1), including all cross-component signs; none of those terms is
omitted. In the lower-vertex index convention the centered averages
are finite integer-shift stencils. Their norms and their ranges are
bounded independently of N. Compact displacement support means that
extending and restricting these nonzero products gives exactly the
finite generator, with no boundary term. L028's global C^1 bounds
give (2), also across the zero coefficient collars.

L110 gives A_k^D=P F_k D Q=P F_k D, since D P=0. At levels s,t,
the core's edge trace is

    min(s,t) Tr[(K_h)_ts D^T F_l(s)^T P F_k(t) D G_tr(t)].

Cyclicity, (1) and (3) turn this into

    a^-1 min(s,t) Tr[D H_t E^pin_ts Z_(kl;st)].         (7)

This step requires no multiplier commutation. In particular the
nonlocal P between the two F factors stays in place. The rectangular
trace identity applies because all the finite spaces are finite
dimensional, even though link and plaquette dimensions differ.

Insert the defining equality E^pin_ts=J^*E_(t-s)J+B_ts into (7).
For sufficiently large N, H_t is zero in a collar wider than the
fixed stencil ranges. Consequently its output and the output of
D H_t vanish near the transverse boundary, and its input stencils
only sample existing finite plaquettes. Thus D H_t J^* on infinite
inputs equals J^*D H_t with infinite D,H. This proves (4), including
its exact boundary correction. No covariance is replaced without
retaining its difference.

### 2. Add the unweighted energy estimate needed by finite shifts

Write e_j(z) for L110's kernel and define

    W_j=(sum_z ||e_j(z)||_F^2)^(1/2),
    Q_j=(sum_z |z|^2 ||e_j(z)||_F^2)^(1/2).

L110 gives Q_j<=C(1+|j|)^(-3/2). Its proof (9) also gives
||E_j(theta)||_F<=C rho exp(-|j|rho/2), with
(2/pi)|theta|<=rho<=|theta|. Entrywise Fourier Plancherel therefore
gives, for n=|j|>=1,

    W_j^2=integral ||E_j(theta)||_F^2 dtheta/(2pi)^3
       <=C integral_0^(sqrt(3)pi) r^4 exp(-2nr/pi) dr
       <=C' n^-5.

For j=0 the same bound on the compact torus gives W_0<=C.
Hence

    W_j<=C(1+|j|)^(-5/2),
    sum_(j in Z)(W_j+Q_j)<infinity.                     (8)

This uses precisely the standard Fourier Plancherel theorem already
imported in L110; it is an unweighted specialization of that kernel's
proved pointwise estimate, without an absolute kernel-moment claim.

### 3. Estimate the exact staggered commutation error

For each summand of H_t, use the common-index scalar multiplication
specified above. Its exact rectangular-operator identity is

    M_b C_r E_j-C_r E_j M_b
          =[M_b,C_r] E_j+C_r[M_b,E_j].                 (9)

The two M_b in [M_b,C_r] act on its vertex and plaquette spaces
respectively; both use b at the integer index. Writing C_r as its
finite sum of component selectors and shifts S_h makes this
commutator a finite sum of

    (b(x)-b(x+h)) times a shifted component row.

Every coefficient is at most C a|h| by (2). Each shifted row of E_j
has squared norm at most W_j^2, by translation invariance and the
Frobenius sum over input and output components. Thus on any set
Lambda of at most C_0 N^3 output indices,

    ||R_Lambda [M_b,C_r]E_j||_HS
                                      <=C a N^(3/2) W_j.          (10)

Left multiplication by the bounded finite stencils D T_r only
enlarges the output restriction by a fixed range and changes C.
The enlarged set still has at most C_1 N^3 indices. L110's scalar
commutator proof gives, at each j,

    ||R_Lambda [M_b,E_j]||_HS<=C a N^(3/2) Q_j.         (11)

The same fixed-range enlargement handles D T_r C_r in front of
(11). Combine (9)--(11), sum the fixed finite list r, and restrict
inputs as well by J. Input restriction can only decrease a
Hilbert--Schmidt norm. For the full compressed error X_(t,j),

    X_(t,j)=J^*D[H_t E_j-sum_r T_r C_r E_j M_(b_(r,t))]J,
    ||X_(t,j)||_HS<=C a N^(3/2)(W_j+Q_j).              (12)

This proof retains the shifts rather than identifying differently
staggered samples. The finite output restriction need not be inside
the displacement support: (10)--(11) hold on all finite output rows.
After the move, the nonlocal bulk kernel may have output outside
that support; those rows are included in (12).

### 4. Count the actual coefficient-error trace at cubic scale

Bounded multiplicity and L088(5) give

    ||F_k(t)||<=C a p(k),
    ||Z_(kl;st)||_HS<=C a^2 p(k)p(l) N^(3/2),
    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.                (13)

The middle P is the exact finite orthogonal projection and has norm
at most one; no commutator or gain for it is used. The dimension of
the finite plaquette space is at most C N^3, justifying its
Hilbert--Schmidt count in (13). Trace Cauchy--Schwarz and (12) give

    |Tr[X_(t,t-s) Z_(kl;st)]|
       <=C a^3 N^3 p(k)p(l)(W_(t-s)+Q_(t-s)).          (14)

For each t, sum_s(W_(t-s)+Q_(t-s)) is bounded by the complete
infinite sum in (8). There are fewer than N levels t and
min(s,t)<=N. Thus the exact weighted finite level sum of the
majorant in (14) is at most C a^3 N^5 p(k)p(l).
The outside a^-1 in (4) and the full heat sum in (13) give

    |R_bulk-R_bulk,moved|<=C_i a^2 N^5
                         =64 C_i N^3,

proving (6). The heat majorant is uniform over every label; no
finite exterior truncation is made. Both finite generator
orientations were already retained in L099's exact symmetric
heat-summed trace imported by L110. This argument alters neither
that normalization nor the complete group's outside factor 3.

### 5. Identify the surviving obligations

Equation (12) shows that the proposed bulk generator-multiplier
placement loses no unsandwiched covariance derivative: D T_r is a
bounded dimensionless finite stencil, and both covariance
circulations remain inside E_j. It does not bound a commutator with
the pinned B_ts or either F coefficient through the middle P.
The pinned correction in (4) contains the full relative transverse
and axial boundary effects. Its size is not inferred from (8).
The moved bulk trace also retains variable F coefficients and
two axial levels; a frozen cancellation cannot be substituted for it.

This is one bounded RESEARCH / REPRODUCTION attempt under the
unchanged complete other/other EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
It supplies a relevant local standard-method input, not a novelty
claim beyond checked sources. The finite contraction and generator
are imported, and the specialization is needed because L110's scalar
estimate alone did not verify its placement through the filtered
generator. No numerical value or limiting sign of either probe is
used. Any subsequent comparison retains L084/L082's qualifications.

## Mathlib

Full matching bulk-generator error or pinned-transfer theorem:
**not checked**. Supporting Fourier Plancherel, finite-stencil,
Hilbert--Schmidt and rectangular trace identities: **not checked**.
Unknown availability is not absence. No general flow or Ward theorem
is used to control this isolated group's coefficient.
