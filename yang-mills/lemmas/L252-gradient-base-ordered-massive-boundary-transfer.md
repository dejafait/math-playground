# L252 — Boundary transfer of the ordered massive gradient-base trace

## Hypotheses

Use precisely L250(1)--(2)'s smooth finite trace and L251's definition
of S_(i,N,epsilon): the relative all-face SU(2) cube, lower-rooted
direction-1 forest, sufficiently large admitted even N, a=8/N,
tau=1/16, stored coordinates, bare-first order and actual probes
i=3,6. Retain all finite transverse sources, normal end edges,
levels 1<=t<N, allowed constant component indices and the complete
continuum exterior heat matrix c_(i;kl). No outside factor 3 occurs.
All imported qualifications remain; L251's separate audit accepts
its comparison relative to its stated inputs.

Here are explicit whole-grid comparison operators; they do not define
a replacement physical covariance law. Write j=f,b for the finite
spaces of L250 and the whole-grid spaces

    V_b=l2(Z^3), H_b=l2(Z^3;R^3), J_b=l2(Z^3;R^3).

Use the original tail-indexed incidence T_j:V_j->H_j, initial-endpoint
selector E_j:V_j->H_j and circulation D_j:H_j->J_j. On V_j put

    Delta_j=T_j* T_j, R_j=(Delta_j+epsilon I)^(-1),
                              0<epsilon<=1.                       (1)

Coordinates on the bulk vertex grid are y=-4(1,1,1)+a n.
Let pi:R^3->[-4,4]^3 clamp each coordinate to that interval.
Extend L104(1)'s h_k and v_l transversely by composition with pi,
at each unchanged level x_1=-4+at. This specifies bounded global
extensions, agreeing with every sample in the closed cube. Only
boundedness and this agreement are used below. Extend the smooth
compact u_1 by zero; its support has fixed clearance from every face.

On the bulk space form X^h_(k,t;b)=T_b* M_(h_k)E_b-E_b* M_(h_k)T_b,
sampling h at the actual edge midpoints. Form zeta^v_(l,t;b) by
exactly L250(1), with beta=v_mu+v_nu, chi=v_nu-v_mu at the
plaquette tail and both whole-grid raw Bb,Bq rows unchanged. Form
W_t^b by exactly L103(3)'s filters with this u_1. On the finite
spaces use precisely L250's X^h,zeta^v,W^u, including its zero
end-wedge representative. Denote these by X^j,zeta^j,W^j.
Thus no finite coefficient, raw path or endpoint filter is frozen.

Define the bulk comparison by

    a^3 S^b_(i,N,epsilon)=a^4 sum_(k,l)c_(i;kl) sum_(t=1)^(N-1)(at)
      Tr_(V_b)[R_b X^b_(k,t) R_b (W_t^b)* D_b* zeta^b_(l,t) T_b]. (2)

The original finite S_(i,N,epsilon), denoted S^f below, has exactly
the same formula with j=f. The bulk trace and series in (2) are
well defined, as proved below; the cumulative h is not compact.

## Conclusion

At the finite-inequality schedule

    epsilon=N^(-2/3),
    m=ceil(260 epsilon^(-1) log(eN)),                       (3)

the two finite and bulk degree-m inverse-polynomial traces agree
exactly. Their inverse approximation errors give, for large N,

    |S^f_(i,N,epsilon)-S^b_(i,N,epsilon)|<=C_i N^(-10).      (4)

Combining this boundary comparison with L250 and L251 gives

    |R_gx(i,N)-S^b_(i,N,N^(-2/3))|<=C_i N^(5/2).           (5)

The combination (5) is conditional on those imported results, with
L251's imported qualifications unchanged. The separate critical audit
in proof section 5 accepts (4)--(5) relative to these inputs.

In particular the retained bulk expression must still be compared
quantitatively with exactly a^(-3)K_(i,G) in L104(6). It contains
the spatially varying h,u_1,v_l in their original order. No freezing
rate, sharper complete remainder, quantitative L011 assembly,
interacting reflected error <=c_box/2, continuum axioms or finite
positive infrared mass follows. There is no solution candidate.

## Proof

### 1. A compact trace anchor and full-space bounds

The finite relative scalar space consists of vertices with zero
boundary values. Its Delta_f has diagonal 6 and nearest-neighbor
entries -1 with missing neighbors pinned to zero. Its spectrum lies
in (0,12]. Delta_b is the bounded whole-grid scalar Laplacian, with
Fourier multiplier sum_mu |1-exp(i theta_mu)|^2 in [0,12].
These are scalar vertex statements, not scalar boundary conditions
on the relative edges. All normal end edges of T_f and the original
finite circulation and raw paths remain.

L250's polynomial mode bounds and the bounded extensions above give
on both spaces, uniformly in t,N,

    ||X^j_(k,t)||<=C p(k), ||zeta^j_(l,t)||<=C p(l),
    ||T_j||+||E_j||+||D_j||<=C, ||W_t^j||<=C,
    ||R_j||<=epsilon^(-1),
    sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i.                     (6)

The first bound follows directly from the two terms defining X^h,
bounded h and bounded T,E. The bound for zeta follows from its two
coefficient multipliers and bounded multiplicities of the actual raw
path rows. Composing h,v with pi preserves their supremum bounds.
The W bound follows from its two bounded averaging/difference
filters and bounded u_1, without an inverse estimate. One enlarged
fixed polynomial p suffices before either full heat sum is taken.

Both input and output of W_t^b lie in a fixed-range neighborhood of
the compact support of u_1(-4+at,.). There are selectors chi_V(t),
chi_H(t) with rank <=C N^3, fixed physical transverse clearance,
and, for sufficiently large N,

    W_t^b=chi_H(t) W_t^b chi_V(t)=i_H W_t^f i_V*,          (7)

where i_V,i_H embed the finite arrays into the whole grids by zero.
Indeed the only coefficient in W is the compact vertex multiplier;
its fixed endpoint/centered filters enlarge that support by a bounded
number of cells. On this neighborhood no finite stencil meets a
face, so its entries are identical to the bulk stencil entries. If
the axial slice misses the support then both W_t are zero. No claim
of compactness is made for X, an inverse, or any covariance output.

Put, in the displayed order,

    A_j=D_j* zeta^j_(l,t) T_j,
    K_j=A_j R_j X^j_(k,t) R_j : V_j->H_j.               (8)

Rectangular trace cyclicity gives

    Tr_(V_j)[R_j X^j R_j (W_t^j)* D_j* zeta^j T_j]
                                      =Tr_(V_j)[(W_t^j)* K_j]. (9)

On the bulk space this is valid because W_t is finite rank and all
other factors are bounded for positive epsilon. Each trace has
absolute value at most C N^3 epsilon^(-2)p(k)p(l), by the rank of
W_t and (6). Consequently (6), the finite axial sum and
a^4 N^3 sum_t(at)<=C prove absolute convergence of (2), without
restricting a single kernel source. This also justifies cyclicity
and subsequent heat summations.

### 2. Import the scalar polynomial and bound both errors

Use exactly the geometric polynomial in L104(14) and L249(6):

    rho=12/(12+epsilon),
    p_m(Delta_j)=(12+epsilon)^(-1)
                sum_(r=0)^m [I-(Delta_j+epsilon I)/(12+epsilon)]^r.

The finite spectral theorem and the bounded self-adjoint spectral
theorem on the bulk space yield

    ||p_m(Delta_j)||<=epsilon^(-1),
    ||R_j-p_m(Delta_j)||<=epsilon^(-1)rho^(m+1).          (10)

The scalar spectrum just checked verifies their hypotheses. Thus
the same already proved polynomial formula applies on the two
spaces; there is no new decay theorem or reproof of a general
approximation result. In particular (10) is an error in the entire
operator, before insertion of any compact selector.

Let P_j=p_m(Delta_j) and K_j^pol=A_j P_j X^j P_j.
Telescoping in the literal order gives

    K_j-K_j^pol
       =A_j(R_j-P_j)X^j R_j+A_j P_j X^j(R_j-P_j),
    ||K_j-K_j^pol||<=C p(k)p(l)epsilon^(-2)rho^(m+1).  (11)

There are exactly two inverse positions. No multiplier has crossed
an inverse, incidence or path map. Since rank W_t<=C N^3, each
finite or bulk trace error in (9) is bounded by

    |Tr[(W_t^j)*(K_j-K_j^pol)]|
                 <=C N^3 p(k)p(l)epsilon^(-2)rho^(m+1). (12)

This uses the finite-rank trace inequality |Tr B|<=rank(B)||B||.
The bulk operator (W_t^b)*(K_b-K_b^pol) has range in chi_V(t),
so exactly the same inequality applies there. Every source, output,
end row and low eigenvalue remains inside the full errors (10)--(11).

### 3. Exact polynomial paths, without absolute-walk freezing

There is a fixed integer r_* bounding the total lattice range of
W*, D*, zeta, T and either term of X, including component offsets.
Since Delta is nearest-neighbor, each P_j has propagation at most
m. Choose a fixed c>0 smaller than the displacement clearance in
lattice units divided by N, allowing the fixed stencil margin. When

    2m+r_*<cN,                                           (13)

expand Tr[(W_t^j)* A_j P_j X^j P_j] into local stencil entries and
Laplacian powers. A nonzero diagonal term starts at a vertex in the
output support of W_t*, hence within the compact neighborhood in (7). Traveling
around the whole closed word covers at most 2m+r_* cells. Every
intermediate vertex, edge and plaquette therefore remains strictly
inside the transverse cube. The finite and bulk Laplacian entries,
path rows, endpoint filters, displacement and coefficient samples
are identical at every such index. In particular the finite zero
end-edge representative of h is never encountered. The noncompact
h at the visited interior indices is retained exactly; there is no
restriction on its cumulative axial integral or upper tail.

Conversely every nonzero bulk polynomial trace term starts at the
same W neighborhood, and under (13) follows this same interior
enumeration. Thus, term for term,

    Tr[(W_t^f)* K_f^pol]=Tr[(W_t^b)* K_b^pol].           (14)

For fixed N,m these are finite sums, even on the whole grid. No
bound on the sum of absolute polynomial coefficients is needed:
the two polynomials are used only for exact locality in (14) and
the spectral errors in (10). Their growing coefficients are not
used to freeze any deterministic coefficient. Polynomial paths
which could reach a face are absent under (13); all corresponding
tails of the original inverses remain bounded by (12). This proves
an equality of complete polynomial traces, not a covariance-source
cutoff or an extension identity for the full resolvent.

### 4. Normalize, sum, then choose the mass and degree

Combine (12) for j=f,b with (14), multiply by a^4(at), and sum
all exterior labels and all original t=1,...,N-1. The heat envelope
in (6) and a^4 N^3 sum_t(at)<=C give the uniform finite inequality

    |a^3(S^f_(i,N,epsilon)-S^b_(i,N,epsilon))|
                              <=C_i epsilon^(-2)rho^(m+1),
    |S^f_(i,N,epsilon)-S^b_(i,N,epsilon)|
                           <=C_i N^3 epsilon^(-2)rho^(m+1),       (15)

whenever (13) holds. All bounds and the range condition precede
the mesh-dependent schedule.

For 0<epsilon<=1, log(1+epsilon/12)>=epsilon/13.
At (3) this gives rho^(m+1)<=(eN)^(-20). Moreover

    (2m+r_*)/N=O(N^(-1/3)log(eN)) -> 0,
    N^3 epsilon^(-2)rho^(m+1)<=C N^(13/3-20)
                                           =C N^(-47/3).         (16)

Hence (13) holds for sufficiently large N and (15) implies (4).
This degree is O(N^(2/3)log(eN)); the inverse square-root length
N^(1/3) is not used as a propagation theorem. The deliberately
small error in (4) is not an optimized rate.

L251(2) supplies |R_gx-S^f_(i,N,N^(-2/3))|<=C_i N^(5/2),
already including L250's coefficient replacement and L102/L103's
removed terms once. Adding (4) proves (5), with the imported audit
qualifications unchanged. No fixed-mass qualitative limit is used
at a varying mass. All constant component labels remain in the
continuum heat sum; no exterior or internal spectral truncation
was introduced.

The remaining bulk-to-L104(6) comparison is unproved. In particular
L249's absolute-walk coefficient-freezing loss is not replaced by
(14), which changes no coefficient. The failed operator-norm,
termwise-commutation and separate first-absolute-moment shortcuts
remain stopped. An eventual ordered joint estimate must address
the original variable coefficients; sublinear range alone does not
bound that error.

This is RESEARCH / REPRODUCTION under the unchanged approved EXPLORE
assessment `drafts/literature/2026-10-20-gradient-base-crossed-quantitative-remainder.md`.
It specializes the existing scalar polynomial and finite-rank trace
methods to this exact cumulative trace and compatible mass. No
general literature theorem is reproved; no claim of originality
beyond the checked sources, signed growth or complete target rate
is made.

### 5. Separate critical audit, 2026-10-20

The audit accepts (4)--(5) under the unchanged EXPLORE assessment
`drafts/literature/2026-10-20-gradient-base-complete-remainder-critical-audit.md`.
It imports L250 and the separately audited L251, with their upstream
qualifications. This verifies the existing specialization and adds no
new boundary estimate or general decay theorem.

**Spaces, anchor and full operator errors.** Both scalar Laplacians
have spectrum in [0,12], with the finite one strictly positive.
The bounded self-adjoint spectral theorem therefore applies to the
same geometric polynomial on both full spaces. Its maximum scalar
ratio is rho=12/(12+epsilon), giving exactly (10), even though the
bulk spectrum contains zero. Positive epsilon is essential. The two
inverse telescoping errors each cost epsilon^-2 rho^(m+1), multiplied
only by bounded local stencils and polynomial mode envelopes.

W:V->H has both supports within a fixed number of cells of u, because
its coefficient is between fixed endpoint and centered-difference
filters. Its rank is O(N^3) per level. Thus W* K is trace class in the
bulk and cyclicity in (9) is justified; no restriction of the sources
of R is involved. The finite-rank trace inequality gives (12) on the
whole finite and bulk spaces before either heat summation or mass
choice. Clamping h and v suffices for these operator norms; no
derivative bound or compactness of h is used in this boundary proof.

**Complete closed paths.** The local word is W* D* zeta T P X P.
Either summand of X contains just its two endpoint incidences/selectors
and the edge coefficient. The three planes, two raw paths per plane,
and every W component have uniformly fixed extra range r_*.
Both polynomial factors together have range at most 2m. A diagonal
term starts in the vertex support of W*, and its entire sequence of
intermediate vertices, edges and plaquettes is within 2m+r_* cells
of that start. Under (13) they are all strictly interior. At every
visited index the finite and bulk scalar Laplacians, incidences,
raw rows, coefficient samples and endpoint filters agree. The zeroed
finite end-wedge representative is never visited. Conversely every
bulk closed path begins at that same finite support and is counted
in the finite expansion. This proves (14) for complete polynomials,
without an absolute coefficient bound or a covariance-output cutoff.

The uniform inverse errors retain the boundary-reaching paths of the
original resolvents. Since each factor is a transverse slice operator,
there is no additional axial propagation claim. All t=1,...,N-1 and
the original cumulative endpoint remain unchanged.

After multiplying by a^4(at), the rank/level count and the complete
heat majorant give (15). At epsilon=N^(-2/3), m is
O(N^(2/3)log(eN)), so (13) holds for sufficiently large N. The logarithm
bound epsilon/13 yields rho^(m+1)<=(eN)^-20, and the unnormalized
error is at most C N^(13/3-20), smaller than N^-10. Adding L251(2)
once establishes (5). No coefficient-freezing rate follows from this
path argument, and no fixed-mass limit has been used at varying mass.

## Mathlib

Full matching ordered gradient-base boundary-transfer theorem:
**not checked**. Supporting bounded self-adjoint spectral calculus,
geometric inverse approximation, finite propagation, finite-rank
trace cyclicity and trace inequalities: **not checked**. Unknown
availability is not evidence of absence. The proof is analytic;
no numerical certificate or mathematical script is used.
