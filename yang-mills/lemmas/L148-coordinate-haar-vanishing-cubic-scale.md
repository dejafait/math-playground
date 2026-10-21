# L148 — The complete coordinate-Haar response vanishes at cubic scale

## Hypotheses

Keep L011's fixed-mesh SU(2) expansion, L010's two actual Wilson-flow
probes i=3,6 at tau=1/16, and L026's direction-1 straight lower-rooted
forest in [-4,4]^4. All physical boundary vertices are pinned; the last
axial link on each interior transverse fiber is omitted from the forest.
Take the bare small-coupling coefficient at each fixed mesh first, then
a=8/N tends to zero through sufficiently fine admitted even meshes.
The displacement and probe weights are exactly those of L008.

Use L018's complete coordinate-density contribution
Gamma^M_(i,F)=-kappa(f_(i,0),r_0,M_(2,F)), including all three colors.
It is distinct from the Haar-divergence insertion of L010. Constants
below may depend on the fixed box, displacement and positive flow time,
but not on N. No bound uniform in flow time or box size is asserted.

## Conclusion

For each actual probe there is a finite C_i such that

\[
 |\Gamma^M_{i,F}|\le C_i a^{-2},\qquad
 \boxed{\lim_{a\downarrow0}a^3\Gamma^M_{i,F}=0.}                 \tag{1}
\]

Thus this same-forest term cannot change the cubic coefficient of the
two groups assembled in L147. That comparison retains all of L147's
qualifications; (1) itself is an analytic bound, without numerical sign
certificates. No a^2-scaled limit, unscaled boundedness, logarithmic
coefficient, or forest-independent interpretation is asserted. Other
action, insertion and observable/flow jets can still compensate the
two-group coefficient. Finite matching, the interacting reflected error
<=c_box/2, continuum axioms, reflection positivity, infrared control and
a finite positive mass remain unresolved.

## Proof

### 1. Preserve the exact finite trace and its normalization

In this proof Delta is the **physical** relative Hodge Laplacian; it
equals a^-2 times L018's dimensionless Delta. Work in orthonormal
cochain coordinates, whose numerical matrices agree with weighted
stored-coordinate operators because every cochain inner product has
the same weight a^4. Define, as in L023 and L028,

\[
 \begin{split}
 E&=e^{-\tau\Delta},\qquad
 N_a=\tfrac12(L_aK_a+K_a^*L_a)-Q_{3,a}-Q_{6,a},\qquad L_a=d_a^*d_a,\\
 \mathcal R_a&=\Delta^{-1/2}N_a\Delta^{-1/2},\qquad
 \mathcal B_{i,a}=\Delta^{-1/2}Q_{i,a}\Delta^{-1/2},\\
 T_{i,a}&=E\mathcal B_{i,a}E,\qquad
 U_a=a^{-1}R_F\Delta^{-1/2},\qquad C_a=U_a^*U_a.
 \end{split}                                                    \tag{2}
\]

The symbol R_F denotes the forest retraction, whereas mathcal R_a is
the symmetric whitened residual. For a standard one-color Gaussian
vector xi, the stored dimensionless forest links are x=U_a xi.
Indeed a physical Gaussian connection has orthonormal vector
Delta^-1/2 xi, stored vector a^-2 Delta^-1/2 xi, and x=a R_F A_stored.
The leading probe and residual have whitened matrices T_(i,a) and
mathcal R_a, respectively, by L018's gauge-invariant linear lift.
Consequently the density has whitened matrix C_a/12 per color.

Importing L018(4), including its connected quadratic contraction and
three-color factor, gives exactly

\[
 \Gamma^M_{i,F}=-2\operatorname{Tr}
       (E\mathcal B_{i,a}E\mathcal R_a C_a).                     \tag{3}
\]

One can also check its powers directly in L018's full trace: its
covariance is a^-2 Delta^-1, residual matrix is a^2 N_a, and flowed
probe matrix is a^2 E Q_(i,a) E. Their product with three covariances
has the overall factor a^-2, exactly the factor in C_a. Only the
heat operator and powers of Delta commute here; neither the residual,
probe weights nor forest map is commuted through another factor.
In particular the unflowed density factor C_a is not heat damped.

### 2. Quantitative one-sided heat smoothing of the residual

Let f_(k,a) be the L2_a-normalized relative product mode, with component
included in k, and let lambda_(k,a) be its physical eigenvalue. The
relative spectrum used in L028 has

\[
 \lambda_{k,a}\ge |k|^2/16\ge\lambda_*:=3/16.                  \tag{4}
\]

The three vertex indices of every one-form component are positive;
its own edge index may be zero. Thus (4) retains the constant axial
mode and gives a gap independent of a.

L028, proof section 1, equation (5) with r=0, proves that N_a f_(k,a)
has a compactly supported smooth extension bounded by
C a^2(1+|k|)^5 in C^0, uniformly over **all** allowed labels. Its
support stays away from the physical faces. The fixed volume converts
this to

\[
 \|N_a f_{k,a}\|_a\le C a^2(1+|k|)^5,
 \qquad
 \|\mathcal R_a f_{k,a}\|_a
 \le\lambda_*^{-1/2}\lambda_{k,a}^{-1/2}
             C a^2(1+|k|)^5
 \le C' a^2(1+|k|)^5.                                        \tag{5}
\]

This imports the proved centered-stencil consistency, including the
adjoint coefficient derivatives. It does not extend L028's later
interior-only forest-lift estimate to an upper pinned row.

Use the finite rank-one expansion from L023, proof section 3, (14).
The trace norm of v f* for unit f is ||v||, hence

\[
 \begin{split}
 \|\mathcal R_a E\|_1
 &\le\sum_{k\text{ allowed}}e^{-\tau\lambda_{k,a}}
                              \|\mathcal R_a f_{k,a}\|_a\\
 &\le C' a^2
       \sum_{\mu=1}^4\sum_{k\in\mathbb N_0^4}
                  (1+|k|)^5e^{-\tau|k|^2/16}
 \le C_\tau a^2.                                             \tag{6}
 \end{split}
\]

The enlarged four-dimensional Gaussian series is finite. Thus (6)
retains every allowed exterior heat mode, uniformly as their number
grows. Both E and mathcal R_a are self-adjoint, so
||E mathcal R_a||_1=||mathcal R_a E||_1. Only one-sided smoothing is
used; no small unflowed residual norm is inferred.

### 3. A coarse forest bound retaining every pinned row

Write P_N for the dimensionless path potential of L026(2): on interior
vertices of each transverse fiber it is

\[
 (P_N z)(j,v_\perp)=\sum_{\ell=0}^{j-1}z_1(\ell,v_\perp),
 \quad 1\le j\le N-1,
 \qquad P_N z=0\text{ on every boundary vertex}.              \tag{7}
\]

Cauchy--Schwarz on each prefix gives

\[
 \sum_{j=1}^{N-1}\left|\sum_{\ell<j}z_1(\ell,v_\perp)\right|^2
 \le\sum_{j=1}^{N-1}j\sum_{\ell<j}|z_1(\ell,v_\perp)|^2
 \le N^2\sum_{\ell=0}^{N-1}|z_1(\ell,v_\perp)|^2.
                                                                    \tag{8}
\]

Summing over fibers proves ||P_N||<=N in ordinary Euclidean norms.
Zero boundary values are imposed before applying the full unscaled
relative vertex differential D0. A vertex has at most eight incident
links. The elementary bound |b-c|^2<=2|b|^2+2|c|^2, with pinned
values zero, gives ||D0 phi||^2<=16||phi||^2 and ||D0||<=4.
L026's exact retraction is R_F=I-D0 P_N, so

\[
 \|R_F\|\le1+4N,\qquad
 \|C_a\|=\|U_a\|^2
 \le a^{-2}(1+4N)^2\lambda_*^{-1}
 \le C a^{-4}.                                               \tag{9}
\]

The last inequality uses N=8/a and sufficiently small a. The same
scalar norm estimates apply to the numerical matrices in (2).
Equation (9) includes upper omitted axial links, transverse end edges
and every pinned incidence row. In particular it does not extend
the prefix smoothly through the upper face or remove its jump.
This intentionally coarse growing bound makes no O(1) claim about
the raw link covariance and is consistent with L026.

### 4. Close the estimate in its original order

L008's bounded curvature forms give sup_a ||mathcal B_(i,a)||=M_i<infinity
for both actual probes; ||E||<=1 by positivity of Delta. Apply the
finite-dimensional trace-ideal inequality to precisely the factors
in (3):

\[
 \begin{split}
 |\Gamma^M_{i,F}|
 &\le2\|E\mathcal B_{i,a}\|\,
           \|E\mathcal R_a\|_1\,\|C_a\|\\
 &\le2M_i(C_\tau a^2)(C a^{-4})
 \le C_i a^{-2}.
 \end{split}                                                  \tag{10}
\]

Multiplication by a^3 leaves an upper bound C_i a tending to zero.
This proves (1). The complete signed residual was retained until (5)
was applied; its consistency cancellation would be lost by separately
bounding the terms defining N_a. No positivity of the response or
forest invariance was used. L019's nonlinear compensation identities
therefore remain relevant to all other terms.

The argument is a specialization of existing local Gaussian and
consistency inputs to the approved isolated-density scale test. The
literature assessment found no matching asymptotic, so its process
classification is POTENTIALLY_NEW, not a claim of certified originality.
No new numerical or mathematical script is needed for these inequalities.

### 5. Separate critical audit, 2026-10-12

The audit accepts (1) under the stated hypotheses, with no change to
the bound or its scope. The following checks concern the load-bearing
steps of the proof, not additional response groups.

For the normalization check, substitute L018's matrices directly into
its full trace (4): B_i=a^2 E Q_i E, A=a^2 N_a and
Sigma=a^-2 Delta^-1. The product has two positive a^2 factors and
three inverse a^2 factors, leaving a^-2. Whitening gives precisely
(3) with C_a=a^-2 Delta^-1/2 R_F* R_F Delta^-1/2. L018's connected
contraction gives 8 times 3/12=2, and the density insertion has the
minus sign. No cyclic permutation exchanges the residual and density.
The isometry from stored L2_a vectors to ordinary Euclidean vectors
is multiplication by a^2; conjugation leaves the numerical operator
matrices unchanged. Thus the two mode normalizations used in (5) and
in the rank-one expansion give the same trace-ideal estimate.

For the rate check, L028's proof of (5), rather than just its
interior-plaquette conclusion, applies before any forest retraction.
Its Taylor inequalities hold without a restriction on a|k|. The
telescoping compositions have differential order at most three and
lose at most two further derivatives in an error term. Their continuum
sum is zero by the polarized compact-displacement identity checked
there; reversed adjoints include derivatives of the coefficient.
All output stencils remain in a fixed compact interior set. Therefore
the all-mode C^0 estimate used here has the stated fifth-degree
polynomial and a^2 factor. The gap in (4) follows directly from
L026's spectrum and sin(t)>=2t/pi for 0<=t<=pi/2. Its three positive
vertex indices remain even when the own-direction mode is zero.
This justifies the summable majorant in (6) uniformly over the entire
allowed spectrum. It does not strengthen an unflowed norm estimate.

For the pinned-row check, the actual last axial row of R_F z is
z_1(N-1,v)+P_N z(N-1,v)=sum_(ell=0)^(N-1) z_1(ell,v), since
the upper vertex potential is zero. This row is present in the
incidence bound (9). Edges joining an interior vertex to a transverse
boundary vertex likewise retain that vertex potential with one sign.
The degree bound counts these rows and uses zero values at pinned
vertices; it omits no boundary jump. The estimate is deliberately
coarse and consistent with the growing raw covariance of L026.

Finally L008's curvature-form estimate bounds both actual probe
matrices, including the triplet average of squares and clover shear.
The three factors in (10) are E B_i, E mathcal R_a and C_a in that
order. Adjoint invariance supplies the needed one-sided trace norm,
with no internal heat damping or commutation assumption. The audit
therefore confirms O(a^-2) and the zero cubic limit. It establishes
no new asymptotic, repairs no mathematical error and makes no claim
of progress beyond the literature already assessed.

## Mathlib

Coverage of this full forest-specific asymptotic: **not checked**.
Supporting Gaussian cumulant, trace-ideal, incidence-norm and heat-series
coverage: **not checked**. No matching Mathlib theorem or absence claim
is asserted. The precise primary source comparison remains in
`drafts/literature/2026-10-12-coordinate-haar-cubic-scale.md`:
Burgio--Feo--Peardon--Ryan, hep-lat/0303005v1, section III.B (21)--(24),
checks the measure-vertex normalization; Luescher--Weisz, 1101.0963v2,
sections 7.2--7.4 and 8.4, does not supply this isolated pinned-forest
bound. Neither external theorem is imported as an ultraviolet estimate.
