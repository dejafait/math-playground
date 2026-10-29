# L291 — Complete distinct-line cubic limit and quadratic-scale cancellation

## Hypotheses

Use L280's SU(2) relative cube D=[-4,4]^4, even N>=2 and a=8/N.
Pin every boundary-contained link, fix gauges at boundary vertices,
and retain all variable links, including both normal endpoint cases.
Use Euclidean counting measure and three colors. Pinned slots are zero.
Keep L290's exact nonnegative product sources h_+=f_*, h_-=theta f_*,
supported in [-1/4,1/4]^3 times [1,2] and [-2,-1], respectively.
Source derivatives are evaluated at zero in
(|s|+|t|)||f_*||_infinity<eta<1. Write F=||f_*||_infinity.

All ambient all-link Wilson jets remain on L280's own slice. In the
notation of L287(1), with every orientation and actual signed slot,

\[
 V(x)=T[x,x,x]/6=\sum_p(Cx)_p\cdot\zeta_p(x).
                                                               \tag{1}
\]

Use G,G_pm from L280(18), L=C*C+BB*, and the scalar integrals Z_0,I_1
of L289, with I_1=Z_0/2-1/16. The functional J_f is exactly L284(2).
There is no additional a^4 weight in a plaquette sum. L287–L290 are
inputs whose separate critical audits remain outstanding; this proof
does not discharge those audits or the qualifications they inherit.

## Conclusion

The entire last group of L280(20) satisfies

\[
 \boxed{\displaystyle
 D_{3,N}:=\tfrac12\mathcal B(T,T;G_-,G_+,G)\ge0,\qquad
 \lim_{N\to\infty\atop N\ {\rm even}}N^{-2}D_{3,N}
       =\frac{22Z_0-3}{128}\mathcal J_f .}                  \tag{2}
\]

The limit includes o(N^2) error for the complete two-vertex sum.
All cross-half vertex pairs, source noise modes, boundary anchors,
normal links, colors and Wilson offsets are retained in the estimates.
Combining (2) with L290(3)–(4) proves

\[
 \boxed{\displaystyle N^{-2}\kappa_a\longrightarrow0.}    \tag{3}
\]

Equivalently, the complete cubic leading coefficient is the negative
of L285(4)'s complete quartic-plus-density coefficient. This is only
an o(N^2) estimate for the fixed-mesh perturbative coefficient. It is
not a logarithmic bound, a mesh-uniform higher remainder, an interacting
lower bound, a continuum construction or a mass-gap result. The separate
critical audit in section 6 accepts this argument conditional on its
stated inputs; it does not discharge the outstanding L286–L290 audits.
This verification is local progress, not a claim of certified originality
beyond the previously checked sources.

## Proof

### 1. Exact positive square and the time-half decomposition

Put U_h=GC_12^*W_h=L^-1 C_12^*W_h, W_h=diag(sqrt(h)).
On a common probability space take independent standard source noises
xi_-,xi_+ and a centered field x of covariance G, with three independent
colors in each. Set y_pm=U_pm xi_pm. Thus Cov(y_pm)=G_pm and

\[
 2D_{3,N}=\mathbb E[T[y_-,y_+,x]^2].                       \tag{4}
\]

This is just the product of the three independent covariance matrices
in the definition of mathcal B; no Wick multiplicity is added.
Also G_h<=F G: on H, G^(1/2)C*C G^(1/2)=I, and
C_12^*diag(h)C_12<=F C*C. These inequalities extend by zero
on im B and independently over colors.

Partition all plaquettes by center time <=0 or >0, denoting their
indicators by w_- and w_+. Let chi_pm select all edges incident to
the corresponding half's plaquettes. The indicators only weight the
vertices; no difference is applied to either indicator. Polarizing
(1) gives, exactly,

\[
 \begin{split}
 T_w[u,y,x]&=A_w(u;y,x)+B_w(u;y,x),\\
 A_w(u;y,x)&=\sum_p w_p(Cu)_p\cdot D\zeta_p(y)[x],\\
 B_w(u;y,x)&=\sum_p w_p\big\{(Cy)_p\cdot D\zeta_p(x)[u]
                         +(Cx)_p\cdot D\zeta_p(y)[u]\big\}.
 \end{split}                                                   \tag{5}
\]

The derivative of a quadratic zeta is symmetric in its two arguments.
Consequently the full random variable in (4) is A+B, where

\[
 \begin{split}
 A&=A_{w_-}(y_+;y_-,x)+A_{w_+}(y_-;y_+,x),\\
 B&=B_{w_-}(y_+;y_-,x)+B_{w_+}(y_-;y_+,x).
 \end{split}                                                   \tag{6}
\]

In each summand the external field is the source remote from that
half. There is no assumption that the two half summands are independent.

### 2. Whole-half estimates and removal of the remote curl

For either half and its remote source, L285 section 2 extends the exact
L284(8) kernel to all its spatial anchors and time endpoints. It gives
uniform bounds for R_a and its first derivatives, with a summable mode
majorant C(1+|k|)exp(-|k|/16). The source map has entries
a^3 R_a sqrt(h). An unscaled curl is a difference over distance a,
and therefore has entries bounded by C_f a^4 on the selected half.
The tangential pinned slots agree with the vanishing sine factors;
components 3 and 4 of U_h vanish exactly. Thus these bounds also apply
to curls using a pinned slot and to both normal-link endpoint cases.

There are O(N^4) rows and source columns. Squaring entries and summing
over the entire rectangular matrices proves

\[
 \|\chi_-U_+\|_{\rm HS}^2+\|\chi_+U_-\|_{\rm HS}^2\le C_fN^2,
 \qquad
 \|w_-CU_+\|_{\rm HS}^2+\|w_+CU_-\|_{\rm HS}^2\le C_f.
                                                               \tag{7}
\]

For fine meshes the separation is at least 1/2. Finitely many coarser
even meshes are included by increasing the constants. No source tail
or vertex pair was truncated in (7).

Here are the needed bilinear specializations of L287's polynomial
bounds. For fixed u, independent x with covariance G and y with
covariance G_h<=FG obey

\[
 \mathbb E|A_w(u;y,x)|^2\le C F\log(eN)\|wCu\|^2,
 \qquad
 \mathbb E|B_w(u;y,x)|^2\le C F\|\chi_wu\|^2.             \tag{8}
\]

To justify the specialization, first take y and x to have covariance
G. The two bilinear forms in (5) are the polarizations of L287(3)'s
quadratic forms, with weight w_p inserted. Each quadratic form is
centered by its two distinct field colors. For a centered quadratic
form z^TKz, its polarization is 2y^TKx. The independent-field second
moment is 4 Tr(KGKG), twice the quadratic second moment. L287's proof
for the external-curl part bounds the coefficient vector wCu; its
internal-curl proof bounds the edge-slot vector w_pu_e(p), whose norm
is at most a fixed multiplicity times ||chi_wu||. Both arguments allow
arbitrary weights |w_p|<=1. Finally a bilinear second moment is
monotone in each positive covariance separately, so replacing one G
by G_h<=FG multiplies the upper bound by at most F. This establishes
(8) without asserting that weighted tensors have the same row sums.

Condition on the remote field, which is independent of the other two
fields, and apply (7)–(8). The L2 triangle inequality, including the
cross-half terms, gives

\[
 \|A\|_2\le C_f\sqrt{\log(eN)},\qquad \|B\|_2\le C_f N,
 \left|D_{3,N}-\tfrac12\mathbb E B^2\right|
          \le C_f\{N\sqrt{\log(eN)}+\log(eN)\}.            \tag{9}
\]

In particular the complete group is O_f(N^2). The remote-curl removal
has o(N^2) error, before making any internal approximation.

### 3. Coupled source-factor approximation with a uniform error

Use L288's polynomial h_m and write M=m+1, r_m=1-Lh_m(L).
All functional calculus here is on the actual finite relative matrix L.
On the same probability space define

\[
 y_{h,m}=h_m(L)C_12^*W_h\xi_h,\quad
 y_{h,r}=y_h-y_{h,m}=r_m y_h,\quad
 x_m=Lh_m(L)x,\quad x_r=r_m x.                             \tag{10}
\]

The retained and residual fields within a pair need not be independent.
The x fields remain independent of all source fields. Put
hat G=C*C h_m(L)^2 and R=G-hat G, as in L288. Cov(x_m)=hat G,
Cov(x_r)=r_m^2G<=R, since for 0<=r<=1, r^2<=2r-r^2.
Furthermore

\[
 \begin{split}
 H_{h,m}:=\operatorname{Cov}(y_{h,m})
      &=h_m(L)C_12^*\operatorname{diag}(h)C_12h_m(L)
         \le F\widehat G,\\
 \operatorname{Cov}(y_{h,r})&\le F r_m^2G\le F R.
 \end{split}                                                   \tag{11}
\]

The first inequality is a congruence of C_12^*hC_12<=FC*C;
the second uses G_h<=FG and congruence by r_m. No commutation
between the source weight and L is used.

L288(6),(10) now supplies for each residual covariance S, after
factoring out F for a source residual,

\[
 \sup_e S_{ee}\le960/M,\quad
 \sup_p(CSC^*)_{pp}\le122880/M^2,\quad \|CSC^*\|\le1.
                                                               \tag{12}
\]

Each retained covariance has norm <=M/16 and curl norm <=1, again
with the factor F for a source field. These estimates include every
boundary row. They do not claim a small operator norm for a residual.

For fixed u, expand
B_w(u;y_h,x)-B_w(u;y_{h,m},x_m). Apart from fixed slot/color
coefficients, its six types are

\[
 (Cy_{h,m})x_r,\quad (Cx_m)y_{h,r},\quad
 (Cy_{h,r})x_m,\quad (Cx_r)y_{h,m},\quad
 (Cy_{h,r})x_r,\quad (Cx_r)y_{h,r},                         \tag{13}
\]

each multiplied by w_pu_e(p). Every product contains independent
fields from the x and source families. Its covariance over p,q is
the entrywise product of a curl covariance and a selected edge
covariance. L287(11)'s positive Schur estimate bounds the first,
second, fifth and sixth types by a curl norm O(1) times a residual
edge diagonal O(M^-1). For the third and fourth types, interchange
the factors: use the retained edge operator norm O(M) and residual
curl diagonal O(M^-2). The fixed edge-selection multiplicity only
changes constants. Thus all six squared L2 norms are at most
C F M^-1||chi_wu||^2. A finite L2 triangle bound retains every
cross term between types, including correlations between a retained
field and its residual. Hence

\[
 \mathbb E|B_w(u;y_h,x)-B_w(u;y_{h,m},x_m)|^2
       \le C F M^{-1}\|\chi_wu\|^2.                       \tag{14}
\]

Let B_m be (6)'s B with the near source and x replaced as in (10)
in each half, leaving its remote source unchanged. Conditioning on
that remote source and applying (7),(14) proves
||B-B_m||_2<=C_f N/sqrt(M). Also ||B_m||_2<=C_f N by (9),(14).
Consequently the COMPLETE normalized error is

\[
 \left|N^{-2}D_{3,N}-\frac1{2N^2}\mathbb E B_m^2\right|
 \le C_f\left\{M^{-1/2}+\frac{\sqrt{\log(eN)}}N
                              +\frac{\log(eN)}{N^2}\right\}.
                                                               \tag{15}
\]

This uses all internal anchors and source modes at once. It is stronger
than local entry convergence and does not differentiate a covariance
approximation error without estimating it.

### 4. Fixed-range separation and the bulk tensor

Fix m. The source map h_m(L)C_12^*W_h has finite lattice range.
Thus y_{h,m}, and every vertex where it or its curl occurs, is supported
within cM lattice steps of supp h. For sufficiently large N, all such
vertices lie strictly in the corresponding time half and away from
every spatial and temporal boundary. The half restriction can then
be removed from its retained amplitude with exact equality.

Also hat G=C*C h_m(L)^2 is a finite-range covariance. The two retained
half amplitudes have zero cross expectation for sufficiently large N:
every x_m slot or curl in one is farther than its covariance range
from every x_m slot or curl in the other. Conditional on both source
noises, the expectation over x_m alone is zero. This argument does
not assume independence of the full source fields or discard their
cross covariance. Therefore, eventually at each fixed m,

\[
 \mathbb E B_m^2
  =\operatorname{Tr}(E_{-,m}G_+)
   +\operatorname{Tr}(E_{+,m}G_-),                         \tag{16}
\]

where, over all plaquettes,
u^*E_{h,m}v=E[B(u;y_{h,m},x_m)B(v;y_{h,m},x_m)].
These are positive finite-range matrices, linear in the source weight
h through H_{h,m}. Their rows are supported in a fixed-range source
neighborhood. In the interior their coefficients are exactly the
bulk polynomial coefficients. Global color rotations make their
color blocks identical with off-color blocks zero, as in L287.

Compute the bulk row sum with the source weight equal to one on all
12-plaquettes. Use L289(5)–(7)'s exact constant-field Wilson matrix
K_u=-iH_u tensor J_A for one external unit color A. In midpoint
Fourier coordinates put

\[
 d_\mu=2\sin(q_\mu/2),\quad\lambda=|d|^2,\quad
 P=I-dd^T/\lambda,\quad
 v_{12}=d_1e_2-d_2e_1,\quad s_u=\sum_\mu u_\mu\sin q_\mu.
\]

The two independent internal covariances have multipliers
Gamma_x=lambda h_m(lambda)^2 P and
Gamma_y=h_m(lambda)^2 v_12 v_12^T. Since the polarization of
x^TK_ux is 2y^TK_ux, its independent-field second moment is
4 Tr(K_u Gamma_x K_u Gamma_y). Now PH_uP=s_uP,
Pv_12=v_12, and (-i)^2 Tr(J_A^2)=2. The entire constant-field
row-sum quadratic form, with normalized Brillouin measure, is therefore

\[
 8\int_{[-\pi,\pi]^4}\lambda h_m(\lambda)^4
          (d_1^2+d_2^2)\left(\sum_\mu u_\mu\sin q_\mu\right)^2
                         \frac{dq}{(2\pi)^4}.             \tag{17}
\]

One can obtain (17) first on odd periodic tori larger than the complete
path range and then pass to the integral, exactly as in L289's
finite-range row-sum calculation. This auxiliary computation does not
change the relative-box covariance. The raw-edge phases and endpoint
averages are retained in K_u; no scalar propagator replacement is made.

Oddness in each coordinate eliminates off-direction entries. Exchange
of coordinates 1 and 2 makes their two diagonal entries equal to

\[
 \beta_m=8\int\sin^2q_1\,\lambda h_m(\lambda)^4
                       (d_1^2+d_2^2)\frac{dq}{(2\pi)^4}.
                                                               \tag{18}
\]

Only these entries are needed because the remote source map has
components 3 and 4 identically zero. Since 0<=lambda h_m<=1,
the integrand is bounded by 8 sin^2(q_1)(d_1^2+d_2^2)/lambda^3
<=8/lambda, integrable in four dimensions. Dominated convergence gives

\[
 \beta_m\longrightarrow
 \beta=8\int\frac{\sin^2q_1(d_1^2+d_2^2)}{\lambda^3}
                                               \frac{dq}{(2\pi)^4}.
                                                               \tag{19}
\]

### 5. All source sums, normalization and the integral evaluation

For fixed m, the matrix E_{h,m} has finitely many offsets per row,
bounded coefficients, and a source-neighborhood support with fixed
physical volume. Every weight h(z) in an entry lies within c_m a
of its external row center x_i. Freezing it at h(x_i) has error O_m(a),
including rows adjacent to the support boundary, by smoothness of h.
Freezing the neighboring remote kernel at x_i has the same error by
the full-half derivative estimate used in (7). All paths are in the
interior once N is sufficiently large at this fixed m. Thus, writing
V_a(x,y)=(R_{a,mu}(x,y))_mu, the scalar color block obeys

\[
 (E_{h,m}V_a(\cdot,y))_i
   =h(x_i)(R_m V_a(x_i,y))_{\mu_i}+O_{m,f}(a),             \tag{20}
\]

uniformly on its source neighborhood and the remote support, and both
sides vanish outside a fixed compact neighborhood. Here R_m is (17)'s
direction matrix. On V_a it acts as beta_m since V_a has only
components 1 and 2. The finite coefficients and offsets justify the
complete row error in (20), rather than a limit of one selected entry.

As in L290(25), the exact trace normalization is

\[
 N^{-2}\operatorname{Tr}(E_{-,m}G_+)
 =\frac3{64}a^8\sum_{i,z}h_+(z)R_{a,\mu_i}(x_i,z)
                         (E_{-,m}V_a(\cdot,z))_i.          \tag{21}
\]

The three counts external colors only; the internal color sum is
already in (17). The original trace has factors a^6 from its two
source maps, and N^-2=a^2/64, giving a^8/64. Uniform convergence
on separated supports and Riemann sums on the actual component grids
therefore give

\[
 \lim N^{-2}\operatorname{Tr}(E_{-,m}G_+)
       =\frac{3\beta_m}{64}\mathcal J_f.                  \tag{22}
\]

The summed O_m(a) error tends to zero because the two physical grid
volumes are bounded. Time reflection gives the identical limit for
the other trace, with the same J_f by L284's reflected kernel identity.
Equations (15),(16),(22), first N to infinity at fixed m and then
m to infinity, prove

\[
 \lim N^{-2}D_{3,N}=\frac{3\beta}{64}\mathcal J_f.          \tag{23}
\]

It remains to evaluate the particular weighted integral in (19).
All integrals in the following calculation have measure dq/(2pi)^4.
Put A_1=int sin^2q_1 d_1^2/lambda^3,
A_2=int sin^2q_1 d_2^2/lambda^3,
J_11=int d_1^4/lambda^2 and J_12=int d_1^2d_2^2/lambda^2.
Coordinate symmetry and sin^2q_1=d_1^2-d_1^4/4 give

\[
 A_1+3A_2=I_1,\qquad
 J_{11}=Z_0-4I_1,\qquad J_{11}+3J_{12}=1/4.              \tag{24}
\]

Here int d_1^2/lambda^2=Z_0/4 and int d_1^2/lambda=1/4.
Integrate the derivative in q_1 of sin(q_1)d_2^2/lambda^2:

\[
 4A_2=\int\frac{\cos(q_1)d_2^2}{\lambda^2}
      =Z_0/4-J_{12}/2,
 \quad
 A_2=\frac{5Z_0-8I_1-1/2}{48}.                            \tag{25}
\]

This integration is legitimate on the periodic cube minus a small
ball about zero: the vector component is O(|q|^-1), so its small-sphere
flux is O(epsilon^2), and each differentiated term is O(|q|^-2),
integrable in four dimensions. Opposite outer faces cancel (the sine
vanishes there). Thus no singular boundary term was omitted.
Combining (24)–(25), and using the already justified scalar identity
L289(16), yields

\[
 \beta=8(A_1+A_2)=8(I_1-2A_2)
       =\frac{64I_1-10Z_0+1}{6}
       =\frac{22Z_0-3}{6}.                                \tag{26}
\]

This evaluates a new weighted numerator needed here; it does not
reprove the imported formula for I_1. Substitution in (23) proves (2).
Finally L290(4) gives the same coefficient with the opposite sign for
all remaining cubic, quartic and density groups. Its o(1) remainder
and the one just proved give (3). No rate stronger than o(N^2) follows.

### 6. Separate critical audit (2026-10-26)

**Verdict and scope.** Equations (2)–(3) pass under the exact hypotheses
above, conditional on the stated L280, L284, L285 and L287–L290 inputs.
Their inherited L286 input and outstanding L286–L290 audits remain
unresolved. This audit checks the new source-factor specialization and
the assembly with L290(3)–(4); it is not a separate acceptance of those
upstream results. It uses the pre-invocation EXPLORE assessment for this
exact critical audit, reuses its literature comparison, and introduces
no new theorem, lemma input, or mathematical script. Acceptance verifies
an existing partial result, not a new discovery or a complete solution.

**Exact square and all boundary rows.** L280(20)'s prefactor is 6/12.
Since the three fields in (4) belong to independent families, expanding
their square gives exactly one covariance for each family and hence
mathcal B(T,T;G_-,G_+,G). There is no extra Gaussian pairing factor.
The third derivative of V=(Cx) dot zeta(x), with zeta quadratic, is
exactly the three terms of (5). This also checks that its bilinear
B is the polarization of L287's quadratic mathsf B, with no extra
factor in the half decomposition.

For fine meshes every slot of a negative-half plaquette has time at
most a/2, so its distance in time from supp h_+ is at least 1/2;
the reversed statement holds on the other half. L285 section 2's
hyperbolic estimate is uniform on the closed spatial box and at both
time endpoints. Its summable first-derivative bound therefore controls
the difference between the two parallel edges forming each curl. A
pinned tangential entry is its exact zero sine value, rather than an
arbitrary zero extension. Normal direction-1 and direction-2 edges
keep their cosine grids; source components 3 and 4 are exactly zero.
Thus every entry of the restricted U is O_f(a^3) and every entry of
the restricted CU is O_f(a^4). There are O(N^4) rows and O(N^4)
source columns, giving O(N^8 a^6)=O(N^2) and O(N^8 a^8)=O(1)
for their squared Hilbert–Schmidt norms. The finitely many coarser
even meshes have finite covariances and are absorbed in the constants.
No boundary layer, curl slot or source tail is removed.

For a real symmetric quadratic-form matrix K, the centered same-field
variance is 2 Tr(KGKG), whereas its polarization 2y^T Kx has
independent-field second moment 4 Tr(KGKG). The centering here follows
from the distinct colors in each L287 monomial. The proof of L287(12)
works with coefficients w_p(Cu)_p and w_pu_e(p); it does not require
translation invariance or apply a derivative to w. Finally, for any
bilinear matrix M, Tr(M G M^T H) is monotone in positive H, which
justifies replacing one covariance by G_h<=FG. These facts prove (8)
for arbitrary fixed u with precisely the restricted norms appearing
there. Conditioning separately in each half is valid because its
remote-source family is independent of its near-source family and x.
The L2 triangle and Cauchy–Schwarz inequalities then give (9) for the
complete two-half variable, including all its cross terms.

**Common-noise error without false independence.** Write r=r_m(L).
On H, G=L^-1 and Lh_m=1-r, while G and C*C vanish on im B.
Hence Cov(x_m)=(Lh_m)G(Lh_m)=C*C h_m(L)^2 and
Cov(x_r)=r^2G. The scalar inequality r^2<=2r-r^2 proves the residual
comparison with R. Also y_{h,m}=(1-r)y_h. Its covariance is bounded
by F widehat G by congruence of C_12^*hC_12<=FC*C; the residual
comparison follows by congruence of G_h<=FG with r. Neither argument
commutes the source weight with L or assumes independence within a
retained/residual pair.

Expanding both internal-curl terms of B gives all six products in
(13). Each individual product still pairs an x-family field with a
source-family field, so its second moment is a positive Schur product.
Let S select the particular edge slot of a monomial. Its multiplicity
is uniformly bounded, ||S||^2<=mu. For products 1, 2, 5 and 6, the
curl covariance norm is at most 1 (or F), and the selected residual
edge diagonal is at most 960/M (or F times that bound). For products
3 and 4, use instead the retained selected-edge norm at most mu M/16
and the residual curl diagonal at most 122880/M^2, with exactly one
factor F. In every case the Schur norm is at most C F/M. The
coefficient norm satisfies sum_p |w_pu_e(p)|^2<=mu||chi_wu||^2.
There are a fixed number of slots, colors and monomial types; the
finite L2 triangle bound thus proves (14), retaining correlations
between types and between retained and residual fields.

Conditioning on each remote family and using (7) yields
||B-B_m||_2<=C_f N/sqrt(M). In particular ||B_m||_2<=C_f N uniformly
in m,N, from (9) and M>=1. Applying
|E B^2-E B_m^2|<=||B-B_m||_2(||B||_2+||B_m||_2)
and then (9) proves the full error (15). This uses only residual
diagonals and retained norms, never a small residual operator norm.

**Cross-half expectation and source weights.** At each fixed m the
map h_m(L)C_12^*W_h is supported within a fixed number of lattice
steps of supp h. A plaquette contributing to B_m must contain a
near-source slot or a curl of that field, so every x_m slot in it
is within a slightly enlarged neighborhood of the same source.
The two neighborhoods are disjoint and separated by more than the
range of Cov(x_m)=widehat G for sufficiently large N. Conditional
on both source noises, the two half amplitudes are linear forms
in x_m with covariance zero. This proves zero cross expectation
before integrating the correlated source coefficients. It does not
assert independence of the full half amplitudes.

For a single half, the remaining remote field is independent of its
near field and x_m; this gives its trace in (16). The matrix E_{h,m}
is positive, finite range, and linear in h: its source covariance is
h_m(L)C_12^*diag(h)C_12h_m(L), even though its random-field factor
contains sqrt(h). Weight freezing therefore uses the smooth function
h itself; no regularity assertion for sqrt(h) is required. Every
path of a nonzero row lies in the interior once N is large at this
fixed m, since the source support has positive distance from every
face. A larger fixed compact neighborhood contains all these rows;
elsewhere they are zero. Thus no relative boundary row is replaced
by an unjustified bulk row. Global adjoint rotations force the
external color blocks to be identical with off-color blocks zero.

**Two different internal covariances and all factors.** For constant
external u, the exact signed-slot identity in L289(4)–(7) gives the
real symmetric quadratic form K_u=-iH_u tensor J_A. Polarizing it
gives 2y^T K_u x, including the cancellation of the terms of the
form (Cx) dot [u,Cx] before or after polarization. With independent
x,y and their different covariances, its second moment is
4 Tr(K_u Gamma_x K_u Gamma_y). The factor four is from the
polarization, not from two identical-field Wick pairings.

Here Gamma_x=lambda h_m^2 P, Gamma_y=h_m^2 vv^T,
v=d_1e_2-d_2e_1, and Pv=v. Therefore
v^T H_u P H_u v=s_u^2|v|^2 by PH_uP=s_uP. The internal color
trace is (-i)^2 Tr(J_A^2)=2. Multiplication gives exactly
8 lambda h_m^4(d_1^2+d_2^2)s_u^2, as in (17); there is no
additional transverse trace of three for this rank-one covariance.
The midpoint curl and endpoint-average factors remain d_mu and
cos(q_mu/2), so s_u=sum_mu u_mu sin(q_mu) retains the Wilson phases.
At fixed m this can be evaluated on arbitrarily large odd tori
without changing any finite path coefficient of the relative-box
bulk rows. Off-direction entries vanish by oddness, and exchange
of coordinates 1 and 2 gives (18). Only these two entries act on
the remote source field. The integrable majorant 8/lambda proves
(19), with no uniform inverse approximation presumed.

**Complete Riemann sums and the ordered limit.** For fixed m, each
row has finitely many offsets and uniformly bounded coefficients.
Every contributing h(z) is within c_m a of the external row center;
so are the neighboring remote-kernel evaluation points. The full-half
first-derivative bound and smoothness of h give the uniform O_{m,f}(a)
row error in (20), including source-support-edge rows where h vanishes.
Both row and source grids have O(a^-4) points in fixed physical sets.
Their complete O_{m,f}(a) error multiplied by a^8 is therefore
O_{m,f}(a), not an error per row left unsummed.

The two source maps contribute a^6, while N^-2=a^2/64. The resulting
factor is a^8/64, and the external colors alone multiply it by three.
The internal color factor two is already in beta_m. Riemann sums
on the actual component grids thus give 3 beta_m J_f/64 for each
trace. The two reflected halves have the same limit; their factor
two cancels the original factor 1/2 in D_{3,N}. Equivalently, for
every fixed m, (15) implies

\[
 \limsup_{N\to\infty\atop N\ {\rm even}}
 \left|N^{-2}D_{3,N}-\frac{3\beta_m}{64}\mathcal J_f\right|
 \le \frac{C_f}{\sqrt{m+1}}.
\]

Together with beta_m->beta this proves (23). No estimate with m
depending on N, and no interchange of two uncontrolled limits, is used.

**Singular integral and final substitution.** In (24), symmetry gives
int d_1^2/lambda^2=Z_0/4 and int d_1^2/lambda=1/4. Hence
J_11=Z_0-4I_1 and J_12=(1/4-Z_0+4I_1)/3. Differentiating
sin(q_1)d_2^2/lambda^2 gives exactly
cos(q_1)d_2^2/lambda^2-4sin^2(q_1)d_2^2/lambda^3.
Both terms are O(|q|^-2), and the vector component is O(|q|^-1),
so the inner-sphere flux is O(epsilon^2) and tends to zero. The
outer flux vanishes. It follows that
A_2=Z_0/16-J_12/8=(5Z_0-8I_1-1/2)/48. Thus
beta=8(I_1-2A_2)=(64I_1-10Z_0+1)/6=(22Z_0-3)/6,
using precisely L289(16)'s I_1=Z_0/2-1/16. Substituting into (23)
gives (22Z_0-3)J_f/128. L290(3)–(4) has the opposite coefficient
for exactly all other groups of L280(20); its o(1) error and the
one proved here add to o(1). This accepts (3) conditionally on that
subtotal. It supplies neither a quantitative subleading rate nor
a uniform higher perturbative remainder, and cannot establish the
interacting comparison, continuum axioms or finite positive mass.

## Mathlib

Coverage of the complete relative-box Wilson result is not checked;
no absence or matching-theorem claim is made. The exact finite source
formula is reused from L280, separated relative modes from L284/L285,
Gaussian polynomial and positive Schur bounds from L287, residual
diagonals and polynomial covariance from L288, exact Wilson Fourier
matrix and scalar identity from L289, and subtotal from L290.
The additional argument is the coupled source-factor specialization,
its complete summed error, fixed-range cross-half separation, and the
weighted bulk integral (24)–(26). Only finite Gaussian identities,
positive-matrix inequalities and elementary integration are used in
that specialization. No new external kernel or renormalization theorem,
nonlinear gauge transport or exchange of unbounded limits is assumed.
