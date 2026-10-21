# L238 — Keep the transverse gradient attached to the full prefix

## Hypotheses

Use exactly L100(1) and L237(1)--(2): the relative all-face pinned
SU(2) cube, straight lower-rooted direction-1 forest, sufficiently
large admitted even N, a=8/N, tau=1/16, ordinary stored coordinates,
bare-first coefficient and both actual probes i=3,6. Retain every
relative source/end row, allowed constant component index and the
complete exterior heat sum. Write

    K_epsilon=(Delta_E+epsilon I)^(-1)Q, 0<epsilon<=1,
    X_k=K_epsilon Omega_(gh,k)^T,
    Y_l=K_epsilon Omega_(hh,l),
    D_mu=S[U_mu,T_1]C_mu,
    E_pref=-T sum_(mu=2)^4 D_mu,
    a A=A_loc+E_pref.                                  (1)

All maps and their orders are those in L100(7), reproduced in
L237, proof section 3. In particular S is the entire lower axial
prefix with its half diagonal, U_mu is the actual displacement
multiplier, T is the transverse pinned vertex-to-edge incidence,
and P T=T, Q=I-P. The finite identity (1) already includes the
lower-end term's justified removal by compact displacement support.
No other endpoint term is removed here.

Import the complete skew alternating matrix in L088(3), its actual
heat coefficients in L088(4)--(5), the split Omega_k=F_k+H_k in
L089(1), and the neighboring coefficient estimates in L090(6).
Use the two-edge path telescoping identities of L087(9) with their
pinned vertex convention, and the relative tensor spectrum used in
L090(8)--(11). These inputs retain the actual endpoint filters and
the entire mode set. No co-closed diagonal trace conclusion is
transferred to this crossed trace.

## Conclusion

For the exact full prefix contribution in L237(12),

    R_(pref,epsilon)=a^-1 sum_(k,l)c_(i;kl,a)
                                  Tr(X_k E_pref Y_l),

one has the uniform finite bound

    |R_(pref,epsilon)|
      <= C_i N^(5/2)[1+a/sqrt(epsilon)+a/epsilon].      (2)

Consequently at epsilon=N^-1,

    |R_(pref,N^-1)|<=C_i N^(5/2).                      (3)

Define R_(loc,epsilon) by replacing A by A_loc/a in L237(2),
without changing any other factor. Combining (3) with L237(3)
gives

    |R_L-R_(loc,N^-1)|
                     <=C_i N^(5/2)sqrt(log(eN)).       (4)

This is only a partial quantitative reduction. The remaining local
trace has no established O(N^(5/2)log(eN)^2) bound here. Its
projection, localization, coefficient-freezing and relative-boundary
errors, other L011 component rates, the interacting reflected bound
<=c_box/2 and the continuum/infrared construction with finite positive
mass remain unresolved. This proof and its new ordered estimate
await a separate critical audit; L237 is imported with its pending
audit qualification. There is no complete-solution candidate.

## Proof

### 1. Localize only the deterministic transverse prefix output

The displacement samples vanish in a fixed physical neighborhood of
each transverse face. Choose a transverse vertex diagonal selector
chi, of norm at most one, equal to one on the transverse projection
of all their supports and zero outside a slightly larger fixed
interior region. For all sufficiently large N, its selected vertices
and every incident path/circulation stencil have fixed physical
clearance from the transverse faces. A smooth cutoff is unnecessary:
no derivative of chi will be taken. Tensor chi with the identity on
all N-1 interior axial levels.

Both U_mu and [U_mu,T_1] act separately at each transverse vertex.
The axial prefix S does not change that vertex. Thus exactly

    D_mu=chi D_mu.                                    (5)

The complete axial output of D_mu need not be compact: its tail up
to level N-1 is retained. Equation (5) restricts neither a covariance
source nor a projection output. In particular no chi is moved
through T, P, Q or K_epsilon.

The individual prefix count used in L100(8) gives

    ||D_mu||_HS<=C N^(3/2).                            (6)

For completeness, [U_mu,T_1] has at most two entries per column,
each of size at most Ca. Every S entry is 0,1/2 or 1. On each
transverse vertex fiber every entry of S[U_mu,T_1] therefore has
size at most Ca. Its squared HS norm is at most Ca^2 N^2.
There are at most N^3 fibers. Composition on the right with the
contraction C_mu gives (6), since aN=8. This counts all axial rows,
including the full tail; it does not estimate a truncated prefix.

### 2. An interior two-difference estimate with full relative inputs

For w on the finite transverse-link array E, let nabla_int w and
nabla_int^2 w denote any fixed finite family of first and second
unscaled coordinate differences, with fixed stencil shifts, restricted
to the transverse interior region needed above. All axial levels are
retained; only transverse differences are needed below. Then

    ||nabla_int w||<=C ||Delta_E^(1/2) w||,
    ||nabla_int^2 w||<=C ||Delta_E w||.                 (7)

Here is the finite spectral justification, including boundary types.
On each edge component, the relative product modes have sine factors
in vertex coordinates and cosine factors in their own edge coordinate;
the axial coordinate of E is Dirichlet. Extend each component by its
corresponding odd/even reflection to the doubled periodic intervals,
keeping the half-step edge locations. This extension has norm at
most a fixed constant times the finite component norm. It intertwines
the component Laplacian with the periodic one; the constant own-edge
mode is included. A first unscaled difference has Fourier modulus
d_j=2|sin(theta_j/2)|. Two differences have modulus d_j d_r,
including j=r. Since the Laplacian symbol is rho=sum_j d_j^2,
d_j^2<=rho and d_j^2 d_r^2<=rho^2. Parseval on the doubled array
proves (7); restriction and the finite stencil shifts only change
the fixed constant. The needed interior stencils agree with the
original finite differences, so this uses no zero extension of a
normal edge and imposes no scalar Dirichlet condition on it.

For arbitrary x in E set w=K_epsilon x. The exact spectral
commutation of Q with Delta_E gives

    ||Delta_E w||<=||x||,
    ||Delta_E^(1/2)w||<=epsilon^(-1/2)||x||,
    ||w||<=epsilon^(-1)||x||.                          (8)

The constants are uniform: rho/(rho+epsilon)<=1 and
sqrt(rho)/(rho+epsilon)<=epsilon^(-1/2). No input mode or source
row of x is restricted in (7)--(8). The extension is solely a proof
of a finite norm estimate, not a replacement of K_epsilon by an
infinite-grid covariance.

### 3. Keep the gradient inside the left alternating factor

The load-bearing composite estimate is

    ||K_epsilon Omega_k^T T chi||
       <=C p(k)[a+a^2/sqrt(epsilon)+a^2/epsilon].       (9)

Since K_epsilon is symmetric, its left side equals
||chi T^T Omega_k K_epsilon||. The exact complex identity Cc T=0
holds on the entire relative cube, including pinned end edges.
Consequently L089(1) gives, before any inequality,

    T^T H_k=(Bq T)^T M_(b_k) Cc
                         -(Bb T)^T M_(q_k) Cc.        (10)

Both other terms vanish by T^T Cc^T=0, not by commuting a
multiplier or by discarding a boundary contribution. In plane mu nu,
L087(9) specifies the complete paths on a pinned vertex field phi:

    (Bb T phi)(v)=phi(v)-phi(v+mu+nu),
    (Bq T phi)(v)=phi(v+mu)-phi(v+nu).                 (11)

Therefore, at an interior vertex v, their adjoints applied to a
plaquette array z have respectively the values

    z(v)-z(v-mu-nu),
    z(v-mu)-z(v-nu).                                 (12)

The selector chi ensures every plaquette in (12) exists in the
finite array. Each displayed diagonal difference is the sum of two
nearest-neighbor plaquette differences. Apply (12) to z=m Cc w,
where m=b_k or q_k, separately for each plane and axial level.
For each neighboring plaquette pair use the exact identity

    m(v+e)z0(v+e)-m(v)z0(v)
     =m(v+e)[z0(v+e)-z0(v)]
                          +[m(v+e)-m(v)]z0(v).

Here z0=Cc w consists of two unscaled first coordinate differences
of the link components. Its neighboring difference is a fixed sum
of second coordinate differences. L090(6) bounds m by Ca p(k)
and its neighboring difference by Ca^2 p(k). Bounded stencil
multiplicity, (7), (8) and (10)--(12) now give

    ||chi T^T H_k K_epsilon x||
       <=C p(k)[a ||Delta_E w||
                           +a^2 ||Delta_E^(1/2)w||]
       <=C p(k)[a+a^2/sqrt(epsilon)]||x||.             (13)

No axial shift occurs in these paths, so (13) holds also at levels
1 and N-1 without an axial collar restriction. All transverse face
sources of w remain present; only the deterministic vertex output
of (10) is selected. In particular L090's global staggered collar
term has not been declared small: its exceptional output rows are
absent from this specific compact composite by (5).

For the actual exterior-circulation part F_k, retain both terms.
L088(5) and bounded path multiplicity give ||F_k||<=Ca^2 p(k).
Using ||T||<=sqrt(12), ||chi||<=1 and (8) yields

    ||chi T^T F_k K_epsilon||<=C a^2 p(k)/epsilon.    (14)

Adding (13),(14) proves (9). The small mass is not chosen until
after this uniform finite inequality. Neither a projection nor a
coefficient has crossed the inverse. An estimate for Omega_k
alone, with its gradient detached, would not give (13).

### 4. Close the original full-prefix trace

Because Omega_(gh,k)^T=Q Omega_k^T P and P T=T,

    X_k T chi=K_epsilon Omega_k^T T chi.              (15)

This uses P T=T before chi, never P chi=chi P. By (1),(5),
the exact prefix trace is

    R_(pref,epsilon)
      =-a^-1 sum_(k,l,mu)c_(i;kl,a)
                           Tr((X_k T chi)D_mu Y_l).   (16)

All products are the original compatible rectangular maps; (16)
needs no cyclic move through a variable factor. L237(10), imported
from L100's full-spectrum estimate, gives

    ||Y_l||_HS<=C p(l)N                              (17)

uniformly for 0<epsilon<=1. The finite inequality
|Tr(B D Y)|<=||B|| ||D||_HS ||Y||_HS applies in (16).
Equations (6),(9),(17) bound each summand by

    C p(k)p(l) a^-1
       [a+a^2/sqrt(epsilon)+a^2/epsilon] N^(3/2) N.

The unchanged full heat estimate
sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i proves (2). This polynomial
may be enlarged as in L090(6); it is still summable for both actual
probes, including all allowed constant indices. At epsilon=N^-1,
a/sqrt(epsilon)=8/sqrt(N) and a/epsilon=8. Thus (2) proves (3).
Finally R_(L,epsilon)=R_(loc,epsilon)+R_(pref,epsilon) exactly.
L237's mass-removal error at epsilon=N^-1 proves (4).

This is a RESEARCH / REPRODUCTION specialization under the unchanged
EXPLORE assessment for the complete quantitative R_L target. The
path identities and spectral framework are imports, with the
necessary ordered-composite applicability argument supplied above.
The product-rule and finite tensor Parseval verification are needed
to retain these particular gradient, prefix and boundary placements;
no general theorem is reproved or claimed as a discovery. No
numerical certificate or external new source is used. The local
companion remains, and this does not audit upstream analytic inputs.

### 5. Separate critical audit of the full-prefix estimate

Audit dated 2026-10-19, STEP_ID YM-20261019-339-left-crossed-complete-rate-audit.
Accept (2)--(4) relative to the stated finite contraction, relative
spectrum and exterior-mode estimates, with L237's comparison checked
in its separate audit in this same step. This supersedes the original
pending-audit qualification without claiming a new exponent.

The selector in (5) acts on the vertex output of D_mu only. Neither
the axial prefix S nor its commutator changes the transverse index,
so its full axial tail remains inside chi D_mu. On each fiber the
N-by-N entry count is O(a^2 N^2); the N^3 transverse fibers give
the claimed squared norm O(N^3). Right composition with C_mu is
a contraction and does not remove a source row.

For (7), the doubled sine/cosine extension uses the same component
boundary type as Delta_E. First transverse differences have multiplier
bounded by sqrt(rho), and every ordered pair of such differences
by rho. Restricting their outputs to the needed transverse interior
does not change that upper bound. The cosine constant mode remains;
its difference is zero, not an omitted summand. No axial difference
is needed in (12)--(13), so the last axial level requires no cutoff.

The two surviving terms in T^T H_k are exactly (10), since Cc T=0
is a finite relative-complex identity. Applying the adjoint paths
to m Cc w produces a second difference of w with coefficient O(a)
and a first difference with coefficient O(a^2). Their bounds are
a||Delta_E w|| and a^2||Delta_E^(1/2)w||, respectively. The output
selector makes every such transverse stencil interior, while w still
has arbitrary finite covariance input. The two F_k terms instead
cost a^2||w|| and give the retained a^2/epsilon allowance. This
justifies (9) with the actual, unequal path filters.

In (15), P T=T is used before chi; neither P nor the inverse crosses
that selector. The three factors in (16) consequently have norms
O(p(k)[a+a^2/sqrt(epsilon)+a^2/epsilon]), O(N^(3/2)) and
O(p(l)N). Including a^-1 gives exactly (2). At epsilon=N^-1,
the bracket after dividing by a is 1+8/sqrt(N)+8, uniformly bounded.
The complete heat envelope gives (3), and L237 gives (4). This
checks the full-prefix estimate rather than a compact-prefix surrogate.

## Mathlib

Full matching ordered crossed-prefix estimate: **not checked**.
Supporting finite relative incidence identities, sine/cosine
spectral calculus, Parseval and Hilbert--Schmidt trace inequalities:
**not checked**. Unknown coverage is not absence. No continuum
flow-finiteness or Ward theorem supplies the isolated trace estimate.
