# L170 — The complete third ordered trace has a finite cubic limit

## Hypotheses

Keep L165's hypotheses: SU(2), the all-face relative fixed-link cube
D=(-4,4)^4, a=8/N through sufficiently fine admitted even meshes,
the straight direction-1 lower-rooted forest, L008's complete compact
displacement, both actual L010 probes at tau=1/16, and the bare
expansion at fixed mesh before refinement. Full tensors precede forest
restriction. Both residual subtractions, every action face and normal
end link, the upper jump, constant axial mode and full heat sum remain.
Let Z_i be exactly L165(1), including its coefficient -6.

Use L156(8)'s finite coefficients c_(i;kl,a) and L080's limiting
coefficients c_(i;kl). For its real relative continuum modes put
A_k=f_k/sqrt(lambda_k), and define the actual forest columns by

    V_(k,1)=0,
    V_(k,nu)=A_(k,nu)-partial_nu integral_(-4)^(x_1)
                                      A_(k,1)(r,x_T) dr, nu=2,3,4.

No numerical or IEEE premise is needed for the result below.

## Conclusion

There is an explicitly specified absolutely convergent real functional

    K_(i,Z)=-6 sum_(k,l)c_(i;kl) integral_D
                    Xi(u(x),V_k(x),V_l(x)) dx,           (1)

where Xi is the full infinite-grid kernel contraction defined in
(3)--(6) below, such that, for i=3,6,

    lim_(a->0) a^3 Z_i=K_(i,Z).                         (2)

This establishes existence, not a value, sign or vanishing, of this
trace's cubic limit. In particular Xi is not replaced by the simpler
action row in L169. The two mixed branches still lack limits, and the
complete cubic residual/action response still lacks a limit and
vanishing test. Other jets, full compensation, finer powers/logarithm,
finite matching, interacting reflected error <=c_box/2, continuum
axioms and infrared finite positive mass remain unresolved. This is
local standard-method REPRODUCTION under the unchanged ready
assessment, without a novelty or candidate-solution claim.

## Proof

### 1. Specify the whole frozen residual tensor

On the full infinite positive-link grid Z^4 use L149(4)--(6)'s ordered
word, clover, endpoint transport and incident action-force formulas.
Set the lattice spacing in those formulas to 1, and set both endpoint
displacements to the same constant vector u. Denote the resulting
generator jets by X^0_1(u), X^0_2(u) and the force jets by G^0_1,G^0_2.
For finitely supported link/color inputs define the homogeneous cubic

    Q^0_u(theta)=sum_e [ <G^0_(e,1)(theta),X^0_(e,2)(theta;u)>
                        +<G^0_(e,2)(theta),X^0_(e,1)(theta;u)> ]. (3)

Each term has bounded stencil radius, and only finitely many terms
are nonzero on such inputs. This is the entire force/vector part of
L155(2), with its exponential-coordinate correction already included
by the exact left-frame force identity; it is not D s_2 X_2 alone.

For a spatially constant link field H, H_1=0, and exterior color c,
define the translation-invariant full-link quadratic tensor M^0 by

    <x,M^0(u,H,c)y>
       =(1/6)[rho s t] Q^0_u(rho H t_c+s x+t y).         (4)

The notation [rho s t] means that coefficient, so (4) is exactly
T_(Q^0_u)(H t_c,x,y), with the third-derivative/3! convention of
L155/L161. For the constant exterior the coefficient is defined by
expanding the LOCAL summands in (3), then summing only those containing
both rough inputs. This is finite when x,y have finite support; no
infinite value of Q^0_u(H) is assigned. It gives a bounded-radius
matrix with entries bounded by C|u||H|. All four force-edge directions
and both transported endpoints are included. Its color entries are
the actual entries of the complete tensor, without a factored color
normalization.

Let g_4 be the scalar infinite Z^4 Green kernel for the unscaled
nearest-neighbor Laplacian, copied to link components and colors.
With D^0 the full vertex-to-link incidence put

    P^0=I-D^0 g_4 (D^0)^T,
    F^-_(v,e)=sum_(j>=0) (g_4)_((1,v_1-j-1/2,v_T),e).   (5)

Thus F^- has zero columns except on component 1; its input sum is
the actual lower half-line. The scalar Green in P^0 acts on vertices,
and that in F^- on component-1 edges, with the indicated staggered
grids. Define B^0_(E t_c)phi=[E t_c,phi_tail+phi_head]. Finally let

    Xi_c(u,H,E)=sum_(nu=1)^4 sum_(alpha=1)^3
       [P^0 B^0_(E t_c) F^- M^0(u,H,c)]_(e_(0,nu,alpha),e_(0,nu,alpha)),
    Xi(u,H,E)=sum_(c=1)^3 Xi_c(u,H,E).                  (6)

Here e_(0,nu,alpha) is the positive nu-link with tail 0 and color
alpha. The product in (6) is defined by its entry sums, not by an
assertion that F^- is a bounded l2 operator. This is a single
trace density per vertex cell, in exactly L165's order.

### 2. Absolute convergence of the density

Fix a diagonal link e in (6). In every nonzero M^0_(e',e), the link
e' is within a fixed stencil distance of e. The infinite versions of
L165(6),(9), justified there by differentiated heat kernels and axial
summation, give

    |P^0_(e,f)|<=C(1+dist(e,f))^-4,
    |F^-_(v,e')|<=C/(1+|v_T-e'_T|).                    (7)

For F^- each individual axial sum converges absolutely, using the
four-dimensional Green bound C(1+dist)^-2. The endpoint map has a
bounded number of entries per link and size <=C|E|. If m is the
transverse separation and n the axial separation, the absolute product
sum is bounded by a constant times

    sum_(m>=0)(1+m)^2/(1+m)
                 sum_(n in Z)(1+sqrt(n^2+m^2))^-4
                       <=C sum_(m>=0)(1+m)^-2<infinity. (8)

Fixed shifts, link directions and colors multiply the constant only.
This proves that (6) is a real, absolutely convergent kernel expression,
trilinear in u,H,E, with

    |Xi(u,H,E)|<=C|u||H||E|.                            (9)

In particular it defines a finite signed coefficient without a Fourier
principal-value prescription. The half-line in (5) is retained in
full; neither its zero-frequency contribution nor its endpoint is
removed. We do not claim a factorization or evaluate its Fourier row.

### 3. Uniform tail control in the actual finite trace

L165(3) gives exactly

    Z_i=-6 sum_(k,l,c)c_(i;kl,a)
                    Tr[Phat B_(ell_b) Fhat M]
                      +O_i(N^2 sqrt(log(eN))).          (10)

Both upper action exterior and smooth-action subtraction are included
in this proved subcubic error. Fix k,l,c before summing heat labels.
L164(2) decomposes the COMPLETE residual M into its force/vector
stencils with frozen u and h_k, plus an entrywise O(a p(k)) sum of
bounded-radius stencils. The latter includes both insertion
subtractions. There are O(N^4) placements. L165's product bound
applies unchanged to these error stencils, and |ell_b|<=C a p(l).
Their total trace is therefore O(p(k)p(l) a^2 N^4)=O(p(k)p(l) N^2).
This estimates the subtractions before removing them at cubic scale.

For each remaining residual entry e',e, the finite product is bounded
by C p(k)p(l) a times

    [(1+dist(e,f))^-4+N^-4]/(1+|f_T-e_T|).              (11)

The decaying part is summable by (8), so its tail outside any fixed
four-dimensional offset radius R tends to zero as R tends to infinity.
The constant part has full finite sum O(N^-1): the axial count is
O(N), and the transverse inverse-distance sum is O(N^2).
After summing O(N^4) placements and multiplying by a^3, (11) thus
gives a limsup tail bounded by C p(k)p(l) times a function of R
tending to zero. The constant part contributes O(p(k)p(l)/N).
This is uniform vanishing tail control, stronger than boundedness of
the normalized trace. It includes all boundary source rows.

For bounded offsets, the actual prefix needs an additional axial
truncation J. L169(6)'s undifferenced-prefix argument gives the bound
C/J+C/N on the omitted axial summands, uniformly at compact residual
observations. Truncate J first. The lower root is a distance >=delta N
from these observations. The finite Green comparison in L164(5)
then gives convergence to (5), first as N tends to infinity and then
as J tends to infinity. No differentiated-prefix estimate or smooth
extension at the upper pin is substituted for this argument.

### 4. Local convergence and cell normalization

On the compact stencil enlargement, L150's smooth forest extension
and L168(5) imply h_k/a -> V_k uniformly at each fixed mode, including
every fixed endpoint shift. The bulk action column likewise satisfies
ell_b/a -> V_l. L164(5) and L165(7)--(8)'s two-difference image
comparison give local convergence P -> P^0. Section 3 gives F -> F^-.
All of these limits are uniform over the compact physical observations.

The force/vector tensor has exactly one 1/a from the generator in
L149(5), and one exterior factor h_k=a(V_k+o(1)). Its finite ordered
word coefficients therefore converge on each fixed stencil to (4),
with u=u(x) and H=V_k(x). This uses the full force/vector jet, not its
quadratic gauge identity. Neighbor displacement and exterior changes
are already covered by L164's O(a) error. There are no further powers
of a in the ordinary-coordinate force or action words.

Group the four positive force-edge centers by their vertex tail.
At bounded offsets the trace is linear in their local residual
summands. Its limiting sum over these four centers and all diagonal
link/color indices is precisely the translation-invariant density
(6). This grouping counts each positive force edge once. Equivalently,
for the translation-invariant kernel product the sum of all local
force contributions to its diagonal equals its diagonal per vertex
cell. Reindexing is legitimate by (8) and the bounded residual radius.
The shifts of force-edge midpoints from their cell tail vanish physically.

The endpoint map contributes its one factor ell_b=a(V_l+o(1)).
Thus each vertex-cell contribution to the unscaled bulk trace, divided
by a, converges to Xi_c(u(x),V_k(x),V_l(x)), before summing colors,
with the offset tails controlled as in section 3. Multiplication by
a^3 gives the Riemann weight a^4, not N^-4 or an additional color
factor. For any fixed offset and prefix cutoffs, smooth fixed modes
and compact displacement give the usual cell Riemann limit over D.
The compact support makes the bounded-offset cells interior for all
large N. Remove prefix and spatial cutoffs in the order of section 3;
its uniform tails and (8) identify the integral in (1). Boundary action
rows are in the controlled spatial tail, while the exceptional upper
exterior has already been retained in (10).

### 5. Restore both actual probes and the outside factor

L156(8) supplies mesh-uniform summability
sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i for each fixed polynomial p.
L080 supplies fixed-pair coefficient convergence; its Gaussian heat
majorants also make tails outside finite exterior-mode sets uniformly
vanishing. The estimates above have only fixed polynomial mode losses.
Consequently finite heat sums can be taken first, and all omitted heat
labels removed last. Equation (9) gives absolute convergence of the
limiting series/integral in (1). The entire lower prefix, including
its constant axial mode, is present in V_k and F^-.

Finally the errors in (10) and section 3 have zero a^3 limit. Restoring
the -6 of L165 once, and the color sum already in Xi, proves (1)--(2).
No additional factor 3 or two-action factor 1/2 is inserted. The
remaining problem is to contract this full frozen residual density
and the two mixed branches, not to infer a sign from its existence.

## Mathlib

Full matching theorem and supporting relative-prefix/kernel coverage:
**not checked**. Unknown is not absence. Reuse the unchanged ready
[target assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No external theorem is newly imported or reproved. The finite words,
complete tensor and normalization come from L149/L155/L161; L164/L165
give the controlled decomposition, exact order and summable product;
L150/L168 give the actual exterior convergence, L169 the undifferenced
half-line limit, and L156/L080 the complete heat bounds and coefficient
convergence. Absolute convergence, dominated convergence and compact
Riemann sums are applied with their explicit bounds above. No numerical
diagnostic, mathematical script, or evaluated compensation is used.
