# L214 — The complete nonradial quartic-action response is cubic-bounded

## Hypotheses

Keep exactly L025 and L213's SU(2) pinned relative cube, admitted even
meshes a=8/N, straight lower-rooted direction-1 forest and both actual
L010 Wilson-flow probes i=3,6 at tau=1/16. Expand in the bare coupling
at each fixed mesh before refinement. All three colors, signed traversal
edges, physical boundary rows, allowed constant modes, both residual
subtractions and the full external heat sums are retained.

Use ordinary stored dimensionless link coordinates throughout the proof.
Thus Sigma=Delta_0^(-1) and A are exactly L018(1)–(2), with Delta_0 the
unscaled relative Hodge Laplacian and A the actual residual matrix.
Write R=R_F=I-D_0 Phi for L026's pinned forest retraction. Let I_1
insert component-1 links, Sigma_1=I_1^T Sigma I_1,
A_11=I_1^T A I_1, and H_T=I_N tensor Delta_3 as in L065.

Let T_i^(0) be the entire transverse no-internal-action-pair class
defined in L213(2), with L025's original universal symmetric tensor K
and local matrices U_(i,p),V_p. The quantity under investigation is

\[
 G_i^{\rm nr}=-\kappa_0(f_{i,0},r_0,S_4-S_{4,\rm rad}).
 \tag{1}
\]

## Conclusion

For any variable transverse links e,f at axial levels 1,...,N-1,
including normal links meeting a transverse face, the exact lifted
one-color residual covariance obeys

\[
 \left|(R\Sigma A\Sigma R^T)_{ef}\right|\le C N.
 \tag{2}
\]

Consequently, for both actual probes,

\[
 \sum_{p\in P_T}\left|24K:U_{i,p}:V_p\right|\le C_i a^{-3},
 \qquad |T_i^{(0)}|+|G_i^{\rm nr}|\le C'_i a^{-3}.
 \tag{3}
\]

The cubic-scaled complete responses are bounded. No convergence,
coefficient, sign or vanishing is established. L213's comparison still
identifies their finite-limit question exactly with that of T_i^(0).
Full compensation, finer powers and logarithms, finite interacting
matching, the reflected-error threshold c_box/2, continuum axioms and
infrared finite positive mass remain unresolved.

## Proof

### 1. Identify the lifted residual covariance before splitting rows

L018 gives A D_0=0 and its transpose, hence R^T A R=A. The lifted
forest covariance is C_F=R Sigma R^T. Inserting the forest residual
matrix into its two covariance legs therefore gives exactly

\[
 C_F A C_F=R\Sigma (R^T A R)\Sigma R^T
          =R\mathscr V R^T,\qquad \mathscr V=\Sigma A\Sigma.
 \tag{4}
\]

Selecting signed plaquette rows in (4) gives L025's V_p. In this
identity A denotes the full-link matrix; restriction to the forest
slice is already effected by the zero rows of C_F. There is no extra
mesh factor or Gaussian-tilt factor 2 in V_p. Equation (4) agrees
with L213(6) after its physical-to-stored normalization conversion.
The action polynomial itself remains the original ordered forest
polynomial; only its Gaussian matrices are lifted.

For a positive transverse edge e of direction mu at axial level j,
let d_e be its direct full-link coordinate selector. Its forest row is

\[
 (Rz)_e=d_e^Tz-w_e^T I_1^Tz,
 \quad
 w_e^T z_1=\sum_{\ell=0}^{j-1}
       [z_1(\ell,v+\widehat\mu)-z_1(\ell,v)].
 \tag{5}
\]

Pinned transverse endpoints contribute zero in this formula. Thus w_e
is supported on at most two axial fibers, with entries of magnitude
one and at most 2j nonzero entries. The last axial source N-1 is
absent from the prefix, even when j=N-1. L213 proof section 2 checks
(5) also for normal transverse end edges: the component-1 value and
its entire prefix vanish at the pinned transverse endpoint. No upper
axial extension or neighbor comparison through that pin is used.

### 2. Direct/direct and both mixed orders

L211(5), proved there by the exact local factorization A=C^T J C
with both generator orders and both insertion subtractions, supplies
the full source-uniform estimate

\[
 |\mathscr V_{he}|\le C N\big[(1+\operatorname{dist}(h,e))^{-2}
                                  +N^{-2}\big].
 \tag{6}
\]

Distances are in lattice units, with staggered link centers; every
variable normal end source is included. The residual's compact
stencils, rather than the sources h,e, are required to be interior
in that proof. Its complete convolution argument and relative Green
estimates retain all allowed constant modes. This is an imported
bound for the actual residual, not an application of smooth residual
consistency to a rough covariance column.

Equation (6) immediately bounds \( |d_e^T\mathscr V d_f| \) by CN.
For any one of the axial fibers in w_f, its transverse position is
fixed. If the axial midpoint of e is s, lattice distance is at least
the axial distance, up to a uniform shift. Hence

\[
 \sum_{r=0}^{j_f-1}
 \big[(1+\operatorname{dist}(e,(r,v)))^{-2}+N^{-2}\big]
 \le C\sum_{n\in\mathbb Z}(1+|n|)^{-2}+N^{-1}\le C'.
 \tag{7}
\]

The uniform shift covers both integer and half-integer centers. The
convergent series in (7) is uniform also when transverse separation
vanishes. There are at most two fibers, and a pinned endpoint removes
one rather than adding another. Thus

\[
 |d_e^T\mathscr V I_1 w_f|\le CN,
 \qquad |w_e^T I_1^T\mathscr V d_f|\le CN.
 \tag{8}
\]

The second bound follows either by the same sum or by symmetry of
mathscr V. No transverse difference of that kernel is needed, and no
prefix is treated as a bounded operator. In particular (8) does not
extend L065's scalar estimate to a mixed residual block.

### 3. Keep the two-prefix term in its scalar block

Sigma is componentwise diagonal, so the remaining term in the row
expansion of (4) is exactly

\[
 w_e^T I_1^T\mathscr V I_1 w_f
       =w_e^T\Sigma_1 A_{11}\Sigma_1 w_f.
 \tag{9}
\]

L065(1),(8) state, for all axial frequencies,

\[
 A_{11}=H_T^{1/2}F H_T^{1/2},\qquad F=F^T,\quad\|F\|\le C.
 \tag{10}
\]

Here H_T is strictly positive by the transverse pinned conditions.
Also Sigma_1=(Delta_edge tensor I+H_T)^(-1) commutes with H_T and
Sigma_1^(1/2) H_T Sigma_1^(1/2)<=I. Thus positive spectral calculus
gives Sigma_1 H_T Sigma_1<=Sigma_1. Apply Cauchy–Schwarz and (10)
to the original order in (9):

\[
 |w_e^T\Sigma_1 A_{11}\Sigma_1 w_f|
 \le C\sqrt{w_e^T\Sigma_1 H_T\Sigma_1w_e}
        \sqrt{w_f^T\Sigma_1 H_T\Sigma_1w_f}
 \le C\sqrt{w_e^T\Sigma_1w_e}\sqrt{w_f^T\Sigma_1w_f}.
 \tag{11}
\]

The prefix-gradient energy estimate L026(14)–(15), with the normal
end-edge verification in L213 section 2, gives

\[
 w_e^T\Sigma_1 w_e\le j_e\le N.
 \tag{12}
\]

To recall the endpoint scope explicitly, w_e=T_mu^T b_e, where b_e
selects the j_e relative (1,mu) plaquettes above this transverse edge.
The component-1 transverse difference T_mu satisfies
T_mu Sigma_1 T_mu^T<=I, and ||b_e||^2=j_e. At a transverse face the
fixed component-1 value is zero, so the same relative difference
and the same j_e plaquettes compute the one remaining fiber. This
proves (12) without extrapolating an interior lower bound. The normal
end edges and normalized constant axial mode are retained.

Equations (11)–(12) bound (9) by C sqrt(j_e j_f)<=CN. Positivity
has been used only for Sigma_1 and its commuting energy sandwich,
never for A_11, mathscr V or V_p. Combining this with the direct term
and the two terms in (8) in the exact four-term row expansion proves
(2). Applying (6) separately to both prefixes instead would leave
O(N^2) even on nearby fibers; that unnecessary loss is avoided by
the actual scalar form (10).

### 4. Sum the complete transverse class and restore L213

Every nonzero transverse action plaquette lies at an axial level
1,...,N-1. L213(11) and its complete double heat expansion of U_i
give, for any two transverse links on such a plaquette,

\[
 |(U_{i,p})_{\alpha\beta}|\le C_i a^2.
 \tag{13}
\]

Indeed its exterior columns v_k obey |(v_k)_e|<=a p(k) even on
normal transverse end links; the whitened probe matrix entries are
bounded, and the full two-mode heat sum of the polynomial majorant
is uniformly summable. This statement concerns only the probe
matrix U_i, not the rough residual matrix just estimated.

The three color blocks of V_p are identical and color diagonal.
Traversal signs preserve absolute entry bounds, and fixed traversal
links have zero rows. Hence (2) gives |(V_p)_(gamma delta)|<=C/a
for all its twelve local indices. K has fixed finite dimension and
mesh-independent coefficients. Keeping the factor 24 exactly once,

\[
 |24K:U_{i,p}:V_p|\le C_i a^2 a^{-1}=C_i a.
 \tag{14}
\]

There are O(a^-4) transverse plaquettes. Equations (13)–(14) prove
the absolute sum bound in (3), retaining every plane 23,24,34 and
every boundary strip. Transverse plaquettes contained in a physical
boundary face have fixed zero rows, as already accounted for in L213.
Finally L213(3) gives

\[
 |G_i^{\rm nr}|\le |T_i^{(0)}|+C_i a^{-5/2}=O(a^{-3}).
 \tag{15}
\]

This uses its complete accounting of both axial classes and the
transverse one-internal-pair class. The O(sqrt(a)) scaled comparison
is unchanged. Bounded scaled values are not a Cauchy estimate or a
signed limit; nothing here evaluates or removes the retained class.

### 5. Scope, source reuse and checks

The unchanged EXPLORE assessment
`drafts/literature/2026-10-16-complete-residual-coefficient-cubic-assembly.md`
already covers this exact complete-response target and explicitly
permits a cubic bound as an intermediate result. Its inspected primary
flow and Ward results supply no matching bare forest estimate. L213
identified the remaining class without a cubic bound. The present
argument reuses L065's scalar bound and L211's full residual kernel
bound in complementary terms of the exact row expansion; it neither
reproves a general source theorem nor imports an unchecked new one.

The load-bearing checks are analytic: the exact normalization in (4),
all four row-expansion terms, source-uniformity and the full axial
series in (7), the all-frequency scalar energy sandwich (10)–(12),
normal end-edge incidence, and the powers a^2*a^-1*a^-4=a^-3 in
(14)–(15). No mathematical script, numerical extrapolation, selected
coefficient sign or IEEE arithmetic premise is needed for this bound.
Earlier analytic statements are imported rather than recursively
audited. This is local progress within the assessed scope, with no
certified originality or complete Yang–Mills solution claim.

## Mathlib

Full coverage of this specialized forest response bound: **not checked**.
Coverage of supporting spectral-order, Cauchy–Schwarz, finite incidence
and convergent axial-series facts: **not checked**. Unknown coverage
does not imply absence. The needed specialization is proved above;
no matching Mathlib theorem is asserted.
