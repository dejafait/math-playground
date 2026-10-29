# L287 — Energy bound for the complete cubic mixed-covariance action term

## Hypotheses

Use L280's SU(2) relative cube [-4,4]^4, even N>=2, a=8/N,
boundary-contained pinned links, boundary-fixed gauges, and every
variable normal link at both endpoints. Keep all three colors and
L002/L282's exact nonnegative product bump h_+=f_*, h_-=theta f_*.
The supports are [-1/4,1/4]^3 times [1,2] and [-2,-1]. Source
derivatives are at zero in (|s|+|t|)||f_*||_infinity<eta<1.

All matrices use Euclidean counting measure. C is the complete relative
plaquette incidence, G is L280(18)'s extended transverse covariance,
and the all-link cubic Wilson jet on that same slice is
V(x)=S_3^H(x)=T[x,x,x]/6. Pinned slots are zero; no forest slots are
deleted. Use L286(4)–(5)'s exact polynomial on every plaquette:

\[
 V(x)=\sum_p (Cx)_p\cdot\zeta_p(x),\qquad
 \zeta_p(x)^ct^c=\tfrac12\sum_{j<k}[X_{p,j},X_{p,k}].       \tag{1}
\]

The ordered signed X_{p,j} are the actual four link matrices.
The algebraic identity in L286 applies to all orientations, even
when some pinned slots vanish. The sources restrict insertions to
12-plaquettes, but the action sum in (1) is over every plaquette.
L286's separate audit accepts this jet under its stated hypotheses.
No assertion about its separated estimate is needed here.

## Conclusion

Write ell_N=log(eN). There is a constant K independent of N such that
the positive symmetric matrix

\[
 (E_N)_{il}=\sum_{j,k,m,n}T_{ijk}T_{lmn}G_{jm}G_{kn}
\]

obeys, for every real edge/color vector u,

\[
 0\le u^*E_Nu\le K\{\|u\|^2+\ell_N\|Cu\|^2\}.           \tag{2}
\]

Define the exact quadratic random polynomials, for x with covariance G,

\[
 \mathsf A(u;x)=\sum_p(Cu)_p\cdot\zeta_p(x),\qquad
 \mathsf B(u;x)=\sum_p(Cx)_p\cdot D\zeta_p(x)[u].           \tag{3}
\]

Let E_N^int be defined by
u^*E_N^int v=2 E[mathsf B(u;x)mathsf B(v;x)]. Then

\[
 0\le E_N^{\rm int},\qquad \|E_N^{\rm int}\|\le K.         \tag{4}
\]

The entire third group of the residual L286(2), including both source
orders, has the bound and reduction

\[
 \begin{split}
 M_{3,N}&:=\tfrac14\mathcal B(T,T;G_{-+},G,G)
            =\tfrac14\operatorname{Tr}(E_NG_{-+}),\\
 |M_{3,N}|&\le C_fN^2,\\
 M_{3,N}&=\tfrac14\operatorname{Tr}(E_N^{\rm int}G_{-+})
                +O_f(N\sqrt{\ell_N}+\ell_N).              \tag{5}
 \end{split}
\]

The error is o(N^2). No internal vertex pair or boundary layer is
removed in (2)–(5). If the separated source matrix in L281(3) is
truncated to |k|<=R as in L281(15), call the resulting quantities
M_{3,N}^{[R]} and M_{3,N}^{int,[R]}. With C_sep(>R) exactly as there,

\[
 \sup_{N\ {\rm even}}N^{-2}
 \left(|M_{3,N}-M_{3,N}^{[R]}|
       +|M_{3,N}^{int}-M_{3,N}^{int,[R]}|\right)
       \le C_f C_{\rm sep}(>R)\longrightarrow0.             \tag{6}
\]

Here M_{3,N}^int is the trace term in the last line of (5). This
controls the complete external tail; it is not a spatial truncation
of the two internal action vertices. Neither convergence of the
bounded internal operator on source fields nor a coefficient or sign
for M_{3,N} is established. The two mixed insertion/action groups and
the distinct-line cubic group in L286(2) also remain unresolved.
L285(4)'s comparison coefficient is unchanged. There is no claim of
complete cubic compensation, subleading control, a uniform higher
remainder, continuum existence, a nonzero physical sector or mass gap.

## Proof

### 1. Relative row energies and the curl projection

Suppress color until needed. All matrices in this paragraph are the
full relative matrices. L280(21)–(23) gives G zero on im B and L^-1
on H, where L=C*C+BB*. Thus G^2<=L^-2 on the orthogonal invariant
decomposition. Each component eigenvector has squared value <=16/N^4,
and lambda_k>=4|k|^2/N^2. Grouping its allowed indices by max k=r,
with at most 15r^3 indices, gives at every variable edge e

\[
 \sum_f|G_{ef}|^2=(G^2)_{ee}
 \le (L^{-2})_{ee}
 \le 15\sum_{r=1}^{N-1}r^{-1}\le15\ell_N.                 \tag{7}
\]

The own-direction cosine zero mode and both normal endpoint values
are included in this count; there is no all-zero edge mode. Also
G_ee<=30 by L280(22)–(23). Extending by zero to pinned slots preserves
both estimates. L281 section 2 proves

\[
 H_C:=CGC^*\text{ is an orthogonal projection},\qquad
 0\le H_C\le I.                                           \tag{8}
\]

The use of (7) below is for two undifferentiated internal lines only.
The internal-curl bound uses (8) instead, which avoids a logarithmic
loss for that part.

### 2. Bounds for both exact pieces of the differentiated vertex

The bracket in (1) has alternating color coefficients. Expanding (3)
therefore gives a fixed finite list of monomial types, indexed by
orientation, ordered link slots, colors and derivative placement.
Their coefficients are independent of N. In mathsf A each type is

\[
 \beta\sum_{p\ {\rm of\ a\ fixed\ orientation}}
       (Cu)_p^a\,x_{e(p)}^b x_{f(p)}^c,\qquad b\ne c,       \tag{9}
\]

where beta is a fixed real coefficient. In mathsf B each type is
a fixed real coefficient times

\[
 \sum_{p\ {\rm of\ a\ fixed\ orientation}}
       u_{e(p)}^b\,(Cx)_p^a x_{f(p)}^c,\qquad a\ne c.       \tag{10}
\]

Signs of oriented slots are included in the coefficients. A zero
pinned slot contributes zero. Each mapping from plaquettes to one
specified edge slot has multiplicity bounded by an absolute constant
mu: any edge belongs to at most six unoriented plaquettes in four
dimensions. Restricting an orientation or slot cannot increase this
bound; taking mu=24 also covers all four slot labels together.

The different colors in each displayed product are independent:
the covariance of x is G tensor I_3. Each polynomial (9) or (10) has
mean zero. For a single type (9), its covariance matrix in p,q is
G_{e(p),e(q)}G_{f(p),f(q)}. By (7) and Cauchy–Schwarz, every absolute
row sum is at most 15 mu ell_N. This real symmetric matrix hence has
operator norm at most that number: expand the quadratic form and use
2|alpha_p alpha_q|<=|alpha_p|^2+|alpha_q|^2. Consequently the L2
norm squared of (9) is bounded by a fixed constant times
ell_N ||Cu||^2.

For (10), put H=(H_C) restricted to the displayed plaquette rows
and K_{pq}=G_{f(p),f(q)}. Both are positive semidefinite, ||H||<=1,
and K_pp<=30. Their entrywise product has norm at most 30. To check
the exact finite-matrix inequality rather than assume a decay bound,
factor K=sum_j v_j v_j^*. For any real alpha,

\[
 \alpha^*(H\circ K)\alpha
 =\sum_j(\operatorname{diag}(v_j)\alpha)^*
             H(\operatorname{diag}(v_j)\alpha)
 \le\|H\|\sum_p K_{pp}|\alpha_p|^2
 \le30\|\alpha\|^2.                                     \tag{11}
\]

This is the positive Schur-product estimate, here applied to the
complete curl projection and a possibly repeated edge selection.
Since sum_p |u_{e(p)}^b|^2<=mu ||u||^2, (10) has L2 norm squared
bounded by a fixed constant times ||u||^2.

There are only a fixed number J of types in the exact four-slot,
three-color polynomial. The elementary inequality
||sum_{j=1}^J Z_j||_{L2}^2<=J sum_j ||Z_j||_{L2}^2 retains all their
cross terms without assuming independence of different types. Thus

\[
 E[\mathsf A(u;x)^2]\le K_0\ell_N\|Cu\|^2,\qquad
 E[\mathsf B(u;x)^2]\le K_0\|u\|^2.                       \tag{12}
\]

These bounds sum over the entire finite plaquette domains at both
vertices. There is no assumption about vertex separation, translation
invariance, or an unproved pointwise differentiated-kernel estimate.

### 3. Tensor normalization and the bounded internal operator

Differentiating the exact polynomial (1) gives

\[
 D V(x)[u]=\tfrac12 T[u,x,x]=\mathsf A(u;x)+\mathsf B(u;x).
\]

All these random polynomials are centered by the color observation
above. The Gaussian pairing identity already used in L279(23)–(24)
and L280(19) gives two crossing pairings for the two quadratic
derivatives. Since T is symmetric,

\[
 E[D V(x)[u]D V(x)[v]]=\tfrac12 u^*E_Nv.                  \tag{13}
\]

Indeed the two factors 1/2 give 1/4, and the two crossing contractions
give 2; the internal pairing is zero. This reuses the finite Gaussian
identity, not a new asymptotic theorem. Equation (13) proves positivity
of E_N, and (12) proves (2) and (4), after increasing K. Each of E_N
and E_N^int is a one-color edge matrix tensored with I_3. To see this
without a color-factor assumption, both expressions in (3) are
invariant under simultaneous adjoint SU(2) rotations of u,x. Rotations
by pi around coordinate axes force off-diagonal color blocks to vanish;
rotations interchanging axes force equality of the diagonal blocks.

### 4. Source sandwiches, complete error and tail

Use L281's one-color source maps and rename its rectangular separated
matrix mathsf T to distinguish it from the cubic tensor:

\[
 U_\pm=GC_\pm^*W_\pm,\quad W_\pm=\operatorname{diag}(\sqrt{h_\pm}),
 \quad\mathsf T=W_-C_-GC_+^*W_+ .
\]

With F=||f_*||_infinity, L281(9)–(10), (13), (15) give

\[
 \begin{gathered}
 \|U_\pm\|\le\sqrt{F/12}\,N,\qquad
 \|CU_\pm\|\le\sqrt F,\\
 G_{-+}=U_-\mathsf T U_+^*+U_+\mathsf T^*U_-^*,\qquad
 \|\mathsf T\|_1\le8^4 F C_{\rm sep},\qquad
 \|\mathsf T-\mathsf T_R\|_1\le8^4 F C_{\rm sep}(>R).
                                                               \tag{14}
 \end{gathered}
\]

The second norm bound is a direct consequence of (8): CU_pm is a
column restriction of the projection H_C followed by W_pm. It holds
for the complete edge and plaquette spaces. For empty source sets all
these quantities are zero.

Let E_0,E_0^int be the scalar color blocks. From (2), positivity and
Cauchy–Schwarz for the E_N quadratic form,

\[
 \|U_+^*E_0U_-\|\le KF(N^2/12+\ell_N).                    \tag{15}
\]

For the difference, apply (12) to U_+v and U_-w, with one fixed
external color and ||v||=||w||=1. Equations (13) and (3) give exactly
the sum of the AA, AB and BA expectations, each multiplied by two.
Their absolute values are bounded respectively by constants times
F ell_N, F N sqrt(ell_N), F N sqrt(ell_N). Consequently

\[
 \|U_+^*(E_0-E_0^{\rm int})U_-\|
       \le K_1F(\ell_N+N\sqrt{\ell_N}).                    \tag{16}
\]

This also shows why the logarithm in (7) is harmless for this source
response: both external-curl norms are bounded uniformly by (14).
No claim of a vanishing operator norm for E_N-E_N^int is made.

The definition of mathcal B in L279(24) and the symmetry of G identify
its single G_-+ line with Tr(E_N G_-+). By (14), transposition gives
two equal order traces. There are three equal external color blocks,
so the exact coefficient for one scalar sandwich is

\[
 M_{3,N}=\tfrac32
        \operatorname{Tr}(U_+^*E_0U_-\,\mathsf T).          \tag{17}
\]

The internal color sums are already in E_0; they are not counted
again. The factor 3/2 is precisely 3 colors times 2 source orders
times L280(20)'s factor 1/4.

For rectangular matrices, the finite singular-value expansion gives
|Tr(V mathsf T)|<=||V|| ||mathsf T||_1, as in L281(14).
Apply it to (17) with (15) to obtain the O_f(N^2) bound, since
ell_N<=N^2 for N>=2. Apply it with (16) to obtain the complete error
in (5). Finally replace mathsf T by mathsf T-mathsf T_R and use
(15) for E_0 and (4), (14) for E_0^int. This proves (6), uniformly
in N. The argument also bounds the sum of absolute discarded mode
contributions by applying the same inequality to each positive
rank-one reflected term before summing; the internal operator is
unchanged throughout that sum.

The external-curl error divided by N^2 tends to zero without any
order-of-limits interchange. A possible future limit of the bounded
internal-curl sandwich still requires a proof; boundedness and the
external tail alone do not supply it. No other cubic group has been
replaced, cancelled or omitted in this partial result.

### 5. Separate critical audit (2026-10-26)

This audit accepts (2)–(6), under the recorded relative-box inputs and
source hypotheses. In particular its conclusion concerns the entire
G_-+ action group, not the other three residual groups in L286(2).

The row estimate (7) follows on the same invariant Hodge splitting
as G<=L^-1: G^2<=L^-2 there. With max k=r, the eigenvector bound
16/N^4 divided by the squared eigenvalue lower bound
16r^4/N^4 leaves r^-4. At most 15r^3 modes then give the stated
15 sum r^-1. The three positive transverse coordinate indices
exclude an all-zero edge mode; no normal endpoint is omitted.

For each type in (9), bounded edge-selection multiplicity and
Cauchy–Schwarz bound its full absolute row sum by 15 mu ell_N.
For (10), the two distinct field colors remove the crossed-color
pairing. Its covariance is exactly the positive Schur product of
the restricted curl projection and the selected edge covariance.
Inequality (11) controls it by the latter's diagonal, even when
the edge-selection map repeats an edge. Summing the finite list of
types with the L2 triangle bound keeps every cross term. These
arguments verify both estimates (12) on the full relative domains.

The differentiated vertex is T[u,x,x]/2. Its two crossing pairings
give (13), with E=2 covariance and no further combinatorial factor.
The independent external-color blocks follow from adjoint rotations;
their internal colors are already summed in E_0. For source fields,
the operator norms of U_pm and CU_pm are respectively O_f(N) and
O_f(1). Thus AA, AB and BA give exactly O_f(ell_N),
O_f(N sqrt(ell_N)) and O_f(N sqrt(ell_N)) in the sandwich, rather
than an assertion that E-E^int itself has small operator norm.

The factorization of G_-+ has two transpose-related source orders.
Three external colors and the original factor 1/4 yield 3/2 in
(17). Pairing its bounded sandwich with L281's nuclear-norm bound
proves (5). The same argument with T-T_R proves (6), because
ell_N/N^2 is bounded on all even N>=2. Applying it to each reflected
rank-one term also controls the sum of absolute discarded-mode
contributions; this is the tail actually needed in L289. Positivity
of G_-+ or of the final trace is neither assumed nor implied.
These checks establish the complete error and tail, conditional on
the imported separated kernel; boundedness alone supplies no limit.

## Mathlib

Full coverage of this Wilson-specific relative-box energy bound is
not checked. No absence claim or matching Mathlib theorem is asserted.
Finite Gaussian pairing is reused from L279/L280; the exact curl jet
comes from L286 and the relative spectral and source estimates from
L280/L281. The finite Schur-product inequality is displayed to verify
its application to repeated edge selections and all relative rows.
No new external kernel, renormalization or continuum theorem is used.
The prior EXPLORE assessment did not establish a matching result;
this is local partial progress, not certified originality. The separate
audit in section 5 accepts the displayed estimates with their qualifications.
