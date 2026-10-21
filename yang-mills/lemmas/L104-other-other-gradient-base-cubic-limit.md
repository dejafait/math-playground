# L104 — A finite cubic limit for the gradient-base crossed pair

## Hypotheses

Use exactly L103's G_R, P_(i,N) and R_gx: SU(2), the actual L010
probes i=3,6, straight lower-rooted direction-1 forest, relative
all-face fixed-link box D=(-4,4)^4, sufficiently fine admitted even N,
a=8/N and tau=1/16. Take the bare small-coupling coefficient at fixed
mesh before refinement. All coordinates, transposes and finite norms
are ordinary stored ones. Retain every transverse end row, interior
axial level, ordered plaquette pair including coincidences, and exterior
heat mode. No outside factor 3 is included here.

Import L103's Delta=T^T T, G=Delta^-1, D_T, E, W_t, Zeta_k,
X_(k,t) and G_epsilon=(Delta+epsilon I)^-1. Write D_T for transverse
circulation to distinguish it from the box. Use L080's continuum
relative modes A_k=f_k/sqrt(nu_k) and heat coefficients c_(i;kl),
equivalently L097's conventions, and put

    v_(k,mu)(x)=A_(k,mu)(x)
       -partial_mu integral_(-4)^(x_1) A_(k,1)(r,x_T) dr,
    F_(k,mu nu)=partial_mu v_(k,nu)-partial_nu v_(k,mu),
    delta_(k,mu)=sum_(nu>mu) partial_nu F_(k,mu nu)
                     -sum_(nu<mu) partial_nu F_(k,nu mu),
    h_(k,mu)(x)=integral_(x_1)^4 delta_(k,mu)(r,x_T) dr,       (1)

where every transverse index lies in {2,3,4}. All these are smooth
deterministic mode functions. The prefix in v is used at interior
levels and does not redefine the separately pinned upper potential.

## Conclusion

There is a finite real functional K_(i,G) such that

    a^3 G_R -> K_(i,G),   a^3 R_gx -> K_(i,G).                (2)

Here is a formula specifying the functional without evaluating it.
Use the Fourier convention that a shift S_mu of a tail-indexed array
has multiplier exp(i theta_mu), theta in [-pi,pi]^3. Put

    tau_mu=1-exp(i theta_mu), lambda=sum_mu |tau_mu|^2,
    sigma_k(x,theta)=2i sum_mu h_(k,mu)(x) sin(theta_mu).       (3)

The column tau is the symbol of the tail-minus-head incidence T.
Define the three plane rows, mu<nu, by

    c_(mu nu)=(1-exp(i theta_nu)) e_mu^T
                                +(exp(i theta_mu)-1) e_nu^T,
    b_(mu nu)=e_mu^T+exp(i theta_mu) e_nu^T,
    q_(mu nu)=-exp(i theta_nu) e_mu^T
                                     +exp(i theta_mu) e_nu^T,
    (z_v)_(mu nu)=(v_mu+v_nu)q_(mu nu)
                                      -(v_nu-v_mu)b_(mu nu).          (4)

Let c be the matrix of the three c rows. These are the raw tail-indexed
versions of L088(11)/L097's staggered symbols, retaining both paths.
Let w(x,theta) be the exact constant-coefficient symbol of L103(3)'s
W with u_(a,1) replaced by u_1(x). To specify the derivative convention
explicitly, C_mu^T has multiplier (1+exp(i theta_mu))/2 and the centered
forward difference T_mu of L065 has multiplier i sin(theta_mu), so

    w_mu=-u_1(x) [(1+exp(i theta_mu))/2] i sin(theta_mu).     (5)

This centered forward difference is distinct from the incidence tau.
Complex adjoints below replace transposes of the real finite matrices.
Set the following integrand to zero at lambda=0:

    K_(i,G)=sum_(k,l)c_(i;kl) integral_D (x_1+4)
      integral_([-pi,pi]^3)
        [sigma_k(x,theta)/lambda^2]
            w(x,theta)^* c(theta)^* z_(v_l)(x,theta) tau(theta)
                                         dtheta/(2pi)^3 dx.          (6)

The spatial/torus integrals and exterior series are absolutely
convergent. No value, sign or equality to a multiple of gamma D_i is
asserted. In particular co-closed-base R_R and transverse R_H,tr still
lack cubic control; K_(i,E), K_(i,ax), K_(i,Q) and K_(i,G) remain
unevaluated. The required joint value is -4 gamma D_i before the
outside factor 3. Other response jets, finer powers/logarithm, matching,
interacting error <=c_box/2, continuum axioms, reflection positivity,
infrared control and finite positive mass remain independent gaps.
There is no Yang--Mills candidate.

## Proof

### 1. Identify the actual cumulative coefficient before freezing

L087(9)--(12) and L103(11) are exact signed identities on each full
pinned layer:

    X_(k,t)=T^T M_(d^>_(k,t)) E-E^T M_(d^>_(k,t)) T,
    d^>_(k,t)=sum_(s>t)d_(k,s)+d_(k,t)/2.                  (7)

For an oriented mu edge starting at v, with both endpoints interior,
the perimeter signs give precisely

    d_(k,s;mu,v)=sum_(nu>mu)
         [f_(k;s,mu nu,v)-f_(k;s,mu nu,v-nu)]
       -sum_(nu<mu)
         [f_(k;s,nu mu,v)-f_(k;s,nu mu,v-nu)].             (8)

Indeed a mu edge is the lower positive and upper negative edge in a
mu nu plane with mu<nu, and the lower negative and upper positive
edge in a nu mu plane with nu<mu. Both incident plaquettes are retained.
An edge meeting a pinned vertex has zero wedge in (7); L087 sets its
d coefficient to zero without changing X. Thus (8) is asserted on the
interior edges where it is used, with the pinned cases still retained
through (7) and its global coefficient bound.

Fix one exterior label k. Its actual circulation f is the direct
circulation of a A_(k,a), since the forest prefix is an exact gradient.
At the plaquette center, L028's centered integral-difference formulas
and L080(5) give

    f_(k;s,mu nu)/a^2=F_(k,mu nu)(x)+O_k(a^2)             (9)

with the same estimate for any fixed number of physical derivatives
of the smooth sample extensions. For completeness, the difference
of the two mu-edge samples is minus a times the centered nu derivative
of A_(k,a,mu), and that of the nu samples is plus a times the centered
mu derivative of A_(k,a,nu). Each centered derivative has O_k(a^2)
error. The exact product-mode physical eigenvalue converges with
O_k(a^2) error by its sine formula. The prefix has zero circulation
exactly, so no derivative of an approximate prefix is needed for (9).
The continuum curl of v equals that of A_k because mixed derivatives
of its smooth prefix commute. These facts prove (9), including the
smooth derivative estimate, uniformly at all s<N.

The two plaquette centers in each difference in (8) lie symmetrically
on opposite sides of the edge center. Applying their integral difference
formula to (9) therefore yields

    d_(k,s;mu)/a^3=delta_(k,mu)(x)+O_k(a^2).             (10)

This is uniform on interior edges, in particular on every fixed compact
transverse region and at every interior axial level. Relative zero
samples preserve the circulation formula at boundary-adjacent
plaquettes. No estimate across the separately pinned s=N potential
is used.

Divide (7)'s cumulative coefficient by a^2. At x_1=-4+at, (10) gives

    d^>_(k,t)/a^2
       =a sum_(s=t+1)^(N-1) delta_k(-4+as,x_T)
                       +(a/2)delta_k(x)+O_k(a^2).        (11)

Changing an edge-center sample to any common point in the same cell
costs O_k(a). Uniform Riemann-sum estimates for smooth delta_k show
that (11) converges to h_k in (1), uniformly in the moving cut t and
on each compact transverse region. In particular the finite half-weight
is retained exactly in (11); its normalized size is O_k(a). It does
not generate a finite endpoint contribution at this normalization.
Missing the upper endpoint in the sum also costs at most O_k(a).

Globally L103(11) gives ||d^>_(k,t)/a^2||_infinity<=C p(k), even on
the pinned rows, hence

    Xhat_(k,t)=X_(k,t)/a^2,
    ||Xhat_(k,t)||<=C p(k).                             (12)

Its transverse range is fixed. For every fixed interior walk its
coefficients converge to those of T^T M_(h_k)E-E^T M_(h_k)T.
The Fourier symbol of this last frozen stencil is sigma_k: E selects
the initial vertex and thus has row multiplier 1; the mu contribution
is h_mu[(1-exp(-i theta_mu))-(1-exp(i theta_mu))]. This proves (3)
with its sign.

### 2. Keep the exact normalization and all other stencil limits

Write zeta_(l,a)=Zeta_l/a. L103(5) with both inverses regularized gives
the exact equality

    a^3 P_(i,N,epsilon)=a^4 sum_(k,l)c_(i;kl,a) sum_t (at)
      Tr[G_epsilon Xhat_(k,t) G_epsilon
                            W_t^T D_T^T zeta_(l,a)(t) T].            (13)

Indeed X contributes a^2, Zeta contributes a and the original prefactor
is a^-1 t; multiplying by a^3 leaves a^5 t=a^4(at). There is no color,
ordered-pair or outside factor change.

L103(13)--(14) give ||W_t||<=C and ||zeta_(l,a)||<=C p(l), with
uniformly bounded fixed ranges and multiplicities. The actual compact
displacement coefficients converge smoothly to u_1 by L028. L080's
exact prefix formula (8)--(10), or its use in L097 section 4, gives
v_(l,a)/a -> v_l on interior rows, with uniform existing-neighbor
control for each fixed label. The constant axial edge mode remains in
that formula. Hence the coefficients of zeta_(l,a) converge uniformly
on the displacement support to the stencil z_(v_l) in (4).

To check the raw paths, a positive mu nu traversal has rows
e_mu, S_mu e_nu, -S_nu e_mu, -e_nu. Therefore its circulation is c,
its first two-edge sum is b, and its second-plus-third sum is q,
exactly (4). Their exterior sums divided by a tend to v_mu+v_nu and
v_nu-v_mu. In particular b tau=1-exp(i(theta_mu+theta_nu)) and
q tau=exp(i theta_mu)-exp(i theta_nu), agreeing with L087's
telescoped vertex rows. This checks the paths independently of a
change of staggered phase. Formula (5) follows from the two endpoint
averages and the centered forward difference in W; it does not change
the tail-minus-head convention of T in (7).

At fixed epsilon all factors in (13) have uniform operator norm
bounded by C_epsilon p(k)p(l). The dimension of its vertex trace is
(N-1)^3, and a^4 sum_t(at) N^3 is bounded independently of N. Thus
normalized trace estimates are uniform. These estimates alone do not
remove epsilon; that removal will use L103's stronger bound.

### 3. Establish the finite pinned trace limit at fixed epsilon

Use the explicit polynomial from L097 section 4:

    p_(epsilon,m)(x)=(1/(12+epsilon))
       sum_(j=0)^m [1-(x+epsilon)/(12+epsilon)]^j,
    sup_(0<=x<=12)|p_(epsilon,m)(x)-1/(x+epsilon)|
                      <=(12/(12+epsilon))^(m+1)/epsilon.              (14)

The spectrum of Delta lies in [0,12]. The finite spectral theorem
therefore gives the same operator error. Replace both inverses in
(13) by p_(epsilon,m)(Delta), telescoping once per position. The
bound |Tr A|<=dimension times ||A||, (12), the bounds in section 2
and the normalized volume count prove that the resulting error is
at most C_epsilon p(k)p(l) times the error in (14), uniformly in N
for each exterior pair. No coefficient is commuted through Delta.

For fixed m the trace is a finite sum of closed walks of index range
bounded independently of N,t. A transverse collar of this fixed width
has O_m(N^2) rows per level. Its contribution, including all pinned
stencil cases, is bounded by

    C_(epsilon,m) p(k)p(l) a^4 N^2 sum_t(at)=O_(epsilon,m,k,l)(N^-1).

Thus the boundary contribution vanishes at cubic normalization. In
fact the W multiplier restricts nonzero walks to a compact physical
region for large N. This observation does not require the cumulative
coefficient h to have compact support. The collar bound remains valid
without deleting any row from the finite trace. Compact axial support
of W also keeps its nonzero walks away from both axial ends.

In the remaining walks freeze the coefficients at a common cell point.
Equations (10)--(12) prove uniform convergence for Xhat on that region,
and section 2 proves it for W,zeta. Smooth limiting coefficients vary
by O_(m,k,l)(a) over a fixed walk. Therefore the error after normalized
summation tends to zero. Each frozen diagonal entry is the zero Fourier
coefficient of the product of its stencil symbols: expansion into
shifts and integration of exp(i n.theta) over the torus select precisely
the closed walks. This finite algebra proves the Fourier-trace identity
without a trace-asymptotic theorem or a bulk/boundary covariance
substitution. The remaining a^4 spatial sum is an ordinary four-
dimensional Riemann sum with weight at=x_1+4.

Consequently, for fixed epsilon and fixed k,l, the limit of (13)'s
pair contribution is the integral in (6) with lambda^-2 replaced by
(lambda+epsilon)^-2. First let N tend to infinity at fixed polynomial
degree; then let m tend to infinity using (14)'s uniform normalized
trace error. This establishes the fixed-epsilon limit, including its
actual cumulative coefficient.

The exterior heat majorant and fixed-pair convergence are imported
from L080(6) and L097 section 5:

    |c_(i;kl,a)| p(k)p(l)
       <=C_i p(k)p(l) exp[-(tau/16)(|k|^2+|l|^2)],
    c_(i;kl,a) -> c_(i;kl).                             (15)

Enlarge the fixed polynomial p for the finitely many coefficient
derivatives above. The right side is summable over the complete
component-labeled relative spectrum. Extend nonadmitted modes by zero.
The fixed-epsilon normalized trace bound in section 2 and (15) justify
uniform tail removal followed by finite-pair convergence. Thus the
entire a^3 P_(i,N,epsilon) has the stated regularized limit, denoted
K_(i,G,epsilon); no exterior heat mode is omitted.

### 4. Remove the regularization only after its trace limit

The explicit frozen formula is uniformly integrable. Indeed

    |sigma_k|<=C p(k) sqrt(lambda),
    ||w||<=C sqrt(lambda), ||c||<=C sqrt(lambda),
    ||z_(v_l)||<=C p(l), ||tau||=sqrt(lambda).

The first bound uses bounded h_k and sin^2(theta_mu)<=|tau_mu|^2;
the second uses the actual endpoint filters, of modulus at most one.
The circulation rows in (4) prove the third. Hence the absolute
regularized scalar integrand is at most

    C p(k)p(l) lambda^2/(lambda+epsilon)^2
                                             <=C p(k)p(l).          (16)

The physical weight and volume are bounded, and (15)'s continuum
version is summable. Dominated convergence gives
K_(i,G,epsilon)->K_(i,G) in (6), proves its absolute convergence,
and defines it independently of the value assigned at lambda=0.

Crucially, L103(7) controls the actual trace, not merely its frozen
symbol. For each fixed 0<epsilon<=1 and all sufficiently large N,

    |a^3 P_(i,N)-a^3 P_(i,N,epsilon)|
                                     <=C_i epsilon^(1/4),           (17)

since eventually N sqrt(epsilon)>=1 and a^3 N^3=512. Apply the
triangle inequality with the fixed-epsilon limit proved in section 3:

    limsup_N |a^3 P_(i,N)-K_(i,G)|
       <=C_i epsilon^(1/4)+|K_(i,G,epsilon)-K_(i,G)|.

Sending epsilon to zero proves a^3 P_(i,N)->K_(i,G). No choice of
epsilon depending on N is made. L103(6)'s O(N^2) and O(N^(5/2))
errors transfer this limit to G_R and R_gx respectively, proving (2).
Reality follows from the real finite traces; it also follows directly
by theta -> -theta conjugation of the raw symbols. Neither argument
supplies a sign.

### 5. What this attempt adds and what it leaves open

The fixed-epsilon trace limit and its coefficient identification were
not present in L103. The specialization needed here is (8)--(11)'s
upper cumulative coefficient convergence, followed by the finite pinned
trace argument in section 3. L103's existing inverse error is imported
with unchanged hypotheses; L097's polynomial formula and L080's actual
prefix/heat normalization are reused, not reproved as general theorems.
No general Ward/flow finiteness theorem is invoked to assign a value
to this isolated action group.

This is one RESEARCH / REPRODUCTION proof attempt under the unchanged
EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
It establishes local standard-method progress without a claim of
originality beyond the sources checked. L094/ATTEMPTS/028's reverse
operator obstruction, L096/ATTEMPTS/029's termwise commutator obstruction
and L099/ATTEMPTS/030's quartic-only H estimate remain intact. No scalar
polarization, free reverse-block gain or singular operator-norm
approximation was used. The whole other/other contribution and its
comparison with -12 gamma D_i remain unresolved. Any later numerical
comparison retains L082's saved-table/IEEE qualifications.

## Mathlib

Full matching gradient-base cubic limit: **not checked**. Supporting
finite spectral polynomial approximation, trace identities, Riemann
sums and dominated convergence: **not checked**. Unknown availability
is not evidence of absence. The displayed mathematical arguments are
the verification; structural documentation validation cannot verify
their hypotheses or estimates.
