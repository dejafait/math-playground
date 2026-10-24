# L261 — Quantitative remainder for the second ordered E,E trace

## Hypotheses

Keep exactly L166/L169's relative SU(2) cube D=(-4,4)^4, sufficiently
fine admitted even N, a=8/N, tau=1/16, straight lower-rooted direction-1
forest, ordinary stored coordinates and bare-first expansion. Let Y_i
be L166(1), including its coefficient -12, for both actual probes i=3,6.
Retain both residual Q forms, every action/source/end row, the upper
pinned jump, allowed constant modes and the complete heat sums.

Import L166's exact bulk order, compact residual support and removed
errors; L164's component Green comparisons and smooth bulk exterior;
L260(5)'s uniform compact-observation residual comparison; and
L248(3)--(11)'s raw interior exterior and complete heat estimates.
All upstream analytic and pending-audit qualifications remain imports.
K_(i,R) is precisely L145's functional, identified with the second
trace coefficient by L169(2). No numerical sign enclosure is used.

## Conclusion

For constants independent of the mesh,

    |Y_i+3a^(-3)K_(i,R)| <= C_i N^2 log(eN),   i=3,6.      (1)

This is within the requested N^(5/2)log(eN)^2 component budget.
The separate critical audit in proof section 6 accepts this specialization
relative to its stated imports; upstream audits remain separate. It is local
REPRODUCTION under the approved assessment, without an originality
claim. It supplies no third-trace rate, complete quantitative response
assembly, interacting reflected estimate, continuum construction or
finite positive infrared mass.

## Proof

### 1. Exact order and the joint kernel counts

L166(3), including the upper action exterior and smooth-residual
subtraction once, gives

    Y_i=-12 sum_(k,l,c)c_(i;kl,a)
          Tr[Sigmahat Ahat B_(h_k t_c) Fhat N_b]+O_i(N^2), (2)

where F=Phi Sigma and N_b=T_S(ell_b t_c,.,.). The full tensors
precede restriction. For a fixed heat pair, polynomial mode factors
are written p(k)p(l); every such polynomial is summed at the end.
An entry of this trace is

    (Sigma A)_(x,e) (B_h)_(e,v) F_(v,y) (N_b)_(y,x).      (3)

Here e lies in a fixed compact interior enlargement S of the support
of A, v is one of its two endpoints, and x,y are within a fixed
stencil distance. There are O(N^4) choices of e and bounded component,
endpoint, action-stencil and color multiplicities. For quantitative
comparison retain individual local action-stencil contributions if
several plaquettes contribute to the same entry. Their multiplicity
is uniformly bounded. Only component-1 y survives in F.

Write r=1+dist(e,x) and b=1+|e_T-x_T|. All distances are lattice
midpoint distances; bounded shifts change constants only. Normalize

    R_N(x,e)=a(Sigma A)_(x,e),
    R_inf,e(x)=(g A^0(u(x_e)))_(x-e),
    F_inf(v,y)=(Phi_- g)_(v,y),                         (4)

with exactly L169(5)--(7)'s frozen residual and lower half-line.
In particular Phi_- uses component-1 edges v_1-j-1/2, j>=0.
The scalar g is the infinite unscaled four-dimensional Green kernel,
copied to link components; x_e denotes the physical midpoint of e.
The bounds in L166 and their infinite constant-coefficient versions are

    |R_N|<=C(r^-4+N^-4),   |R_inf,e|<=C r^-4,
    |F|+|F_inf|<=C b^-1.                               (5)

For F_inf the last bound follows by the same full axial sum of g as
L166(11)--(12). In (3) the two normalized exterior factors are
B_h/a and N_b/a, bounded by C p(k) and C p(l). Thus the actual row
prefactor is a, not a^2 or 1. No prefix has been moved through A or N_b.

The joint infinite majorant q(n,z)=(1+sqrt(n^2+|z|^2))^-4
(1+|z|)^-1 satisfies, for R>=2,

    sum q <= C,
    sum_(sqrt(n^2+|z|^2)>R) q <= C/R,
    sum_(sqrt(n^2+|z|^2)<=R)
                    (1+sqrt(n^2+|z|^2)) q <= C log(eR). (6)

Here and below sums include all axial integers and transverse Z^3
sites. To verify these claims, a transverse shell m has at most
C(1+m)^2 sites and the complete axial sum of the power -j is
C(1+m)^(1-j), j>1. For the zeroth moment the resulting series is
sum_m C(1+m)^-2. For the truncated first moment, enlarge its axial
range to all integers and use j=3, leaving sum_(m<=R) C(1+m)^-1.
For the tail, |z|>R/2 costs C/R by the zeroth-moment series. In
the complement the axial index obeys |n|>cR; its fourth-power sum
is O(R^-3). The remaining transverse weighted count through radius
R is O(R^2), again giving O(R^-1). The added 1 covers small distances.
The finite constant term has the separate complete-box bound

    N^-4 sum_x b^-1 <= C N^-4 N sum_(m<=CN)(1+m)
                         <= C/N.                      (7)

These are the second trace's counts. Its first joint moment is only
logarithmically bounded on a finite ball; L260's different product
moments are not used.

### 2. Compare the undifferenced prefix only in the near region

Choose a fixed eta>0 sufficiently small that every source x with
r<=eta N, its action stencil and the adjacent y have fixed positive
physical clearance from all faces, uniformly for e in S. This is
possible because S has fixed clearance. All near action stencils
therefore agree with their infinite-grid counterparts. This split
selects action placements, not the covariance inputs in F.

For such y, component symmetry permits viewing y as the compact
observation in the Green comparison. For every actual component-1
prefix input z below v, including the first normal link at the lower
face, L260(7)'s j=0 comparison (equivalently the image proof of
L164(5)) gives

    |Sigma_(z,y)-g_(z-y)|<=C N^-2.                     (8)

The compact set here is a fixed enlargement with smaller clearance
than S. The image proof depends only on that clearance, so its same
constant type applies. No compactness of z is required: by symmetry
it is the arbitrary source. Its component is Neumann in direction 1
and Dirichlet in the other three directions, exactly as in L166.
There are at most N such z. The missing infinite half-line below the
lower root has axial distance at least cN from y, because y is near
the compact e. Consequently

    sum_(missing z)|g_(z-y)|
                  <=C sum_(n>=cN)n^-2 <= C/N.

The actual finite prefix and Phi_- have identical upper endpoints
at v and identical link-center offsets. Thus, on the entire near set,

    |F_(v,y)-F_inf(v,y)|<=C/N.                          (9)

This estimate keeps the complete finite prefix and constant axial mode.
It is not asserted when y approaches a face. In particular no upper
pinned prefix row is compared to a nonzero infinite extension: v is
an interior endpoint of e throughout.

For the other factor, L260(5) applies at exactly its existing compact
residual observation, before any prefix sum:

    |R_N(x,e)-R_inf,e(x)|
                 <=C[a r^-3+a^2 r^-2+N^-4].            (10)

Both generator orientations and both Q forms are already included in
this imported estimate. Only this residual comparison from L260 is
used, not its fourth-trace conclusion or its prefixed-residual bound.

Apply the ordered two-term telescoping on the near set,

    R_N F-R_inf,e F_inf
       =(R_N-R_inf,e)F+R_inf,e(F-F_inf).                (11)

Products here mean the original fixed component/color entries of
(3), with their endpoint and action indices unchanged. Taking absolute
values after this identity, (5), (9), (10) give

    sum_near |(R_N-R_inf,e)F|
       <=C[a log(eN)+a^2 N+N^-1],
    sum_near |R_inf,e(F-F_inf)|<=C N^-1 log(eN).         (12)

For the first line, sum axial powers -3 and -2 first: with the
transverse shell and b^-1 they leave respectively sum_(m<=CN)b^-1
and sum_(m<=CN)1. The constant term is (7). For the second line,
four-dimensional shells give sum_(r<=CN) r^-4<=C log(eN).
Since aN=8, the complete normalized near-row error is O(log(eN)/N).
No separate l2 assertion for the undifferenced four-dimensional g
or operator norm for Phi is needed.

### 3. Far action rows, boundaries and exterior freezing

On every far finite action placement r>eta N, use (5)--(7) and the
global bulk coefficient bounds of L164(3), without a Green comparison:

    sum_far |R_N F| <= C/N.                            (13)

The whole infinite frozen product outside that same near region also
costs C/N, by (6). In particular all boundary-touching plaquettes,
fixed-link omissions, normal end links and missing infinite action
rows are included in (13) or the restored infinite tail. Compactness
of e separates each boundary stencil by order N. Each finite entry
is bounded by (5) even there; pinned zeros can only reduce that
bound. The upper action exterior is a different part, already retained
in (2)'s O(N^2) error. No bulk bound is assigned to its jump.

It remains to match deterministic coefficients on the near region.
Apply L164(3)'s same-component smooth bulk extension to each exterior
link in a local action stencil about x. Compare it with a same-component
link within bounded distance of e, then use L248(6)--(8)'s compact raw
matching at that reference link. All near stencils are interior.
Thus each normalized exterior sample differs from its appropriate
component of V_l(x_e) by at most C a p(l) r. The identical compact
matching for h_k at e costs C a p(k).

The exact trilinear action is a fixed finite linear combination of
these samples with mesh-independent coefficients: L164(7) retains
all three polarized placements and the factor 1/3. Replacing every
sample by the constant V_l(x_e) therefore changes each normalized
local action stencil by at most C a p(l) r. In particular the exterior
circulation is included in this bound; it is not silently set to zero
in the original trace. Both spatial orientations and each color slot
remain. The endpoint map B_h retains its two summed endpoint slots.
Hence the product of normalized deterministic coefficients in (3)
differs from its frozen counterpart by at most

    C a p(k)p(l) r.                                    (14)

Use actual bounded coefficients while applying (11)--(12). Then use
(14) on the frozen kernel product. Equation (6)'s truncated first
moment bounds this latter cost by C a p(k)p(l) log(eN). Restore the
infinite frozen action rows only afterwards, using their bounded
constant coefficients and (6). This order avoids applying compact
raw matching to a remote or pinned exterior row.

Combining (12)--(14) proves, for each residual observation and each
heat pair, a complete normalized row comparison bounded by

    C p(k)p(l) log(eN)/N.                              (15)

Every finite action/source/end row has now been estimated. The entire
prefix input sum was retained during (8)--(9), and (13) retains every
far action source. No varying cutoff was inserted into L169's
qualitative local-limit argument: eta is fixed and (8)--(15) are
uniform finite inequalities.

### 4. Exact coefficient, quadrature and both full heat sums

Include the original -12 and color sum in the stationary row density
for each component of e. L169 sections 2--3 evaluate the sum of their
integrals as exactly

    -3 g_G integral_D u_1(x) V_k(x) dot V_l(x) dx.       (16)

This imports L169's full constant-exterior action polarization,
residual symbol, actual-prefix half-weight and color calculation.
In particular its endpoint factor 2, residual half, prefix half,
action polarization 1/3 and color sum are not recomputed or multiplied
by another outside factor 3. There is no numerical sign premise.

Each individual component density before summing components is a
smooth compactly supported function with polynomially bounded C^1
norm in k,l: the stationary kernel product is absolutely summable by
(6), linear in u(x) and bilinear in the smooth V fields. Its derivatives
act only on these deterministic coefficients; the kernel and endpoint
stencils are fixed. Quadrature on each component's own midpoint grid
therefore costs C a p(k)p(l). One may include all cells outside S
since the frozen density vanishes there; any finite residual rows in
the stencil enlargement of the support were already covered by (15).
The separate component integrals may then be summed in (16). No
rough Green column is differentiated by a physical Taylor argument.

The row prefactor in (3) is a. Multiplication by a^3 makes the physical
weight a^4; there are O(N^4) residual rows. Thus (15) gives a complete
cubic-normalized fixed-pair error C p(k)p(l) log(eN)/N. The component
quadrature error is smaller. To sum all pairs use exactly L248(10)--(11):

    |c_(i;kl,a)|+|c_(i;kl)|<=C_i exp[-c0(|k|^2+|l|^2)],
    |c_(i;kl,a)-c_(i;kl)|
       <=C_i a(1+|k|+|l|)^4 exp[-c0(|k|^2+|l|^2)].      (17)

L156's heat normalization is the same one in (2). The finite mode
errors above hold with fixed polynomial envelopes for every retained
label. These are summable against (17). Missing continuum labels
have at least one index of order N, so their polynomially weighted
Gaussian tail is exponentially small and in particular O(1/N).
Allowed zero axial indices, their linear primitive and every constant
prefix remain. Equation (17) includes all four products of the triplet
average and both shear polarizations. There is no selected-probe-sector
replacement. Restoring L166's heat-summed O(N^2) error once yields

    |a^3 Y_i+3K_(i,R)|<=C_i log(eN)/N.                  (18)

As a^(-3)=N^3/512, this proves (1). The removed smooth-residual term
O(sqrt(log(eN))) is already inside the O(N^2) allowance in (2).

### 5. Original verification scope

The new load-bearing steps are the near-region uniform prefix estimate
(9), its ordered product comparison (12), and the far-region accounting
(13). The complete joint tail is O(1/R), whereas the truncated first
moment is logarithmic. Neither bound is borrowed from the fourth trace.
All shell estimates are analytic sums, not numerical diagnostics. No
mathematical script is needed. A later critical audit must check the
symmetry/source placement in (8), the lower missing half-line, all
boundary action stencils, and the full coefficient/heat normalization.
The proof does not audit any upstream premise or resolve the independent
interacting and construction gaps.

### 6. Separate critical audit, 2026-10-23

This audit accepts (1) relative to the stated analytic inputs. It checks
the quantitative specialization, not the proofs of every imported
lemma. The original verification scope above records the pre-audit
obligations; the checks below discharge them for this result. No new
external theorem, numerical premise or mathematical script is used.

**Exact placement and normalization.** L166(4) cycles the second trace
to Sigma A B_h F N minus B_(A h) F N Sigma. Its (16)--(17) bound
the complete upper-exterior term and the latter subtraction by O(N^2)
and O(sqrt(log(eN))), respectively, after the heat sum. Thus (2)
retains both exactly once. In (3), compactness belongs to e and its
adjacent vertex v, not to x, y or the inputs summed inside F. The
symmetry identity is (Sigma A)_(x,e)=(A Sigma)_(e,x); it does not
commute A and Sigma. L260(5) applies to precisely this row, with
the same frozen A^0, both generator orders and both Q subtractions.
The factors Sigma A, B_h and N_b have scales a^-1, a and a.
The remaining prefix is unscaled. Hence the row weight really is a.

**Near-source comparison with every prefix input.** Choose delta>0
so that S, including all residual/end-point stencils, is at least
delta N from every face for sufficiently large N. Choose fixed
eta<delta/4. A near action link y and its bounded stencil shifts
then have clearance at least delta N/2. Their union lies in one
fixed compact physical set, independently of e, N and the heat labels.
Since F has only component-1 columns, its entries here sum the same
component Green function Sigma_11(z,y). Symmetry changes this to
Sigma_11(y,z) on the same staggered grid. L260(7), with j=0 and
this enlarged observation set, therefore bounds Sigma_11-g by
C_delta N^-2 for every actual z. It includes z at the first normal
link, all intermediate prefix levels and all constant edge modes.
It requires no clearance of z. The one-Neumann/three-Dirichlet
component, rather than the scalar killed kernel, is essential.

There are at most N actual inputs. The infinite prefix has the
identical upper endpoint v_1-1/2. Its additional inputs lie below
the lower root, at axial distance at least delta N/2 from y;
their g sum is bounded by C sum_(j>=delta N/2) j^-2<=C_delta/N.
Together these give (9), without a comparison at a pinned vertex
row or any extension above the prefix endpoint. This proves the
needed uniformity on the whole near region, not just at fixed offsets.

**Independent row sums and ordered errors.** Let b=1+|z| and
rho=1+sqrt(n^2+|z|^2). For j>1 the full axial sum of rho^-j is
at most C_j b^(1-j). A transverse shell of radius m has O((1+m)^2)
sites. Thus rho^-4 b^-1 has shell sum O((1+m)^-2). Multiplying
by rho and restricting to rho<=R gives at most
C sum_(m<=R)(1+m)^-1. For its tail split at |z|=R/2:
the outer transverse part costs C/R; the inner part has |n|>cR,
so its axial sum is O(R^-3), multiplied by
sum_(|z|<=R/2) b^-1=O(R^2). The tail also costs C/R.
This verifies all of (6), including the long axial tail at small
transverse separation. Over the complete finite box,
N^-4 sum_(n,z)b^-1<=C N^-4 N N^2=C/N, proving (7).

In (11) the first difference must multiply the actual F. With its
full-source bound b^-1, the three terms of (10) sum to

    C a sum_(m<=CN)(1+m)^-1,
    C a^2 sum_(m<=CN)1,
    C/N.

They are O(log(eN)/N), O(1/N) and O(1/N). In the second
telescoping term (9) multiplies the infinite residual rho^-4.
Four-dimensional shells give C N^-1 sum_(r<=CN) r^-1,
again O(log(eN)/N). No product of two errors is omitted: (11)
is the exact two-term identity with F, not F_inf, in its first term.
No l2 property of g or operator bound for Phi is invoked.

**Every far action stencil.** Keep the action as a sum of individual
plaquette contributions, with bounded multiplicity and stencil radius.
Any plaquette touching a physical face is distance at least c_delta N
from e, even after its rough links are shifted within that stencil.
The bulk exterior coefficient is globally bounded by C a p(l),
including its actual zeros; no boundary Lipschitz estimate is needed.
The decaying product in (5) then costs C/N by the tail just proved,
and its finite constant costs C/N over the larger complete box.
This covers normal end links at both axial ends and at every transverse
face, as well as surviving variable links of plaquettes with fixed
tangential links. Edges and corners are included in the same finite
stencil count. Fixed rough links themselves are absent from the finite
space; the corresponding infinite rows and all rows outside the cube
are in the frozen tail. They too cost C/N. Pinned zeros are used only
in finite value bounds, not to assert equality of boundary tensors.
The separate upper exterior N_top has its already-counted O(N^2)
bound and is never assigned the bulk exterior scale a. Thus no action
face, fixed-link omission or normal end row requires an unproved
near-source comparison.

**Deterministic matching, coefficient and heat sum.** Only interior
near stencils receive coefficient freezing. L164(3) compares each
bulk exterior component at its actual action link with a same-component
reference within bounded distance of e. After division by a the
cost is C a p(l)rho. The reference, and h_k at e, satisfy L248(6)--(8)
with error C a p(l) and C a p(k). Axial bulk exterior components
are exactly zero on both sides. The full action polarization is a
fixed linear combination of these samples, including its exterior
circulation and its factor 1/3. Multilinearity and the separate value
bounds give (14) for every endpoint/color/stencil slot. Applying the
truncated joint first moment costs C a p(k)p(l)log(eN). Infinite
far rows are restored with constant coefficients only after this step.
Raw matching is never asserted for a remote or pinned exterior link.

The frozen order is exactly L169(4)--(7), so its section 3 applies.
Its scalar integral J=-g_G/4 and factors give
(-12)(-6)(1/6)J=-3g_G. The 1/6 already includes the endpoint,
residual, actual-prefix half and polarized-action normalizations.
There is no additional outside factor 3. L145(1) uses the same
physical V columns and covariance-normalized c_(i;kl). This confirms
the exact subtracted coefficient in (18), without using its sign.

For each observation component separately, the stationary density is
linear in u(x) and bilinear in V_k(x),V_l(x), times fixed absolutely
summable kernel coefficients. Its physical first derivatives have
polynomial mode bounds by the same summable majorant. Compact u
support permits O(a p(k)p(l)) midpoint quadrature on that component's
own grid, without differentiating a rough kernel. The row count and
weight are a^3 times a times O(N^4)=O(1). Thus the normalized
response error is O(p(k)p(l)log(eN)/N).

L156(8) defines h_k as the forest retraction of a A_(k,a); its probe
matrix is exactly the covariance-normalized matrix in L248(10).
L248(11) supplies both Gaussian value and O(a) polynomial error
envelopes in (17) for every retained pair. They sum all the polynomials
above and retain the triplet's four products and both shear terms.
The allowed zero axial labels remain; missing labels have size at
least order N and exponentially small polynomially weighted tails.
Finally the original O(N^2) removal contributes O(1/N) after cubic
normalization, once. This establishes (18), hence (1).

No unsupported estimate was found within this specialization. The
audit verifies one existing local input, without claiming a new rate
beyond the original proof or originality beyond the checked sources.
The third trace, quantitative full-response assembly and all interacting,
continuum and infrared construction gaps remain independent.

## Mathlib

Full matching result and supporting relative discrete-kernel coverage:
**not checked**. Unknown is not absence. Reuse the approved
[second-trace assessment](../drafts/literature/2026-10-22-second-ee-trace-quantitative-remainder.md).
No external theorem is newly imported or reproved. Its recorded primary
coverage is Lawler--Limic, *Random Walk: A Modern Introduction* (2010),
Theorem 4.3.1, Proposition 4.6.2(a), and Lemma 6.3.3, with the inspected
transient cases and normalization qualifications stated there. Those
scalar theorems are supporting coverage, not a theorem about this relative
ordered trace. The actual component boundary comparison is imported from
L164/L260; the new undifferenced-prefix specialization is justified above
because its placement differs. L169 supplies the coefficient and L248
the raw/heat bounds, not a quantitative conclusion for this trace.
