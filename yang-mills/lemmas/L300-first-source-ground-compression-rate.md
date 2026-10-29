# L300 — First-source ground compression on the relative cube

## Hypotheses

Use L297's exact SU(2) relative cube, even N>=2, a=8/N, Euclidean
counting measure, boundary-contained links pinned, gauge transformations
fixed at every boundary vertex, and all remaining links variable,
including both normal endpoint cases. Keep the fixed unweighted
transverse space H=ker B*, its orthonormal inclusion Q, and the ambient
own-slice Wilson jets of L279/L280. No nonlinear jet is transported
from another slice. The complete density D_N retains Haar and both
gauge-coordinate determinant terms and is source independent.

The two sources h_i, i in {-,+}, are exactly the reflected product
bumps of L282(1), sampled as in L279 on 12-plaquettes and zero on the
other orientations. Write C_12 for the 12 rows of the full relative
incidence C. Retain all upstream premises of the cited local results.
In particular use L297(6)--(13)'s complete contractions and inverse
derivatives, L298(9)'s exact cube kernels and its normalized ground
fields, L287's exact Wilson vertex split and energy estimates,
L283's local quartic tensor, and L299's constant-anisotropy row identity.

Let P_N be L298's rank-four one-color ground projection on H, with
lambda_0=12 sin^2(pi/(2N)), and let W_N(s,t) be exactly L297(7).
All derivatives below are at s=t=0. Internal colors are fully
contracted before passing to the one-color block. Define

\[
 V_{i,N}=Q^*(\partial_i W_N)_0 Q,
 \qquad \ell_N=\log(eN).
 \tag{1}
\]

## Conclusion

There is a constant C_f independent of even N and of i such that

\[
 \boxed{\quad
 \|P_NV_{i,N}P_N\|
 \le C_f\{N^{-1}+N^{-1}\sqrt{\ell_N}+N^{-2}\ell_N\}
 \le C'_f N^{-1}\ell_N^2,
 \qquad i\in\{-,+\}.
 \quad}                                                     \tag{2}
\]

The internal-curl cubic plus quartic derivative has ground compression
O_f(N^-1). The other terms in the first bound retain every
external-curl placement. This is a local estimate under the saved
EXPLORE assessment; originality beyond the inspected sources is not
claimed. The separate conceptual audit in section 7 accepts (2)
under the stated upstream premises, without auditing those premises
afresh or asserting any of the independent conclusions below.

It can control the all-ground parts of Tr((W_N)_- H_+) and
Tr((W_N)_+ H_-) in L297(22). It does not estimate the off-ground
residues, the mixed-source compression, the complete tail, the uncut
coefficient or uniform higher remainder. The interacting lower bound,
continuum field axioms and positive mass remain unresolved. It is not
a complete-solution candidate.

## Proof

### 1. Exact differentiated slots and source regularity

Write G=QA^-1Q*, and put

\[
 R_i=G C_{12}^*\operatorname{diag}(h_i)C_{12}G,
 \qquad R=G C_{12}^*C_{12}G.                               \tag{3}
\]

These are the exact inverse derivative and the same derivative with
constant 12-weight, on the fixed slice. In particular R_i is not
replaced by multiplication of G by a source. L297(10) gives
R_i=G^(1/2) Z_i G^(1/2), with ||Z_i||<=F=||f_*||_infinity.
All square roots and inverses refer to H and are extended by zero.

Let T_h and U_h denote the jets with plaquette weight h, and T,U
the unweighted jets. The full derivative is precisely

\[
\begin{split}
4(\partial_iW_N)_0={}&
 -\mathcal E(T_{h_i},T;G,G)-\mathcal E(T,T_{h_i};G,G)\\
 &+\mathcal E(T,T;R_i,G)+\mathcal E(T,T;G,R_i)\\
 &+\mathcal A(U_{h_i};G)-\mathcal A(U;R_i).
\end{split}                                                \tag{4}
\]

There are two distinct vertex and two distinct inverse slots in the
cubic term, and both quartic slots. The density derivative is zero.
The signs are those of the phase S-sH_- -tH_+, not those of a
positive source added to S. Formula (4) is L297's already established
finite product rule; no Gaussian differentiation theorem is reproved.

For reference the finite Wick input used in L287/L297 is
Bauerschmidt--Brydges--Slade, *Introduction to a Renormalisation Group
Method*, LNM 2242 (2019),
[arXiv:1907.05474v2](https://arxiv.org/pdf/1907.05474v2),
Propositions 2.1.6 and 2.1.9 and Corollary 2.1.11, printed pp. 31--33.
Its finite positive semidefinite covariance hypotheses hold for G on
the fixed slice. Signed slot formulas in (4) are finite multilinear
contractions, not assertions of a positive differentiated measure.

Use lattice coordinates x in [0,N]^4, so the physical point is
a x-(4,4,4,4). Evaluate h_i also away from its prescribed plaquette
sampling points, using the specified smooth bump. For either reflection,

\[
 |h_i(x)|\le F,\qquad
 |h_i(x)-h_i(y)|\le L_f N^{-1}|x-y|.                       \tag{5}
\]

This follows from L282's explicit C-infinity compactly supported
product and a=8/N; L_f may include 8||gradient f_*||_infinity.
The zero extension is smooth. The orientation restriction is always
kept in C_12 or the 12-vertex, not differentiated as a spatial weight.
Fixed stencil shifts can add a constant to |x-y| in (5).

### 2. Convolution bounds for the actual inverse insertion

Set k_b(r)=(1+r)^(-b), l(r)=log(e+r). Distances are between the
actual cell centers. A fixed translation of a cell type changes all
bounds below by a fixed constant. There are at most C(1+r)^3 cells
of a specified type in a unit shell in dimension four.

For a,b<=4 with a+b>4 and a,b>0, the cases used here satisfy

\[
 \sum_z k_a(|x-z|)k_b(|z-y|)
 \le C k_{a+b-4}(|x-y|)l(|x-y|),                          \tag{6}
\]

where l can be omitted if a,b<4. This is used for
(a,b)=(3,3),(4,3),(3,4),(4,4),(2,3),(2,4).
To verify the bound, put r=|x-y|>=2 and split into the two balls
of radius r/2 about x,y and their complement. In the first ball
the second factor is O(r^-b), while the sum of the first factor is
O(r^(4-a)) for a<4 and O(log(er)) for a=4; exchange a,b in the
second ball. The part of the complement at distance O(r) has
O(r^4) sites with both factors O(r^-a), O(r^-b). The remaining
dyadic shells of radius 2^j r sum to O(r^(4-a-b)), since a+b>4.
For r<2 summability follows directly from a+b>4. Boundedly many
orientations/offsets do not change the argument. A finite-domain sum
is bounded by the corresponding full-lattice positive sum.

Let a left endpoint operation indexed by j be identity for j=0
and any component of C for j=1; define the right operation indexed
by k similarly with C*. Write R_i^{jk}, R^{jk} and R_infinity^{jk}
for (3) with these operations, the last using full-lattice G.
This notation records actual curled kernels, not differences of a
frozen scalar product. L298(9) bounds the two factors in their
insertion-point formula by k_(3+j)(|x-z|) and k_(3+k)(|z-y|).
Thus for j,k in {0,1}, uniformly on the entire finite domain,

\[
 |R_i^{jk}(x,y)|+|R^{jk}(x,y)|+|R_\infty^{jk}(x,y)|
 \le C_f l(r)k_{2+j+k}(r),\qquad r=|x-y|.                \tag{7}
\]

For j=k=0 the logarithm can be omitted. The finite source factor
is bounded by F. The infinite convolution is absolutely convergent;
its factors have square-summable rows, so Fourier multiplication
also identifies it with G_infinity C_12* C_12 G_infinity.

For any anchor x_e within a fixed distance of the first endpoint,
subtract h_i(x_e) inside the insertion sum. Equation (5) bounds
the difference by C_f N^-1(1+|x-z|). Applying (6) with the left
exponent reduced by one gives the important estimate

\[
 |R_i^{jk}(x,y)-h_i(x_e)R^{jk}(x,y)|
 \le C_f N^{-1} l(r)k_{1+j+k}(r).                        \tag{8}
\]

The exponent pairs are (2,3), (3,3), (2,4), (3,4), respectively.
All have sum greater than four, so the far insertion region is
included, not silently cut off. Neither a variable-coefficient
Green theorem nor a frozen-inverse differentiation rule is used.

### 3. Constant-insertion transfer through all relative boundaries

For a variable edge e put d(e)=1+min_mu{x_(e,mu),N-x_(e,mu)}.
For endpoints within fixed stencil distance of external edges e,f,
with r=|x_e-x_f|<=c d(e), choose a sufficiently small fixed c>0.
When d=d(e) exceeds a fixed stencil constant, L298(9) gives

\[
 |R^{jk}(x,y)-R_\infty^{jk}(x,y)|
 \le C d^{-2-j-k}\log(ed),\qquad j,k\in\{0,1\}.         \tag{9}
\]

For j=k=0 one may omit the logarithm. Here are the insertion-point
and domain details. Split z at distance 4cd from x_e, making c small
enough that both short factors satisfy L298's nearby-stencil
comparison. All these insertion plaquettes lie in the actual cube
with the same 12-stencils as the infinite lattice; their endpoints
have depth comparable to d. The difference of the two products on
this region is bounded by

\[
 C\{d^{-3-j}k_{3+k}(|z-y|)
       +d^{-3-k}k_{3+j}(|x-z|)\}.
\]

The sum of k_3 through radius O(d) is O(d); that of k_4 is
O(log(ed)). These give d^-2 for (j,k)=(0,0), d^-3 log(ed) for
(1,0),(0,1), and d^-4 log(ed) for (1,1). Outside this region
the distances to x,y are comparable, after increasing the fixed
stencil threshold. Both absolute products are bounded by a
constant times (1+|z-x_e|)^(-6-j-k), whose tail is
O(d^(-2-j-k)). Infinite insertion plaquettes missing from the
finite domain are at distance at least d-O(1) and belong to this
tail. The finite-domain sum is simply a subset for this absolute
estimate. Thus the normal endpoints, intersections of faces and
omitted exterior insertions are all covered. Bounded d will be
handled below by the global row bounds, without this interior split.

### 4. Complete internal-curl and quartic derivative rows

Use the exact split of L287, with any bounded plaquette weight w,

\[
 D S_{3,w}(x)[u]=\mathsf A_w(u;x)+\mathsf B_w(u;x),
 \quad \mathsf A_w=\sum_p w_p(Cu)_p\cdot\zeta_p(x),\quad
 \mathsf B_w=\sum_p w_p(Cx)_p\cdot D\zeta_p(x)[u].        \tag{10}
\]

At every source value define E^int as the B/B crossing contraction,
with the same factor two as L287(13). Let K_i be the ambient
one-color derivative of (E^int-A(U;G))/4, including all four cubic
and two quartic placements of (4). Let S_N be this same derivative
for h=1 on 12-plaquettes, and S_infinity its full-lattice version.
These are auxiliary operators within this proof, not new source
families substituted for the original observable.

Each internal B/B kernel is the complete finite sum of local
slot/color coefficients multiplying

\[
 (CGC^*)_{pq}G_{fg},\qquad (CG)_{pg}(GC^*)_{fq},          \tag{11}
\]

with p,f near the external row and q,g near the external column.
This is L298(12). The two crossing pairings and L287's external
factor two are unchanged. Within-vertex pairings are zero by the
distinct internal colors, also with R_i, which is color diagonal.
Vertex derivatives multiply (11) by -h_i at one 12-vertex.
Inverse derivatives replace exactly one factor by the corresponding
R_i^{jk}. Every external pair has a bounded number of orientations,
slots and colors. Pinning deletes slots but introduces none.

Equations (7), L298(9) and quartic locality give

\[
 |(K_i)_{ef}|+|(S_N)_{ef}|+|(S_\infty)_{ef}|
 \le C_f l(r)k_6(r),\qquad
 \sup_e\sum_f(1+r)|(K_i)_{ef}|\le C_f.                  \tag{12}
\]

For example the inverse placements are R_i^{11}G, (CGC*)R_i^{00},
R_i^{10}(GC*), and (CG)R_i^{01}. Each has the stated decay.
The quartic's two external and two internal slots lie on one
plaquette, with the uniform coefficient sum of L283(9); it has
finite range and bounded entries. The first-moment assertion in
(12) uses the convergent series sum_r (1+r)^(-2)log(e+r).

Now freeze the source at x_e, after keeping the complete derivative.
For the inverse placements, (8) multiplied by the other kernel
gives C_f N^-1 l(r)k_5(r). For a vertex placement, (5) gives
C_f N^-1(1+r) times the original k_6(r) kernel; the near vertex
is within a fixed stencil of e and the other within one of f.
The quartic inverse uses (8) with j=k=0 at bounded separation,
and its vertex source is within a fixed distance of e. Hence

\[
 \sup_e\sum_f|(K_i)_{ef}-h_i(x_e)(S_N)_{ef}|
 \le C_f N^{-1}.                                        \tag{13}
\]

The radial sum here is sum_r (1+r)^(-2)log(e+r), again finite.
This includes the complete insertion-point sum before the external
column sum. No commutation of h_i with an inverse has been assumed.

We next compare complete S_N and S_infinity direction rows. For
nearby columns r<=cd, the original product differences in (11)
are bounded by sums of d^-4 k_2(r), d^-2 k_4(r), d^-3 k_3(r).
For inverse placements use (9) and (7). The additional majorants
needed, including the differences of both factors, are

\[
\begin{split}
 &d^{-4}\log(ed) k_2(r)+d^{-2}l(r)k_4(r),\\
 &d^{-2}k_4(r)+d^{-4}k_2(r),\\
 &d^{-3}\log(ed)k_3(r)+d^{-3}l(r)k_3(r).
\end{split}                                                \tag{14}
\]

The first line handles R^{11}G, the second (CGC*)R^{00}, and
the third the two one-curl placements. Summing four-dimensional
shells through O(d) gives O(d^-2 log(ed)^2): in particular
sum_{r<=Cd}(1+r)^3 l(r)k_4(r)=O(log(ed)^2), and the k_2 and
k_3 sums are O(d^2), O(d), respectively. The local quartic
difference is O(d^-2) by (9) at bounded separation and L298(9).
The vertex slots are identical in this interior region.

Far finite columns and omitted infinite columns contribute at most
C d^-2 log(ed) by (12). Omitted columns are at distance at least
d-O(1). For bounded d, use the uniform row bounds (12). Therefore,
for every row e and every direction nu,

\[
 \left|\sum_{f\parallel\nu}(S_N)_{ef}
       -\sum_{f\parallel\nu}(S_\infty)_{ef}\right|
 \le C\eta_2(d(e)),\qquad
 \eta_2(d)=d^{-2}\log(ed)^2.                              \tag{15}
\]

The second sum is over the full lattice. Every layer
k<=d(e)<k+1 has at most C N^3 edges, by the eight face slabs
and four orientations, including all their intersections. Thus

\[
 \sum_{e\ {m variable}}\eta_2(d(e))\le C N^3,           \tag{16}
\]

since sum_{k>=1} k^-2 log(ek)^2 converges. No separate face
approximation or deletion of normal endpoints is involved.

### 5. Differentiating the frozen row identity with domination

It remains to determine the infinite row in (15); a formal
derivative of L299 would not suffice. Use precisely its constant
rho family, not the nonconstant source covariance. In its midpoint
notation, v=d_1 e_2-d_2 e_1 and
kappa=lambda+(rho-1)(d_1^2+d_2^2), so L299(7) gives explicitly

\[
 -\partial_\rho\Gamma_\rho(q)
       =\frac{vv^{\mathsf T}}{\kappa^2},
 \qquad \tfrac12\lambda\le\kappa\le\tfrac32\lambda.
 \tag{17}
\]

The raw-edge unitary phases are independent of rho and are retained.
For every spatial symbol derivative of order m, the right side
has bound C_m |q|^(-2-m), uniformly for rho in [1/2,3/2]: its
numerator is quadratic and its denominator is comparable to |q|^4,
and differentiation of the smooth rational expression has the
indicated order. One or two endpoint curls raise the order by one
or two. Applying L299(9)'s annular proof to this explicit derivative
therefore gives k_2, k_3, k_4 bounds, respectively, uniformly in rho.
Differentiation of each Fourier kernel is legitimate by the
integrable order-minus-two bound (and the better curled bounds).

Consequently the derivative of every internal product (11) is
bounded by C k_6(r); the differentiated quartic is finite range
and bounded. These bounds are summable, uniformly on the rho
interval, and justify differentiation of their direction row sums
by dominated convergence. At rho=1, (17) is the Fourier product
of the two C_12-curled zero-source covariances in (3), as also
identified after (7). The affine weighted vertices have the exact
derivatives T_12,U_12. Thus S_infinity is minus the rho derivative
of (E^int_rho-A(U_rho;G_rho))/4, with all its signs and slots.

L299(5) states that the complete W_rho direction row is zero for
every such rho. L299 section 1 also proves that the AA, AB and BA
external-curl direction rows are zero, using regulated summable
products before telescoping and then dominated kernel limits. Hence
the row of
D+(E^int_rho-A(U_rho;G_rho))/4 is zero for every rho. D is
unchanged. Differentiation, now justified for these remaining
summable rows, proves

\[
 \sum_{f\parallel\nu}(S_\infty)_{ef}=0
 \quad\text{for every pair of external directions}.       \tag{18}
\]

This use of L299 requires its audited full tensor identity and
unchanged density, not just one scalar entry or an assumed gauge
equivalence. The estimates (8), (9), (13), (15) are the independent
finite-source and boundary errors needed before this frozen identity
can be used.

### 6. Ground compression and every external-curl derivative

Combine (13), (15), (18) and |h_i|<=F. For every direction nu,

\[
 \left|\sum_{f\parallel\nu}(K_i)_{ef}\right|
 \le C_f\{N^{-1}+\eta_2(d(e))\}.                         \tag{19}
\]

An ambient counting-normalized ground field has L298(18)'s exact form

\[
 v_\mu(x)=\frac{\sqrt8}{N^2}c_\mu
             \prod_{\nu\ne\mu}\sin(\pi x_\nu/N),
 \quad \|v\|=|c|,\quad
 \|v\|_\infty\le C N^{-2}|c|,\quad
 \|\nabla v\|_\infty\le C N^{-3}|c|.                    \tag{20}
\]

It is evaluated on the actual midpoint/vertex grids, including the
constant own-direction cosine and both normal endpoints. In each
direction column subtract and add v_nu(x_e). Equations (12),(19)
give

\[
 |(K_i v)_e|\le C_f\|v\|
       \{N^{-3}+N^{-2}\eta_2(d(e))\}.
\]

Pairing with another ground vector u uses at most 4N^4 edges and
(16), so

\[
 |\langle u,K_i v\rangle|
       \le C_f N^{-1}\|u\|\|v\|.                        \tag{21}
\]

This is a bilinear compression estimate, not a strong-norm estimate
on all edge vectors. The row-freezing operator need not itself be
symmetric; only its proved row error was used. The actual derivative
operator retains its exact symmetry.

Finally restore every external-curl term in (4). L287(12)'s separate
weighted bounds follow on the same domains by inserting w in its
plaquette coefficient vectors:

\[
 \mathbb E[\mathsf A_w(u;x)^2]
       \le C\|w\|_\infty^2\ell_N\|Cu\|^2,
 \qquad
 \mathbb E[\mathsf B_w(u;x)^2]
       \le C\|w\|_\infty^2\|u\|^2.                     \tag{22}
\]

For A its Schur bound is applied to w_p(Cu)_p; for B it is applied
to w_p u_(e(p)), whose squared sum is bounded by the same finite
plaquette multiplicity times ||w||_infinity^2||u||^2. The complete
finite list of types and their cross terms is retained exactly as
in L287. Thus (22) holds separately for w=1 and w=h_i even near
every boundary. In particular no derivative of the external field
times h_i is substituted for h_i Cu.

To include an inverse derivative, represent the two remaining slots
of each symmetric quadratic tensor in the G^(1/2) coordinates.
If A_w(u), B_w(u) are its symmetric matrices with
mathsf A_w=x* A_w(u)x/2 and mathsf B_w=x* B_w(u)x/2, their transformed
Hilbert--Schmidt norms squared are twice the corresponding variances
in (22). This follows from the cited two crossing Wick pairings;
the internal mean is zero by color. The cubic contraction of two
such tensors with slots X,Y is their tensor inner product with
Z_X tensor Z_Y, where X=G^(1/2)Z_XG^(1/2) and likewise for Y.
For the slots of (4), ||Z|| is 1 or at most F by (3). Thus the
same Cauchy--Schwarz bound applies to G,R_i and either vertex
derivative, with no positivity or commutation assumption.

There are exactly the four differentiated cubic placements of (4).
Removing their B/B pieces leaves AA, AB and BA in each one. From
(22) their total absolute bilinear form is bounded by

\[
 C_f\{\ell_N\|Cu\|\|Cv\|
       +\sqrt{\ell_N}(\|Cu\|\|v\|+\|u\|\|Cv\|)\}.
 \tag{23}
\]

The factor 1/4 from W and the fixed Wick factors are included in
C_f; no one of these finitely many placements is discarded. On
the ground space ||Cu||=sqrt(lambda_0)||u|| and
lambda_0<=3pi^2/N^2, so (23) is at most
C_f(N^-2 ell_N+N^-1 sqrt(ell_N))||u||||v||.
Together with (21) this proves (2). All estimates are uniform in
the two reflected sources because their sup and gradient bounds
agree. Global color invariance makes the final operator scalar in
color after the full internal contractions, exactly as in L297;
it does not delete an internal color multiplicity.

### 7. Separate conceptual audit (2026-10-29)

This audit accepts (2), including both reflected sources and the
stronger displayed rate O_f(N^-1 sqrt(log(eN))), under the exact
hypotheses above. It reuses the prior primary-source assessment and
checks the Wilson-specific argument; it is not an additional result
beyond (2) or a new verification of every upstream lemma.

**Conventions and complete differentiation.** L279(2) samples only
12-plaquettes, with no extra a^4, and L280(2) uses S-sH_- -tH_+.
Its ambient jets on the relative-Coulomb slice include every variable
normal edge. Thus differentiating the inverse of A-sK_- -tK_+ gives
the positive R_i in (3), while the vertex derivatives are -T_h and
-U_h. Applied to L297(7), these signs give exactly the four cubic
and two quartic placements in (4). The density is unchanged, not
discarded from the constant-weight identity. L283(9) supplies a
uniform finite coefficient sum and single-plaquette support for all
quartic slots. The same color-diagonal covariances make every
within-vertex cubic pairing zero; the two crossing pairings and the
factor two relating E to the quadratic Gaussian expectation remain.

**Actual inverse insertion and freezing.** L298(9) applies to
GC_12* and C_12G, with any of the stated endpoint curls. The
insertion formula therefore has exponents (3+j,3+k). For source
freezing, multiplication by |h(z)-h(x_e)| reduces the left exponent
by one, giving (2,3), (3,3), (2,4), (3,4). Each sum of exponents
exceeds four. The two endpoint balls and the remaining dyadic shells
in (6) give precisely (7)--(8), including the logarithm when an
exponent is four. In particular the infinite far insertion sum is
finite even for (2,3); no N-dependent truncation is needed. The
source's smooth zero extension and fixed stencil shifts justify
the same Lipschitz estimate at every insertion point.

For the four inverse placements in an internal crossing product,
the other factor has decay respectively k_2, k_4, k_3, k_3.
Multiplying (8) gives N^-1 l(r)k_5(r) in all four cases. Its
four-dimensional row sum is bounded by N^-1 times the convergent
series sum_r log(e+r)/(1+r)^2. A far vertex weight costs at most
C_f(1+r)/N and has the same summable majorant; a near vertex costs
only C_f/N. The quartic inverse uses (8) at bounded separation.
These facts verify (13) for the full differentiated operator,
without commuting h through G or omitting an internal source point.
The first moment in (12) uses the same convergent radial series.

**Insertion and column boundary transfers.** Choose c in section 3
small enough that the stencils within 4cd of x_e satisfy L298(9)'s
interior comparison, with depth comparable to d. In this region the
difference of the two insertion products is exactly bounded by
d^(-3-j) k_(3+k)+d^(-3-k) k_(3+j). Their sums are d^-2 for
j+k=0, d^-3 log(ed) for j+k=1 and d^-4 log(ed) for j+k=2.
Outside that region, r<=cd makes the two insertion distances
comparable, and the absolute tail is O(d^(-2-j-k)). Every omitted
infinite insertion is in this latter region. This verifies (9)
without a scalar or one-face boundary substitution.

For nearby external columns, the R^11 G product has the two
majorants d^-4 log(ed) k_2 and d^-2 l(r) k_4. The (CGC*)R^00
product has d^-4 k_2 and d^-2 k_4. Each one-curl product has
d^-3 log(ed) k_3 and d^-3 l(r) k_3. With shell counts O((1+r)^3),
their sums through Cd are at most O(d^-2 log(ed)^2). Undifferentiated
vertex products satisfy the smaller bounds stated before (14).
The quartic comparison uses local covariance entries only. Far and
omitted columns contribute O(d^-2 log(ed)) by (12); bounded-depth
rows use its uniform row bound. This checks (15). Each depth layer
contains at most C N^3 variable edges, including intersections of
faces and both normal endpoints. Since sum_k k^-2 log(ek)^2 is
finite, the full defect sum is O(N^3), as required in (16).

**Legitimate differentiation of the zero row.** Direct differentiation
of L299(7), using kappa=lambda+(rho-1)|v|^2, gives (17) with its
minus sign. The raw-edge phases are rho independent. On the fixed
rho interval this derivative has symbol order -2; endpoint curls
give orders -1 and zero, and all spatial symbol derivatives obey
the corresponding uniform bounds. L299's annular argument then
gives k_2, k_3 and k_4 decay for these derivative kernels, including
the order-zero endpoint case. Fourier differentiation is dominated
by an integrable |q|^-2 bound. Thus the rho derivative of each
internal crossing product is bounded by C k_6, and the quartic
derivative is local and bounded. Their full direction row sums can
be differentiated by dominated convergence.

For the external-curl rows L299 first uses regulated products with
summable rows, telescopes their external differences, and then takes
the uniformly summable kernel limit. Hence their rows vanish for
every rho, not merely at rho=1. Subtracting them from the complete
zero row and retaining the rho-independent D leaves the internal
identity used here. The derivative of this identity has all the
constant-insertion and affine vertex slots, and its negative is
S_infinity. This proves (18) with the actual source sign. No
nonconstant-weight identity has been inferred from L299.

**Normalization and external-curl terms.** In each direction the
ground field has N own-direction midpoint samples and three sine
squared sums N/2. The factor 8/N^4 in its squared amplitude makes
its norm exactly |c|. Its sup and Lipschitz bounds are respectively
O(N^-2)|c| and O(N^-3)|c|, on the actual relative grids. The
first-moment error paired with u is O(N^-2 N^-3 N^4)=O(N^-1).
The boundary term pairs to O(N^-4 N^3)=O(N^-1). These are bilinear
compression estimates; a small strong-norm error on all fields is
not used.

L287's separate monomial bounds also permit weights: replace its
coefficient vectors by w_p(Cu)_p and w_p u_e. Their squared norms
increase by at most ||w||_infinity^2, and their plaquette-to-edge
multiplicities remain bounded. The finite sum of monomial types
retains cross terms by L2 Cauchy--Schwarz. This proves (22) with
no derivative falling on w. For a centered symmetric quadratic
polynomial x*Mx/2 its variance is half the squared Hilbert--Schmidt
norm of G^1/2 M G^1/2. Each inverse insertion acts on one tensor
factor by Z_i, whose norm is at most F. Tensor Cauchy--Schwarz
therefore gives the same bounds for either inverse slot, as well
as for either weighted vertex. Removing B/B from each of the four
cubic placements leaves exactly AA, AB and BA. Their bounds are
the three terms in (23), with no missing color or source slot.
On the ground space ||Cu||=sqrt(lambda_0)||u|| and
lambda_0<=3pi^2/N^2, giving O_f(N^-2 ell_N+N^-1 sqrt(ell_N)).
Together with (21) this verifies the complete asserted rate.

No mathematical script or numerical diagnostic is needed for this
audit. It adds no mathematical dependency to the existing DAG row.
It accepts a relevant local input, not mixed-source or off-ground
control, a full tail estimate, an uncut bound, a uniform higher
remainder, or the interacting continuum/mass construction.

## Mathlib

Full matching Mathlib coverage for (2), the Wilson contractions and
the relative-cube source/boundary estimates has **not been checked**.
No absence is inferred. Finite Gaussian contraction and inverse-slot
identities are imported from the precise source/local results above;
the new work is the quantitative Wilson-specific localization and
complete compression argument, not a reproof of those general facts.
