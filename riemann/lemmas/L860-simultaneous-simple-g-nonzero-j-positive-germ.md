# Lemma 860: simultaneous simple-G contacts admit a nonzero-J positive germ

## Hypotheses

Use the actual entire G and the positive constants R,C of L847, with
its full form on X=(C minus zero)^2:

\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
 \qquad
 \omega=C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^3z_2^3}
                    dz_1\wedge dz_2.                         \tag{1}
\]

Explicitly hypothesize distinct nonzero numbers zeta,eta with
G(zeta)=G(eta)=0 and G'(zeta)G'(eta)!=0. Fix arbitrary real lifts
p=(arg zeta,arg eta). No actual pair is selected or certified here.
For a real C2 map u on an open angular neighborhood O of p, retain

\[
 \Phi_{u,j}(\theta)=R e^{u_j(\theta)+i\theta_j},\qquad
 J_u=\det(I-iDu),\qquad q_u=F(\Phi_u)J_u,\qquad
 \Phi_u^*\omega=q_u\,d\theta_1\wedge d\theta_2.              \tag{2}
\]

The orientation in (2) is fixed. No transversality, rank restriction,
prescribed boundary data, symmetry, periodic extension or RH is assumed.

## Conclusion

There is such a graph through (zeta,eta) with u real analytic, J_u
nowhere zero, q_u(p)=0 and q_u(theta)>0 for every theta!=p in O.
Both coordinate maps Phi_u,j have real rank two throughout a sufficiently
small O. Each pulled-back G factor vanishes precisely at p on O;
the two distinct coordinate values remain distinct.

Conversely, any C2 graph through this pair with q_u real nonnegative
on an open neighborhood and J_u(p)!=0 must have real rank two for
both coordinate maps at p. More precisely, set

\[
 l_j=D\Phi_{u,j}(p):\mathbb R^2\longrightarrow\mathbb C,
 \quad
 K_0=-C\frac{G'(\zeta)G'(\eta)(\zeta-\eta)^2}
                  {\zeta^2\eta^2}J_u(p)\ne0.                \tag{3}
\]

Then l_2=c conjugate(l_1) for some c!=0 with K_0 c real strictly
positive. This is a necessary tangent condition, not a theorem that
arbitrary prescribed tangent or boundary data extend.

The existence assertion is an exact conditional local germ, not just
a quadratic jet. It shows that two odd simple factors can meet with
positive density and nonzero J. It does not produce a global torus,
force a contact, glue prescribed data, establish any new Xi mixed-minor
sign, or prove RH. The neighborhood is not effective or uniform in the
pair. The independent conceptual audit of 6 November 2026 below
accepts this conditional conclusion and its necessary tangent condition.
POTENTIALLY_NEW refers only to the bounded comparison's failure to
locate a matching radial-graph result, not to certified originality.

## Proof

### Reused sources and the specific calculation required

The invocation-start assessment
`drafts/literature/2026-11-06-simultaneous-simple-g-contact-scope.md`
has decision EXPLORE and covers this exact C2, all-rank, full-form test.
Import the following standard tools, already inspected there and in
its cited single-contact assessments:

- Jiří Lebl, *Guide to Cultivating Complex Analysis*, v1.10,
  5 November 2026, [Theorem 2.4.7, pp49-50, and Corollary 3.2.12,
  pp67-68](https://www.jirka.org/ca/ca.pdf): finite-order Taylor
  factorization and primitives on star-like plane domains.
- Lebl, *Tasty Bits of Several Complex Variables*, v4.4,
  31 May 2026, [Theorem 1.2.1 and proof,
  pp20-21](https://www.jirka.org/scv/scv.pdf#page=20): holomorphic
  polydisc power series, compact uniform absolute convergence and
  the converse. Closed polydiscs below lie inside a larger domain
  of holomorphicity.
- Marc Chaperon, *On the Cauchy-Kowalevski theorem*, 9 January 2007,
  [Section 1, Corollary 1 and the real/complex justification,
  p2](https://webusers.imj-prg.fr/~marc.chaperon/Chaperon_Cauchy_Kowalevski.pdf#page=2):
  the analytic local inverse theorem at an invertible derivative.

We do not reprove these general results. Their applications below need
the displayed derivatives, joint holomorphicity, both zero divisors
and the original angular orientation. These are the specific differences
not supplied by a bare primitive theorem. Szawlowski's inspected
function-germ normal form is not imported: it does not by itself give
this oriented surface. L855/L859 motivate the comparison but are not
mathematical inputs; their single-G primitive has a vanishing derivative
at the present second zero. C858b is not used.

### A joint coordinate that retains both simple factors

Put w=z1-zeta and t=z2-eta. The simple-zero factorization gives

\[
 G(\zeta+w)=w g_1(w),\quad G(\eta+t)=t g_2(t),\quad
 g_1(0)=G'(\zeta)\ne0,\quad g_2(0)=G'(\eta)\ne0.
\]

Choose a product of discs centered at (0,0), with closure in a larger
product where all of g1(w), g2(t), zeta+w, eta+t and zeta+w-eta-t
are nonzero. This is possible by continuity and the pair hypotheses.
The function

\[
 H(w,t)=C\frac{g_1(w)g_2(t)(\zeta+w-\eta-t)^2}
                      {(\zeta+w)^3(\eta+t)^3},\qquad
 H_0=H(0,0)\ne0                                           \tag{4}
\]

is holomorphic and nonvanishing there, and the full form is exactly
omega=w t H(w,t) dw wedge dt. Define

\[
 E(w,t)=2\int_0^1 s H(w,s t)\,ds.                          \tag{5}
\]

This is jointly holomorphic, including t=0. Indeed the polydisc
series H=sum h_ab w^a t^b integrates termwise on every smaller
compact polydisc to E=sum 2h_ab w^a t^b/(b+2). Compact uniform
absolute convergence justifies the integration, and the converse
power-series theorem gives holomorphicity. Equivalently,
t^2 E(w,t)=2 integral_0^t tau H(w,tau) d tau on the second disc.
The cited primitive theorem therefore gives

\[
 \partial_t(t^2 E)=2tH,\qquad E(0,0)=H_0.                 \tag{6}
\]

Choose B0 with B0^2=H0; then B0!=0. The map B->B^2 has derivative
2B0!=0 at B0. Its holomorphic local inverse, composed with E after
shrinking the product, gives a holomorphic nonzero B(w,t) with
B^2=E and B(0,0)=B0. Set

\[
 v=V(w,t)=tB(w,t).
\]

Differentiating V^2=t^2 E in (6) gives the identity

\[
 V V_t=tH.                                                \tag{7}
\]

No division by t or V was used. In particular the identity holds on
t=0. Also V(w,0)=0, V_w(0,0)=0 and V_t(0,0)=B0!=0. The analytic
inverse theorem applied to (w,t)->(w,V(w,t)) yields, on neighborhoods
of (0,0), an inverse (w,v)->(w,h(w,v)). Shrink inside the previous
product and, if necessary, take a smaller polydisc in the inverse
domain. Uniqueness, V(w,0)=0 and differentiation give

\[
 h(w,0)=0,\quad h_w(0,0)=0,\quad
 h_v(w,v)=1/V_t(w,h(w,v))\ne0,\quad h_v(0,0)=1/B_0.        \tag{8}
\]

Here V_t is nonzero throughout the chosen inverse neighborhood.
The wedge identity dw wedge dV=V_t dw wedge dt and (7) give exactly

\[
                         \omega=w v\,dw\wedge dv.         \tag{9}
\]

Both divisors are retained: w=0 stays w=0, and t=0 is equivalent
to v=0 because B is nonzero. This normalization did not divide by
either G factor, F, or the form's vanishing coefficient.

### Choosing a conjugate plane with the original orientation

Let D=zeta eta B0!=0. Set k1=exp(i pi/4), k2=i k1. For these choices

\[
 \rho(k):=-2i k^2\in\{2,-2\},\qquad
 \lambda_0(k):=-\operatorname{Im}(k/D).                    \tag{10}
\]

At least one lambda0(kj) is nonzero: otherwise the nonzero numbers
k1/D and i k1/D would both be real. Choose that j, and replace kj
by -kj if needed. This leaves rho unchanged and reverses lambda0,
so we obtain k with rho(k)/lambda0(k)>0. Neither quantity is zero.
This finite choice is valid for every hypothesized pair and either
choice of B0; no phase condition on G' is assumed.

For real x,y near zero put W=x+i y and define the actual surface

\[
 S(x,y)=\bigl(\zeta+W,\ \eta+h(W,k\overline W)\bigr).     \tag{11}
\]

A sufficiently small open neighborhood of the origin maps
(W,k conjugate(W)) inside the inverse domain. Thus S is real
analytic. By (9), using dW wedge d conjugate(W)=-2i dx wedge dy,

\[
 S^*\omega=\rho(k)(x^2+y^2)\,dx\wedge dy.                 \tag{12}
\]

To check the required orientation, take local logarithms near 1 and
define Theta_j=p_j+Im log(S_j/S_j(0,0)), normalized by Theta(0)=p.
These logarithms exist by the holomorphic inverse theorem for exp
at zero; S_j is close to its nonzero central value. Equation (8) gives

\[
 dS_1=dW,\qquad dS_2=(k/B_0)d\overline W
                 \quad\hbox{at }(0,0).
\]

Writing alpha=1/zeta and beta=k/(B0 eta), the angular derivative is

\[
 D\Theta(0)=
 \begin{pmatrix}\operatorname{Im}\alpha&\operatorname{Re}\alpha\\
                 \operatorname{Im}\beta&-\operatorname{Re}\beta
 \end{pmatrix},\quad
 \det D\Theta(0)=-\operatorname{Im}(\alpha\beta)
                         =\lambda_0(k)\ne0.               \tag{13}
\]

The real analytic inverse theorem now applies to Theta. Take a small
open disc U about (0,0) inside its injectivity neighborhood and every
previous domain, with lambda=det DTheta of constant sign and
|lambda|>|lambda0|/2. Also shrink so both S coordinates are nonzero
and distinct, and all nonzero factors in (4) remain nonzero.
All these restrictions hold simultaneously by continuity. Put
O=Theta(U), an open neighborhood of p, and use the analytic inverse
(x(theta),y(theta)). Define

\[
 u_j(\theta)=\log\bigl(|S_j(x(\theta),y(\theta))|/R\bigr).
\]

These functions are real analytic and real valued. The angle lifts
ensure Phi_u=S composed with Theta inverse, with Phi_u(p)=(zeta,eta).
Transforming (12), with its actual determinant rather than its
absolute value, gives

\[
 q_u(\Theta(x,y))=
             \frac{\rho(k)(x^2+y^2)}{\lambda(x,y)}.        \tag{14}
\]

The sign choice in (10) proves positivity off the center and zero at
the center. A negative lambda is allowed only with negative rho;
their ratio in the original angular orientation is strictly positive.

### Nonzero J and the two contact sets

The h_w term disappears from dS1 wedge dS2, so (11) gives

\[
 S^*(dz_1\wedge dz_2)=-2i k h_v(W,k\overline W)\,dx\wedge dy.
\]

For any angular graph, the coefficient of dz1 wedge dz2 is
-Phi_u,1 Phi_u,2 J_u. Consequently

\[
 J_u(\Theta(x,y))=
       \frac{2i k h_v(W,k\overline W)}
            {S_1(x,y)S_2(x,y)\lambda(x,y)}\ne0.            \tag{15}
\]

All factors here are nonzero on the same U, including its center.
For a second full-density check, (1) and (4) give
F(S)=-W h(W,k conjugate(W)) H(W,h(W,k conjugate(W))) S1 S2.
Equations (7)-(8) imply h H h_v=v on the inverse domain, also at
v=0. Multiplication by (15) therefore gives
-2i k W v/lambda=rho(k)|W|^2/lambda, exactly (14). Neither factor
nor the full-J contribution has been suppressed.

Since g1 and g2 stay nonzero, the first G factor vanishes exactly
when W=0. For the second factor, h(w,v)=0 is equivalent to v=0
by V(w,0)=0 and the inverse identity. On this surface v=k conjugate(W),
so it too vanishes exactly at W=0. The first coordinate differential
has real rank two. At the center the second is (k/B0)d conjugate(W),
whose real determinant is -|k/B0|^2!=0. Continuity permits a further
common shrink making its rank two throughout U. Composing with the
angular diffeomorphism preserves both ranks and the contact sets.

### First-order necessity for every C2 graph: no rank-one exception

Consider any graph in the converse assertion. Let w_j(theta) be
Phi_u,j(theta) minus its respective central zero. Factorization in
(1) gives q_u=w_1 w_2 K on a neighborhood, where K is continuous and
K(p)=K0 of (3). In fact its coefficient is

\[
 K(\theta)=-C\frac{g_1(w_1)g_2(w_2)
                 (\Phi_{u,1}-\Phi_{u,2})^2}
                 {\Phi_{u,1}^2\Phi_{u,2}^2}J_u(\theta).
\]

For every real vector a, first-order differentiability and continuity
give, along positive epsilon tending to zero,

\[
 \frac{q_u(p+\epsilon a)}{\epsilon^2}
             \longrightarrow K_0 l_1(a)l_2(a)
                          \in\mathbb R_{\geq0}.            \tag{16}
\]

The open parameter domain permits every direction. This calculation
uses no second derivative of q or high-order Taylor expansion of J.
Neither l_j is zero: its own-angular derivative is respectively
zeta(partial_1 u1+i) or eta(partial_2 u2+i), which cannot vanish
for real u. Their complex determinant is

\[
 \det_{\mathbb C}(l_1,l_2)
       =\zeta\eta\det(Du(p)+iI)=-\zeta\eta J_u(p)\ne0.    \tag{17}
\]

Suppose l1 has real rank one. Write l1=a r with a!=0 complex and
r a nonzero real linear form. The reality in (16) says
r Im(K0 a l2)=0 identically. On the dense set r!=0 the second
linear form vanishes, hence it vanishes everywhere. Thus
s=K0 a l2 is a nonzero real linear form, and (16) says r s>=0.
If r and s were independent, their joint real map would be invertible
and attain (1,-1), contradicting this inequality. Hence s=c r,
with c>0, and l1,l2 are complex proportional, contradicting (17).
The same argument with the two roles interchanged excludes rank one
for l2. Both ranks must therefore be two. Rank zero was already
excluded without a transversality assumption.

For the more precise tangent claim, l1 is now a real-linear
isomorphism onto C. Express l2 after that isomorphism as
l2=A l1+B conjugate(l1), with A,B complex; every real-linear map
of C has this expression, as is checked from its values at 1 and i.
Equation (16) then says

\[
             K_0 A Z^2+K_0 B|Z|^2\in\mathbb R_{\geq0}
                          \quad\hbox{for all }Z\in\mathbb C.
\]

Set Z=1 and i. Reality implies Im(K0 A)=Im(K0 B)=0.
Setting Z=exp(i pi/4) additionally gives Re(K0 A)=0. Thus A=0,
and K0 B is real nonnegative. Since l2 is nonzero, B!=0, so
K0 B>0. Taking c=B proves the claim. These necessary first-order
conditions were not used as a substitute for the exact construction
(5)-(15).

As a consistency check at the constructed center, c=k/B0 and
K0=-zeta eta H0 J_u(p), so (15) gives K0 c=rho(k)/lambda0(k)>0.
This uses the signed angular determinant, as required by (3).

### Scope toward the main gap

Simultaneous simple contacts are locally feasible even though the
single-odd-factor comparison has a different sign mechanism. The
construction uses a coupled conjugate plane: it is not in L847's
globally separated product subclass. L855/L859 serve only as contrasts.
Existing free-germ/boundary and full-phase two-period
stops remain in force for those mechanisms. No prescribed collar,
forced contact, existence of a selected pair, all-degree transfer,
or resolution of L030-L032/C032a follows from this local result.

### Independent conceptual audit, 6 November 2026

This audit uses the previously approved SPECIALIZE assessment
`drafts/literature/2026-11-06-l860-simultaneous-contact-conceptual-audit.md`.
It independently checks the complete proof against L847(1)-(3) and
the exact source hypotheses recorded above. No new source theorem,
stronger conclusion or mathematical repair is required. The result
is accepted under the stated distinct, nonzero, simple-zero pair
hypotheses, with the original angular orientation.

**Analytic domains and retained divisors.** Simple-zero factorization
is applied separately to the entire G at zeta and eta. Their nonzero
derivatives, nonzero values of zeta and eta, and zeta!=eta make every
factor of H a unit on a sufficiently small product of discs. The
line segments used in (5) stay in those discs. On every smaller
closed polydisc the absolutely uniformly convergent series can be
integrated against the bounded weight 2s; the coefficient multiplier
2/(b+2) is at most one. The imported polydisc theorem therefore
supplies joint holomorphicity, and the disc primitive gives (6).

The inverse theorem for B squared applies at B0 because 2B0!=0;
shrinking the image of E inside that inverse neighborhood yields a
single nonzero B on the product. The derivative of (w,t)->(w,V)
at zero is diag(1,B0). Its inverse can be restricted to a polydisc
where V_t!=0 and both (w,0) and its image remain in the chosen
domains. Hence h(w,0)=0 by uniqueness, and h(w,v)=0 implies
v=V(w,0)=0. Conversely v=0 implies h=0. Differentiating
V squared=t squared E gives V V_t=tH at t=0 as well as elsewhere;
thus omega=wV dw wedge dV and (9) retains both factors. No
cancellation of a vanishing function is hidden in the normalization.

**Signed angular graph and its full density.** At the constructed
center the two coordinate differentials are dW and (k/B0)d conjugate(W).
The angular rows in (13) follow by taking Im(dS_j/S_j), so their
determinant is -Im(k/(zeta eta B0)), with the stated minus sign.
Among k1 and i k1 one determinant is nonzero; changing its sign
leaves -2i k squared unchanged and reverses that determinant.
Consequently the finite choice indeed makes rho/lambda0 positive
for every allowed pair and either square root B0.

All restrictions are open at zero: the triangular inverse domain,
local logarithms, angular inverse domain, nonzero coordinate values,
distinctness, h_v!=0, constant sign of lambda, and the two real-rank
conditions. Intersecting these neighborhoods and taking a smaller
disc U imposes them simultaneously. Theta is injective there and
O=Theta(U) is open. The lifted angles and positive moduli then give
exactly Phi_u=S composed with Theta inverse; u is real analytic.

Directly, wv dw wedge dv pulls back to
-2i k squared |W| squared dx wedge dy. Since
dtheta1 wedge dtheta2=lambda dx wedge dy, (14) divides by lambda,
not its absolute value. The unweighted wedge is independently
-2i k h_v dx wedge dy, whereas on an angular graph its coefficient
is -Phi_u,1 Phi_u,2 J_u. This proves (15), including at W=0.
In particular
J_u(p)=2i k/(B0 zeta eta lambda0)!=0.
Using hHh_v=v checks F(S)J_u=-2i k squared |W| squared/lambda
on the entire neighborhood, including its center. Thus positivity
is exact, not a leading-term claim. The first contact set is W=0;
the second is v=k conjugate(W)=0. The second coordinate has real
determinant -|k/B0| squared at zero, so both ranks remain two
after the common shrink and angular reparametrization.

**All ranks and C2 regularity in the converse.** Here J is continuous
and Phi is differentiable. For every real direction a, openness
permits p+epsilon a and yields (16) from w_j=epsilon l_j(a)+o(epsilon).
No second derivative of q, differentiability of its phase at zero,
or transversality is assumed. Each l_j is nonzero by its own-angular
derivative, and their complex determinant is exactly
-zeta eta J_u(p), not an unsigned real determinant.

If l1=a r has rank one, reality makes Im(K0 a l2) vanish on the
dense set r!=0 and hence everywhere. The resulting nonzero real
linear form s=K0 a l2 obeys rs>=0. Independent r,s attain opposite
signs; proportionality therefore follows with a strictly positive
coefficient. This contradicts the nonzero complex determinant.
Interchanging the roles gives the same contradiction for rank-one
l2. Rank zero was already excluded. For rank two write
l2=A l1+B conjugate(l1). Applying (16) at l1=1,i,exp(i pi/4)
forces K0 A=0 and K0 B real; nonnegativity and B!=0 make K0 B>0.
This verifies the precise necessary condition and every rank case.
For the constructed graph, K0=-zeta eta H0 J_u(p) gives
K0(k/B0)=-2i k squared/lambda0>0, checking the same orientation.

The audit validates an existing local input; it establishes no new
germ, selected actual pair, prescribed gluing, forced contact or
all-degree Xi sign. L847 remains the sole direct local mathematical
input. L855, L859 and C858b are not premises. No numerical script or
formal verification is needed or claimed for these exact checks.

## Mathlib

Full matching coverage for this simultaneous-contact radial-graph
result is not checked. The cited factorization, joint power-series
and inverse theorems are imported classical inputs; no matching
Mathlib declarations were verified in this turn. Unknown availability
is not evidence of absence, and no formalization is claimed.
