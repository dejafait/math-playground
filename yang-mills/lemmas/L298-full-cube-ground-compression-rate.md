# L298 — Quantitative ground compression on the full relative cube

## Hypotheses

Retain exactly L297's SU(2) relative cube, even N>=2, a=8/N,
counting measure, boundary-contained links pinned, boundary-fixed
gauges, every variable normal link at both endpoints, and the ambient
Wilson jets and complete density on L280's own slice. In particular
there are no added longitudinal Gaussian variables or counterterms.
All operators in this result are at zero sources. The exact reflected
bump and source hypotheses of L297 are retained for the stated possible
application, but no source derivative estimate is strengthened here.

Use L003's tensor grids and L280's unscaled incidence matrices B,C,
Delta=B*B and L=C*C+BB*. On the fixed transverse space H=ker B*,
Q is the orthonormal inclusion used by L297. P_N is its rank-four
one-color ground projection, with lambda_0=12 sin^2(pi/(2N)).
The one-color operator W_N^(0) is precisely L297(7),(18):

\[
 W_N^{(0)}=Q^*(D_N+\tfrac14\mathcal E_N
                         -\tfrac14\mathcal A_N)Q,
 \quad \mathcal E_N=\mathcal E(T,T;G,G),\quad
 \mathcal A_N=\mathcal A(U;G),\quad G=QL_H^{-1}Q^*.
 \tag{1}
\]

Here L_H=Q*LQ; the notation on the right of (1) suppresses the
external color identity only. All internal color contractions and
Wilson factors are retained. D_N includes Haar and both determinants.
Use L282's complete-density formula and constant, L283's local
quartic contraction and constant, L287's exact internal/external-curl
split and energy bounds, L289's constant-field Wilson algebra and
identity I_1=Z_0/2-1/16, and L297(17)'s ground-space error for that
split. Their upstream hypotheses remain assumptions of this result.
No one-face replacement, L291 cancellation, or unproved quantitative
boundary theorem is an input.

## Conclusion

With ell_N=log(eN), there is a constant independent of even N such that

\[
 \boxed{\quad
 \|P_NW_N^{(0)}P_N\|
       \le C\left(N^{-1}+N^{-1}\sqrt{\ell_N}
                              +N^{-2}\ell_N\right).
 \quad}                                                     \tag{2}
\]

In particular the requested O(N^-1 log(eN)^2) bound holds. The
density, contracted quartic and internal-curl compressions each differ
from their respective bulk constants by O(N^-1). The external-curl
error is retained; it is not asserted to have this latter rate.

This is a local quantitative development within the saved EXPLORE
assessment, not a claim of originality beyond the sources checked.
The separate conceptual audit in section 6 accepts the mixed-grid
heat comparison and complete boundary row sums under the stated
upstream inputs. It is not a complete Yang--Mills candidate.
Other one-heat-line residues and source
derivatives, the full tail, higher perturbative remainder, interacting
reflection lower bound, continuum sector/axioms and positive
infinite-volume mass remain unresolved.

## Proof

### 1. A heat comparison on the actual tensor grids

Translate and rescale lattice coordinates to [0,N]^4; all operators
in this proof are unscaled counting-measure matrices, so their scalar
Fourier symbol is lambda(q)=4 sum_mu sin^2(q_mu/2). Distances below
are in these lattice units between the actual cell centers. All
constants may depend on fixed cell orientations and finite stencil
sizes, never on N. Pinned cells are extended by zero when they occur
in an incidence stencil.

Here is the elementary heat estimate needed for this particular
mixed-grid specialization. It is proved explicitly because neither
a scalar Dirichlet estimate nor L282/L289's fixed-polynomial limits
supply this specialization. Let

\[
 p_t(z)=\int_{[-\pi,\pi]^4}e^{iq\cdot z-t\lambda(q)}
                         \frac{dq}{(2\pi)^4},\qquad z\in\mathbb Z^4.
\]

For any fixed composition delta^j of j forward/backward differences,
0<=j<=2, and every integer K>=0,

\[
 |\delta^j p_t(z)|\le C_{j,K}(1+t)^{-(4+j)/2}
                (1+|z|/\sqrt{1+t})^{-K}.                    \tag{3}
\]

To verify (3), its difference multiplier m(q) is a product of j
factors exp(plus/minus iq_mu)-1, up to a fixed translation. Near
zero, |partial^beta m(q)|<=C_beta |q|^{max(j-|beta|,0)}.
Also lambda(q)>=4|q|^2/pi^2 on the integration cube. For t>=1,
the product rule, |partial lambda|<=C|q| and bounded higher
derivatives give, for every multi-index alpha,

\[
 \int|\partial^\alpha(m(q)e^{-t\lambda(q)})|dq
       \le C_\alpha t^{(|\alpha|-4-j)/2}.                  \tag{4}
\]

For detail, a derivative of order h of the exponential is bounded
by C_h t^{h/2}(1+sqrt(t)|q|)^h exp(-c t|q|^2), after slightly
reducing c. A term with b derivatives on m and h on the exponential,
b+h=|alpha|, then has integral bounded by
C t^{h/2-(4+max(j-b,0))/2}, which is at most the right side of
(4). For 0<=t<=1 all these derivative integrals are bounded on
the compact Fourier cube. The zero-derivative estimate and integration
by parts K times in a coordinate with largest |z_mu| prove (3).
There are no boundary terms: the multiplier is periodic and z is
integer. Fixed shifts of z only change constants. This argument
handles repeated as well as mixed differences.

The exact one-dimensional interval kernels from L003 section 2 are
the following image sums, with p_t^(1) the one-dimensional version:

\[
 \begin{split}
 H_t^D(i,j)&=\sum_{k\in\mathbb Z}
    [p_t^{(1)}(i-j+2Nk)-p_t^{(1)}(i+j+2Nk)],\\
 H_t^E(i+\tfrac12,j+\tfrac12)&=\sum_{k\in\mathbb Z}
    [p_t^{(1)}(i-j+2Nk)+p_t^{(1)}(i+j+1+2Nk)].
 \end{split}                                                \tag{5}
\]

Here 1<=i,j<N for D and 0<=i,j<N for E. One may check (5)
without a boundary theorem: periodize the Fourier integral with
period 2N and subtract/add the reflected point. Pair opposite
frequencies to obtain respectively the sine/sine sum with weights
2/N and the midpoint cosine/cosine sum with weights 2/N, including
weight 1/N for the constant cosine. The frequency N term vanishes
on these sine or midpoint-cosine grids. These are exactly L003's
counting-normalized spectral kernels. In particular D is zero at
both endpoint vertices, while E retains both normal endpoint edges.
The series and their finitely many differences converge absolutely
at each t by (3), or its one-dimensional proof.

For Delta take four D factors; for component mu of L take E in
mu and D in the other three coordinates. Products of (5) are sums
of the four-dimensional p_t over reflected images, with the
appropriate signs. Incidence differences apply directly to these
sums: a difference across an endpoint uses the zero sine value,
and produces the same midpoint-cosine identity as L003. Applying a
curl at the left or right therefore uses the corresponding one or
two differences of the image kernel. Endpoint sums M use the same
zero extension and at most two terms. No continuum normal derivative
or alternative Neumann convention is being substituted.

For 0<=t<=N^2 these image sums have two useful bounds. If R is
the separation of the actual cell centers, the kernel with j
differences has the right side of (3), with R in place of |z| and
a changed constant. If both stencils lie within distance d/8 of a
row whose distance to every face is at least d-1, and d exceeds a
fixed stencil constant, its difference from the full-lattice kernel
has that same bound with d in place of |z|. To see the summation
uniformly, in (5) and its products every image displacement has
length at least the direct separation, up to fixed stencil shifts.
For the difference from the infinite kernel delete its direct,
unreflected image. Every remaining displacement is at least c d
in the stated interior situation. Image points have spacing 2N
in each coordinate with only 16 reflection choices. Since
sqrt(1+t)<=2N, summing (3) with exponent K+6 bounds either image
sum by C times the stated expression with exponent K. One can
group image points in shells of width N: their counts are O((l+1)^3),
and the extra six powers make the shell sum uniform. Stencil shifts
and the finitely many nearest images are absorbed in the constant.

For t>=N^2 use the actual finite-domain modes instead. Each mode
has pointwise magnitude <=4/N^2. Each incidence difference costs
at most C sqrt(lambda_k). All these mode sets have at least three
positive indices for L, or four for Delta, and
4|k|^2/N^2<=lambda_k<=pi^2|k|^2/N^2. Summing by max k gives

\[
 |\delta^j H_{t,N}(x,y)|
       \le C_j N^{-4-j}e^{-c t/N^2},\qquad j=0,1,2.        \tag{6}
\]

More explicitly the sum is bounded by N^-4-j times
sum_{k!=0}|k|^j exp(-4(t/N^2)|k|^2), which is at most
C_j exp(-c t/N^2) for t/N^2>=1. This also controls left/right
mixed differences, since the two differentiated eigenfunctions
give the same total power lambda_k^(j/2). Formula (6) includes
the own-direction zero cosine index; no all-zero one-form mode
exists. M factors change constants only.

### 2. Transverse and density kernels, including their boundary errors

Write Pi_N=B Delta^-1 B* and J_N=M Delta^-1 B*, reserving P_N
for the ground projection. The exact transverse identities are

\[
 \begin{split}
 G_N&=\int_0^\infty
       (e^{-tL}-tB e^{-t\Delta}B^*)dt,\\
 C G_N&=\int_0^\infty C e^{-tL}dt,\qquad
 C G_N C^*=\int_0^\infty C e^{-tL}C^*dt,\\
 J_N&=\int_0^\infty M e^{-t\Delta}B^*dt,\qquad
 \Pi_N=\int_0^\infty B e^{-t\Delta}B^*dt.
 \end{split}                                                \tag{7}
\]

The first is L280's G=L^-1-B Delta^-2 B*. The two curl formulas
use CB=0 before integration. The infinite-lattice kernels are
defined by the same integrals after applying the displayed
differences. In particular Delta_infinity^-2 is never used as an
undifferentiated kernel: its logarithmically divergent diagonal
in dimension four is not an intermediate quantity. Fourier
transformation of the convergent differentiated expressions gives
the full transverse multiplier (I-dd*/lambda)/lambda, with the
raw-edge phases or the equivalent midpoint phases retained.

Integrate (3)--(6) in (7). The elementary bound used for the short
time integral is, for alpha>0 and K>alpha,

\[
 \int_0^\infty(1+t)^{-(\alpha+2)/2}
             (1+R/\sqrt{1+t})^{-K}dt
       \le C_{\alpha,K}(1+R)^{-\alpha}.                    \tag{8}
\]

It follows by splitting at 1+t=(1+R)^2 (or by substituting
sqrt(1+t)/(1+R)). The extra t in G's second term is bounded by
1+t and its two differences therefore give the same alpha=2
as its first term. The finite long-time contributions are bounded
by C N^-2 for G, C N^-3 for CG or J, and C N^-4 for CGC* or Pi.
For example the second term of G has bound
C N^-6 integral_{N^2}^infinity t exp(-ct/N^2)dt<=C N^-2.
The infinite long-time integrals have the same bounds by (3).

Consequently, writing R for the relevant cell separation,

\[
 \begin{array}{c|c|c}
 K & |K_N(x,y)|+|K_\infty(x,y)|
       & |K_N(x,y)-K_\infty(x,y)|\text{ for }R\le d/8\\ \hline
 G & C(1+R)^{-2} & C d^{-2}\\
 CG,\ GC^*,\ J & C(1+R)^{-3} & C d^{-3}\\
 CGC^*,\ \Pi & C(1+R)^{-4} & C d^{-4}
 \end{array}                                                \tag{9}
\]

The comparison column requires an interior row of depth d as in
section 1 and all involved stencils; adjusting the fixed minimum
depth and the factor 1/8 covers all their offsets. The absolute
bounds hold on the entire relative domain. For finite kernels the
long-time contribution is compatible with the first column because
R<=2N+O(1). For the comparison column N^-alpha<=C d^-alpha.
Thus (9) controls the nonlocal transverse part, and is not a scalar
replacement. It also controls all normal end links and intersections
of faces through the exact images and the finite-mode bounds.

### 3. Complete internal pairs and the infinite-lattice constants

Use one external color block. Define the three ambient operators

\[
 K_N\in\{D_N,\mathcal A_N,\mathcal E_N^{\rm int}\},\qquad
 u^*\mathcal E_N^{\rm int}v
      =2\mathbb E[\mathsf B(u;x)\mathsf B(v;x)],
 \quad \mathsf B(u;x)=\sum_p(Cx)_p\cdot D\zeta_p(x)[u].
 \tag{10}
\]

This is the exact internal-curl part of L287; its coefficient is
two, not an additional convention. The finite Gaussian contractions
are those already fixed in L287(13) and L297(6)--(8). The standard
finite Gaussian input is Bauerschmidt--Brydges--Slade,
*Introduction to a Renormalisation Group Method*, LNM 2242 (2019),
[arXiv:1907.05474v2](https://arxiv.org/pdf/1907.05474v2),
Propositions 2.1.6 and 2.1.9 and Corollary 2.1.11, pp. 31--33,
as assessed for L297. Positive semidefinite transverse covariances
satisfy those hypotheses; only polynomial Wick contraction is used.

D_N has precisely L282(6)'s formula

\[
 (D_N)_{ef}=-\tfrac1{12}\delta_{ef}
   -\tfrac16(\Pi_N)_{ee}\delta_{ef}
   +\tfrac14(J_N)_{ef}(J_N)_{fe}.                           \tag{11}
\]

The quartic operator has external and internal slots on a single
plaquette and the uniform finite coefficient sum C_U of L283(9).
For the last operator in (10), expand the two exact local quadratic
vertices and apply the two crossing Wick pairings. Each matrix
entry is a fixed finite sum, with bounded coefficients and bounded
plaquette/slot multiplicities, of terms of the forms

\[
 (CG_NC^*)_{pq}(G_N)_{fg},\qquad
 (CG_N)_{pg}(G_NC^*)_{fq}.                                 \tag{12}
\]

Here p,f are within a fixed distance of the external row edge,
and q,g of the external column edge. The differing field colors
make within-vertex contractions zero as in L287. All actual
plaquette orientations, slot signs and internal color sums are
included. Missing pinned slots delete terms only; the number of
terms for each external pair is uniformly bounded. Thus this is
a bound on complete internal sums, not a choice of one contraction.

Define K_infinity by these same local formulas and the full-lattice
kernels. From (9), (11), (12) and locality of the quartic,

\[
 |(K_N)_{ef}|+|(K_\infty)_{ef}|
       \le C(1+|x_e-x_f|)^{-6},\qquad
 \sup_e\sum_f(1+|x_e-x_f|)|(K_N)_{ef}|\le C.              \tag{13}
\]

The first bound includes the bounded local terms by enlarging C;
it also holds for K_infinity. The second follows since at most
C(1+r)^3 edge centers lie in a unit shell of radius r in dimension
four, and sum_r (1+r)^3(1+r)(1+r)^-6 is finite.

The row-sum tensors of these infinite-lattice operators on constant
vector fields are respectively d_* I, a_* I and e_* I, where

\[
 d_*=-\tfrac18-I_1,\qquad
 a_*=8Z_0-\tfrac32+4I_1,\qquad e_*=24I_1.                 \tag{14}
\]

For D this is L282(15)--(16): the product J_ef J_fe is absolutely
summable by (9), so its Fourier integral and oddness calculation
apply directly. For the local quartic it is exactly the finite
offset calculation L283(13)--(16) with multiplier G_infinity.
No approximation of an unbounded finite-domain row sum is involved.

To justify identification of e_* with the entire kernel (12),
rather than only fixed-range approximants, regularize the full-lattice
covariance by Gamma_epsilon(q)=P(q)/(lambda(q)+epsilon), epsilon>0.
Here P is the full transverse Fourier projection. The representation

\[
 G_\epsilon=\int_0^\infty
       \frac{1-e^{-\epsilon t}}{\epsilon}
                 C^*C e^{-tL_\infty}dt                    \tag{15}
\]

follows from C*C=lambda P in Fourier space. The weight is at most
t, so (3),(8) give the G decay in (9) uniformly in epsilon.
Moreover CG_epsilon=integral e^{-epsilon t}C e^{-tL_infinity}dt,
and similarly with a curl on the right; hence their differentiated
decay bounds are also uniform. Pointwise convergence as epsilon
decreases to zero follows from the integrable bounds in these
representations. Therefore the corresponding kernel (12) is
dominated by C(1+R)^-6 and its whole row sum converges.

For each epsilon>0 the covariance and its curls have square-summable
rows, so Parseval applies to the two crossing products. The exact
constant-field Wilson calculation in L289(4)--(8), now with
gamma(q)=(lambda(q)+epsilon)^-1, gives their row-sum tensor

\[
 24\int\frac{\sin^2q_1}{(\lambda(q)+\epsilon)^2}
                 \frac{dq}{(2\pi)^4}\ I.
\]

It uses the same three transverse polarizations, two Wick pairings,
external factor two, midpoint averages and signed plaquette slots.
Off-diagonal direction entries vanish by oddness. The integrand
is bounded by 24/lambda, integrable in four dimensions. Taking
epsilon to zero and using the preceding dominated row-sum limit
proves the last value in (14) for K_infinity itself. The regulator
is only for this Fourier calculation; it never changes the finite
relative covariance or the Wilson vertices.

### 4. Quantitative boundary row defects on all strata

For an edge e with center x_e put
d(e)=1+min_mu{x_(e,mu),N-x_(e,mu)}. Compare complete finite and
infinite rows, restricting an infinite column to the actual relative
edge set and treating omitted columns separately. For d=d(e) above
a fixed stencil constant, split columns at |x_e-x_f|=d/16; this
ensures the comparison hypotheses of (9) for every nearby stencil.

For the density, the diagonal Pi difference is O(d^-4). For nearby
columns the two J products differ by at most
C d^-3(1+R)^-3, using the difference of products and (9).
For the reversed J entry the nearby column has depth comparable
to d, so the same comparison applies with its indices interchanged.
Their absolute sum is at most C d^-3(1+d)=O(d^-2).
Far columns have total O(d^-2) by (13), for both matrices and
for omitted infinite columns. Omitted columns are at distance at
least d-O(1). This proves the density row comparison O(d^-2).

For the quartic, the finite list of local covariance entries differs
by O(d^-2) by (9), and the vertex coefficients are identical at
these interior rows. Its row comparison is therefore O(d^-2).

For (12), the nearby difference of the first product is bounded by

\[
 C\{d^{-4}(1+R)^{-2}+d^{-2}(1+R)^{-4}\},
\]

and that of the second product by C d^-3(1+R)^-3. Summing shells
through radius O(d) gives respectively O(d^-2),
O(d^-2 log(ed)), and O(d^-2). The far-column tails of both
matrices, including omitted infinite columns, are O(d^-2) by
(13). Every row uses only a fixed number of local stencils, so
these estimates include all internal pairs in (12). They require
no sign assertion or cancellation between boundary terms.

For bounded d use the uniform row bounds (13) and the constants
(14); the same result holds after enlarging C. Consequently, for
K_N any of the three operators and b_* its corresponding constant,

\[
 \max_\nu\left|
    \sum_{f\parallel\nu}(K_N)_{ef}
                        -b_*\delta_{\mu\nu}\right|
       \le C\eta(d(e)),\qquad
 \eta(d)=\frac{\log(ed)}{d^2},\quad e\parallel\mu.         \tag{16}
\]

For each integer k, the set k<=d(e)<k+1 has at most C N^3
edges: cover it by the eight coordinate face slabs and four
orientations. This bound includes all intersections without needing
disjoint faces or deleting any endpoints. Since sum_{k>=1}
log(ek)/k^2 is finite,

\[
 \sum_{e\ {m variable}}\eta(d(e))\le C N^3.             \tag{17}
\]

Thus the required boundary error is summed over the complete cube,
including faces, edges, corners and both normal endpoints.

### 5. Ground bilinear forms and the signed cancellation

The ambient counting-normalized ground field with coefficients
c=(c_1,...,c_4) is the restriction of the smooth vector function

\[
 v_\mu(x)=\frac{\sqrt8}{N^2}c_\mu
               \prod_{\nu\ne\mu}\sin(\pi x_\nu/N).        \tag{18}
\]

Component mu is evaluated on its actual midpoint/vertex edge grid.
The own-coordinate constant cosine and the three vertex sine norms
give exactly ||v||_2=|c|, as in L296 section 2. Its values at
arbitrary points of the cube obey
max_mu |v_mu|<=C N^-2|c| and max_mu |gradient v_mu|<=C N^-3|c|.

For e parallel to mu, subtract and add v_nu(x_e) in each direction
column of K_N v. Equations (13),(16) give

\[
 |(K_Nv)_e-b_*v_\mu(x_e)|
     \le C|c|\{N^{-3}+N^{-2}\eta(d(e))\}.                \tag{19}
\]

Indeed the first term uses the uniformly summable first spatial
moment in (13) and the Lipschitz bound in (18); the second is the
complete row-sum defect. If u is another ground vector, then
|u_e|<=C N^-2||u||. There are at most 4N^4 variable edges, and
(17) sums the second term. Pairing (19) with u proves

\[
 |\langle u,(K_N-b_*I)v\rangle|
                \le C N^{-1}\|u\|\|v\|.                 \tag{20}
\]

Equivalently, after the isometry Q, all three rank-four compressed
operators have the claimed O(N^-1) errors. This bilinear estimate
does not assert an O(N^-1) strong-norm error on arbitrary fields.

For the full cubic operator L297(17), directly from L287's two
energy bounds and both cross pairings, retains

\[
 |\langle u,(\mathcal E_N-\mathcal E_N^{\rm int})v\rangle|
 \le C(\ell_N\lambda_0+\sqrt{\ell_N\lambda_0})\|u\|\|v\|.
 \tag{21}
\]

The formula includes the external/external and both mixed
internal/external-curl placements. Since lambda_0<=3pi^2/N^2,
(20),(21) apply to the entire operator (1). Its scalar constant is

\[
 d_*-\tfrac14a_*+\tfrac14e_*
       =\tfrac14-2Z_0+4I_1=0,                            \tag{22}
\]

where the final equality is L289(16)'s justified identity. Hence
(2) follows. Color invariance makes the calculation a one-color
compression with all internal multiplicities already included;
no factor three is dropped from an internal contraction.

For the limited downstream use, L297(23) and
||P_N B_i P_N||<=F give |b_N|<=4F^2||P_N W_N^(0)P_N||.
At its r_N, the displayed largest-pole term in L297(24) is thus
O_F(N^-1/2 log(eN)^(5/2)), and tends to zero. This substitution
does not improve the other terms in L297(24): their existing
bounds alone do not establish a bounded complete response.

### 6. Separate conceptual audit (2026-10-28)

This audit accepts (2) under the stated inputs. It checks the new
quantitative argument, not the whole upstream Yang--Mills construction.
The saved EXPLORE assessment covers exactly this target; no external
rate theorem or unassessed boundary specialization is imported here.

**Counting normalization and endpoint differences.** Periodization
with period 2N gives Fourier weight 1/(2N). Subtracting or adding
the reflected argument and pairing k with 2N-k gives weight 2/N
for each nonconstant sine or midpoint cosine, and 1/N for the
constant cosine. The k=N term vanishes on each relevant grid.
Thus (5) has precisely the kernels of D*D on interior vertices and
DD* on all N interval edges, for unscaled incidence D.

For an explicit endpoint check, put p=p_t^(1) and suppress the
common shifts 2Nk in the following image terms. The difference
H_t^D(i+1,j)-H_t^D(i,j), including i=0 and i=N-1, is the sum of

\[
 [p(i+1-j)-p(i-j)]-[p(i+1+j)-p(i+j)].
\]

The image sum has H_t^D(0,j)=H_t^D(N,j)=0, so this formula
uses the actual pinned endpoint values. Conversely D* acting on
the E kernel at the interior vertex i gives the image terms

\[
 [p(i-1-j)-p(i-j)]+[p(i+j)-p(i+j+1)].
\]

Each bracket is one lattice difference, with its indicated sign.
Right differences work the same way; applying both sides gives
two differences. These are the only endpoint operations used in
B, C and their adjoints in (7); M is a sum, not a derivative.
The minus sign between B and D in L280 cancels in B Delta^-2 B*.
No normal end edge is dropped or assigned a Dirichlet value.

For t>=1, a term with b derivatives on the difference multiplier
and h on the exponential, b+h=|alpha|, has the integral power
t^((h-4-max(j-b,0))/2). This is at most the power in (4), also
when b>j. Repeated integration by parts on the periodic integer
Fourier grid therefore proves (3) for all the required mixed
differences. At t<=1 the derivative integrals are bounded, including
t=0. Fixed stencil shifts change only constants.

For x,y in an interval, every reflected image distance is at least
|x-y|. A non-direct image for nearby stencils at depth d is at
least c d, after allowing the bounded offsets just displayed.
The 16 reflection choices and 2N-periodic image shells have only
O((l+1)^3) points in shell l. Since sqrt(1+t)<=2N in the short-time
range, the six additional decay powers used in section 1 sum
uniformly. This proves both image estimates simultaneously at
face intersections; it is not an independent one-face approximation.

**Transverse kernel and large times.** The exact tensor modes have
at least three positive indices for a one-form and four for a
vertex. An incidence difference contributes the corresponding
2 sin(pi k_mu/(2N)) multiplier; two differences contribute at most
C lambda_k. Together with the N^-4 product normalization, their
spectral sums prove (6), including the own-direction constant
cosine. There is no undamped all-zero mode in these two spaces.

The identity L B=B Delta and the orthogonal splitting in L280(23)
give the first line of (7). CB=0 removes its second term whenever
a curl is present. The transverse subtraction has two differences
and one factor t: its short-time majorant is
(1+t)^-2 times the spatial decay factor, and its long-time integral
is N^-6 times O(N^4)=O(N^-2). The other integrated powers are
(1+t)^-5/2 for CG and J and (1+t)^-3 for CGC* and Pi, giving
respectively N^-3 and N^-4 long-time bounds. Applying the same
estimates to the infinite tail and using d<=N/2+1 proves every
entry of (9). The divergent undifferentiated infinite Delta^-2
kernel is never formed. These checks justify the transverse,
mixed-direction entries as well as the diagonal components.

**Complete contractions and bulk constants.** Each term in
mathsf B has the form u_e^b (Cx)_p^a x_f^c with a!=c, with p,f
at bounded distance from e. Each external edge has only a bounded
number of such slots. Within-vertex Wick pairings vanish by color;
the two crossing pairings are exactly the two products in (12).
Consequently their complete sum has R^-6 decay. The first moment
uses the convergent series sum_r (1+r)^-2, with the four-dimensional
shell multiplicity included. This verifies (13) without deleting
an internal vertex or bounding only one pairing. D follows from
the two J factors and its local terms; A follows from C_U and its
single-plaquette support.

For the infinite internal-curl row sum, (15) gives decay uniformly
in epsilon because (1-exp(-epsilon t))/epsilon<=t and C*C is a
two-difference operator. Its curls have the asserted exponentially
weighted heat representations. For fixed epsilon the rows are in
l2, so Parseval is applicable to each crossing product. The full
constant-field Wilson algebra from L289(6)--(8) gives factor
4 times 2 times 3=24: the two Wick pairings, the factor two in
E^int, the color trace and the three transverse polarizations.
Its applicability only requires Gamma=gamma P, which the regulator
has. Dominated row summation uses (1+R)^-6, and dominated Fourier
integration uses sin^2(q_1)/(lambda+epsilon)^2<=1/lambda.
Thus this calculation concerns the entire infinite kernel, not
only a fixed-range limit. The D and A constants are precisely
L282(15)--(16) and L283(13)--(16), with unchanged raw-edge phases
and internal colors. Their finite Wilson algebra is retained as
an upstream input. These checks give all three constants in (14).

**Full boundary sum and ground compression.** The nearby column
sums in section 4 reduce, with shell multiplicities, to
d^-4 sum_{r<=C d}(1+r), d^-2 sum_{r<=C d}(1+r)^-1, and
d^-3 sum_{r<=C d}1. They are O(d^-2), O(d^-2 log(ed)),
and O(d^-2). Far or omitted columns give
sum_{r>=c d}(1+r)^-3=O(d^-2). The reversed J entry has comparable
depth; the local quartic uses only the first comparison in (9).
For bounded depth the uniform row bounds suffice. Every depth
layer has at most C N^3 edges, even where faces intersect.
Since sum_k log(ek)/k^2<infinity, (17) follows for the whole box.

The four fields (18) have exact norm one: N constant-cosine
samples and three sine squared sums N/2 cancel the factor 8/N^4.
They have B*v=0 and eigenvalue lambda_0, so they span precisely
L296's ground space. Their smooth interpolants have sup norm
O(N^-2) and Lipschitz constant O(N^-3). Equation (19) can therefore
be paired with any ground field: the smooth-variation contribution
is O(N^-2 N^-3 N^4)=O(N^-1), and the boundary contribution is
O(N^-4 N^3)=O(N^-1). This is a bilinear compression estimate;
no O(N^-1) strong-norm error on arbitrary vectors was inferred.

Finally, L287(12)--(13) gives the AA, AB and BA external-curl
terms, with respective bounds O(ell_N lambda_0) and twice
O(sqrt(ell_N lambda_0)). These are precisely (21). The signed
constant d_*-a_*/4+e_*/4 is zero by L289(16), whose small-sphere
flux justification is retained. Thus the complete error is
O(N^-1 sqrt(log(eN))) for all even N>=2, within the registered
threshold. No sign for any boundary subtotal is required.

At theta_N=(3/2)log N, lambda_0^-1=O(N^2) and exp(-theta_N)=N^-3/2.
The largest pole in L297(24) is therefore
O_F(N^-1/2 log(eN)^(5/2)) as claimed. The two other displayed
remainder bounds remain O_F(N^1/2 log(eN)) and
O_F(N^1/4 log(eN)); this audit supplies no improvement to them.
It verifies a relevant local rate, not a bounded complete tail or
an interacting continuum or mass construction. No new mathematical
input beyond the existing DAG row is used.

## Mathlib

Full matching coverage for (2), the relative tensor heat comparison,
and the signed Wilson compression has not been checked. Absence is
not asserted. Finite sums, spectral decomposition and Fourier/heat
integrals above are informal arguments, not a Lean verification.
The general finite Gaussian theorem is cited precisely in section 3;
the needed mixed-grid and Wilson specializations are proved here
because the saved source comparison supplies no matching rate.
