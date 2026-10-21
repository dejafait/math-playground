# L244 — Ordered massive boundary transfer for the reduced reverse trace

## Hypotheses

Use exactly L242(3)'s B_(i,N;epsilon,h,delta), with L243's middle
mass h, on the same relative SU(2) cube, lower-rooted forest, admitted
even N, a=8/N, tau=1/16, stored coordinates, bare-first order and
actual probes i=3,6. Retain the original levels 1<=s,t<=n=N-1,
S_st=1_(t<s)+delta_st/2, every source/end row, constant component
index, path/generator filter and finite-mesh heat coefficient.
L242 and L243 are imported with their pending separate-audit qualifications.

Superscripts f,b denote the finite relative spaces and whole grids.
The latter have transverse spaces V_b=l2(Z^3), E_b=l2(Z^3;R^3)
and F_b=l2(Z^3;R^3), with the actual staggered component positions.
Use their usual incidence T_b and circulation D_b. Define

    R_ts^f=[(L_D tensor I+I tensor Delta_T,f+epsilon I)^-1]_ts,
    R_ts^b=[(L_Z tensor I+I tensor Delta_T,b+epsilon I)^-1]_ts,
    G_h^j=(Delta_0,j+h I)^-1,
    Q_delta^j=I-T_j(Delta_0,j+delta I)^-1 T_j*,  j=f,b.       (1)

Here L_Z is the nearest-neighbor axial Laplacian on Z. The block
R_ts^b is taken from its full infinite axial inverse, but s,t in the
comparison trace below retain their original finite ranges. No axial
extension of the response sum is part of this lemma.

On the bulk grid extend L228(1)'s bounded normalized actual exterior
columns, preserving finite samples before pinned zero extension.
With b_k=Bb z_k and q_k=Bq z_k, define

    Z_k^b=a^-1(M_(b_k) Bq-M_(q_k) Bb).                     (2)

This is the same raw path stencil as Z_k^f in L242, with both original
coefficient levels kept. Only its supremum bound and interior agreement
are used here, not a smooth extension of a pinned upper zero. Use
L105(2)'s whole-grid W_t with the same compact displacement and both
endpoint filters. It agrees with the finite W_t on its complete input
and output support, for sufficiently large N.

Define B_i^b by precisely L242(3), replacing R,D,T,G_h,Q_delta,Z,W
by these bulk counterparts, taking the transverse edge trace on E_b,
and retaining s,t=1,...,n and the original c_(i;kl,a). In particular
its two ordered summands are

    Tr[R_ts^b D_b* Z_k^b(s) T_b G_h^b W_t^{b*}
                                      Q_delta^b Z_l^b(t)* D_b]
     -Tr[R_ts^b D_b* Z_k^b(s) T_b G_h^b W_t^{b*}
                                                   D_b* Z_l^b(t)]. (3)

They have the original common prefactor a c_(i;kl,a) S_st.
The bulk trace is a comparison expression, not a replacement Gaussian
law for the physical problem. Every product is trace class because
W_t is finite rank and all inverse masses are positive.

## Conclusion

At the uniform finite-inequality schedule

    epsilon=N^-1, h=N^(-4/3), delta=N^(-2/3),
    m=ceil(60 N^(2/3)log(eN)),                             (4)

both ordered terms, jointly summed over every source, level and heat
label, admit degree-(m-1) inverse-polynomial comparison with error
O_i(N^-13). Their finite and bulk polynomial traces agree exactly.
Consequently, for sufficiently large admitted N,

    |B_(i,N;epsilon,h,delta)-B_i^b(epsilon,h,delta)|
                                                       <=C_i N^-10. (5)

Together with L243(2), this gives

    |R_R-B_i^b(N^-1,N^(-4/3),N^(-2/3))|
                                         <=C_i N^(5/2)log(eN).   (6)

This is quantitative localization and boundary transfer only. The
ordered bulk trace still needs comparison with exactly a^-3 K_(i,R)
in L107(2); coefficient freezing, the weighted axial summation and
mass-removal error for that comparison are not proved here. In
particular the sublinear range alone gives no freezing rate. Other
component rates, quantitative L011 assembly, interacting reflected
error <=c_box/2, continuum axioms, infrared control and finite positive
mass remain unresolved. The separate critical audit in proof section 5
accepts this boundary comparison relative to its imported inputs;
L242--L243 retain their qualifications. This is not a solution candidate.

## Proof

### 1. Anchor the literal ordered traces at the compact insertion

Write G_h and Q_delta for (1), without assuming Q_delta idempotent.
On either transverse space set, for each fixed s,t,k,l,

    X_1^j=Q_delta^j Z_l^j(t)* D_j R_ts^j D_j*
                                              Z_k^j(s) T_j G_h^j,
    X_2^j=D_j* Z_l^j(t) R_ts^j D_j* Z_k^j(s) T_j G_h^j.   (7)

Both map V_j to E_j. Rectangular trace cyclicity turns (3), and
its finite counterpart, into

    Tr_(V_j)(W_t^{j*} X_1^j)-Tr_(V_j)(W_t^{j*} X_2^j).    (8)

These are cyclic rotations only: neither coefficient has crossed
an inverse, circulation, projection or filter. In particular the
second term still has just its original one circulation adjacent
to the covariance on the right of R_ts.

L105(2) writes W_t as a bounded finite-range product containing
the compact multiplier u_(a,1)(t). Thus there are transverse selectors
chi_E(t),chi_V(t), of rank <=C N^3, such that

    W_t^b=chi_E(t) W_t^b chi_V(t)=i_E W_t^f i_V*,
    ||W_t^j||<=C.                                        (9)

The embeddings i_E,i_V extend by zero. If W_t is nonzero, t and
both selectors lie at distance >=cN from every axial/transverse face,
for a fixed c>0, including a fixed stencil allowance. This follows
from the fixed physical clearance of the displacement; the endpoint
averages only enlarge its support by a fixed number of cells.
If W_t=0 both terms in (8) are zero. No compactness is asserted
for X_1,X_2, the covariance, or a projection kernel.

L242's bounds and L228's extensions, with bounded stencil multiplicity,
give on both spaces

    ||Z_k^j(s)||<=C p(k), ||D_j||+||T_j||<=C,
    ||Q_delta^j||<=1, ||G_h^j||<=h^-1, ||R_ts^j||<=epsilon^-1,
    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.                    (10)

For bulk Q the contraction follows either from its Fourier symbol or
the gradient singular values lambda/(lambda+delta). The same finite
singular-value calculation applies on the relative spaces. For the
covariance block use the norm of the full positive-mass inverse;
this bound deliberately makes no favorable axial summation claim.

### 2. Approximate all three inverse positions uniformly

Import the scalar Chebyshev residual of L205(2),(9)--(10), specialized
to finite relative and infinite grids in L229(6)--(7). If
0<mu<=1, there is a degree-(m-1) polynomial p_(m-1,mu) such that
for every bounded nonnegative self-adjoint H with spectrum in [0,16],

    ||(H+mu I)^-1-p_(m-1,mu)(H+mu I)||<=mu^-1 eta_mu,
    eta_mu=2 rho_mu^m<=2exp(-m sqrt(mu)/3),
    rho_mu=(sqrt(16+mu)-sqrt(mu))
                                    /(sqrt(16+mu)+sqrt(mu)). (11)

The scalar polynomial theorem is imported, not reproved. Its
hypotheses hold here: L229 checks the true relative interval factors,
including normal end diagonals and constant normal modes, and their
infinite symbols. The covariance uses four factors with spectral
sum <=16; Delta_0 uses three with sum <=12. L085's Delta_T has the
relative component tensor form used in that same check. No scalar
Dirichlet condition is imposed on every link component. On the bulk
grid the bounded self-adjoint spectral theorem applies also at zero
frequency because every mass is positive.

Replace the full covariance inverse by its polynomial and take its
(t,s) block; replace G_h by its polynomial; replace Q_delta by
I-T p_(m-1,delta)(Delta_0+delta I) T*. Write tildes for all of
these and for (7). Then on each space

    ||R_ts-Rtilde_ts||<=epsilon^-1 eta_epsilon,
    ||G_h-Gtilde_h||<=h^-1 eta_h,
    ||Q_delta-Qtilde_delta||<=12delta^-1 eta_delta.        (12)

If eta_epsilon,eta_h<=1 and 12delta^-1 eta_delta<=1, the corresponding
polynomial norms are at most 2epsilon^-1, 2h^-1 and 2. Telescope
the two changed inverse positions of X_2 and the three of X_1,
keeping their literal order. From (10)--(12), for J=1,2,

    ||X_J^j-Xtilde_J^j||
       <=C p(k)p(l)epsilon^-1 h^-1 E_m,
    E_m=eta_epsilon+eta_h+delta^-1 eta_delta.              (13)

There is only one Q in X_1 and none in X_2. All D,T and both
Z factors are retained. This estimates all covariance inputs and
outputs before any spatial restriction.

### 3. Exact interior polynomial paths with the two levels retained

The covariance polynomial has four-dimensional range <=m-1. In
particular its (t,s) block is zero when |s-t|>m-1. Its finite and
bulk versions have this same property. For a nonzero block the two
levels are therefore within m of each other. The middle inverse is
a transverse polynomial of range <=m-1, and the projection polynomial
has range <=m+1, including its two incidences. The Z,D,T and generator
filters have fixed range. A common upper bound on the transverse
path length in either Xtilde word is 4m+r_*, with r_* fixed.
All intermediate axial coordinates in the covariance polynomial
are also within that bound of t.

The middle factor T G_h in (7) is a transverse matrix between the
layer-indexed factors, not an extra axial Green kernel. Its layer
identification must not be called a local axial step: the required
bound on |s-t| comes from the covariance polynomial just proved.
The exact triangular S_st is kept outside both words throughout.

Take 4m+r_*<cN with a fixed further stencil margin. Expand a
polynomial word into its finite sums of nearest-neighbor Laplacian
steps and the existing path/incidence stencils. Starting at any row
of chi_E(t), every intermediate vertex, edge and plaquette index
then lies strictly inside the physical box, at either s or t or
an intermediate covariance level. Finite and bulk Laplacian entries,
component positions and exterior coefficients agree at every such
index. Each endpoint is still in the finite vertex input grid.
Therefore there are full row identities

    chi_E(t)(i_E Xtilde_J^f i_V*-Xtilde_J^b)=0,
                                                   J=1,2. (14)

When |s-t|>m-1 both sides vanish already. No covariance source column
was discarded in (14): polynomial propagation shows that every
possible endpoint from the selected row is interior. Actual inverse
tails, all physical end rows and all constant indices remain in
the global errors (12)--(13). Using (9), cyclicity and embedding
invariance of finite traces, (14) gives exact equality of each
finite and bulk polynomial trace in (8), at every original s,t.

### 4. Count every row, level and heat label before choosing parameters

For any finite-rank K, |Tr K|<=rank(K)||K||. The range of
W_t* (X_J-Xtilde_J) is contained in chi_V(t). Equations (9),(13)
give the same bound on each space,

    |Tr[W_t*(X_J-Xtilde_J)]|
       <=C N^3 p(k)p(l)epsilon^-1 h^-1 E_m.               (15)

There are at most n^2 original axial pairs. Bound |S_st|<=1 only
in this error estimate; the retained traces still contain S_st and
its diagonal half. Sum (15) for J=1,2, both finite/bulk errors,
and the full heat envelope (10), with the original a prefactor.
Since a n^2 N^3<=C N^4, (14) yields the uniform inequality

    |B_i^f-B_i^b|
       <=C_i N^4 epsilon^-1 h^-1
                        (eta_epsilon+eta_h+delta^-1 eta_delta). (16)

This explicit n^2 count is why an ordinary operator approximation
is sufficient at the deliberately high accuracy used here. A small
operator error without this count would not justify the assertion.
All estimates and the range/accuracy conditions precede (4).

At (4), h is the smallest mass. Hence every eta_mu in (16) is
at most eta=2(eN)^-20. The accuracy conditions hold, and
(4m+r_*)/N=O(N^(-1/3)log(eN)) tends to zero, so (14) holds for
sufficiently large admitted N. Finally

    N^4 epsilon^-1 h^-1(2+delta^-1)eta
       <=C N^(4+1+4/3+2/3)eta
       =C N^7 eta<=C N^-13.                              (17)

This proves the stronger polynomial comparison and (5). Combining
with L243's already uniform finite bound gives (6). No fixed-mass
limit receives varying parameters, and no R_L trace estimate is
transferred. Only the common scalar approximation tool was reused.

The comparison deliberately retains the finite axial level ranges.
It neither extends them to Z nor freezes the two coefficient levels.
The original middle-inverse order and both signs in (3) remain.
Comparison with L107(2), including its triangular half-factor, remains
a separate quantitative obligation; no mass-removal or freezing rate
for that bulk functional is inferred from (17). This is local progress
by established polynomial/spectral and trace-ideal methods, classified
REPRODUCTION under the prior reverse-remainder EXPLORE assessment,
without claiming progress beyond the sources checked.

### 5. Separate critical audit of the ordered boundary comparison

Audit date: 2026-10-20. Verdict: accept (5), including the stronger
O_i(N^-13) comparison, relative to the stated imported inputs.
Equation (6) follows conditionally on L243(2); this audit does not
independently certify that middle-mass estimate or L242's projection
estimate. No exponent is improved and no progress beyond the checked
standard polynomial/spectral methods is claimed.

**Domains and cyclic orders.** On each finite or bulk layer,
T:V->E, D:E->F, Z_k:E->F, W_t:V->E, G_h:V->V and
R_ts:E->E. Thus the two words in (7) really are maps V->E.
In the first word, starting from V on the right, the intermediate
spaces are V,E,F,E,E,F,E,E, after G_h,T,Z_k,D*,R_ts,D,Z_l*,Q_delta.
In the second they are V,E,F,E,E,F,E, after
G_h,T,Z_k,D*,R_ts,Z_l,D*. These give exactly (8) by cyclicity
with the finite-rank W_t*, for finite matrices and bounded bulk
operators alike. The second word has no extra Q or extra circulation
beside R_ts. Neither word is obtained by transposing the other.

L105(2) has the literal stencil
W_(t,mu)=-C_mu* M_(u_(a,1)(t)) C_mu D_mu.
The endpoint averages and dimensionless difference have bounded
norms and fixed ranges. Nonzero input and output rows of this product
are within a fixed number of cells of the compact multiplier support.
They therefore have fixed physical clearance on both sides and
rank at most C N^3 in a transverse layer. If the multiplier is zero
at t, W_t is zero; otherwise t also has axial clearance cN.
This proves the applicability of (9) without assigning compact output
to X_J or to a Green column. Interior embedding of W_t is exact.

**Scalar input and complete inverse errors.** The input used from
L205 is the explicit polynomial residual (2),(9)--(10),(14), with
the finite/infinite spectral specialization in L229(6)--(7), not
L229's differently ordered product estimate. The four-factor covariance
L_D tensor I+I tensor Delta_T is nonnegative self-adjoint with
spectrum in [0,16]; the three-factor vertex Laplacian has spectrum
in [0,12]. These are the same relative component operators checked
there, with their normal end diagonals and allowed constant indices.
Their bulk Fourier symbols have the same upper bounds. Positive mass
permits the bounded self-adjoint spectral theorem even when zero
belongs to the infinite-grid spectrum. Restriction to an axial block
is a contraction in operator norm, so it preserves the full covariance
approximation error. No input or end row is removed by that restriction.

The projection difference costs ||T||^2 delta^-1 eta_delta,
with ||T||^2<=12, while ||Q_delta||<=1. Telescope
the three inverse positions of X_1 and the two of X_2 without changing
their order. Bounds on the polynomial norms follow from (12) under
the stated accuracy conditions. Each term then costs at most
C p(k)p(l) epsilon^-1 h^-1 times, respectively, eta_epsilon,
eta_h or delta^-1 eta_delta. This is (13) on the complete spaces;
the constant is independent of all three masses under those conditions.
L228(1)'s sample-preserving extensions bound the bulk Z_k by the
same polynomial mode envelope as the finite Z_k. No regularity or
pinning assertion for a rough kernel is used.

**Full-row propagation with a nonlocal level identification.** A
power of the four-dimensional covariance Laplacian changes the axial
index by at most its degree. Consequently both polynomial blocks
vanish identically when |s-t|>m-1. For a remaining pair, start from
an output edge selected by chi_E(t) in either word, reading matrix
entries from left to right. Every transverse step belongs to one
of the at most three polynomial factors or to a fixed local stencil;
4m+r_* is a valid common upper range bound. The covariance paths
have axial distance at most m-1 from t; the other coefficients are
at s or t, and |s-t|<=m-1. The transverse G_h factor identifies
vertex coordinates at the two levels but has no independent axial
propagation. It cannot defeat the covariance's bound on |s-t|.

For 4m+r_*<cN with the stipulated stencil margin, all intermediate
indices, and every possible input endpoint, are interior. The finite
and bulk component, incidence and coefficient entries coincide there.
Expansion in polynomial powers therefore proves (14) as a full row
identity, including the claim of zero entries for inputs outside
the finite grid. It is not merely equality on two compressed endpoints.
The rectangular vertex endpoint in X_2 satisfies the same argument.
Using W_t*=W_t* chi_E(t) now proves equality of both polynomial
traces for each original pair s,t. No finite level range is extended,
and S_st, including its diagonal half, is unchanged.

**Complete count and schedule.** For each mode pair and axial pair,
W_t*(X_J-Xtilde_J) has rank at most C N^3 and norm at most the
right side of (13) times ||W_t||. The finite-rank trace inequality
therefore gives (15), including on the infinite grid. Sum the errors
for both words and both spaces, all n^2 axial pairs and all heat
labels. The imported absolute envelope
sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i holds for each actual probe.
It controls the entire sum, without a new heat cutoff or deletion
of allowed constant labels. Since a=8/N and n=N-1, the row/level
prefactor is a n^2 N^3<=8N^4, precisely (16).

At (4), m sqrt(mu)/3>=20 log(eN) for every one of the three
masses, because h is the smallest. Thus eta_mu<=2(eN)^-20;
the accuracy conditions hold and (4m+r_*)/N tends to zero.
The remaining error is bounded by
C_i N^(4+1+4/3)(2+N^(2/3))2(eN)^-20<=C'_i N^-13.
This verifies the claimed stronger error and hence (5) for sufficiently
large admitted N. Adding L243(2) once gives (6) with its original
qualification. The proof specifies no effective numerical constant
or threshold mesh; neither is required for this asymptotic assertion.

No unsupported assertion was found within this specialization.
It does not audit the upstream inverse/projection comparisons, apply
a fixed-mass limit at varying masses, freeze an exterior coefficient,
or identify the bulk trace with L107(2). The eventual component and
L011 assembly retain their independent premises. There is no new
reflected-error estimate, interacting theory or mass-gap conclusion.

## Mathlib

Full matching ordered reverse-trace boundary-transfer theorem: **not
checked**. Supporting bounded self-adjoint spectral calculus,
Chebyshev approximation, finite-propagation polynomial matrices,
rectangular trace cyclicity and finite-rank trace inequalities:
**not checked**. Unknown coverage is not absence. The imported local
scalar polynomial input and its checked spectral hypotheses are
specified above; no external continuum Ward or flow theorem is
claimed to supply this isolated bare forest estimate.
