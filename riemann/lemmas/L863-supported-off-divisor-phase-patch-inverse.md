# Lemma 863: a conditional supported inverse on an off-divisor phase patch

## Hypotheses

Use the actual G,R,C,F and oriented graph density of L847. Let Omega
be a bounded connected smooth domain whose closure lies in one original
angular coordinate chart (t,s). Let u be a real smooth graph on a
neighborhood of its closure, and set

\[
 A=Du,\quad F(\Phi_u)=P+iQ,\quad
 \sigma=\operatorname{Im}\{F(\Phi_u)(1-\det A-i\operatorname{tr}A)\},
 \qquad M=P I+Q\operatorname{adj}A.                         \tag{1}
\]

Assume F(Phi_u) is nonzero on the closure. Separately assume

\[
 \lambda:=\inf_{x\in\overline\Omega}s_{\min}(M(x))>0.       \tag{2}
\]

Here singular values and matrix norms are Euclidean. Off-divisor status
alone does not imply (2). Fix 0<alpha<1 and a boundary collar U of
Omega of the kind in Teixeira Theorem3 cited below. Sources f are real
C^(0,alpha) on the closure, zero on U. Variations must also vanish on U;
no nonzero boundary trace is permitted. Smooth sources are included.
This is a local statement, with no exchange symmetry or global extension
of the background graph assumed. All constants depend on this patch and
collar; no uniform family or divisor limit is assumed.

For a scalar, vector or matrix H, use the following equivalent Holder
norms, with Euclidean/operator norms inside suprema and seminorms:

\[
 N_0(H)=\|H\|_\infty+[H]_\alpha,\qquad
 N_1(H)=N_0(H)+\sum_{j=1}^2 N_0(\partial_j H).              \tag{3}
\]

The seminorm compares all distinct points of the closure. Constants in
the divergence estimate below incorporate equivalence to its stated
Holder norms on the fixed smooth domain.

## Conclusion

The phase derivative is the existing L850 operator

\[
 L v=D\sigma_u[v]=-\operatorname{div}(Mv).                 \tag{4}
\]

It is underdetermined elliptic under (2). Its entire distributional
formal-adjoint kernel on connected Omega consists of constants.
Consequently there is a bounded real linear right inverse on precisely
the supported data of zero integral:

\[
 \int_\Omega f\,dt\,ds=0,\qquad
 v={\cal R}_u f=-M^{-1}{\cal B}_{\Omega,U}f,\qquad
 Lv=f,\qquad v|_U=0.                                    \tag{5}
\]

Here B is Teixeira's known supported ordinary-divergence solver; it is
not a new solver. Fix its constant C_div such that
N_1(B f)<=C_div N_0(f). Put

\[
 H=[M]_\alpha,\quad
 D_0=\sum_j\|\partial_jM\|_\infty,\quad
 D_\alpha=\sum_j[\partial_jM]_\alpha.
\]

Then the concrete bound is

\[
 N_1({\cal R}_u f)\le C_{\rm div}
 \left\{\lambda^{-1}+\lambda^{-2}(H+D_0+D_\alpha)
                  +2\lambda^{-3}H D_0\right\}N_0(f).     \tag{6}
\]

In particular the braces are at most
lambda^(-1)+lambda^(-2)N_1(M)+2lambda^(-3)N_1(M)^2.
The same linear operator preserves smooth data, and has higher Holder
bounds with the corresponding M^(-1) norms and divergence constants.
Extension of v by zero outside the patch is C^(1,alpha), or smooth for
smooth f, because v already vanishes on a boundary collar.

A sufficient actual-density test for (2) is

\[
 \delta:=\inf_{\overline\Omega}|F(\Phi_u)|>0,\quad
 e:=\sup_{\overline\Omega}|Q\sigma|<\delta^2,\quad
 K:=\sup_{\overline\Omega}\|M\|,
 \qquad \lambda\ge {\delta^2-e\over K}>0.                 \tag{7}
\]

This is a conditional quantitative specialization of known divergence
solvability, not a new general PDE theorem or a global correction. No
particular nonzero residual is shown to satisfy (2), (5) on the missing
transition region. A local patch source must have zero integral on that
patch; global zero integral does not impose that condition on each member
of a partition. Nonlinear convergence, a global seed, patch assembly,
divisor extension, nonnegative density and all-degree Xi signs remain
open. The separate 6 November 2026 audit below accepts this conditional
specialization only, including its stated threshold and norm constant.

## Proof

### Reused source coverage and reason for specialization

The invocation-start SPECIALIZE assessment is
drafts/literature/2026-11-06-off-divisor-linear-patch-inverse-test.md.
Its Teixeira coverage is reused without another literature search.
Precisely, Pedro Teixeira, *Dacorogna-Moser theorem on the Jacobian
determinant equation with control of support*, DCDS **37** (2017),
4071-4089, DOI10.3934/dcds.2017173,
[arXiv:1608.06213v7, Section4 Theorem3/Remark3 and proofs, pp8-10](https://arxiv.org/pdf/1608.06213v7#page=8),
provides a bounded linear C^(r,alpha) to C^(r+1,alpha) divergence solver
on a bounded connected smooth domain in R^n, n>=2, for signed
zero-integral data zero on its prescribed boundary collar, with the
solution zero on that collar. Its operator is independent of regularity
indices and preserves smoothness. Constants depend on the domain,
collar and regularity. Here n=2, the domain is the original coordinate
patch Omega with measure dt ds, and its collar and signed-data hypotheses
are exactly those above. No nonlinear determinant theorem is used.

L850 already supplies M and det M; neither is claimed as a new result.
L851's exterior lift, L852's forced transition zeros and L853's finite
jets do not supply this quantitative invertible-patch criterion. Nor
does it remove their singular/global limitations. We retain only the
local coefficient lifting, adjoint and norm checks necessary to apply
the named divergence theorem. There is no reproof of that theorem.
Delay's broader API/KRC theorem is unnecessary here and is not invoked
without checking its hypotheses: the explicit change of flux in (5)
gives the inverse directly.

### Operator, symbol, and complete compatibility

Check the relevant L850 sign without using its numerical certificates
or its special cutoff construction. For a real radial variation v,
dot z_j=z_j v_j. For pullback differentiation use Victor Guillemin and
Shlomo Sternberg, *Semi-classical analysis*, manuscript 13 January 2010,
[Section13.13, (13.7)-(13.9), pp449-452](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449),
already inspected in L850's reused assessment. L847's closed form and
this smooth-family formula give the one-form

\[
 \beta=F(\Phi_u)\{v_2du_1-v_1du_2+i(v_2dt-v_1ds)\}.
\]

Its imaginary part is (Mv)_2 dt-(Mv)_1 ds. Its exterior derivative is
-div(Mv) dt wedge ds, establishing (4) in the original orientation.
This check uses only a smooth graph and a closed form, so L850's cutoff
restrictions are not needed for the identity on Omega. Initially take
smooth v. Both the direct density variation and the displayed first-order
operator depend continuously on v and Dv, so the identity also holds
for C^(1,alpha) variations.

With the Fourier symbol convention partial_j -> i xi_j, the symbol is

\[
 \ell(x,\xi)v=-i\xi^T M(x)v,\qquad
 \|M(x)^T\xi\|\ge\lambda\|\xi\|.                         \tag{8}
\]

Thus it is surjective onto the complexified scalar space for every
nonzero real xi. Conversely, a singular M at a point has a nonzero real
left null covector, so surjectivity fails there. In this first-order
operator class symbol surjectivity is exactly matrix invertibility;
it cannot be inferred just from F!=0.

Integration by parts against a compactly supported test field gives
L*psi=M^T grad psi. The coefficients and M^(-1) are smooth, so this
identity makes sense for every distribution psi and
L*psi=0 iff grad psi=0. On connected Omega the distributions with all
first derivatives zero are the constant distributions. Hence there is
no additional adjoint-kernel compatibility hidden by (5). The elementary
distribution fact follows, for example, by mollifying on each ball:
the mollifications have zero gradient and are constant there. Pairing
against a test function of integral one on a smaller ball shows that
these constants converge; distributional convergence then identifies
psi with that constant on the smaller ball. Overlapping balls and
connectedness make the constant global. This is the formal adjoint on
Omega, tested against arbitrary compactly supported fields there. It
is not an assertion that restricting every test field to vanish on the
fixed U has the same annihilator. Sufficiency for that more restrictive
support class follows from the cited divergence solver, not merely
from the formal-adjoint computation.

For any C^1 v zero on U, Mv vanishes near the boundary; the divergence
theorem yields integral Lv=0. Thus zero integral is necessary. If f
has zero integral, the cited theorem provides W=B f with div W=f and
W=0 on U. Define v=-M^(-1)W. This proves sufficiency, linearity and
support. A collar of the whole compact boundary supplies a neighborhood
where the zero extension agrees identically with zero, proving its
regularity without any boundary-flatness substitution.

### Quantitative coefficient lifting

Let B=M^(-1). Condition (2) gives sup norm B<=lambda^(-1). The exact
two-point identity and derivative identity are

\[
 B(x)-B(y)=B(x)(M(y)-M(x))B(y),\qquad
 \partial_jB=-B(\partial_jM)B.
\]

They imply

\[
 [B]_\alpha\le\lambda^{-2}H,\quad
 \|\partial_jB\|_\infty\le\lambda^{-2}\|\partial_jM\|_\infty,
\]
\[
 [\partial_jB]_\alpha\le
 \lambda^{-2}[\partial_jM]_\alpha
 +2\lambda^{-3}H\|\partial_jM\|_\infty.                  \tag{9}
\]

For the last inequality, subtract the three-factor products
B(x) partial_jM(x) B(x) and B(y) partial_jM(y) B(y), changing one
factor at a time. The middle change gives the first term and the
two outer changes give the second. Summing (9) and the supremum bound
gives precisely the braces in (6) as an upper bound for N_1(B).
The norms (3) obey N_0(HJ)<=N_0(H)N_0(J), by the two-factor difference
identity. Leibniz' rule then gives N_1(HJ)<=N_1(H)N_1(J).
Apply this to v=-BW and use the stated divergence estimate to obtain
(6). The coarser bound follows from H+D_0+D_alpha<=N_1(M) and
H D_0<=N_1(M)^2. These bounds expose all matrix degeneration; C_div
still depends on the patch and collar and is not claimed numerically
effective or uniform in a shrinking patch.

For available coefficient estimates one can use
N_1(M)<=N_1(P)+N_1(Q)N_1(Du). In dimension two adjugation is a fixed
orthogonal conjugation of transpose, so it preserves the operator norms
and seminorms used here. Smoothness and the higher regularity assertions
follow from the same imported operator and multiplication by smooth B.

Finally L850's already established identity is

\[
 \det M=|F(\Phi_u)|^2-Q\sigma.
\]

Under (7) it is at least delta^2-e>0. For a real two-by-two matrix the
product of the two singular values is |det M|. The larger singular
value is ||M||<=K; K is positive because the determinant is positive.
This proves (7), including its direction and strict threshold.
On a relatively compact patch where L850 already gives real phase
and nonzero F, one has e=0. This shows the conditional regime is
nonempty, but those collar patches already have zero phase residual.
It does not establish a new correction on the transition.

### Required versus achieved control

The achieved bound is (6) for one stated invertible patch, with the
sufficient threshold e<delta^2 in (7). Global off-divisor status, or
global zero total phase residual, would not supply either that threshold
or patchwise zero integrals. Where M is singular the symbol test (8)
fails; this observation concerns this elliptic method, not the full
range of the differential operator, whose coefficient derivatives
still matter. No singular-range obstruction is inferred. In particular
the retained transition/divisor stops cannot be crossed by claiming
that this estimate stays uniform as lambda decreases to zero. The
downstream use is limited to correcting a compatible supported source
on a specified approximate graph satisfying these quantitative bounds.

### Separate bounded audit, 6 November 2026

The audit used the prior SPECIALIZE assessment
drafts/literature/2026-11-06-l863-supported-patch-inverse-audit.md.
It checked L847's original convention A_(j l)=partial_l u_j and
L850's general identities only; the exterior certificate, cutoff
construction and singular-range claims were not inputs. In particular,
the two coefficients of Im beta are

\[
 Q(v_2 A_{11}-v_1 A_{21})+P v_2,\qquad
 Q(v_2 A_{12}-v_1 A_{22})-P v_1.
\]

These are (Mv)_2 and -(Mv)_1 respectively, so exterior differentiation
has exactly the negative-divergence sign in (4). No derivative of F
is omitted: differentiating beta differentiates its full coefficient F.
Expanding the determinant independently gives
P^2+PQ tr A+Q^2 det A=P^2+Q^2-Q sigma. Thus its lower bound in (7)
is delta^2-e. The larger singular value is at most K, giving the
claimed lower bound for the smaller singular value. Strict inequality
e<delta^2 is sufficient, not asserted necessary; equality supplies no
positive bound by this test.

The coefficient estimate (9) was checked by changing the left B,
middle partial_j M and right B one at a time. The two outer differences
each cost lambda^(-3) H ||partial_j M||_infinity. To check the norm
constant without hiding a product factor, write
b=N_0(B), b'=sum_j N_0(partial_j B), w=N_0(W) and
w'=sum_j N_0(partial_j W). Leibniz and the N_0 product bound give

\[
 N_1(BW)\le bw+b'w+bw'\le(b+b')(w+w').
\]

This verifies (6) with exactly its displayed braces. The norm
equivalence is included in C_div; it is not an extra unstated factor.
The adjoint distribution argument and the full fixed-collar necessity
and sufficiency were checked separately as above. Smooth coefficients,
n=2, connectedness, the prescribed whole-boundary collar, signed
C^(0,alpha) data and zero integral satisfy the reused Teixeira theorem.
No additional regularity gain for M^(-1), uniform patch constant,
nonzero transition source or nonlinear solution is inferred. The audit
found no mathematical correction to (4)-(9); its only clarification is
the distinction between the formal adjoint and the fixed-support tests.

## Mathlib

Full matching Mathlib coverage of this supported actual-G phase inverse
and its Holder estimate was not checked. No absence claim is made.
The support-preserving divergence input is imported from the precise
primary theorem above. Supporting matrix, differentiation, integration
and distribution results may be available; no formalization is claimed.
This is a local known-theorem specialization (REPRODUCTION), not a
claim of progress beyond the inspected general PDE sources or of RH.
