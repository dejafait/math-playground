# L301 — Complete low one-heat-line response from signed energy-form bounds

## Hypotheses

Retain L297's exact SU(2) relative cube, even N>=2, a=8/N,
Euclidean counting measure, boundary-contained pinned links,
boundary-fixed gauges and every variable normal link at both ends.
Use the fixed unweighted transverse space H=ker B*, its orthonormal
inclusion Q, and L279/L280's ambient Wilson jets on their own slice.
The complete source-independent density retains Haar and both gauge
determinants. All upstream premises of the results used below remain
assumptions; no different gauge, boundary or Gaussian law is substituted.

The sources h_-,h_+ are exactly L282(1)'s reflected 12-bumps,
sampled with L297's convention and zero on other orientations.
Their smooth spatial extensions to lattice coordinates [0,N]^4 obey

\[
 |h_i(x)|\le F,\qquad
 |h_i(x)-h_i(y)|\le C_fN^{-1}|x-y|,\qquad
 h_-(x)h_+(x)=0.                                      \tag{1}
\]

The last identity follows from their disjoint physical time supports
[-2,-1] and [1,2]; both are zero off their supports. Fixed sampling
shifts are retained in differences, not used to identify nearby values.

On one-color H put A=Q*C*CQ, Ahat=A/lambda_0, and

\[
 \lambda_0=12\sin^2(\pi/(2N)),\quad
 \theta_N=\tfrac32\log N,\quad r_N=\theta_N/\lambda_0,
 \quad A(s,t)=A-sK_--tK_+,
 \quad K_i=Q^*C_{12}^*\operatorname{diag}(h_i)C_{12}Q.
                                                               \tag{2}
\]

Let Wtilde(s,t) be the one-color compression Q*W_N(s,t)Q of
L297(7), after all internal color contractions. Its density and
cubic/quartic factors are unchanged. With gamma_N positively oriented,
|z-lambda_0|=lambda_0/12, use the registered moving-cluster function

\[
 H^{\rm lo}(s,t)=\frac1{2\pi i}\oint_{\gamma_N}
       \frac{e^{-r_Nz}}z\,(z-A(s,t))^{-1}\,dz.             \tag{3}
\]

Keep r_N and the contour fixed in all source derivatives. A subscript
alpha denotes the zero-source derivative for alpha empty, -, +, or -+.
Inverses and square roots of the extended covariance mean restriction
to H. Write ell_N=log(eN). Use the audited inputs L297's full source
product rule and weighted low-contour bounds, L298's exact transverse
kernels and signed zeroth-order row estimates, and L300's first-source
kernel, row and external-curl estimates. L003 supplies the relative
tensor grids, and L287 the exact cubic split. No source-uniform moving
compression or regularity of individual eigenbranches is assumed.

## Conclusion

For all four alpha there is C_f independent of even N such that

\[
 \boxed{\quad
 \|\widehat A^{-1/2}\widetilde W_\alpha
                      \widehat A^{-1/2}\|
 \le C_f\{N^{-1}+N^{-1}\sqrt{\ell_N}+N^{-2}\ell_N\}.
 \quad}                                                    \tag{4}
\]

Consequently the complete signed low one-heat-line response satisfies

\[
 \boxed{\quad
 \left|3\left.\partial_s\partial_t
        \operatorname{Tr}_H(\widetilde W(s,t)H^{\rm lo}(s,t))
                      \right|_{0,0}\right|
       \le C_f N^{-1/2}\ell_N^{5/2}=o(1).
 \quad}                                                    \tag{5}
\]

Every term in L297(22), including every off-ground low-contour residue,
is included. The proof bounds the zero-source derivatives in a form
norm on the full fixed H; it does not assert a small unweighted operator
norm, a complex-source estimate, or a new gauge-slice identification.
This is local progress under the saved EXPLORE assessment, with no
claim of originality beyond the sources checked. The separate conceptual
audit in section 8 accepts (4)--(5) under the stated upstream premises;
it does not verify those premises afresh.

The high-contour response, complete tail, uncut coefficient, uniform
higher remainder, interacting reflection lower bound, continuum axioms
and positive infinite-volume mass remain unresolved. This is not a
complete-solution candidate.

## Proof

### 1. The signed internal operators already controlled by row estimates

For arbitrary sources split each exact weighted cubic derivative as
in L287 and L300(10):

\[
 D S_{3,w}(x)[u]=\mathsf A_w(u;x)+\mathsf B_w(u;x),\quad
 \mathsf A_w=\sum_p w_p(Cu)_p\cdot\zeta_p(x),\quad
 \mathsf B_w=\sum_p w_p(Cx)_p\cdot D\zeta_p(x)[u].       \tag{6}
\]

Let Eint(s,t) be the B/B crossing contraction, with exactly L287's
factor two, and define the ambient one-color operator

\[
 Z(s,t)=D_N+\tfrac14 E^{\rm int}(s,t)
                  -\tfrac14\mathcal A(U(s,t);G(s,t)).    \tag{7}
\]

This removes only external-curl terms for subsequent estimation;
none are discarded from W. For r=|x_e-x_f|, put
k_b(r)=(1+r)^(-b), l(r)=log(e+r), and
d(e)=1+min_mu{x_(e,mu),N-x_(e,mu)}.

L298(13),(16),(22) imply for Z_empty a C k_6 entry envelope and
direction-row bound C d(e)^-2 log(ed(e)). The three bulk constants
cancel before taking absolute values. L300(12),(19) imply for Z_i
a C_f l k_6 envelope and direction-row bound
C_f(N^-1+d(e)^-2 log(ed(e))^2), including both first sources.
Thus for alpha empty,-,+, we have the common bounds

\[
 |(Z_\alpha)_{ef}|\le C_f l(r)k_6(r),\qquad
 \left|\sum_{f\parallel\nu}(Z_\alpha)_{ef}\right|
       \le C_f\{N^{-1}+\eta(d(e))\},\quad
 \eta(d)=d^{-2}\log(ed)^2.                              \tag{8}
\]

The constants include diagonal/local terms, all orientations and
internal colors. The cited statements are full finite-domain bounds,
including missing infinite columns in their boundary comparisons.
No differentiation of L299's constant-rho identity is added here:
the first-derivative transfer and its domination are already in L300.

### 2. Relative-grid extension and a summed boundary trace estimate

Write an edge as (n,mu), with integer starting vertex n and center
n+e_mu/2. Its variable domain has 0<=n_mu<N and
1<=n_nu<N for nu different from mu. For each component v_mu extend
to the torus T_N=(Z/(2N)Z)^4 as follows. In the mu coordinate reflect
evenly across the midpoint-grid ends, so v_mu(-1-j)=v_mu(j).
In every other coordinate use odd reflection at 0 and N, with
the endpoint value zero. Denote the extension by E v_mu.

L003's component Laplacians are DD* on the edge coordinate and
D*D on the vertex coordinates, in unscaled counting units here.
Directly pairing the reflected entries and their forward differences
gives

\[
 \sum_\mu\|E v_\mu\|_{\ell^2(T_N)}^2=16\|v\|^2,
 \qquad
 \sum_{\mu,j}\|\delta_j E v_\mu\|_{\ell^2(T_N)}^2
     =16\langle v,Lv\rangle,\quad L=C^*C+BB^* .        \tag{9}
\]

For completeness the one-dimensional edge reflection duplicates
each of its N values, duplicates each interior difference, and has
zero difference at the two reflected joins; its energy is twice
the DD* form. The odd vertex reflection duplicates the N-1 interior
values; its differences include both zero-endpoint intervals and
duplicate precisely the D*D form. Tensoring multiplies each squared
norm and each coordinate energy by 2^4. This explains (9) also at
both variable normal endpoints. It is a finite-grid specialization
to fix these conventions, not an imported scalar boundary theorem.

Set E(v)=sqrt(<v,Lv>). Periodic translation and telescoping along
integer coordinate steps give, for any integer displacement b,

\[
 \|E v_\nu(\cdot+b)-E v_\nu\|_2
       \le |b|_1\Big(\sum_j\|\delta_j E v_\nu\|_2^2\Big)^{1/2}.
                                                               \tag{10}
\]

There is also the following uniform bound on any one coordinate slice
of a torus function w:

\[
 \sup_j\sum_{n:n_k=j}|w(n)|^2
 \le (2N)^{-1}\|w\|_2^2+2\|w\|_2\|\delta_k w\|_2.    \tag{11}
\]

Indeed choose a slice with squared norm no greater than the average.
The difference between consecutive squared slice norms is bounded
by the norm of their difference times the sum of their norms.
Sum along the cyclic path from that slice to any other and apply
Cauchy--Schwarz over the full cycle. The second factor is at most
2||w||_2; this proves (11) for real or complex fields.

To apply it to every boundary stratum, eta(d(e)) is bounded by a
constant times the sum of the eight face weights
q(n_k),q(N-n_k), where q(j)=(1+j)^-2 log(e+j)^2.
Replacing an edge center by its start changes depths by at most 1/2
and only changes the constant. The sum of q(j) for j>=0 is finite.
Summing (11) against each face weight and using (9) therefore gives

\[
 \sum_{e\ {\rm variable}}\eta(d(e))|v_e|^2
       \le C\{N^{-1}\|v\|^2+\|v\|E(v)\}.              \tag{12}
\]

The same bound holds for the sum over any pair of component labels
mu,nu of eta(d(n,mu)) |E v_nu(n)|^2 restricted to variable mu edges.
To see this, enlarge that restriction to all n in {0,...,N-1}^4
for each face weight and apply (11) to E v_nu. Sum the four
components by Cauchy--Schwarz. This includes values of another
component at a row anchor, whether that value is a variable edge or
a pinned zero. Face intersections are overcounted by at most the
fixed number of faces; no edge, corner or normal endpoint is omitted.

### 3. From the signed rows to a full-space energy form

Let K be any of the three operators in (8) and set
r_(e,nu)=sum_(f parallel nu) K_ef. On the exact edge domain write

\[
 (Kv)_e=\sum_\nu\sum_{f\parallel\nu}K_{ef}
       [v_f-Ev_\nu(n_e)]+\sum_\nu r_{e,\nu}Ev_\nu(n_e).
                                                               \tag{13}
\]

For fixed external directions and b=n_f-n_e, the first operator
in (13) is bounded in l^2 by C_f l(|b|)k_6(|b|) times the
translation-difference norm in (10). Centers and anchors differ
by bounded offsets, already absorbed in this envelope. Each n_e
occurs at most once for fixed b and directions; enlarging the sum
to the torus is therefore valid. Minkowski's inequality gives

\[
 \left\|\sum_{\nu,f\parallel\nu}K_{ef}
                   [v_f-Ev_\nu(n_e)]\right\|_{\ell^2(e)}
       \le C_f E(v),                                    \tag{14}
\]

since sum_(b in Z^4) |b|_1 l(|b|)k_6(|b|)<infinity.
In dimension four its large-radius shell sum is bounded by
sum_(j>=1) j^-2 log(ej). Actual finite-domain displacements form
a subset; periodic translation introduces no extra column multiplicity.

For the second term in (13), use (8) and Cauchy--Schwarz with
the boundary weight. The unweighted restriction of each extended
component has norm at most 4||v||. By (12), for any u,v,

\[
 |\langle u,Kv\rangle|
 \le C_f\left[\|u\|E(v)+N^{-1}\|u\|\|v\|
        +\mathfrak b(u)^{1/2}\mathfrak b(v)^{1/2}\right],
 \quad \mathfrak b(v)=N^{-1}\|v\|^2+\|v\|E(v).           \tag{15}
\]

This uses full direction rows; it requires neither positive K nor
ground-field supremum estimates. It is valid for the actual complex
bilinear pairings as well.

For u=Q u_H and v=Q v_H, B*u=B*v=0, so L's form is C*C and

\[
 \|u\|\le\|\widehat A^{1/2}u_H\|,\quad
 E(u)=\sqrt{\lambda_0}\|\widehat A^{1/2}u_H\|
       \le\sqrt3\pi N^{-1}\|\widehat A^{1/2}u_H\|.      \tag{16}
\]

Here Ahat>=I is L297's ground eigenvalue statement. Thus (15)
proves

\[
 \|\widehat A^{-1/2}Q^*Z_\alpha Q\widehat A^{-1/2}\|
       \le C_fN^{-1},\qquad \alpha=\varnothing,-,+.     \tag{17}
\]

This is the additional estimate that controls off-ground vectors:
unlike a ground compression, it is a form bound on the entire H.

### 4. Both mixed inverse orders and the disjoint-source gain

Use L300(3)'s R_i=G C_12* h_i C_12 G and its constant-insertion
operator R=G C_12* C_12 G. Let a superscript jk mean a left
endpoint curl when j=1 and a right endpoint curl when k=1;
j,k belong to {0,1}. At endpoints x,y, r=|x-y|, L300(7),(8)
give, for an anchor x_e within a fixed stencil of x,

\[
 |R_i^{jk}(x,y)|+|R^{jk}(x,y)|
       \le C_f l(r)k_{2+j+k}(r),\quad
 |R_i^{jk}(x,y)-h_i(x_e)R^{jk}(x,y)|
       \le C_fN^{-1}l(r)k_{1+j+k}(r).                   \tag{18}
\]

These are finite-cube estimates, not a frozen replacement for an inverse.
The exact mixed derivative contains both orders:

\[
 G_{-+}=G C_{12}^*h_-C_{12}G C_{12}^*h_+C_{12}G
             +G C_{12}^*h_+C_{12}G C_{12}^*h_-C_{12}G.  \tag{19}
\]

For either order, its jk endpoint kernel is the sum over the two
actual insertion plaquettes z,w of three factors, with envelopes
k_(3+j)(|x-z|), k_4(|z-w|), k_(3+k)(|w-y|), by L298(9).
The sources multiply these factors. By (1),

\[
 |h_-(z)h_+(w)|
 \le C_fN^{-1}\{1+|x-z|+|z-w|\}.                       \tag{20}
\]

To check (20), subtract the zero product h_-(x_e)h_+(x_e),
use the sup bound for the undifferenced factor and Lipschitz bounds
for the other, and then |w-x_e|<=|x-z|+|z-w|+O(1).
The same argument applies to the reverse source order. Hence

\[
 |G_{-+}^{jk}(x,y)|
       \le C_fN^{-1}l(r)^2k_{1+j+k}(r).                \tag{21}
\]

Here are the complete convolution estimates needed for this gain.
The two triple envelopes after (20) have exponent triples
(2+j,4,3+k) and (3+j,3,3+k). In dimension four, if
0<a,b<=4, a+b>4, and p=0 or 1, the usual three-region shell split
gives

\[
 (l^p k_a)*k_b\,(r)
       \le C_{a,b,p}\,l(r)^{p+1}k_{a+b-4}(r).          \tag{22}
\]

Precisely, on the radius-r/2 ball about one endpoint the other
factor is bounded at radius r; the partial radial sum of l^p k_a
is O(r^(4-a)l(r)^p) for a<4 and O(l(r)^(p+1)) for a=4.
Exchange endpoints for the second ball. On the remaining region
at radius O(r) count O(r^4) sites, and on successive outer dyadic
annuli sum O((2^j r)^(4-a-b)l(2^j r)^p). This converges with the
asserted bound since a+b>4. For r<2 the same tail is summable.
This is L300's elementary convolution argument with the displayed
logarithmic weight retained, not a variable-coefficient Green theorem.

Convolve the first two exponents of either triple and then the third.
The intermediate exponent is 2+j in either case; the final sum
of exponents is 5+j+k>4. All exponents encountered are at most 4.
Two applications of (22) prove (21), including j=k=1. Sums over
finite insertion domains are bounded by the positive infinite sums;
boundedly many cell types and their shifts only change C_f. Thus all
insertions at relative boundaries and at large separation are included.

### 5. The entire mixed internal-curl and quartic operator

Each B/B kernel in (7) is exactly a finite sum of the two forms
L298(12),

\[
       (CGC^*)_{pq}G_{fg},\qquad
       (CG)_{pg}(GC^*)_{fq},                            \tag{23}
\]

with p,f within a fixed stencil of the external row e and q,g
within one of the external column. Their internal curl orders sum
to two. All coefficients, crossing pairings and colors are those
already fixed in L287/L297; source derivatives change weights and
covariance slots, not their local tensor coefficients.

L297(13)'s labeled product rule allocates the two distinct source
labels to two vertex slots and two covariance slots. Its nonzero
allocations are exactly: two different vertex slots (2 allocations),
one vertex and one covariance slot (8), two different covariance
slots (2), and both labels on one covariance slot (2, each using
both orders in (19)). Both labels on a single affine vertex give
zero. The following estimates cover each allocation, with its sign
unchanged before bounding it.

For two vertex slots, subtract their common-anchor product, zero by
(1). The source product is bounded by C_f N^-1(1+r), where now
r=|x_e-x_external_column|. Multiplication by (23)'s k_6 envelope
gives C_f N^-1 k_5(r).

For one vertex and one inverse slot, subtract
h_vertex(x_e)h_inverse(x_e) times the constant-insertion kernel.
The subtracted product is zero. The vertex displacement is at most
C(1+r), and (18) controls the inverse error. Multiplying by the
other, undifferentiated line gives C_f N^-1 l(r)k_5(r).
Orientation indicators are retained: a differentiated vertex is a
12-vertex and its constant-insertion counterpart uses C_12.

For two different inverse slots, write
R_i(x,y)=h_i(x_e)R(x,y)+error separately for both factors,
with their actual endpoint curls. Subtract the zero product of
the two constants. Equivalently subtract in two stages, keeping
one full R_i in one error term; (18) gives
C_f N^-1 l(r)^2 k_5(r). This does not require a bound on the
square of a localization error. For both labels on one inverse
slot, (21) times the other kernel gives the same bound. In all
cases the two curl orders in (23) make the total decay exponent
five, and both factors have left endpoints within a fixed stencil
of e, as required by (18),(20).

The quartic mixed derivative is exactly

\[
 \mathcal A(U;G_{-+})-\mathcal A(U_{h_-};R_+)
                         -\mathcal A(U_{h_+};R_-).      \tag{24}
\]

Its external and internal slots lie on one actual plaquette.
Equation (21) at bounded separation bounds its first term by
C_f/N per entry. For each other term freeze the vertex source
and (18)'s inverse source at the same external anchor. Their product
is zero by (1); the two errors are C_f/N at bounded separation.
The quartic coefficient sum is uniformly bounded as recorded in
L298 section 3, so its finite-range row norm is O_f(N^-1).
The density has zero mixed derivative.

The internal cubic bounds have summable rows, since
sum_(j>=0)(1+j)^3 l(j)^2 k_5(j)<infinity. Missing pinned slots
only delete terms; none of these arguments invokes translation
invariance or an infinite-volume boundary replacement. We obtain

\[
 \sup_e\sum_f|(Z_{-+})_{ef}|\le C_f N^{-1}.             \tag{25}
\]

The complete Z(s,t) is real symmetric for real sources, so its
mixed derivative has the same column bound. The elementary Schur
estimate (Cauchy--Schwarz in the weighted double sum) gives
||Z_-+||<=C_f/N. Since ||Ahat^-1/2||<=1, (17) therefore holds
for the mixed derivative as well. In this step separation replaced
any need for a second constant-rho identity or a new boundary transfer.

### 6. Restoring every external-curl placement

The exact weighted estimates L300(22), from L287's complete vertex,
are

\[
 \mathbb E[\mathsf A_w(u;x)^2]
       \le C\|w\|_\infty^2\ell_N\|Cu\|^2,\qquad
 \mathbb E[\mathsf B_w(u;x)^2]
       \le C\|w\|_\infty^2\|u\|^2.                    \tag{26}
\]

They apply to weights 1,h_-,h_+, with the 12 restriction, at all
relative endpoints. No curl of h_i u replaces h_i Cu. The finite
Gaussian identities used here are the already imported
Bauerschmidt--Brydges--Slade, *Introduction to a Renormalisation
Group Method*, LNM 2242 (2019),
[arXiv:1907.05474v2](https://arxiv.org/pdf/1907.05474v2),
Propositions 2.1.6/2.1.9 and Corollary 2.1.11, printed pp. 31--33.
Their positive semidefinite covariance hypotheses hold on the fixed H;
source derivatives are multilinear signed slots, not new positive laws.

By L297(10), any differentiated covariance slot is G^(1/2) Z G^(1/2)
with ||Z|| bounded by 1,F, or 2F^2, for orders empty, first, or mixed.
The mixed Z contains both inverse orders. In the two internal Gaussian
coordinates of each quadratic vertex, its covariance contraction is
the tensor inner product acted on by Z_X tensor Z_Y. Cauchy--Schwarz
therefore bounds it by ||Z_X||||Z_Y|| times the corresponding
Hilbert--Schmidt norms. As in L300's proof of (23), these norms are
controlled by (26), with their fixed Wick factors. This argument
does not assume that differentiated covariances commute or are positive.

Apply this estimate to every nonzero labeled allocation in L297(13),
including the mixed allocations counted in section 5. Each difference
between the full cubic term and its B/B part has type A/A, A/B or
B/A. Consequently, for each of the four alpha and all u,v,

\[
 |\langle u,(W_\alpha-Z_\alpha)v\rangle|
 \le C_f\{\ell_N\|Cu\|\|Cv\|
       +\sqrt{\ell_N}(\|Cu\|\|v\|+\|u\|\|Cv\|)\}.      \tag{27}
\]

The factor 1/4 and every finite source/Wick multiplicity are included
in C_f. The quartic and density were already retained in Z. On H,
(16) turns (27) into a form bound
C_f(N^-2 ell_N+N^-1 sqrt(ell_N)). Combine with (17),(25) to
prove (4), for real and hence also complex vectors. Global color
invariance makes each final block scalar in external color after,
not before, its complete internal contractions.

### 7. Complete low trace, including the moving subspace

L297(19), including its all-ground pole and its off-ground remainder,
gives for alpha empty,-,+,-+,

\[
 \|\widehat A^{1/2}H^{\rm lo}_\alpha
                   \widehat A^{1/2}\|_1
       \le C_f\lambda_0^{-1}(1+\theta_N)^{|\alpha|}
                                           e^{-\theta_N}. \tag{28}
\]

For mixed order, the explicitly displayed all-ground coefficient
has bounded weighted trace norm times |f_theta''(1)|;
the other six placements per source order have L297's
O((1+theta)e^-theta) remainder. Thus (28) does not take a supremum
of the heat function on the circle or omit an off-ground coefficient.
The fixed-contour derivatives already differentiate the total moving
cluster. No individual eigenvector is differentiated here.

The matrix inputs were assessed before this attempt: Texier,
*Basic matrix perturbation theory*, Enseign. Math. 64 (2018),
Propositions 1.1 and 2.1, pp. 250,252--253,
[publisher PDF](https://ems.press/content/serial-article-files/44369?nt=1),
for the total isolated projector; and Schweitzer,
[arXiv:2203.03930v1](https://arxiv.org/pdf/2203.03930v1),
section 2.1, Lemma 1, PDF pp. 2--3, for ordered resolvent derivatives.
Use L297's justified local contour, not the full-spectrum hypothesis
of Schweitzer's Theorem 2 as a low-contour theorem. The affine family
acts on the same finite H and its ground cluster is isolated; internal
splitting is allowed. The quantitative weights in (28) are L297's
local estimates, not a consequence of finite-dimensional analyticity.
No standard spectral theorem is reproved.

The full product rule is exactly

\[
 3\operatorname{Tr}_H(\widetilde W H^{\rm lo}_{-+}
       +\widetilde W_-H^{\rm lo}_+
       +\widetilde W_+H^{\rm lo}_-
       +\widetilde W_{-+}H^{\rm lo}).                    \tag{29}
\]

For each term use (4) against (28) by finite-matrix trace duality,
after cycling the two Ahat half-powers. That inequality is
|Tr(XY)|<=||X||||Y||_1, with no positivity assumption; its source
and applicability are already recorded in L297 section 4 (Watrous,
*The Theory of Quantum Information*,
[2018 draft](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf),
section 1.1, pp. 32--33, (1.165)--(1.175)). Thus (29) is bounded by

\[
 C_f\{N^{-1}+N^{-1}\sqrt{\ell_N}+N^{-2}\ell_N\}
           \lambda_0^{-1}(1+\theta_N)^2e^{-\theta_N}.    \tag{30}
\]

Since 12/N^2<=lambda_0<=3pi^2/N^2 and
e^-theta_N=N^-3/2, (30) is O_f(N^-1/2 ell_N^(5/2)).
The contribution N^-3/2 ell_N^3 is smaller and is absorbed
uniformly for N>=2. This proves (5). The factor three in (29) is
the external color trace; the two source orders have already been
counted. No estimate of the high contour or interchange of ultraviolet
and coupling limits was used or concluded.

### 8. Separate conceptual audit (2026-10-29)

This audit accepts the complete bounds (4)--(5), conditional on the
stated inputs. It reuses the approved primary-source assessment and
checks the local argument beyond those sources. In particular it
does not replace a signed direction row by an absolute row, a
transverse kernel by a scalar kernel, or a moving cluster by its
fixed-ground compression. No numerical check is needed for the
finite identities and uniform estimates below.

**Imported rows and exact relative energy.** L298(13),(16),(22)
give the entry and direction-row bounds for the entire zeroth-order
operator (7): its three bulk constants cancel with the coefficients
1, 1/4, -1/4. L300's auxiliary K_i in its section 4 is exactly
the derivative of (7), since D_N is source independent. Thus its
(12),(19) give (8) for each first derivative on the full edge domain,
not merely after ground compression. The derivative of the frozen
row identity and its boundary transfer are retained upstream premises.
The two first derivatives need no new constant-weight identity here.

For (9), use the unscaled interval incidence D_0 (equal to a times
L003's D). In the edge coordinate the reflected sequence has two
copies of each value and interior difference; both joins have zero
difference. Its energy is twice
sum_{j=1}^{N-1}|v_j-v_{j-1}|^2, the D_0 D_0* form.
In a vertex coordinate the zero values at 0,N contribute both
endpoint intervals; odd reflection doubles precisely the D_0* D_0
form. Tensoring gives the factor 16 for norms and every coordinate
energy. This also works for N=2 and includes the variable normal
edges starting at 0 and N-1. The identity L=C*C+BB* is on this
same counting-measure relative complex.

To check (11), regard each slice as a vector w_j in its remaining
coordinates. Along a path of the cyclic coordinate,
| ||w_{j+1}||^2-||w_j||^2 |
is at most ||w_{j+1}-w_j||(||w_{j+1}||+||w_j||).
Cauchy--Schwarz bounds the path sum by
2||delta_k w|| ||w||. Starting at a slice no larger than the
average proves (11), also for complex entries. The eight face
weights dominate eta of the minimum depth, up to an absolute
constant, and each weight has a finite depth sum. This proves
(12). For cross-component anchor values, enlarge to the full
integer cube before applying the same slice inequality. This
enlargement includes pinned zeros and retains all values of an
evenly extended normal component. Intersections of faces are only
overcounted a fixed number of times; no boundary stratum is removed.

**Signed rows on all of H.** For each fixed displacement b and
pair of component labels, there is at most one column at n_e+b.
On an actual column, v_f=Ev_nu(n_f). Thus the first summand of
(13) is bounded by its coefficient supremum times the torus
translation difference, even though its coefficients are not
translation invariant. The enlargement to the torus introduces
no multiplicity depending on N. The shell sum of its first moment
is sum_{j>=1} O(j^-2 log(ej)), which converges. This checks (14).
The second summand uses the signed direction row itself; weighted
Cauchy--Schwarz and the cross-component version of (12) give (15).
Neither symmetry nor positivity of K is needed in this step.

For u=Q u_H, B*u=0 gives E(u)^2=<u_H,A u_H> exactly.
The spectral lower bound Ahat>=I and
sqrt(lambda_0)<=sqrt(3) pi/N then imply
||u||<=||Ahat^(1/2)u_H|| and
mathfrak b(u)<=C N^-1||Ahat^(1/2)u_H||^2.
Using these inequalities for both vectors in (15) yields (17)
as an operator norm after the two inverse half-powers. This is a
bound on every vector of H, including off-ground vectors; it is
not an extrapolation of L298/L300's ground-space conclusions.

**Mixed inverse orders and source allocations.** The exact bumps
in L282(1) have disjoint time supports. Their smooth zero extensions
give (1) at a common spatial anchor as well as at the actual
plaquette sampling points. For either order in (19), expand
h_-(z)h_+(w)-h_-(x_e)h_+(x_e) into two differences.
The sup and Lipschitz bounds give (20), with bounded stencil shifts
absorbed in its constant. The original three kernel exponents are
(3+j,4,3+k). The two resulting majorants have exponents
(2+j,4,3+k) and (3+j,3,3+k). For each j,k in {0,1},
the first convolution has exponent 2+j; its convolution with
3+k has exponent 1+j+k. Both sums of exponents are strictly
greater than four. The endpoint shell sums add at most one
logarithm at each convolution, so (21) holds also at j=k=1
and at bounded separation. Extending positive envelopes to the
infinite lattice controls the full insertion sums, including
insertions near boundaries; no finite-volume tail is omitted.

There are 4^2 assignments of two distinct labels to four slots.
The two assignments putting both labels on one affine vertex
vanish. The other 14 are exactly 2 vertex/vertex, 8 vertex/inverse,
2 different-inverse and 2 same-inverse assignments. Each of the
last two contains both ordered products in (19). The two crossing
kernel types (23) have total curl order two and both left endpoints
within a fixed stencil of the external row. Consequently all
freezings in (18) may use the same external anchor.

For different inverse slots write their product minus the zero
frozen product as (R_--h_-R)R_+ + h_-R(R_+-h_+R), with the
appropriate endpoint operations on each factor. This uses one
localization error in each summand, not the square of such an
error. It gives N^-1 l(r)^2 k_5(r). Vertex/inverse and
vertex/vertex assignments have the smaller displayed logarithmic
majorants; same-inverse assignments use (21) and give the same
k_5 bound. In every case the total curl order is what makes the
exponent five. Its external row sum is bounded uniformly by
sum_{j>=0} O((1+j)^-2 log(e+j)^2).

The quartic has only the three terms (24). Each uses one actual
plaquette and the uniform coefficient sum imported from L300's
quartic estimate. At its bounded slot separations, (18),(21)
and the same zero source product give an O_f(N^-1) entry bound.
The mixed density derivative is zero. This proves (25) for the
complete Z_-+. For real sources Z(s,t) is symmetric: its B/B
part is the symmetric quadratic-tensor contraction, and its other
parts are symmetric. Its mixed derivative therefore has the same
column bound. Schur's estimate proves the claimed norm bound
without a second frozen-anisotropy derivative or a boundary deletion.

**Every external curl.** The weighted estimates (26) hold for
the separate A and B quadratic polynomials on all edge vectors.
This follows from the full monomial estimates of L287, as made
explicit in L300(22): bounded weights multiply the coefficient
vectors without differentiating them. Each polynomial is centered
because its two internal colors differ. If it is written x*M*x/2,
its variance is half the squared Hilbert--Schmidt norm of
G^(1/2) M G^(1/2), by the imported finite Wick formula.
For either inverse slot, a source derivative acts on the transformed
tensor by Z_X or Z_Y from L297(10); the mixed slot is the sum of
both orders and has norm at most 2F^2. Tensor Cauchy--Schwarz
therefore applies to each labeled assignment, without assuming
positivity or commutation of these insertions. Subtracting B/B
leaves exactly AA, AB and BA, giving (27) on the full H after
(16). The color argument and factor 1/4 are unchanged. Combining
this with (17),(25) verifies (4) for every source order.

**All weighted low residues and the scalar rate.** A direct way
to check the half-power placements in L297(19) is to put
T(z)=Ahat^(1/2) S_N(z) Ahat^(1/2). On the scaled low circle,
T and its required z derivatives are uniformly bounded by the
spectral gap. The weighted resolvent is
P_N/(z-1)+T(z). Each weighted first or mixed derivative is a
product of two or three such factors with bounded M_i between
them, with a minus sign for the first derivative and a plus sign
for each mixed order. This follows by inserting
B_i=Ahat^(1/2)M_i Ahat^(1/2), so no half-power is moved through
M_i.

For a first derivative the PP term has a double pole, the two
one-P terms have simple poles, and the no-P term is analytic.
For each mixed order, PPP has a triple pole; the three two-P
placements have double poles and include derivatives of their
analytic coefficients; the three one-P placements have simple
poles. The no-P term is analytic. Every nonzero coefficient and
needed derivative contains a rank-four P_N between uniformly
bounded factors, hence has bounded weighted trace norm. The
residues use f_theta(1), f_theta'(1), f_theta''(1), bounded by
C(1+theta)^k exp(-theta), k<=2. This verifies (28) with all
off-ground terms and the factor lambda_0^-1. The fixed contour
already differentiates the whole moving cluster, including any
internal splitting; no individual eigenbranch argument is used.

In (29), cyclicity pairs Ahat^-1/2 Wtilde_alpha Ahat^-1/2
with Ahat^(1/2) H_beta^lo Ahat^(1/2). Finite trace duality
applies without positivity. There are exactly four product-rule
terms and three external colors; internal colors and the two source
orders have already been counted. Since
12/N^2<=lambda_0<=3pi^2/N^2 and theta_N=(3/2)log N>=1
for N>=2, (30) is bounded by
C_f[N^-1/2 ell_N^2+N^-1/2 ell_N^(5/2)+N^-3/2 ell_N^3].
The final term is absorbed uniformly into the middle one, which
tends to zero. Thus the complete scalar has exactly the claimed
rate, not only a vanishing largest-pole contribution.

No new mathematical dependency is added to the DAG. The audit
accepts a local perturbative input under its upstream premises;
it supplies no high-contour estimate, full tail control, uncut
bound, uniform higher remainder or interacting continuum/mass
construction. Full matching Mathlib coverage remains not checked.

## Mathlib

Full matching Mathlib coverage for the relative-grid signed form bound,
mixed Wilson contractions and complete low-contour response has not
been checked. The finite Gaussian and spectral results are imported
from the precise sources above; their use does not assert a matching
Mathlib theorem. The new local content is the finite-grid energy-form
specialization, complete separated mixed-source estimate and their
application to L297's existing moving contour, under all stated inputs.
