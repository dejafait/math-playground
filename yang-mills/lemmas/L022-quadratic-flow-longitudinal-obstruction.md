# L022 — A longitudinal obstruction and cancellation in the quadratic flow term

## Hypotheses

Keep the SU(2) box, pinned boundary links, bare coupling, Wilson flow,
two actual probe numerators and tau = 1/16 of L010–L011. Write D for
unscaled edge-to-plaquette incidence and L = a^-2 D*D in full link
exponential coordinates. Put H_t = exp(-t L). These are coordinate
matrices with ordinary Euclidean adjoints; the common cochain weight
does not change these matrices. Use Q_2 and j_(i,m) as in L011.

The flow jets below are defined by L011's full-link ODE starting at
theta(0,g)=g x, with an arbitrary full-link vector x. This extends their
definition off the forest slice only for a deterministic polynomial test;
it changes no Gaussian measure in the coefficient Gamma.

Let phi be a site Lie-algebra field zero at every boundary vertex. On an
oriented positive edge e:v->w define

\[
x_e=\phi_v-\phi_w,\qquad y_e=-\tfrac12[\phi_v,\phi_w].
\tag{1}
\]

Boundary edge entries vanish. In particular D x=0. The bracket convention
is t_c=i sigma_c/2, so [t_1,t_2]=-t_3. All expansions take g to zero
at fixed mesh first. No probability law is assigned to phi.

## Conclusion

The actual quadratic coordinate-flow vertex and its time integral satisfy

\[
Q_2(x)=L y,\qquad z_1(t)=x,\qquad
z_2(t)=(1-H_t)y.
\tag{2}
\]

There are boundary-compatible choices (1) for which D z_2(t) is nonzero
for every t>0. Thus even the curvature of this quadratic jet is not a
function of the input's linear curvature.

For each actual probe i=3,6, let b_i be the polarization of j_(i,2),
so j_(i,2)(h)=b_i(h,h). Gauge invariance gives, for every full-link h,

\[
j_{i,3}(x)=0,\quad j_{i,4}(x)=j_{i,2}(y),\quad
D j_{i,3}(x)h=-2b_i(h,y).
\tag{3}
\]

In particular its full quartic flowed coefficient on this input is

\[
\begin{split}
f_{i,2}(x)
&=j_{i,2}(z_2(\tau))+D j_{i,3}(x)z_2(\tau)+j_{i,4}(x)\\
&=j_{i,2}(H_\tau y).
\end{split}\tag{4}
\]

The cubic flow term D j_(i,2)(x) z_3 is zero on this input. Formula (4)
is a deterministic identity of the actual probe jets, not a replacement
for their cumulants in L011.

More concretely, for every sufficiently fine even mesh put phi=t_1 and
phi=t_2 at two adjacent central sites joined in direction 1, and zero
elsewhere. Then y is t_3/2 on their shared edge and zero elsewhere,
and the actual triplet satisfies

\[
\begin{split}
\|D y\|_{\ell^2}^2&=3/2,\qquad j_{3,2}(y)=j_{3,4}(x)=1,\\
j_{3,2}(z_2(\tau))&=1+O(a^2),\\
D j_{3,3}(x)z_2(\tau)&=-2+O(a^2),\\
f_{i,2}(x)&=O(a^4),\qquad i=3,6.
\end{split}\tag{5}
\]

Thus the isolated two-quadratic-flow contribution j_(3,2)(z_2) stays
nonzero on a zero-curvature input as a tends to zero. Its direct transfer
by the free curvature-quotient argument used for the radial vertex is
invalid. The cancellation in (4) identifies observable terms that cannot
be omitted from a proposed extension of that argument. This does not
prove that any particular forest and Hodge expectations differ, nor
that the grouping (4) is linearly gauge invariant on general inputs.
It gives no value for the full logarithm, no full covariance bound and
no interacting reflected-error estimate against c_box/2.

## Proof

### 1. Stationary flat families determine the quadratic flow vertex

The exactly flat, pinned-gauge family

\[
U_e(g)=\exp(g\phi_v)\exp(-g\phi_w)
\]

has exponential-coordinate expansion g x+g^2 y+O(g^3) by multiplying
the exponential series, or degree-two BCH. Every plaquette is identity,
so every first derivative of the Wilson action vanishes. This family is
therefore stationary under L010's flow. Substitute its coordinate jets
in Q(theta)=-L theta+Q_2(theta)+O(theta^3). The order-g term vanishes
because D x=0, and the order-g^2 term gives -L y+Q_2(x)=0.

For the straight initial family theta(0,g)=g x, the linear jet is x at
all times. L011's variation-of-constants formula then gives

\[
z_2(t)=\int_0^t H_{t-s}L y\,ds=(1-H_t)y.
\]

No inverse of L is used, and its gradient kernel is retained. These two
initial families agree to first order only: exp(g x) is generally not
an exactly flat link configuration. Flow equivariance is not violated.

An independent action check fixes the sign and normalization. For a
plaquette word with signed link entries eta_1,...,eta_4, its logarithm
has W_1=sum eta_r and W_2=(1/2)sum_(r<s)[eta_r,eta_s]. The cubic Wilson
numerator is S_3=sum_p W_1 dot W_2. On x, W_1=0 and exact flatness of
g x+g^2 y implies W_2(x)=-D y. Consequently
grad S_3(x)=-D*D y. The exponential-chart metric has no linear term
(the linear differential-of-exp correction is skew-adjoint), so
Q_2=-a^-2 grad S_3. This recovers (2) directly from the action.

### 2. An actual interior configuration gives nonzero curvature

Choose the sites with lattice indices (N/2,N/2,N/2,N/2) and
(N/2+1,N/2,N/2,N/2). For sufficiently fine even N they and all stencils
used here are in L008's affine core. Put phi=t_1,t_2 there, respectively.
Only their common edge has a nonzero bracket in (1); y=t_3/2 on it.
Exactly six plaquettes meet that edge in four dimensions, each with
circulation plus or minus t_3/2. Hence ||D y||^2=6/4=3/2.

Decompose y into L-eigenvectors. Since D y is nonzero, y has a component
with eigenvalue lambda>0. For every t>0, the factor 1-exp(-t lambda)
is strictly positive on every such component. Therefore

\[
\|D(1-H_t)y\|^2
=a^2\sum_{\lambda>0}\lambda(1-e^{-t\lambda})^2|y_\lambda|^2>0.
\]

Also Q_2(x)=L y is nonzero. Both Q_2 and D z_2 are zero on input zero,
which has the same linear curvature as x. Neither polynomial factors
through D x. This construction embeds in every sufficiently fine
admitted box and uses only pinned interior gauge transformations.

### 3. Locate the exact probe-jet cancellation

Apply the inverse pinned gauge transformation exp(-g phi) to the
configuration whose log coordinates are g x+g^2 h. On edge v->w its
word is

\[
\exp(-g\phi_v)\exp(g x_e+g^2h_e)\exp(g\phi_w).
\]

Its linear term vanishes and its quadratic logarithm is h_e-y_e,
by the same degree-two BCH expansion. Thus its log coordinates are
g^2(h-y)+O(g^3). Each j_i is exactly invariant under this transformation
and has zero constant and linear jets. Its transformed degree-four
coefficient is therefore j_(i,2)(h-y); higher log terms cannot contribute
at degree four.

The actual j_(i,2) is a quadratic form in D theta, including the clover
averages in the shear case. Thus j_(i,2)(x)=0 and
D j_(i,2)(x)=0 on the entire space, not just along gauge directions.
Expand the untransformed j_i(g x+g^2 h). Its degree-three coefficient
is j_(i,3)(x), and its degree-four coefficient is

\[
j_{i,2}(h)+D j_{i,3}(x)h+j_{i,4}(x)=j_{i,2}(h-y).
\tag{6}
\]

Comparison first gives j_(i,3)(x)=0; setting h=0 and then comparing
the part linear in h gives (3). In L011's flowed composition the
z_3 term is annihilated by D j_(i,2)(x). Substituting h=z_2(t) into
(6) gives j_(i,2)(-H_t y)=j_(i,2)(H_t y), proving (4).

This argument applies to both original numerators without changing
their normalization, plaquette averages or clover representatives.
It transfers no nonlinear observable polynomial to a new Gaussian law.

### 4. Distinguish the unsuppressed isolated triplet from the canceled sum

The core strains of L008 are exactly (1,1,-1,-1) for these discrete
stencils. In exponential coordinates the triplet quadratic form is

\[
j_{3,2}(h)=\sum_p\widetilde b_p |(D h)_p|^2.
\]

Of the six plaquettes meeting the selected direction-1 edge, two have
plane 12 and weight 2; four have planes 13 or 14 and weight zero.
Consequently j_(3,2)(y)=2 times 2 times (1/4)=1, exactly. The factors
of a cancel because j_(3,2)(h)=sum_c q_(3,a)(h^c/a).

Both actual quadratic forms have the mesh-independent bound
|j_(i,2)(h)|<=C_i ||D h||^2, and their polarizations satisfy the
corresponding product bound. This follows from L008's bounded smooth
strain coefficients and the bounded four-plaquette averaging operator.

Let Delta_2 be the relative two-form Hodge Laplacian. The finite cochain
identity gives D H_t=exp(-t Delta_2)D. L020's relative heat-diagonal
estimate at fixed positive time, including boundary plaquettes, gives

\[
(e^{-2\tau\Delta_2})_{pp}\le C_\tau a^4.
\]

For the positive matrix K=exp(-2 tau Delta_2), Cauchy–Schwarz gives
|K_pq|<=sqrt(K_pp K_qq)<=C_tau a^4. Since D y has six fixed-size
nonzero entries,

\[
\|D H_\tau y\|^2
=\langle D y,K D y\rangle
\le C_\tau a^4\Big(\sum_p|(D y)_p|\Big)^2=O(a^4).
\tag{7}
\]

Thus j_(i,2)(H_tau y)=O(a^4). The polarization bound also gives
b_3(y,H_tau y)=O(a^2). Expanding j_(3,2)((1-H_tau)y) proves
1+O(a^2); using (3) proves -2+O(a^2) for its cubic-jet partner.
Equations (4) and (7) prove all of (5). In particular the isolated
triplet term is nonzero for all sufficiently fine meshes, while its
input has D x=0 exactly.

### 5. Verification, scope and literature comparison

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_quadratic_flow_longitudinal.py`.
Exact rational calculations on the complete relative complexes N=4,6
check the plaquette BCH coefficient, the cubic Wilson-action gradient,
the inverse gauge jet, ||D y||^2=3/2 and the core triplet stencil value 1.
These coarse meshes check local algebra, not admissibility of the full
supported probes. The proof embeds the same stencil in every sufficiently
fine admitted mesh; (7), not a numerical extrapolation, proves its bound.

This is an informative negative test for extending L021's termwise
curvature-quotient transfer to the remaining quadratic flow term. The
failure is not a failure of Wilson flow or of gauge invariance: nonlinear
gauge jets produce exactly the cancellation in (6). The deterministic
test neither evaluates a Wick contraction nor proves its cutoff
asymptotic. Even the sum in (4) is not shown to be linearly gauge
invariant on general inputs. Actual forest-coordinate contractions or
complete coordinate-change corrections are still required in L011.

The [saved SPECIALIZE assessment](../drafts/literature/2026-09-26-current-target.md)
is reused. Luescher–Weisz,
[arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2), sections 7 and 8.2,
supplies supporting perturbative flow-renormalization context, not a
theorem evaluating this bare-normalized box coefficient. This is local
specialization/reproduction of gauge equivariance, finite Taylor jets
and relative heat estimates, with no claimed discovery beyond checked
literature. The full logarithm, interacting error <= c_box/2, continuum
construction and finite positive mass remain unresolved.

## Mathlib

Coverage of the full longitudinal-flow and probe-cancellation statement:
**not checked**. Coverage of supporting BCH coefficients, smooth flow
jets, finite-dimensional spectral calculus and relative heat estimates:
**not checked**. No Mathlib theorem is asserted to match the statement;
the named primary source is supporting context, not a full match.
