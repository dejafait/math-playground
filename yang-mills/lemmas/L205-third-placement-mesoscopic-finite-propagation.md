# L205 — Sublinear finite propagation for the third-placement covariance legs

## Hypotheses

Use L204's complete SU(2) setting: relative box (-4,4)^4, sufficiently
fine admitted even N, a=8/N, straight lower-rooted direction-1 forest,
complete compact L008 displacement, both actual L010 probes i=3,6 at
tau=1/16, and bare expansion at fixed mesh before refinement. Coordinates
and adjoints are ordinary full variable-link coordinates. Keep every
physical face, normal end edge, allowed constant own-direction mode,
insertion subtraction and exterior heat mode.

Thus Delta is the dimensionless relative one-form Hodge Laplacian,
P its co-closed projection, S=P Delta^(-1), A=PAP the full signed
symmetric residual, and M=2SAS. Retain L204(1)'s linear functional

    Q_(i,N)[X]=-6a^2 sum_(k,l)d_(i;kl)
                    Tr(J_(e_l) X U_(n_k)^T P),       (1)

where n_k=S e_k, J_y=P Gamma_y P, and H,V,U,Gamma and both pinned
prefixes have exactly their original definitions. In particular
Q_(i,N)[M]=Q_(3,i,N). Only X in (1) will change.

For 0<epsilon<=1 set R_epsilon=(Delta+epsilon I)^(-1) and
M_epsilon=2R_epsilon A R_epsilon, as in L204(20). For integer m>=1
define T_0(x)=1, T_1(x)=x and
T_(j+1)(x)=2x T_j(x)-T_(j-1)(x), and put

    r_(m,epsilon)(t)=T_m((8+epsilon-t)/8)/T_m(1+epsilon/8),
    p_(m-1,epsilon)(t)=(1-r_(m,epsilon)(t))/t,
    Z_(m,epsilon)=p_(m-1,epsilon)(Delta+epsilon I),
    M_(m,epsilon)^pol=2 Z_(m,epsilon) A Z_(m,epsilon). (2)

The quotient defining p is a polynomial of degree at most m-1:
r_(m,epsilon)(0)=1. No numerical polynomial evaluation is assumed.

## Conclusion

Write

    rho_epsilon=(sqrt(16+epsilon)-sqrt(epsilon))
                    /(sqrt(16+epsilon)+sqrt(epsilon)),
    eta_(m,epsilon)=2 rho_epsilon^m.

Uniformly in N,epsilon,m,

    |Q_(i,N)[M_epsilon]-Q_(i,N)[M_(m,epsilon)^pol]|
       <=C_i N^(7/2) eta_(m,epsilon)(2+eta_(m,epsilon)). (3)

Each Z is componentwise of graph range at most m-1 on the actual
relative component grids, including their normal end rows. Take

    epsilon_N=N^(-7/4),
    m_N=ceil(6 epsilon_N^(-1/2) log N), d_N=m_N-1,
    M_N^pol=M_(m_N,epsilon_N)^pol.                    (4)

Then eta_(m_N,epsilon_N)<=2N^(-2), d_N=O(N^(7/8)log N)=o(N), and

    |Q_(i,N)[M_(epsilon_N)]-Q_(i,N)[M_N^pol]|
                                                   <=C_i N^(3/2), (5)
    Q_(3,i,N)=Q_(i,N)[M_N^pol]+O_i(N^(23/8)),
    a^3|Q_(3,i,N)-Q_(i,N)[M_N^pol]|<=C_i N^(-1/8),  (6)
    G_(i,a)=-Q_(i,N)[M_N^pol]+o(N^3).                (7)

Here G is L202's original joint cubic probe-jet group. The polynomial
trace is cubic-bounded by (6) and L202, with no proved limit or coefficient.

There is also an exact boundary comparison for M_N^pol, for large N.
Let E extend variable links by zero to the full infinite component
grids, Delta_infinity be their standard dimensionless scalar
nearest-neighbor Laplacian on each component, and A_ext=E A E^T.
Define Z_infinity by the same polynomial (2) with Delta_infinity.
Then

    M_N^pol=2 E^T Z_infinity A_ext Z_infinity E.       (8)

Both endpoints of every nonzero M_N^pol entry lie within d_N graph
steps of the row/column support of A. If r_A is its fixed stencil
range, M_N^pol has range at most 2d_N+r_A in lattice distance between
link centers (allowing half-integer component offsets).
This compares only covariance legs adjacent to A. J, U and P stay
nonlocal, neither prefix is shortened, and no selector is moved
through a projection. Physical faces, constant modes and the upper
prefix jump remain in (1).

This is a local application of standard polynomial and matrix
estimates, not progress beyond the checked sources. Independent
f_(i,2),r_0, full compensation, finer asymptotics, finite matching,
interacting reflected error <=c_box/2, continuum axioms and infrared
finite positive mass remain unresolved.

## Proof

### 1. A relative polynomial residual uniform in the mass

L026(6)--(7) gives spec(Delta) contained in (0,16], including each
allowed constant own-direction mode. Thus spec(Delta+epsilon I)
lies in [epsilon,16+epsilon], where (8+epsilon-t)/8 is in [-1,1].
The Chebyshev recurrence gives

    T_m(cos theta)=cos(m theta),
    T_m((rho+rho^(-1))/2)=(rho^m+rho^(-m))/2.          (9)

Both identities follow by substitution into the recurrence and its
initial values. Hence |T_m(x)|<=1 for |x|<=1. Direct algebra gives

    1+epsilon/8=(rho_epsilon+rho_epsilon^(-1))/2,
    0<rho_epsilon<1.

Consequently T_m(1+epsilon/8)>=rho_epsilon^(-m)/2>0 and

    sup_(epsilon<=t<=16+epsilon)|r_(m,epsilon)(t)|
                                            <=eta_(m,epsilon). (10)

Apply the finite-dimensional spectral theorem. Set

    F=Delta R_epsilon, F_pol=Delta Z_(m,epsilon),
    D_f=F-F_pol.

The polynomial identity t p(t)=1-r(t) gives exactly

    D_f=F r_(m,epsilon)(Delta+epsilon I),
    ||F||_op<=1, ||D_f||_op<=eta,
    ||F_pol||_op<=1+eta.                             (11)

This relative filter estimate avoids an unnecessary epsilon^(-1)
loss in an absolute inverse estimate. The recurrence calculation is
included to justify the mass-uniform residual and effective degree.
L178's different fixed-mass transverse Neumann estimate is not
substituted at a growing degree without an error proof.

### 2. Both errors in the original signed trace

F and F_pol commute with S and P, being functions of Delta. Since
A=PAP, without commuting a filter through A,

    M_epsilon=F M F,
    M_(m,epsilon)^pol=F_pol M F_pol=P M_(m,epsilon)^pol P,
    M_epsilon-M_(m,epsilon)^pol=D_f M F+F_pol M D_f.  (12)

Indeed F_pol S=P Z, which proves the middle identity. Let
E_A=S^(1/2) A S^(1/2), which is signed. L204's imported
original-order bounds from L186--L187 and L203 give

    ||E_A||_op<=C N,
    ||J_(e_l)S^(1/2)||_HS<=C N^(3/2),
    ||P U_(n_k)S^(1/2)||_HS<=C p(k)N^3.              (13)

For the first summand in (12), its trace in (1) is 2Tr(X E_A Y^T),
where

    X=J_(e_l)S^(1/2)D_f,
    Y=P U_(n_k)S^(1/2)F.

For the second use instead

    X=J_(e_l)S^(1/2)F_pol,
    Y=P U_(n_k)S^(1/2)D_f.

Each filter is at the right end of a factor bounded in (13).
The finite trace inequality
|Tr(X E_A Y^T)|<=||X||_HS ||E_A||_op ||Y||_HS bounds their sum by
C p(k)N^(11/2)eta(2+eta). Multiply by a^2 in (1), and use L204's
complete polynomially summable heat expansion, to obtain (3).
Both error placements, the signed residual and the upper pinned
prefix contribution to (13) remain. Positivity of M, rough-column
smoothness and prefix/covariance commutation are not used.

### 3. Degree selection before limits

For u=sqrt(epsilon/(16+epsilon)), rho_epsilon=(1-u)/(1+u).
Integrating 2/(1-v^2)>=2 from 0 to u gives

    log(1/rho_epsilon)>=2u
       >=(2/sqrt(17))sqrt(epsilon)>sqrt(epsilon)/3,  (14)

for 0<epsilon<=1. The degree (4) therefore gives

    eta<=2 exp(-m_N sqrt(epsilon_N)/3)<=2N^(-2).

For N>=2, 2+eta is uniformly bounded, so (3) proves (5).
Since epsilon_N^(-1/2)=N^(7/8), d_N/N tends to zero. Combining (5)
with L204(5)'s O(N^(23/8)) error proves (6), and L202's
G=-Q_3+o(N^3) proves (7). The estimates were uniform before this
simultaneous mass/degree choice. No fixed-degree convergence theorem
is applied with d_N.

### 4. Finite propagation and the compact boundary comparison

L003's relative tensor-product Hodge calculation (proof section 2)
and L026's spectrum identify Delta as a sum of scalar
nearest-neighbor Laplacians on each component: its own coordinate
is an edge interval, the other three interior vertex intervals.
Normal end rows have the actual edge-interval diagonals. There is
no component mixing. A product of j copies of Delta+epsilon I
joins only rows separated by at most j nearest-neighbor steps;
diagonal steps do not increase distance. Induction proves this
including all end rows. A degree d polynomial thus has range d.

L018(2) writes the complete residual as

    A=(L K_a+K_a^T L)/2-Q_3-Q_6.

L028, proof section 1, specifies its endpoint/clover, incidence,
coefficient and reverse-adjoint factors. Each has a fixed finite
stencil. Every term contains a compact displacement or strain
multiplier, with only a fixed number of shifts on either side.
Thus there is a fixed compact K inside (-4,4)^4 containing A's row
and column support for all sufficiently fine meshes, and its range
r_A is bounded independently of N. This retains both subtractions.
The coefficients may grow with N; their size is irrelevant to
the exact propagation argument.

The distance from K's component rows to a physical end is at least
cN steps for some c>0, after a fixed stencil allowance. For large N,
d_N=o(N) implies that every path of at most d_N steps starting in
A's support stays away from rows where the finite and infinite
Laplacians differ. Finite and infinite paths have identical
coefficients and endpoints, all inside the variable-link grids.
Compare each power in (2), starting at a column of A, to get

    E Z_(m_N,epsilon_N) A=Z_infinity E A.             (15)

Equivalently, Z_infinity E agrees with E Z on vectors supported
in K. Since A has both input and output support in K, this identity
and its transpose give
Z_infinity E A E^T Z_infinity=E Z A Z E^T.
Multiplying by E^T and E proves (8).

The support statement follows from the range bound on both sides
of A; the triangle inequality gives range 2d_N+r_A.
The physical enlargement a d_N=O(N^(-1/8)log N) tends to zero,
so all endpoints stay in a fixed compact interior enlargement
of K. Nothing here replaces finite P by an infinite projection.

The prefixes in J and U can traverse long axial intervals even
when their adjacent X indices are interior. Their pins, faces,
coefficient levels and source rows remain. Small d_N/N alone does
not control coefficient freezing: the available absolute trace
count is O(N^(7/2)), and multiplying it by d_N/N would not give
o(N^3). A sharper signed estimate or exact prefix evaluation is
still required for the cubic limit.

All checks are analytic: the spectral interval, polynomial
divisibility, both trace-error orders, mass/degree exponents and
finite-path comparison. No numerical diagnostic or mathematical
script is used. This removes covariance-leg tails as an obstacle,
while leaving the signed prefix/coefficient-limit problem.

## Mathlib

Full matching actual-probe mesoscopic comparison and joint cubic
limit: **not checked**. Supporting Chebyshev recurrence, spectral
functional calculus, polynomial propagation and Hilbert--Schmidt
ideal inequalities: **not checked**; unknown coverage is not absence.
The finite-dimensional spectral theorem is used in its standard
self-adjoint form. The elementary Chebyshev identities are verified
above because the relative error, effective degree and varying mass
must be justified here. L003 and L026 supply the relative grid and
spectrum, L018 and L028 the complete residual's compact local
stencil, L204 the signed trace and ordered estimates, and L202 the
joint-group reduction. No general renormalization theorem is reproved.
The unchanged [approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers this bounded attempt within the exact joint-group target.
