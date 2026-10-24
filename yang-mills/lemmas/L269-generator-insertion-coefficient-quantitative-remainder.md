# L269 — Quantitative generator insertion coefficient comparison

## Hypotheses

Use exactly L119(2)--(3)'s kernels B_(r,j,m), output derivatives
v_(r,t,m), finite insertion V_N and L120(1)--(3)'s q kernels,
continuum exterior coefficients and coefficient K_(i,V). Retain their
lower-vertex index and finite-shift conventions. The setting is SU(2),
the relative all-face fixed-link cube D=(-4,4)^4, sufficiently fine
admitted even N, a=8/N, tau=1/16, the straight lower-rooted direction-1
forest, ordinary stored coordinates and the bare small-coupling
expansion taken at each fixed mesh before refinement. Both actual
probes i=3,6 and both residual forms are unchanged.

Keep the finite middle projection in
Z_(kl;st)=F_l(s)^T P F_k(t), min(s,t), both coefficient levels,
every shifted generator/path stencil and both orientations. All
source, output and normal/end rows, the upper pinned jump, constant
axial modes and complete heat sums remain in the starting expression.
The imported analytic and audit qualifications remain; this is not
an audit of those inputs.

The quantitative inputs are L267(1)'s full shifted energy-kernel
decay, L114(2)'s fixed-clearance projection-row estimate, L248(3)--(8)
and (10)--(11)'s raw interior mode and complete heat-matrix estimates,
and L222(5)'s compact rectangle-quadrature bound. L113 supplies the
exact path decomposition used in L120. No rate is imported from
L120's qualitative limit or from L268's different first-order error.

## Conclusion

For both actual probes there are constants independent of sufficiently
fine admitted N such that

    |V_N-a^(-3) K_(i,V)| <= C_i N^(5/2).                     (1)

In particular this meets the approved N^(5/2)log(eN)^2 threshold.
The coefficient is exactly L120(3), with its physical lower-distance
weight, original output derivative and no outside factor 3. It is
not L179's K_(i,Vmix). No coefficient evaluation or sign is asserted.

This is local RESEARCH / REPRODUCTION under the prior SPECIALIZE
assessment
`drafts/literature/2026-10-24-generator-insertion-coefficient-quantitative-remainder.md`.
The separate critical audit in proof section 7 accepts this specialization
relative to its imported premises. Combined with the separate L268 reduction it can supply the
generator-displacement component rate; the other three transverse-H
coefficient remainders, full quantitative L011 assembly, upstream
audits and interacting/continuum/infrared construction remain open.

## Proof

### 1. Uniform joint tails and clipped coefficient moments

Throughout this proof the finitely many r,m,alpha,beta and stencil
shifts have constants independent of N and of exterior mode labels.
Write rho=|d| and M=1+|j|. L119(2) is the exact finite sum

    B_(r,j,m)(d)=sum_(h,q) (d_m+h_m) A_r(h) C_r(q)
                                                    e_j(d+h+q).

The fixed shifts and L267(1) imply, at every d,j including zero,

    ||B_(r,j,m)(d)||_F <= C (1+rho)/(M+rho)^4.              (2)

Indeed 1+sqrt(j^2+|d+h+q|^2) is bounded below by a fixed positive
multiple of M+rho, uniformly over the finite shift list, and
|d_m+h_m|<=C(1+rho). Thus no scalar asymptotic remainder is
differentiated and no component or reversed mixed entry is omitted.

There are at most C(n+1)^2 spatial lattice points with n<=|d|<n+1.
Consequently, with all norms below over Z^3 and Frobenius entries,

    ||B_j||_2^2 <= C sum_(n>=0) (n+1)^4/(M+n)^8 <= C M^(-3),
    ||(1+|d|)B_j||_2^2
                <= C sum_(n>=0) (n+1)^6/(M+n)^8 <= C M^(-1).
                                                               (3)

Here and below an unlabelled B_j denotes any one of the original
B_(r,j,m), with a common constant. To verify both series estimates,
put u=n+1. For u<=M bound the denominator below by M^8 and sum
u^p, p=4 or 6. This gives C M^(p-7). For u>M use M+n>=u and
sum u^(p-8), whose first term plus integral is C M^(p-7).
The estimates include M=1 and require no asymptotic interchange.

For real R>=2 the omitted spatial norm also satisfies

    ||1_(|d|>R) B_j||_2 <= C(M+R)^(-3/2).                 (4)

In fact its square is bounded by the same p=4 series restricted to
n>=floor R. Since n+1<=M+n, that series is at most
C sum_(n>=floor R)(M+n)^(-4)<=C'(M+R)^(-3).
Taking the complete signed axial sum in (3)--(4) proves

    sum_(|j|>J)||B_j||_2 <= C(1+J)^(-1/2),
    sum_(j in Z)||1_(|d|>R)B_j||_2 <= C(1+R)^(-1/2),
    sum_j ||B_j||_2 <= C.                                (5)

These are uniform finite inequalities, prior to any choice of J,R.

Define w_a(d)=min(1,a(1+|d|)), 0<a<=1. Using the two bounds in
(3) separately gives

    ||w_a B_j||_2 <= C min(M^(-3/2),a M^(-1/2)).           (6)

Split the signed j sum at M=ceil(1/a). The part below this threshold
is bounded by C a sum_(M<=ceil(1/a)) M^(-1/2)<=C sqrt(a);
the complementary sum of M^(-3/2) is also at most C sqrt(a).
Likewise min(1,a|j|)||B_j||_2 is bounded by the right side of (6).
It follows that

    sum_j ||min(1,a(1+|d|)) B_j||_2 <= C sqrt(a),
    sum_j min(1,a|j|)||B_j||_2 <= C sqrt(a).               (7)

The square root of the second moment in (3) alone is not summable
in j. Both sides of the clipped bound (6) are essential. These are
joint energy estimates, not the factorwise first absolute moments
excluded by L109.

L120(14) imports ||q_(alpha,beta)||_(ell^2,F)<=C from the bounded
symbol (S_alpha^inf)^* P_inf S_beta^inf. For every nonnegative
scalar w(d), spatial Cauchy--Schwarz therefore gives

    sum_d w(d)|tr[B_j(d)q_(alpha,beta)(-d)]|
                                           <= C ||w B_j||_2. (8)

Equations (5)--(8) control the full closed kernel product, its
spatial/axial tails and the coefficient changes needed below. The
projection q is never assigned a separate first absolute moment.

The primary scalar theorem underlying (2) is imported through L267:
Lawler--Limic, *Random Walk: A Modern Introduction* (2010),
Theorem 4.3.1, printed pp. 81--83, in the
[author-hosted text](https://www.math.uchicago.edu/~lawler/srwbook.pdf#page=81).
Its symmetric finite-range irreducible four-dimensional simple-walk
case includes the bipartite lattice. L267 verifies H=G_walk/8 and
the complete matrix differences. We use that established
specialization, without reproving the scalar theorem or replacing
any finite relative link covariance by a scalar Dirichlet kernel.

### 2. Separate remote rows at fixed physical clearance

Choose eta>0 such that the supports of every v_(r,t,m), viewed as
samples of partial_m u_(rho(r)), have distance at least eta from
every face of D. Fix a positive c with 8c<eta/4 and c<1/4.
Set J_N=R_N=floor(cN). Increase the eventual mesh threshold so
these radii exceed 2 and all fixed path stencils have physical
radius less than eta/4. Let V_N^near be L119(3) with B replaced by

    1_(|j|<=J_N) 1_(|d|<=R_N) B_(r,j,m)(d).

By (5), L119's Theta(J_N,R_N) is at most C_c N^(-1/2).
Its uniform trace estimate L119(6), with aN=8, hence gives

    |V_N-V_N^near| <= C_i N^(5/2).                       (9)

This step estimates the entire remote contribution in the original
finite trace. It retains every finite middle-projection input and
all original levels, upper/end rows and heat labels in the norm.
No raw forest value at a remote row has been replaced or smoothly
extended. Constants in (5) and in L119(6) are uniform before the
choice J_N,R_N; this is not a varying-cutoff application of L120's
fixed-cutoff qualitative theorem.

Whenever v_(r,t,m)(x) is nonzero and |j|<=J_N, |d|<=R_N,
both physical points (xi_t,xi_x) and (xi_(t-j),xi_(x-d)), together
with all adjacent path stencils, lie in a single fixed compact
subset of D with clearance at least eta/2 after decreasing the
clearance constant if necessary. In particular s=t-j is an
admitted interior level. All plane grids and path columns at these
points are genuine interior ones. This uses only the prescribed
displacement derivative support and the two explicit cutoffs.

### 3. Replace the finite projection without a cutoff loss

Put W_(t,j)=J^* M_(v_(r,t,m)) B_j^near J. Replacing P by
P_bulk=J_1^*P_inf J_1 only in V_N^near gives a trace denoted
V_N^near,bulk. For each heat pair, the difference is exactly

    Tr[F_k(t) W_(t,j) F_l(s)^T (P-P_bulk)].              (10)

All input edges of F_k W F_l^T lie in the fixed interior set from
section 2. Thus it equals its right multiplication by an interior
edge selector R_Omega. L114(2) applies to R_Omega(P-P_bulk),
with a clearance independent of N,J_N,R_N and the heat labels.
Every input edge of that projection difference is still present.

L119(16), the actual F operator bounds in L120(5), and trace
Cauchy--Schwarz give for (10)

    C a^2 p(k)p(l) N^(3/2) ||B_j^near||_2 log(eN)^(3/4).

Here p can be enlarged to a fixed polynomial. Neither the number
of retained d nor a kernel l1 norm enters the estimate: it is the
complete row l2 norm, followed by two bounded F factors. For each
j the sum of min(t-j,t) over allowed t is at most N^2. Sum (5)
and the complete Gaussian heat envelope from L120(6)--(7) to obtain

    |V_N^near-V_N^near,bulk|
                 <= C_i a^2 N^(7/2) log(eN)^(3/4)
                  = C_i' N^(3/2) log(eN)^(3/4).          (11)

There is no outside a^(-1) in V_N. The estimate has the same count
as L120(9), now with an explicitly uniform support clearance and
sum_j ||B_j^near||_2<=C. The nonlocal projection output is not
made compact, and no small projection operator norm is assumed.

### 4. Match and freeze the original two exterior coefficients

L113's exact F_k(t)=a sum_alpha S_alpha M_(phi_(k,alpha,t))
and the interior support from section 2 give the exact expression

    V_N^near,bulk
      =a^2 sum_(k,l,r,m,alpha,beta,j,t,x,d)
          c_(i;kl,a) min(t-j,t) v_(r,t,m)(x)
          phi_(l,alpha,t-j)(x-d) phi_(k,beta,t)(x)
          tr[B_(r,j,m)(d)q_(alpha,beta)(-d)].             (12)

The j,d sums in (12) are restricted by J_N,R_N; the original level
and spatial grids remain. This is L120(11) with its full matrix
order, all component selectors and argument -d. We have not used
L113's scalar-collected approximation or commuted a coefficient
through P. When multiplied by v, the t sum can be written as the
entire interior t grid for every retained j, since s=t-j is then
automatically interior. The same observation permits the common
interior vertex grid for x; all other values of v vanish.

For a retained mode label k, L248(4)--(8) applies at every sample
in this fixed compact region. It gives the raw, unaveraged path
coefficient estimate

    |phi_(k,alpha,t)(x)-phi_(k,alpha)(xi_t,xi_x)|
                                                      <= C a p(k),
    |phi_(k,alpha,t)(x)|+||phi_(k,alpha)||_(C^1(K)) <= C p(k).
                                                               (13)

Here K is a fixed interior box containing the region and all
segments between its sampled points. The continuum coefficients
are exactly L120(2). The path signs are b: V_mu+V_nu and
q: -V_mu+V_nu: L248 explicitly checks all four raw traversal
slots, including the shifted second and third edges. This import
concerns those supporting estimates, not L248's reverse-trace
conclusion. Its direct and prefix samples require no upper-face
extension. Its estimates are uniform on any such fixed compact
box: the displayed prefix sums have length at most 8 and their
mode derivative bounds are uniform there, independent of the
number of retained cells. Constant component-1 axial modes and
the entire lower prefix are included.

Using the value and C^1 bounds in (13) separately, the difference
between the product of raw coefficients in (12) and

    phi_(l,alpha)(xi_t,xi_x) phi_(k,beta)(xi_t,xi_x)

is bounded by

    C p(k)p(l) [a + min(1,a(|j|+|d|))].                 (14)

Indeed first match each raw value to its own continuum point,
costing C a p(k)p(l), then change only the l point by the
physical displacement (-aj,-ad). The mean value estimate and the
independent value bound give the minimum in (14). Both points
and their segment lie in K; no smoothness of a rough kernel or
of the forest upper jump is invoked. Increasing p covers every
mode degree. Since min(1,a(|j|+|d|)) is at most
min(1,a|j|)+min(1,a(1+|d|)), (7)--(8) bound its complete j,d
kernel sum by C sqrt(a). The additional a term costs C a.

Define V_N^frozen by this product replacement in (12), keeping
c_(i;kl,a), the cutoffs and min(t-j,t) unchanged. There are O(N^4)
t,x points and min(t-j,t)<=N. The complete heat sum with the
enlarged polynomial p is finite uniformly in N. Therefore

    |V_N^near,bulk-V_N^frozen|
               <= C_i a^2 N^5 [a+sqrt(a)]
               <= C_i' N^(5/2).                         (15)

All j,d sums were bounded before the t,x count. There is no
additional axial-pair factor after (7). This is where joint
decay, rather than the separate forbidden absolute moment, pays
for changing the second coefficient's point and level.

### 5. Retain the lower-distance weight, heat sum and quadrature

Let beta^R_(r,j,m;alpha,beta) be the d sum in L120(3) restricted
to |d|<=R_N, and zero for |j|>J_N. Equations (5),(8) give a
uniform bound on the sum of its absolute values. After multiplying
V_N^frozen by a^3, its physical cell weight is precisely

    a^5 min(t-j,t)=a^4 [at-a max(j,0)].                  (16)

Write x_1=-4+at. Replacing the bracket by x_1+4 costs at most
C min(1,a|j|) on the retained range (in fact a|j|<8c<2).
Equations (7)--(8), the O(1) total a^4 cell volume and the full
heat bound show that this normalized weight error is at most
C_i sqrt(a). Thus no diagonal/axial half-weight or factor of 8
is created or removed. The min kink is estimated explicitly.

For retained labels L248(10)--(11), for each i=3,6, gives

    |c_(i;kl,a)-c_(i;kl)|
        <= C_i a (1+|k|+|l|)^4 exp[-c_0(|k|^2+|l|^2)],
    |c_(i;kl,a)|+|c_(i;kl)|
        <= C_i exp[-c_0(|k|^2+|l|^2)], c_0=tau/16.      (17)

Both complete matrices are meant here: the triplet average of four
curvature squares and both shear polarizations, with all original
weights. The same physical normalization is used in L120(2).
Polynomial mode bounds and sum |beta^R|<=C make the error from
(17) at most C_i a in the normalized expression. Extend the
retained label set to the full continuum set. Every omitted label
has |k|>=N or |l|>=N; its polynomially weighted Gaussian tail is
at most C_i exp(-c_1 N^2), after decreasing c_1>0. To see the
uniform bound, extract exp(-c_0 N^2/2) on that set and sum the
remaining polynomial times exp[-c_0(|k|^2+|l|^2)/2] over the
full component-labeled integer set. This includes all permitted
constant indices and has no finite-mode approximation premise.

For each heat pair and finite stencil label put

    g_(kl;r,m,alpha,beta)(x)
      =(x_1+4) partial_m u_(rho(r))(x)
                         phi_(l,alpha)(x) phi_(k,beta)(x).

This function is smooth and compactly supported in D, with C^1
norm at most C p(k)p(l) for a fixed polynomial. L222(5) bounds
its complete a^4 rectangle-quadrature error by C a p(k)p(l).
Multiplying by beta^R and c_(i;kl), and taking the complete sums,
costs at most C_i a, uniformly in the N-dependent cutoffs because
their absolute kernel sum is uniformly bounded. The endpoint cells
are part of this estimate; no forest value is sampled at the upper
pin. The resulting integral is precisely L120(3) with beta^R.

Finally (5),(8) bound the difference between this truncated
functional and K_(i,V) by C_i N^(-1/2). The spatial and axial
tails here are full infinite tails; in particular they include
offsets beyond every finite level range. Absolute convergence from
these same estimates and the Gaussian envelope justifies all the
reorderings. Combining (16)--(17), quadrature and coefficient tails,

    |a^3 V_N^frozen-K_(i,V)|
                 <= C_i [sqrt(a)+a+N^(-1/2)]
                 <= C_i' N^(-1/2).                      (18)

The quadrature input is the standard first-order Taylor rectangle
bound already specialized in L222. Its precise calculus source is
NIST DLMF, version 1.2.8, section 1.4(vi),
[(1.4.35)--(1.4.37)](https://dlmf.nist.gov/1.4#vi).
The smooth compact functions above satisfy its closed-segment
derivative hypotheses. No reproof of Taylor's theorem, new primary
source or qualitative-limit rate inference is needed.

### 6. Combine the complete error budget

Restore a^(-3) in (18), and telescope only the comparisons actually
made in (9), (11), (15) and (18). Their unnormalized allowances are

| Comparison | Complete bound |
| --- | --- |
| Remote spatial and axial rows of the original V_N | C_i N^(5/2) |
| Finite middle projection on retained adjacent rows | C_i N^(3/2)log(eN)^(3/4) |
| Raw two-point/two-level exterior matching and freezing | C_i N^(5/2) |
| Physical min weight and infinite coefficient tails | C_i N^(5/2) |
| Complete heat matching, omitted labels and quadrature | C_i N^2 |

For N>=1, log(eN)<=N, so the projection allowance is also below
C_i N^(5/2). A common sufficiently fine threshold for both probes
and the finite list of stencils proves (1). The physical relation
aN=8 is retained throughout; the coefficient has neither an extra
outside 3 nor an unaccounted cell-volume factor.

All cutoff-dependent estimates were uniform finite bounds before
R_N,J_N were chosen. Remote rows were controlled in the original
finite expression, before raw matching. Projection inputs were
never cut down. Only the already compact derivative support and
near offsets localized adjacent path columns. No nonlocal output
was assumed compact, no upper prefix jump was smoothed, and no
factorwise absolute projection/path moment was used. L268 was not
used to prove this independent coefficient comparison. The result
is a quantitative standard-method specialization, not a claim of
originality beyond the inspected sources, an upstream audit, a complete
L011 remainder or a Yang--Mills candidate.

### 7. Separate critical audit — 2026-10-24

**Verdict: accepted relative to the stated imported premises.** This
RESEARCH / REPRODUCTION proof_audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-24-generator-insertion-coefficient-rate-critical-audit.md`.
No correction, stronger estimate or new direct mathematical input is
needed. The audit checks the quantitative specialization against the
original L119 insertion and exactly L120(3); it does not recursively
audit the imported Green, projection, mode or contraction results.

**Full shifted kernels and clipped moments.** For every fixed h,q, the
ratio (1+|j|+|d|)/(1+sqrt(j^2+|d+h+q|^2)) is bounded, including
when the shifted argument is zero. Thus L267(1) gives (2) for the
full Frobenius kernel. Shell multiplicity O((n+1)^2) and the squared
linear numerator give the powers 4 and 6 in (3). Splitting at n+1=M
gives M^(-3) and M^(-1), respectively. The tail is bounded by
C sum_(n>=floor R)(M+n)^(-4), hence its norm is O((M+R)^(-3/2)).
Its full signed axial sum is O(R^(-1/2)); the axial tail of the
unweighted norm is O(J^(-1/2)). All these bounds are uniform.

Both inequalities w_a<=1 and w_a<=a(1+|d|) are necessary in (6).
Below M=ceil(1/a), the sum a sum M^(-1/2) is O(sqrt(a)); above it,
sum M^(-3/2) is O(sqrt(a)). The same split controls the axial
weight. This verifies (7), including a=1 and j=0. The product
estimate (8) uses |tr(Bq)|<=||B||_F||q||_F and L120(14)'s full
ell2 norm of q. It assumes neither a first absolute moment of q
nor summability of the weighted norm M^(-1/2) alone.

**Original remote trace and clearance.** L119(6) is a uniform finite
inequality, not merely its subsequent ordered limit. Its proof uses
an N^(3/2) row-count factor in each of two Hilbert--Schmidt norms, a^2 from
the exterior paths, and at most N^2 for the weighted t sum at fixed j.
Thus the unnormalized remote allowance is C_i a^2 N^5 Theta(J,R).
With J=R=floor(cN), the preceding tails give O(N^(5/2)).

If v(t,x) is nonzero, its physical point has clearance eta.
Each retained offset moves a coordinate by at most 8c<eta/4;
every adjacent fixed stencil eventually moves it by less than eta/4.
Both points and their path edges therefore have clearance eta/2.
A fixed interior box contains their joining segments. In particular
t-j and x-d are existing interior indices on all required grids.
All remote/end rows were counted before any raw value changed;
there is no interpolation of the upper pin or varying-cutoff use
of L120's qualitative theorem.

**Projection side and all inputs.** Let A=F_k W F_l^T. Its input edges
lie beside the compact input plaquettes of W, so A=A R_Omega.
The exact cyclic error Tr[A(P-P_bulk)] is bounded by
||A||_HS ||R_Omega(P-P_bulk)||_HS. The selector acts on projection
output rows, leaving every finite input edge. L114(2) applies with
O(N^3) rows and the fixed clearance above. The full row estimate is
||A||_HS<=C a^2 p(k)p(l)N^(3/2)||B_j^near||_2.
After the min weight and full heat sum the error is therefore
C_i a^2 N^(7/2)log(eN)^(3/4) sum_j||B_j^near||_2,
which is O(N^(3/2)log(eN)^(3/4)). No number of retained spatial
offsets or extra a^(-1) occurs. Projection output is not assumed
compact, and covariance inputs are not restricted.

**Exact paths and both raw points.** L113 gives F_k=a sum S_beta M_phi
exactly, before scalar collection. Expanding Tr[W F_l^T P_bulk F_k]
puts the l coefficient at y=x-d and the k coefficient at x, with
the closed product B(d)q_(alpha,beta)(-d). Both adjacent S columns
are fully present by clearance. This verifies (12), its argument
-d, and the finite component selectors and signed path order.

L248(3)--(8) uses a length-at-most-8 midpoint prefix and its one-sided
transverse quotient, with stored mode column a A_(k,a). Its displayed
bounds apply on the enlarged fixed interior box. The four signed
raw slots are +mu at x, +nu at x+e_mu, -mu at x+e_nu, -nu at x;
their path sums match V_mu+V_nu and V_nu-V_mu, exactly L120(2).
Independent raw value and polynomial error bounds, and polynomial
continuum C^1 bounds, justify first matching both points at cost
C a p(k)p(l), then moving the l point at cost
C p(k)p(l)min(1,a(|j|+|d|)). Only smooth continuum coefficients
on the closed segment receive the latter estimate. Equations
(7)--(8) bound the complete kernel sum by O(sqrt(a)), before the
O(N^4) cells and min(s,t)<=N are counted. Thus (15) is
O(a^2 N^5 sqrt(a))=O(N^(5/2)), with no second axial-pair count.

**Complete heat matching and normalization.** L248(10)--(11) compares
the same complete matrices as L120: all four triplet products with
their 1/4 and both shear polarizations with their 1/2. Independent
value and polynomial error envelopes justify the full heat sum.
Own-direction zero indices remain; the component-1 prefix retains
the physical lower distance, while other components have zero
component-1 prefix. Any omitted mesh label has a component index
at least N. Extracting half its Gaussian exponent proves the
exponential omission bound with the remaining polynomial summable.

After cubic normalization the exact prefactor is
a^3 a^2 min(t-j,t)=a^4[at-a max(j,0)]. On the retained range
a|j|<=8c<2, so the weight change is at most 2 min(1,a|j|).
Its complete sum is O(sqrt(a)) by (7)--(8). The frozen compact
integrand has polynomially bounded C^1 norm, so L222(5) applies
to the full interior vertex sum, including all endpoint cells.
The absolute beta^R sum is uniformly bounded; thus quadrature
and heat matching each cost O(a), with no cutoff loss. Restoring
the infinite tensor costs O(N^(-1/2)). The integral is exactly
L120(3): x_1+4, the original output derivative, and no new half,
color, factor 8 or outside factor 3.

The five allowances in section 6 are therefore valid and counted
once. Multiplying the normalized O(N^(-1/2)) error by
a^(-3)=N^3/512 gives O(N^(5/2)); the projection and O(N^2)
heat/quadrature errors fit the same threshold. A common mesh
threshold suffices for both probes and all fixed stencils.
This accepts (1) as a local standard-method input, without claiming
novelty beyond the inspected sources. The precise Lawler--Limic and
DLMF citations and specialization limits above are reused; no fresh
source retrieval or reproof is claimed. L268 remains a distinct
reduction. The other three coefficient rates, quantitative L011
assembly and interacting/continuum/infrared construction remain
unresolved. There is no mass-gap or complete-response conclusion.

## Mathlib

Full matching generator insertion coefficient-rate theorem: **not
checked**. Supporting discrete Green decay, Fourier Plancherel,
Hilbert--Schmidt trace inequalities, clipped series estimates and
rectangle quadrature: **not checked**. Unknown availability is not
absence. No numerical diagnostic or mathematical script supplies any
part of this proof; section 7 records the separate critical audit.
