# Conductor-eleven degree-five isogeny production — known construction assessed

TARGET: Construct and independently verify a degree-five quotient of L039's conductor-eleven curve using candidate kernel generator (5,5), then apply L045 to all twelve L043 generator values.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Vélu's exact title/year/pages, explicit normalized quotient formulas, kernel/degree and minimal-model criteria; compared the exact source equation against Sage 10.8's official isogeny examples. Narrow local comparison read L039 arithmetic, L043 hypotheses/twelve values, L045 transfer/audit and ATTEMPTS/023--024; no local instance-production duplicate was found in those checked paths.
SOURCE_EVIDENCE: Vélu (1971), §§2--3, equations (7)--(13), Remarks 2--3, pp.2--4 of Ghitza's English translation; Cremona (1997 corrected second edition), §3.1 pp.62--64, equations (3.1.2)--(3.1.3), Proposition 3.1.1, §3.2 pp.64--65 minimal-model algorithm and pp.66--67 Tate good/multiplicative exits; Sutherland Fall 2025 Lectures 2 §2.2 and 5 Corollary 5.2, Theorems 5.8/5.11/5.15 and Remark 5.16; Sage 10.8 EllipticCurveIsogeny exact 11a1 example and EllipticCurveHom.scaling_factor definition inspected. Audited L045 period/common-newform coverage is reused.
COMPARISON: Known formulas construct a normalized separable quotient over Q from a verified rational finite subgroup, and known model algorithms certify an integral globally minimal representative. Sage already documents a degree-five quotient of this exact source, so this is known-algorithm reproduction. The identified difference is independently certifying the specified candidate, complete rational map/model/differential witnesses and all twelve transferred denominators in the notebook's conventions.
GAP: Essential construction coverage is now available; candidate membership/order, full local map identities including exceptional points, target minimality, minimal-differential scalar and real-kernel evidence still require exact production/replay. No instance certificate, numerical period ratio or transferred value is established in this literature turn; arbitrary-curve BSD gaps remain independent.
REASON: Approve the saved finite target as a specialization of known construction and verification methods, retaining source qualifications and forbidding novelty or BSD-completion claims. Citation alone does not supply the notebook's independent finite witnesses.
LITERATURE_REASON: The saved target exceeds L045's previously granted-witness scope; its quotient construction, field of definition, candidate-order test and target minimality were essential unread inputs at invocation start.
SCOPE: The exact TARGET only, at L039's fixed rational model and candidate (5,5); rational group-law replay, characteristic-zero cyclic order-five Vélu quotient, full polynomial/map/exceptional-point and differential verification, integral target minimality with explicit coordinate transformations if needed, L045's odd-prime real case, and reduction of every L043 generator value. Existing source optimality/normalization qualifications remain. No composite-degree, uniform witness-production, coefficient, point-rank or complex-order theorem is approved.

The main gap remains arbitrary analytic order at least two versus rational
rank. This finite target could activate L045 on a nonoptimal model and
supply L027's normalization input. It cannot supply rational points of
infinite order, a coefficient certificate or complex-order comparison.

Essential local inputs are L039 source arithmetic, audited L043's twelve
full-relative values and audited L045. The source is
y^2+y=x^3-x^2-10x-20. The coordinate pair (5,5) remains a candidate to
test; this review does not establish its order or construct a subgroup.

## Inspected construction and verification coverage

[Jacques Vélu, *Isogénies entre courbes elliptiques*, C. R. Acad. Sci.
Paris Sér. A 273 (26 July 1971), A238--A241, English translation by
Alexandru Ghitza](https://aghitza.github.io/publications/translation-velu.pdf)
was read in §§2--3, pp.2--4. The hypothesis is a nonsingular general
Weierstrass equation and a finite subgroup F. Equation (7) defines the
two coordinates by sums over all nonidentity subgroup points. For the
expanded formulas (8)--(11), the summation set instead uses all points
of order two and one representative of each remaining pair Q,-Q.
Those two summation conventions must not be mixed. Equation (11)
retains a1,a2,a3 and specifies the new a4,a6. The proof uses group-law
expansions and the local parameters in (12)--(13). Remark 2 states the
invariant-differential identity for these chosen coordinates; Remark 3
requires a separable subgroup stable under conjugation for descent to
the base field. These are the imported construction and normalization
results; no general reproof is needed.

Applicability is conditional on the finite candidate test: characteristic
zero meets separability, and verified rational multiples provide the
required conjugation stability. This is not an assertion that those
multiples have been computed. The target equation's nonsingularity and
the coordinate maps must also be checked independently.

[Andrew V. Sutherland, MIT 18.783, Fall 2025, Lecture 5,
§§5.1--5.2](https://math.mit.edu/classes/18.783/2025/LectureNotes5.pdf)
was read for Corollary 5.2 (p.2), the statement and proof of Theorem 5.8
(pp.3--4), Theorem 5.11 and its quotient/descent proof sketch (pp.5--6),
and Theorem 5.15/Remark 5.16 (pp.7--8). These identify degree with
geometric kernel cardinality for separable isogenies, give the quotient
over the field of subgroup stability, and give the odd-order short-model
formulas. In that last convention the sum runs over all nonidentity
points, rather than Vélu's representatives. A rational coordinate change
to a short equation, its inverse and differential must be retained if
this alternate formula is used. The source's characteristic restrictions
are harmless over Q; short-model formulas are not to be applied directly
to the displayed long equation.

[Sutherland, Lecture 2, §2.2, pp.3--4](https://math.mit.edu/classes/18.783/2025/LectureNotes2.pdf)
supplies exact addition and doubling for a short equation over a field
of characteristic different from two and three, including identity,
inverse and vertical-tangent cases. The candidate can be tested after an
explicit checked coordinate change. Every required branch and rational
denominator must be retained; a torsion-table label or a zero numerical
division-polynomial value is insufficient.

[John Cremona, *Algorithms for Modular Elliptic Curves*, corrected second
edition (1997), §§3.1--3.2, pp.62--67](https://johncremona.github.io/book/fulltext/chapter3.pdf)
was read for the coordinate/invariant transformations (3.1.2)--(3.1.3),
Proposition 3.1.1, the full minimal-model algorithm on pp.64--65, and
Tate's good/multiplicative exits on pp.66--67. The input is an integral
nonsingular model or admissible integral invariants; the algorithm
handles the special factors two and three explicitly. It gives a
finite exact minimal-model procedure, not minimality from an isogeny
label. The discriminant transformation already used in L039 also permits
a direct minimality certificate if all integral discriminant valuations
are below twelve. Its threshold must be checked on the actual target;
source minimality cannot be transferred without evidence. For larger
valuations use the inspected minimal-model criterion, preserving the
full rational isomorphism, or record a failed instance attempt.

## Exact-model overlap and qualifications

The [SageMath 10.8 official isogeny manual, EllipticCurveIsogeny,
odd-degree rational example](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_curve_isogeny.html#sage.schemes.elliptic_curves.ell_curve_isogeny.EllipticCurveIsogeny)
documents this exact source and a degree-five target
y^2+y=x^3-x^2-7820x-263580, with kernel polynomial x^2-21x+80.
It compares point-list Vélu and polynomial-kernel Kohel constructions.
This is a published implementation example, not this notebook's verified
target equation or proof that (5,5) generates that kernel. It establishes
overlap and supplies an external comparison after independent recovery.
The same manual states the point-input and model-selection conventions;
passing a codomain may postcompose with an isomorphism. Consequently its
default normalization is not evidence about a separately minimalized map.

The [SageMath 10.8 morphism manual,
scaling_factor](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/hom.html#sage.schemes.elliptic_curves.hom.EllipticCurveHom.scaling_factor)
defines its scalar by pullback of the standard Weierstrass differentials
dx/(2y+a1x+a3). The approved replay must prove this identity for the final
specified minimal models. Vélu's Remark 2 only applies to its raw chosen
coordinates. Preserve every subsequent isomorphism and verify the final
pullback as a rational-function identity; do not infer its direction from
a software flag or reuse the raw scalar without checking model changes.

The extracted translation contains apparent inconsistent derivative
labels in §1 and denominator exponents in the displayed paired-x
expansion following (9), compared with (8). No erratum or corrected
general theorem is established here. These displays are not essential
inputs: use equation (7), the stated formulas (8)--(11), and independent
short-model coverage, with complete exact equation and differential
identities checked next turn. This verification justifies the finite
algebraic replay; it does not authorize an unrecorded general reproof.
The original French C. R. scan and Washington's Theorem 12.16 were not
inspected. Ghitza's direct translation and the independently inspected
primary exposition provide the stated coverage. Silverman PDF retrievals
returned internal errors; no Silverman passage is credited as inspected
or used as an essential new input.

## Approved attempt and stopping test

Import the known results by these precise citations in a future canonical
instance lemma, with hypotheses, qualifications and Mathlib status. The
permitted specialization is exact finite arithmetic and rational-identity
verification, with a complete disk certificate and a distinct replay if
scripts are used. It should record the candidate's actual order, all
subgroup points, every quotient coefficient and map, the geometric
kernel and exceptional-point treatment, nonsingularity, target integral
minimality, all coordinate changes and the final differential scalar.
Affine substitution alone does not certify an everywhere-defined
isogeny: retain the cited projective quotient theorem and verify that
the constructed formulas represent it, including the kernel and infinity.

Reuse audited L045 and its existing Dokchitser--Dokchitser Lemma 7.4/
Proposition 7.6 assessment for the real period identity and odd-prime
case. A verified full rational cyclic kernel is an eligible real-kernel
witness under that imported case; no independent period approximation
or component-count guess is needed. Only after the map, minimality and
pullback witnesses pass may L045 transfer the same full-relative
numerator and reduce all twelve audited L043 values, including zeros.
This approval includes that finite bookkeeping, not a new period theorem.

Continue if source coverage provides a finite exact verification procedure
for the generator, quotient map, degree, target minimality and pullback.
Abandon this specified instance if the candidate fails the order test or
its witnesses cannot be independently certified; preserve any evidence.
Once witnesses exist, use L045's real-case criterion and reduce all twelve
values. Agreement with a desired scale or the cited Sage example is
insufficient. A successful certificate would add one fixed normalization
input within known mathematics. It would leave coefficient production,
infinite-order rational points, Sha and complex-order comparison unresolved.
Matching full Mathlib coverage is not checked; the lecture's group-law
reference is supporting coverage, not a full quotient/period certificate.

This literature turn performs no candidate-order computation, constructs
no map, derives no lemma and writes no mathematical script. The assessment
approves the same saved target for a separate research turn.
