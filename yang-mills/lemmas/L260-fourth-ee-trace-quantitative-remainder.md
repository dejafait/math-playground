# L260 — Quantitative remainder for the fourth ordered E,E trace

## Hypotheses

Keep precisely L167 and L168's relative SU(2) cube D=(-4,4)^4,
admitted even N, a=8/N, tau=1/16, lower-rooted direction-1 forest,
ordinary stored coordinates and bare-first expansion. Let X_i be
L167(1), with its coefficient -1, for both actual probes i=3,6.
Retain both Q subtractions, every action/source/end row, the upper
jump, constant axial modes and the complete exterior heat sums.

Use the exact residual A=(L K_a+K_a^T L)/2-Q_3-Q_6 and its compact
support and smooth coefficient bounds from L018/L028 and L166.
Import the relative Green/image estimates in L164--L167, the global
smooth bulk exterior extension in L164(3), and the raw interior
exterior and complete heat estimates in L248(3)--(11). Their upstream
analytic premises and audit qualifications remain imports. No numerical
sign or IEEE enclosure is needed. K_(i,R) is exactly L145's functional,
identified with this trace's coefficient by L168(2).

## Conclusion

For mesh-independent constants and sufficiently fine admitted meshes,

    |X_i-a^(-3)(3/2)K_(i,R)| <= C_i N^2,       i=3,6.       (1)

In particular this meets the requested N^(5/2)log(eN)^2 budget.
The separate critical audit in proof section 6 accepts this quantitative
specialization relative to its imports; it does not audit the imported
lemmas. It supplies only this component
rate. Second/third ordered-trace rates, complete quantitative assembly,
interacting reflected control, continuum axioms and a finite positive
infrared mass remain unresolved. This is local progress using the
assessed standard kernel method, not a claim of originality.

## Proof

### 1. Preserve the ordered trace and normalize its kernels

L167(3) already gives, with all three smooth-column terms and the
upper exterior accounted for once,

    X_i = sum_(k,l,c) c_(i;kl,a)
           Tr[B_(h_k t_c) Ghat_v Dhat^T
                         B_(ell_b t_c) Fhat Ahat] + O_i(N^2). (2)

The retained sign is +1. F=Phi Sigma; G_v is the scalar vertex
Dirichlet inverse. The two B maps are endpoint sums with color bracket,
not averages. In an entry of (2), e is in a fixed compact interior
enlargement S of both index supports of A, v is an endpoint of e,
f is an arbitrary variable link and w is an endpoint of f. There
are O(N^4) possible e and bounded endpoint/color multiplicities.
Only transverse e,f survive since both bulk forest exteriors have
zero component 1. For a fixed exterior pair write p(k),p(l) for
fixed polynomials; they will be summed with heat at the end.

Put

    J_N(v,f)=(G_v D^T)_(v,f),
    H_N(w,e)=a(F A)_(w,e).

Let g be the infinite unscaled Z^4 scalar Green kernel, copied to
link components, and freeze the dimensionless generator a K_a at
u(x_e), where x_e is the physical midpoint of e. Its frozen value
K^0 and A^0=(L^0 K^0+(K^0)^T L^0)/2 are exactly L168(6).
Set

    J_inf(v,f)=(g D^T)_(v,f),
    H_inf,e(w)=(Phi_- g A^0(u(x_e)))_(w-e).               (3)

Phi_- has the same component-1 inputs w_1-j-1/2, j>=0, as L168(8).
No finite prefix is replaced by an odd principal value. The observation
e remains fixed while its prefix sources are compared.

In the following estimates r=1+dist(e,f) and b=1+|e_T-f_T|;
fixed endpoint and stencil shifts change only constants. The imported
estimates and their infinite versions give

    |J_N| <= C(r^-3+N^-3),   |J_inf| <= C r^-3,
    |H_N|+|H_inf,e| <= C b^-3.                            (4)

The bound for H_inf follows by summing the frozen residual kernel
C(1+dist(z,e))^-4 along the complete axial line, not by a bounded
prefix operator norm. The frozen residual bound follows from the
same constant-coefficient two-difference decomposition as L166(8)--(9).

### 2. Uniform normalized residual comparison before the prefix sum

We prove, for every variable source link z and e in S, with
R=1+dist(e,z),

    |a(Sigma A)_(z,e)-(g A^0(u(x_e)))_(z-e)|
          <= C[a R^-3+a^2 R^-2+N^-4].                   (5)

Symmetry changes this to the row comparison of a A Sigma with
A^0 g. This is essential: every coefficient of A in this expression
lies a bounded number of lattice steps from e, regardless of z.
It does not freeze a coefficient at a remote prefix source.

Write Kbar=a K_a. By L028's explicit endpoint/clover composition,
Kbar is a fixed finite sum of component shifts with coefficients
k_b(y) sampled from smooth u_a. If k_b^0 is its constant value with
u replaced by u(x_e), then on the finite row stencil around e,

    |k_b-k_b^0| <= C a,
    |partial k_b| <= C a,  |partial partial' k_b| <= C a^2. (6)

These unscaled differences include all staggered offsets. They follow
from L028(4)'s uniform physical C^2 bounds and O(a^2) convergence
of u_a; transposed stencils have the same properties.

The image/spectral proofs in L164(5), L166(7), and L165 section 2
give the following difference comparisons, not just magnitude bounds:

    |partial_e^j(Sigma-g)_(e',z)| <= C N^(-2-j), j=0,1,2,
    |(P-P_inf)_(e',z)| <= C N^-4.                       (7)

Here e' ranges over the fixed enlargement of e, P=L Sigma and
P_inf=L^0 g. Each difference is on the appropriate single-component
grid; the P comparison includes the mixed observation/source
Dirichlet differences. To recall why (7) is uniform in z, only e'
is separated from all faces. Every nonidentity reflected image is
then at least cN away. The j-difference heat integral up to N^2 is
O(N^(-2-j)); the finite sine/cosine tail and infinite heat tail are
of the same order. The two Dirichlet differences for P give N^-4.
The identity entries of P cancel in P-P_inf. These are precisely
the error terms in the cited proofs, including normal end sources
and the constant own-direction edge mode. No scalar Dirichlet
condition is substituted for a normal link condition.

In L Kbar Sigma, replace Sigma by g first. Apply the exact twice
iterated discrete product rule to each local product k_b times its
component Green entry. By (6)--(7) this costs

    C[N^-4+a N^-3+a^2 N^-2] <= C N^-4.                 (8)

Now freeze k_b in L Kbar g. The same product rule bounds the
difference by

    C[a R^-4+a R^-3+a^2 R^-2].                         (9)

This uses respectively two, one and zero Green differences. The
right incidence inside Kbar may be bounded as a fixed local map;
it is not needed for an additional decay gain. Each cross-component
term uses its corresponding scalar component Green function.

For the other orientation use Kbar^T L Sigma=Kbar^T P exactly.
The P comparison in (7) costs C N^-4. Freezing the transposed
coefficients then costs C a R^-4, including the identity part of
P_inf at bounded R. There is no commutation of a coefficient with P.
Finally L166(10), retaining both Q forms in their original order,
gives

    |a(Q_j Sigma)_(e,z)| <= C a(R^-3+N^-3), j=3,6.       (10)

Since a=8/N, the constant part is O(N^-4). Equations (8)--(10),
with the symmetric residual factor 1/2, prove (5). They do not use
smooth-column consistency on a rough Green column.

Sum (5) over the actual prefix inputs z below the interior vertex w.
With b=1+|w_T-e_T|, elementary one-dimensional integral comparisons give

    sum_(n in Z)(1+sqrt(n^2+(b-1)^2))^-j <= C b^(1-j),
                                                     j=2,3,4.

There are at most N finite prefix inputs. The missing infinite
inputs below the lower root have axial distance at least cN from e,
since e is compactly interior. Their frozen residual sum is at most
C sum_(n>=cN) n^-4 <= C N^-3, uniformly in w. Therefore

    |H_N(w,e)-H_inf,e(w)|
           <= C[a b^-2+a^2 b^-1+N^-3].                 (11)

This holds for every interior w, including the last interior axial
level. It compares the full actual lower prefix with the half-line,
without truncation or a varying-cutoff limit. No upper prefix extension
has been introduced. Boundary vertex w is handled separately below.

### 3. Ordered product comparison and every boundary endpoint

L167 section 2 also proves, uniformly for all variable f and compact v,

    |J_N(v,f)-J_inf(v,f)| <= C N^-3.                    (12)

For the moment take f whose endpoint stencil is wholly interior.
Use the exact two-term telescoping

    J_N H_N-J_inf H_inf,e
          =(J_N-J_inf)H_N+J_inf(H_N-H_inf,e).           (13)

The transverse shell of radius m has at most C(1+m)^2 sites,
and the full axial sum of r^-3 is at most C(1+m)^-2.
All finite f lie within O(N) lattice steps of e. Equations
(4),(11)--(13) consequently give, for each e and its endpoints,

    sum_f |(J_N-J_inf)H_N| <= C N^-2 log(eN),
    sum_f |J_inf(H_N-H_inf,e)|
       <= C[a sum_(m<=CN)(1+m)^-2
             +a^2 sum_(m<=CN)(1+m)^-1+N^-2]
       <= C[a+a^2 log(eN)+N^-2].                       (14)

Thus the complete ordered product error is O(a+N^-2 log(eN)),
which is O(a). Neither factor alone was given a uniform small
operator norm; both kernel placements stay exactly as in (2).

Here are the required tail and first-moment counts for the frozen
product, also useful for all excluded endpoint stencils. Uniformly
in the component and bounded shifts, put

    q(n,y)=(1+sqrt(n^2+|y|^2))^-3(1+|y|)^-3.

Then

    sum_(n,y) q(n,y) <= C,
    sum_(n,y)(1+sqrt(n^2+|y|^2)) q(n,y) <= C,
    sum_(sqrt(n^2+|y|^2)>R) q(n,y)
                         <= C R^-2 log(eR), R>=2.      (15)

For the second estimate, sum the axial power -2 first, obtaining
C(1+|y|)^-1, and then sum transverse shells C(1+m)^-2.
For the last estimate, the part |y|>R/2 costs C R^-2 by
the axial power -3 sum. In the remaining part necessarily |n|>cR;
its axial sum is O(R^-2), and the transverse sum of (1+|y|)^-3
through radius R is O(log(eR)). These estimates include small
distances by the added 1. They are joint moments, not first absolute
moments of either undamped factor separately.

To treat boundary vertices in B_ell, temporarily remove a fixed-width
collar of f containing every boundary-touching endpoint stencil.
Its distance from e is at least cN. For the original product, (4)
and (15) bound the decaying part of this collar by C N^-2 log(eN)
per e. Its N^-3 b^-3 part is bounded by the first estimate in (14),
even if summed over the entire box. Both normalized exterior
values are globally bounded by C p(k)p(l) on the actual bulk links,
by L167 and L164. Hence the removed original collar has the stated
O(N^-2 log(eN)) normalized row cost. This retains every normal
end link and the zero endpoint of each such link through an explicit
error estimate. The discontinuous axial upper exterior was already
estimated in (2) and is not part of ell_b.

Apply (13)--(14) on the remaining interior links, where all endpoint
maps agree with the infinite maps. After exterior freezing in the
next section, restoring the infinite collar and every link outside
the original cube costs the same bound by (15): every missing link
is at least cN from e. Thus no missing endpoint, fixed tangential
link, covariance source or exterior half-line is silently discarded.

### 4. Raw exterior freezing, full heat matching, and quadrature

In (2) each normalized product J_N H_N is multiplied by

    a (h_(k,e)/a) ((ell_b)_(l,f)/a),

with its original endpoint maps and color bracket. This accounts
for both exterior factors a and the single a^-1 in F A. The
product comparison in section 3 may use their bounded actual values;
it does not yet match the remote exterior to a continuum sample.

On the remaining interior f, use L164(3)'s smooth bulk extension
componentwise to compare ell_b(f)/a with an actual link of the same
component within bounded distance of e. Its error is
C a p(l) r. Only that nearby link is then matched to V_l(x_e)
using L248(6)--(8). Likewise h_k(e)/a matches V_k(x_e) locally.
Both local errors are C a times fixed mode polynomials. It follows
that the product of the two normalized exterior values differs
from V_(k,nu)(x_e)V_(l,mu)(x_e) by at most

    C a p(k)p(l) r.                                    (16)

For different components choose their respective nearby reference
links; no difference between different component functions is taken.
The positive stored-link orientation is unchanged. The two endpoint
slots of each B retain their identical link coefficient and their
two incidence placements. Thus their frozen symbols are the same
2 eta_nu V_(k,nu) and 2 eta_mu V_(l,mu) used in L168(13).
Equation (15)'s joint first moment bounds the complete cost of (16)
by C a p(k)p(l) per normalized row. We have not extended L248's
interior raw matching to the pinned upper value or asserted that
a rough prefix is smooth.

Extend the resulting frozen source sum to every infinite f by
section 3. Let d_(kl,nu) be its density for observation component nu,
including every endpoint and color. L168 sections 3--4 identify their
sum. The prefix half-weight, symmetric residual factor and color sum
therefore give precisely

    sum_(nu=2)^4 d_(kl,nu)(x)
                    =(3/2)g_G u_1(x) V_k(x) dot V_l(x). (17)

This imports that established coefficient calculation, not its
qualitative finite-box limiting argument as a rate. There is no new
outside factor 3 and no further sign reversal.

All the errors through (16), multiplied by a^3 and summed over e,
have magnitude at most

    C a^4 |S| p(k)p(l)[a+N^-2 log(eN)]
                          <= C a p(k)p(l),             (18)

since |S|<=C N^4. The finite support of u and its stencil enlargement
also permit including all midpoint cells in this expression; each
component density vanishes outside that compact support. Before component summation,
each component density is smooth and compactly supported with C^1 norm
bounded by a fixed polynomial in k,l: this follows either from the
absolutely summable frozen kernel linear in u and smooth V, or directly
from the component integrals in L168(16)--(17). On each cell, integrating
its difference from the midpoint value costs at most the cell volume
times C a p(k)p(l). Summing cells on each staggered component grid gives
an O(a p(k)p(l)) quadrature error. No rough Green column receives a
Taylor estimate.

Finally use L248(10)--(11) for both actual full probe matrices:

    |c_(i;kl,a)|+|c_(i;kl)| <= C_i exp[-c0(|k|^2+|l|^2)],
    |c_(i;kl,a)-c_(i;kl)|
       <= C_i a(1+|k|+|l|)^4 exp[-c0(|k|^2+|l|^2)].     (19)

Every polynomial in (18) and the density/quadrature estimates is
summable against this Gaussian, by the same full-mode count in
L156(8). Finite-mesh omitted continuum labels have at least one
index of order N; their polynomially weighted Gaussian tail is
O(exp(-c N^2)), hence O(a). Allowed zero axial indices and their
constant prefixes are retained. The triplet average of four products
and both shear polarizations are already included in (19).

Restoring the already heat-summed error in (2), whose cubic-normalized
size is O(N^-1), proves

    |a^3 X_i-(3/2)g_G B_(i,R)| <= C_i/N.                (20)

As a^(-3)=N^3/512, (20) proves (1). All comparisons were uniform
finite inequalities before normalization; no mesh-dependent parameter
was inserted into a fixed-cutoff or fixed-mass limit.

### 5. Scope and checks

The load-bearing new estimate is (5), obtained from the exact residual
on its compact row, followed by the full prefix bound (11). The
two-term product telescoping (13) preserves the original order.
The shell counts (14)--(15) retain every axial and transverse source;
the action collar and all missing infinite endpoints are estimated
before their removal. Both Q forms enter (10); L167's other subtraction
terms and upper exterior enter (2) once. The new rate uses L168's exact
coefficient identity, including its actual half-line half-weight.

Verification here is analytic: the finite stencil product rule, error
powers in (8)--(11), complete shell sums, raw endpoint normalization,
and heat-weighted quadrature. No numerical extrapolation, synthetic
fixture or finite spectrum can establish (20), and no mathematical
script is required. A separate critical audit should particularly
check (5)'s component/adjoint placements and the boundary accounting
around (13)--(16). The argument does not resolve any independent
interacting or construction requirement.

### 6. Separate critical audit, 2026-10-22

This audit accepts (1) relative to the stated imported hypotheses. It
checks the new uniform comparison, original trace placements, endpoints
and normalization, rather than inferring a rate from L168's limit.
No change to the exponent, coefficient or direct mathematical inputs
is needed. Upstream analytic and separate-audit qualifications remain;
no numerical sign premise is used. This is verification of an existing
local result, not a new result beyond the assessed sources.

**Exact order and the two residual orientations.** L167(7) expands the
original negative trace as T+U+V-W, with
T=Tr[B_h G_v D^T B_ell F A]. Its full upper-exterior estimate is
O(N log(eN)), and U,V,W cost respectively O(N^2), O(N), O(N^-2).
Thus (2)'s positive sign and O(N^2) allowance include those removals
once. At a surviving observation e, both endpoints of B_h are interior
and both indices of A are within the fixed compact enlargement.
Symmetry gives (Sigma A)_(z,e)=(A Sigma)_(e,z), not A Sigma=Sigma A.
For the frozen symmetric A^0 the same transposition gives g A^0.
It therefore suffices to compare a A Sigma at this compact row.

In ordinary coordinates L=D_1^T D_1 and
Kbar=a K_a=E_a M_a C_a D_1, by L018(1)--(2) and L028's explicit
composition. Every component of L is a sum of two first differences
between its own staggered grids. Writing Kbar as finitely many
coefficient/shift terms, transposition changes shifts and evaluation
points but not the bounds in (6). In particular it retains derivatives
of u_a; it does not freeze a coefficient at z. On any scalar entry the
twice-applied exact product rule for Delta_alpha Delta_beta(k h)
has only these three types: a shifted k times two differences of h,
one difference of k times one of h, and two differences of k times h.
This holds also for different alpha,beta and either incidence sign.

For h=Sigma-g, the three error sizes are respectively
N^-4, a N^-3 and a^2 N^-2. They are all O(N^-4) since aN=8.
For h=g and coefficient k-k^0 the sizes are
a R^-4, a R^-3 and a^2 R^-2. Each cross-component term of
L Kbar uses the appropriate diagonal component of Sigma; the
estimate never differences two different component Green kernels.
For Kbar^T L Sigma, the exact identity L Sigma=P is used first.
Its difference from (Kbar^0)^T P_inf splits as
Kbar^T(P-P_inf)+(Kbar^T-(Kbar^0)^T)P_inf, bounded by
C N^-4+C a R^-4. The local identity part of P_inf is covered
at bounded R. There is no coefficient/projection commutation.
Finally Q_j=D_1^T W_j D_1 has bounded local W_j for each j=3,6;
retaining its right incidence gives a(R^-3+N^-3). The shear's
two clovers and the triplet's average of products remain in W_j.
These checks establish (5) for both orientations and both subtractions.

**Uniform component and adjoint boundary comparison.** The error
estimates used in that product rule follow from the actual proofs of
L164(5)--(6), L165(7)--(8) and L166(7), rather than from their
magnitude bounds alone. For component Sigma, the observation has
fixed clearance, while every source remains allowed. The one-Neumann,
three-Dirichlet image formula puts each nonidentity image at distance
at least cN after the finite reflection choices. Observation differences
through order j=2 retain their order in each image. The integrated
image bound up to N^2 and both subsequent heat tails are
O(N^(-2-j)). In the finite long-time bound each observation difference
contributes |q|/N; constant own-direction modes are retained, with
zero difference in a constant coordinate. Mixed components of Sigma
vanish identically.

For P, use I-D G_v D^T. Its error has one observation and one source
Dirichlet difference, hence O(N^-4), including different directions.
At a normal end source the head-minus-tail formula includes the pinned
zero vertex: odd image cancellation there is exact, and both reflected
differences retain their signs before the bound. The identity terms
cancel. The same argument with only the source difference gives
J_N-J_inf=O(N^-3). These arguments retain all normal end rows; they
do not assign Dirichlet conditions to a normal component of Sigma.

**Full prefix and endpoint accounting.** At every interior w the
finite prefix sums component-1 links below w and has at most N terms.
With b=1+|w_T-e_T|, summing the three errors in (5) gives respectively
C a b^-2, C a^2 b^-1 and C N^-3. The omitted half-line below the
lower root has distance at least cN from e, uniformly even when w
is near either axial end, and its frozen fourth-power tail is
C sum_(n>=cN)n^-4=O(N^-3). This proves (11) without replacing the
prefix by a full line. It also keeps the last interior prefix input;
the separately pinned row w_1=N is not compared by (11).

The two products in (13) have distinct complete row counts. The first
is at most C N^-3 N sum_(m<=CN)(1+m)^-1, or
O(N^-2 log(eN)). For the second, the transverse shell count is
C(1+m)^2 and the axial sum of r^-3 is C(1+m)^-2. The three
prefix errors therefore contribute

    C a sum_(m<=CN)(1+m)^-2,
    C a^2 sum_(m<=CN)(1+m)^-1,
    C N^-3 sum_(m<=CN)1,

namely O(a), O(a^2 log(eN)) and O(N^-2). This confirms (14).
For the joint first moment, summing r^-2 along the axial line gives
C(1+m)^-1; after the remaining b^-3 and shell count the sum is
C sum_m(1+m)^-2<infinity. For the tail, transverse distances
above R/2 cost O(R^-2); below R/2 the required axial distance cR
costs R^-2 times the transverse logarithm. Thus all three assertions
in (15) hold, including coincident and bounded-offset entries.

A boundary-touching f lies at distance cN from e. For its original
product the decaying bound in (4) has row cost O(N^-2 log(eN)),
and its constant part has the same bound even over the entire box.
Pinned endpoint w has F row zero; the other endpoint and every
normal end link still enter that estimate. Fixed tangential links
absent from the finite space and all links outside the cube enter
only the restored infinite tail, with that same cost. This handles
lower/upper axial vertices and transverse faces, edges and corners.
No formula for a nonzero prefix at a pinned vertex is required.
The distinct upper axial exterior was already counted in (2).

**Exterior, component quadrature and full normalization.** L164(3)
supplies a global bulk same-component difference bound, not a bound
across a fixed tangential link or the upper pin. It compares ell_b(f)/a
with a nearby same-component reference at e at cost C a p(l)r.
Only that reference and h(e)/a use L248(6)--(8)'s compact raw-link
matching. Values of different components are never subtracted.
Equation (15)'s first moment then bounds (16)'s row error by
C a p(k)p(l). B uses endpoint sums, so both endpoint slots retain
their factors 2 and their original incidence placements.

For each transverse observation component nu, its stationary kernel
sum is absolutely convergent, linear in u(x), and bilinear in the
two smooth V fields. Thus its own C^1 norm is polynomially bounded
in k,l and it is compactly supported. The midpoint-cell error is
O(a p(k)p(l)) separately on each staggered component grid; only
after integrating those densities is their sum (17) used. A derivative
of a rough Green column or equality of shifted component grids is
unnecessary. L168(13)--(18)'s endpoint factors, residual half,
actual-prefix half and color sum give (3/2)g_G u_1 V_k dot V_l.
This is exactly L145(1)--(2)'s B_(i,R), with the positive bulk sign
already fixed and no outside factor 3.

The unnormalized row prefactor is a*a/a=a. Multiplication by a^3
therefore makes a^4 times each row error; there are O(N^4) rows.
An O(a) normalized row error gives O(a) cubic-normalized response
error, and the collar's O(N^-2 log(eN)) is smaller. L248(10)--(11)
applies to precisely the same covariance-normalized heat matrices as
L156(8). Their separate value and error envelopes retain the triplet's
four products, both shear polarizations and all allowed constant modes.
Every polynomial above is summable against their Gaussian envelope.
Omitted continuum labels have size at least order N and an exponentially
small polynomially weighted tail. Finally the O(N^2) removal in (2)
also becomes O(N^-1) after multiplication by a^3. Hence (20) follows,
and multiplying by a^-3=N^3/512 gives (1).

No first unsupported estimate was found in this specialization. The
audited result supplies only the fourth-trace remainder; it neither
accepts an upstream unaudited proof nor establishes a complete response
rate, an interacting reflected bound or a Yang--Mills construction.

## Mathlib

Full matching result and supporting relative discrete-kernel coverage:
**not checked**. Unknown is not absence. Reuse the prior approved
[quantitative assessment](../drafts/literature/2026-10-21-fourth-ee-trace-quantitative-remainder.md).
No new external theorem is imported or reproved. L164--L167 already
provide the differentiated heat/image estimates with their exact
relative boundary cases; the new specialization quantifies the
coefficient difference and sums it in this trace's original prefix
order. L248 supplies quantitative raw/heat bounds, not its different
reverse-trace conclusion. L168 supplies the established stationary
coefficient, not a modulus for its earlier limiting argument.
