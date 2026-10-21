# L049 — Upper-face cubic conditioning retains observable corrections

## Hypotheses

Use L011's fixed-mesh SU(2) Gaussian in dimensionless ordinary forest
coordinates, L018's actual quadratic probes and residual, and L026's
lower-rooted direction-1 forest on the all-face pinned cube. Set a=8/N
and tau=1/16, with N admitted and even. The small-coupling coefficient
is taken at fixed mesh first. Let X denote all three color copies of
forest coordinates and let their covariance be
S=diag(Sigma_F,Sigma_F,Sigma_F). Write f=f_(i,0), i=3 or 6, and r=r0.
Their additive constants are irrelevant; both are color-diagonal
quadratic polynomials. This statement does not replace the full-link
flow by the restricted forest Hessian.

Let E_top be the transverse edges labeling L029's upper-face (1,mu)
plaquettes, mu=2,3,4, with plaquettes contained in another fixed face
omitted as identically zero. Include edges meeting a transverse boundary.
On transverse interior vertices let u(v) be the upper omitted axial
link vector, and extend u by zero to transverse boundary vertices.
For e=(v,v') in E_top, use exactly L029's traversal and set

\[
 H_e=(u(v)+u(v'))/2,\quad L_e=u(v)-u(v'),\quad
 d_e=L_e-T_e,\quad \eta_e=d_e-L_e/N,\quad
 Q_e=u(v)\mathbin\times u(v').                         \tag{1}
\]

T_e is the positive transverse link at axial level N-1; the positive
transverse link at level N is fixed. Thus the ordered entries are
(u(v),0,-u(v'),-T_e). No omitted axial link is set to zero.

Let G3 be the inverse dimensionless transverse Dirichlet vertex
Laplacian, and let T3 be the incidence map with
(T3 phi)_e=phi(v)-phi(v'), with boundary values zero. Put

\[
 P=T3 G3 T3^T,\qquad K_d=\operatorname{Cov}(d^c,d^c),
 \qquad K=K_d-P/N.                                    \tag{2}
\]

These are matrices on the whole E_top set for one color, including
distinct edges and all transverse directions. In formulas involving
all colors use mathcal K=diag(K,K,K). Index j below runs over edge
and color together, so eta_j and Q_j are scalar entries. Define the
constant Gaussian directional derivatives on all forest coordinates

\[
 v_j=\operatorname{Cov}(X,\eta_j),\qquad
 \mathcal D_j h=v_j\mathbin\cdot\nabla_X h.            \tag{3}
\]

No inverse of K or of a local covariance block is required.

## Conclusion

The entire field eta is independent of the entire field u, not just
of its values on the same edge. Its colors have covariance K and

\[
 0\preceq K\preceq I,\qquad
 I-K\succeq P/N,\qquad \|P\|\le1.                   \tag{4}
\]

This is an operator bound for the residual curvature noise, not a
bound for the growing upper potentials or the forest link covariance.

The upper-face cubic action and its conditional square are exactly

\[
 S_{3,\mathrm{top}}=\tfrac12\sum_j\eta_j Q_j,
 \qquad
 F(u):=E[S_{3,\mathrm{top}}^2/2\mid u]
       =\tfrac18 Q^T\mathcal K Q.                    \tag{5}
\]

Let q_A(u)=sum_e |Q_e|^2/8, and let S_(4,nr,top) be precisely the
sum of L029's nonradial quartic (not the radial action term). Then

\[
\begin{split}
 Z(u)&=q_A(u)-F(u)=\tfrac18 Q^T(I-\mathcal K)Q\ge0,\\
 Z(u)&\ge\tfrac1{8N}\sum_c (Q^c)^T P Q^c,\\
 R(X)&=S_{4,\mathrm{nr,top}}-q_A(u)\\
 &=\sum_e\left[-\tfrac1{24}|[L_e,d_e]|^2
 -\tfrac16\langle[H_e,d_e],[H_e,L_e]\rangle\right].
\end{split}                                                        \tag{6}
\]

The actual quadratic observables cannot be deleted from conditioning.
Their complete upper-face/upper-face cubic-pair cumulant is

\[
 \tfrac12\kappa(f,r,S_{3,\mathrm{top}},S_{3,\mathrm{top}})
 =\kappa(f,r,F)+\mathcal E(f,r),                       \tag{7}
\]

where all expectations on the right are in the original forest law,
and the explicit correction is

\[
\begin{split}
\mathcal E(f,r)=\tfrac18 E\sum_{j,k}Q_jQ_k\big[&
(f-Ef)\mathcal D_j\mathcal D_k r
 +(r-Er)\mathcal D_j\mathcal D_k f\\
&+(\mathcal D_j f)(\mathcal D_k r)
 +(\mathcal D_k f)(\mathcal D_j r)\big].               \tag{8}
\end{split}
\]

Consequently the complete selected nonradial upper-face quartic and
upper-face/upper-face cubic pair satisfy the finite identity

\[
 -\kappa(f,r,S_{4,\mathrm{nr,top}})
 +\tfrac12\kappa(f,r,S_{3,\mathrm{top}},S_{3,\mathrm{top}})
 =-\kappa(f,r,Z+R)+\mathcal E(f,r).                   \tag{9}
\]

All distinct upper-face pairs and both L048 pairing classes are in
(7)–(9). Pairs involving a non-upper-face cubic remain outside this
selected identity. Pointwise positivity of Z gives no sign for its
cumulant against the indefinite residual r. Neither Z, R nor E has
been bounded at a^2 scale, and no cancellation of L047's coefficient,
logarithmic coefficient, finite matching, mesh-uniform interacting
remainder or reflected error <= c_box/2 is asserted. Full field
construction, reflection positivity, infrared control and finite
positive mass remain open.

## Proof

### 1. Global Gaussian regression and the uniform noise bound

Use the Hodge Gaussian z only through L026's exact *linear* lift into
the forest law. The three independent colors have identical covariance.
L029's zero-axial-mode identity gives, for every interior vertex pair
v,w and every axial level s,

\[
 u(v)=\sum_{s=0}^{N-1}z_1(s,v),\quad
 \operatorname{Cov}(u(v),u(w))=N G3(v,w),\quad
 \operatorname{Cov}(u(v),z_1(s,w))=G3(v,w).            \tag{10}
\]

Boundary values in these equations are zero. Different link components
of z are independent. L029's actual upper circulation is

\[
 d_e=z_1(N-1,v)-z_1(N-1,v')-z_\mu(N-1,v).            \tag{11}
\]

Combining (10) and (11), simultaneously for all vertices and edges,
gives

\[
 \operatorname{Cov}(u,d)=G3 T3^T,
 \quad \operatorname{Cov}(u,L)=N G3 T3^T,
 \quad \operatorname{Cov}(L,L)=N P.                 \tag{12}
\]

Hence Cov(u,eta)=0. These fields are jointly centered Gaussian linear
functions of the original forest vector; zero cross covariance implies
independence, including any degenerate edge rows. Moreover
Cov(d,L)=P and Cov(L,d)=P, so expanding Cov(d-L/N) gives
K=K_d-P/N. Covariance positivity proves K>=0.

For clarity, K_d<=I is a bound on the *whole* upper-face block.
The full dimensionless relative curvature covariance is
D1 Delta^(-1) D1^T. From D1^T D1<=Delta its operator norm is at
most one. Restricting to distinct upper-face plaquette rows is an
orthogonal coordinate restriction; consequently K_d<=I, with the
boundary rows retained. This does not follow merely from the
individual variance bounds in L029. Also T3^T T3=Delta3 for the
relative transverse vertex space, since all active transverse edges,
including end edges, are retained. Thus P is the orthogonal projection
onto im T3, in particular 0<=P<=I. The weaker inequality
T3^T T3<=Delta3 would suffice for its norm bound. Therefore
K<=I and I-K=(I-K_d)+P/N>=P/N. This proves (4).
No external heat factor has been assigned to K.

### 2. The cubic and the action-only conditional compensation

L029's ordered logarithm has w1=d and
w2=([H,L]+[L,d])/2. L048's cubic convention is <w1,w2>.
Ad-invariance gives <d,[L,d]>=0, and the SU(2) bracket is
minus cross product. Since H cross L=-u(v) cross u(v'),

\[
 q_{3,e}=\tfrac12\langle d_e,[H_e,L_e]\rangle
         =\tfrac12 d_e\mathbin\cdot Q_e.
\]

L_e is a linear combination of the two factors of Q_e, so
L_e dot Q_e=0 identically. Replacing d_e by eta_e+L_e/N
therefore proves the first identity in (5). This includes an edge
with a pinned endpoint, where Q_e and the cubic both vanish.
It is the actual polynomial on the forest slice, not a replacement
by a linearly gauge-invariant Hodge polynomial.

Independence from (12) gives the second identity in (5), with
factor (1/2)*(1/2)^2=1/8. The nonlocal covariance mathcal K
retains every edge pair and all colors. From (4) one gets (6)'s
bounds. The first term in L029's exact quartic is
|[H,L]|^2/8=|Q_e|^2/8. Subtracting it leaves exactly R in (6).
Thus the conditional action square is dominated pointwise by the
quartic restricted to d=0; this is not a statement about the full
quartic, about a cumulant sign, or about its leading cutoff coefficient.

### 3. Keep both observable derivatives in Gaussian conditioning

Import the standard **finite-dimensional Gaussian integration-by-parts
identity**, E[Y_j h(Y)]=sum_k Cov(Y_j,Y_k) E[partial_k h(Y)]
for a centered Gaussian vector and a polynomial h. It follows by
ordinary integration by parts against the nondegenerate Gaussian
density; a linear-image representation gives the same identity for
degenerate joint vectors. No exponential cubic moment is needed.

The covariance of u on its interior vertex space is N G3 per color,
hence invertible. Write X=m(u)+Y by Gaussian regression. Y is
independent of u, eta is a centered linear function of Y, and
Cov(Y,eta_j)=Cov(X,eta_j)=v_j, since Cov(u,eta)=0.
In particular D_j u=0, and thus D_j Q=0. Twice applying the
Gaussian identity conditionally on u gives, for every polynomial h,

\[
 E[\eta_j\eta_k h\mid u]
 =\mathcal K_{jk} E[h\mid u]
  +E[\mathcal D_j\mathcal D_k h\mid u].              \tag{13}
\]

The first application differentiates eta_k and produces K_(jk);
the second contracts eta_k with the derivative of h. There are
no derivatives of a conditional mean or of Q, since u is fixed and
D_j u=0. The full covariance directions v_j in (3) include every
forest coordinate, not just the three local upper-face entries.

Multiplying by Q_j Q_k/8 and summing yields

\[
 E[h S_{3,\mathrm{top}}^2/2]=E[h F]+H(h),\quad
 H(h)=\tfrac18 E\sum_{j,k}Q_jQ_k\mathcal D_j\mathcal D_k h,
 \quad H(1)=0.                                      \tag{14}
\]

Because f,r are even quadratics and S_(3,top) is odd, the finite
cumulant partition formula of L011, or L048(7), gives

\[
 \tfrac12\kappa(f,r,S_{3,\mathrm{top}},S_{3,\mathrm{top}})
 =\kappa(f,r,S_{3,\mathrm{top}}^2/2).                \tag{15}
\]

Indeed pair terms involving E[f S3_top], E[r S3_top] or E[S3_top]
vanish by Gaussian parity; the remaining five terms are precisely the
three-cumulant on the right. Substitute (14) for h=fr,r,f,1 in
those five terms. The correction is H(fr)-Ef H(r)-Er H(f).
The product rule for the commuting constant directions D_j,D_k
expands this expression into (8), proving (7). These algebraic
steps use the entire top cubic sum, hence do not delete ordered
distinct plaquettes or either quadratic-path orientation. Finally
F-S_(4,nr,top)=-Z-R by (6); cumulant multilinearity proves (9).

### 4. What the identity does and does not settle

Equations (4) and (9) replace an undamped upper cubic-pair covariance
by a bounded noise operator, a nonlocal quartic defect, and explicit
observable derivative corrections. They supply a possible route to
scaling estimates without the false uniform forest-link bound.
They do not prove that I-K is small: (4) is an upper bound for K,
not convergence of K to identity. Even small pointwise Z would not
control its cumulant without retaining f and r. Nor may E be dropped
merely because eta is independent of u: f and r are functions of all
forest coordinates. R still contains internal d contractions.

There is no claimed a^2 limit in (9). L047's selected noncancellation
is preserved; its comparison requires evaluating or bounding the
complete right side plus pairs outside E_top and other L011 jets.
L019's full nonlinear forest compensation is still an independent
requirement. This is a local reproduction/specialization of finite
Gaussian regression and integration by parts; no originality or
progress beyond the inspected bulk renormalization sources is claimed.

### 5. Exact finite checks

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_upper_cubic_conditioning.py`.
The certificate is `scripts/combined-ward-response/upper-cubic-conditioning-certificate.json`.
Its complete ten checks and empty failures field were inspected. The test
uses three independent SU(2) colors, three vertex potentials, two adjacent
edges sharing a potential, and correlated noise with one-color covariance
[[1/2,1/4],[1/4,3/4]], independent of the potentials. Direct rational
Gaussian moment recursion verifies (14) for h=1,f,r,fr for two quadratic
probes, and verifies (7). One probe involves only the potentials; the
other also involves noise. Both residuals depend on noise.

The complete/effective/correction values are respectively
(-45189/16,-11403/4,423/16) and
(-25443/64,-4617/32,-16209/64). Thus the correction need not vanish
even when the probe depends only on potentials: the residual remains
noise dependent. These are finite surrogate checks of factors and
connected subtractions, not original-box probe evaluations or cutoff
bounds. The lattice noise bound and identity for arbitrary mesh follow
from the analytic proof above, not these examples.

## Mathlib

Coverage of the full specialized conditional compensation identity:
**not checked**. Coverage of supporting finite Gaussian regression,
independence from vanishing cross covariance, integration by parts,
relative cochain projections and SU(2) Taylor identities: **not checked**.
No matching Mathlib theorem is asserted. The named finite Gaussian
identity is imported; L011, L018, L026, L029 and L048 supply the actual
lattice conventions. The specialization is needed to identify the
boundary noise, its global operator bound and the observable derivative
terms, which the approved literature does not evaluate for these probes.
