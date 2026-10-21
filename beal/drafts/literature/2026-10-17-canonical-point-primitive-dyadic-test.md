# Canonical global point under the primitive dyadic two-descent filter

TARGET: Determine whether the two-descent class of L062's fixed canonical whole-fiber point satisfies L082's primitive dyadic image condition.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused canonical-fiber and primitive-dyadic assessments; searched exact 9261/8/X0(11)/descent and 54a1/Kummer/canonical variants and checked L062, L069, L078, L082, history/266 and ATTEMPTS/014,034–037. No matching fixed-point membership theorem was identified; search details and scope comparison follow.
SOURCE_EVIDENCE: Inspected FNS final author manuscript June 10, 2019 Section 7.2 pp.25–29, canonical-fiber paragraph, (7.4), Lemmas 7.3/7.5/7.6 and relevant proofs; BPT arXiv:2001.02263v3 Section 1 p.3; Stacks Lemma 26.17.2/01JQ statement and proof; Clark Theorem 1.79 p.58; Bruin–Stoll March 14, 2008 Lemma 4.4 and full proof pp.7–8.
COMPARISON: General Kummer evaluation, affine base change, certified Hensel lifting and dyadic square comparison cover the fixed-point test without a primitive-scalar premise. Neither these sources nor L062/L082 imports its answer; FNS's restricted constancy and conditional global conclusions do not supply it.
GAP: Source scope is ready; the exact localized point, nonvanishing evaluations and both fixed-theta square-class comparisons remain uncomputed. No independent global-unit direction or rank improvement is certified.
REASON: Approve one explicit specialization of existing methods to the saved fixed point; do not extend L082's scalar formula, infer nonmembership from its scalar domain, or reprove general descent theory.
SCOPE: The single fixed P_sigma of L062 under L069's two-descent map, its entire dyadic localization and membership in L082; no full global unit basis, class computation, rank bound or integer exclusion.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes the scalar and global-point input; this separate comparison covers those changed hypotheses while reusing settled local arithmetic and source assessments.

## Original proposal, superseded by the completed source approval below

The exact Next action above preserves the proposed mathematical test;
this file does not approve or perform it. The next turn must be a
literature-only comparison, reusing the ready sources wherever adequate
and checking the changed hypotheses and relevant FNS proof cases.
The reason for that source turn is the changed scalar domain and global
point input, not a periodic refresh of L082's settled audit.

Essential inputs are L062's one Q-algebra identification sigma and
point P_sigma at j=9261/8, L033/L034's curve and entire modular map,
L046's fixed A2=Q2 × H, L069/L071's Kummer coordinates, L078's
whole cubic field and square test, and audited L082's exact image.
L047 supplies the canonical-fiber identification used by L062. All
identifications must be the localizations of the same sigma. There
is no cross-notebook input.

The main gap remains primitive integer emptiness. A certified exclusion
would show that this new necessary filter removes an actual global
two-descent point class; membership would retire this single witness
as a way to exhibit global removal. Either outcome is independently
testable without a class-group backend or a search for a full unit
basis. No implication for L077's remaining unit dimension is assumed:
the tested class need not be a new direction in the previously filtered
unit space. Full simultaneous class contributions and integer lifting
remain unresolved in either case.

Continue only with source coverage for the complete localized point,
fixed theta, all identifications and exact square-class comparison;
otherwise isolate the missing source hypothesis. A later approved
mathematical test must decide membership with a proof, rather than
compare scalar domains alone: distinct points/scalars can have the
same Kummer class. Preserve the five-isogeny survivor and the stopped
mechanisms in ATTEMPTS/014 and 034–037. Mathlib coverage is not checked.

## Completed source comparison — 2026-10-17

The main gap is global primitive integer emptiness. This single test
asks whether an actual global two-descent point class is removed by
the audited local condition; it does not ask for another local image.
The exact TARGET is unchanged. No membership calculation or new
mathematical assertion is made in this literature turn.

### Discovery, duplicates and reusable assessments

Reused the inspected canonical-fiber/localization coverage in
[the canonical-class assessment](2026-10-12-canonical-global-five-eleven-class.md)
and the general local methods in
[the primitive-image audit assessment](2026-10-17-primitive-dyadic-image-critical-audit.md).
The new queries were `"Freitas" "Naskręcki" "Stoll" "54a1" descent`,
`"9261/8" "descent" elliptic`,
`"9261/8" "X0" "11"`, `"54a1" "Kummer" "canonical"`, and
`"On 2-Selmer groups and quadratic twists" "Kummer"`.
Returned primary leads included the known BPT manuscript; several exact
queries returned irrelevant items. No exact fixed-point answer was
identified. This bounded search establishes neither novelty nor absence
of a stronger theorem elsewhere. No new essential unread lead remains.

L062 defines one point but its computed class uses fifth powers; L069
defines the different cubic map; L078 provides exact arithmetic for its
fixed local cubic; L082 supplies the comparison set. These do not
duplicate the proposed membership decision. History/266 records its
proposal only. ATTEMPTS/014 is the different five-isogeny filter;
034–036 exhaust prescribed supported-unit searches and 037 parks a
class backend. None decides this test or is reopened. All earlier
stop evidence and unfinished work remain in place.

### Primary statements and applicability

Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents
2, 3, n*, Compositio Math. 156 (2020), 77–113,
[final author manuscript, June 10, 2019](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, pp.25–29, was inspected at the canonical-fiber paragraph,
map, (7.4), Table 5 and Lemmas 7.3/7.5/7.6 with relevant proofs.
The canonical fiber consists of the twelve cyclic order-eleven
subgroups and is irreducible for the five listed curves. The model and
elimination polynomial are unconditional inputs. Table 5's Selmer
dimensions require GRH and are excluded. Lemma 7.3 assumes a
2-adically good j-invariant; Lemma 7.6 assumes a set in (7.2) other
than the cusp set and absence of local two-torsion. Its proof treats
ordinary disks and the four near-1728 parameterizations separately.
These are domain-dependent statements, not a theorem for arbitrary
canonical scalars. The approved alternative is direct fixed-fiber
evaluation using L034, rather than invoking those constancy conclusions
or a conditional global elimination. No new power-series construction
or formal-halving theorem is required.

Barrera Salazar–Pacetti–Tornaría, *On 2-Selmer groups and quadratic
twists of elliptic curves*,
[arXiv:2001.02263v3, September 17, 2020](https://arxiv.org/pdf/2001.02263v3),
Section 1, p.3, states the Kummer injection for a field of characteristic
different from two and a monic square-free cubic. The affine value is
the class of x(P) minus the distinguished generator when invertible.
There is no primitive-scalar, integrality-of-point or unramified-base
premise in this interface. Thus its field hypotheses cover Q2 and H
separately and the number field K. L069's origin-preserving coordinate
change and nonzero cubic discriminant are already documented inputs.
Use its X=4x coordinate and L078's same theta, not an independently
chosen cubic root. Invertibility at the tested point remains a research
obligation. Simon's number-field formulation is not substituted for
this general-field statement.

[Stacks Lemma 26.17.2, tag 01JQ](https://stacks.math.columbia.edu/tag/01JQ),
live statement and full proof inspected 2026-10-17, identifies the
affine fiber product with the spectrum of the tensor product. This
covers base change of L062's finite rational fiber and its fixed sigma.
The same evaluation must be transported through sigma tensor 1; the
explicit polynomial Kummer formula provides its localization without
assuming any equality between Selmer and global point classes.

Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields
and Adeles*, [161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
accessed 2026-10-17, revision date unidentified, Theorem 1.79, p.58:
for a complete nonarchimedean field, integral polynomial f and integral
approximation a with |f(a)|<|f'(a)|², there is a unique root b with
|b−a|<|f'(a)| and the stated residual/derivative error formula. This
covers exact root isolation only after checking each scaled equation's
integrality and strict inequality. Reuse L082's proved field-only
Aut_Q2(H) calculation when identifying the localization; its primitive
scalar root estimates are not transferred to the new scalar.

Bruin–Stoll, *Two-cover descent on hyperelliptic curves*, Math. Comp.
78 (2009), 2347–2370,
[author manuscript, March 14, 2008](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Section 4, Lemma 4.4 and full proof, pp.7–8, gives square-class
constancy under its polynomial-variation bound, using a strict square
neighborhood in the full extension. It includes dyadic residue
characteristic. Reuse that precision method and L078's already proved
exact valuation and square-label rules. A finite approximation alone
does not certify the class: bound its relative error strictly beyond
2v(2) in the appropriate field, or supply an exact square/nonsquare
certificate. No general local-image reproof or enumeration is needed.

### Approved bounded attempt and stopping test

Keep L062's fixed sigma, L047's entire canonical fiber, L033/L034's
complete map, L046's fixed Q2 times H, L069/L071's cubic coordinates,
L078's whole J and audited L082. Localize the same point, isolate and
reconstruct both factors at the one scalar, and justify the identification
with the fixed fields. Retain removable charts if encountered; do not
select independent local points. Establish nonvanishing or use the
correct exceptional Kummer evaluation. Compute the rational and ramified
square classes and decide membership in L082's displayed two-element
set, including the comparison with its fixed xi representative.

An exclusion would certify removal of this one actual global class
only. Membership retires this witness as a way to demonstrate removal.
Neither outcome alone improves L077's fourteen-dimensional unit bound
to eleven, decides the localized class contribution, bounds rank or
lifts primitive integer powers. Scalar nonadmissibility alone is not
the test because different scalars can yield the same class. If the
chosen coordinates cannot certify a root or class at the required
precision, record that specific obstruction without deciding membership;
a materially different mechanism needs separate source review.

SPECIALIZE approves this one calculation using known methods, with no
claim of progress beyond the sources checked. Mathlib coverage of this
fixed-point membership theorem and supporting interfaces is not checked;
unknown coverage is not absence. No lemma, mathematical script, DAG or
argument overview is changed in this source-only step.
