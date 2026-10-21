# L255 — Quantitative action-Hessian branch remainder

## Hypotheses

Keep exactly L173's relative SU(2) cube D=(-4,4)^4, admitted even
N, a=8/N, straight direction-1 lower-rooted forest, stored coordinates,
bare-first expansion, complete compact displacement and actual probes
i=3,6 at tau=1/16. Use L173(1)'s exact one-color branch

    T_i=-6 sum_(e,f) A_ef U_(i,fe) K^+_fe.                 (1)

The coefficient K_(i,T) is exactly L173(8), with its alpha,beta,W,S,
H^0,H^1 and physical lower distance d=x_1+4. Both insertion
subtractions, the adjoint coefficient derivative and all four endpoint
pairs retain those definitions. There is no additional color factor.
All source/end rows, constant modes, pinned upper jumps and complete
heat sums in the exact reduction remain. The residual row support and
its fixed stencil enlargement have clearance at least delta N from
every face for large N, for a fixed delta>0.

Import L173's exact scalar representation, bounds (9)--(13), finite
row parity (17) and displacement expansion (18). Import L156's
smooth residual-column estimate (9) and full heat sum (8), as used
in L173. Import only L254(18)'s quantitative C^2 exterior estimate,
whose columns and probe coefficients are exactly L173(6); retain its
L222/L248 qualifications. No upstream audit or other response estimate
is asserted here.

## Conclusion

For both actual probes, constants independent of sufficiently large
admitted N give the stronger-than-requested bound

    |a^3 T_i-K_(i,T)| <= C_i N^(-1/2) log(eN),
    |T_i-a^(-3)K_(i,T)| <= C_i N^(5/2) log(eN).           (2)

In particular the approved O(N^(5/2)log(eN)^2) budget holds for this
branch. This is a quantitative specialization of an existing signed
limit argument, classified REPRODUCTION with no originality claim.
Section 4's separate critical audit accepts this rate relative to the
stated imported premises. It supplies no complete cubic
residual/action or L011 remainder, interacting reflected-error bound,
continuum axioms or finite positive infrared mass.

## Proof

### 1. Quantify the subtracted double-heat comparison

Write the axial Dirichlet heat kernel as h^D_v and the transverse
three-dimensional Dirichlet heat kernel as p^D_u. L173(12) states

    F_N((s,y),(t,z))=
      integral_(v,w>=0) h^D_v(s,t) p^D_(v+w)(y,z) dw dv. (3)

Let h_v,p_u denote the corresponding infinite kernels. Set
alpha_e=F_N(v_e,v_e), with precisely L173's reference vertex, and
let f(r) be L173(14)'s subtracted infinite potential. We prove uniformly
over all supported stencil endpoint pairs

    |F_N(v_0,w_0)-alpha_e-f(v_0-w_0)|
                            <= C N^(-1/2) log(eN).       (4)

Here v_0,w_0 denote spatial vertices, distinct from heat times v,w.
All heat times in this proof are dimensionless. We never assign a
finite integral to either unsubtracted infinite term.

Join (v_e,v_e) to (v_0,w_0) by a bounded number of single-coordinate
steps in either argument. The number is fixed by the residual stencil,
and every intermediate vertex has the same clearance after reducing
delta. For an axial step, L173(13) bounds the difference integrand,
for either finite or infinite kernels, by

    C (1+v)^(-1) (1+v+w)^(-3/2).                         (5)

For a transverse step the bound is

    C (1+v)^(-1/2) (1+v+w)^(-2).                         (6)

These estimates include all low modes and times above N^2. Put u=v+w.
On the entire complementary region u>T, (5) has integral at most

    C integral_T^infinity (1+u)^(-3/2)
                    [integral_0^u (1+v)^(-1) dv] du
      <= C log(e+T)/sqrt(1+T).                           (7)

Indeed the inner integral is log(1+u); integration by parts bounds
the outer integral by
2 log(1+T)/sqrt(1+T)+4/sqrt(1+T). The analogous integral of (6)
is at most

    C integral_T^infinity (1+u)^(-2)
                    [integral_0^u (1+v)^(-1/2) dv] du
      <= C/sqrt(1+T).                                   (8)

This includes the strip with small v and arbitrarily large w, rather
than merely the region where both times are large. Finite and infinite
tails are bounded separately; no cancellation between them is needed.

On u<=T use a uniform polynomial comparison. The finite and infinite
axial and scalar transverse Laplacians are self-adjoint bounded
operators with norm at most M=12. For example, their quadratic forms
are sums of squared nearest-neighbor differences, including the
Dirichlet end edges; (x-y)^2<=2x^2+2y^2 gives the bound 4d in
dimension d. Their interior coefficients agree and their range is one.

Take m=floor(delta N/2), with delta reduced so all paths of length
at most m from every selected row stay strictly interior. For each
of the axial and transverse operators, finite and infinite matrix
entries of every power through degree m agree exactly. Expand a
power into nearest-neighbor paths: none reaches a changed boundary
coefficient or an omitted row. This is a local-entry equality, not
an equality or approximation of the full finite and infinite inverses.

For a heat time t define q_m(t,L)=sum_(j=0)^m (-tL)^j/j! and put

    T=m/(8 e M).

For 0<=t<=T the spectral theorem and scalar Taylor remainder give

    ||exp(-tL)-q_m(t,L)||
       <= exp(Mt)(Mt)^(m+1)/(m+1)!
       <= exp(m/(8e)) 8^(-(m+1)) <= exp(-m).             (9)

The factorial estimate n!>=(n/e)^n follows by integrating log x
from 1 to n (and holds also at n=1). The same (9) holds on all four
finite/infinite spaces. Polynomial entry equality therefore gives a
finite-to-infinite error at most 2 exp(-m) for either heat kernel,
uniformly over t<=T and all selected entries. Heat operators have
norm at most one, so their individual entries have absolute value at
most one. Telescoping a product h_v p_(v+w) then costs at most
4 exp(-m). A single-coordinate difference uses two such products
and costs at most 8 exp(-m).

The triangle v,w>=0, v+w<=T has area T^2/2. For each step, the
retained integral error is thus at most C T^2 exp(-m). Combine this
with (7)--(8) for both finite and infinite kernels, and telescope the
bounded chain. The infinite differences telescope exactly to f(v_0-w_0)
because their initial displacement is zero. Since m and T are fixed
positive multiples of N up to integer rounding, this proves (4).
The finitely many smaller N may be absorbed in the constants if desired.

The polynomial argument is the existing finite-range heat method
specialized to this scalar double integral; the newly quantified part
is its complete two-time tail. No derivative image theorem, projection
estimate or local central limit assertion is substituted for (5)--(6).

### 2. Retain the scalar and inversion-even pieces

Use exactly L173(5),(16)'s W,S,E and eta_e=j_e b_e-alpha_e, where
j_e=d(x_e)/a and b_e is the local scalar transverse boundary correction.
L173(11)'s O(N^-1) error and (4), summed over the four endpoint pairs,
give

    K^+_fe=j_e W_(mu f)+4 eta_e+S_(mu f)+E_(mu f)+rho_(ef),
    |rho_(ef)|<=C r_N,     r_N=N^(-1/2)log(eN),
    |eta_e|<=C log(eN).                                  (10)

The arrays W,E are bounded and inversion-even, S is bounded and
inversion-odd. These are the same finite arrays as in L173; in
particular E includes its convergent subtracted f and absolute-value
axial kink. The boundary error N^-1 is below r_N. The logarithmic
scalar remains a separate exact row contribution.

For that scalar, sum over f before estimating:

    sum_f A_ef U_(i,fe)
      =sum_(k,l) c_(i;kl) (h_l)_e (A h_k)_e.             (11)

L173 section 4's column bound gives |h_l|<=C a p(l), and L156(9)
gives |A h_k|<=C a^5 p(k) on the supported rows. The full heat sum controls
all k,l. There are O(a^-4) such rows. Thus the scalar contribution
to T_i is O_i(a^2 log(eN)), and its a^3-normalized size is
O_i(a^5 log(eN)). No eta_e crosses A or is assumed constant in e.

For rho, the exact fixed-range row bounds |A_ef|<=C/a and
|U_(i,fe)|<=C_i a^2 give, after all rows and the single -6,

    |a^3 sum_(e,f) (-6) A_ef U_(i,fe) rho_(ef)|
                                                    <= C_i r_N. (12)

This is where a uniform local comparison is sufficient. There is no
global prefix-covariance replacement or damping of an internal loop.

### 3. Match the complete three densities at a rate

Keep the finite exterior H_(i,a) from L173(6). The matching statement
L254(18) gives on the compact two-point enlargement

    ||H_(i,a)-H_i||_(C^2)<=C_i a,
    ||H_(i,a)||_(C^2)+||H_i||_(C^2)<=C_i.                 (13)

This uses the same raw, unaveraged links, constant axial primitive,
covariance-normalized full probe matrices and both complete heat sums.
Only this exterior estimate is imported, not L254's different local
projected covariance, response normalization or factor twelve.

Let alpha_a,beta_a be the frozen finite-mesh rows of L173(18).
The finite linear stencil maps and the imported O(a^2) smooth
coefficient errors imply

    A_ef=a^-1 alpha_(a,mu f)(x_e)+beta_(a,mu f)(x_e)+O(a),
    alpha_a-alpha=O(a^2),       beta_a-beta=O(a^2).        (14)

The same estimates hold for the coefficient derivatives needed below.
The transposed coefficient samples and both frozen insertion stencils
are included. H_a^0,H_a^1 mean exactly L173(7), with only its first
argument differentiated in H_a^1. Taylor expansion of the actual raw
link samples and (13) gives

    U_(i,fe)=a^2[H^0_(a,i,mu f)(x_e)
                         +a H^1_(a,i,mu f)(x_e)+O_i(a^2)],
    H_a^0-H^0=O_i(a),       H_a^1-H^1=O_i(a).            (15)

Apply L173(17)'s complete-row parity identities with alpha_a and
the frozen H_a^0 separately for every component pair. The stationary
j_e W part of A_ef U_(i,fe), summed over f, is consequently

    a d(x_e) sum_f W_(mu f)
       [beta_(a,mu f) H^0_(a,i,mu f)
                         +alpha_(a,mu f) H^1_(a,i,mu f)]
       +O_i(a^2).                                      (16)

The naively order-one term j_e a alpha_a W H_a^0 is exactly zero
at each mesh. The E part's order-a term is also exactly zero by the
other parity identity. Its remaining complete contribution per row
is O_i(a^2), using (14)--(15) and bounded E. The S part contributes

    a sum_f alpha_(a,mu f) S_(mu f) H^0_(a,i,mu f)
       +O_i(a^2).                                      (17)

No cancellation is assigned to S. Equations (16)--(17) retain exactly
the displacement/adjoint derivative, exterior derivative and prefix
slope of L173(8), including both insertion subtractions.

There are O(a^-4) rows, so the a^3-normalized sum of the O_i(a^2)
remainders is O_i(a). Replacing the three leading finite densities
by those in L173(8) costs O_i(a) after normalization, by (13)--(15)
and their uniform value bounds. The continuum densities have compact
support and bounded first derivatives: H^1 needs at most C^2 exterior
control, while alpha,beta use the fixed smooth displacement/strains.
For each shifted output-edge grid, comparison on each physical cell
of side a gives a total rectangle-rule error O_i(a). There is one
positive edge per output direction per cell; no orientation or color
factor is inserted. Multiplying the densities by the original -6
therefore matches exactly K_(i,T), not its evaluation in L174.

Combining (11)--(17) yields

    |a^3 T_i-K_(i,T)|
       <= C_i [r_N+a+a^5 log(eN)] <= C_i r_N.            (18)

Since a^-3=N^3/512, (18) proves both claims in (2). Also
log(eN)>=1, so the requested log(eN)^2 budget follows directly.

### Qualifications

The exact Hessian/gauge collapse has already retained all action faces
and the forest upper jump before compact residual support restricts
the endpoint pairs used in (3)--(10). No forest field is continued
through its pinned upper value. Neither constant edge modes nor any
source/end rows are cut from the scalar spectral estimates. Full heat
sums are controlled in (11),(13),(15) before row counting. The outside
-6 is used once, with a one-color U_i, and no quartic factor twelve.

The sole intermediate approximation parameter T is chosen in a
uniform finite estimate with an explicit error, rather than inserted
into a qualitative fixed-time limit. The entire complementary quadrant
is controlled by (7)--(8), and the locally logarithmic scalar is removed
only through (11). Frozen parity removes E and W only in their complete
principal rows. There is no signed growth or full-response cancellation
claim. The separate audit below checks these tail and normalization
steps relative to the stated imports.

### 4. Separate critical audit, 2026-10-20

**Verdict: accepted relative to the imported premises.** This audit uses
the pre-existing EXPLORE assessment
`drafts/literature/2026-10-20-action-hessian-branch-rate-critical-audit.md`.
It checks (2) against exactly L173(8), without evaluating that coefficient
or recursively auditing the Hessian collapse and all upstream estimates.
L173's scalar representation and global heat bounds, L156(8)--(9),
L028's centered coefficient calculus and the separately audited L254(18)
are premises. The latter retains L222/L248's qualifications. No different
covariance estimate or quartic normalization is transferred from L254.

**Full complementary time region.** The substitution u=v+w has Jacobian
one and transforms the quadrant to 0<=v<=u. Thus the axial difference
majorant on u>T integrates exactly, apart from its constant, to

    integral_T^infinity log(1+u)(1+u)^(-3/2) du
      =2 log(1+T)/sqrt(1+T)+4/sqrt(1+T).

For the transverse difference the corresponding integral is

    integral_T^infinity 2(sqrt(1+u)-1)(1+u)^(-2) du
      =4/sqrt(1+T)-2/(1+T).

Both formulas hold for T>=0. In particular v need not be large, and
no part with small axial time and large transverse time is omitted.
The finite and infinite bounds apply separately in either argument.
Every endpoint chain has bounded length, so their constants are uniform
over the compact residual rows. These bounds concern differences only;
neither logarithmically divergent infinite potential is integrated alone.

**Polynomial paths and explicit heat error.** The axial norm is at most
4 and the transverse norm at most 12, including Dirichlet end diagonals;
M=12 bounds both finite and infinite operators. Reduce delta once to
cover every endpoint and the bounded chains. For sufficiently large N,
m=floor(delta N/2) leaves a positive clearance beyond all length-m paths.
Diagonal steps in a matrix power do not increase its range. Consequently
each required local entry of every power through degree m agrees on the
finite and infinite spaces. No restriction on an inverse's source rows
is involved in this identity.

For t<=m/(8eM), the factorial estimate gives

    exp(Mt)(Mt)^(m+1)/(m+1)!
      <=exp(m/(8e))[m/(8(m+1))]^(m+1)
      <=exp(m/(8e))8^(-(m+1))<=exp(-m).

The final inequality follows from log(8)-1/(8e)>1. Heat contraction
bounds each exact entry by one. The finite/infinite product error is
therefore <=4 exp(-m), and its endpoint difference <=8 exp(-m).
Integration over the triangle of area T^2/2 costs at most
4 T^2 exp(-m) per chain step. With m and T proportional to N, this
is below C N^(-1/2)log(eN). Combining both tails with this estimate
proves (4) uniformly; it does not substitute a growing time into a
qualitative convergence assertion.

**Local covariance and scalar contraction.** L173(9)--(11) bounds each
transverse Green correction difference by O(N^-2). Its factor j_e<=N
therefore costs O(N^-1). Its reference value b_e=O(N^-1) stays in
eta_e, together with alpha_e=O(log(eN)). Summing the four endpoint pairs
gives precisely (10): four copies of eta_e, the stationary W, the
odd slope S, and the even array E containing the subtracted potential
and the absolute-value kink. No endpoint average replaces that sum.

For each fixed e, eta_e multiplies the exact row identity (11); it is
not commuted through A. L156(8)--(9) and the interior exterior-column
bound give an absolutely summable mode envelope for a^6 per row.
Thus the scalar is O(a^2 log(eN)) before normalization and
O(a^5 log(eN)) after multiplying by a^3. The other local error is
bounded by a^3 times O(a^-4) rows times O(a^-1) times O(a^2) r_N,
which is O(r_N). The fixed number of stencil entries, four endpoint
pairs and outside -6 change only the constant. These counts do not
assume a uniformly bounded raw forest covariance.

**Exterior, frozen parity and all three densities.** L173(6) and
L156(8) identify exactly the columns and covariance-normalized probe
matrix used in L254(18). Its separate exterior audit includes raw
transverse midpoint quotients, the constant axial primitive, both probe
polarizations, derivatives in the two arguments, and omitted labels
in the full polynomial-Gaussian heat sum. Hence (13) applies here
with U_(i,fe)=a^2 H_(i,a,nu(f) mu)(x_e+a r_f,x_e).
Taylor's theorem differentiates only the first argument. Its error
inside the brackets in (15) is O(a^2); the comparison of its linear
jet uses the C^1 portion of (13), and quadrature uses C^2.

L028 gives O(a^2) coefficient errors in each fixed C^r norm. The finite
linear row maps in L173(3)--(4) preserve these errors, including the
adjoint coefficient derivative and both insertion forms, establishing
(14). At each mesh, alpha_a is the same constant-displacement frozen
row to which L173(17) applies. Inversion permutes the complete stencil
within each component, making alpha_a odd and W,E even. The frozen
H_a^0 depends on the component but not the offset. Both leading sums
therefore vanish exactly before any continuum substitution. S is odd
and remains; no parity claim removes its product with alpha_a.

Using j_e=d/a, the surviving per-row products are exactly

    a d beta_a W H_a^0,
    a d alpha_a W H_a^1,
    a alpha_a S H_a^0.

All other products from these expansions, including the remaining E
terms, are O(a^2) per row. For example the stationary product of the
O(a) residual remainder, the O(a^2) exterior and j_e=O(a^-1)
is O(a^2); its exterior Taylor remainder gives the same order.
The two insertions enter through beta_a with their original minus
signs. There is no additional derivative of the second exterior
argument or deletion of the prefix slope.

Multiplying each leading row by a^3 gives the volume weight a^4.
Each output direction has one positive edge per shifted cell, and
the compactly supported densities have uniformly bounded first
derivatives. Cell quadrature thus costs O(a); replacement by the
continuum densities also costs O(a) using (13)--(15). The O(a^2)
row remainder contributes O(a) after the complete row sum. Applying
the original one-color -6 once gives exactly all three terms of
L173(8), with no factor twelve or extra factor three.

The resulting normalized bound is C_i[r_N+a+a^5 log(eN)], as in
(18). Since a=8/N and a^-3=N^3/512, it yields the stated
O(N^(5/2)log(eN)) remainder, below the requested log(eN)^2 budget.
All restrictions to interior endpoints occur after the imported exact
collapse; they do not discard action faces, normal source rows, the
upper jump or constant modes. No unsupported estimate or normalization
was found within this relative-premise audit. This verifies an existing
component input, not a new rate or a complete-response theorem.

## Mathlib

Full matching branch remainder and scalar discrete double-heat coverage:
**not checked**; unknown is not absence. Supporting methods are the
bounded self-adjoint spectral theorem, exponential Taylor remainder,
finite propagation of matrix powers, elementary absolutely convergent
integrals, finite-stencil parity and compact-support quadrature.
The exact scalar heat representation and global one-difference bounds
are imported from L173, not inferred from an unread source. Its
quantitative tail and specialization are proved above because neither
the general scalar rectangle spectrum nor the cited Ward/flow results
state this forest-branch estimate. The saved
[SPECIALIZE assessment](../drafts/literature/2026-10-20-action-hessian-branch-quantitative-remainder.md)
records the inspected primary inputs and scope exclusions. No new
external theorem is imported and no general scalar theorem is reproved.
