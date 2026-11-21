# C466u — Short-time complete localized current across collisions

## Hypotheses

Use real numbers 0<a<R<infinity, 0<b<L<infinity, finite
nonnegative M_1,M_2, and H_0 in C. On
B={|q|<R, |z|<L}, let H be holomorphic with

\[
 H(0,0)=H_0,\qquad \|\nabla H\|_2\le M_1,\qquad
 \|D^2H\|_{\mathrm{op}}\le M_2.                         \tag{1}
\]

The norms are the standard Hermitian ones on the holomorphic
derivatives. On U=B minus {q=0}, set

\[
 f=(-2/q+H_q,H_z),\qquad v=\overline f,\qquad
 \dot X=v(X),\qquad X(0,r,s)=(ir,s).                       \tag{2}
\]

Here I=(-a,a) times (-b,b), r!=0, and [0,tau(r,s)) is the
first maximal forward interval in U. This is C466s's unit flat
raw physical-time flow. No map after tau or at r=0 is defined.
Assume precisely the additional restriction

\[
 T_0>0,\qquad M_1T_0<\min\{R-a,L-b\}.                     \tag{3}
\]

Put Q=(0,T_0) times I and
D={ (t,r,s) in Q : r!=0, t<tau(r,s) }. Let Psi=X on D.
For any complex or real chi in C_c^infinity(B), set

\[
 F=q^2e^{-H},\quad \Omega=F\,dq\wedge dz,\quad
 \beta=\Psi^*(\chi\Omega),\quad
 \gamma=\Psi^*(d\chi\wedge\Omega).                        \tag{4}
\]

All forms are ordinary complex-valued real differential forms.
Bars denote coefficientwise zero extension from D to Q, including
at r=0. Orientation is dt wedge dr wedge ds. In particular beta
has all three coefficients beta_tr, beta_ts and beta_rs.

## Conclusion

No trajectory starting in I has a first outer-boundary endpoint
at a time tau<=T_0. Every such finite endpoint has q=0 and lies
strictly inside both outer modulus bounds. Both bar(beta) and
bar(gamma) have bounded Borel coefficients on Q, and

\[
 d\bar\beta=\bar\gamma\quad\hbox{in distributions on }Q.  \tag{5}
\]

More explicitly, write

\[
 \begin{split}
 E&=\exp\{(3M_2+M_1^2)T_0-\Re H_0
                         +M_1\sqrt{a^2+b^2}\},\\
 m(r)&=2|r|+M_1r^2,\qquad
 C_0=\sup_B|\chi|,\qquad C_1=\sup_B\|d\chi\|.
 \end{split}                                               \tag{6}
\]

For the complex-valued covector dchi, its norm is its operator
norm on real Euclidean tangent vectors. Throughout Q,

\[
 |\bar\beta_{rs}|\le C_0Er^2,\qquad
 |\bar\beta_{tr}|,|\bar\beta_{ts}|\le C_0E m(r),\qquad
 |\bar\gamma_{trs}|\le3C_1E m(r).                         \tag{7}
\]

For every scalar phi in C_c^infinity(Q), a family of smooth
survivor cutoffs constructed below has complete cutoff error
bounded by

\[
 \left|\int_D\phi\,d\eta_\epsilon\wedge\beta\right|
 \le\frac92\|\phi\|_\infty C_0\|\theta'\|_\infty E
       \epsilon\left(4ba^2+\frac43 bM_1a^3\right)
 \longrightarrow0.                                      \tag{8}
\]

The proof uses no regularity assumption on tau, no smooth stopping
hypersurface and no post-exit flow. The same cutoff handles collision
preimages and the initial axis. This local identity does not sign
the complex determinant, prove global signed-integral invariance,
permit an unrestricted-time restart, or supply all-degree positivity
or actual-Xi realization. The proof was completed in attempt966;
independent conceptual audit968 below validates its stated scope. It is a specialization
under assessment964, not a claim of certified originality or an RH
candidate. C466t is a contrasting outer-grazing obstruction, not
a premise of this proof; its unrestricted-time stop is preserved.

## Proof

### Imported local machinery and the additional specialization

C466s supplies the smooth open survivor domain, the finite-endpoint
classification, the real variational matrix, the identity
dot F=-||f||_2^2 F, and the complex-determinant/real-area inequality.
We use these on compact surviving intervals only. The underlying
standard local-flow and continuation results may be located in
Gerald Teschl, *Ordinary Differential Equations and Dynamical
Systems*, author-hosted April2012 preliminary version,
[Lemma2.14 and Corollary2.15, p52; Theorem6.1 and proof, pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
Continuation requires an interior endpoint or compact containment
in the open ODE domain. Nothing here invokes continuation through
the divisor or an outer boundary.

Wu, Kanevskiy and Margaliot, *k-Contraction: Theory and Applications*,
[arXiv:2008.10321v2](https://arxiv.org/pdf/2008.10321v2),
27 September2021, Section3.1, Proposition5 and its proof, printed
p9, with (29) on p8, gives for a continuous real matrix A on a
compact interval and dot Phi=A Phi, Phi(0)=Id,

\[
 \|\Lambda^k\Phi(t)\|
 \le\exp\int_0^t\mu_2(A(u)^{[k]})\,du.                   \tag{9}
\]

This is the compound-evolution growth inequality in the proof;
the negative uniform matrix-measure hypothesis is needed for its
contraction consequence, not for (9). For symmetric A the measure
is the sum of its k largest real eigenvalues. The retained source
assessment covers every k; we apply k=2 and k=3 in real dimension
four. All these applications are to compact smooth survivor
segments, where continuity holds. No singular-endpoint theorem
is being imported.

For the real-parameter variational convention, see also Tanizaki,
Nishimura and Verbaarschot, *Gradient flows without blow-up for
Lefschetz thimbles*, JHEP10(2017)100,
[arXiv:1706.03822v2](https://arxiv.org/pdf/1706.03822v2),
27 September2017, AppendixB, (B.1)–(B.5), printed p22.
The law is dot J=conjugate((D^2S)J), with both factors conjugated.
The realification and its hypotheses are justified in C466s.

These results do not already prove (5). What follows adds the
strict-buffer comparison, velocity/parameter and three-volume
estimates, locally supported survivor cutoffs, and their weak
limit. The fixed-time spatial bound alone cannot replace those
steps. We prove the inhomogeneous weak identity directly; no
homogeneous Harvey–Polking removability conclusion is invoked.

### Outer endpoints are excluded by the actual radial equation

On a survivor write rho=|q|>0, g=H_q(X), h=H_z(X). Equation (2)
gives exactly

\[
 (\rho^2)'=-4+2\Re(qg),\qquad
 \rho'=-2/\rho+\Re(qg)/\rho\le M_1,\qquad
 |\dot z|\le M_1.                                       \tag{10}
\]

Integrating these inequalities only over surviving times yields

\[
 \rho(t)\le |r|+M_1t\le R_*:=a+M_1T_0<R,\qquad
 |z(t)|\le |s|+M_1t\le L_*:=b+M_1T_0<L.                 \tag{11}
\]

The possible finite endpoints from C466s are q=0, |q|=R or
|z|=L, with simultaneous events initially allowed. If tau<=T_0,
taking limits in (11) excludes both outer equalities. Thus only
q=0 remains, with |z_*|<=L_*<L. This also treats tau=T_0
and M_1=0. It does not mistake M_1 for a full velocity bound:
the singular radial velocity in (10) points inward.

### All complete two- and three-dimensional minors

Let V(t)=v(X(t)), U_r=partial_r X and U_s=partial_s X,
regarded as real vectors in R^4. Since the vector field is
autonomous, differentiating V(t) gives dot V=Dv(X)V. Parameter
differentiation gives the same equation for U_r and U_s. Hence
all three vectors evolve under the same real fundamental matrix.

As in C466s this real symmetric variational matrix is

\[
 A w=\overline{(D^2S)w}=A_0w+A_Hw,
 \quad D^2S=\operatorname{diag}(2/q^2,0)+D^2H,
 \quad \|A_H\|\le M_2.                                  \tag{12}
\]

The real spectrum of A_0 is {2/rho^2,0,0,-2/rho^2}.
For k=2 and k=3 its largest-k sum is 2/rho^2. The variational
characterization as maximal trace on an orthonormal k-frame shows
that adding A_H raises that sum by at most kM_2. Therefore

\[
 \mu_2(A^{[k]})\le2/\rho^2+kM_2\quad(k=2,3).             \tag{13}
\]

For either of these k, combine (13) with the exact weighted
identity from C466s before estimating:

\[
 \begin{split}
 \mu_2(A^{[k]})-\|f\|_2^2
 &\le kM_2-2/\rho^2+4|g|/\rho-|g|^2-|h|^2\\
 &=kM_2+|g|^2-|h|^2-2(1/\rho-|g|)^2\\
 &\le kM_2+M_1^2.                                      \tag{14}
 \end{split}
\]

Thus for any k initial real vectors w_1,...,w_k, transported
by this fundamental matrix, (9) and dot F=-||f||_2^2 F imply

\[
 |F(X(t))|\,\|w_1(t)\wedge\cdots\wedge w_k(t)\|
 \le |F(ir,s)|e^{(kM_2+M_1^2)t}
                  \|w_1(0)\wedge\cdots\wedge w_k(0)\|. \tag{15}
\]

All integrated quantities are finite on the chosen compact
surviving interval. In particular (15) is not a cancellation of
two divergent endpoint integrals.

Initially U_r=(i,0), U_s=(0,1) are real orthonormal vectors and

\[
 \|V(0)\|\le2/|r|+M_1,\qquad
 |F(ir,s)|\le r^2\exp\{-\Re H_0+M_1\sqrt{a^2+b^2}\}.     \tag{16}
\]

The second bound is C466s's straight-segment gradient bound on
H(ir,s). The initial two-volumes V wedge U_r and V wedge U_s,
and the initial three-volume V wedge U_r wedge U_s, are at most
||V(0)||. The initial U_r wedge U_s has norm one. Consequently
(15) and M_2>=0 give on every survivor

\[
 \begin{split}
 |F|\|U_r\wedge U_s\|&\le Er^2,\\
 |F|\|V\wedge U_r\|,\ |F|\|V\wedge U_s\|&\le E m(r),\\
 |F|\|V\wedge U_r\wedge U_s\|&\le E m(r).                \tag{17}
 \end{split}
\]

For two real vectors u,w in C^2, C466s's complex Gram identity
gives |dq wedge dz(u,w)|<=||u wedge w||. For a real or complex
covector alpha, evaluated on any real orthonormal triple, expansion
of alpha wedge dq wedge dz has three terms, each of modulus at
most ||alpha||. By an orthonormal basis of the span, and
multilinearity (with the dependent case zero), this proves

\[
 |(\alpha\wedge dq\wedge dz)(u_1,u_2,u_3)|
 \le3\|\alpha\|\,\|u_1\wedge u_2\wedge u_3\|.            \tag{18}
\]

Applying the two-vector bound to (V,U_r), (V,U_s), (U_r,U_s)
and applying (18) with alpha=dchi proves every bound in (7).
This retains the entire mixed minors, including the velocity
column, and the full three-form gamma. The survivor domain is
open, its coefficients are smooth there, and its complement is
Borel. Their zero extensions are therefore Borel. Since r is
bounded on I, (7) proves L^infinity(Q), in particular L1(Q).

### A collision cutoff has locally interior survivor support

Choose a smooth theta:R->[0,1] with theta=0 on (-infinity,1]
and theta=1 on [2,infinity). Write B_theta=||theta'||_infinity.
Take epsilon>0 small enough that 2epsilon M_1<=1, with no
restriction of this kind when M_1=0. On D define

\[
 \eta_\epsilon=\theta(\rho\circ\Psi/\epsilon),             \tag{19}
\]

and set it to zero elsewhere in Q. We now prove this is smooth
on Q and its nonzero set has closure, relative to Q, contained
in D. This is essential: smoothness of a cutoff only on D would
not by itself license extension by zero.

From (10), whenever 0<rho<=2epsilon,

\[
 (\rho^2)'\le-4+4\epsilon M_1\le-2.                     \tag{20}
\]

In particular a surviving trajectory that enters rho<=epsilon
cannot subsequently leave it through rho=epsilon. Indeed the
derivative there is strictly negative; inside rho<=2epsilon it
is bounded above by -2. The same inward-barrier argument holds
at rho=2epsilon. This follows by the first upward-crossing
argument for the C^1 scalar function rho^2 and uses no endpoint
regularity. Consequently, if rho(t)>epsilon, every earlier
rho(u), 0<=u<=t, is >epsilon. In particular |r|>epsilon.

Suppose contrary to the asserted support property that points
p_n=(t_n,r_n,s_n) with eta_epsilon(p_n)!=0 tend to p=(t,r,s)
in Q outside D. Their whole earlier paths lie in the fixed compact
subset of U

\[
 K_\epsilon=\{\epsilon\le|q|\le R_*,\ |z|\le L_*\}.       \tag{21}
\]

Also |r|>=epsilon, so the limiting initial condition has a
positive maximal existence time tau_*. For every fixed
u<min(t,tau_*), smooth continuous dependence along the compact
limiting segment [0,u] and t_n>u for large n give
X(u,r_n,s_n)->X(u,r,s). Thus X(u,r,s) lies in K_epsilon.
If tau_*<=t, the limiting path stays in K_epsilon for its
entire maximal interval [0,tau_*). Compact continuation in U
then extends it past tau_*, a contradiction. Equivalently use
C466s's unique endpoint, which here belongs to K_epsilon and
is an interior nonzero point. It follows that tau_*>t, so
p belongs to D, also a contradiction.

Every point outside D therefore has a neighborhood on which
eta_epsilon vanishes. Within D it is smooth because |q| is
smooth for q!=0. Its extension is consequently smooth on Q.
The same argument makes the zero-extended forms eta_epsilon beta
and eta_epsilon gamma smooth on Q. No comparison flow after an
exit is introduced. Moreover eta_epsilon=0 whenever |r|<=epsilon,
even on surviving points, by the barrier just proved. Thus these
cutoffs also avoid the initial axis, with no missing separate
axis-boundary term.

### Collision-shell time and the full weak cutoff error

For fixed (r,s), r!=0, define the measurable time set

\[
 J_\epsilon(r,s)=\{0<t<\min(T_0,\tau(r,s)):
                          \epsilon<\rho(t)<2\epsilon\}.
\]

Once rho has entered rho<=2epsilon it cannot leave upward, and
within that region rho^2 strictly decreases at speed at least2.
It therefore passes through this shell at most once. For any two
times t_1<t_2 in J_epsilon, the path between them remains in the
shell, and integration of (20) gives

\[
 2(t_2-t_1)\le\rho(t_1)^2-\rho(t_2)^2\le3\epsilon^2.
\]

Taking the supremum over such times (or using measure<=diameter)
proves

\[
 |J_\epsilon(r,s)|\le\frac32\epsilon^2.                  \tag{22}
\]

This also holds if the initial point is inside the shell or the
time interval ends before leaving it. No differentiation of tau
or integration on a stopping hypersurface occurs.

On D, pullback and the chain rule give the complete identity

\[
 d\eta_\epsilon\wedge\beta
 =\frac{\theta'(\rho/\epsilon)}{\epsilon}\,
        \Psi^*(\chi\,d\rho\wedge\Omega).                 \tag{23}
\]

The ambient real covector d rho has Euclidean norm one. Equations
(17)–(18) therefore bound the absolute value of its dt wedge dr
wedge ds coefficient by

\[
 \frac{3C_0B_\theta E}{\epsilon}\,m(r)
             \mathbf1_{J_\epsilon(r,s)}(t).              \tag{24}
\]

This is a bound for the full differential in all three parameter
directions, including any initial-axis or stopping-preimage
variation. It is not merely a time-derivative estimate.
Tonelli's theorem applies to this nonnegative Borel bound.
Using (22), then integrating m(r), yields

\[
 \begin{split}
 \int_D |\phi\,d\eta_\epsilon\wedge\beta|
 &\le\frac92\|\phi\|_\infty C_0B_\theta E\epsilon
                                      \int_I m(r)\,dr\,ds,\\
 \int_I m(r)\,dr\,ds&=4ba^2+\frac43bM_1a^3.
 \end{split}                                             \tag{25}
\]

Here the absolute value in the first integral means the absolute
value of the oriented scalar coefficient against Lebesgue measure.
This proves (8), including a vanishing bound for tests meeting
r=0 or any collision preimage.

### Passing to the inhomogeneous distributional identity

Holomorphy of F on B implies dOmega=0: dF is a linear
combination of dq,dz, so dF wedge dq wedge dz=0. On D,
smooth pullback therefore gives d beta=gamma exactly.
Because the cutoff forms extend smoothly as established above,
on Q their ordinary derivatives satisfy

\[
 d(\eta_\epsilon\bar\beta)
 =\eta_\epsilon\bar\gamma+
                      \overline{d\eta_\epsilon\wedge\beta}. \tag{26}
\]

For every phi in C_c^infinity(Q), integration of
d(phi eta_epsilon bar(beta)) gives

\[
 -\int_Q d\phi\wedge\eta_\epsilon\bar\beta
 =\int_Q\phi\,\eta_\epsilon\bar\gamma
                  +\int_D\phi\,d\eta_\epsilon\wedge\beta. \tag{27}
\]

For each survivor, eta_epsilon tends to1 as epsilon decreases
to0. Elsewhere the zero extensions vanish. Bounds (7), finite
volume of Q and 0<=eta_epsilon<=1 justify coefficientwise L1
convergence of eta_epsilon bar(beta), eta_epsilon bar(gamma)
to bar(beta), bar(gamma). The last integral tends to zero by
(25). Passing to the limit in (27) proves

\[
 -\int_Q d\phi\wedge\bar\beta=\int_Q\phi\,\bar\gamma,
\]

which is precisely (5). In the stated orientation the coefficient
of d beta is partial_t beta_rs minus partial_r beta_ts plus
partial_s beta_tr; thus (27) has the claimed sign. Compact test
support removes only the external Q boundary. The interior
collision and initial-axis contributions were paid by (19)–(25),
not suppressed by that support convention. The gamma term remains
throughout. This completes the local identity under (1)–(3).

### Independent conceptual audit968 — 14 November 2026

This audit checks the complete proof, including the relative support
claim, with the unchanged hypotheses (1)–(3). It reuses assessment966,
separately approved967, and C466s's audited local machinery. No
load-bearing error or missing hypothesis was found. This establishes
the usability of the stated local input; it is reproduction of the
existing specialization, not a stronger theorem or a discovery claim.

**Endpoint and source hypotheses.** Direct differentiation gives
2 Re(bar(q) dot(q))=-4+2 Re(qH_q), so (10) has the correct
conjugation and inward singular term. Integrating rho'<=M_1 and
|dot z|<=M_1 before the first lifetime yields the fixed bounds
R_*,L_* strictly inside B. C466s's endpoint classification therefore
excludes outer hits, also simultaneous outer/collision events and
tau=T_0. For M_1=0 the same strict margins hold since a<R,b<L.
No bound on the full speed near q=0 is asserted. Every use of
Teschl's continuation/smooth-dependence results is inside U; no
extension of H beyond B or of the flow past its first exit is used.

**Complete exterior estimates.** For an autonomous smooth vector
field, d(v(X))/dt=Dv(X)v(X), so V, U_r and U_s really do share
one fundamental matrix on each compact survivor segment. For the
complex symmetric matrix B=D^2S, the real inner product satisfies

    (u, conjugate(Bw))_R = Re(u^T B w).

Thus A is real symmetric and conjugation causes no norm factor.
The singular q-block has eigenvalues +/-2/rho^2; the z-block has
two zero eigenvalues. Both the largest-two and largest-three sums
are 2/rho^2. On an orthonormal k-frame the regular perturbation
contributes at most kM_2. This verifies (13) for k=2,3, precisely
the two degrees needed for the complete forms. The cited WKM growth
inequality applies to continuous A on these compact intervals; its
separate uniform-contraction hypothesis is not needed or asserted.

The cross term in the weight is

    |f|^2 = 4/rho^2 - 4 Re(qg)/rho^2 + |g|^2 + |h|^2.

With x=1/rho and y=|g|, subtracting it from the exterior growth
bound gives kM_2-2x^2+4xy-y^2-|h|^2, which equals
kM_2+y^2-|h|^2-2(x-y)^2 and is at most kM_2+M_1^2.
This checks the cancellation in (14) before integration. F'=-|f|^2F
is an exact identity on U; all integrals multiplied in (15) are
finite on the same compact interval. No endpoint infinity is
subtracted from another infinity.

The initial U_r,U_s are real orthonormal, and any initial volume
involving V is bounded by ||V(0)||<=2/|r|+M_1. Multiplication by
|F(ir,s)| therefore gives r^2 for the spatial area and
m(r)=2|r|+M_1r^2 for every mixed area and the triple volume, with
the common exponential E. The straight initial segment lies in B,
so its H bound in (16) is legitimate for every allowed H.

The complex determinant is bounded by real two-area, including
degenerate complex determinants. On an orthonormal real triple,
alpha wedge dq wedge dz has three summands, each bounded by the
real operator norm of alpha. Applying this on the span of arbitrary
three real vectors proves (18); a dependent triple gives zero.
It is valid for complex dchi as well as real d rho. Consequently
all of beta_tr,beta_ts,beta_rs and gamma_trs satisfy (7).
There is no replacement of a mixed minor by a spatial minor.

**Support at a nonregular lifetime boundary.** For fixed epsilon
with 2epsilon M_1<=1, rho^2 has derivative <=-2 whenever
0<rho<=2epsilon. At either threshold epsilon or 2epsilon an
upward first crossing would contradict that strict derivative.
A current rho>epsilon therefore forces all earlier radii, including
the initial one, above epsilon. This proves the required no-return
property without assuming a continuous lifetime function.

For a convergent sequence p_n with eta_epsilon(p_n)!=0 and
limit p=(t,r,s) in Q, one has |r|>=epsilon. Each earlier path
lies in the same compact K_epsilon subset U. Let tau_* be the
limiting initial point's maximal lifetime. For each fixed
u<min(t,tau_*), eventually t_n>u and continuous dependence on
the limiting compact segment [0,u] puts X(u,r,s) in K_epsilon.
If tau_*<=t, this holds throughout its maximal interval and compact
continuation contradicts maximality. Hence tau_*>t. This also
excludes tau_*=t, which would otherwise be a missing boundary case.
It proves that the relative closure of the nonzero cutoff set lies
in D for varying terminal times, not merely on a fixed time slice.

Every point outside D now has a neighborhood where the extended
cutoff is identically zero. Inside D it is smooth. The same is true
of its products with beta and gamma, irrespective of derivative
growth near the excluded boundary. Also |r|<=epsilon implies
eta_epsilon=0 on every survivor, by the same no-return property.
The initial axis is therefore covered by this support argument;
neither a separately differentiated axis cutoff nor a smooth
stopping hypersurface has been assumed.

**Full weak flux and limit.** Once the path enters rho<=2epsilon
it cannot leave upward; there rho^2 strictly decreases. Any two
shell times enclose only shell times, and integration of its
derivative gives shell length <=(4epsilon^2-epsilon^2)/2.
This remains true for a path starting in the shell or a time
interval ending there. Since ||d rho||=1, the entire pulled-back
three-form in (23), rather than only its time component, is bounded
by 3C_0 B_theta E m(r)/epsilon on that shell. Integrating first in
time gives the factor 9epsilon/2. Direct integration in (r,s)
gives 4ba^2+(4/3)bM_1a^3, verifying (8) without a hidden
dependence on epsilon or on a regularity constant for tau.

These nonnegative Borel bounds justify Tonelli. Both cutoff forms
converge coefficientwise in L1 by (7), since Q has finite measure
and the cutoffs tend to one at every survivor. In particular the
inhomogeneous gamma term also has a valid dominating function.
Holomorphy makes dOmega=0, so d beta=gamma on D. The smooth
extensions justify integration by parts before the limit, and (8)
pays the error afterwards. For beta=beta_tr dt wedge dr +
beta_ts dt wedge ds + beta_rs dr wedge ds, its differential has
coefficient partial_t beta_rs-partial_r beta_ts+partial_s beta_tr.
This confirms both the orientation and the minus sign in (27).
Tests may meet r=0 or collision preimages; only the external
boundary of Q is removed by compact test support.

**Scope verdict.** C466s is the only direct local theorem input.
C466t remains a contrast: its stated M_1=L+sqrt113,T_0=2
already has M_1T_0>R-a=1 and thus fails (3). Its grazing defect
has not been refuted or suppressed. No new node or DAG edge is
needed. The current identity does not state a time-slice invariant
integral: gamma and external parameter-boundary terms have not been
removed. It also gives no sign to the full weighted Jacobian.
Unbounded-time restart, arbitrary initial surfaces, other metrics,
intersecting divisors, global homology, all-degree signs and actual-Xi
transfer remain outside this result. No RH candidate is asserted.

## Mathlib

Full matching coverage of this short-time zero-extended logarithmic
flow current has not been checked. Supporting ODE continuation,
exterior powers, differential forms and dominated convergence have
not been mapped to exact Mathlib declarations in this step. Unknown
coverage is not absence. This is an informal proof using the precise
sources above, with the scope of informal conceptual audit968 stated above;
no numerical certificate or machine-checked proof is claimed.
