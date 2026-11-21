# Lemma 861: individual-divisor balances and a conditional four-cycle

## Hypotheses

Use the actual G,R,C,F and angular graph Phi_u of L847. Let u be
real C2, periodic on T2, and exchange symmetric:
u_1(theta_2,theta_1)=u_2(theta_1,theta_2). Require its complete density
q=F(Phi_u)J, J=det(I-iDu), to be real and nonnegative everywhere.
Assume the ENTIRE set where either G(Phi_u,1) or G(Phi_u,2) vanishes
is finite and nonempty. At every such point require a simultaneous
pair (zeta,eta) of distinct nonzero simple zeros of G and J!=0.
These are restrictions, not consequences of q>=0. No condition on
J away from these contacts, no collar and no RH is assumed.

For the conditional compatibility statement only, additionally
hypothesize four simple nonzero zeros zeta_1,...,zeta_4 of this actual
G, with pairwise distinct arguments alpha_1,...,alpha_4 modulo 2pi,
and, for ij=12,23,34,41, require

\[
 T_{ij}=\frac{G'(\zeta_i)G'(\zeta_j)(\zeta_i-\zeta_j)^2}
                  {\zeta_i\zeta_j},\qquad \Re T_{ij}\ne0.       \tag{1}
\]

No such actual quadruple is selected or proved to exist here. In
particular these conditional data must not be inferred from RH or
from the existence of one off-line zero. The compatibility assertion
below concerns a finite census and exact local germs, not a global u.

## Conclusion

For each zero label zeta attained by the first coordinate, ALL its
preimages obey

\[
 \sum_{\Phi_{u,1}(p)=\zeta}\operatorname{sgn}\partial_2u_1(p)=0.
                                                               \tag{2}
\]

The second coordinate has the corresponding zero sum of
sgn(partial_1 u_2). At every contact, writing
Du(p)=[[a,b],[c,d]], one necessarily has

\[
 d=a,\qquad bc=1+a^2,\qquad J(p)=2-2ia.                       \tag{3}
\]

Thus b,c are nonzero and have the same sign. Exchange preserves
this sign at the swapped contact. At least four different angular
directions and at least eight ordered parameter contacts are necessary.
These are conditional restrictions on this class of tori, not an
exclusion of that class or a statement about arbitrary G contacts.

Under the ADDITIONAL unverified zero-data hypotheses (1), a census
with exactly eight ordered contacts meets (2), the angular-fiber
alternation requirement, exchange, (3), and the full L860 conjugate
tangent/positive-density requirement. Every assigned contact admits
an exact local positive germ of the ACTUAL full form, with nonzero J;
exchange partners can be assigned exchanged germs. No global extension
or avoidance of other contacts by a global map is asserted. Thus the
listed constraints alone have a nonempty conditional solution; their
unconditional incompatibility cannot be claimed without further input
on actual zero data or global extension. The four/eight lower bounds
are attained at the level of this conditional assignment only.

## Proof

### Imported degree result and applicability

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-06-individual-divisor-contact-incidence.md`.
Import Gerald Teschl, *Nonlinear Functional Analysis*, version
23 June 2004, Sections 2.2-2.3, printed pp13-22, specifically
Theorem 2.4 (C1 regular-value signed-Jacobian formula) and
Theorems 2.1-2.2 and 2.11 (degree, admissible homotopy invariance,
and vanishing for a value outside the image), from the
[inspected primary manuscript](https://www.math.chalmers.se/Math/Grundutb/GU/MMA120/A14/lecture%20notes/Teschl%20G.%20Nonlinear%20functional%20analysis%20%28lecture%20notes%2C%20web%20draft%2C%202004%29%2874s%29.pdf).
The bounded open-domain, closure regularity and boundary-admissibility
checks follow below. No general degree theorem is reproved, and no
smooth closed-manifold formula is silently applied to C2 u. The
argument after degree is the problem-specific specialization and
finite compatibility test, not a claimed new degree theorem.

### Tangents and real orientations

At a contact (zeta,eta), L860 supplies real rank two for each
coordinate differential and
l_2=kappa conjugate(l_1), with kappa!=0 and K0 kappa>0, where K0
is exactly L860(3). On a real vector (x,y),

\[
 l_1=\zeta((a+i)x+by),\qquad l_2=\eta(cx+(d+i)y).
\]

Rank two of l_1 implies b!=0. Comparing the x and y coefficients
in the conjugate relation gives

\[
 \eta c=\kappa\bar\zeta(a-i),\quad
 \eta(d+i)=\kappa\bar\zeta b,
 \quad bc=(a-i)(d+i)=ad+1+i(a-d).
\]

All a,b,c,d are real; hence d=a and bc=1+a^2. This proves (3).
For the standard complex orientation on C and parameter orientation
dtheta_1 wedge dtheta_2, the real determinants are

\[
 \det_{\mathbb R}D\Phi_{u,1}=-|\zeta|^2b,\qquad
 \det_{\mathbb R}D\Phi_{u,2}= |\eta|^2c.                    \tag{4}
\]

For example before multiplication by zeta, the first real matrix is
[[a,b],[1,0]]. These real determinants are not the complex number J.
The two signs in (4) are opposite, as conjugation requires.

### Each individual value has total signed count zero

Fix an attained first-coordinate zero zeta. Its full preimage is
finite by the entire-contact-set assumption, and every point of it
is regular by L860 and (4); no subset of preimages is discarded.
Choose cuts theta_1=s and theta_2=t so neither cut contains a contact,
and s!=arg zeta modulo 2pi. Finitely many forbidden coordinates
permit this. On the bounded rectangle U=(s,s+2pi)x(t,t+2pi),
f=Phi_u,1 extends C2 to the closure. The entire boundary misses zeta.

Consider the C2 homotopy

\[
 f_\tau(\theta)=R\exp\big((1-\tau)u_1(\theta_1,\theta_2)
              +\tau u_1(\theta_1,t)+i\theta_1\big),
 \qquad 0\le\tau\le1.
\]

On the two horizontal sides periodicity makes this independent of
tau and equal to the original boundary values, which avoid zeta.
On the two vertical sides its argument is s, so it cannot equal zeta.
This proves admissibility on ALL of the boundary for ALL tau. At
tau=1 it is independent of theta_2 and equals the horizontal trace,
which avoids zeta everywhere; otherwise that trace would be a
boundary preimage. Hence deg(f,U,zeta)=0 by the imported theorem.
The signed-Jacobian formula and (4) give (2). For the second
coordinate freeze u_2 at theta_1=s instead, choose t!=arg eta, and
interchange horizontal and vertical in the same boundary check.
It gives the second zero sum. All maps and homotopies have the
required closure regularity; no regularity in excess of C2 is used.

There is also an angular ordering constraint. At first-coordinate
value zeta the preimages lie on theta_1=arg zeta and are exactly the
zeros of the periodic real function
h(t)=u_1(arg zeta,t)-log(|zeta|/R). Its derivative there is b!=0.
The sign changes from minus to plus at b>0 and from plus to minus
at b<0. Between consecutive roots it cannot change sign, since that
would give another root. Thus these derivative signs alternate in
the full cyclic order, including across the cut. This retains more
information than an unsigned count. The same statement holds for
the second-coordinate fibers.

### Exchange and the minimal census

The parameter point of a pair (zeta,eta) is necessarily
(arg zeta,arg eta); there cannot be two points for the same ordered
argument pair. Exchange gives the contact (eta,zeta) at the swapped
point and changes Du to P Du P, P=[[0,1],[1,0]]. Its b is the
original c, so (3) preserves sgn b. A diagonal angular point is
impossible: exchange symmetry there forces u_1=u_2 and hence
Phi_u,1=Phi_u,2, contradicting the distinct-pair restriction.

For this finite calculation only, associate an undirected edge to
each exchanged contact pair, joining its two angular directions and
giving it sign sgn b. There are no loops or multiple edges: angles
already determine the parameter point. Sum (2) over all attained
zero labels of a given argument. This includes every incident edge
exactly once at that angular vertex, and says its incident signs
sum to zero. Every nonisolated vertex therefore has even degree
at least two. With at most two vertices this is impossible for a
simple graph. With three, the only possibility is the triangle;
degree two would require opposite signs on consecutive edges at
each vertex, which is impossible around three edges. Thus there
are at least four angular vertices. The sum of degrees then gives
at least four edges, each representing two distinct parameter
points, proving the four-direction/eight-contact bounds. These are
signed real intersections; no positivity theorem for holomorphic
intersections is being applied.

### A conditional eight-contact assignment with exact local densities

Assume (1). Declare the unordered contacts 12,23,34,41 and their
swapped ordered partners, at the prescribed argument pairs. Give
edges 12 and 34 sign +, and edges 23 and 41 sign -. These eight
points are distinct and off the angular diagonal. Each individual
label has two first-coordinate occurrences with opposite signs,
and likewise for the second coordinate. Thus all individual-value
counts are zero, including the aggregate angular counts. On each
angular fiber its two roots have opposite signs and therefore obey
the full cyclic alternation condition, whatever the circular order
of the four distinct alpha_i. Other zero labels are assigned no
contacts and their empty counts are zero. This last declaration
describes a census, not a verified global avoidance property.

It remains essential to check that either assigned edge sign is
compatible with the ACTUAL full density, not just to prescribe free
signs. Use L860's exact construction at each unordered pair. In its
notation H0=C G'(zeta_i)G'(zeta_j)(zeta_i-zeta_j)^2/
(zeta_i^3 zeta_j^3), B0^2=H0, D=zeta_i zeta_j B0. Then

\[
 D^2=C T_{ij},\quad k_+=e^{i\pi/4},\quad k_-=ik_+,
 \quad \rho(k_+)=2,\quad \rho(k_-)=-2,\quad
 \lambda_0(k)=-\Im(k/D).                                  \tag{5}
\]

Both lambda_0 values are nonzero under (1). Indeed a zero would
make k/D real, hence k^2/D^2=(+i or -i)/(CT_ij) positive real,
which would force T_ij purely imaginary, contrary to (1).
Changing k to -k reverses lambda_0 without changing rho. For either
branch choose that sign so lambda_0 has the sign of rho. L860 then
gives EXACT density q=rho |W|^2/lambda, with lambda of constant sign
lambda_0, and nonzero J on an open angular neighborhood. This keeps
both G factors, the squared difference, denominators, J and the
original orientation, including at the contact.

At its center, the first coordinate is zeta_i+W before the angular
change. Its real determinant in angular parameters is 1/lambda_0.
Comparing with (4) gives

\[
 b=-\frac{1}{|\zeta_i|^2\lambda_0}.                         \tag{6}
\]

Thus branch k_- realizes b>0 and branch k_+ realizes b<0.
The L860 construction also supplies the complete conjugate tangent
and K0 kappa=rho/lambda_0>0, not merely the opposite determinant
signs. Equation (3) follows for these actual local germs as well.
No arbitrary prescribed tangent-extension theorem is invoked.

Assign the exchanged germ at the swapped contact. Explicitly replace
u(theta) by P u(P theta); F is symmetric in its two arguments and
det(I-iP Du P)=det(I-iDu), so its q is q(P theta). Nonnegativity
and nonzero J persist with the original angular orientation; the
sign b is preserved by (3). The eight distinct centers allow
pairwise disjoint small neighborhoods, chosen in exchanged pairs.
L860 ensures that within each neighborhood each G-contact set is
exactly its center, and q is strictly positive elsewhere there.

This completes the finite compatibility test, including full local
density, angular and exchange constraints. Extending these disjoint
germs to a periodic graph with q>=0 on their complement is an
independent unresolved problem. No such extension, actual quadruple,
forced contact, global torus or Xi sign has been obtained. In
particular the result neither refutes RH nor proves it. Retire only
a zero-data-independent no-go from these counts and jets; a decision
for actual G still requires the explicitly missing zero data or a
new global constraint. The older free-germ/gluing and total-phase
stops are unchanged. The independent conceptual audit below accepts
exactly these restricted and conditional conclusions.

### Independent conceptual audit, 6 November 2026

This audit uses the unchanged, separately approved SPECIALIZE assessment
`drafts/literature/2026-11-06-l861-incidence-audit.md`. It checks the full
proof against L847(1)-(3), the audited construction and all-rank converse
of L860, and the finite-domain degree hypotheses in the cited 23 June
2004 Teschl manuscript. All conclusions above are retained without
mathematical repair. No new degree theorem, actual zero data, extension
theorem or stronger sign assertion is imported or established.

**Contact tangents and all preimages.** At every point where either
pulled-back G vanishes, the explicit entire-contact-set hypothesis gives
exactly the nonzero, distinct, simple pair required by L860, and J is
nonzero there. Global q>=0 supplies its neighborhood sign hypothesis.
Its all-rank converse therefore applies to every such point, not just
a chosen list. For l1=zeta((a+i)x+by), real rank two forces b!=0;
the two coefficients in l2=kappa conjugate(l1) give
bc=(a-i)(d+i). Its imaginary part forces d=a, its real part gives
bc=1+a^2, and L847's exact determinant gives J=2-2ia.
Multiplication by a nonzero complex number has real determinant its
modulus squared, so the matrices [[a,b],[1,0]] and [[c,d],[0,1]]
give exactly the two signs in (4). Neither is the complex scalar J.

For an attained first-coordinate zero zeta, every preimage belongs
to the assumed finite contact set and is regular by this calculation.
Choosing each cut outside the finite set of contact coordinates, and
the first cut away from arg zeta, places all preimages in the open
rectangle and none on its boundary. Periodicity gives C2 extensions
to a neighborhood of its closure. At every homotopy time the two
horizontal sides equal the original avoiding trace; the two vertical
sides have the fixed argument of the first cut, different from arg
zeta. This checks all four sides and the corners for every time.
At the terminal time the whole image is the same avoiding trace.
Teschl's admissible homotopy invariance, zero degree outside the image,
and C1 regular-value formula therefore yield the complete zero signed
count. The determinant's minus sign changes that count to (2), still
zero. For the second coordinate choose its argument cut in theta2
and freeze u2 on the theta1 cut: vertical sides are fixed avoiding
traces, horizontal sides have the avoiding argument. Its determinant
has the plus sign in (4). No closed-manifold smoothness assumption or
unexamined preimage is needed.

**Ordering, aggregation and the minimum.** For a fixed zero label,
the radial exponential is injective on real log radii. Hence h=0
describes its complete fiber preimage, not merely a subset. Its roots
are simple since b!=0. On each intervening open arc h has constant
nonzero sign; continuity and the local sign change at a simple root
give alternating derivative signs even across the chosen cut. The
second-coordinate statement follows with c in place of b.

Angles determine the parameter point uniquely modulo 2pi. Exchange
changes b to c at the swapped point, preserving its sign because
bc>0. On the angular diagonal it instead forces both coordinate
values equal, which the distinct-pair hypothesis excludes. Thus
each unordered angular pair has at most one edge and there are no
loops. For each angular direction, summing the complete individual
counts includes every incident edge exactly once, even when different
zero labels share that direction. The sum of signs is zero, so every
vertex used has even degree at least two. One or two vertices cannot
meet that condition in a simple loop-free graph. With three vertices
all three degrees must be two; successively requiring opposite signs
on a triangle contradicts the requirement at its third vertex. At
least four vertices and, by summing degrees, four edges follow. Each
edge gives two distinct off-diagonal parameter points. This verifies
the four-direction/eight-contact bound without assuming distinct
arguments for all actual zeros or a positivity-of-intersections theorem.

**Both exact branches and the conditional census.** Under (1), put
Z=k/D and write Z=x+iy. For either k branch, D!=0. If lambda0=-y
were zero, Z would be nonzero real, so k^2/(C T_ij)=Z^2 would be
positive real. Since k^2 is i or -i, T_ij would be purely imaginary,
contrary to Re T_ij!=0. Thus both branches have a valid angular inverse.
Changing k to -k preserves rho=-2ik^2 and reverses lambda0; the
choice making rho/lambda0>0 is always available separately for each
branch. L860's common neighborhood shrink then preserves the inverse,
the sign of lambda, the distinct nonzero coordinates, nonzero J and
the isolated contact sets. Its exact pullback is rho|W|^2/lambda,
including at W=0. Positivity is not inferred from a quadratic preview.

At the center the first real coordinate determinant after the angular
inverse is 1/lambda0. Comparison with (4) gives (6), so k_- has
b>0 and k_+ has b<0. As an independent consistency check, L860(15)
gives J=2iZ/(-y)=2-2i x/y, with the required real part 2. Its
central conjugate multiplier is kappa=k/B0; using
K0=-zeta_i zeta_j H0 J gives K0 kappa=-2ik^2/lambda0>0.
This verifies the full tangent condition for both edge signs, beyond
opposite real orientation alone. Every original factor of the full
form is retained by L860's exact identity.

The four specified edges form a cycle with alternating signs. Each
label therefore has two first-coordinate occurrences of opposite sign
and two second-coordinate occurrences of opposite sign. Two simple
roots of opposite signs satisfy cyclic alternation regardless of the
order of the four distinct arguments. This is a check of the stated
finite constraint, not a construction of a periodic fiber function
avoiding all other actual zero labels. Under exchange, F is symmetric
and the Jacobian matrix is conjugated by P; hence q becomes q(P theta)
with its original angular orientation. The local positivity and sign
assignment persist. All eight centers are distinct, so paired disjoint
neighborhoods can be chosen, each containing just its specified local
G contact. No overlap compatibility is required for disjoint germs.

**Scope and status.** The minimum is necessary only under the stated
finite, nonempty, all-simultaneous-simple, distinct-pair and nonzero-J
contact restrictions. The attaining assignment is additionally
conditional on (1), which has not been verified for actual G. It
does not verify global avoidance of other zeros, interpolation between
neighborhoods, or q>=0 on their complement. In particular it does not
show that the restricted class of global tori is nonempty, nor that
it is empty. Its effect on the count-only route is conditional: these
listed constraints admit the prescribed assignment if the explicit
zero data hold. No actual-G counterexample or unconditional existence
claim follows. No collar, global restriction on J, C858b premise or
cross-notebook input has entered. The direct mathematical inputs remain
L847 and L860. This first independent audit validates a local input;
it supplies no new Xi sign or progress beyond the checked sources.

## Mathlib

Full matching coverage for this specialized balance/conditional-census
statement has not been checked. The cited degree theorems are standard
imported inputs; no Mathlib declaration or formal verification is
claimed. Unknown coverage is not evidence of absence. The literature
assessment did not settle the coupled calculation; POTENTIALLY_NEW
records that limited comparison, not certified originality.
The audit is REPRODUCTION and does not alter that coverage qualification;
no numerical script or formal proof was needed or claimed.
