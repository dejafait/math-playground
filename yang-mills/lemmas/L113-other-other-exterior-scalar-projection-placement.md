# L113 — Exterior scalar placement through the finite gradient projection

## Hypotheses

Use exactly L111's moved bulk trace, with both actual L010 probes
i=3,6, SU(2), straight lower-rooted direction-1 forest, all-face relative
fixed-link box (-4,4)^4, admitted even N, a=8/N and tau=1/16. Take the
bare small-coupling coefficient at fixed mesh before refinement. All
spaces and norms are ordinary stored-coordinate spaces. Retain all
interior axial levels, transverse end rows, both generator orientations
and every exterior heat mode. Import L111's actual F_k(t), J, E_j,
generator stencils T_r,C_r and displacement coefficients b_(r,t).

On the transverse relative vertex and edge spaces let T be the
dimensionless gradient, Delta_0=T^T T and P=T Delta_0^-1 T^T, as in
L085. Vertex fields have zero boundary values; normal end edges remain.
This T is the gradient, not one of the generator's stencils T_r.

Use lower-vertex integer indices on each component. For each transverse
plane pi and each path type b or q, let alpha=(pi,b) or (pi,q), and set

    S_(pi,b)=B_q^T Pi_pi,       S_(pi,q)=-B_b^T Pi_pi.       (1)

Here Pi_pi selects that plane in the finite plaquette space and B_b,B_q
are L088's exact two-edge path maps. Thus S_alpha maps plaquettes to
edges, with bounded multiplicity and fixed range. Define real scalar
functions on all integer transverse indices by extending

    phi_(k,pi,b,t)(x)=b_k(t,x,pi)/a,
    phi_(k,pi,q,t)(x)=q_k(t,x,pi)/a                     (2)

from the existing rows of plane pi by coordinate clamping to that
plane's rectangular index set. No zero extension is used in (2).
For each such scalar phi, M_phi^1 and M_phi^2 multiply every edge or
plaquette component respectively by phi at its lower-vertex index.
Different alpha have different scalar functions; their fixed component
selectors and path filters remain in S_alpha.

## Conclusion

L090(6) implies, for an enlarged fixed polynomial p,

    ||phi_(k,alpha,t)||_infinity <= C p(k),
    |phi_(k,alpha,t)(x)-phi_(k,alpha,t)(y)|
                                    <= C a p(k) |x-y|_1.          (3)

The exact finite scalar projection commutator obeys

    ||[P,M_phi^1]||_HS <= C a L N^(3/2)                 (4)

whenever |phi(x)-phi(y)|<=a L |x-y|_1. In particular (4) applies
to (2), uniformly over all levels and heat labels. This is a
Hilbert--Schmidt estimate; no O(a) operator-norm estimate is asserted.

For Z_(kl;st)=F_l(s)^T P F_k(t) in L111 define the scalar-collected
replacement, still on the actual finite spaces, by

    Z^sc_(kl;st)=a^2 sum_(alpha,beta)
       S_alpha^T P M^1_(phi_(l,alpha,s) phi_(k,beta,t)) S_beta.
                                                               (5)

Then

    ||Z_(kl;st)-Z^sc_(kl;st)||_HS
                            <= C a^3 p(k)p(l) N^(3/2).           (6)

Write the exact moved bulk kernel as

    X_(t,j)=J^* D sum_r T_r C_r E_j M_(b_(r,t)) J.        (7)

Define R_bulk,sc by replacing only Z with Z^sc in L111's moved trace:

    R_bulk,sc=a^-1 sum_(k,l,s,t)c_(i;kl,a) min(s,t)
                              Tr[X_(t,t-s) Z^sc_(kl;st)].        (8)

For both actual probes,

    |R_bulk,moved-R_bulk,sc| <= C_i N^3.                 (9)

Both coefficient levels and the middle finite P remain in (5).
All actual path filters remain in their order; none has crossed P.
The error in (9) may contribute to the a^3 coefficient. No bound for
R_bulk,sc, negligible cubic error, scaled limit, value or compensation
is proved. A finite-to-infinite projection comparison and the remaining
coefficient placements needed for frozen cancellation are still open.
L110/L111's earlier cubic errors also remain. The complete other/other
limit, unevaluated functionals, other jets, finer powers/logarithm,
matching, interacting error <=c_box/2, continuum axioms, reflection
positivity, infrared control and finite positive mass are unresolved.

## Proof

### 1. Extend coefficients, without extending a field across a pinned face

For a plane pi, its relative plaquette indices range over N cells in
each plane direction and N-1 interior vertices in the remaining
direction. Thus they form a rectangular integer set. L090(6), with
its proof from L028's exact smooth-mode prefix, gives the O(a^2 p(k))
neighbor differences of b_k and q_k on all existing plaquette rows.
It includes transverse end rows and levels 1,...,N-1. Division by a
and a coordinate-by-coordinate path inside that rectangle give (3)
there. Coordinate clamping is nonexpansive for the integer l1 distance,
so it preserves this bound and the supremum bound on the entire grid.

This extension does not change a single coefficient in F_k. It supplies
values only when a scalar is evaluated on another component grid during
the following comparison. In particular it does not claim smoothness
of zero-extended edge fields at a face. Any nonzero matrix entry of
S_alpha connects indices at distance bounded by its fixed stencil range;
(3) applies to that pair, including at every boundary row.

### 2. Prove the scalar finite-projection estimate with the pinned vertices

Let M_phi^0 multiply the interior vertex fields by the same scalar.
Define the rectangular finite error

    B_phi=M_phi^1 T-T M_phi^0.

For an oriented edge from x to x+e_nu, extend an admissible vertex
field h by zero on boundary vertices. The convention in L085 gives

    (B_phi h)_(x,nu)
                    =[phi(x+e_nu)-phi(x)] h(x+e_nu).              (10)

This formula is still exact if either endpoint is pinned, since its
h value is zero. Missing tangential boundary edges have no output row.
Every retained row has at most one nonzero coefficient in (10), bounded
by a L, and each vertex occurs in at most three such rows. Therefore

    ||B_phi|| <= sqrt(3) a L.                           (11)

Let U=T Delta_0^-1/2. Positivity of the relative scalar Dirichlet
Laplacian gives U^T U=I, UU^T=P. With Q=I-P, QT=0 implies

    Q M_phi^1 U=Q B_phi Delta_0^-1/2.

Consequently

    ||Q M_phi^1 P||_HS
      =||Q M_phi^1 U||_HS
      <=sqrt(3) a L (Tr Delta_0^-1)^(1/2).              (12)

All matrices are finite; the equality uses U^T U=I. The two off-diagonal
blocks of [P,M_phi^1] are adjoints up to sign because phi is real.
They have orthogonal matrix supports in the P,Q decomposition, so
its squared Hilbert--Schmidt norm is twice the square in (12).

For completeness, the complete relative vertex spectrum from L085 is

    lambda_m=4 sum_(nu=2)^4 sin^2(pi m_nu/(2N)),
                                    1<=m_nu<N.

Since sin(pi m/(2N))>=m/N, lambda_m>=4|m|^2/N^2.
The shell max(m_nu)=r has r^3-(r-1)^3<=3r^2 labels. Summing inverse
eigenvalues over all shells 1<=r<N gives

    Tr Delta_0^-1 <= sum_(r=1)^(N-1) (3r^2) N^2/(4r^2)
                  <=(3/4) N^3.                        (13)

Equations (12)--(13) prove (4). No infinite projection, mass, spectral
truncation or boundary collar removal has been used. The inverse norm
itself is O(N^2), so this argument would not give the asserted power
by replacing the trace in (13) with dimension times the worst mode.

### 3. Move scalars across the path stencils, then across P

By the definitions of F_k in L110/L111 and (1)--(2), exactly

    F_k(t)=a sum_alpha S_alpha M^2_(phi_(k,alpha,t)).

Put

    Ftilde_k(t)=a sum_alpha M^1_(phi_(k,alpha,t)) S_alpha.

At a nonzero entry of each S_alpha, the difference between these two
scalar placements is at most C a p(k) by (3). Bounded row and column
multiplicity of the original path stencil therefore proves

    ||F_k(t)-Ftilde_k(t)|| <= C a^2 p(k),
    ||F_k(t)||+||Ftilde_k(t)|| <= C a p(k).              (14)

Boundary restrictions remove entries rather than add an unbounded
number. No commutator between a path stencil and P is taken.

Let Ztilde=Ftilde_l(s)^T P Ftilde_k(t). Telescoping the two F factors
in Z, using ||P||=1 and (14), gives

    ||Z-Ztilde|| <= C a^3 p(k)p(l).

The finite plaquette space has at most C N^3 rows, so

    ||Z-Ztilde||_HS <= C a^3 p(k)p(l) N^(3/2).          (15)

Expanding the remaining expression leaves

    Ztilde=a^2 sum_(alpha,beta)
          S_alpha^T M^1_(phi_(l,alpha,s)) P
                     M^1_(phi_(k,beta,t)) S_beta.

The scalar functions on this edge space commute with each other,
although neither commutes with P. Its exact difference from (5) is

    Ztilde-Z^sc=a^2 sum_(alpha,beta) S_alpha^T
          [M^1_(phi_(l,alpha,s)),P]
                    M^1_(phi_(k,beta,t)) S_beta.        (16)

Each S has bounded norm and there are a fixed number of alpha,beta.
Apply (4) and (3) to (16) to obtain the right side of (6).
Adding (15) proves (6). The product in (5) still involves levels
s and t independently; it has not been replaced by a same-level or
spatially constant coefficient. Different plane/path coefficients
have not been identified with components of one frozen exterior vector.

### 4. Count the actual moved-trace error using its joint energy kernel

L111(8) supplies for the complete bulk energy kernel

    W_j=(sum_z ||e_j(z)||_F^2)^(1/2)
                            <=C(1+|j|)^(-5/2),
    sum_(j in Z) W_j < infinity.                       (17)

Each translation-invariant finite stencil D T_r C_r has bounded range
and coefficients. Every full input row of its convolution with E_j has
l2 norm at most C W_j: expand the finite shifts and use the triangle
inequality in l2. There are at most C N^3 output rows after J^*,
and input multiplication by b_(r,t) has uniformly bounded norm by
L111's actual smooth displacement bounds. Input restriction by J cannot
increase a Hilbert--Schmidt norm. Hence (7) satisfies

    ||X_(t,j)||_HS <= C N^(3/2) W_j.                    (18)

This argument needs no compact-output assertion after the displacement
has been moved; every finite output row is counted. It also takes no
first absolute moment of a projected alternating factor.

Finite trace Cauchy--Schwarz, (6) and (18) give

    |Tr[X_(t,t-s)(Z_(kl;st)-Z^sc_(kl;st))]|
                    <= C a^3 p(k)p(l) N^3 W_(t-s).     (19)

Retain the full prefix weight. Since min(s,t)<=N and t has fewer
than N possible values,

    sum_(s,t=1)^(N-1) min(s,t) W_(t-s)
                                      <= N^2 sum_(j in Z) W_j.

Multiplying (19) by L111's outside a^-1 and summing all heat labels
using sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i gives

    |R_bulk,moved-R_bulk,sc| <= C_i a^2 N^5
                             =64 C_i N^3.

This proves (9). Every mode and both orientations in the imported
heat-summed trace remain; the estimate works before taking that signed
sum. The complete group's outside factor 3 is not introduced here.

### 5. Applicability and limits of the improvement

L096's obstructed operator is component-dependent and contains unequal
endpoint filters. In (16) only a common-index scalar multiplier crosses
P. All those fixed component selectors and path filters remain on their
original sides of P. Moreover (4) is a Hilbert--Schmidt estimate of size
O(N^(1/2)) when a=8/N, not a small operator bound. Thus (9) does not
reopen the false termwise operator estimate in ATTEMPTS/029. It likewise
does not use the false separate absolute moments in ATTEMPTS/032.

The result controls a definite part of the actual coefficient-placement
error, beyond the recorded generator placement. It leaves a finite P
between S_alpha^T and the product multiplier. Replacing that projection
by a bulk convolution, moving the remaining product past the energy
kernel, and justifying the joint frozen cancellation still need their
own trace estimates. A uniform cubic bound would itself leave existence
and evaluation of the cubic coefficient unresolved. None of the cubic
errors already proved is implicitly discarded.

This is one RESEARCH / REPRODUCTION subtest under the unchanged EXPLORE
assessment `drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The finite contraction and energy estimates are imported. The proof
specializes standard finite projection, relative spectral and trace
identities to this particular placement; the earlier estimates did not
control it with the finite middle P. This is local standard-method
progress, without a novelty claim beyond the sources checked. No value
of either probe is used; any eventual comparison with D_i retains
L084/L082's numerical qualifications.

## Mathlib

Full matching exterior-placement theorem: **not checked**. Supporting
finite orthogonal projection, relative spectrum, Hilbert--Schmidt and
trace identities: **not checked**. Unknown availability is not absence.
No general flow or Ward finiteness theorem is assigned to this isolated
bare forest group.
