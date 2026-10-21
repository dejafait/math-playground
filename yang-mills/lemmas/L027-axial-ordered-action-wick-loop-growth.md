# L027 — Axial ordered-action Wick coefficients retain path growth

## Hypotheses

Keep L025's dimensionless coordinates x=theta/g=a A and its exact
three-color forest Gaussian at fixed admitted mesh. Use precisely
L026's lower-rooted direction-1 straight forest. Select an oriented
(1,mu) plaquette, mu in {2,3,4}, whose four vertices are interior,
with lower axial level j (thus 1 <= j <= N-2). In traversal order
its local entries are (0,u,0,v), where

\[
u=x_\mu(z+\widehat1),\qquad v=-x_\mu(z).
\tag{1}
\]

The zero entries are actual frozen forest links. For each color the
covariance of (u,v) is

\[
C^{\rm act}=\begin{pmatrix}\alpha&\rho\\\rho&\beta\end{pmatrix},
\quad s=\alpha+\beta,\quad e=s+2\rho,\quad h=s-2\rho.
\tag{2}
\]

Different colors are independent copies. The symbols alpha,beta,rho
here are local scalar covariances, not L025's probe/residual matrices.
Let Q2(y)=y^T M_p y be the restriction to the active six coordinates
of the quadratic Wick coefficient 6 K:C_p in L025. Wick ordering is
with respect to this actual local Gaussian; no covariance inverse
is required. The matrix norm uses the ordinary active-coordinate
Euclidean metric, summed over colors.

## Conclusion

The selected nonradial quartic polynomial and its quadratic Wick
coefficient are exactly

\[
q(0,u,0,v)=-\frac{|[u,v]|^2}{24},\qquad
Q2(u,v)=-\frac{\beta|u|^2+\alpha|v|^2-2\rho\,u\cdot v}{12}.
\tag{3}
\]

In per-color coordinate order,

\[
M_p=-\frac1{12}
 \begin{pmatrix}\beta&-\rho\\-\rho&\alpha\end{pmatrix}
 \otimes I_3,\qquad
\boxed{\frac{2j+1}{192}\le\|M_p\|\le\frac{2j+17}{12}}.
\tag{4}
\]

The displayed Kronecker form orders all u colors before all v colors;
a permutation gives three identical two-by-two blocks. In particular,
M_p is negative semidefinite and has norm Theta(a^(-1)) on compact
interior plaquettes with j proportional to N. Thus the ordered tensor
alone does not make this restricted quadratic coefficient O(1).

The directions matter. Put d=u+v=(D1 x)_p and m=(u-v)/2. Then

\[
Q2=-\frac1{12}\left(e|m|^2+(\beta-\alpha)m\cdot d
                       +\frac h4|d|^2\right),\qquad
0\le e\le1,
\tag{5}
\]
\[
(\alpha-\beta)^2\le eh\le4j+34,\qquad
\frac{2j-3}{192}\le\frac h{48}\le\frac{2j+17}{24}.
\tag{6}
\]

For j>=2 the lower curvature-square bound is positive. On d=0,
Q2=-e|m|^2/12 is bounded independently of j. Its coefficient on
the slice m=0 grows linearly with j. The mixed coefficient is only
bounded here by O(sqrt(j)); no cancellation or convergence of it is
claimed. Coordinates (m,d) have a different metric from (u,v).

For either actual probe i=3,6, let w_(i,p) be the active two-by-two
one-color submatrix of L025's W_(i,p). The contribution of this
plaquette's one-internal-action-pair class to the *negative* action
cumulant is exactly

\[
G^{\rm loop}_{i,p}
=2\left[\beta w_{uu}+\alpha w_{vv}
           -\rho(w_{uv}+w_{vu})\right].
\tag{7}
\]

No mesh-uniform bound or certified sign for w or this signed contraction
is established here; section 4 records qualified finite-mesh diagnostics. Purely
transverse plaquettes, L025's no-internal-pair class and L011's
other terms remain. In particular (4) does not establish growing
probe responses, a power or logarithmic term in the full Gamma,
absence of faster growth, or failure of L019's cancellations.
The interacting reflected-error threshold c_box/2 is unchanged;
no continuum construction or mass gap is supplied.

## Proof

### 1. The two-edge action and its normal-order coefficient

For su(2) vectors in L025's normalization, |[u,v]|^2 equals
|u|^2|v|^2-(u.v)^2. Write U=|u|^2, V=|v|^2, T=u.v.
Using exp(g u)=cos(g|u|/2) I +
2 sin(g|u|/2) u/|u|, with the analytic extension at zero, gives

\[
\tfrac12\operatorname{Tr}(e^{gu}e^{gv})
=1-\frac{g^2}{8}(U+V+2T)
 +g^4\left[\frac{U^2+V^2}{384}
            +\frac{UV}{64}+\frac{T(U+V)}{96}\right]+O(g^6).
\tag{8}
\]

This is a finite Taylor identity, with fixed u,v. The plaquette's
action is four times one minus this trace. Subtract L025's radial
fourth coefficient -(U+V+2T)^2/96 from the fourth action coefficient
in (8). The difference is -(UV-T^2)/24, proving the first part of
(3). This computes the actual restricted ordered polynomial, rather
than replacing a nonlinear forest vertex by a Hodge vertex.

For any homogeneous quartic q=K y^4, its quadratic Wick coefficient
is (1/2) C_(ab) partial_a partial_b q = 6 K:C applied to y^2.
The factor follows by differentiating its four symmetric legs, or
by choosing the six internal pairs. For f=UV-T^2 in three colors,
direct differentiation gives

\[
\sum_c\partial_{u_c}^2 f=4V,\quad
\sum_c\partial_{v_c}^2 f=4U,\quad
\sum_c\partial_{u_c}\partial_{v_c}f=-4T.
\tag{9}
\]

The actual covariance contraction is
(alpha Delta_u + beta Delta_v +
2 rho sum_c partial_(u_c) partial_(v_c))/2.
Apply it to -f/24 to get the second part of (3) and the matrix (4).
All axial covariance rows are zero, so restriction before this
contraction is valid. L025's external local matrices also have zero
axial rows and columns. No dropped axial derivative can contribute.

For clarity, Q2 is the coefficient polynomial, not the whole q or
its expectation. The full decomposition is

\[
q=:q:+:Q2:-\frac{\alpha\beta-\rho^2}{4}.
\tag{10}
\]

Indeed E[UV]=9 alpha beta and E[T^2]=3 alpha beta+6 rho^2,
so E[q]=-(alpha beta-rho^2)/4. This also covers singular C.
The constant drops from the cumulant; the fourth Wick part remains.

### 2. Bounds on the actual covariance and its curvature direction

L026 applied to the two active edges gives

\[
\frac{j+1}{8}\le\alpha\le j+9,\qquad
\frac j8\le\beta\le j+8,\qquad
\frac{2j+1}{8}\le s\le2j+17.
\tag{11}
\]

The upper-level edge is interior even when j=N-2, so that same
bound applies at level j+1. Positivity of the covariance implies
alpha beta-rho^2>=0. The matrix with diagonal (beta,alpha) and
off-diagonal -rho is therefore positive semidefinite, has trace s,
and largest eigenvalue between s/2 and s. Dividing by 12 proves (4).
The three color copies do not change its norm. On a fixed compact
interior region with j>=delta N, its lower bound is at least
delta/(12a); its upper bound is O(a^(-1)), since N=8/a.

To prove e<=1, use L018's exact linear lift R_F Sigma R_F^T and
D1 R_F=D1, where Delta=D1^T D1+D0 D0^T and Sigma=Delta^(-1)
in ordinary coordinates. The covariance of d=u+v is exactly the
corresponding diagonal of D1 Sigma D1^T. Since D1^T D1<=Delta,

\[
\|D1\,\Delta^{-1/2}\|\le1,\qquad
0\le D1\,\Sigma\,D1^T\le I.
\tag{12}
\]

Taking its diagonal yields 0<=e<=1. This step uses only a linear
curvature covariance, not a transfer of q. Substituting u=m+d/2,
v=-m+d/2 into (3) gives (5). The covariance determinant identity is

\[
eh-(\alpha-\beta)^2=4(\alpha\beta-\rho^2)\ge0.
\tag{13}
\]

Furthermore h=2s-e, hence (11) and e<=1 give
h>=(2j-3)/4 and h<=4j+34. These imply (6), including its cross
bound. For compact interior j>=delta N and sufficiently large N,
j>=3, and h/48>=j/192>=delta/(24a). The curvature-square coefficient
therefore grows at order a^(-1), while the m-square coefficient
is bounded. The determinant inequality controls the mixed term
but does not remove it.

### 3. Its position in the response and the limitation of the test

L025's one-internal-pair class is -48 K_(abcd) W_(ab) C_(cd).
By M_(ab)=6 K_(abcd) C_(cd), this equals -8 Tr(M W).
Restrict to the six active coordinates as justified above. Each
color block of W is identical, by L025's block-diagonal definitions
of S,B_i,A and the color-independent local map. Thus the trace is
three times the two-by-two trace. Substituting (4) gives exactly (7),
including its plus sign and factor two. W may be nonsymmetric;
only w_uv+w_vu occurs. W need not be positive or negative.

A lower bound for ||M|| cannot be substituted as a lower bound for
Tr(M W). The result stops an absolute O(1) estimate of this local
coefficient in the specified forest, and locates its curvature
direction. Estimating (7), summing plaquettes, controlling the other
pairing class, and grouping with the other action, measure and
observable jets are still required. L019's cancellations remain
an obligation, not an established cancellation of this term.

### 4. Verification

Run `OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_ordered_action_loop_direction.py`.
The independent scalar/vector exponential Taylor product verifies
the quartic-minus-radial identity exactly over rational polynomials.
Exact differentiation verifies (3), and normal ordering and full
Isserlis moments are checked, including a singular covariance.

The script also computes the two actual edge covariances by L026's
relative tensor modes at N=4,8,16,32, retaining every mode and the
zero own-direction edge mode. It retains both the direct transverse
component covariance and the independent axial path covariance,
including cross covariance between the two path lengths. These
samples check the normalization and bounds, not their all-mesh proof
or the supported Ward stencil's admission at small N.

The restricted coefficient norms are approximately 0.13223, 0.24661,
0.46890, 0.91323; their required intervals are respectively
[5/192,21/12], [9/192,25/12], [17/192,33/12], [33/192,49/12].
The certificate is
`scripts/combined-ward-response/ordered-action-loop-direction-certificate.json`.
All ten checks passed; the complete checks field was inspected.
The analytic argument (11)–(13), rather than the samples, proves
the path-growth and bounded-direction assertions. Neither actual
probe's W entries are computed by this script.

### Additional signed-contraction diagnostic (2026-10-05)

Run `OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_axial_signed_response.py --samples 64`.
This separate script tests (7), summed only over axial plaquettes with
all four vertices interior. It uses the actual smooth displacement and
both leading L010 probes at the admitted meshes N=24,32. It does not
include upper-face omitted axial links, other boundary plaquettes,
transverse plaquettes or the other pairing class.

Here is the covariance order and normalization of this diagnostic.
Use the full one-color matrices Sigma,H,Q_i,A and retraction R_F
of L018, where B_i=H Q_i H. Since R_F differs from identity by a
gradient and A,B_i annihilate gradients, R_F^T A R_F=A and
R_F^T B_i R_F=B_i. Substitution of
I_F Sigma_F I_F^T=R_F Sigma R_F^T into the exterior three-covariance
product therefore gives precisely

\[
I_F\Sigma_F B_{i,F}\Sigma_F A_F\Sigma_F I_F^T
=R_F\Sigma H Q_i H\Sigma A\Sigma R_F^T.
\tag{14}
\]

This is a linear lift of the exterior contraction, not a transfer of
the quartic action polynomial. The latter is retained through its
actual local forest covariance C. Let xi have independent real
standard Gaussian stored coordinates and set

\[
x=H^{1/2}\xi,\quad
y_i=R_F\Sigma H Q_i x,\quad z=R_F\Sigma A\Sigma x.
\tag{15}
\]

Then E[x x^T]=H, and multiplication, with Sigma H=H Sigma, proves
E[y_i z^T] equals the right side of (14). Each sample of (7), with
w_ab replaced by (y_i)_a z_b, is consequently unbiased in exact
arithmetic. Its factor two already includes all three colors; they
are not independently sampled or counted again. The script uses
floating-point arithmetic, so unbiasedness is an algebraic property
of the ideal estimator, not a bound on rounding error.

With y_m=(y_u-y_v)/2, y_d=y_u+y_v and the same definitions for z,
substitution into (7) separates each sample as

\[
2e\,y_m z_m
+(\beta-\alpha)(y_m z_d+y_d z_m)
+\tfrac h2 y_d z_d.
\tag{16}
\]

These are respectively the common path, mixed and curvature pieces.
Their sum is checked against the original (u,v) formula on every
sample. Local alpha,beta,rho are computed by complete relative-mode
sums for the direct transverse component and the axial path component,
including the edge zero mode. The two components have no cross
covariance. Neighboring path lengths are retained in rho. The full
floating-point coefficient arrays are saved in
`scripts/combined-ward-response/axial-signed-response-N24-covariances.npz`
and the corresponding N32 archive; no internal covariance is heated.

With 64 independent samples per mesh, the summed signed-loop estimates
and their sample standard errors are:

| N | Probe 3: mean (standard error) | Probe 6: mean (standard error) |
| --- | --- | --- |
| 24 | 722.76 (188.96) | 19994.46 (130.33) |
| 32 | 7976.96 (308.13) | 56039.92 (377.08) |

The common path/mixed/curvature mean pieces are respectively
(2123.74,-69.71,-1331.27) and (15112.60,-455.70,5337.55) at N=24,
and (7591.23,-172.20,557.94) and (44255.84,-980.49,12764.57) at N=32.
Thus the common path mean is numerically larger than the other pieces
at these two meshes; the triplet curvature mean changes sign. These
are observations about the samples, not certified signs of expectations.
The total standard error is computed from each sample's total, retaining
the correlation among pieces; it is not a confidence guarantee.

The full certificate, including individual samples, piece covariance
matrices, complete-grid covariance-bound margins and failures, is
`scripts/combined-ward-response/axial-signed-response-certificate.json`.
All 14 checks passed, and their complete entries and empty failures
were inspected. The dense N=4 one-site displacement diagnostic checks
the mode-sum covariance against an incidence inverse, the solver/heat,
the exact covariance order and the color factor, with maximum errors
below 1.8e-15 against required tolerances 1e-11 or 1e-10. This dense
sample does not use the actual smooth displacement. At the actual
meshes every interior axial covariance passes (11)–(13)'s selected
bound tests; the largest sample decomposition error is 7.3e-12
against 1e-9. An independent reread of all 2304 stored sample
components reproduces every reported mean and standard error exactly
in the same floating-point arithmetic, and all coefficient arrays
are finite. This checks evidence integrity, not mathematical asymptotics.

Two meshes cannot establish a uniform bound, a power, a logarithm,
or the absence of faster growth. No confidence interval, exact
nonvanishing claim, full coefficient, or interacting bound follows.
This numerical continuation is EXPLORATION within the same screened
target; the analytic conclusions (3)–(7) and stopped tensor-only route
remain unchanged.

## Mathlib

Coverage of the full specialized axial Wick coefficient and its
forest-growth bound: **not checked**. Supporting finite Taylor,
Gaussian normal-ordering and spectral-order results: **not checked**.
No matching Mathlib theorem is asserted.
Coverage of the supporting Gaussian randomized-trace identity: **not checked**.

This is local REPRODUCTION of finite SU(2) Taylor, Isserlis and
covariance-order identities, needed to test L025's ordered vertex
after L026 ruled out a raw-loop bound. It makes no novelty claim.
The unchanged ready assessment
`drafts/literature/2026-09-26-current-target.md` supplies the precise
primary source comparison and bare-normalization/physical-boundary
qualifications. No cited general flow-finiteness or stress-matching
theorem assigns a value to this loop or to the full logarithm.
