# L262 — Quantitative remainder for the third ordered E,E trace

## Hypotheses

Keep exactly L165/L170's relative SU(2) cube D=(-4,4)^4,
sufficiently fine admitted even N, a=8/N, tau=1/16, straight
direction-1 lower-rooted forest, ordinary stored coordinates and
bare-first expansion. Z_i is precisely L165(1), with its sole -6,
for both actual probes i=3,6. Retain full tensors before forest
restriction, both residual insertion subtractions, every source/end
row, the upper jump, allowed constant modes and complete heat sums.

Import L164(2)--(3)'s complete local residual decomposition and smooth
bulk exterior extension; L165's ordered bulk reduction and all-source
kernel magnitudes; L260(7)'s compact-observation relative Green and
projection comparisons; and L248(3)--(11)'s normalized raw exterior
and full heat estimates. These inputs retain their upstream analytic
and pending-audit qualifications. No numerical sign premise is used.
L170 defines the complete frozen tensor and coefficient; L171/L172
identify that coefficient with exactly -(9/2)K_(i,R), with K_(i,R)
as in L145. No new tensor contraction or torus evaluation is assumed.

## Conclusion

There are mesh-independent constants such that

    |Z_i+(9/2)a^(-3)K_(i,R)| <= C_i N^2 log(eN), i=3,6.    (1)

This is stronger than the requested N^(5/2)log(eN)^2 component
budget. The separate critical audit in proof section 6 accepts this
specialization relative to its stated imports; it does not audit those
upstream inputs.
It is local REPRODUCTION under the approved SPECIALIZE assessment,
without a claim of originality beyond the sources checked. Quantitative
full-response assembly, independent upstream audits, interacting
reflected control, continuum axioms and finite positive infrared mass
remain unresolved. No Yang--Mills candidate solution is supplied.

## Proof

### 1. Exact order, compact indices and joint moments

L165(3), counting the complete upper exterior and smooth-action
subtraction once, gives

    Z_i=-6 sum_(k,l,c)c_(i;kl,a)
                  Tr[Phat B_(ell_b t_c) Fhat M]
                    +O_i(N^2 sqrt(log(eN))).              (2)

Here P=Sigma L is the full four-dimensional co-closed projection,
F=Phi Sigma, ell_b is the bulk part of h_l, and
M=T_R(h_k t_c,.,.). The notation in (2) writes ell_b as a one-color
column, so t_c is inserted just once. The B map is an endpoint sum
with color bracket, not an endpoint average. For a fixed heat pair,
write polynomial mode bounds as p(k)p(l), enlarging the fixed
polynomial when needed. L156(8) sums every such polynomial.

Each entry contribution in the retained trace has the order

    P_(e,f) (B_(ell_b t_c))_(f,v) F_(v,e') M_(e',e).       (3)

The residual indices e,e' are in a fixed compact interior set S
and a bounded distance apart. There are O(N^4) residual placements,
with bounded local, endpoint, component and color multiplicities.
Keep individual local force/vector and insertion stencils if multiple
summands contribute to one matrix entry. The link f and its vertex
endpoint v can range over the cube; no covariance input is restricted.
F has zero columns except for component-1 e'.

Let g be the infinite unscaled four-dimensional scalar Green kernel,
copied diagonally to link components and colors, and put

    P^0=I-D^0 g(D^0)^T,
    F^-(v,e')=sum_(j>=0) g_((1,v_1-j-1/2,v_T),e').       (4)

The staggering and upper endpoint of this half-line are exactly
L170(5)'s. Put r=1+dist(e,f), b=1+|e_T-f_T|, absorbing all fixed
stencil/endpoint shifts into constants. L165(6),(9) and their infinite
versions give, for interior v,

    |P_(e,f)|<=C(r^-4+N^-4), |P^0_(e,f)|<=C r^-4,
    |F_(v,e')|+|F^-(v,e')|<=C b^-1.                    (5)

For boundary v the finite prefix row is zero by its definition.
The normalized exterior ell_b/a is globally bounded by C p(l)
on all variable links. The residual entries are bounded by C p(k).

The joint majorant q(n,z)=(1+sqrt(n^2+|z|^2))^-4/(1+|z|)
has the same scalar counts as L261(6)--(7): for R>=2,

    sum q<=C, sum_(sqrt(n^2+|z|^2)>R) q<=C/R,
    sum_(sqrt(n^2+|z|^2)<=R)
                    (1+sqrt(n^2+|z|^2))q<=C log(eR),
    N^-4 sum_(finite f) b^-1<=C/N.                     (6)

These counts apply to (3) because e' differs from e by a bounded
stencil displacement. Explicitly, a transverse shell m has O((1+m)^2)
points and the axial sum of (1+sqrt(n^2+m^2))^-j is at most
C_j(1+m)^(1-j), j>1. The zeroth and truncated first moments
leave respectively sum_m C(1+m)^-2 and sum_(m<=R) C(1+m)^-1.
For the tail split at |z|=R/2: the outer transverse part is O(1/R);
the inner part has |n|>cR, whose fourth-power sum is O(R^-3),
times sum_(|z|<=R/2)(1+|z|)^-1=O(R^2). Finally the finite
axial count is O(N), and the transverse inverse-distance sum O(N^2),
which proves the last line. No absolute first moment of either
separate kernel, or operator bound for F, is asserted.

### 2. Uniform prefix comparison with compact source and remote endpoint

For each compact source e' of component 1 and EVERY actual input
link z below an interior vertex v, component symmetry and L260(7)
with j=0 give

    |Sigma_(z,e')-g_(z-e')|<=C_S N^-2.                  (7)

The compact observation is e', not v or z. L164 section 2's image
proof, restated in L260(7), is uniform in its other index, including
the first and last normal links. On component 1 it uses the axial
edge-Neumann and three transverse vertex-Dirichlet kernels, retaining
the constant axial mode. It is not a scalar killed-kernel statement
for every link component.

There are at most N actual prefix inputs, so their total comparison
error is at most C/N. In integer axial coordinates the finite prefix
uses t=0,...,s-1 when v has interior level s. The infinite half-line
in (4) adds exactly t<0, keeping the identical last link s-1/2.
Since e' has clearance delta N from the lower face, all these missing
inputs have axial distance at least delta N from e'. Thus, uniformly
in the endpoint's transverse coordinate and in s,

    sum_(t<0)|g_((1,t+1/2,v_T),e')|
                 <=C sum_(j>=delta N) j^-2<=C/N.

Consequently the whole prefix satisfies

    |F_(v,e')-F^-(v,e')|<=C/N                          (8)

for every interior v. If e' is not component 1, both sides vanish.
Neither a finite axial cutoff nor a compact endpoint assumption is
used. Boundary vertex rows, where the finite prefix is separately
pinned to zero, are NOT compared by (8).

For compact e the other relevant comparison is exactly

    |P_(e,f)-P^0_(e,f)|<=C_S N^-4                     (9)

from L260(7), on every variable f. This uses two Dirichlet vertex
differences in I-D G_v D^T, including mixed observation/source
directions and normal end edges. The identity parts cancel. This
projection geometry differs from the component geometry in (7).

Choose fixed eta>0 small enough that r<=eta N places f, both of
its endpoints and every bounded stencil shift in one compact interior
set, uniformly for e in S. On this near set use the exact ordered
two-term entry identity

    P F-P^0 F^-=(P-P^0)F+P^0(F-F^-).                  (10)

The endpoint and residual indices in each product remain those of
(3). From (5),(8),(9),

    sum_near |(P-P^0)F|<=C N^-4 N N^2<=C/N,
    sum_near |P^0(F-F^-)|
                   <=C N^-1 sum_(r<=CN) r^-4
                   <=C log(eN)/N.                     (11)

The last shell sum is four-dimensional: r^3 sites times r^-4.
The first term uses the actual F, so (10) has no omitted product
of two errors. Equation (8) is the newly checked placement; neither
L260's prefixed-residual rate nor L261's compact-endpoint prefix
comparison has been transferred to this trace.

### 3. Every far row and deterministic coefficient placement

For r>eta N, keep the actual coefficients bounded and use (5)--(6).
The complete finite far product and the omitted infinite frozen
product are each bounded by C/N per normalized residual placement:

    sum_far |P F|<=C/N,  sum_far |P^0 F^-|<=C/N.         (12)

For a boundary endpoint in the finite trace the corresponding F row
is zero and satisfies the same magnitude bound. Every boundary-touching
endpoint stencil is distance at least c_S N from e. Thus (12)
accounts for both physical axial ends, all transverse faces, normal
end links, fixed-link omissions, corners, all infinite rows outside
the finite cube, and the difference between a pinned vertex row and
its infinite counterpart. No equality of finite and infinite boundary
stencils is assumed. The exceptional upper exterior is a separate
term already retained once in (2); it is never given the bulk scale a.

We next match coefficients ONLY on the interior near set. L164(2)
decomposes M into complete frozen force/vector local stencils and
O(a p(k)) error stencils, the latter including both insertion
subtractions. The product sum (5)--(6) bounds the complete response
of these error stencils by

    C p(k)p(l) a^2 N^4 = O(p(k)p(l)N^2).               (13)

This estimate is made on the full finite product before discarding
those stencils. No gauge identity substitutes for the force/vector
tensor.

For each remaining local force/vector summand choose its vertex-tail
cell x. Its two rough indices e,e' and its force-edge midpoint differ
from x by only a bounded number of cells. L248(6)--(9) compares each
normalized raw exterior h_k/a there with V_k(x), and u_a with u(x),
with error C a p(k). The complete force/vector coefficients have
their single factor 1/a canceled by the one exterior factor a.
They are finite multilinear ordered-word expressions; hence freezing
these local samples at u(x),V_k(x) costs C a p(k) per stencil entry.
The resulting complete local tensor is precisely the one in
L170(3)--(4), including all four rough directions and the full
exponential-coordinate force correction. Summation with (5)--(6)
makes this another O(p(k)p(l)N^2) response error.

For the exterior at f, L164(3)'s smooth SAME-COMPONENT bulk extension
compares ell_b(f)/a with its value at a same-component reference link
within bounded distance of x. The cost is C a p(l)r. L248(6)--(8)
matches that compact reference to the corresponding component of
V_l(x), at additional cost C a p(l). Both near endpoints are interior,
and the axial bulk exterior component is zero on both sides. Thus
the normalized B coefficient, retaining both endpoint slots and its
color bracket, changes by at most C a p(l)r. The full combined
deterministic coefficient difference is bounded by

    C a p(k)p(l)r.                                    (14)

Use bounded actual deterministic coefficients during (10)--(11).
Then apply (14) to the stationary product P^0 F^-. By its truncated
first moment in (6), this costs C a p(k)p(l)log(eN) per normalized
placement. Only afterwards restore every infinite far row with the
frozen bounded coefficients, using (12). In particular raw matching
is not applied to a remote or pinned exterior link.

Equations (11)--(14) show that the complete normalized row error is

    C p(k)p(l)log(eN)/N.                              (15)

This is a finite inequality at fixed eta, not a growing cutoff
inserted into L170's qualitative local convergence argument.

### 4. Exact coefficient, cell weight and complete probe matrices

Group the local force/vector contributions by vertex-tail cells,
including all four positive force directions once. For constant frozen
u,H,E, the sum of their infinite traces equals the diagonal per vertex
cell of the translation-invariant full tensor M^0(u,H,c). Indeed
each local contribution has only boundedly many residual indices;
translating its force center relative to each diagonal link reindexes
these finite stencil sums into the four positive-link diagonals of
the full M^0. The nonlocal endpoint sum is absolutely convergent by
(6). This is exactly the grouping in L170 section 4, with no extra
force-direction or color multiplicity. Bounded shifts from midpoint
to cell-tail sampling have already been estimated in (14).

The resulting density is L170(6)'s Xi_c(u(x),V_k(x),V_l(x)); sum
over c and insert the original -6 once. L171/L172 import the exact
identity for its continuum integral and full heat series:

    -6 sum_(k,l)c_(i;kl) integral_D
                      Xi(u(x),V_k(x),V_l(x)) dx
                              =-(9/2)K_(i,R).          (16)

This retains the actual half-line half-weight already proved there.
It is not replaced by odd principal-value parity. No new scalar
contraction, numerical sign, outside factor 3 or two-action factor
1/2 enters (16).

Each cell contribution before cubic normalization has the single
factor a from ell_b. Multiplication by a^3 therefore gives exactly
the physical weight a^4. Each fixed frozen component density is smooth
and compactly supported through u, trilinear in u,V_k,V_l, with a
polynomially bounded C^1 norm: derivatives act only on these smooth
coefficients, and their fixed kernel contractions are absolutely
summable by (6). Cell rectangle quadrature costs C a p(k)p(l).
If component midpoint grids are used instead, compare each to the
cell-tail grid by the same C^1 bound before summing components.
No rough projection or prefix column is assigned physical smoothness.
The total cubic-normalized row error in (15) is consequently
C p(k)p(l)log(eN)/N, since a^4 O(N^4)=O(1).

Finally L156(8)'s h_k is exactly the forest retraction of the stored
column a A_(k,a), and its heat coefficient is the covariance-normalized
one of L248(10). L248(11) supplies, for both complete actual probes,

    |c_(i;kl,a)|+|c_(i;kl)|<=C_i exp[-c0(|k|^2+|l|^2)],
    |c_(i;kl,a)-c_(i;kl)|
      <=C_i a(1+|k|+|l|)^4 exp[-c0(|k|^2+|l|^2)].       (17)

All fixed polynomials in (13)--(15) and quadrature are summable
against (17). Missing continuum labels have at least one index of
order N and a polynomially weighted exponentially small tail.
Both triplet average-of-products and shear polarizations, every
allowed zero axial index, the constant prefix and the full physical
lower distance remain. These statements concern both full probe
matrices, not L222's different diagnostic conclusion.

Restore the heat-summed error of (2) once. After multiplication by
a^3 it is O(sqrt(log(eN))/N), within (15)'s allowance. We obtain

    |a^3 Z_i+(9/2)K_(i,R)|<=C_i log(eN)/N.             (18)

Since a^(-3)=N^3/512, (18) proves (1).

### 5. Verification scope and remaining review

The meaningful checks are analytic: (7)--(8)'s compact-source/all-input
prefix comparison and missing lower half-line; (9)'s different
projection geometry; (10)--(12)'s ordered shell sums and complete far
boundary accounting; (13)--(14)'s full residual and remote exterior
placement; and (16)--(18)'s exact coefficient, a^4 weight and complete
heat normalization. No mathematical script or finite-mode test is
needed. Section 6 records the later independent audit of these
specializations; the original derivation does not audit upstream
lemmas. The complete response rate and Yang--Mills construction gaps
are independent.

### 6. Separate critical audit, 2026-10-23

The audit accepts (1) relative to the hypotheses above. It checks the
new quantitative specialization against exactly L172(2), not the
upstream tensor identities or their independent audit qualifications.
No correction to the argument or weaker replacement rate is needed.
This verifies an existing local input; it is not a new rate or a
claim of progress beyond the assessed sources.

**Exact trace and source geometry.** L161(3)'s third term is
-6 Tr[Q_L(ell) F M Sigma]. Expanding Q_L and cycling Sigma past
the trace boundary gives P B_ell F M and the retained B_(L ell)
subtraction, precisely L165(4). It does not commute B with either
kernel. L161 section 3 puts both indices of M in the same compact
stencil enlargement, including its two insertion terms. Expanding
the retained product therefore gives exactly (3), with e' adjacent
to e and component 1 selected by F. Neither the remote link f nor
its prefix inputs acquire a compact-support restriction.

On this component, symmetry changes Sigma(z,e') to Sigma(e',z)
on the SAME edge-Neumann/transverse-Dirichlet grid. L260(7)'s j=0
comparison applies because e' is compact; it is uniform for every
variable z, including normal end links. The prefix has at most N
such terms. Its missing lower inputs have distance at least delta N
from e', irrespective of the transverse coordinate of v or its
interior axial level. Thus the finite comparison and omitted tail
are respectively N O(N^-2) and sum_(j>=delta N) O(j^-2), both
O(N^-1). The finite and infinite upper endpoints coincide. This
checks (8) without requiring the endpoint v to be compact and without
extending the pinned boundary vertex row. The constant axial mode
belongs to the imported component kernel throughout.

For P the inverse instead acts on fully Dirichlet vertices. Its
two differences are at e and f, and the identity terms cancel in
P-P^0. The all-source two-difference comparison in L260(7), with
the normal end-edge convention checked in L165 section 2, gives
N^-4. It is not obtained by differentiating a bound on a different
component kernel. This independently checks the applicability of
the two distinct imported comparisons in (7) and (9).

**Ordered errors and boundaries.** For each residual placement the
first telescoping term in (10) has absolute sum at most
N^-4 times O(N) axial rows times O(N^2) transverse inverse-distance
sum, namely O(N^-1). The second has sum at most
N^-1 sum_(r<=CN) O(r^3) r^-4=O(log(eN)/N).
The endpoint map has finitely many slots and does not change these
powers. The first term uses the finite F, so no error product is lost.

For the stationary product, summing the axial power -4 first gives
O((1+m)^-3); the transverse shell and prefix factors then leave
O((1+m)^-2). Multiplication by r for the truncated first moment
changes the axial power to -3 and leaves O((1+m)^-1). These yield
the finite total mass and logarithmic first moment. For the tail,
transverse distances above R/2 cost O(R^-1); at smaller transverse
distance the remaining axial sum costs O(R^-3) and the transverse
sum O(R^2). This verifies the joint O(R^-1) tail rather than
asserting a first absolute moment for either kernel separately.
The finite N^-4 correction has total O(N^-1) as above.

Choose eta from the fixed clearance of the residual stencil, before
letting N grow. Every near endpoint is interior. Every boundary
vertex, omitted fixed link, normal end link or restored infinite row
is in the complementary product tail; pinned finite prefix rows are
zero there, and their infinite replacements have that same tail bound.
Faces and corners need no different row identity. The exceptional
upper exterior has size O(1), not O(a), and remains solely in L165's
separate O(N^2) error. This checks all rows without assigning a smooth
extension across the upper jump.

**Actual coefficients.** L164(2) supplies the complete force/vector
decomposition with error O(a p(k)) and both insertion subtractions.
Its response error is O(a^2 N^4)=O(N^2), because the other exterior
has size O(a) and the full product sum is bounded. The same count
applies to the raw local matching error. L248(6)--(8) is the
unaveraged h_k/a comparison at compact reference links; no diagnostic
endpoint average is substituted. For every displacement component,
the smooth sampled u_a estimate is the one used in L164 section 1
from L028; L248(9)'s displayed u_1 case is not by itself a claim
about all components. Thus the full tensor in L170(3)--(4), including
the exponential-coordinate correction and all rough directions,
is retained before freezing.

At the remote exterior the relevant input is L164(3)'s global bulk
SAME-COMPONENT difference bound. Dividing by a gives O(a p(l)r),
and only its compact reference link uses L248's raw matching. The
axial bulk component is identically zero. The joint truncated first
moment therefore gives O(a log(eN)) normalized row error. The
coefficient replacement follows the ordered kernel comparison, so
neither a multiplier commutation nor smoothness of a rough column is
needed. Combining these counts gives (15) with a fixed polynomial
envelope in each exterior label.

**Reindexing, coefficient and complete heat normalization.** Write
the frozen tensor as the sum of translates of its finitely supported
force-center contributions. In the trace, translating each such center
to its vertex tail and then translating the diagonal link to its tail
is a bijective reindexing of this finite local sum. The remaining
endpoint sum is absolutely convergent by the joint bound above.
The result is precisely the sum over four positive-link diagonals
and their colors in L170(6); no force direction is counted twice.
The polarization is still L170(4)'s 1/6. Its frozen residual has
size O(1), and B contributes one factor a. Consequently a^3 times
the unscaled cell sum has weight a^4. It is not N^-4, and neither
an outside color factor 3 nor a two-action factor 1/2 is present.

The density is the very Xi used in L171(2) and L172(2), so its
full integral is -(9/2)K_(i,R). L171 section 2's half-line half-weight
is imported with the endpoint sum and color trace intact; it is not
evaluated again here. Smooth coefficients and the absolute kernel sum
give a polynomial C^1 density bound, which justifies O(a) cell
quadrature and bounded midpoint shifts before any heat summation.

L156(8)'s stored column is a A_(k,a) before retraction, exactly the
normalization in L248. The latter's (10)--(11) concern the whole
triplet average of four products and both shear polarizations, not
a selected diagnostic sector. Their two-label Gaussian envelope
sums every fixed polynomial appearing above. Omitted labels have
one frequency of order N; their full polynomially weighted tail is
exponentially small. Own-direction zero indices and their nonzero
physical prefix remain included. Hence both complete probe matrices
permit all comparisons and quadrature just described.

Finally the unscaled comparison costs a O(N^4) times
O(log(eN)/N)=O(N^2 log(eN)). The single imported removed error
O(N^2 sqrt(log(eN))) from L165 is smaller and is counted once.
This proves the audited bound (1), within the requested
N^(5/2)log(eN)^2 budget. No numerical sign, new external theorem,
mathematical script, or full-response cancellation is used.

## Mathlib

Full matching result and supporting relative discrete-kernel coverage:
**not checked**. Unknown is not absence. Reuse the approved
[third-trace assessment](../drafts/literature/2026-10-23-third-ee-trace-quantitative-remainder.md).
Its inspected primary scalar inputs are Lawler--Limic, *Random Walk:
A Modern Introduction* (2010), Theorem 4.3.1, pp. 81--82;
Proposition 4.6.2(a), p. 97; and Lemma 6.3.3, pp. 127--128,
with their transient cases and Delta_d=2d(I-P_walk) normalization
recorded there. They do not state this ordered relative-prefix rate.
No external theorem is newly imported or reproved: the needed mixed
relative image comparisons are L164/L165/L260's qualified inputs.
The new prefix specialization is justified in section 2 because its
source/endpoint placement differs. L170--L172 supply the complete
tensor and exact coefficient; L248 supplies raw/heat estimates,
not a quantitative conclusion for this third trace.
