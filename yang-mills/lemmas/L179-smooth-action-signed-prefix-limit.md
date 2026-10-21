# L179 — Signed smooth-action prefix limit with both axial profiles retained

## Hypotheses

Keep L178's exact hypotheses and ordinary stored-coordinate convention:
SU(2), the all-face relative box D=(-4,4)^4, a=8/N through admitted
even meshes, the straight direction-1 lower-rooted forest, the full
compact L008 displacement u and both actual L010 probes i=3,6 at
tau=1/16. Take the bare expansion at fixed mesh before refinement.
Keep L175's symmetric A^gen, signed J_j, endpoint-sum S, action
multiplier m_(j,l), exterior column h_k and coefficient c_(i;kl).
Use exactly L178(2)'s W_i[Q_1,Q_2], with M_st=min(s,t) and
P_(t,r)=1_(0<=r<t). All action faces, pinned links, axial end modes
and exterior heat modes remain.

Use L080's continuum relative modes f_k, lambda_k and A_k=f_k/sqrt(lambda_k).
Define the physical functions, on interior points x=(xi,y),

    H_(k,1)=0,
    H_(k,mu)(xi,y)=A_(k,mu)(xi,y)
             -partial_mu integral_(-4)^xi A_(k,1)(z,y) dz, mu=2,3,4,
    q_l=d^*d A_l,
    c_(i;kl)^cont=exp(-tau(lambda_k+lambda_l)) (B_i)_(kl).  (1)

Here d^*d is the continuum relative action operator on these smooth
modes; q_l has its componentwise trigonometric extension to the faces.
H_k is used only on the compact generator support, and is not assigned
the separately pinned upper forest value. The constant axial cosine
mode is included in the integral in (1).

The following unit-grid definitions specify a finite-stencil density
without phase or endpoint conventions left implicit. Index positive
links of Z^4 by their integer initial vertex and component; use the
ordinary link-to-plaquette incidence D_infty,
L_infty=D_infty^T D_infty on links,
four-plaquette-to-vertex clover average C_infty, vertex-to-link
endpoint average E_infty, and endpoint sum S_infty, with exactly
L028's oriented compositions. For constant b in R^4 put

    (M_b F)_nu=sum_rho b_rho F_(rho nu),
    K_infty(b)=E_infty M_b C_infty D_infty,
    Gamma(b)=[L_infty K_infty(b)+K_infty(b)^T L_infty]/2. (2)

These are unit-spacing stencils: D_infty has no factor 1/a.
There is no color extension in (2). In particular Gamma includes
both actual generator orders and all unequal endpoint/clover filters.

Let T_infty be adjacency on Z^3 and, for 0<epsilon<=1, define

    Q_d=(6+epsilon)^(-1) sum_(n=0)^d
                               [T_infty/(6+epsilon)]^n,
    G_epsilon=(6+epsilon)^(-1) sum_(n=0)^infinity
                               [T_infty/(6+epsilon)]^n.       (3)

For j,mu=2,3,4, or for j=2,3,4 and mu=1, define

    T_(j,mu)[Q,b]=sum_(Y,Z,U in Z^3) Q_(0,Y)(J_j)_(Y,Z)Q_(Z,U)
           sum_(r in Z, f a positive mu-link of Z^4)
                   Gamma(b)_((r,U,1),f) (S_infty)_(f,(0,0)). (4)

In (4), J_j has +1 on forward and -1 on backward transverse
neighbors, as in L175. The closing vertex is (0,0) in Z x Z^3;
(r,U,1) means a component-1 link with initial vertex (r,U).
The S factor permits just the two mu-links incident to that vertex.
Gamma then permits only finitely many r,U. Thus (4) is a finite sum
for Q_d and an absolutely convergent sum for G_epsilon, as proved
below. This definition fixes the order Q J Q Gamma S; neither path
filter is replaced by a centered substitute.

## Conclusion

At every fixed epsilon and degree d, the signed limit exists and equals

    lim_(N->infinity) a^3 W_i[Q_(d,N),Q_(d,N)] = K_(i;epsilon,d),
    K_(i;epsilon,d)=-6 sum_(k,l) c_(i;kl)^cont
      integral_((-4,4)^3) integral_(-4)^4 integral_(xi)^4
        (xi+4) sum_(j=2)^4 sum_(mu=1)^4
        q_(l,j)(eta,y) H_(k,mu)(xi,y)
        T_(j,mu)[Q_d,u(xi,y)] d eta d xi d y.          (5)

All sums over k,l are over the complete relative spectrum. They are
absolutely convergent. The separate levels eta and xi in (5) are
essential: the upper cumulative action integral has not been frozen
at the generator level. The component-1 term is zero by (1), rather
than by dropping an original component row.

Replacing Q_d by G_epsilon in (5) gives a real, absolutely convergent
fixed-mass functional K_(i;epsilon), with

    lim a^3 W_i^(epsilon,epsilon)=K_(i;epsilon),
    |K_(i;epsilon)-K_(i;epsilon,d)|
                       <=C_i epsilon^(-2)[6/(6+epsilon)]^(d+1).
                                                               (6)

There is a finite real coefficient K_(i,Vmix), defined by the controlled
mass limit, such that

    K_(i,Vmix)=lim_(epsilon down to 0) K_(i;epsilon),
    |K_(i,Vmix)-K_(i;epsilon)|<=C_i epsilon^(1/4),
    lim_(N->infinity) a^3 V_i=K_(i,Vmix).                (7)

The name Vmix distinguishes this smooth-action mixed branch from
L120's displacement-placement coefficient K_(i,V). No expression
obtained by simply setting epsilon=0 in (5) is asserted here.

Together with L159's finite assembly, L172's E,E limit and L174's
action-Hessian coefficient, the complete cubic residual/action response
has a finite cubic limit

    lim a^3[-kappa_0(f_(i,0),r_1,S_3)]
                   =K_(i,T)+K_(i,Vmix)-6K_(i,R).        (8)

Its value and whether it vanishes for either actual probe remain
unresolved. Formula (8) carries no additional outside factor three.
This is local standard-method REPRODUCTION, not a novelty claim or
a solution of any continuum/interacting requirement.

## Proof

### 1. Actual coefficient convergence and the complete frozen stencil

Fix a pair of exterior mode labels k,l for now. L080's exact ordinary
normalization gives v_(k,a)=a A_(k,a), where
A_(k,a)=f_k/sqrt(lambda_(k,a)), sampled on its staggered link grid.
Its physical eigenvalues converge to lambda_k. On every compact
interior set, the unaveraged forest column satisfies

    a^(-1) h_(k,a,mu) -> H_(k,mu),
    a^(-3) m_(j,l,a) -> q_(l,j),
    c_(i;kl,a) -> c_(i;kl)^cont.                         (9)

The second convergence is uniform up to the axial faces for the
componentwise smooth extension. To justify each specialization:
for mu>1 the exact forest retraction gives
h_mu/a=A_(k,a,mu) at its link center minus the forward transverse
difference divided by a of

    phi_(k,a)(s,y)=a sum_(r=0)^(s-1)
                              A_(k,a,1)(-4+(r+1/2)a,y).

L080(8)-(10) gives uniform convergence of this expression and all
fixed transverse derivatives to the physical lower integral. The
integral difference formula for the forward difference proves the
first convergence in (9) at each unaveraged link center, including
every bounded stencil shift. The component-1 retracted column is
exactly zero on interior forest links. Compact generator support
excludes the upper normal jump; no extension across that jump is used.

For the second convergence, L159(6) and L156(10) give exactly
L h_l=L v_l=a^3 d_a^*d_a A_(l,a). Each discrete derivative of the
relative product modes interchanges the appropriate sine/cosine
factor with coefficient 2 sin(pi l_j/(2N))/a. These coefficients
converge to pi l_j/8, including zero when l_j=0. The resulting
finite trigonometric sum converges uniformly, with every fixed
derivative, to d^*d A_l on the whole box. Evaluation at vertices
instead of link centers changes a fixed smooth mode by O(a).
Normal end-edge derivatives obey the same relative-mode formula;
the global action extension is not the upper forest lift.
The last convergence in (9) is L080(4)-(6), with the actual
triplet average of squares and shear form retained.

For a closing vertex x=(s,X), write its physical location
x_a=(-4+sa,-4+aX). L028's exact compositions in stored coordinates
give, for each bounded local offset e,f from x,

    a (A^gen)_ef = Gamma(u(x_a))_(e-x,f-x)+O(a).         (10)

The error is uniform over all closing vertices and over the finite
stencil entries. Indeed a K_a=E M_(u_a) C D_1, with unscaled
incidence D_1; hence a A^gen is exactly the two products in (2)
with the actual variable coefficient at its intermediate vertices.
Every such vertex differs from x_a by a fixed bounded multiple
of a. L028 gives u_a-u=O(a^2) and bounded physical first derivatives.
Replace each sampled coefficient by u(x_a) only in this finite
product. The error per entry is O(a), including the reversed adjoint
and its coefficient differences. All stencil maps otherwise agree
exactly with the oriented unit-grid maps in (2). This is a local
entry comparison, not a commutation of u with any covariance.
Outside a common compact interior enlargement both actual generator
and frozen nonzero coefficients are zero; (10) still holds there.

### 2. Finite degree localizes only the transverse factors

Hold epsilon,d fixed. In the expansion L178(6), the closing endpoint
S_fx and generator entry force r-s and all generator/closing
transverse offsets into a fixed set. Each Q_(d,N) has range at most
d, and J_j range one. Thus Y,Z,U differ from X by bounded offsets
depending on d. The compact generator support places every one of
these transverse vertices a fixed physical distance from the boundary
when N is sufficiently large. Every path of length <=d contributing
to a polynomial entry also lies in the transverse interior.
Consequently the two finite killed-adjacency polynomial entries agree
*exactly* with the corresponding entries of Q_d in (3), at all
nonzero trace summands. This does not replace a boundary inverse
by an infinite-grid inverse: it is a fixed-degree polynomial identity
on already supported rows. The diagonal remains six, including the
Dirichlet end-edge convention.

No axial degree or axial range restriction is introduced for M or P.
In particular t still ranges through every interior axial level,
while only the generator's component-1 row r is within a fixed
integer distance R' of s.

### 3. Moving-cut estimate and five-dimensional signed Riemann limit

For each finite stencil term, multiply the original ordered expansion
by a^3 and use the exact rescalings

    m=a^3 (m/a^3),  h=a(h/a),  A^gen=a^(-1)(a A^gen),
    a M_st=min(sa,ta).

The remaining cell factor is a^5. Its weight is
min(sa,ta) 1_(t>r), with r=s+v and |v|<=R'. None of these
rescalings changes which level carries which multiplier.

Replace only 1_(t>s+v) by 1_(t>s). Its difference is supported
on |t-s|<=R'+1. There are O(N) choices of s, O(1) of t in this
strip and O(N^3) of X, so there are O(N^4) closing/level points.
The rescaled coefficients are bounded for a fixed k,l, the finite
number of stencil terms depends only on d, and min(sa,ta)<=8.
The complete scaled strip contribution is therefore
C_(epsilon,d,k,l) a^5 N^4=O(a). This proves that the moving
prefix cut has zero cubic-scale error; no half-weight is assigned
to a strip whose normalized measure tends to zero.

On the retained domain t>s, min(sa,ta)=sa=x_(a,1)+4 exactly.
Apply (9)-(10) and the uniform continuity of fixed smooth modes
to each finite transverse/link offset. Keep m/a^3 at
eta=-4+ta and h/a and u at xi=-4+sa. The coefficient replacement
error is o(1) per normalized integrand, uniformly in s,t,X.
There are O(N^5) such points, and a^5 N^5 is bounded, so the
total error tends to zero. The link/vertex center offsets tend to
zero, while their incidence and endpoint signs remain the exact
finite factors in (4). The sum of these factors is precisely
T_(j,mu)[Q_d,u(xi,y)].

We have now obtained the right-hand side of (5) as a Riemann sum
on three transverse coordinates and two independent axial coordinates.
For a fixed pair its integrand is continuous on the box and bounded,
except for the indicator eta>xi. That indicator's discontinuity
lies on a hyperplane of zero five-dimensional volume. To verify
convergence directly, remove a strip |eta-xi|<=delta: its bounded
integral is O(delta), and its normalized grid count is O(delta+a).
On each of the two remaining closed regions use uniform continuity
and ordinary rectangular Riemann sums. Let a go to zero first and
then delta go to zero. The compact generator support also makes
extension by zero across the xi and transverse faces continuous.
Axial action rows t adjacent to either face have bounded coefficients
and normalized measure O(a); they have been retained until this limit,
not discarded by an unproved smooth upper forest extension.
This establishes (5) for the fixed pair, including the -6 once.

### 4. Full heat sums and polynomial removal at fixed mass

All fixed-mode estimates above admit bounds polynomial in k,l,
with a fixed enlargement of the polynomial p. L156(8) gives a
summable, mesh-uniform Gaussian majorant for
|c_(i;kl,a)|p(k)p(l); L080's normalization gives the same majorant
for the continuum coefficients. L178(3) bounds each scaled
polynomial trace by C p(k)p(l) epsilon^(-2). The density in (5)
has the same bound: endpoint/generator incidence is finite, its
entries are bounded by C|u|, and the absolute row sums of Q_d
are at most epsilon^(-1). The physical box and triangular axial
domain have bounded volume. Thus the full exterior tail tends to
zero uniformly in N; taking a finite exterior cutoff first and
then removing it proves the absolutely convergent heat series (5).
Neither an actual probe sector nor a constant axial mode is omitted.

On Z^3, every adjacency row sums to six, so the nonnegative series
in (3) converges in absolute row/column sum norm, with

    ||G_epsilon||_abs<=epsilon^(-1),
    ||Q_d||_abs<=epsilon^(-1),
    ||G_epsilon-Q_d||_abs
                       <=epsilon^(-1)[6/(6+epsilon)]^(d+1). (11)

These follow by summing the geometric walk coefficients; a finite
partial sum has remainder bounded by the scalar geometric tail.
In (4), finite Gamma S bounds the two-kernel product by a constant
times the product of these absolute row/column sums. Telescoping
the two Q factors, in their existing positions around J_j, bounds
the density difference by C |u| epsilon^(-2)rho^(d+1),
rho=6/(6+epsilon). Integrate and use the heat majorant to obtain
absolute convergence of the fixed-mass version of (5) and the
second bound in (6). This elementary Neumann specialization is
needed to identify the limiting density, not to reprove an external
flow/Ward theorem.

Every finite-degree mesh limit is now established. Apply L178's
conditional transfer, whose premise was (5), with its independent
uniform finite-box error. First take N to infinity at fixed degree
and mass, then d to infinity at that same mass. The resulting
massive trace limit equals the fixed-mass functional just constructed.
This proves the first statement of (6). No degree depending on N
has been selected and neither long axial profile has been localized.

### 5. Mass removal and assembly without assigning a coefficient value

Let v_N=a^3 V_i and K_epsilon=K_(i;epsilon). L177(5) gives

    limsup_N |v_N-a^3 W_i^(epsilon,epsilon)|
                                            <=C_i epsilon^(1/4).

Since the massive sequence has the limit proved in (6), it follows
that limsup_N |v_N-K_epsilon|<=C_i epsilon^(1/4).
For any two fixed positive masses, the triangle inequality before
the mesh limsup therefore gives

    |K_epsilon-K_delta|
                           <=C_i(epsilon^(1/4)+delta^(1/4)). (12)

This is the Cauchy criterion as both masses tend to zero, so the
finite real limit K_(i,Vmix) exists. Let delta tend to zero in
(12) to get its error bound in (7). For any fixed epsilon,

    limsup_N |v_N-K_(i,Vmix)|<=2 C_i epsilon^(1/4).

Now let epsilon decrease to zero to prove the last limit in (7).
This order uses the mesh limsup first; no mesh-dependent mass,
uniform polynomial degree at zero mass, or interchange of a
singular torus integral with mass removal is assumed.

Finally L159(3)'s exact-response assembly is
H_i=T_i+V_i+H_i^EE+O_i(N). L174 imports the established limit
of T_i as K_(i,T), and L172(3) gives a^3 H_i^EE->-6K_(i,R).
Our (7) supplies the missing V_i limit. Since a^3 O(N) tends to
zero, this proves (8). The finite algebraic assembly already
contains all color and pairing factors; the -6 in (5) is retained
once and no new factor three is introduced. The numerical signs
quoted for other coefficients are not needed for this existence
proof and do not give a sign or value for K_(i,Vmix).

The meaningful checks in this attempt are the full entry comparison
(10), the actual moving-cut count O(a^5 N^4), the five-coordinate
normalization a^5 N^5, the two independent coefficient levels in
(5), and the uniform mesh/degree/mass transfers (6),(12). They are
analytic; no numerical script or upstream heat-arithmetic audit is
claimed. The target's vanishing question now reduces to evaluating
whether K_(i,Vmix)=6K_(i,R)-K_(i,T), for each actual probe. Other
response jets, complete compensation, finer powers/logarithm, finite
matching, reflected error <=c_box/2 and the continuum/infrared mass
requirements remain independent unresolved gaps. No candidate exists.

### 6. Separate critical audit of the coefficient identification

The 2026-10-21 audit accepts (5)--(7) relative to the stated inputs,
in particular L177(5)'s uniform comparison. No correction is needed.
L178's separate section-5 audit checks its independent approximation
bound. Neither acceptance audits L175--L177 upstream or asserts a
quantitative rate for the present successive-limit proof. The assembly
(8) retains its stated imported premises.

**Actual modes and ordered stencil.** L156(8) and L080(4)--(6)
use the same stored square-root covariance columns a A_(k,a) and
heat coefficients as here. L080(8)--(10) retain the constant axial
mode and the exact midpoint lower prefix. For an unaveraged transverse
link the forward difference of that prefix, evaluated at the link
center, converges to its transverse derivative; this checks (9)
without replacing raw links by L080's endpoint-averaged diagnostic.
The component-1 forest column is exactly zero on the compact generator
input. The separate upper pin is never substituted into H. The action
extension instead uses L h_l=L v_l, including its normal end rows.
Its unscaled two differences give precisely a^3 q_l. L028's actual
endpoint/clover compositions and their adjoints give (10) after
multiplication by a, with both Gamma orders and every S slot intact.

**Finite-degree locality and normalization.** At fixed epsilon,d,
compact generator support and the two transverse ranges d place every
polynomial path in the interior for sufficiently large N. Only these
paths become infinite-grid polynomial entries; neither M nor P is
localized. Expanding the trace leaves one closing transverse coordinate
X, the two independent axial levels s,t, and finitely many offsets.
The scaled coefficient product is

    a^3 [a^3 q_l] [a^(-1) Gamma] [a H_k]
                     [a^(-1) min(sa,ta)] = a^5 q_l Gamma H_k min(sa,ta).

Thus there is exactly a five-dimensional cell weight, with no extra
axial sum, color multiplicity or orientation factor. For r=s+v the
changed cut has only O(N^4) points at fixed degree, so its scaled
error is O(a). On t>s, min(sa,ta)=sa=xi+4. The action remains at
eta=-4+ta and the generator/exterior at xi=-4+sa. Bounded fixed-mode
entry errors over O(N^5) cells vanish; the diagonal and axial face
strips have vanishing normalized measure. Their rows were included
before taking this limit. The finite offset sum is exactly (4),
which still has both generator orders and the sole -6 of (5).

**Both complete probes and degree removal.** L156(8), with
lambda_(k,a)>=|k|^2/16 and uniformly bounded whitened probe forms,
dominates the polynomial mode factors by a mesh-independent Gaussian
series. Each fixed continuum label is eventually a mesh label; extend
finite label sums by zero to apply this domination to omitted labels
as well. L080 gives the corresponding continuum coefficient bound.
The row-sum estimates bound the full finite trace and the density by
C p(k)p(l)epsilon^(-2), independently of degree. Consequently a finite
exterior cutoff can be removed uniformly after the pairwise limit.
The argument includes both triplet and shear polarizations and allowed
zero component indices, rather than transferring a selected diagnostic
sector. The infinite-grid Neumann tail has the same absolute norm
bound as the finite tail. Telescoping its two original positions in
(4) proves the density error in (6). L178's now-established conditional
transfer identifies its degree limit with this same density, at each
fixed positive mass.

**Subsequent mass limit and its exact name.** Write
w_N^epsilon=a^3 W_i^(epsilon,epsilon). Its just-proved limit is
K_epsilon. For any two fixed masses L177(5) bounds
|K_epsilon-K_delta| by C_i(epsilon^(1/4)+delta^(1/4)) after the
mesh limsup. This proves a finite Cauchy limit, its error in (7),
and then convergence of a^3 V_i by sending epsilon to zero after
the mesh limsup. No mass-dependent degree is inserted into a mesh
limit. In particular this proof does not evaluate a zero-mass torus
density. L256's subcubic comparison then gives the same qualitative
limit for U_i^0(F^0); L257/L258 preserve it, and the independently
quantified L259 density is identified by uniqueness of that limit.
This downstream use introduces no circular input to (5)--(7).

The audit therefore accepts the coefficient identification required by
the static rate, conditional on L177(5) and its upstream premises.
It does not assert vanishing of this coefficient, isolated-response
compensation, a complete L011 remainder, an interacting reflected
bound, continuum axioms or finite positive infrared mass. Mathlib
coverage remains as qualified below; no new external theorem or
mathematical script is needed for this audit.

## Mathlib

Full matching result: **not checked**. Supporting Riemann integrability
off a measure-zero hyperplane, dominated convergence, finite Neumann
series and the Cauchy criterion: **not checked**. Unknown coverage is
not absence. Reuse the unchanged
[assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No new external theorem is imported. The elementary specialization
above is necessary because a generic local trace limit does not
retain two different long axial profiles and the action coefficient
at its separate level.
