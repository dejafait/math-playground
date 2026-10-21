# Marked octic two-cover support — primary-source assessment

TARGET: Certify a sufficient finite prime support for two-cover descent on L113's exact octic, retaining both rational infinity-point images.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the model, audit and marked-quotient assessments; checked L113's exact model/charts, ATTEMPTS/050–051 and history/395; searched the exact octic coefficient string and Bruin–Stoll support/infinity terminology. No matching instance certificate was identified; this is not a novelty claim.
SOURCE_EVIDENCE: Directly read Bruin–Stoll arXiv:0803.2052v2 (21 October 2008), Section 2 p.3, Definitions 4.1–4.2 and Lemma 4.3 p.6 with its containment proof pp.6–7, LocalImage infinity explanation p.11, and Section 6 pp.11–13 including the supported-representative and class/unit qualifications; reused prior Theorem 3.4/Section 8 coverage.
COMPARISON: The source covers squarefree even-degree nonmonic models and entire etale algebras; it supplies support containment and both exceptional-point conventions. It does not supply this polynomial's discriminant certificate, enumerate its supported classes or determine its rational points.
GAP: Perform only the exact instance support arithmetic and record both infinity rows under the cited map; class/unit arithmetic, local-image completeness, surviving-cover point control and all integer-lifting gaps remain independent.
REASON: Essential primary coverage is now ready for the unchanged bounded research target; import the general theorem and evaluation conventions, without reproof, and calculate only the missing instance certificate next turn.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED: prior construction/audit coverage did not extract Lemma 4.3's support hypotheses or the exceptional infinity convention. This turn supplies that missing coverage rather than repeating the model assessment.
SCOPE: Exactly TARGET for L113's squarefree octic over Q, retaining every etale factor, both smooth infinity points and the even-degree scalar quotient; exact discriminant/support arithmetic and theorem application only, with no field, maximal-order, class-group, full local-image or point-completeness assumption.

The main gap remains rational-point and ultimately primitive integer
control. A sufficient finite support certificate could make one later
two-cover computation precise without claiming it is executable or
complete. Inputs are audited L113, the L109 marking and L110–L111
original functions. Use the exact octic and its two known infinity
points, not the unmarked genus-two model or the different ordered twist.

The bounded research test is approved by the source comparison below.
This literature turn does not compute a discriminant, factorization,
support list or new lemma, and does not write mathematical scripts.

Independent gaps remain maximal-ring unit/class data, certified local
images, surviving-cover point control, degree-nine root recovery,
remaining factors, both L095 integer systems and minus-eleven.
Keep ATTEMPTS/050–051 and unfinished L108; neither an empty fake Selmer
set nor a rank-zero elliptic list can be the proposed success criterion.

## Primary result and exact conventions

Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370, DOI
[10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8).
The inspected primary version is
[arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2), dated
21 October 2008; page references below are its printed manuscript
pages, not unverified journal-page correspondences. Accessed 2026-10-21.

**Section 2, p.3.** The base field has characteristic zero, the curve
is the nonsingular projective hyperelliptic model of y²=f(x), and f is
squarefree. For even degree n, use the entire algebra A=k[x]/(f),
with theta the image of x, and

    H_k={delta in A*/(A*² k*): N_(A/k)(delta) in f_n k*²}.

This is a norm fiber, not in general a subgroup. For ordinary finite
points the map is mu(x,y)=[x−theta]. At a rational Weierstrass point
(a,0), write f(x)=(x−a) f_tilde(x); the stated replacement is
[(a−theta)+f_tilde(theta)]. At infinity, when f_n is a square in k*,
there are two rational points and the source defines
mu(infinity_plus)=mu(infinity_minus)=[f_n]=[1]. No y-sign is stored in
this fake class. The source explicitly gives
mu(C(k)) contained in Sel_fake^(2)(C/k), with the latter defined by
membership in the point images at every completion. These are imported
definitions and containment, not newly derived results here.

**Definitions 4.1–4.2 and Lemma 4.3, p.6; containment proof pp.6–7.**
For a nonarchimedean complete characteristic-zero local field with
finite residue field, a square class is unramified when its quadratic
extension is unramified. At odd residue characteristic this means even
valuation. For a product algebra this is required in every field
factor; for the scalar quotient it means that an unramified
representative exists. Lemma 4.3 assumes f in O[x], odd residue
characteristic, valuation of disc(f) at most one, and leading
coefficient a unit. It concludes that the entire point image consists
of unramified classes.

The first-part proof covers integral x using the root separation forced
by discriminant valuation at most one, including its possible ramified
quadratic pair. For nonintegral x it divides x−theta by the common
scalar x and obtains a square in every factor. Thus denominators of
points do not require a solution-dependent support. The source's
exceptional evaluations must also be retained; its LocalImage algorithm
in Section 4, p.11, explanation of steps 10–12 explicitly inserts the
infinity identity before treating reciprocal coordinates. In particular
one must not substitute zero into z(1−z theta) at reciprocal coordinate
z=0 and call that an invertible algebra representative.

The second part of Lemma 4.3 additionally requires a residue-size
inequality and gives equality with the unramified part of H_k. That
stronger part is unnecessary for a sufficient support certificate.
It is not an authorization to declare all local tests complete.

**Section 6, pp.11–12, with qualifications p.13.** The prescribed S
contains the infinite places, even-residue-characteristic places,
places of nonintegral coefficients, places where the leading
coefficient is not a unit, and places with disc(f) valuation greater
than one. The source asserts

    mu(C(k)) subset Sel_fake^(2)(C/k) subset H_k(S).

It also states that classes can be represented in the finite group
A(2,S) of square classes unramified outside S, followed by the scalar
quotient in even degree. Its computation requires unit and class data
of **all** simple factors. The explanation enlarges S to S' containing
generators for the relevant class-group 2-parts before using S'-units;
one must not silently replace A(2,S) by S-units alone. This imports
the supported-representative statement rather than attempting a new
local-to-global argument in this review.

Section 6 separately enlarges the tested places using the second part
of Lemma 4.3. Its p.12 explanation warns that omitting required local
tests can return a strict superset of the fake Selmer set. Finite
support containment is therefore different from a complete fake-Selmer
computation. Real-place signs and the scalar quotient remain relevant
to that later computation, even though no real-image calculation is
needed to certify a finite rational-prime support now.

## Applicability and comparison with existing work

L113 already proves squarefreeness, geometric integrality, degree eight,
genus three and smooth proper finite/infinity charts for the exact
polynomial G displayed in its conclusion. Its coefficients are integers.
Its existing infinity chart records G's leading coefficient as
3025=55² and the two rational points Z=+55 and Z=−55 at q=0.
Consequently the even-degree, square-leading-coefficient clause just
read is the applicable source convention. The exact specialized
evaluation rows should be recorded with the forthcoming certificate;
the two points remain distinct even though this convention identifies
their fake images. Neither a monic model nor an irreducible polynomial
is required. Do not divide G by a nonsquare constant to simplify it.

For Q, the source's sufficient set can be obtained from the exact
leading coefficient and polynomial discriminant, together with two;
the infinite place is tracked separately. A conservative superset
including every discriminant prime is permitted, rather than seeking
minimal support. The next step must actually certify the discriminant
and the asserted prime support. A nonzero resultant alone would not
certify its displayed prime factors. No maximal-order computation is
needed for that polynomial certificate; any later ideal valuations,
class groups or unit enumeration must use the maximal rings of every
field factor, rather than assume the polynomial order is maximal.

The earlier marked-quotient, model-construction and audit assessments
provide geometric inputs, not this arithmetic certificate. ATTEMPTS/050
stops a prescribed bounded rank-lower detector on the different
unmarked genus-two model; ATTEMPTS/051 stops rank zero for L111's
elliptic quotient. Neither contradicts support containment for L113.
The source's Section 8, already assessed in the model construction,
explains why covers can still help with a nonempty rational-point set;
it does not supply point completeness for this curve. Its Theorem 3.4
retains everywhere-local solubility and the hyperelliptic-involution
equivalence when interpreting fake classes as actual two-covers.
The point-support statement does not need a new proof of that theorem.

The exact-coefficient search found no inspected theorem or certificate
for this instance; irrelevant search hits were discarded. The support
mechanism itself is known and will be imported. Instance arithmetic is
reproduction/specialization, not evidence of a new general theorem.
Mathlib coverage of the full point-support theorem and exceptional
evaluation conventions was not checked; no absence claim is made.

## Bounded continuation and decision test

Use L113, including its completed independent audit, and preserve L109's
marking and L110–L111's original functions. In one research step import
the cited support theorem and evaluation rules, compute an exact
discriminant/resultant certificate for the unchanged G, verify any
claimed rational-prime factorization, and specify a sufficient finite
base-prime support whose extensions mean all maximal-ring places in
every etale factor. Retain the real place separately. Record both
infinity rows from L113's smooth chart and the corresponding source
evaluation, without changing the original boundary interpretation.
No etale-factor irreducibility decision, maximal-order basis, class
group, unit list, cover enumeration or point search is required.

Continue this prerequisite only if the complete exact certificate
verifies every displayed factor and the outside-support hypotheses of
Lemma 4.3, with both infinity rows retained under the even-degree map.
If a claimed prime support misses a factor or a convention fails to
match the exact chart, report the mismatch and leave that certificate
unproved; do not promote a finite sample or a polynomial-order
valuation to the required evidence. Completing support alone authorizes
no claim that the supported group or fake Selmer set has been computed.
An empty fake-Selmer criterion is incompatible with the known rational
boundary points and is not the intended success test.

The downstream possibility is a certified finite covering collection
for rational-point control on the marked curve. Independent unresolved
steps are maximal-ring unit/class arithmetic and local images,
surviving-cover rational points, degree-nine distinguished-root recovery,
compatibility of the remaining factors, both L095 integer power systems
and the minus-eleven alternative. None is assumed in approving this
strictly smaller target. No new mathematical lemma or instance
arithmetic was derived in this literature-only turn.
