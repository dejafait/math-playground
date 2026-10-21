# L250 — Mass-independent coefficient comparison in the gradient-base trace

## Hypotheses

Use exactly L102--L104's SU(2) relative all-face cube, straight lower-rooted
direction-1 forest, sufficiently large admitted even N, a=8/N, tau=1/16,
stored coordinates, bare-first order and actual probes i=3,6. Retain the
full relative spaces, normal end edges, axial levels 1<=t<N, constant
component indices and complete heat sums. There is no outside factor 3.

Use L103's T, E, G=(T^T T)^(-1), D=D_T, W, X and Zeta, and L104's
continuum h_k, v_l and K_(i,G). Import the smooth product-mode bounds
L248(3)--(11), the centered sample bounds L028(4), and L249's quantified
cumulative formula. Only these supporting results, not a reverse-trace
conclusion, are used. All imported qualifications remain in force.

At x_1=-4+at define the following operators on the **same finite spaces**.
For each positive transverse mu edge e with physical midpoint y_e put

    h^N_(k,t;e)=h_(k,mu)(x_1,y_e)

if both endpoints are interior, and put it equal to zero otherwise. Set

    X^h_(k,t)=T^T M_(h^N_(k,t)) E-E^T M_(h^N_(k,t)) T.

The zero convention on end edges changes no wedge, by L087(12).
Let W^u_t be exactly L103(3), replacing u_(a,1) only by the samples
of u_1 at the same vertices; its endpoint and centered-difference
filters are unchanged. For each retained transverse mu nu plaquette p
with physical tail y_p, put

    beta_(l,t;p)=v_(l,mu)(x_1,y_p)+v_(l,nu)(x_1,y_p),
    chi_(l,t;p)=v_(l,nu)(x_1,y_p)-v_(l,mu)(x_1,y_p),
    zeta^v_(l,t)=M_(beta_(l,t)) Bq-M_(chi_(l,t)) Bb.       (1)

Bb,Bq are the original finite raw two-edge path rows, with their pinned
slots; they are not infinite-grid paths. These definitions also apply to
continuum labels not admitted at mesh N. Define S_(i,N) by

    a^3 S_(i,N)=a^4 sum_(k,l)c_(i;kl) sum_(t=1)^(N-1) (at)
      Tr[G X^h_(k,t) G (W^u_t)^T D^T zeta^v_(l,t) T],   (2)

where c_(i;kl) is L104's complete continuum heat coefficient matrix.
The series in (2) is absolutely convergent, as proved below.

## Conclusion

Uniformly in sufficiently large admitted N, for both actual probes,

    |P_(i,N)-S_(i,N)|<=C_i N^2,
    |R_gx(i,N)-S_(i,N)|<=C_i N^(5/2).                  (3)

The inverses in (2) are massless and remain in their original positions.
Thus all finite-mesh deterministic coefficient and heat discrepancies
can be removed within the desired component budget without a mass loss.
The cumulative upper primitive, moving-cut half and upper endpoint are
accounted for, rather than replacing X by a compact coefficient.

This is a partial comparison, **not** the requested complete remainder.
The missing estimate is still

    |S_(i,N)-a^(-3)K_(i,G)|<=C_i N^(5/2)log(eN)^2,       (4)

with K_(i,G) exactly L104(6). In particular (2) retains pinned inverses
and spatially varying coefficients. It is not a frozen trace. No improved
complete exponent, coefficient value, interacting estimate or construction
follows. The separate critical audit in proof section 5 accepts (3)
relative to the stated imported inputs; it does not audit their entire
ancestry or establish (4).

## Proof

### 1. Global sample comparison on the actual finite rows

Write d_hat=d^>/a^2 and zeta_a=Zeta/a. We first check, for one fixed
polynomial p enlarged finitely often below,

    ||d_hat_(k,t)-h^N_(k,t)||_infinity<=C a p(k),
    ||d_hat_(k,t)||_infinity+||h^N_(k,t)||_infinity<=C p(k),
    ||zeta_(l,a)(t)-zeta^v_(l,t)||<=C a p(l),
    ||zeta_(l,a)(t)||+||zeta^v_(l,t)||<=C p(l).          (5)

Here the first line uses L087's representative d=0 on end edges on
both sides. The checks extending the compact-interior statements of
L249 to every relevant row are as follows.

On a transverse face normal to j, the relative smooth mode component
A_mu vanishes when mu!=j. The component A_1 and its transverse
derivatives tangent to that face vanish there as well. Thus the
prefix Phi and its tangential derivatives vanish on that face. The
finite prefix has the same exact zero values. Tangential pinned raw
links therefore agree with the smooth zero samples, and normal end
links use the actual midpoint and one-sided quotient in L248(6).
That quotient is an integral average of the derivative of the smooth
finite prefix along the existing link, including a pinned endpoint.
The C^m product-mode bounds in L248(3) hold on the closed cube.
The length-8 prefix estimates in L248(5) and its integral-quotient
argument consequently apply on these end links too: they do not
require continuing a forest field outside the cube. They give the
same independent polynomial value bounds and O(a p(l)) errors at
all existing raw transverse link midpoints, for every t<N.

For a transverse plaquette adjacent to a face, its direct circulation
is still the centered circulation of a A_(k,a). Any fixed tangential
slot is exactly zero by the preceding relative mode condition.
The forest prefix cancels exactly around the plaquette. Thus the
smooth centered circulation formula used in L104(9) is valid there,
with a uniform C^1 remainder from L028(4) and L248(3). For an edge
with two interior endpoints, both neighboring plaquettes in every
incident transverse plane exist, including when their far edges
lie on a face. L104(8)'s opposite-center difference therefore gives,
at the edge midpoint, uniformly over all such edges and all s<N,

    d_(k,s)/a^3=delta_k(-4+as,.)+O(a^2 p(k)).           (6)

Taking the difference through the smooth circulation remainder is
essential: its C^1 bound avoids dividing two unrelated O(a^2) errors
by a. Edges meeting a pinned vertex have zero wedge and use d=0;
edges contained in a boundary face are absent. L087's enumeration
exhausts the edge cases, so there is no omitted transverse collar.

Sum (6) with exactly the weights in L103(2). On the nonzero wedges,

    d_hat_(k,t)=a sum_(s=t+1)^(N-1)delta_k(-4+as,.)
                   +(a/2)delta_k(-4+at,.)+O(a^2 p(k)). (7)

The right endpoint sum for the full integral from x_1 to 4 includes
the s=N term. The displayed delta-sum differs from that endpoint
sum by -a delta_k(4,.)+(a/2)delta_k(x_1,.). The rectangle error is
at most 8a||partial_1 delta_k||_infinity. Both endpoint corrections
are at most (3a/2)||delta_k||_infinity. This proves the first line
of (5) uniformly in the moving cut, using the full h_k in L104(1).
It neither discards the upper tail nor samples the upper pinned
potential. The global value bound is L103(11), and h_k has polynomial
norm by the same smooth modes and length-8 integral.

For zeta, all four signed actual raw slots are
+mu at y, +nu at y+a e_mu, -mu at y+a e_nu, -nu at y.
Apply the established midpoint comparison to each slot, then use
the C^1 bound of v_l to move its sample to the common tail y.
The first two slots sum to v_mu+v_nu and the second and third sum
to v_nu-v_mu, within C a p(l). This holds also on a face: a pinned
tangential slot is zero, and moving its continuum sample by one
cell costs the same C a p(l). A plaquette wholly contained in a
fixed face has zero rough path rows. The finite Bb,Bq have fixed
range and bounded row and column multiplicity. Consequently their
coefficient errors give the operator bounds in (5), without any
replacement of their pinned geometry.

Finally, L028(4) on the globally smooth compact displacement gives

    ||u_(a,1)-u_1|_vertices||_infinity<=C a,
    ||W_t G^(1/2)||+||W^u_t G^(1/2)||<=C,
    ||(W_t-W^u_t)G^(1/2)||<=C a.                      (8)

For the last two inequalities use W_mu=-C_mu^T M_u T_mu and
||T_mu G^(1/2)||<=1, not an inverse operator supremum. The actual
and continuum displacements are compact with a common fixed
clearance. The weaker O(a) in (8) suffices. All estimates are uniform
in t; constant axial modes retain their entire lower linear prefix.

### 2. Ordered energy estimate before coefficient replacements

For any edge coefficient d, vertex displacement u and plaquette-to-edge
path operator zeta define

    F(d,u,zeta)=Tr[G(T^T M_d E-E^T M_d T)
                                 G W(u)^T D^T zeta T].

Here W(u) is the unchanged filtered stencil in (8). We claim on the
entire pinned spaces

    |F(d,u,zeta)|<=C N^3 ||d||_infinity
                                    ||u||_infinity ||zeta||. (9)

Indeed exact finite trace cyclicity gives

    F=Tr[(T G T^T) M_d (E G W(u)^T) D^T zeta]
          -Tr[(T G E^T) M_d (T G W(u)^T) D^T zeta].   (10)

Only the trace starting point has changed; no coefficient crosses G.
L103's full pinned scalar spectrum gives Tr G<=C N^3 and
||T G^(1/2)||=1. Also ||E||+||D||<=C. Hence

    ||T G T^T||<=1,
    ||E G W(u)^T||_HS<=C N^(3/2)||u||_infinity,
    ||T G E^T||_HS<=C N^(3/2),
    ||T G W(u)^T||<=C||u||_infinity,
    ||D^T zeta||_HS<=C N^(3/2)||zeta||.             (11)

For example factor G W(u)^T as G^(1/2)(G^(1/2)W(u)^T);
the first factor has squared Hilbert--Schmidt norm Tr G, and the
second is bounded by (8). The final bound uses the full edge-space
dimension O(N^3). Apply trace Cauchy--Schwarz to the two
Hilbert--Schmidt factors of each word in (10), leaving the other
factors in operator norm. This proves (9). It includes every Green
source and every normal end row, with no auxiliary mass or separate
absolute kernel moment.

The expression is trilinear in d,u,zeta. Telescope those three
arguments once each from (d_hat,u_a,zeta_a) to (h^N,u_1,zeta^v).
Use (5), (8), (9) and their independent value bounds. Uniformly
for each retained pair k,l and every t,

    |F(d_hat,u_a,zeta_a)-F(h^N,u_1,zeta^v)|
                                 <=C a N^3 p(k)p(l). (12)

This estimates coefficient errors in the original finite trace;
it is not a spatial freezing of its smooth coefficients.

### 3. Full heat matrices, omitted labels and response normalization

L249(3) at zero mass is the exact normalized P trace with
(d_hat,u_a,zeta_a). The identity itself needs no mass assumption.
L248(11) supplies, for retained labels and c0=tau/16,

    |c_(i;kl,a)|+|c_(i;kl)|<=C_i exp[-c0(|k|^2+|l|^2)],
    |c_(i;kl,a)-c_(i;kl)|
       <=C_i a p(k)p(l) exp[-c0(|k|^2+|l|^2)].         (13)

These are the exact two probe matrices used in L104; the triplet's
four products and shear's two polarizations remain. Multiplying
(12) by the first bound in (13) and using (9) with the second
bound controls both coefficient and heat replacements. The full
polynomial-times-Gaussian sum is finite. The normalization satisfies

    a^4 N^3 sum_(t=1)^(N-1) at <= C,

so the total normalized error for retained labels is <=C_i a.

For any pair with a continuum label absent from the finite mesh,
|k|+|l|>=cN for a fixed c>0. Bound its indicator by
(|k|+|l|)/(cN), apply (9) to its smooth coefficients, and sum the
enlarged Gaussian polynomial. This gives another normalized error
<=C_i/N<=C'_i a. It also proves absolute convergence of (2) for
each N. Allowed zero own-direction indices are retained labels,
not omitted labels. No covariance spectrum is truncated.

Thus |a^3(P_(i,N)-S_(i,N))|<=C_i a. Multiplication by a^(-3)
gives C_i a^(-2)=O_i(N^2). L103(6) then proves the second part
of (3), with its O(N^(5/2)) removed terms counted once. This is
exactly the original normalization; no new half, color factor or
outside 3 occurs.

### 4. What remains unproved

The smooth finite trace (2) has the same frozen continuum symbol
as L104(6), but (9) supplies only a cubic bound for it. It does not
quantify its boundary transfer or spatial coefficient freezing.
Those steps require a further ordered joint comparison with G still
massless, or new uniform regularized estimates. No such step is
asserted here. In particular (3) alone improves no complete
remainder exponent from L249.

This is RESEARCH / REPRODUCTION within the unchanged EXPLORE
assessment `drafts/literature/2026-10-20-gradient-base-crossed-quantitative-remainder.md`.
The finite energy and raw-sample specialization is given explicitly
because the imported compact-walk comparison does not assert this
mass-independent, full-row conclusion. No general literature theorem
is reproved, and no originality beyond the sources checked is claimed.
Independent component rates, full quantitative L011 assembly,
interacting reflected error <=c_box/2, continuum axioms and infrared
finite positive mass all remain open.

### 5. Separate critical audit, 2026-10-20

The audit accepts (3), under the unchanged EXPLORE assessment
`drafts/literature/2026-10-20-gradient-base-coefficient-energy-critical-audit.md`.
It checks the full-row specialization and ordered energy estimate,
not merely their compact-interior versions. This is RESEARCH /
REPRODUCTION: it certifies the existing local partial input, without
a new rate or a claim of progress beyond the sources checked. The
following checks use the stated imports and the named finite spectral
theorem, compatible trace cyclicity and Hilbert--Schmidt ideal
inequalities. No external decay theorem or inverse operator bound is
required.

**End wedges and surviving normal slots are distinct.** Let V be the
space of transverse vertex values pinned on the boundary, H the full
relative transverse edge space, and J the relative transverse plaquette
space. Then T,E,W:V->H and D,zeta:H->J. On an end edge with pinned
tail, E has zero row. On an end edge with pinned head, E and T have
the same row. In both cases the row's contribution to
T^T M_d E-E^T M_d T is identically zero. Thus setting both d_hat and
h^N to zero there is legitimate before taking their difference.
This does not set a raw normal exterior link to zero. Nor does it
assert that the zeroed representative h^N has a uniform derivative
bound across that end edge; (9) only uses its supremum.

The relative product modes underlying L248(3)--(6) have a cosine in
their own component direction and sines in the other three directions,
with the allowed constant cosine retained. Hence on a transverse face
normal to j, A_mu=0 for mu!=j. Component A_1 and every derivative
tangent to that face vanish there. Both phi_a and Phi therefore
vanish identically on the face, as do their tangential derivatives.
These statements also hold at intersections of faces. For a tangential
fixed link, its direct value and both prefix endpoints are zero; its
continuum tangential value is zero as well.

For a surviving link normal to a transverse face, the finite prefix
still equals L248(4)'s smooth sine-product sum at both endpoints,
including the pinned endpoint. For either the lower or upper end link,
the exact quotient in L248(6) is

    [phi_a(t,y+a e_mu)-phi_a(t,y)]/a
      =integral_0^1 partial_mu phi_a(t,y+r a e_mu) dr.

The integration segment is contained in the closed cube. With
z=y+a e_mu/2, its discrepancy from partial_mu Phi(t,z) is at most

    ||partial_mu(phi_a-Phi)||_infinity
                         +(a/2)||partial_mu^2 phi_a||_infinity.

L248(5) bounds this by C a p(k) for every retained label, uniformly
in t<N; L248(3) bounds the direct midpoint discrepancy. Independent
value bounds follow by integrating bounded first derivatives over
the length-8 prefix. Thus the raw midpoint comparison applies to all
surviving normal slots without any extension beyond a face or through
the separately pinned axial value t=N. The constant axial cosine gives
the exact prefix at/sqrt(8), with its transverse factors and
normalization, so it is included in these same bounds.

**Adjacent circulations and the cumulative endpoint.** If both endpoints
of a mu edge are interior, its coordinate in any other transverse
direction nu is in {1,...,N-1}. Both incident plaquettes with tails y
and y-a e_nu exist. When that coordinate is 1 or N-1, a far tangential
edge may be fixed, but its actual value equals the smooth zero sample.
Consequently the four-sample circulation formula remains exact. An
edge with a pinned endpoint instead has the zero wedge checked above;
an edge contained in a boundary face is absent. This enumerates all
cases needed for (6), rather than dropping a collar.

On every such plaquette the forest prefix telescopes to zero, so only
the smooth direct A_(k,a) enters its circulation. L028(4) and L248(3)
give a uniform C^1 bound C a^2 p(k) for the smooth extension of
f/a^2-F. Applying the opposite-center difference by its integral
derivative, and applying the centered remainder to F itself, gives
C a^2 p(k) for d/a^3-delta. In particular no division of two
unrelated remainder bounds by a occurs. Summing this error with the
weights a in (7) costs at most C a^2 p(k), since aN=8.

The right-endpoint quadrature from x_1 to 4 differs from the retained
delta-sum by exactly a delta_k(4)-(a/2)delta_k(x_1). Its quadrature
error is at most 8a||partial_1 delta_k||_infinity. Thus both endpoint
terms and the moving-cut half yield the stated O(a p(k)) error for
all t, including t=N-1. The upper primitive is never truncated to the
displacement support. On end-edge representatives the comparison is
exactly zero instead.

For zeta the four signed slots are +mu at y, +nu at y+a e_mu,
-mu at y+a e_nu, and -nu at y. The preceding global midpoint bound,
followed by one bounded sample shift, gives their first-two and
second-plus-third sums as beta and chi from (1), with O(a p(l))
errors. A missing tangential slot has zero midpoint value; its
same-component common-tail value differs by at most that same error.
The finite Bb and Bq keep their actual missing slots. Their uniformly
bounded row and column multiplicities turn these scalar errors into
the operator error in (5). No path or covariance is replaced by an
infinite-grid object.

**Both ordered energy words.** In (10) every displayed factor is an
endomorphism of H. The first word uses E G W^T and D^T zeta as its
two Hilbert--Schmidt factors; T G T^T and M_d are bounded in operator
norm. The second uses T G E^T and D^T zeta in Hilbert--Schmidt norm;
M_d and T G W^T are bounded in operator norm. In detail,

    E G W^T=E G^(1/2)(G^(1/2)W^T),
    T G E^T=(T G^(1/2))G^(1/2)E^T,
    T G W^T=(T G^(1/2))(G^(1/2)W^T).

L103(13)'s filtered difference argument gives
||W(u)G^(1/2)||<=C||u||_infinity for an arbitrary vertex multiplier
u, also for the difference u_a-u_1. L087(13)'s full pinned scalar
spectrum gives ||G^(1/2)||_HS<=C N^(3/2), while
||T G^(1/2)||=1. Finally dim H=O(N^3) and ||D||<=C give
||D^T zeta||_HS<=C N^(3/2)||zeta||. These facts verify every
factor of (11) and hence (9). All normal end edges and Green inputs
are included. Taking the three multilinear differences in this exact
order proves (12), using the separate value bounds for unchanged
factors. No projection commutator or absolute kernel moment is assumed.

**Complete heat sum and normalization.** L248(10)--(11) concerns the
same B matrices as L104(13): the four triplet curvature products retain
1/4 and both shear polarizations retain 1/2. The ordinary covariance
column is a A_(k,a); dividing the actual raw link by a and the cumulative
coefficient by a^2 gives exactly L249(3) at zero mass. Thus multiplying
the original prefactor a^-1 t by a^3 and these two coefficient factors
gives a^5 t=a^4(at), with no extra color or orientation factor.

The mode polynomials in the preceding bounds have fixed degree, so
both full heat sums converge under (13). Explicitly,

    a^4 N^3 sum_(t=1)^(N-1) at
                         =(8^5/2)(1-1/N).

Consequently either an O(a) coefficient replacement or the O(a)
heat-coefficient discrepancy gives an O(a) normalized total error.
A continuum label absent from the finite mesh has |k|+|l|>=N;
its indicator is bounded by (|k|+|l|)/N. The same energy estimate
and an enlarged Gaussian polynomial bound its full contribution by
O(1/N). Allowed constant own-direction indices remain present on
both sides. This also proves absolute convergence of (2).

It follows that |P-S|<=C_i a^-2=O(N^2). Adding L103(6)'s
already combined removed-term estimate once proves the second bound
in (3). The required smooth comparison (4) is neither used nor
established. L249's complete coarse exponent remains unchanged.
Acceptance supplies no quantitative L011 assembly, interacting
reflected estimate, continuum axioms or finite positive mass.

## Mathlib

Full matching mass-independent cumulative coefficient comparison:
**not checked**. Supporting finite trace cyclicity, Hilbert--Schmidt
ideal inequalities, finite spectral sums and smooth rectangle
quadrature: **not checked**. Unknown availability is not absence.
The analytic proof uses no numerical certificate or new source theorem;
documentation validation does not verify its mathematics.
