# C466s — Coupled stopped weighted density from real two-volume

## Hypotheses

Fix real 0<a<R<infinity, 0<b<L<infinity, finite nonnegative M_1,M_2,
and a complex value H_0. Let H be holomorphic on the bidisk
B={|q|<R, |z|<L}, with H(0,0)=H_0 and, throughout B,
\[
 \|\nabla H\|_2\le M_1,\qquad \|D^2H\|_{\mathrm{op}}\le M_2.
                                                               \tag{1}
\]
These are holomorphic derivatives with the standard Hermitian norms;
the Hessian is the complex symmetric matrix of second derivatives.
On U=B minus {q=0}, use the unit flat raw conjugated-gradient flow
\[
 S=-2\log q+H(q,z),\quad f=\nabla S=(-2/q+H_q,H_z),\quad
 \dot X=\overline f(X),\quad X=(q,z),\quad X(0,r,s)=(ir,s),       \tag{2}
\]
where (r,s) belongs to I=(-a,a) times (-b,b) and r!=0. A local
logarithm suffices: f, D^2S and F=q^2 exp(-H)=exp(-S) are single
valued on U. Let [0,tau(r,s)) be the maximal forward interval in U.

At a surviving time T<tau, let J_T be the complex 2 by 2 matrix
whose columns are partial_r X and partial_s X, both taken at fixed
physical time T. Thus J_0=diag(i,1). Define
\[
 W_T(r,s)=-F(X(T,r,s))\det_{\mathbb C}J_T/i \quad(T<\tau(r,s)),  \tag{3}
\]
and set W_T=0 when T>=tau or r=0. The latter is a definition of a
stopped density, not a classical derivative of a stopped flow.

## Conclusion

For every finite T_0>=0 put
\[
 K=2M_2+M_1^2,\qquad
 C(T_0)=\exp\{KT_0-\Re H_0+M_1\sqrt{a^2+b^2}\}.
                                                               \tag{4}
\]
The density is jointly Borel measurable in (T,r,s), and
\[
 |W_T(r,s)|\le C(T_0)r^2 \quad(0\le T\le T_0,\ (r,s)\in I).
                                                               \tag{5}
\]
Consequently, for every Lebesgue measurable E subset I,
\[
 \sup_{H,\ 0\le T\le T_0}\int_E |W_T|\,dr\,ds
 \le C(T_0)\int_E r^2\,dr\,ds
 \le C(T_0)a^2|E|.                                            \tag{6}
\]
The supremum is over the entire class sharing the displayed data.
Thus omega(u)=C(T_0)a^2 u is a finite measurable-set modulus tending
to zero as u decreases to zero; any finite positive T_0, for example
T_0=1, meets the requested existence claim. Total absolute mass is
at most 4C(T_0)ba^3/3. There is no claim uniform in unbounded time.

Every finite maximal lifetime has a unique limiting endpoint in the
closed bidisk, with q=0 or |q|=R or |z|=L, allowing simultaneous
events. The definition (3) includes every such stopping boundary
without requiring a trace or boundary value of J.

This establishes the local absolute-mass target under its full
coupled hypotheses. It does not give a sign, conserved signed
integral, vanishing endpoint cost, global contour, metric change,
intersecting-divisor estimate, all-degree positivity or Xi realization.
This is a specialization beyond the exact passages inspected, with
originality unestablished. Independent conceptual audit959 below
validates the stated local result without strengthening it.

## Proof

### Imported machinery and scope

Tanizaki, Nishimura and Verbaarschot, *Gradient flows without blow-up
for Lefschetz thimbles*, JHEP10(2017)100,
[arXiv:1706.03822v2](https://arxiv.org/pdf/1706.03822v2), 27 September
2017, Appendix B, (B.1)–(B.5), printed p22, supplies the
real-parameter variational law
\[
 \dot J=\overline{(D^2S)J}.                                  \tag{7}
\]
Both the Hessian and J are conjugated; no holomorphic dependence on
the real parameters is asserted. The source derivation applies to
our initial tangent matrix diag(i,1) on each nonsingular surviving
interval. A global choice of log q is unnecessary for (7).

Wu, Kanevskiy and Margaliot, *k-Contraction: Theory and Applications*,
[arXiv:2008.10321v2](https://arxiv.org/pdf/2008.10321v2), 27 September
2021, Sections 2.2, 2.4–2.5, printed pp5–7, and Section 3.1,
Theorem 4 and Proposition 5 with their proofs, printed pp8–9,
give the following compound-matrix growth bound. If A(t) is a
continuous real matrix on a compact interval and Phi solves
dot Phi=A Phi, Phi(0)=Id, then in the Euclidean exterior norm
\[
 \|\Phi(t)^{(2)}\|\le
 \exp\!\int_0^t\mu_2(A(v)^{[2]})\,dv.                       \tag{8}
\]
Here (2) is the multiplicative compound acting on two-vectors and
[2] is the additive compound. The Euclidean matrix measure is the
sum of the two largest eigenvalues of (A+A^T)/2. This is the growth
inequality in the cited proof, without imposing the uniform negative
matrix-measure assumption of the contraction conclusion. It applies
to rectangular tangent two-area by acting on the initial two-vector.

These imported results are used only on compact surviving intervals,
where A is continuous. Their singular weighted specialization,
comparison with the complex determinant, and stopped extension are
proved below. C466r and C466q are scalar comparison results, not
premises. The cited sources do not assert (5)–(6) for this H class.

### Maximal lifetimes and the measurable extension

The vector field is smooth on the open subset U of real four-space.
The Picard–Lindelof theorem, maximal-continuation theorem, and smooth
dependence theorem for smooth ordinary differential equations give
unique maximal solutions and a smooth flow on its open domain in
time and initial position. Each trajectory segment [0,T] with
T<tau is a compact subset of U. Smooth dependence therefore supplies
J_T in a neighborhood of its initial parameters at fixed T, with
(7) and the stated initialization. No common survival time for all
initial parameters or all H is required.

For the endpoint assertion write rho=|q|. Along any trajectory,
\[
 \frac{d}{dt}\rho^2=-4+2\Re(qH_q),\quad
 |(\rho^2)'|\le4+2RM_1,\quad |\dot z|\le M_1.                \tag{9}
\]
If tau<infinity, rho^2 therefore has a limit ell^2 in [0,R^2], and
z has a limit z_* in the closed disk of radius L. When ell=0,
q tends to zero. When ell>0, eventually rho>=ell/2 and
|dot q|<=4/ell+M_1, so q is Cauchy as t increases to tau and has a
unique limit q_* of modulus ell. Thus X has a unique endpoint in
all cases. If 0<ell<R and |z_*|<L, the endpoint is in U. The
integral equation and continuity of the vector field extend the
solution to tau, and local existence there extends it past tau,
contradicting maximality. Hence q_*=0, |q_*|=R or |z_*|=L.
The argument permits both boundary moduli simultaneously, or q_*=0
and |z_*|=L. No value of H outside B, or on its boundary, was used.
Since the trajectory remains in U for every t<tau, these are first
limiting zero/escape events. Infinite lifetimes need no endpoint.

For fixed H the survivor domain
\[
 \mathcal D_H=\{(T,r,s):T\ge0,\ (r,s)\in I,\ r\ne0,
                              \ T<\tau(r,s)\}
\]
is relatively open in [0,infinity) times I: it is the pullback of
the open maximal flow domain along the smooth initial surface, with
r=0 removed. Formula (3) is continuous on this relative-open domain,
including relative continuity at T=0. Its zero extension is Borel:
for any open subset O of C, the inverse image inside D_H is relatively
open there, and the full inverse image additionally contains the
Borel complement of D_H exactly when 0 belongs to O. This proves
joint measurability without continuity of tau, a regular survivor
boundary, or matching boundary traces. Each time slice is Borel.

### The full complex determinant versus real two-area

For two vectors u,v in C^2, identify them with vectors of R^4 and set
\[
 V(u,v)^2=\|u\|^2\|v\|^2-(\Re\langle u,v\rangle)^2.
\]
This is their squared Euclidean real two-area. The complex Gram
determinant identity gives
\[
 |\det_{\mathbb C}[u\ v]|^2
 =\|u\|^2\|v\|^2-|\langle u,v\rangle|^2
 =V(u,v)^2-(\Im\langle u,v\rangle)^2\le V(u,v)^2.             \tag{10}
\]
Apply this to the two columns of J_t and write V(t) for their real
two-area. Initially the columns (i,0) and (0,1) are orthonormal over
R, so V(0)=1. Inequality (10) requires neither a nonzero complex
determinant nor a Lagrangian tangent plane. In particular it controls
the full determinant, including the mixed variations in both columns.

### Singular real-volume growth and its weighted cancellation

Fix an initial (r,s) with r!=0 and any T<tau. On [0,T] the real
variational matrix is
\[
 A(t)v=\overline{(D^2S(X(t)))v}=A_0(t)v+A_H(t)v,
 \quad D^2S=\operatorname{diag}(2/q^2,0)+D^2H.               \tag{11}
\]
The real inner product of u with A v is Re(u^T(D^2S)v), symmetric
in u,v because the complex Hessian is symmetric. Thus A, A_0 and
A_H are real symmetric. Moreover ||A_H||_op<=M_2, since conjugation
is an isometry and (1) bounds the complex Hessian operator norm.

On the q-plane the map v maps to overline((2/q^2)v) has real
eigenvalues 2/rho^2 and -2/rho^2; on the z-plane A_0 is zero.
For example, the real matrix of v maps to overline(cv) is
[[Re c,-Im c],[-Im c,-Re c]], whose eigenvalues are +/-|c|.
Consequently the two largest eigenvalues of A_0 sum to 2/rho^2.
Adding A_H increases their sum by at most 2M_2. Explicitly, for
any orthonormal real pair e_1,e_2, the trace of A_H on their span
is at most 2M_2; the trace of A_0 is at most 2/rho^2, since its
positive eigenvector contributes at most that number and its only
other nonzero eigenvalue is negative. Maximizing this trace over
orthonormal pairs gives the two largest eigenvalues of A by the
spectral theorem. Hence
\[
 \mu_2(A(t)^{[2]})\le 2/\rho(t)^2+2M_2.                     \tag{12}
\]
The compound estimate (8) applies to the real tangent columns of J
on [0,T]; their initial two-vector has norm one. It gives
\[
 V(T)\le \exp\!\int_0^T\mu_2(A(t)^{[2]})\,dt.               \tag{13}
\]

The analytic, nonzero function F on U satisfies partial_j F=-F f_j.
Along the raw flow (2) this yields the exact identity
\[
 \dot F=-\|f\|_2^2F,\qquad
 |F(X(T))|=|F(X(0))|\exp\!\left(-\int_0^T\|f\|_2^2dt\right).
                                                               \tag{14}
\]
Every integral here is finite on the compact surviving interval.
Put g=H_q(X(t)) and h=H_z(X(t)). Combining (12) with
|f|^2=4/rho^2-4 Re(qg)/rho^2+|g|^2+|h|^2 gives
\[
 \begin{aligned}
 \mu_2(A^{[2]})-\|f\|_2^2
 &\le 2M_2-2/\rho^2+4\Re(qg)/\rho^2-|g|^2-|h|^2\\
 &\le 2M_2-2/\rho^2+4|g|/\rho-|g|^2-|h|^2\\
 &=2M_2+|g|^2-|h|^2-2(1/\rho-|g|)^2\\
 &\le 2M_2+M_1^2=K.                                        \tag{15}
 \end{aligned}
\]
There is no lower bound on rho in K. The singular growth and weight
are combined before applying a uniform estimate; separate bounds
on individual tangent lengths are not substituted for (13).

Using (10), (13), (14), and then (15), we obtain for each survivor
\[
 |W_T|\le |F(X(T))|V(T)
 \le |F(X(0))|\exp\!\int_0^T
              (\mu_2(A^{[2]})-\|f\|_2^2)dt
 \le r^2e^{-\Re H(ir,s)}e^{KT}.                             \tag{16}
\]
Each T<tau has been treated directly, with constants independent of
the distance of its trajectory to the divisor and boundary. No
singular-cutoff limit, determinant division, or interchange of
improper integrals is needed. No independent scalar flows were used.

### Common initial bound and measurable-set quantifiers

The straight segment t maps to (tir,ts), 0<=t<=1, lies in B. The
fundamental theorem of calculus and complex Cauchy–Schwarz give
\[
 |H(ir,s)-H_0|
 \le\int_0^1\|\nabla H(tir,ts)\|_2\sqrt{r^2+s^2}\,dt
 \le M_1\sqrt{a^2+b^2}.                                    \tag{17}
\]
Thus (16) implies (5) on survivors for all T<=T_0. At stopped
points and r=0, (5) follows from the stipulated zero value. There is
no multiplication of an infinite boundary Jacobian by a zero weight.

Integrating the common envelope over E proves (6) for each H,T,
so also for their supremum. This is a supremum of bounded numbers;
no measurability of the indexing class or exchange of supremum and
integration is used. The bound also holds separately for any family
of measurable sets E_{H,T} of measure at most u, proving the full
uniform-integrability quantifier near arbitrary moving boundaries.
The integral of r^2 over I is 4ba^3/3, which gives the asserted
total-mass bound. Together with omega(u)->0 this establishes the
requested class-uniform modulus.

At T=0 the sign convention gives W_0=r^2 exp(-H(ir,s)). When H=0,
(16) reduces to |W_T|<=r^2, consistent with the frozen scalar control;
no scalar theorem was needed in the coupled proof. For general H,
the determinant retains a complex phase. Neither (14) nor any
absolute-value inequality signs that determinant or preserves a
signed integral across the moving stopping boundary.

### Independent conceptual audit959 — 14 November 2026

The audit retains all the hypotheses, the full complex determinant,
and every quantifier in (4)–(6). It reuses the primary-source coverage
in assessments954/955/957 and checks the entire proof above. No
load-bearing error or missing hypothesis was found. This closes a
local verification gap; it is reproduction of the existing argument,
not a new bound or a claim of progress beyond the literature checked.

**Variational convention and applicability.** Regard C^2 as R^4
with real inner product Re(u* v). Differentiating the smooth real
flow with respect to either real initial parameter gives exactly
(7), not dot J=conjugate(D^2S)J. For a complex symmetric matrix B,

\[
 (u,\overline{Bv})_{\mathbb R}
 =\Re(u^*\overline{Bv})=\Re(u^T Bv)
 =\Re(v^T Bu)=(v,\overline{Bu})_{\mathbb R}.
\]

This verifies the real symmetry used in (11). Conjugation preserves
the Hermitian norm, so the real operator norm of v -> conjugate(Bv)
equals the complex operator norm of B; no factor of two arises from
realification. The singular block is the displayed 2 by 2 real
matrix with c=2/q^2, and its spectrum is {2/rho^2,-2/rho^2};
the remaining two real directions have eigenvalue zero. For any real
orthonormal pair, the positive singular eigendirection has total
squared projection at most one, while the negative eigendirection
can only reduce the trace. Each of the two background quadratic
forms is at most M_2. This verifies the top-two bound (12), including
the ordering and multiplicity of the zero eigenvalues.

On every compact surviving interval the real A is continuous and
bounded, however large its bound may be. The real fundamental matrix
therefore exists, and its second exterior power acts on the initial
two-vector of norm one. These are precisely the hypotheses needed
for the cited WKM Proposition 5 growth estimate. Neither uniform
negative matrix measure nor global nonlinear existence is invoked.
The resulting estimate is for the rectangular tangent two-area;
it is not a bound obtained by multiplying two independent tangent
length estimates. The TNV local variational identity applies on the
same intervals with the stated initial tangent columns. Derivatives
of the local logarithm agree on overlaps, so no global branch is used.

**Complex determinant and singular coefficient.** Expanding the
Hermitian 2 by 2 Gram determinant gives |det_C J|^2 exactly, whereas
the real Gram determinant subtracts only (Re <u,v>)^2. Their
difference is (Im <u,v>)^2. Thus (10) has the correct inequality
direction and remains valid when the complex determinant is zero.
No determinant division, Lagrangian condition, or scalar separation
is hidden in its application to both complete tangent columns.

The holomorphic chain rule and dot X_j=conjugate(f_j) give
dot F=-F sum_j |f_j|^2. F is nonzero on U, and integrating this
scalar real-coefficient equation gives (14) without any choice of
phase or logarithm of F. The cross term is

\[
 |-2/q+g|^2
 =4/\rho^2-4\Re(qg)/\rho^2+|g|^2.
\]

With x=1/rho and y=|g|, the entire singular scalar expression is
-2x^2+4xy-y^2 = y^2-2(x-y)^2. Retaining the other term -|h|^2
and using |g|^2+|h|^2<=M_1^2 gives (15) with precisely
K=2M_2+M_1^2. It is an upper bound at every surviving point; it
does not assert a sign for the full signed density. Multiplying
(13) and (14) combines finite integrals on the same interval before
using K. There is consequently no unjustified cancellation of
infinite integrals, loss depending on a cutoff, or limiting passage
through a zero in (16).

**Finite endpoints and measurable zero extension.** Equation (9)
uses Re(qH_q), with the same conjugation convention as the cross
term above. Its uniform bounds make rho^2 and z Lipschitz up to
every finite maximal time. A zero limiting modulus forces q->0
even if its argument has no limit. For a positive limiting modulus,
the eventual lower bound rho>=ell/2 bounds dot q, giving a unique
complex limit. This exhausts the cases. Only an interior nonzero
endpoint uses the ODE continuation theorem; no continuation across
the divisor or the bidisk boundary is asserted. In particular the
case q->0 and |z|->L simultaneously needs no separate smoothness or
boundary value of H. A finite endpoint in U would extend the
integral equation and contradict maximality, so the asserted list
of limiting boundaries is complete.

Smooth dependence applies on a neighborhood of each compact
trajectory segment, yielding the relatively open domain D_H and
the full fixed-time derivative J. This gives continuity of (3) on
D_H, including at T=0 in the relative topology. For an open O in C,
the preimage under the zero extension is its relatively open
preimage in D_H, together with D_H's Borel complement if 0 is in O.
This proves joint Borel measurability for each fixed H. It does not
require tau to be continuous, a regular survivor boundary, or a
limit for F det J at a stopping event. The prescribed zero at r=0
is included in that complement, also when T=0.

**Class and measurable-set quantifiers.** The initial segment from
(0,0) to (ir,s) stays in the open bidisk since |r|<a<R and |s|<b<L.
The norm of its constant velocity is sqrt(r^2+s^2). Applying (1)
along it verifies (17) uniformly in the entire H class, including
its fixed complex value H_0. As K>=0, the common constant (4)
works for every 0<=T<=T_0, for any finite T_0, also T_0=0.
On survivors (16) proves the envelope; elsewhere the definition
proves it directly. Hence each time slice is Lebesgue integrable,
and integrating over any Lebesgue measurable E proves (6) before
taking the supremum over H and T. No measurable structure on the
space of H, or measurable uncountable supremum, is required. The
same estimate for separately chosen E_{H,T} with measure at most u
is C(T_0)a^2 u. Direct integration of r^2 over the given rectangle
gives 4ba^3/3, confirming the total-mass coefficient.

**Scope verdict.** All direct mathematical inputs are the cited
variational/compound bounds and the named standard ODE, spectral
and elementary identities already used above. C466q and C466r are
comparisons only; the empty local DAG row remains correct. No
script, numerical sampling, changed premise or stronger result was
needed for this audit. In particular, a stopped density bound does
not prove a boundary trace or control the additional time/parameter
minors of a swept surface. It cannot by itself justify Stokes across
the stopping locus or signed integral invariance. Metric changes,
intersecting divisors, global homology, signed positivity, all orders
and actual-Xi realization remain unresolved. There is no RH candidate.

## Mathlib

Full matching coverage of this coupled stopped logarithmic-flow
modulus has not been checked. The inputs are the precisely cited
real-parameter variational law and compound-volume inequality,
the named smooth ODE existence/continuation/dependence theorems,
the real spectral theorem, and elementary Gram and integral
identities. No exact Mathlib theorem for the full result is claimed;
unknown availability is not evidence of absence. Audit959 checks
the informal proof and its cited applicability; it is not a Mathlib
formalization or a new search for matching formal coverage.
