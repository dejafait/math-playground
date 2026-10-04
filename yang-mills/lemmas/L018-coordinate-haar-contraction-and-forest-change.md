# L018 — The coordinate-Haar contraction changes its quadratic insertion with the forest

## Hypotheses

Keep the admitted fixed mesh, SU(2) box, boundary pinning, bare coupling,
displacement, and two Wilson-flow probes of L011, with tau = 1/16. Use
L017's compensated free generator for a boundary-rooted forest F. Each
tree contains exactly one boundary root; all boundary vertices are pinned.
Write I_F for insertion of remaining-link coordinates and pi_F for their
restriction. The three colors are independent at quadratic order.

In x = a A coordinates let D_0 = a d_0 and D_1 = a d_1 be the unscaled
relative incidence matrices, and put

\[
L=D_1^T D_1,\qquad \Delta=L+D_0D_0^T,\qquad
\Sigma=\Delta^{-1},\qquad H=e^{-\tau\Delta/a^2}. \tag{1}
\]

All transposes and norms below use ordinary stored coordinates. The
matrix Delta is positive by L003. Its inverse is the full Hodge covariance
in x coordinates: the a^4 cochain weight and the scaling x=a A cancel
the remaining factors of a. Let Q_i be the symmetric matrix of the
one-color polynomial q_(i,a)(x/a), for i=3,6, and set

\[
B_i=H Q_i H,\qquad
A=\tfrac12(LK_a+K_a^T L)-Q_3-Q_6. \tag{2}
\]

Thus A denotes a residual matrix, not a connection. L017 identifies the
leading Wilson-flow polynomial with B_i; flowing the restricted forest
Hessian instead would define a different probe. Its retraction R_F has
zero forest entries, R_F D_0=0 and D_1 R_F=D_1. Define

\[
\begin{split}
H_F&=(D_1 I_F)^T(D_1 I_F),& \Sigma_F&=H_F^{-1},\\
B_{i,F}&=I_F^T B_i I_F,& A_F&=I_F^T A I_F,\\
G_F&=R_F^T R_F.& &
\end{split} \tag{3}
\]

L017 gives the equivalent compensated expression
A_F=(H_F k_F+k_F^T H_F)/2-I_F^T(Q_3+Q_6)I_F. L011's uncentered leading
polynomials are f_(i,0)=sum_c (x^c)^T B_(i,F) x^c and
r_0=sum_c (x^c)^T A_F x^c, with covariance Sigma_F. Additive constants
in these polynomials do not affect the cumulants used here.

## Conclusion

The actual coordinate-density contribution in L011, with its minus sign,
has the exact finite contraction

\[
\begin{split}
\Gamma^M_{i,F}
&=-\kappa_F(f_{i,0},r_0,M_{2,F})\\
&=-2\operatorname{Tr}(B_{i,F}\Sigma_F A_F\Sigma_F^2)\\
&=-2\operatorname{Tr}(B_i\Sigma A\Sigma G_F\Sigma),\qquad
M_{2,F}=\tfrac1{12}\sum_{c=1}^3|x^c|^2.
\end{split} \tag{4}
\]

This is the coordinate Haar term, not L010's Haar-divergence insertion.
For another admitted forest F', put T=pi_(F') R_(F') I_F. This is an
invertible real linear map. In F coordinates the changed density and its
contraction are

\[
M_{2,F'}(Tx)=\tfrac1{12}\sum_c(x^c)^T T^T T x^c,\qquad
\Gamma^M_{i,F'}=-2\operatorname{Tr}
 (B_{i,F}\Sigma_F A_F\Sigma_F T^T T\Sigma_F). \tag{5}
\]

In particular, the exact quotient law does not identify the two
quadratic density insertions. For the direction-1 straight forest with
its omitted axial link at the upper face, and the forest with its
omitted link at level m, 0 <= m < N-1, there is an explicit one-color
unit field for which

\[
\|R_F x\|^2=1,\qquad
\|R_{F'}x\|^2=1+6(N-m-1),\qquad
M_{2,F'}-M_{2,F}=\frac{N-m-1}{2}. \tag{6}
\]

This proves a difference of density functions; it does not prove a
nonzero contraction difference for every probe, or for the original two
probes. Their evaluated diagnostics below are qualified separately.

Let Gamma_(i,F) be the **complete** coefficient in L011 and define
Gamma^other_(i,F)=Gamma_(i,F)-Gamma^M_(i,F), retaining every other term
of that expansion. At every fixed mesh,

\[
\Gamma_{i,F'}=\Gamma_{i,F},\qquad
\Gamma^{other}_{i,F'}-\Gamma^{other}_{i,F}
=-(\Gamma^M_{i,F'}-\Gamma^M_{i,F}). \tag{7}
\]

No value or asymptotic is established for the complete coefficient, its
cutoff logarithm, or its remainder. The required interacting reflected
error <= c_box/2 remains unbounded.

## Proof

### 1. Connected quadratic contraction

For a centered real Gaussian y with covariance S>0 and real symmetric
matrices U,V,W, elementary Gaussian integration gives, for sufficiently
small real t,s,u,

\[
\log E e^{t y^T U y+s y^T V y+u y^T W y}
=-\tfrac12\log\det[1-2S^{1/2}(tU+sV+uW)S^{1/2}]. \tag{8}
\]

The matrix in brackets is positive near zero, so this identity and its
third mixed derivative are justified without any formal convergence
assumption. Expand the logarithm in its norm-convergent trace series.
Only its degree-three term contributes to that derivative. There are
six orders of the three whitened matrices; cyclicity and reversal by
transpose make all six traces equal. The resulting third cumulant is

\[
\kappa(y^T U y,y^T V y,y^T W y)=8\operatorname{Tr}(U S V S W S). \tag{9}
\]

Mixed cumulants between independent colors vanish. Apply (9) with
U=B_(i,F), V=A_F, W=1/12 and sum the three colors. The factor is
8 times 3/12 = 2. L011 supplies the minus sign, proving the first two
lines of (4). No trace-zero condition on A_F is needed.

### 2. Explicit lift to the full free cochains

The leading probe and residual are free-gauge invariant. In particular
K_a D_0=0, Q_i D_0=0 and L D_0=0, so A D_0=B_i D_0=0. Both leading
polynomials are unchanged by replacing a full field z by R_F z.

The lifted coordinate density is explicitly
sum_c ||R_F z^c||^2/12, with matrix G_F/12. Because R_F D_0=0 this
is also free-gauge invariant, although nonlocal and forest dependent.
L003's normalized linear quotient law applies to this polynomial and
its products with the other two. Equivalently, after removal of the
independent Hodge gradient Gaussian, pi_F R_F z has covariance Sigma_F;
its curvature action is exactly x^T H_F x/2. Positive definiteness and
the quotient-law identification are those of L003 and L017.

Apply (9) in the full Gaussian with covariance Sigma and density matrix
G_F/12 to obtain the last line of (4). This transfer is justified by
the explicitly gauge-invariant **lift**. It does not identify the
unmodified coordinate density with a local Hodge density, nor transfer
S_3,S_4 or higher flow/insertion vertices to that law.

### 3. Change of forest

Each R_F is a projection onto its forest slice with kernel im D_0.
Thus R_F R_(F')=R_F and R_(F') R_F=R_(F'). Applying restriction and
insertion proves that pi_F R_F I_(F') is the inverse of T. The leading
probe and residual depend only on the quotient, so

\[
\Sigma_{F'}=T\Sigma_F T^T,\qquad
B_{i,F'}=T^{-T}B_{i,F}T^{-1},\qquad
A_{F'}=T^{-T}A_F T^{-1}. \tag{10}
\]

Pull back M_(2,F') by T and use (9). This proves (5), including all
noncommuting factors. An exact change of nonlinear forest coordinates
also changes the action and observable Taylor polynomials; its Haar
invariance does not impose T^T T=1 on this single quadratic term.

For (7), L003's exact product-Haar quotient identifies the original
gauge-invariant covariance for every g>0 in both forests. L011's
fixed-mesh Laplace expansion, with the same nondegenerate minimum on
either rooted slice, therefore has a unique leading coefficient and a
unique g^2 coefficient. Subtract the coordinate-density contributions
to get the second identity in (7). This requires the other terms in
their **full sum**; it does not locate the cancellation in a particular
quartic, cubic, insertion or flow term.

### 4. Exact density-function countertest

Fix an interior triple of transverse vertex coordinates. Let x have
value 1 on the direction-1 edge at axial level N-1 above that triple,
and zero elsewhere. With the forest omitting that upper edge, every
path sum is zero, so its retracted squared norm is 1.

For the forest omitting level m, roots lie on the lower face for
vertices at levels i<=m and on the upper face for i>m. Its path
potential is zero at i<=m and -1 at i>m on the chosen transverse
triple, zero at other triples. Retraction puts the axial value 1
on the omitted edge at level m. At each of the N-m-1 upper interior
levels, each of the other three coordinate derivatives of the point
profile has two entries of magnitude 1. Their squared norm is 6
per level. This proves (6). The retracted fields differ by a pinned
gradient and have identical curvature.

For N=24, m=12, their norms are exactly 1 and 67 and the one-color
density difference is 11/2. This example uses the original relative
cochains at an admitted mesh; it is independent of displacement weights.
It excludes forest independence of M2 as a function. It makes no claim
that either actual covariance with f_(i,0),r_0 is nonzero.

### 5. Evaluated finite diagnostics and their limits

Run
`PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/combined-ward-response/haar_contraction.py --dense-only --output scripts/combined-ward-response/haar-dense-results.json`.
The existing N=4 rational one-site diagnostic of L017 independently
constructs dense incidence, probe, generator, covariance and heat
matrices. The matrix-free operators agree with it within 5.2e-15.
The full and forest traces in (4) agree within 3e-11. Moving the
omitted axial edge from level 3 to level 2 changes the two diagnostic
contributions from (0.0087936037,-0.0013986119) to
(0.0140100950,-0.0006144473). These are floating evaluations for
one-site sample weights, not the original smooth displacement or a
rigorously rounded nonvanishing theorem.

The original-probe diagnostic is
`PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/combined-ward-response/haar_contraction.py --skip-dense --N 24 --samples 64 --output scripts/combined-ward-response/haar-original-results.json`.
It retains L008's rho, central differences, average of squares and
clover-product shear. The active vertex indices are 2 through 22
in each direction, so their incident clovers stay strictly inside
the box. The full relative one-form space has 1,168,032 real entries
per color. Product sine/cosine transforms apply the actual Hodge
covariance and full free-flow heat operator without a mode truncation.

For independent standard Gaussian z let w=Sigma^(1/2) H^(1/2) z.
The statistic used for each forest and probe is

\[
-2\,(Q_i w)^T H\Sigma A\Sigma G_F w. \tag{11}
\]

Since E[ww^T]=Sigma H, cyclicity of trace and commutation of H and
Sigma show that its expectation is exactly the last line of (4).
Sharing z between forests estimates their difference. Finite sample
averages and sample standard errors are diagnostics, without a proven
confidence guarantee. In row order (upper-edge forest, middle-edge
forest) and column order (triplet, shear), the 64-sample values are

\[
\begin{pmatrix}
-5692.71&-35447.30\\
-916.38&-18632.83
\end{pmatrix},\qquad
\text{sample standard errors}=
\begin{pmatrix}
422.85&368.49\\
146.87&150.12
\end{pmatrix}. \tag{12}
\]

The paired differences are (4776.32,16814.47), with sample standard
errors (315.38,256.75). Together with the exact density-function test,
these give a concrete reason to group the remaining contractions before
interpreting an isolated density contribution. They do not prove exact
nonzero contraction differences for these probes, determine cutoff
growth from one mesh, or evaluate the full coefficient in (7).

This specializes the covered Gaussian/forest machinery and is
REPRODUCTION, without a claim beyond the checked literature. The exact
finite identities and the qualified diagnostics leave the ultraviolet
logarithm, finite matching, physical-boundary subtraction, and reflected
error <= c_box/2 unresolved, as well as the continuum and mass-gap target.

## Mathlib

Coverage of the full forest-specific contraction and change-of-forest
statement: **not checked**. Coverage of supporting quadratic Gaussian
cumulants, finite trace identities, projections and product heat
transforms: **not checked**. No Mathlib theorem is asserted to match
this result. The [prior SPECIALIZE assessment](../drafts/literature/2026-09-26-current-target.md)
records the inspected primary sources and direct links; in particular
Del Debbio--Patella--Rago, [arXiv:1306.1173v1](https://arxiv.org/pdf/1306.1173v1),
section 6, is supporting translation/flow context, not a match for this
coordinate-Haar contraction or its physical-boundary specialization.
