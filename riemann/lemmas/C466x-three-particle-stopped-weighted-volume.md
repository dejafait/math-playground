# C466x — Three-particle stopped weighted determinant

## Hypotheses

Fix real numbers 0<a<R<infinity, T_0>0, M_1,M_2>=0, all finite,
and H_0 in C. Let H be holomorphic on
B={z in C^3: |z_j|<R for j=1,2,3}, with H(0)=H_0 and
\[
 \|\nabla H(z)\|_2\le M_1,\qquad
 \|D^2H(z)\|_{\mathrm{op}}\le M_2\quad(z\in B).             \tag{1}
\]
These are holomorphic derivatives in the standard Hermitian norms.
No permutation symmetry or separability of H is assumed. Define
\[
 \Delta(z)=\prod_{i<j}(z_j-z_i),\quad U=B\setminus\{\Delta=0\},
 \quad S=-2\log\Delta+H,\quad F=\Delta^2e^{-H}.             \tag{2}
\]
Only derivatives of a local logarithm are used; they and F are
single valued on U. For pairwise distinct real u in I=(-a,a)^3,
let X(t,u) solve the unit-flat raw physical-time equation
\[
 \dot X=\overline{\nabla S(X)},\qquad X(0,u)=iu             \tag{3}
\]
on its first maximal forward interval [0,tau(u)) in U. Write
J_t=D_uX(t,u) for the full complex 3-by-3 matrix of derivatives
with respect to the real initial parameters at fixed time, J_0=iId.
For t<tau(u) put
\[
 W_t(u)=(-1)^3F(X(t,u))\det_{\mathbb C}J_t/i^3.             \tag{4}
\]
Set W_t(u)=0 for t>=tau(u) and at initial coincidences. This is
a prescribed stopped density, not a derivative of a stopped map.
An outer exit stops the trajectory as well as a collision; no restart
is made. A unique limiting endpoint or regular first-hit surface is
not assumed.

## Conclusion

With
\[
 K=3M_2+M_1^2,\qquad
 C=\exp\{KT_0-\Re H_0+\sqrt3\,aM_1\},                    \tag{5}
\]
the full stopped density satisfies
\[
 |W_t(u)|\le C|\Delta(u)|^2
 \qquad(0\le t\le T_0,\ u\in I).                           \tag{6}
\]
C is common to the entire class in (1), independent of all initial
pair spacings, relative collision rates, and surviving distances to
the divisors or outer boundary. Its formula happens not to need R.
For each fixed H the stopped density is jointly Borel measurable.

This supplies the local multidivisor modulus sought in attempt977.
It supplies no determinant sign, endpoint trace, complete-form current
bound, conserved signed integral, global contour, actual-H bounds,
all-degree positivity or Xi transfer. Independent conceptual audit979
below validates the full stated bound and its quantifiers. Its tools are imported;
the combined specialization was not supplied by the sources checked
in review975, and no originality of its elementary identities or
of the resulting bound is asserted. C466s is a comparison, and C466k
motivates the convention (4); neither is used as a theorem premise.

## Proof

### Imported local tools and their applicability

Tanizaki, Nishimura and Verbaarschot, *Gradient flows without blow-up
for Lefschetz thimbles*, JHEP10(2017)100,
[arXiv:1706.03822v2](https://arxiv.org/pdf/1706.03822v2),
27 September 2017, Appendix B, (B.1)-(B.5), printed p22, gives
the real-parameter variational equation
\[
 \dot J=\overline{(D^2S)J}.                                \tag{7}
\]
Both factors inside the product are conjugated. No holomorphic
dependence on the real initial parameters is asserted.

Wu, Kanevskiy and Margaliot, *k-Contraction: Theory and Applications*,
[arXiv:2008.10321v2](https://arxiv.org/pdf/2008.10321v2),
27 September 2021, Sections 2.2, 2.4-2.5, equation (17), and
Section 3.1, Theorem 4 and Proposition 5 with their proofs,
printed pp4-9, supplies the following growth bound. For a continuous
real A(t), with dot Phi=A Phi and Phi(0)=Id,
\[
 \|\Phi(t)^{(3)}\|\le
 \exp\!\int_0^t\mu_2(A(s)^{[3]})\,ds.                     \tag{8}
\]
Here (3) and [3] denote multiplicative and additive compounds in
the Euclidean exterior norm. The matrix measure in (8) is the sum
of the three largest eigenvalues of (A+A^T)/2. This is the growth
inequality in the cited proof; uniform negativity is required for
its contraction conclusion, not for (8). The range k<=n permits
k=3,n=6. Acting on the initial decomposable three-vector gives the
same bound for the real three-volume of three tangent columns.
Neither imported result is reproved here.

The vector field in (3) is smooth on the open set U in R^6.
The Picard-Lindelof theorem and smooth-dependence and maximal-flow
theorems for smooth ODEs give its maximal flow on an open domain.
For any fixed u and T<tau(u), the image of [0,T] is compact in U.
On that interval all coefficients in (7) are continuous and bounded,
and neighboring initial points survive up to T. Thus the full
fixed-time J is well defined and obeys (7). Local logarithmic
derivatives agree on overlaps. These observations verify the exact
local hypotheses of (7)-(8), without requiring a class-uniform
survival time or a boundary value of H.

### Elementary comparison of the two volume norms

For three columns v_1,v_2,v_3 in C^3, let V be their Euclidean real
three-volume in R^6. Then
\[
 |\det_{\mathbb C}[v_1\ v_2\ v_3]|\le V.                  \tag{9}
\]
If they are real-linearly dependent, their complex determinant and
V both vanish. Otherwise real Gram-Schmidt writes the column matrix
as E Q, where E has real-orthonormal columns and Q is a real
invertible triangular matrix. The real Gram identity gives
V=|det Q|. Each column of E has Hermitian norm one, so the complex
Hadamard determinant inequality gives |det_C E|<=1. Multiplicativity
of the complex determinant, with det_C Q=det_R Q, proves (9).
This supporting elementary verification fixes the norm convention;
no calibration theorem, complex invertibility, or Lagrangian
condition is needed. For the columns of J write V(t); V(0)=1.

### Collective force estimate for every complex triangle

For pairwise distinct z_1,z_2,z_3, put
\[
 g_j=\partial_j\log\Delta=\sum_{k\ne j}\frac1{z_j-z_k},
 \quad f_0=-2g,\quad
 P=\sum_{i<j}|z_i-z_j|^{-2}.                               \tag{10}
\]
We need the collective lower bound
\[
 \|g\|^2=2P+\frac{16\mathcal A^2}{|\Delta(z)|^2}
 \ge2P,\qquad \|f_0\|^2\ge8P,                            \tag{11}
\]
where mathcal A is the unsigned Euclidean area of the triangle
with these complex vertices. Collinear triples are included.

Here is a direct verification of the cancellation and its constant.
Set p=z_2-z_1, q=z_3-z_1 and
D=|pq(p-q)|^2=|Delta(z)|^2>0. Then
\[
 g_1=-1/p-1/q,\quad
 g_2=1/p+1/(p-q),\quad g_3=1/q+1/(q-p).
\]
Expanding their squared moduli gives 2P plus twice the real part of
\[
 E=\frac1{p\bar q}+
   \frac1{p\overline{(p-q)}}+
   \frac1{q\overline{(q-p)}}.
\]
Let A=|p|^2, B=|q|^2, c=Re(bar p q), d=Im(bar p q). Multiplying
by D before taking real parts gives
\[
 \begin{aligned}
 D\Re E
 &=\Re\{\bar p q|p-q|^2+
           \bar p(p-q)|q|^2+\bar q(q-p)|p|^2\}\\
 &=c(A+B-2c)+(A-c)B+(B-c)A\\
 &=2(AB-c^2)=2d^2.
 \end{aligned}                                             \tag{12}
\]
Since mathcal A=|d|/2, the cross-term contribution 2 Re E is
4d^2/D=16 mathcal A^2/D. This proves (11) for all distinct triples,
including d=0, without a relative-spacing or angle restriction.
The algebra is supporting elementary mathematics, not a novelty
claim. In particular no independent-pair evolution is substituted
for the coupled force.

### Real third-volume growth and the singular weight

Let h=grad H, f=grad S=f_0+h, evaluated along a fixed surviving
trajectory. Write b_ij=e_i-e_j, d_ij=z_i-z_j. The complex Hessian is
\[
 D^2S=\sum_{i<j}\frac{2b_{ij}b_{ij}^T}{d_{ij}^2}+D^2H.
                                                               \tag{13}
\]
For any complex symmetric B, the real map v maps to overline(Bv)
is symmetric: its real inner product with u is Re(u^T Bv), which
is symmetric in u,v. Consequently the real variational matrix
A_R:v maps to overline((D^2S)v) is real symmetric, as are each of
its pair summands and the background summand A_H. Conjugation is
an isometry, so ||A_H||_op<=M_2 with no realification factor.

For a pair, decompose C^3 into the complex line through
b_ij/sqrt(2) and its Hermitian orthogonal complement. Because b_ij
is real, the summand vanishes on the complement and on that line
acts as alpha maps to overline(4 alpha/d_ij^2). The real matrix
of alpha maps to overline(c alpha) is
\[
 \begin{pmatrix}\Re c&-\Im c\\-\Im c&-\Re c\end{pmatrix},
\]
with eigenvalues +/-|c|. Thus the pair summand has spectrum
{4/|d_ij|^2,-4/|d_ij|^2,0,0,0,0} in R^6.
For any real orthonormal three-frame, its trace on the frame is at
most 4/|d_ij|^2: the squared projections onto the positive
eigendirection sum to at most one, and the negative contribution
can only decrease that trace. Each background diagonal entry is
at most M_2. Summing on the same frame and then maximizing gives
\[
 \mu_2(A_R^{[3]})\le4P+3M_2
                  \le\tfrac12\|f_0\|^2+3M_2.              \tag{14}
\]
The maximization is the usual spectral-theorem characterization
of the top three eigenvalue sum. Pair summands need not commute,
share eigenvectors, or provide independent divisor coordinates.
The second inequality is exactly the collective estimate (11).
Applying (8) to (7) now yields
\[
 V(T)\le\exp\!\int_0^T\mu_2(A_R(t)^{[3]})\,dt.             \tag{15}
\]

F is nonzero and holomorphic on U and partial_j F=-F f_j.
The chain rule along (3) therefore gives the exact scalar identity
\[
 \dot F=-\|f\|^2F,\qquad
 |F(X(T))|=|F(iu)|\exp\!\left(-\int_0^T\|f\|^2dt\right).
                                                               \tag{16}
\]
All integrals in (15)-(16) are finite on this compact surviving
interval. With the Hermitian norm and its real cross term,
completing the square in (14) gives
\[
 \begin{aligned}
 \mu_2(A_R^{[3]})-\|f_0+h\|^2
 &\le3M_2+\tfrac12\|f_0\|^2-\|f_0+h\|^2\\
 &=3M_2+\|h\|^2-\tfrac12\|f_0+2h\|^2\\
 &\le3M_2+M_1^2=K.
 \end{aligned}                                             \tag{17}
\]
This inequality is uniform throughout U. In particular, its constant
does not deteriorate when all three divisors approach each other.
It combines the singular growth and exact weight before taking a
uniform bound; no uncontrolled product of column norms is used.

Combining (4), (9), (15)-(17) gives, at every T<tau(u),
\[
 |W_T(u)|\le |F(X(T))|V(T)
           \le |F(iu)|e^{KT}
           =|\Delta(u)|^2e^{-\Re H(iu)+KT}.                 \tag{18}
\]
Here Delta(iu)=i^3 Delta(u), and the prefactor in (4) has modulus
one. At T=0 the same convention gives
W_0(u)=Delta(u)^2 exp(-H(iu)), as required.

### Uniform initial bound and stopping

The straight segment s maps to siu, 0<=s<=1, lies in B. By (1)
and the fundamental theorem of calculus,
\[
 |H(iu)-H_0|\le M_1\|u\|_2\le\sqrt3\,aM_1.               \tag{19}
\]
Substitute (19) into (18) and use K>=0, T<=T_0 to obtain (6)
at every survivor, with precisely the constant (5). The estimate
holds for each compact surviving interval with the same constant;
it requires no improper-integral limit at tau. At stopped points
and initial coincidences (6) follows from the assigned zero value.
No infinite endpoint determinant is multiplied by a zero weight.

For fixed H the survivor set
{(t,u): t>=0, u in I, Delta(u)!=0, t<tau(u)} is relatively open
in [0,infinity) times I by the open maximal-flow domain. Formula
(4) is continuous there by smooth dependence. Its extension by
zero on the Borel complement is Borel measurable. This proves the
measurability assertion without continuity of tau, an endpoint
uniqueness theorem, or a boundary trace. It treats an outer exit
and a collision identically for the prescribed stopped observable.

Only the modulus has been estimated. In particular, (16) fixes
the phase of F along a trajectory but does not fix the phase of
det_C J, or identify any stopped signed integral with its initial
value. Such claims, and the actual-Xi specialization, remain open.

### Independent conceptual audit979 — 14 November 2026

This audit replays the complete fixed-data statement under the
unchanged SPECIALIZE assessment977, separately approved in step978.
It reproduces the existing specialization; it supplies neither a new
bound nor an originality claim. The approved source comparison for
the precisely cited TNV and WKM passages above is reused. No essential
source mismatch was found and no new theorem premise is introduced.

**Triangle and singular constants.** In the coordinates of (12),
the three cross products come from the two terms in each respective
g_j. The signs in g_2 and g_3 are essential: the last denominator
is conjugate(q-p), not conjugate(p-q). Multiplication by
D=AB(A+B-2c)>0 gives the three real numerators
c(A+B-2c), (A-c)B and (B-c)A. Their sum is
2AB-2c^2=2d^2 because |conj(p)q|^2=AB=c^2+d^2.
The square expansion contributes twice this sum divided by D,
namely 4d^2/D. The geometric area is |d|/2, verifying exactly
16 mathcal A^2/D. Thus ||f_0||^2=8P+16d^2/D>=8P.
The only denominator restriction is pairwise distinctness. Collinear
triples give d=0 and equality; arbitrarily unequal spacings are
included, with no discarded error depending on a spacing ratio.

**Real variation and volume.** Differentiating the vector field with
respect to a real initial parameter yields conjugate((D^2S)J),
including conjugation of J. For B=B^T the real Euclidean pairing
of u with conjugate(Bv) is Re(u^T Bv), hence symmetric.
The norm of that real map equals the Hermitian operator norm of B.
For b=e_i-e_j, ||b||^2=2, so the Hessian term 2bb^T/d^2
acts on b/sqrt(2) with coefficient 4/d^2 before conjugation.
Its real spectrum is precisely +/-4/|d|^2 and four zeros.
For any single orthonormal real three-frame (e_l), writing the
unit pair eigenvectors as v_+,v_-, its trace is
(4/|d|^2) sum_l((e_l dot v_+)^2-(e_l dot v_-)^2)
<=4/|d|^2. Each positive projection sum is at most one.
Summing these bounds on that same frame and bounding the background
trace by 3M_2 proves (14) without simultaneous diagonalization.

The Euclidean exterior norm in WKM applies with n=6,k=3.
The tangent columns are the real fundamental matrix applied to
their initial imaginary coordinate vectors; their initial wedge
norm is one. The coefficients are continuous on every compact
surviving interval, so the growth inequality, without its optional
contraction hypothesis, gives (15). In the proof of (9), real
Gram-Schmidt gives a real triangular Q and real-orthonormal E.
Its columns also have Hermitian norm one, so complex Hadamard
gives |det_C E|<=1. This remains valid when E is complex-singular;
there is no assumption that real independence implies complex
independence. If the original columns are real-dependent, both
sides vanish. Thus (9) is valid in all cases needed here.

**Weight, coupled background and orientation.** On U,
partial_j F=-F(f_0+h)_j and dot X_j=conjugate((f_0+h)_j).
Therefore dot F=-||f_0+h||^2 F exactly; no branch of log F
or logarithm of det J is differentiated. Both integrals used in
(15)-(16) are finite on each compact survivor. Multiplying their
estimates before bounding the exponent is legitimate. Expanding
the Hermitian square gives
\[
 \tfrac12\|f_0\|^2-\|f_0+h\|^2
 =-\tfrac12\|f_0\|^2-2\Re\langle f_0,h\rangle-\|h\|^2
 =\|h\|^2-\tfrac12\|f_0+2h\|^2.
\]
This proves exactly K=3M_2+M_1^2 for arbitrary coupled H.
No componentwise separation, symmetry or smallness of H is used.
At t=0, det_C J=i^3 and Delta(iu)=i^3 Delta(u), so
(-1)^3 Delta(iu)^2=Delta(u)^2. The normalization in (4)
therefore gives the stated W_0 with no extra sign. Along the
segment siu in B, the bilinear differential obeys
|sum_j H_j(siu) i u_j|<=M_1||u||_2 by Cauchy-Schwarz.
Integrating gives (19) and hence exactly the constant C in (5).

**First-lifetime and common quantifiers.** Fix any H in the class,
distinct u in I, and 0<=T<=T_0 with T<tau(u). The image of [0,T]
is compact in U, so local ODE smooth dependence defines all fixed-time
derivatives on a neighborhood of this initial point. These are not
derivatives of the zero-extended map. Applying the preceding argument
on this interval gives the same C for every such H,u,T; none of its
steps requires a common compact set or a uniform positive lifetime.
For T>=tau(u) and for initial coincidences the asserted bound follows
directly from the assigned value zero. No limiting product at tau,
unique collision endpoint, or continuity of the lifetime is used.
An infinite lifetime and T=0 are included. The open maximal-flow
domain restricted to initial points iu makes the survivor set
relatively open in [0,infinity) times I. Its continuous density has
a Borel zero extension, jointly in t,u for each fixed H. Outer
exits require no separate endpoint argument under this definition.

**Verdict and limits.** All steps of (6), with the exact constant
(5), pass this audit. This validates a local mathematical input,
not progress beyond the inspected sources in the sense of established
novelty. C466s and C466k remain comparisons/conventions, not theorem
premises. No nonzero boundary trace is set equal to zero by the proof:
only the prescribed observable is set to zero after stopping.
The audit does not establish integrability of complete spacetime-form
coefficients, a weak Stokes identity, phase positivity, actual-H bounds,
global signed assembly or actual-Xi all-degree positivity. In
particular a modulus cannot be substituted for an algebraic square.
No numerical experiment or mathematical script was needed for these
exact checks; Mathlib coverage remains as qualified below.

## Mathlib

Full matching coverage has not been checked. The source comparison
used primary analytic-flow and compound-matrix papers, not a
Mathlib theorem for this stopped three-particle bound. The real
Gram identity, complex Hadamard inequality and finite-dimensional
spectral theorem are supporting standard inputs; exact Mathlib
names for their needed forms have not been checked. Unknown
availability is not evidence of absence, and no formal verification
is claimed.
