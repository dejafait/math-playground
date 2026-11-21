# Lemma 865: rank-one double contacts force crossing angular fibers

## Hypotheses

Use the actual entire G and positive R,C of L847, with its full form

\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2}.
\]

Conditionally fix distinct nonzero zeros zeta,eta of G, each of order
exactly two. No such actual pair is asserted. Choose real argument
lifts p=(p1,p2)=(arg zeta,arg eta). On an open neighborhood of p let
u=(u1,u2) be real C2, and set

\[
 \Phi_j(\theta)=R e^{u_j(\theta)+i\theta_j},\qquad
 \Phi(p)=(\zeta,\eta),\qquad
 J=\det(I-iDu),\qquad q=F(\Phi)J.
\]

Assume q is real nonnegative throughout that neighborhood, J(p)!=0,
and both real-linear maps D Phi1(p), D Phi2(p) have real rank one.
The orientation is dtheta1 wedge dtheta2, exactly as in L847.
No periodic extension, exchange symmetry, constant rank near p,
nondegenerate scalar minimum or contact-isolation hypothesis is used.

## Conclusion

For some epsilon>0, in the local coordinates x=theta1-p1,
y=theta2-p2 on the open rectangle U={|x|,|y|<epsilon},

\[
 \begin{split}
 \{G(\Phi_1)=0\}\cap U&=\{x=0\}\cap U,\\
 \{G(\Phi_2)=0\}\cap U&=\{y=0\}\cap U.                 \tag{1}
 \end{split}
\]

Thus the ENTIRE local G-contact union is the two crossing angular
fibers, and cannot be locally {p}. Equivalently, after shrinking,
u1(p1,p2+y)=log(|zeta|/R) and
u2(p1+x,p2)=log(|eta|/R). The full density vanishes on these fibers
and is strictly positive elsewhere in U, conditionally on the
hypotheses. This last statement asserts no existence of such a germ.

In particular a finite entire-contact census cannot contain this
rank-one/rank-one two-double-zero branch. The statement does not
exclude rank-two contacts, other multiplicities, J(p)=0, or
nonisolated germs. Actual zero data, global extension and actual-Xi
all-degree mixed positivity remain open. The independent conceptual
audit of 6 November 2026 below accepts exactly this conditional result.

## Proof

### Sources, scope and applicability

The original attempt's invocation-start EXPLORE assessment is
`drafts/literature/2026-11-06-double-contact-isolation-scope.md`.
It covers this exact two-double-zero isolation test using the full
L847 coefficient, audited L864 and elementary continuity/fiber tools.
Its bounded comparison found no inspected matching theorem; that is
not a claim of originality. L864 is used only for its necessary
rank-one tangent and positive scalar, never for a germ converse.

Import Jiří Lebl, *Guide to Cultivating Complex Analysis*, v1.10,
5 November 2026, [Theorem 2.4.7 and its finite-zero factorization
proof, pp49–50](https://www.jirka.org/ca/ca.pdf#page=49).
G is entire and nonzero by L847, and the two exact orders are
hypotheses. It supplies the nonvanishing local holomorphic units below.
For first-order curve restrictions use Lebl, *Basic Analysis I*,
v6.3, 15 May 2026, [Definition 4.1.1, p155](https://www.jirka.org/ra/realanal.pdf#page=155).
Import that book's [Theorem 3.3.8, intermediate value theorem,
pp132–134](https://www.jirka.org/ra/html/sec_minmaxint.html): a
continuous real function on a closed interval takes every value
strictly between its endpoint values, for either endpoint ordering.
The source assessment inspected both order cases and the proof.
Below the real function is the real part of an explicitly continuous
product restricted to a compact segment inside the given domain.

These standard results are cited, not reproved. The necessary
specialization is the full-coefficient sign argument and its angular
fiber consequence. There is no inverse theorem, singular PDE, complex
square-root choice, higher-order Taylor expansion of q or assumed
isolated minimum in this proof. No further external input is required.

### Exact factorization and normalization

Translate p to (0,0), leaving the angular orientation unchanged, and
write w1(x,y)=Phi1(p+(x,y))-zeta and
w2(x,y)=Phi2(p+(x,y))-eta. The factorization theorem gives

\[
 G(\zeta+w)=w^2g_1(w),\quad
 G(\eta+v)=v^2g_2(v),\qquad
 g_1(0)=G''(\zeta)/2\ne0,\quad g_2(0)=G''(\eta)/2\ne0.
\]

Shrink to an open angular rectangle centered at zero, with both
coordinate widths less than pi. By continuity we may require
g1(w1),g2(w2), Phi1, Phi2, Phi1-Phi2 and J to be nonzero
throughout it. For the difference and J this uses zeta!=eta and
J(p)!=0; the radial maps themselves never vanish. In particular
there are no additional G-zero labels in either coordinate image.
L847 gives the EXACT factorization

\[
 \begin{split}
 q&=K w_1^2w_2^2,\\
 K&=-C\frac{g_1(w_1)g_2(w_2)(\Phi_1-\Phi_2)^2}
                 {\Phi_1^2\Phi_2^2}J,\qquad K(0)=K_0\ne0.
                                                               \tag{2}
 \end{split}
\]

K is continuous (indeed C1); no zero factor has been canceled from q.

Write Du(p)=[[a,b],[c,d]]. L864's rank-one alternative gives b=c=0.
Put

\[
 \alpha=\zeta(a+i),\qquad \beta=\eta(d+i).
\]

Both are nonzero, and the first-order maps are
D w1(0)(x,y)=alpha x, D w2(0)(x,y)=beta y.
The same alternative, with m=n=2, gives

\[
 B_0:=K_0\alpha^2\beta^2\in\mathbb R_{>0}.              \tag{3}
\]

Define the continuous functions

\[
 H=\frac{w_1w_2}{\alpha\beta},\qquad
 B=K\alpha^2\beta^2.
\]

Equation (2) becomes q=B H^2, without division by either wj.
Shrink once more so Re B>B0/2>0 everywhere. If Re H=0 at any
point of this rectangle, write H=i h with h real. The full sign
condition then implies

\[
 0\le\operatorname{Re}q
   =\operatorname{Re}(B(ih)^2)=-(\operatorname{Re}B)h^2.
\]

Consequently

\[
 \operatorname{Re}H=0\quad\Longrightarrow\quad H=0.       \tag{4}
\]

This uses the exact varying coefficient B, not merely its value or
phase at p. Only its positive real part is bounded away from zero.

### First-order endpoint limits force both fibers

For each fixed real direction (r,s), differentiability gives, as
t tends to zero through either sign,

\[
 \frac{w_1(tr,ts)}t\longrightarrow\alpha r,
 \qquad
 \frac{w_2(tr,ts)}t\longrightarrow\beta s,
 \qquad
 \frac{H(tr,ts)}{t^2}\longrightarrow rs.                 \tag{5}
\]

This is the product of two first-order limits, not a second-order
Taylor assumption on H or a fourth-order expansion of q. Apply (5)
only to the three fixed directions (1,1),(-1,1),(1,-1). There is
one epsilon>0, smaller than the preceding rectangle widths, such
that for every 0<|t|<epsilon all relevant segments stay in that
rectangle and

\[
 \operatorname{Re}H(t,t)>\tfrac12t^2,
 \quad \operatorname{Re}H(-t,t)<-\tfrac12t^2,
 \quad \operatorname{Re}H(t,-t)<-\tfrac12t^2.             \tag{6}
\]

The common epsilon exists by taking the minimum of the finitely
many two-sided limit neighborhoods; no uniform estimate over
arbitrary directions is asserted.

Fix any such t. On the closed segment y=t, x between -|t| and
|t|, the real continuous function Re H(x,t) has opposite signs
at the endpoints by (6), including when t<0 and their order is
reversed. The cited intermediate value theorem gives an interior
x_t with Re H(x_t,t)=0. By (4), H(x_t,t)=0.

The value Phi2(p+(x,t)) cannot equal eta on this segment: their
arguments differ by t, and 0<|t|<pi. Thus w2(x_t,t)!=0.
The definition of H forces w1(x_t,t)=0. Equality Phi1=zeta
requires e^(i x_t)=1; since |x_t|<pi, it forces x_t=0.
We have proved w1(0,t)=0 for EVERY 0<|t|<epsilon, and it also
holds at t=0 by hypothesis.

Now use the segment x=t, y between -|t| and |t|. Its endpoint
signs are the first and third inequalities in (6). The identical
intermediate-value argument gives H(t,y_t)=0. On this segment
Phi1 cannot equal zeta since its argument differs by t!=0, so
w1 is nonzero and w2(t,y_t)=0. Equality Phi2=eta forces y_t=0.
Hence w2(t,0)=0 for every |t|<epsilon, including the center.

### The whole zero set and the isolation obstruction

On U={|x|,|y|<epsilon}, the unit factorization ensures
G(Phi1)=0 iff w1=0. Its angular argument forces x=0, and the
previous paragraph gives the reverse inclusion for every point
of that fiber. This proves the first equality in (1). The second
follows in exactly the same way from the second coordinate and
w2(x,0)=0. Thus no other local contact component or zero label
has been omitted. Equation (2), with K nowhere zero, says q
vanishes exactly on their union. Elsewhere q is nonzero and real
nonnegative by hypothesis, hence strictly positive.

Every neighborhood of p contains noncentral points on both fibers.
An entire contact union locally equal to {p}, or a finite entire
contact census containing such a point, is therefore impossible.
This is a conditional local obstruction only. It does not construct
a nonisolated germ or change any global range, zero-data or sign
assumption. The argument allows arbitrarily flat scalar restrictions
and uses no constant-rank assertion away from p.

### Independent conceptual audit — 6 November 2026

The separate audit uses the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-06-l865-crossed-fiber-conceptual-audit.md`.
Its approved source coverage is reused without new browsing. The
standard factorization, first-order limit and intermediate-value
inputs are the precise citations above; the full-coefficient and
angular specializations are checked here. No substantive mathematical
defect or additional essential source requirement was found. This is
verification of the existing local input, not a new theorem, a germ
construction or an advance beyond the checked literature.

In (2), both unit factors come from the hypothesized exact double
orders of the nonzero entire G. Their local nonvanishing, the distinct
nonzero centers and J(p)!=0 allow one common neighborhood on which
every factor of K is nonzero. The sign -C and the squared difference
agree with L847's original angular orientation. In particular the
denominators and J have not been absorbed into an unjustified positive
constant. C2 regularity gives C1 J and K; continuity is all that the
normalization uses. No division by a vanishing wj occurs.

For (3), audited L864's real determinants are -|zeta|^2 b and
|eta|^2 c. Both ranks one therefore give b=c=0 and precisely the
two nonzero coefficients alpha=zeta(a+i), beta=eta(d+i). L864's
strict scalar condition at m=n=2 is K0 alpha^2 beta^2>0, with
the same K0 as (2). The leading polynomial is B0 x^2 y^2;
its value at (1,1) is strictly positive, not merely nonnegative
at a kernel direction. This import asserts no nearby constant rank
and no germ converse.

The definitions of B,H give B H^2=K w1^2 w2^2 exactly, including
at contacts. Since B(0)=B0 is positive real, continuity gives
Re B>B0/2 on a smaller neighborhood. If Re H=0, write H=ih
with h real; then Re q=-(Re B)h^2. The assumed full sign forces
h=0. Thus (4) uses the actual varying coefficient, and does not
require B to be real or choose a complex square root. The reality
of q will also be used for strict positivity off its zero set.

For (5), each wj is differentiable at the origin and vanishes there.
On every one of the three fixed lines, the two quotients by t have
the stated limits for t tending to zero from either side. Their
product divided by alpha beta is H/t^2, with limit rs. A single
epsilon is the minimum of the three two-sided limit radii and the
two coordinate radii of the preceding rectangle, also less than pi.
All segments in the proof then stay inside the same neighborhood.
No uniform estimate over a continuum of directions or high-order
Taylor expansion of the C1 density is required.

For clarity the endpoint signs on BOTH segments are as follows.
On y=t the ordered endpoints x=-|t|,|t| have signs (-,+) if
t>0 and (+,-) if t<0. On x=t the ordered endpoints
y=-|t|,|t| have exactly the same respective signs. These are
precisely the three inequalities (6); all inequalities are strict.
The real part of H is continuous on each closed segment, so the
cited intermediate value theorem applies with either ordering and
puts its zero in the interior.

On the horizontal segment, Phi2/eta has phase e^(it) multiplied
by a positive real number. Since 0<|t|<pi, Phi2 cannot equal eta
at any point of that segment. Consequently (4) and H=0 force
w1=0 at the intermediate point. There Phi1/zeta has phase e^(ix),
so |x|<pi forces x=0. This proves w1(0,t)=0 for every signed t
in the interval; the value at zero is the original contact. On the
vertical segment Phi1/zeta instead has fixed phase e^(it), excluding
w1=0 throughout it, and w2=0 at the intermediate point forces
y=0. This proves w2(t,0)=0 with the same epsilon. No scalar
nondegeneracy or transverse inverse enters either argument.

Finally, on that common open rectangle the unit factorizations give
G(Phi1)=0 iff w1=0 and G(Phi2)=0 iff w2=0. The angular restrictions
give the forward inclusions into x=0 and y=0. The fiber identities
just proved give the reverse inclusions at every point of the two
fibers. The coordinate images remain in the unit neighborhoods, so
no other G-zero label can contribute. Since K is nonzero, (2) also
makes the full density's zero set exactly this union, with no extra
diagonal or J zero; elsewhere q is nonzero and real nonnegative,
hence positive. Every neighborhood of the origin contains infinitely
many points of this union. This excludes a finite entire-contact
census containing the hypothesized contact, even if the rest of the
census has other local types.

These checks accept (1)–(6) and their stated C2 conclusion without
repair or strengthening. The direct mathematical inputs remain L847
and L864; count-only, moment, real-flux, single-contact and simple-pair
results are contrasts, not additional inputs. Other multiplicities,
other ranks, J(p)=0, actual zero configurations, global extension and
actual-Xi signs remain outside this audit. In particular, no
higher-multiplicity extension is proved by this acceptance.

## Mathlib

Full matching coverage for this actual-G crossed-fiber statement has
not been checked. The cited holomorphic factorization, differentiation
and real intermediate value theorem are mathematical inputs; no Lean
theorem names or formal verification are claimed. Unknown coverage is
not evidence of absence. The independent informal audit above is not
formal verification or a new Mathlib coverage check.
