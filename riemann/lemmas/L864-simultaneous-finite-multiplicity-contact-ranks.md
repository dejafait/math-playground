# Lemma 864: necessary ranks at simultaneous finite-multiplicity contacts

## Hypotheses

Use the actual entire G and positive R,C of L847, and exactly its form

\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2}.
\]

Conditionally fix distinct nonzero zeros zeta,eta of G of fixed finite
multiplicities m,n>=1. No actual multiple zero or selected pair is
asserted. On an open angular neighborhood of p=(arg zeta,arg eta),
using real argument lifts, let u be real C2 and put

\[
 \Phi_j(\theta)=R e^{u_j(\theta)+i\theta_j},\quad
 \Phi(p)=(\zeta,\eta),\quad J=\det(I-iDu),\quad q=F(\Phi)J.
\]

Require q real nonnegative on that whole neighborhood and J(p)!=0.
The orientation is dtheta_1 wedge dtheta_2. Write
Du(p)=[[a,b],[c,d]], and l_j=D Phi_j(p), as real-linear maps to C.
Let g1,g2 denote the holomorphic units in

\[
 G(\zeta+w)=w^m g_1(w),\qquad G(\eta+t)=t^n g_2(t),
 \quad g_1(0)=G^{(m)}(\zeta)/m!,\quad g_2(0)=G^{(n)}(\eta)/n!.
\]

For the global balance statement only, assume a real C2 periodic
exchange-symmetric u on T2, with q>=0 everywhere. Retain L861's
finite nonempty ENTIRE G-contact census: the whole set where either
G(Phi1) or G(Phi2) vanishes is finite and nonempty, and every point
of this union is a simultaneous pair of distinct nonzero G zeros
with J!=0. Replace simple zeros by arbitrary finite positive
multiplicities. These census restrictions are hypotheses, not
consequences of q>=0. No global extension or existence of such a
torus is assumed.

## Conclusion

Define the nonzero coefficient

\[
 K_0=-C\frac{g_1(0)g_2(0)(\zeta-\eta)^2}{\zeta^2\eta^2}J(p).
                                                               \tag{1}
\]

Neither coordinate differential has rank zero. Every hypothesized
contact satisfies one of the following two NECESSARY cases:

1. **Both real ranks two.** The multiplicities are equal, m=n, and
   l2=kappa conjugate(l1) for kappa!=0, with
   K0 kappa^m real strictly positive. In angular coordinates,

   \[
    d=a,\qquad bc=1+a^2,\qquad J(p)=2-2ia.                    \tag{2}
   \]

   In particular b,c are nonzero of the same sign, and the real
   coordinate determinants are -|zeta|^2 b and |eta|^2 c.
2. **Both real ranks one.** One has b=c=0, both m,n are even, and

   \[
    K_0[\zeta(a+i)]^m[\eta(d+i)]^n\in\mathbb R_{>0}.         \tag{3}
   \]

Mixed real ranks (one,two) or (two,one) are impossible. The second
case and (3) describe necessary leading-polynomial conditions only;
no exact germ, isolated-contact realization or sufficiency for the
full-neighborhood sign condition is asserted.

Under the additional global hypotheses, EVERY contact has both real
coordinate ranks two, and its two zero multiplicities are equal.
Consequently EVERY attained first-coordinate zero label zeta obeys

\[
 \sum_{\Phi_1(p)=\zeta}\operatorname{sgn}\partial_2u_1(p)=0. \tag{4}
\]

Those signs alternate in cyclic angular-fiber order. For EVERY attained
second-coordinate label eta, the corresponding sum of
sgn(partial_1 u2) also vanishes and its signs alternate. Both statements
include odd and even labels and count every preimage. Whole-preimage
regularity is now a consequence of the finite ENTIRE census and L866,
not an extra hypothesis. No singular local index is assigned. The
local rank-one necessary alternative remains valid without the global
census, and no germ existence is inferred from it.

The all-label strengthening and L866's accompanying direct normalization
are accepted by the separate composition audit below and the normalization
audit in L866. The older audit below accepted only the local classification
and then-qualified global balance.
No new global census bound, actual zero data, Xi sign or RH conclusion
follows from this strengthening.

## Proof

### Imported inputs and why a specialization is needed

The original local-classification SPECIALIZE assessment is
`drafts/literature/2026-11-06-simultaneous-multiple-contact-rank-scope.md`.
It covers necessary simultaneous-contact ranks and their regular-value
use. The subsequent all-label application uses the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-11-06-finite-census-all-label-balance.md`,
reusing those same sources and L866's audited fiber conclusion.
Import these previously inspected standard inputs:

- Jiri Lebl, *Guide to Cultivating Complex Analysis*, v1.10,
  5 November 2026, [Theorem 2.4.7, factorization proof/remark,
  pp49–50](https://www.jirka.org/ca/ca.pdf): finite holomorphic zero
  factorization. G is entire and G(0)>0 by L847, so is not identically
  zero; the hypothesized orders give the displayed nonzero units.
  For first-order differentiation use Lebl, *Basic Analysis I*, v6.3,
  15 May 2026, [Definition 4.1.1, p155, and Exercise 4.1.14,
  p161](https://www.jirka.org/ra/realanal.pdf#page=155), on each
  differentiable curve t -> Phi_j(p+t v). No higher-order surface
  Taylor theorem is used.
- Mateusz Michalek, *Algebraic Varieties*, 17 April 2018,
  [Example 7, p4](https://www.math.uni-konstanz.de/~michalek/april17.pdf#page=4):
  complex binary-form factorization, unique up to nonzero scalars and
  order, with conjugation preserving the projective factor multiset
  for real coefficients. Grigoriy Blekherman, Rainer Sinn, Gregory
  G. Smith and Mauricio Velasco, *Sums of Squares: A Real Projective
  Story*, Notices AMS **68** (2021), 734–747,
  [Section 3, binary-form paragraph, p742](https://ggsmith.ca/Papers/notices.pdf#page=9):
  real projective root multiplicities of a nonnegative nonzero binary
  form are even. Their stronger sum-of-two-squares conclusion is not
  needed. These are homogeneous statements, including the direction
  at infinity, rather than an affine-chart test.
- Gerald Teschl, *Nonlinear Functional Analysis*, 23 June 2004,
  [Theorem 2.4 and Sections 2.2–2.3, pp13–22](https://www.math.chalmers.se/Math/Grundutb/GU/MMA120/A14/lecture%20notes/Teschl%20G.%20Nonlinear%20functional%20analysis%20%28lecture%20notes%2C%20web%20draft%2C%202004%29%2874s%29.pdf):
  the C1 regular-value signed-Jacobian formula on a bounded open
  domain, with Theorems 2.1–2.2/2.11 for admissible homotopy invariance
  and degree zero outside the image. Singular-value sign sums are
  not imported.

No standard factorization or degree theorem is reproved. The needed
specialization checks the actual nonvanishing coefficient, C2
regularity, all coordinate ranks, original orientation and the whole
preimage of a value. L860's simple-pair converse and L859's single-even
result are scope comparisons only; neither is a mathematical input.
The global homotopy below repeats the explicit method in L861 to
check its application after the multiplicity hypothesis changes; its
simple-zero rank conclusion and four-cycle construction are not used.
For the strengthened global application, L866 is used only after the
local rank classification below. Its proof now derives its rank-one
normalization directly from its own hypotheses; it does not use any
conclusion of this lemma. Thus the composition is not circular.

### First-order tangent reduction with the full coefficient

Put w1=Phi1-zeta and w2=Phi2-eta. Shrink the angular neighborhood so
the coordinate values, their difference, g1(w1), g2(w2), and J are
all nonzero where these are coefficient factors. Continuity and the
center hypotheses permit this. L847's complete formula factors as

\[
 q=w_1^m w_2^n K,\qquad
 K=-C\frac{g_1(w_1)g_2(w_2)(\Phi_1-\Phi_2)^2}
                  {\Phi_1^2\Phi_2^2}J,\qquad K(p)=K_0\ne0. \tag{5}
\]

Only continuity of K is required; C2 u gives C1 J. For every fixed
v in R2, differentiability gives wj(p+t v)/t -> lj(v) as t->0+.
The domain is open, so this holds for every direction. Taking finite
integer powers in (5) therefore gives

\[
 P(v):=K_0 l_1(v)^m l_2(v)^n
       =\lim_{t\to0+}\frac{q(p+t v)}{t^{m+n}}
       \in\mathbb R_{\ge0}.                                \tag{6}
\]

No derivative of q of order m+n is used. In particular no C^(m+n)
surface assumption is hidden here. In the original angular basis,

\[
 l_1(x,y)=\zeta((a+i)x+b y),\quad
 l_2(x,y)=\eta(c x+(d+i)y),\quad
 \det_{\mathbb C}(l_1,l_2)=-\zeta\eta J(p)\ne0.            \tag{7}
\]

Each row is nonzero by its own-angular imaginary coefficient.
They are also distinct up to complex scalar, by (7). The polynomial
P is thus a nonzero homogeneous polynomial of degree m+n. Its
imaginary part vanishes at every real (x,y) by (6), hence all of that
polynomial's real coefficients vanish; P has real coefficients and
is nonnegative. Also m+n is even: choose v with P(v)>0 and use
P(-v)=(-1)^(m+n)P(v)>=0. This checks the hypotheses for both
binary-form inputs, including nonzeroness and even total degree.

### All four rank combinations

A nonzero complex-valued real-linear form l has real rank one
exactly when it is a nonzero complex scalar times a nonzero real
linear form; equivalently its projective complex factor is fixed by
conjugation. Indeed a one-dimensional real image is a real line in C,
and scaling that line to R proves the assertion in both directions.
Otherwise l has real rank two and l,conjugate(l) represent distinct
projective factors. From (7) or its real matrices,

\[
 \det_{\mathbb R}l_1=-|\zeta|^2 b,\qquad
 \det_{\mathbb R}l_2= |\eta|^2 c.                           \tag{8}
\]

If both ranks are two, conjugation must permute P's two distinct
projective factors. Neither is fixed, so it exchanges them, and their
multiplicities must agree. Thus m=n and l2=kappa conjugate(l1) with
kappa!=0. Substitution into (6) gives
P=K0 kappa^m |l1|^(2m). Since l1 is onto C, this is nonnegative and
nonzero exactly when K0 kappa^m is real strictly positive.

Comparing x and y coefficients in this conjugate relation gives

\[
 \eta c=\kappa\bar\zeta(a-i),\qquad
 \eta(d+i)=\kappa\bar\zeta b,
 \quad bc=(a-i)(d+i)=ad+1+i(a-d).
\]

Here b!=0 by (8). Reality of a,b,c,d gives d=a and bc=1+a^2.
Consequently det Du=-1 and tr Du=2a, proving (2) and both signs.

If one rank is one and the other two, the rank-one factor is fixed
by conjugation. The rank-two factor is not fixed, and its distinct
conjugate is not the fixed factor. P would therefore lack a required
factor. This contradicts real coefficients, for either mixed order.

If both ranks are one, (8) says b=c=0. The forms in (7) are then
zeta(a+i)x and eta(d+i)y. Their two distinct projective real factors
must each have even multiplicity by the imported nonnegative-form
parity result. Thus m,n are both even. Formula (6) becomes a scalar
times x^m y^n; its value at (1,1), nonzero by (1), must be strictly
positive. This is precisely (3). Conversely these parity and scalar
conditions make this LEADING POLYNOMIAL nonnegative; this observation
makes no assertion about higher terms of q or exact realizability.
These alternatives exhaust the nonzero real ranks.

### Finite entire census excludes every singular preimage

Let S be the ENTIRE set where G(Phi1)=0 or G(Phi2)=0 on the torus.
Fix any p in S. The global hypotheses give simultaneous distinct
nonzero labels at p, each of fixed finite positive order, and J(p)!=0.
A small lifted angular neighborhood has real C2 u and full real
q>=0; thus the local classification just proved applies there. Zero
ranks and mixed ranks have been excluded. If both ranks were one,
both orders would be even and at least two. These are precisely L866's
local hypotheses, with the same G,R,C,F,J and original orientation.
No rank condition away from p, constant-rank theorem or high-order
surface regularity is needed.

L866 gives both complete angular contact fibers in some open rectangle
about p. Choose that rectangle smaller than one angular period, so
its infinitely many first-fiber points are distinct points of T2.
They all belong to S, contradicting its assumed finiteness. The
contradiction concerns the ENTIRE union: it would not follow by
counting only the simultaneous intersection of the two fibers. The
local radius may depend on the two orders and on p; one such radius
at a hypothesized singular point suffices. Thus both coordinate ranks
are two at every p in S, and the local classification also gives
equal orders, (2), and nonzero b,c of the same sign there.

For any attained zero label zeta of the first coordinate, EVERY
preimage of zeta belongs to S by its definition. The preceding
argument applies at each preimage, even if its second label varies.
Hence zeta is a regular value of the first coordinate map, with a
finite full preimage. The same reasoning holds for every attained
second-coordinate label. This establishes regularity before applying
any degree formula and makes no assertion about J away from S.

### All-label regular-value sign balance

Under the additional global hypotheses, fix an attained first-coordinate
zero label zeta. The preceding argument establishes regularity of its
entire preimage and b!=0 there, as well as (2).
Choose angular cuts theta1=s, theta2=t missing the entire finite
census and s!=arg zeta modulo 2pi. On the bounded rectangle
U=(s,s+2pi)x(t,t+2pi), Phi1 is C2 on the closure and the whole
boundary avoids zeta. Consider

\[
 f_\tau(\theta)=R\exp\big((1-\tau)u_1(\theta_1,\theta_2)
                 +\tau u_1(\theta_1,t)+i\theta_1\big),
 \qquad 0\le\tau\le1.                                    \tag{9}
\]

The horizontal boundary values are unchanged by periodicity and avoid
zeta. The vertical boundary has argument s and also avoids zeta for
all tau. These statements include the four corners. Continuity on
the compact boundary times [0,1] gives positive separation from zeta.
The maps extend C2 to a neighborhood of the closed rectangle, and
the homotopy is continuous there with the stated C1 regularity.
At tau=1 the map is the horizontal trace, independent of
theta2; its image misses zeta because the entire horizontal boundary
does. Teschl's admissible homotopy and outside-image properties give
degree zero. Every preimage is regular, so the signed-Jacobian formula
with (8) gives minus the sum in (4) equal to zero. This proves (4).
For an attained second-coordinate label eta choose t!=arg eta and use

\[
 \widetilde f_\tau(\theta)=R\exp\big((1-\tau)u_2(\theta_1,\theta_2)
                  +\tau u_2(s,\theta_2)+i\theta_2\big).
\]

The cuts can again avoid the full finite S. The vertical traces
are fixed by periodicity and miss eta, while the horizontal sides
have argument t and avoid eta for every tau. This covers the corners
and gives uniform boundary separation by compactness. The terminal
map is the avoiding vertical trace, and the same C2 closure regularity
holds. The degree is zero by the same cited properties. Every preimage
is regular by the preceding whole-census argument. Formula (8) gives
the corresponding sum of sgn c equal to zero. Exchange symmetry is
not required for these two applications, but has not been removed
from the stated global comparison.
The real target plane has its usual (Re,Im) orientation throughout;
the complex J is not used as a real coordinate determinant. These
degree sums count preimages of Phi_j, without weights from the orders
of the zeros of G.

On a first-coordinate fiber the preimages are exactly the roots of
the real periodic function
h(y)=u1(arg zeta,y)-log(|zeta|/R). Its derivative is b!=0 at every
root, so its signs change alternately from negative to positive and
positive to negative in the full cyclic order. Between consecutive
roots the sign cannot change, by continuity and absence of another
root. This proves the claimed alternation, including across the cut.
The second-coordinate proof uses c on its angular fiber.

No parity distinction remains in this global argument: the finite
entire census excludes the only singular rank alternative even for
even labels. If that census is relaxed, a singular preimage would
still invalidate the cited regular-value formula; this proof neither
omits one nor assigns it an index. In particular it does not extend
to J=0, diagonal pairs, or a merely finite simultaneous subset.

This is a local specialization of standard factorization and degree
inputs, recorded as REPRODUCTION. It extends the necessary contact
information beyond simple pairs; it is not a claim of originality
beyond the inspected sources. Actual multiple zeros, realization of
the singular leading case, global extension and actual-Xi all-degree
mixed positivity remain unresolved. Count-only, two-unweighted-moment
and singular real-flux route stops are not removed. No new numerical
or mathematical script is needed. The all-label application is likewise
REPRODUCTION of a composition of existing local results and imported
degree theory, not progress beyond the sources checked. The separate
critical review below accepts this composition at exactly its stated scope.

### Independent conceptual audit, 6 November 2026

This historical audit precedes the all-label strengthening. Statements
below about a still-qualified global conclusion describe that earlier
version; that earlier audit did not cover the new composition with L866
or its direct normalization rewrite. Its accepted local classification
is unchanged; the later composition audit follows below.

The unchanged invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-06-l864-multiple-contact-conceptual-audit.md`.
This audit independently checks (1)--(9), reusing its inspected
factorization, conjugation/parity and C1 degree inputs. It finds no
mathematical defect in the stated necessary classification or the
qualified whole-preimage balance. The explicit entire-union definition
and even-total-degree check above clarify existing hypotheses and an
already implicit source-applicability step; no hypothesis is relaxed
and no conclusion is enlarged. This is REPRODUCTION, not a claim of
progress beyond the cited standard mathematics.

For (1), (5) and (6), distinctness of the two nonzero centers, the
two nonzero holomorphic units, C>0 and J(p)!=0 make every coefficient
factor nonzero on one sufficiently small neighborhood. Only w_j(p)=0,
first-order differentiability and continuity of K enter the limit.
The positive t denominator works for every direction v; v and -v
are both available because the domain is open. Points on a kernel
line may have P(v)=0 without invalidating the limit or proving an
exact zero curve. Thus arbitrary fixed m,n require no high-order
derivative of the C1 density.

For (7), direct expansion gives
zeta eta[(a+i)(d+i)-bc]=-zeta eta[1-ad+bc-i(a+d)],
which is -zeta eta J. The imaginary own-angle coefficients exclude
zero rows, while J!=0 excludes proportional rows. Products of these
nonzero linear polynomials cannot be the zero polynomial. The
conjugation argument therefore concerns exactly two distinct
projective factors, with their actual multiplicities; it does not
identify literal normalized factors or discard the direction at
infinity. In the two-rank-two case the conjugate factors must be
exchanged. In either mixed case the nonreal factor's conjugate is
missing. In the two-rank-one case b=c=0 makes the distinct real
factors x,y explicit, and each has even multiplicity. The positive
scalar conditions follow by evaluating a nonzero value of P, not
from a weak inequality at its zero. These checks exhaust all ranks.

For (2) and (8), multiplication by zeta or eta has positive real
determinant |zeta|^2 or |eta|^2. The unscaled matrices are
[[a,b],[1,0]] and [[c,d],[0,1]], giving respectively -b and c.
Conjugate-coefficient comparison then gives a=d, bc=1+a^2,
det Du=-1 and J=2-2ia, with no choice of angular orientation left
implicit. The complex J is never substituted for either real
coordinate determinant.

For (4) and (9), the explicit entire-union hypothesis ensures that
every preimage of the chosen zero label lies in the finite census.
Finitely many forbidden angular coordinates permit both cuts.
For every homotopy parameter the horizontal sides stay equal to
the original trace by periodicity, and the vertical sides have
argument s different from arg zeta. Compactness of the boundary
times [0,1] also supplies positive separation from zeta. The
terminal image is precisely that avoiding horizontal trace, so its
degree is zero. The maps extend C2 to a neighborhood of the closed
rectangle, sufficient for the cited C1 formula. Only after checking
regularity at every preimage does (8) give the zero sum with its
minus sign. Freezing theta1 proves the second-coordinate statement
with plus sgn c. Neither argument needs J!=0 away from contacts.

The cyclic alternation uses all roots of the periodic scalar fiber
function; regularity makes each root a sign change, and continuity
prevents any additional sign change between successive roots. For
an odd-order label, each contact independently excludes the even/even
rank-one alternative, so the full preimage is regular and has equal
orders. For an even label, one singular preimage invalidates the
regular-value sign formula at that value even if all other preimages
are regular. The same boundary homotopy still gives degree zero;
this audit assigns no singular local index and omits no preimage.

The continuation test is met only for these necessary conditions.
The rank-one leading polynomial is not an exact C2 germ, an isolated
contact, a finite census, or a global extension. Actual multiple-zero
data, singular realization and actual-Xi signs remain open. The sole
local mathematical input is still L847; L861 supplies a method to
recheck, not a simple-zero theorem used outside its hypotheses.

### Independent all-label composition audit — 6 November 2026

Use the unchanged invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-06-all-label-balance-composition-audit.md`.
This RESEARCH / proof_audit / REPRODUCTION step accepts the strengthened
conclusion with no substantive repair, relaxed hypothesis or new lemma.
It verifies an existing conditional input, not new mathematics beyond
the sources checked. Teschl's 23 June 2004 Theorem 2.4 and the stated
admissible-homotopy/outside-image properties are imported with the
precise finite-regularity scope above, not reproved or replaced by a
singular-index formula. The earlier primary-read records are adequate.

First, the separately recorded normalization audit in L866 checks its
current proof directly from L847 and its own local hypotheses: both
real ranks one imply b=c=0; the nonzero coefficient and positive-ray
limit give B0>0. Its existing signed-segment argument then gives the
two complete fibers. It uses no conclusion of this lemma. In this
lemma, the local classification preceding the global argument uses
only L847 and the cited factorization/binary-form inputs. Thus there
is no circular use between that classification and the fiber theorem.

Now fix ANY point of the entire finite union S. The global hypotheses
give a lifted open C2 neighborhood, real nonnegative full q, distinct
nonzero labels of fixed finite orders, and J!=0 at its center. These
are exactly the local classification hypotheses. A zero rank is
impossible from the own-angle derivatives; mixed ranks are excluded
by that classification. If both ranks are one, both orders are even
and at least two. Every L866 hypothesis then holds, without a rank
condition away from this point or a uniform neighborhood over orders.
One of its complete fibers already contains infinitely many distinct
torus points in a rectangle of width less than one period. Each point
belongs to S, a contradiction. This uses the entire OR union, not
just the simultaneous intersection. Hence both coordinate ranks are
two at every point of S, with equal orders and b,c nonzero of the
same sign. All preimages of every attained coordinate zero label
lie in S even when the other label varies. Whole-preimage regularity
is therefore established before degree is invoked.

For the first coordinate choose s outside the finite first-coordinate
projection of S and different from arg zeta, and t outside its finite
second-coordinate projection. Periodic cuts then place every preimage
strictly inside the rectangle. On theta2=t and theta2=t+2pi, (9)
equals the original avoiding trace for all tau; on theta1=s and
theta1=s+2pi its argument is s, so it cannot equal zeta. The corners
obey both descriptions. This checks avoidance on the entire boundary
times [0,1]; its compactness yields a strictly positive distance from
zeta. The periodic C2 lift supplies C2 maps on a neighborhood of the
closed rectangle, and the displayed homotopy is jointly continuous
there. The terminal image is the whole avoiding horizontal trace.
Thus its degree and the original degree are zero. In the original
(theta1,theta2) and (Re,Im) orientations the real determinant at a
preimage is -|zeta|^2 b, so the regular-value formula gives (4).

For the second coordinate choose t also different from arg eta and
both cuts missing S. The two vertical sides of the second displayed
homotopy stay equal to the avoiding original vertical trace. The two
horizontal sides have argument t for every tau and miss eta. Corners,
compact separation and C2 extension follow with these exact sides.
The terminal image is the avoiding vertical trace. Its zero degree
and determinant +|eta|^2 c give the second zero sum. These checks
require no regularity during the homotopy, no nonvanishing J away
from S and no weighting by a G-zero multiplicity.

Finally, each first-coordinate preimage is exactly a root of the
displayed periodic real h on its complete angular fiber. Every root
has h'=b!=0, hence is a sign crossing. The sign is constant on each
open interval between consecutive roots, since another change would
give an omitted root by the IVT. Periodicity gives the same conclusion
on the last interval across the cut. The derivative signs therefore
alternate around the whole cycle (in particular its nonempty number
of roots is even). For the second fiber h'=c and the same complete
root argument applies. No label or endpoint is omitted.

All stated continuation tests are met for the conditional all-label
balance. This neither relaxes J!=0 or distinctness nor replaces the
finite ENTIRE union by a finite simultaneous subset. It supplies no
actual zero configuration, global graph, new census lower bound or
actual-Xi sign. The count-only, unweighted-moment and incomplete
singular real-flux failures remain unchanged. The current direct
mathematical uses in DAG are accurate; no edge change is needed.

## Mathlib

Full matching coverage for this actual-form multiplicity/rank and
regular-value specialization has not been checked. The binary-form
factorization and degree results above are imported standard inputs;
no matching Mathlib declaration or formal verification is claimed.
Unknown coverage is not evidence of absence.
