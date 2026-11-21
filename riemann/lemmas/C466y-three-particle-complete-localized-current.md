# C466y — Complete localized three-particle current

## Hypotheses

Fix finite real 0<a<R, T_0>0, M_1,M_2>=0 and complex H_0.
Let H be holomorphic on B={z in C^3: |z_j|<R}, with

\[
 H(0)=H_0,\qquad \|\nabla H(z)\|_2\le M_1,\qquad
 \|D^2H(z)\|_{\rm op}\le M_2\quad(z\in B).                 \tag{1}
\]

These are holomorphic derivatives in the standard Hermitian norms.
No symmetry or separability is assumed. Define

\[
 \Delta(z)=\prod_{i<j}(z_j-z_i),\quad
 F=\Delta^2e^{-H},\quad U=B\setminus\{\Delta=0\},\quad
 S=-2\log\Delta+H.                                      \tag{2}
\]

Only logarithmic derivatives are used; these and F are single valued.
For pairwise distinct real u in I=(-a,a)^3, let X(t,u) be the
unit-flat raw flow

\[
 \dot X=v(X):=\overline{\nabla S(X)},\qquad X(0,u)=iu       \tag{3}
\]

on its first maximal interval [0,tau(u)) in U, with no restart.
Assume precisely the additional strict buffer

\[
 r_*:=\sqrt3\,a+M_1T_0<R.                                \tag{4}
\]

Put Q=(0,T_0) times I,
D={(t,u) in Q: Delta(u)!=0, t<tau(u)}, and Psi=X on D only.
For every complex or real chi in C_c^infinity(B), set

\[
 \omega=dz_1\wedge dz_2\wedge dz_3,\quad \Omega=F\omega,
 \quad\beta=\Psi^*(\chi\Omega),\quad
 \gamma=\Psi^*(d\chi\wedge\Omega).                        \tag{5}
\]

These are complex-valued real differential forms. Bars mean
coefficientwise zero extension from D to Q, including stopped
parameters and all initial diagonals. No derivative of a stopped map
is defined. The orientation is dt wedge du_1 wedge du_2 wedge du_3.

## Conclusion

There is no first outer exit at any time <=T_0, including a limiting
event simultaneous with collision. Every coefficient of bar(beta)
and bar(gamma) belongs to L^infinity(Q), hence L1_loc(Q), and

\[
                  d\bar\beta=\bar\gamma
                     \quad\hbox{in distributions on }Q. \tag{6}
\]

The proof supplies smooth survivor cutoffs whose full weak error is
O(epsilon^(1/4)), with the explicit constant in (24) below. Triple
collisions, arbitrary relative spacings, and tests meeting intersections
of initial diagonals are included. No endpoint uniqueness, regular
lifetime, collision trace, independent pair coordinates or continuation
through a divisor is assumed.

This is the local result of attempt981 under the invocation-start
EXPLORE assessment980. Independent conceptual audit983 below validates
the full statement, including the constant in (24).
It is local progress using imported tools and a singular-flow
specialization, not certified originality or an RH candidate. It
does not sign a determinant, prove global signed assembly, realize
the actual H, or establish actual-Xi all-degree positivity.

## Proof

### Inputs and the required specialization

C466x supplies the smooth survivor-domain setting, real variational
matrix, complex determinant/real three-volume comparison, and the
following identities on U. Write h=grad H, f_0=-2 grad log Delta,
f=f_0+h, and P=sum_(i<j)|z_i-z_j|^(-2). Then

\[
 \|f_0\|^2\ge8P,\qquad
 A\xi=Dv\,\xi=\overline{(D^2S)\xi},\qquad
 \frac{d}{dt}F(X)=-\|f(X)\|^2F(X).                       \tag{7}
\]

Here A is real symmetric in R^6. Its pair summand for (i,j) has
real spectrum {4/|z_i-z_j|^2,-4/|z_i-z_j|^2,0,0,0,0}, and
the background summand has operator norm at most M_2. C466x proves
these collectively, including the triangle-area identity behind the
first inequality. They are used without repeating their proofs.

The local-flow and compact-continuation tools are the standard smooth
ODE theorems; see Gerald Teschl, *Ordinary Differential Equations and
Dynamical Systems*, author-hosted April2012 preliminary version,
[Lemma2.14/Corollary2.15, p52; Theorem6.1 and proof, pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
They apply to the smooth real field on the open set U. In particular
the maximal-flow domain is open, and a solution staying in a compact
subset of U cannot have a finite maximal endpoint. We apply the latter
only after exhibiting such a compact set, never across Delta=0.

For real-parameter variation see Tanizaki, Nishimura and Verbaarschot,
*Gradient flows without blow-up for Lefschetz thimbles*,
JHEP10(2017)100,
[arXiv:1706.03822v2](https://arxiv.org/pdf/1706.03822v2),
27 September2017, AppendixB (B.1)–(B.5), printed p22.
The convention is dot J=conjugate((D^2S)J), conjugating both factors.

Wu, Kanevskiy and Margaliot, *k-Contraction: Theory and Applications*,
[arXiv:2008.10321v2](https://arxiv.org/pdf/2008.10321v2),
27 September2021, Section3.1 (29), Theorem4/Proposition5 and proofs,
printed pp8–9, supplies for a continuous real A and its fundamental
matrix Phi the growth bound

\[
 \|\Lambda^k\Phi(t)\|\le
       \exp\!\int_0^t\mu_2(A(s)^{[k]})\,ds.              \tag{8}
\]

For symmetric A, the matrix measure is the sum of its k largest
eigenvalues. This growth inequality does not require the negative
uniform measure used for the source's contraction conclusion. We
use k=3,4 in dimension six, on compact surviving intervals where
all coefficients are continuous and bounded. No endpoint theorem
is imported and no reproof of (8) is needed.

Assessment980 covers these tools in these degrees. The additions
below are the exact buffer argument, full velocity/parameter minors,
fractional weighted damping and a cutoff using |F|. C466u is a
one-divisor method comparison, not a theorem premise for this
coupled geometry. Its pair-shell residence estimate is not used.
C466t is the contrasting earlier-outer-grazing obstruction; the
new proof must exclude such events rather than discard their shadows.

### The strict buffer excludes every outer event

The singular part of the real velocity is

\[
 (\overline{f_0})_j=-2\sum_{k\ne j}
                       \frac{z_j-z_k}{|z_j-z_k|^2}.
\]

For one pair its contribution to
Re sum_j conjugate(z_j)(overline(f_0))_j is exactly -2.
There are three pairs. Thus, on every surviving segment,

\[
 \frac d{dt}\|X\|^2
  =-12+2\Re\sum_j\overline{X_j}\,\overline{h_j(X)}.
                                                               \tag{9}
\]

Since a distinct triple is not the zero vector, rho=||X||>0 on U.
Cauchy-Schwarz gives rho'<=-6/rho+M_1<=M_1, whence

\[
 \|X(t,u)\|\le\|u\|+M_1t\le r_*<R
       \quad(0\le t\le T_0,\ t<\tau(u)).                 \tag{10}
\]

Consequently every surviving image stays in the closed Euclidean
ball of radius r_*, a compact subset of B. No sequence tending to
a first lifetime <=T_0 can approach any |z_j|=R; this excludes outer
and simultaneous outer/collision events without requiring a unique
endpoint. If a finite lifetime <=T_0 occurs, compact continuation
also implies the path cannot stay separated from {Delta=0}.
These conclusions include M_1=0 and tau=T_0. M_1 has only bounded
the background force; the singular force was retained in (9).

### Complete weighted three- and four-volumes

Let J_j=partial_(u_j)X and V=v(X), all regarded as real vectors in
R^6. Parameter differentiation and autonomy give

\[
 \dot J_j=A J_j,\qquad \dot V=A V,\qquad
 J_j(0)=ie_j,\quad V(0)=v(iu).                            \tag{11}
\]

The last equation follows by differentiating v(X(t)); it does not
assume a time-dependent initial manifold or any stopped derivative.
For either k=3 or k=4, the trace of a pair summand of A on an
orthonormal real k-frame is at most 4/|z_i-z_j|^2: the total squared
projection on its one positive eigendirection is at most one, and
its negative contribution can only decrease the trace. On the same
frame the background trace is at most kM_2. Maximizing the sum on
that frame, using (7), proves

\[
 \mu_k:=\mu_2(A^{[k]})\le4P+kM_2
                         \le\tfrac12\|f_0\|^2+kM_2.
                                                               \tag{12}
\]

No pair matrices need commute. Completing the square yields

\[
 \mu_k-\|f\|^2
 \le kM_2+\tfrac12\|f_0\|^2-\|f_0+h\|^2
 =kM_2+\|h\|^2-\tfrac12\|f_0+2h\|^2
 \le kM_2+M_1^2.                                        \tag{13}
\]

Let W_k(t) be the real exterior norm of any k vectors transported
by (11). Multiplying (8) by the absolute-value form of (7), on a
compact surviving interval, gives

\[
 w(t)W_k(t)\le w_0e^{(kM_2+M_1^2)t}W_k(0),\quad
 w(t)=|F(X(t,u))|>0,\quad w_0=|F(iu)|.                   \tag{14}
\]

All integrals here are finite before the first lifetime. Define

\[
 E_0=e^{-\Re H_0+\sqrt3aM_1},\qquad
 E=E_0e^{(4M_2+M_1^2)T_0},\qquad p(u)=|\Delta(u)|^2.
\]

The straight segment from 0 to iu lies in B, so
w_0<=E_0 p(u). Writing d_ij=u_i-u_j, we have

\[
 \|V(0)\|\le b(u):=2\sqrt2\sum_{i<j}|d_{ij}|^{-1}+M_1.
                                                               \tag{15}
\]

Indeed each pair term of f_0 is -2(e_i-e_j)/(z_i-z_j), of norm
2sqrt2/|z_i-z_j|. Define m(u)=p(u)b(u) off the initial diagonals
and set it equal to zero on them. This is a bounded continuous
function: its pair terms are
2sqrt2 |d_ij| product_(other pairs)|d|^2. In particular

\[
 m(u)\le6\sqrt2(2a)^5+M_1(2a)^6.                        \tag{16}
\]

The three J_j have initial three-volume one. Each initial wedge
V wedge J_i wedge J_j, and V wedge J_1 wedge J_2 wedge J_3,
has norm at most ||V(0)||. Thus (14) controls every needed
minor, including those containing the velocity column.

C466x's comparison gives |omega(w_1,w_2,w_3)|<=||w_1 wedge
w_2 wedge w_3|| for real vectors. For a complex-valued real
covector alpha, expansion on an orthonormal real four-frame has
four terms, each of modulus at most ||alpha||. Passing to an
orthonormal basis of the span, with the dependent case zero, gives

\[
 |(\alpha\wedge\omega)(w_1,w_2,w_3,w_4)|
 \le4\|\alpha\|\,\|w_1\wedge w_2\wedge w_3\wedge w_4\|.
                                                               \tag{17}
\]

Let C_0=||chi||_infinity and C_1=sup_B||dchi|| in this real
covector norm. On D and after zero extension, (14)–(17) prove

\[
 |\bar\beta_{123}|\le C_0E p(u),\qquad
 |\bar\beta_{tij}|\le C_0E m(u)\quad(i<j),\qquad
 |\bar\gamma_{t123}|\le4C_1E m(u).                       \tag{18}
\]

Smooth dependence makes D open and the coefficients smooth on D;
their zero extensions are Borel. Bounds (16),(18) establish
L^infinity(Q) for all four coefficients of beta and the full gamma.

### Fractional damping for the full cutoff error

It is useful not to discard all singular damping in (13).
The exact elementary inequality

\[
 \tfrac34\|f\|^2+\tfrac32\|h\|^2
          -\tfrac12\|f-h\|^2=\tfrac14\|f+2h\|^2\ge0
\]

and (12) instead give
mu_k-||f||^2<=kM_2+3M_1^2/2-||f||^2/4. Since
w(t)=w_0 exp(-integral_0^t||f||^2 ds), the same application of
(8), now retaining this last term, proves

\[
 w(t)W_k(t)\le e^{(kM_2+3M_1^2/2)t}
                         w_0^{3/4}w(t)^{1/4}W_k(0).
                                                               \tag{19}
\]

No fractional power of the complex F is taken: w and w_0 are
strictly positive real numbers on the surviving interval. Put
Lambda=4M_2+3M_1^2/2, and set
A(u)=w_0^(3/4)||V(0)|| for distinct u, zero on the diagonals.
Equation (15) and the bound for w_0 show

\[
 \begin{split}
 A(u)&\le E_0^{3/4}
       \{6\sqrt2(2a)^{7/2}+M_1(2a)^{9/2}\},\\
 \int_I A(u)\,du&\le G:=(2a)^3E_0^{3/4}
       \{6\sqrt2(2a)^{7/2}+M_1(2a)^{9/2}\}<\infty.
 \end{split}                                                   \tag{20}
\]

For each pair the relevant factor is
|Delta(u)|^(3/2)/|d_ij|=|d_ij|^(1/2)
product_(other pairs)|d|^(3/2), bounded by (2a)^(7/2).
This verifies (20) uniformly even near simultaneous coincidences.

### A cutoff supported inside the actual survivor domain

Choose smooth theta:R->[0,1], zero on (-infinity,1] and one on
[2,infinity), and let B_theta=||theta'||_infinity. For epsilon>0
put eta_epsilon=theta(w/epsilon) on D and zero elsewhere in Q.
We prove that the closure of its nonzero set, relative to Q, is
contained in D. This cannot follow merely from its smoothness on D.

Along each survivor w'=-||f||^2w<=0. If eta_epsilon(t,u)!=0,
then w(t)>epsilon and every earlier surviving w(s)>=w(t)>epsilon.
By (10) the whole earlier path therefore lies in

\[
 K_\epsilon=\{z:\|z\|\le r_*,\ |F(z)|\ge\epsilon\}.
                                                               \tag{21}
\]

This is a compact subset of U: the closed ball lies strictly
inside B, F is continuous there, and its only zeros are Delta=0.
No boundary value of H outside B is used.

Suppose p_n=(t_n,u_n) with nonzero eta_epsilon converges to
p=(t,u) in Q. Every earlier path lies in K_epsilon. In particular
|F(iu_n)|>=epsilon, hence |F(iu)|>=epsilon and Delta(u)!=0.
Let tau_* be the first maximal lifetime for this limiting initial
point. For every s<min(t,tau_*), smooth dependence on the compact
limiting interval [0,s] gives X(s,u_n)->X(s,u) for all sufficiently
large n (also s<t_n). Thus X(s,u) belongs to K_epsilon. If
tau_*<=t, the whole limiting path stays in this fixed compact
subset of U up to its finite maximal endpoint, contradicting
compact continuation. Consequently tau_*>t and p belongs to D.

This proves the support assertion without assuming continuity of
tau or existence of a unique collision endpoint. Each point of
Q outside D has a neighborhood where the cutoff vanishes. Inside
D, |F| and the flow are smooth. Thus eta_epsilon and the forms
eta_epsilon bar(beta), eta_epsilon bar(gamma) are smooth on Q.
The same proof excludes every initial diagonal and their intersection
from the cutoff support. No independent initial-diagonal cutoff or
post-stop comparison flow is being introduced.

### Monotone-weight shell and the complete weak flux

For fixed distinct u let
J_epsilon(u)={0<t<min(T_0,tau(u)): epsilon<w(t)<2epsilon}.
Because w is nonincreasing this set is an interval, possibly empty
or truncated by the initial/final time; constant portions cause no
difficulty. For any t_1<t_2 in this set, integration of (7) gives
integral_(t_1)^(t_2)||f||^2 dt=log(w(t_1)/w(t_2))<=log2.
Exhausting the interval and using nonnegativity gives

\[
 \int_{J_\epsilon(u)}\|f\|^2dt\le\log2,\qquad
 \int_{J_\epsilon(u)}\|f\|dt\le\sqrt{T_0\log2}.           \tag{22}
\]

The second inequality is Cauchy-Schwarz and |J_epsilon|<=T_0.
Flat portions with f=0 contribute zero; no lower speed or pairwise
shell-residence estimate is needed. Endpoint truncation, including
a collision before T_0, is covered by the same exhaustion.

On U regard w(z)=|F(z)| as an ambient smooth real function. Since
dF=-F sum_j f_j dz_j, its differential is
dw=-w Re(sum_j f_j dz_j), of real covector norm w||f||.
The full chain and wedge rules on D therefore give

\[
 d\eta_\epsilon\wedge\beta
  =\frac{\theta'(w/\epsilon)}{\epsilon}
                   \Psi^*(\chi\,dw\wedge\Omega).         \tag{23}
\]

This includes all parameter derivatives, not just partial_t eta.
Applying (17) to V,J_1,J_2,J_3, and (19) with k=4, bounds
the absolute value of its oriented coefficient on the shell by
8 C_0 B_theta e^(Lambda T_0) A(u)(2epsilon)^(1/4)||f||.
Here the factor eight is four from (17) times w/epsilon<=2.
Off the shell theta' vanishes. For every scalar
phi in C_c^infinity(Q), Tonelli, (20) and (22) now yield

\[
 \begin{split}
 \int_D |\phi\,d\eta_\epsilon\wedge\beta|
 &\le 8\,2^{1/4}\|\phi\|_\infty C_0 B_\theta
       e^{\Lambda T_0}\sqrt{T_0\log2}\,G\,\epsilon^{1/4}
   \longrightarrow0.                                    \tag{24}
 \end{split}
\]

Absolute value here means the modulus of the coefficient relative
to dt du_1 du_2 du_3. The nonnegative bounds are Borel, so these
integrations are legitimate. Equations (21)–(24) pay the full
collision and initial-diagonal cutoff flux, including all intersections.

### Distributional passage and its limits

Holomorphy implies dOmega=0 on B: dF is a linear combination of
dz_1,dz_2,dz_3. Smooth pullback gives d beta=gamma on D. The
support result proves on all of Q that

\[
 d(\eta_\epsilon\bar\beta)
  =\eta_\epsilon\bar\gamma+
                       \overline{d\eta_\epsilon\wedge\beta}.
                                                               \tag{25}
\]

For each point in D, w>0, so eta_epsilon->1 as epsilon decreases
to zero. On Q minus D the extended coefficients vanish. Bounds
(18) and 0<=eta_epsilon<=1 give coefficientwise L1 convergence
of both cutoff forms to their zero extensions, by dominated
convergence (indeed globally on the finite-measure Q).

Integrate d(phi eta_epsilon bar(beta)) over Q; it is an exact
compactly supported four-form, so its integral is zero. Equation
(25) gives
-integral_Q dphi wedge eta_epsilon bar(beta)
=integral_Q phi eta_epsilon bar(gamma)
+integral_D phi d eta_epsilon wedge beta.
Pass to the limit using the L1 convergence and (24). This yields

\[
 -\int_Q d\phi\wedge\bar\beta
       =\int_Q\phi\,\bar\gamma,                          \tag{26}
\]

the distributional identity (6) in the stated orientation.

All estimates were made before the first lifetime, with limits
only of coefficientwise extended forms. No zero times infinite
endpoint determinant, assumed boundary trace, independent pair
flow or discarded gamma term occurs. The buffer is essential to
the compact support argument; the earlier-grazing stop in C466t
is not contradicted. Neither (6) nor any modulus estimate supplies
a phase/sign, global contour equality or actual-Xi specialization.

### Independent conceptual audit — 14 November 2026, step983

This audit uses the invocation-start SPECIALIZE assessment981,
separately approved982. The source versions and hypotheses cited above
are reused: Teschl applies inside the smooth open domain U, TNV
conjugates both factors in the real variational equation, and WKM
covers k=3,4 in real dimension six without a negative-measure premise.
C466x's audited force estimate, pair spectra, weight identity and
determinant comparison are the only local theorem input. C466u/t
are comparisons. No endpoint-removability theorem is imported.

**Buffer.** Each pair contributes
-2 Re((conjugate(z_i)-conjugate(z_j))(z_i-z_j))/|z_i-z_j|^2
=-2 to the radial pairing. Three pairs and the factor two from
differentiating the squared norm give exactly -12. A point of U has
nonzero Euclidean norm, so division by rho and integration of
rho'<=M_1 are legitimate before the first lifetime. The resulting
closed ball of radius r_* is compact inside B. This excludes any
outer-approaching sequence, even without a unique collision endpoint
and when tau=T_0. M_1=0 is included; no full-speed bound is used.

**Every complete coefficient.** Autonomy gives dot V=A V, so the
continuous real fundamental matrix transports both V and the J's.
On one orthonormal k-frame each pair's positive eigendirection has
squared projection sum at most one. Adding the background trace and
then maximizing proves (12) for both degrees without commuting
matrices. Completing the Hermitian square verifies exactly (13).
The four three-form coefficients use J_1,J_2,J_3 or V,J_i,J_j;
their initial wedge norms are at most 1 or ||V(0)||. The sole
four-form coefficient uses V,J_1,J_2,J_3, also with initial norm
at most ||V(0)||. Real Gram-Schmidt and C466x's comparison bound
every three-form evaluation; expansion on a real orthonormal
four-frame gives the four terms in (17). This holds for complex
dchi in its real-linear covector norm and for dependent columns.
Thus (18) includes all time coefficients with no extra norm factor.
The powers five and six in (16) account for every initial simple
pole; the zero-extended coefficients are bounded and Borel.

**Fractional damping and intersections.** Expansion verifies
(3/4)||f||^2+(3/2)||h||^2-(1/2)||f-h||^2
=(1/4)||f+2h||^2. Hence the weighted exponent retains
-(1/4) integral ||f||^2. Its exponential is (w/w_0)^(1/4),
proving precisely (19), without fractional powers of complex F.
Every initial velocity pole multiplied by |Delta(u)|^(3/2)
leaves exponent 1/2 on that difference and 3/2 on the other
two. The three pair terms therefore have coefficient 6sqrt2 and
degree 7/2; the background term has degree 9/2. This proves the
uniform A(u) bound and finite G in (20), at all initial intersections
and for arbitrary spacing ratios.

**Support at an irregular lifetime.** Nonzero eta_epsilon at
(t_n,u_n) puts the entire earlier path in the same K_epsilon,
because the full weight is monotone. For a limit (t,u) in Q,
continuity of F at iu first excludes an initial coincidence.
Smooth dependence is used only on [0,s] for arbitrary
s<min(t,tau_*), where the limiting trajectory already exists.
It puts every such X(s,u) in K_epsilon. If tau_*<=t, the whole
limiting interval [0,tau_*) lies in this compact subset of U,
contradicting compact continuation, including when tau_*=t.
Thus t<tau_*. The closure assertion follows and every point outside
D has a neighborhood of zero cutoff. This proves smooth extension
of both cutoff forms without lifetime continuity, boundary traces,
post-stop comparison flows or independent initial-diagonal cutoffs.

**Full flux and its constant.** Writing f_j=a_j+ib_j shows that
Re(sum f_j dz_j) has real coefficients a_j,-b_j and norm ||f||.
Thus ||dw||=w||f|| exactly. Equation (23) is the full pullback
chain rule, including parameter derivatives. Equations (17),(19)
bound its coefficient by
4 C_0 B_theta (w/epsilon)||f|| exp(Lambda T_0) A(u)w^(1/4).
On the shell, w/epsilon<=2 and w^(1/4)<=(2epsilon)^(1/4),
giving precisely the factor eight in the text. The shell is an
interval because w is continuous and monotone. Integrating between
interior times gives energy at most log2. Exhaustion by nested
subintervals proves the bound also for truncated or open-ended
shells; flat portions have f=0. Cauchy-Schwarz gives the stated
sqrt(T_0 log2) bound. Tonelli and (20) now reproduce exactly
the constant 8 times 2^(1/4) and O(epsilon^(1/4)) error in
(24). No parameter derivative, weight or intersection is omitted.

**Distributional limit and verdict.** Holomorphy gives dOmega=0;
the support assertion makes (25) smooth on all Q. Bounds (18)
dominate the cutoff forms on finite-measure Q, proving coefficientwise
L1 convergence. The product rule for d(phi eta beta) gives the
minus sign in (26) after integration of the compactly supported
exact form. The full four-form error tends to zero by (24).
Scalar tests suffice for the top-degree distribution on this
four-dimensional parameter domain. This verifies exactly (6).

The full statement passes without a proof correction. No time-zero
trace or boundary flux at the edges of I is asserted: Q is open
and tests are compactly supported there. The strict buffer is
essential to this proof; C466t's earlier-grazing stop is preserved.
This validates a previously unaudited local input, classified as
reproduction/specialization, not a discovery beyond the sources
checked. Determinant phase, actual-H realization, global signed
assembly and actual-Xi all-degree signs remain unpaid. No numerical
script, formal verification or RH candidate is claimed.

## Mathlib

Full matching coverage has not been checked. The retained primary
source assessment concerns smooth ODE/compound tools, not a Mathlib
theorem for this stopped intersecting-divisor current. Smooth-flow
continuation, exterior-algebra norm estimates, dominated convergence
and distributional exterior differentiation are supporting standard
inputs; exact Mathlib names for their required forms have not been
checked. Unknown availability is not evidence of absence. No formal
verification or numerical certificate is claimed.
