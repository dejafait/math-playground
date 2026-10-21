# L058 — Mixed upper/transverse cubic pairs have a retained defect operator

## Hypotheses

Keep the admitted even mesh a=8/N, SU(2), all-face pinned box, bare
coupling, direction-1 lower-rooted straight forest and both actual
Wilson-flow probes i=3,6 at tau=1/16. Take the small-coupling coefficient
at fixed mesh first. Use L011's cumulants and L048's actual forest
Gaussian vector X, with three independent colors and identical one-color
covariance Sigma_F. Set f=f_(i,0), r=r0; these are the actual
color-diagonal quadratics, up to irrelevant constants, not replacements
by a restricted-Hessian flow.

Use exactly L049's whole upper transverse edge set, upper potentials u,
Q_e=u(v) cross u(v'), eta=d-Tu/N and constant covariance derivatives
mathcal D_j=Cov(X,eta_j) dot grad_X. The index j includes edge and color.
Use L050's transverse relative cochains T=T3, D=D_(1,T),
Delta_T=TT^T+D^T D, P=T(T^T T)^(-1)T^T, and boundary symbol b_N.
All transverse end edges and every transverse direction remain.

Split the complete cubic action as

\[
 C=S_{3,\mathrm{top}}=\tfrac12\sum_j\eta_j Q_j,
 \qquad Y=S_3-C.
\tag{1}
\]

Here Y contains **every** other plaquette, including zero vertices.
The selected contribution of exactly-one-upper ordered pairs to
L011's two-cubic term is

\[
 \mathcal M_i=\kappa(f,r,C,Y).
\tag{2}
\]

There is no outside factor 1/2 in (2): the two mixed regions of the
ordered sum each carry 1/2 and cumulant symmetry combines them.

For lambda>0 let L_D be the unscaled interval Dirichlet vertex
Laplacian on s=1,...,N-1, with diagonal 2 and neighboring entries -1.
Define

\[
\begin{split}
 g_N(s;\lambda)&=((L_D+\lambda I)^{-1})_{N-1,s}
     =\frac{\sinh(s\gamma)}{\sinh(N\gamma)},
 \quad\gamma=2\operatorname{arsinh}(\sqrt\lambda/2),\\
 \chi_N(\lambda)&=\lambda\sum_{s=1}^{N-1}(s/N)^2g_N(s;\lambda).
\end{split}\tag{3}
\]

All finite-matrix spectral functions below use the **whole** spectrum.

## Conclusion

The conditional mixed action product is exactly the nonnegative quartic

\[
 \boxed{M(u):=E[CY\mid u]
   =\tfrac14\sum_{c=1}^3
     \langle Q_\perp^c,\chi_N(\Delta_T)Q_\perp^c\rangle,
 \quad Q_\perp^c=(I-P)Q^c.}
\tag{4}
\]

For every lambda>0 and N>=2,

\[
 \chi_N(\lambda)>0,\qquad
 \frac1N\le b_N(\lambda)-\chi_N(\lambda)\le\frac2N.
\tag{5}
\]

Thus the conditional mixed operator approaches the *same* rough defect
operator, uniformly over all frequencies, rather than making the defect
small. In L049–L050's notation q_A=sum_c ||Q^c||^2/8 and
Z=Q^T(I-mathcal K)Q/8, the precise pointwise comparison is

\[
 \frac{2q_A}{N}\le 2Z-M\le\frac{4q_A}{N}.
\tag{6}
\]

The actual mixed cumulant retains both observable corrections and the
fluctuations removed by conditional averaging. Define the quartics

\[
 H(X)=\tfrac12\sum_j Q_j\mathcal D_jY,
 \qquad T_*(X)=H(X)-M(u),\qquad E[T_*\mid u]=0.
\tag{7}
\]

Then the exact complete identity is

\[
\begin{split}
 \boxed{\mathcal M_i
 =\kappa(f,r,M)+\kappa(f,r,T_*)+\mathcal E_{\mathrm{mix}}(f,r),}\\
 \mathcal E_{\mathrm{mix}}(f,r)
 =\tfrac12 E\sum_j Q_jY\big[(r-Er)\mathcal D_j f
                         +(f-Ef)\mathcal D_j r\big].
\end{split}\tag{8}
\]

Neither correction in (8) is deleted. All other plaquettes and both
L048 connected pairing classes are retained by the exact cumulant.
Positivity of M, or (6), gives no sign for (8) against the indefinite r,
and no scaled bound for either correction. This proves no a^2-scaled
mixed response, compensation of C057a, complete power or logarithmic
coefficient, bounded remainder, finite matching, interacting reflected
error <=c_box/2, continuum construction or finite positive mass.
The mixed action group is not asserted to be forest invariant by itself;
L019's full nonlinear observable-jet compensation is still required.

## Proof

### 1. Every non-upper cubic and the conditional mean links

L026's exact linear forest lift is x=z-D0 phi_z, with phi_z(s,v)
the lower axial sum for 1<=s<=N-1 and zero at boundary vertices.
L049's global zero-axial-mode covariance gives

\[
 E[z_1(\ell,v)\mid u]=u(v)/N,
 \qquad E[z_\mu(s,e)\mid u]=0\quad(\mu=2,3,4).
\tag{9}
\]

Indeed Cov(u,u)=NG3 and Cov(z_1(ell),u)=G3; the transverse components
are independent of the axial field. Both formulas hold with pinned
transverse values zero. Hence the conditional mean transverse links at
axial level s are

\[
 m_\mu(s,e)=(s/N)(Tu)_e,\qquad 1\le s\le N-1.
\tag{10}
\]

For an axial plaquette below the upper layer, both axial entries in the
forest slice are zero, including boundary zero-row cases. Its only
possible nonzero ordered entries are its two transverse edges. L048's
cubic needs three distinct entries, so this cubic vanishes identically,
without conditioning. Axial plaquettes in the last layer are exactly C;
those contained in another fixed face are zero. Transverse plaquettes
at s=0,N are fixed and zero. Consequently Y consists exactly of the
transverse plaquette cubics at s=1,...,N-1, with every active relative
plaquette retained. This includes transverse boundary zero edges.

For a transverse oriented polygon with consecutive vertices
v0,v1,v2,v3, its mean signed entries are
y_l=(s/N)(u(v_l)-u(v_(l+1))), with v4=v0. Their sum w1 is zero.
The elementary polygon identity is

\[
 \sum_{l<k}(u_l-u_{l+1})\times(u_k-u_{k+1})
       =\sum_{l=0}^3u_l\times u_{l+1}.
\tag{11}
\]

To check it, the left side equals sum_k (u0-u_k) cross
(u_k-u_(k+1)); the u0 terms telescope, leaving the right side.
The identity holds also at a pinned vertex u_l=0. Since the SU(2)
bracket here is minus cross product, L048's w2=(1/2)sum_(l<k)[y_l,y_k]
at the conditional mean is therefore

\[
 w_2(m)=-\tfrac12(s/N)^2(DQ)_p,
 \qquad w_1(m)=0.
\tag{12}
\]

D uses precisely the signed edge traversal, so its action on Q is the
right side of (11). No continuum, locality or heat approximation enters.

### 2. Retain the full cross covariance before conditional averaging

The transverse circulation at level s is D z_T(s): the path correction
is a gradient and D T=0. L049's upper noise is
eta=T z_1(N-1)-z_T(N-1)-Tu/N. The first and last terms depend only on
the axial component and are independent of z_T. L026/L050's complete
relative tensor decomposition therefore gives, for one color,

\[
 \operatorname{Cov}(\eta,Dz_T(s))
       =-g_N(s;\Delta_T)D^T.
\tag{13}
\]

In fact Cov(z_T(N-1),z_T(s))=g_N(s;Delta_T), since the axial coordinate
of every transverse component has Dirichlet vertex conditions and the
remaining operator is Delta_T. This identity includes its edge cosine
zero modes, transverse vertex sine modes and end-edge rows. It does not
assign any positive-time heat factor to an internal contraction.

Import the standard finite-dimensional **Gaussian integration-by-parts
identity** E[Z_j h]=sum_k Cov(Z_j,Z_k) E[partial_k h] for centered
Gaussian vectors and polynomials. This is the named identity used and
justified for degenerate joint linear images in L049, proof section 3.
Since eta is independent of u, the same identity conditioned on u uses
the unchanged directions mathcal D_j=Cov(X,eta_j) dot grad_X, and
mathcal D_j u=mathcal D_j Q=0. Thus

\[
 E[CY\mid u]=\tfrac12\sum_j Q_j E[\mathcal D_jY\mid u].
\tag{14}
\]

For each cubic q_3, E[mathcal D_j q_3|u]=(mathcal D_j q_3)(m).
Here is the essential color check. L048's symmetric cubic tensor is
-omega_(rst) epsilon_(abc)/12. A directional derivative leaves a
quadratic tensor with two remaining colors. Their conditional covariance
is color diagonal because regression on the entire u field is identical
in the three independent colors. Every conditional contraction then sets
these two colors equal, annihilating epsilon. The only surviving term is
the product of the two means. This reasoning includes zero rows and does
not assume that the conditional link covariance is local.

At a transverse mean, q3=<w1,w2> and w1(m)=0, so
(mathcal D_j q3)(m)=<mathcal D_j w1,w2(m)>.
Insert (12) and (13) into (14) to obtain, for every color,

\[
 E[CY\mid u]
  =\tfrac14\sum_c\sum_{s=1}^{N-1}(s/N)^2
       \langle Q^c,g_N(s;\Delta_T)D^T D Q^c\rangle.
\tag{15}
\]

Both minus signs have been retained. On relative transverse cochains,
P is the orthogonal gradient projection, Delta_T commutes with P, and
D^T D=Delta_T(I-P). Indeed D T=0, while TT^T=Delta_T on im T and
T^T vanishes on its orthogonal complement. These are the same finite
cochain identities as L050. Equation (15) is therefore (4). Positivity
of g_N follows either from (3) or the interval maximum principle.

### 3. The discrepancy bound is uniform over rough modes

The endpoint Green row in (3) follows directly from the recurrence
(2+lambda)g_s-g_(s-1)-g_(s+1)=0, g_0=0, g_N=1. In matrix form this
says (L_D+lambda)g=e_(N-1). The hyperbolic formula satisfies the two
boundary values and recurrence; positivity of L_D+lambda gives uniqueness.
In particular its last interior entry is L050's W_N(lambda), and that
lemma's exact identity gives

\[
 b_N(\lambda)=1-g_N(N-1;\lambda).
\tag{16}
\]

Let t_s=(s/N)^2 on interior vertices. Its full second difference is
-2/N^2 and its boundary values are t0=0, tN=1. With the missing boundary
value restored separately, exactly

\[
 (L_D+\lambda)t=\lambda t-2\mathbf1/N^2+e_{N-1}.
\tag{17}
\]

Multiply (17) by the last row of (L_D+lambda)^(-1). Using
t_(N-1)=(1-1/N)^2 and (16) yields

\[
 \chi_N=b_N-\frac2N+\frac1{N^2}
                  +\frac2{N^2}\sum_{s=1}^{N-1}g_N(s;\lambda).
\tag{18}
\]

For lambda>0 the interval inverse has nonnegative entries: a negative
minimum in a vector solving (L_D+lambda)v>=0 with zero boundary
contradicts its minimum-row equation. This proves inverse positivity.
Compare g with h_s=s/N, for which (L_D+lambda)h=e_(N-1)+lambda h.
Inverse positivity gives 0<=g_s<=s/N, hence
0<=sum_s g_s<=(N-1)/2. Substituting these two bounds into (18) gives
1/N<=b_N-chi_N<=2/N-1/N^2<=2/N. Also chi_N>0 from (3), since each
interior g_s and t_s is positive. This proves (5) for all lambda>0,
independently of the cutoff-frequency regime.

L050's full defect is P/N+b_N(Delta_T)(I-P). Subtracting (4) from
twice its quartic form gives

\[
 2Z-M=\tfrac1{4N}\sum_c\|Q_\parallel^c\|^2
  +\tfrac14\sum_c\langle Q_\perp^c,
                      (b_N-\chi_N)(\Delta_T)Q_\perp^c\rangle.
\tag{19}
\]

Orthogonality of P and (5) prove (6), with no restriction on the actual
nonlinear product Q. This compares M with 2Z; it does not contradict
L050's nonsmall rough defect or revive ATTEMPTS/017's stopped route.

### 4. Complete connected observables remain

Apply Gaussian integration by parts to CY times any polynomial h,
using mathcal D_j Q=0. The exact unconditioned formula is

\[
 E[hCY]=E[hH]+\tfrac12\sum_j E[Q_jY\mathcal D_jh].
\tag{20}
\]

All expectations are finite Gaussian polynomial moments. There is no
exponential of a cubic to integrate. Equations (14) and (20) conditioned
on u prove E[H|u]=M, so the last statement of (7) follows.

Because f,r are even and C,Y are odd, parity removes E[C], E[Y],
E[fC], E[fY], E[rC], E[rY] and the corresponding triple terms from
the cumulant partition formula. Its remaining terms are exactly

\[
\begin{split}
 \kappa(f,r,C,Y)=\kappa(f,r,CY)
  ={}&E[frCY]-Ef E[rCY]-Er E[fCY]\\
     &-E[fr]E[CY]+2Ef Er E[CY].
\end{split}\tag{21}
\]

Use (20) for h=fr,r,f,1. The derivative of 1 is zero. The product
rule gives mathcal D_j(fr)=r mathcal D_j f+f mathcal D_j r, so the
extra terms are precisely mathcal E_mix in (8). The remaining terms
are kappa(f,r,H). Splitting H=M+T_* proves (8). This calculation uses
the complete Y and is equivalent to retaining both L048 connected
pairing classes; it neither truncates the plaquette index nor drops a
quadratic-path orientation.

Conditional centering of T_* does not imply kappa(f,r,T_*)=0:
f and r depend on the residual field. Similarly, independence of eta
and u does not eliminate the derivatives in (8). Inequality (6) is
pointwise and supplies no signed-cumulant estimate with the indefinite
residual. An all-mode analysis of these retained terms is still needed
before comparing a^2 mathcal M_i with C057a or extracting logarithms.

### 5. Exact finite consistency checks and qualifications

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_top_other_cubic.py`.
The complete certificate is
`scripts/combined-ward-response/top-other-cubic-certificate.json`.
All 46 exact checks and its empty failures field were inspected.
Three polynomial identities check (11)–(12), including a pinned
vertex. A Gaussian surrogate with three vertex potentials, two
correlated noise coordinates and three independent colors checks the
conditional product, (20) for h=1,f,r,fr for two probes, and (8).
Its cubic uses an actual ordered four-edge tensor with a gradient mean,
but its covariance is a surrogate, not the original box cross block.

For its two complete cumulants, the effective quartic, fluctuation and
observable correction are respectively
(15192,0,-549/8) and (3159/4,0,22761/16), giving totals
120987/8 and 35397/16. Thus the observable correction is not generally
zero. The fluctuation happens to contract to zero in these cases; no
such statement is made for the actual probes. Sixteen exact rational
interval cases N=2,4,8,16, lambda=1/N^2,1,4,12 check (18), positivity,
the Green comparison and the two bounds in (5). These are finite
algebra checks. The arbitrary-mesh/full-spectrum claims follow from
the analytic proof, not those finitely sampled eigenvalues.

This is a necessary local specialization of standard Gaussian regression,
integration by parts and finite cochain spectral machinery under the
unchanged combined-response SPECIALIZE assessment. No full matching
claim, originality or progress beyond the inspected sources is asserted.

## Mathlib

Coverage of the full specialized mixed-cubic identity and symbol
comparison: **not checked**. Coverage of supporting finite Gaussian
regression/integration by parts, SU(2) Taylor tensors, relative cochains
and finite-matrix spectral calculus: **not checked**. No matching Mathlib
theorem is asserted. The standard named Gaussian integration-by-parts
identity is imported above; the existing exact lattice identities are
reused. General flow renormalizability and bulk stress matching are not
reproved or used to assign a cutoff coefficient to this selected group.
