# L060 — The mixed-cubic residual cross covariance is not boundary localized

## Hypotheses

Keep L026 and L048–L050's actual SU(2) straight lower-rooted forest
Gaussian on the all-face pinned box, in dimensionless stored coordinates,
a=8/N, with admitted even N. The small-coupling coefficient is taken at
fixed mesh first. There are three independent colors with identical
covariance; all covariance operators below are for one color. Retain
every transverse end edge and every axial level s=1,...,N-1. Use the
original two quadratic probes and residual when interpreting the result
inside L058's mixed cumulant; no observable is conditionally averaged.

Let z be L026's Hodge field whose exact linear forest lift is x. Write
T, Delta_0, Delta_T, G=Delta_0^(-1), P=TGT^T as in L050, and D for
the transverse edge-to-plaquette incidence. Thus Delta_0=T^T T,
Delta_T=TT^T+D^T D and DT=0. Set

\[
 t_s=s/N,\quad u=\sum_{\ell=0}^{N-1}z_1(\ell),\quad
 \beta_s=\sum_{\ell=0}^{s-1}z_1(\ell)-t_su,\quad
 \xi_s=x_T(s)-t_sTu=z_T(s)+T\beta_s.                 \tag{1}
\]

The signs agree with (T phi)_e=phi(v)-phi(v') and L026's forest
lift. Vertex fields are zero on the transverse boundary. Keep L049's
upper noise eta=T(z_1(N-1)-u/N)-z_T(N-1). Let g_s(lambda) be exactly
L058(3)'s last-row interval Dirichlet Green function.

## Conclusion

The entire residual field xi is independent of u, and its cross
covariance with the upper noise is exactly

\[
 \boxed{K_s:=\operatorname{Cov}(\eta,\xi_s)
       =-t_sP-g_s(\Delta_T)(I-P).}                 \tag{2}
\]

This identity uses all frequencies and all boundary rows. For the
Euclidean direct sum of the N-1 transverse edge spaces define
\(\mathscr K(v_1,\ldots,v_{N-1})=\sum_s K_sv_s\). Then

\[
 \|K_s\|=t_s,\qquad
 \boxed{\|\mathscr K\|^2
   =\sum_{s=1}^{N-1}t_s^2
   =\frac{(N-1)(2N-1)}{6N}.}                       \tag{3}
\]

In particular neither a mesh-uniform square-summability bound for the
link cross block nor uniform decay with distance from the upper face
is available. Its gradient restriction has norm asymptotic to
sqrt(N/3). Also sum_s ||K_s||=(N-1)/2 exactly.

Nevertheless for every retained transverse edge e,

\[
 \operatorname{Var}(\xi_s(e))\le8+s(1-s/N).
                                                               \tag{4}
\]

If both endpoints of e are interior, there is also the lower bound
\(\operatorname{Var}(\xi_s(e))\ge s(1-s/N)/8\).
Thus local residual variances are bounded at a fixed number of lattice
steps from the upper face, while remaining of order N in the bulk.
These diagonal facts do not imply a localized cross operator.

Equation (2) recovers L058's curvature covariance after multiplication
by D^T, since PD^T=0. The deleted gradient block cannot be omitted
from derivatives of an entire transverse cubic merely because its
linear circulation vanishes. A single actual cubic vertex has a
nonzero derivative in a gradient direction, as checked below.

This is a negative test of a proposed covariance-localization estimate
for kappa(f,r,H-M)+E_mix. It is NOT a lower bound, nonvanishing claim,
or cutoff estimate for that signed correction. Cancellation after
the full cubic and observable contractions remains possible. No new
a^2-scaled mixed coefficient, logarithm, matching, reflected-error
bound <=c_box/2, continuum construction or mass gap follows.

## Proof

### 1. Exact regression and the scalar interval identity

Use the standard finite-dimensional Gaussian regression theorem:
jointly Gaussian linear images with zero cross covariance are
independent, including degenerate images. This is the same named
input used in L049, proof section 1. Its hypotheses hold for the
finite Hodge vector and its exact forest lift; no nonlinear action
is transferred to an unmodified Hodge law.

L049(10) gives Cov(u,u)=NG and Cov(z_1(ell),u)=G.
Hence Cov(beta_s,u)=sG-t_s NG=0. The transverse components z_T
are independent of the axial component, so Cov(xi_s,u)=0 for every
s. Gaussian regression proves the claimed joint independence and
E[x_T(s)|u]=t_s Tu. It does not make xi independent of eta or of
either observable.

For the scalar computation let L_E be the N-by-N interval edge
Neumann Laplacian, with endpoint diagonal 1, interior diagonal 2,
and neighboring entries -1. Let B be the (N-1)-by-N difference
matrix (Bh)_s=h_s-h_(s-1). Then L_E=B^T B and
L_D=BB^T, where L_D has diagonal 2 and neighboring entries -1.
For lambda>0 put h=(L_E+lambda I)^(-1)e_(N-1).
The intertwining identity B L_E=L_D B gives

\[
 Bh=(L_D+\lambda I)^{-1}e_{N-1},\qquad
 h_s-h_{s-1}=g_s(\lambda).                         \tag{5}
\]

Here the last equality uses symmetry of the Dirichlet inverse and
L058's exact definition, including s=N-1. Sum the first s rows of
(L_E+lambda I)h=e_(N-1), for s<N. The Laplacian terms telescope
to h_(s-1)-h_s and the source is absent. Therefore

\[
 \lambda\sum_{\ell=0}^{s-1}h_\ell=g_s(\lambda).
                                                               \tag{6}
\]

Summing all N rows similarly gives sum_ell h_ell=1/lambda.
The covariance with the centered path coefficients is consequently

\[
 \operatorname{Cov}(z_1(N-1)-u/N,\beta_s)
       =\frac{g_s(\Delta_0)-t_s I}{\Delta_0}.       \tag{7}
\]

For clarity, on each transverse vertex eigenmode the first path
term in (7) is sum_(ell<s) h_ell=g_s(lambda)/lambda; subtracting
t_su contributes t_s/lambda. Subtracting u/N from the first factor
has no further effect because Cov(u,beta_s)=0. This is an exact
finite-matrix identity over the complete positive spectrum, not a
low-frequency asymptotic statement.

### 2. Link cross covariance and its full operator norm

Independence of the Hodge components and their tensor-product
relative boundary conditions give

\[
 \operatorname{Cov}(z_T(N-1),z_T(s))=g_s(\Delta_T).
                                                               \tag{8}
\]

Every transverse link component has an axial Dirichlet vertex
coordinate. The remaining three coordinates give Delta_T, including
its own-direction edge cosine modes and all end rows; this is the
same block used in L058(13), before applying D^T.

Combine (1), (7), (8) with eta's definition. The component cross terms
vanish, and Delta_T T=T Delta_0 implies

\[
 K_s=T[g_s(\Delta_0)-t_sI]\Delta_0^{-1}T^T
                 -g_s(\Delta_T)
     =[g_s(\Delta_T)-t_sI]P-g_s(\Delta_T).
\]

This proves (2). All spectral functions commute with P by L050.
L058's interval maximum-principle proof gives 0<=g_s(lambda)<=t_s
for every lambda>0 and every s. Thus (2) is an orthogonal block
decomposition: on im P it is -t_s I and on ker P its norm is at
most t_s. The gradient space is nonempty because there are
(N-1)^3>0 interior vertices and T^T T is positive definite. Hence
||K_s||=t_s, including N=2.

The adjoint product of the concatenated cross operator is

\[
 \mathscr K\mathscr K^T
   =\left(\sum_s t_s^2\right)P
      +\left(\sum_s g_s(\Delta_T)^2\right)(I-P).
                                                               \tag{9}
\]

The second block is bounded by sum_s t_s^2 and the first attains
it. The elementary sum of squares proves (3), and the sum of t_s
gives the stated sum of norms. For example, s=N/2 has
K_s P=-P/2 at physical distance 4 from the upper face for every
even N. At the last level xi_(N-1)=-eta by (1), and (2) becomes
-[(1-1/N)P+g_(N-1)(Delta_T)(I-P)]=-Cov(eta,eta),
agreeing with L050's K and g_(N-1)=1-b_N. This independently checks
the sign and the gradient normalization at the endpoint.

### 3. Local conditional variance does not yield cross localization

For a fixed edge e the path term T beta_s uses the axial coefficient
vector b_ell=1_(ell<s)-t_s. Its squared Euclidean norm is exactly

\[
 \sum_{\ell=0}^{N-1}b_\ell^2=s(1-s/N).             \tag{10}
\]

L026's full-spectrum bound for the transverse difference of the axial
Hodge field is T_ax Sigma_1 T_ax^T<=I, with the entire axial index
retained. Apply that bound to the vector b on the selected edge and
zero on the other edges. It bounds Var((T beta_s)_e) by (10).
This argument includes an end edge: its missing boundary vertex is
zero in precisely the same incidence map. The independent direct
transverse Hodge link has variance at most 8 by L026(11), proving
(4). If both endpoints are interior, the axial linear functional
has two disjoint copies of b, with squared norm 2||b||^2. L026's
Sigma_1>=I/16 therefore gives the claimed lower bound. No local
covariance has been used to bound the full concatenated operator.

### 4. Why the curvature projection alone does not remove this block

Since PD^T=0, (2) implies Cov(eta,Dxi_s)=-g_s(Delta_T)D^T.
This is exactly the covariance used in the conditional mean
calculation L058(13). At the conditional mean, the transverse
linear circulation w1 is zero and only its derivative contributes
to the cubic q3=<w1,w2>. Away from the conditional mean the other
product-rule term <w1,partial w2> is present.

An explicit check uses L048(4)'s actual ordered SU(2) cubic
q3(y)=-sum_(r<s<t) y_r dot (y_s cross y_t)/2. On a transverse
plaquette with four interior vertices take y=(0,e1,e2,0), where
e1,e2,e3 are the standard color basis. Take the gradient variation
h=(e3,-e3,0,0), realized by vertex values (0,-e3,0,0) in traversal
order. This potential extends by zero to the other vertices and
respects the pinned boundary. The selected forest transverse links
are free coordinates, so the displayed y is admissible on that
plaquette. Its directional derivative is exactly

\[
 D_h q3(y)=-\tfrac12 e3\mathbin\cdot(e1\mathbin\times e2)
          =-\tfrac12,\qquad \sum_r h_r=0.          \tag{11}
\]

Only the increasing triple (1,2,3) contributes. Thus the cubic
derivative does not factor only through the linear circulation of
the variation. This example does not compute the sum over all
plaquettes, the contraction with the actual Q, or either observable;
those may still cancel the gradient block. It identifies precisely
why the operator in (2) cannot be replaced by its transverse block
on the strength of L058's conditional calculation alone.

### 5. Scope, verification and specialization

The attempted estimate was uniform boundary localization of the
cross covariance entering L058's retained mixed correction. Equations
(2)–(3) disprove that estimate for the actual covariance, not for a
surrogate. The discriminating threshold was an N-independent squared
norm; the actual value is (N-1)(2N-1)/(6N), asymptotic to N/3.
The exact interval recurrence, its two endpoint conditions, pinned
cochain intertwining, and (11) were checked analytically. No numerical
certificate or mathematical script is needed for these identities.

The downstream task remains to contract the gradient sector jointly
with the full cubic derivatives and both quadratic observables, or
to prove a weaker bound sufficient after that contraction. Neither
the norm in (3) nor the variance lower bound is a lower bound on a
signed cumulant. In particular they do not alter L059's conditional
scaled limit, assign it to the mixed response, or obstruct every
possible estimate of the remainder.

Reuse the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`. This is local
REPRODUCTION using the named finite Gaussian regression theorem and
existing finite relative spectral identities, not a claim of progress
beyond the literature checked. The necessary specialization is the
link cross block left out by the already computed curvature
projection; no general flow or stress-renormalization theorem is
reproved or given new boundary hypotheses.

## Mathlib

Coverage of this full specialized covariance identity and norm:
**not checked**. Supporting finite Gaussian regression, cochain
intertwining, spectral calculus and finite sum identities:
**not checked**. No matching Mathlib theorem is asserted. The named
Gaussian theorem and the exact local spectral inputs are specified
above; unknown coverage is not evidence of absence.
