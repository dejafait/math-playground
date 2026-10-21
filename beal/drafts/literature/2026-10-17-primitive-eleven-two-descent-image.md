# Primitive eleven-adic two-descent image — completed source assessment

TARGET: Determine the exact primitive whole-fiber two-descent image at eleven for L033's 54a1 branch, using all three base factors and one common primitive scalar.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L041/L042/L044/L069/L073, the ready eleven-adic and primitive-dyadic assessments, and ATTEMPTS/014,033–037; searched exact 54a1/eleven-adic and X0(11)/two-descent terms, restricted-image terminology and the stronger (2,3,11) classification. Useful primary matches were FNS and general local descent methods; no inspected result gives this exact correlated set. Queries and inspected scope are recorded below; no novelty inference.
SOURCE_EVIDENCE: Reopened BPT arXiv:2001.02263v3 Section 1, especially Lemma 1.3/Remark 1.4 and Definition 1.6/Theorem 1.8; Bruin–Stoll 14 March 2008 manuscript Section 2/Remark 2.1, Section 4 Lemma 4.4 with its proof and all SquareClasses/LocalImage cases, and Section 9; FNS 10 June 2019 final author manuscript Section 7.2, equation (7.4), Lemmas 7.5–7.6 and their proofs, with its GRH boundary. Reused the documented Clark Hensel/Eisenstein coverage; precise URLs and locators appear below.
COMPARISON: General full-cubic Kummer and bad-prime square-neighborhood methods cover a bounded specialization, but unrestricted image sizes, five-isogeny vectors and FNS's dyadic constancy lemma do not compute this correlated eleven-adic image. The difference to prove is the simultaneous full-fiber restriction, retaining unit classes, the fixed generator and every identification; no new general descent theorem needs reproof.
GAP: Essential method coverage is adequate; uniform class constancy or another exhaustive finite reduction, exact full-fiber realizations, all embeddings and any subgroup status remain mathematical obligations. No restricted image, additional codimension, class-kernel value, rank bound or integer exclusion is established by this review.
REASON: Approve one subsequent REPRODUCTION proof attempt on the unchanged target using cited general inputs and existing local arithmetic. No essential source blocker remains for that attempt; do not import FNS's conditional global Selmer data or assert that a generic local algorithm already preserves the common scalar.
SCOPE: Fixed K,E0,g,theta and ordered full eleven-adic algebra of L033/L041/L069/L073, with the common primitive scalar domain of L044; no changed twist, global class computation or assumed subgroup closure.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED: its correlated restriction at a bad-reduction odd prime lay outside the ready unrestricted and primitive-dyadic assessments. This turn completes that essential comparison, without repeating their calculations.

## Completed comparison — 2026-10-17

The original proposal below is preserved as historical specification;
its statements about uncompleted review describe its startup state.
This section supplies source approval only. No local image has been
computed in this turn, and no lemma or mathematical script was changed.

### Primary results and applicability limits

**Barrera Salazar–Pacetti–Tornaría**, *On 2-Selmer groups and quadratic
twists of elliptic curves*, Math. Res. Lett. **28** (2021), 1633–1659,
[arXiv:2001.02263v3, 17 September 2020](https://arxiv.org/pdf/2001.02263v3),
Section 1, pp.3–6. The setup is a monic square-free cubic over a field
of characteristic different from two; its entire cubic algebra may
split. Lemma 1.3, p.4, gives

    |delta_F(E(F))| = [O_F:2 O_F] |E(F)[2]|

for every finite extension F/Q_p. It does not assume the later
unit-containment alternatives. Remark 1.4 retains maximal integer
rings in all factors. Definition 1.6/Theorem 1.8 have additional
hypotheses and cannot be used as an unconditional unit-image shortcut.
Their split, quadratic-factor and reduction cases were inspected.
This covers the general full-image input of L073 over both kinds of
base factor, not the size or group structure of the restricted set.
Independent spanning or exhausting the full local group would not
prove whole-fiber realization of its elements at one scalar.

**Bruin–Stoll**, *Two-cover descent on hyperelliptic curves*, Math. Comp.
**78** (2009), 2347–2370,
[14 March 2008 author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf).
Section 2/Remark 2.1, p.3, uses the full algebra modulo squares in
odd degree: for f=(X-a)h, the root-point value is
[(a-theta)+h(theta)], and monic infinity has value one.
Section 4 assumes a characteristic-zero complete local field with
finite residue field, integral square-free f, and its full irreducible
factorization. Lemma 4.4, pp.7–8, requires irreducible h, integral x0,
e>=0 and the coefficient inequality

    ord(h(x0+epsilon*pi^e)-h(x0)) > ord(h(x0)).

It proves square-class constancy on x0+pi^(e+ord(4)) O.
Read all recursion, realization, root-neighborhood and reciprocal cases,
pp.8–10, and the genus-one identification, Section 9, p.15. Bad
reduction is allowed; the correlated restriction requires separate proof.

**Freitas–Naskręcki–Stoll**, *The generalized Fermat equation with
exponents 2, 3, n*, Compositio Math. **156** (2020), 77–113,
[final author manuscript dated 10 June 2019](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, equation (7.4), Lemmas 7.5–7.6 (PDF pages 25–29, numbered
from one). The field-transport paragraph identifies the twelve-subgroup
fiber; the modular formula is the input already imported in L033/L034.
The following global Selmer computation explicitly assumes GRH and is
not imported. Lemma 7.6 assumes a finite extension of Q2 without
rational two-torsion and specified non-cusp dyadic domains. Its
statement and both proof cases were read; no eleven-adic application
follows. Lemma 7.5 was read, without asserting its convergence
hypotheses here. Theorem 7.1's stronger classification remains conditional.

**Local-field inputs reused.** The ready eleven-adic containment and
audit assessments document Pete L. Clark,
[Algebraic Number Theory II notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
161-page version without identified revision date: Theorem 1.75/Remark
1.76 p.57, Theorem 1.79 p.58, Proposition 2.9/Corollary 2.10 p.65.
This review reuses that inspected complete-DVR, strict Hensel–Newton,
coprime-factor and Eisenstein coverage. It does not claim a new read
of those notes. Require the actual derivative/coefficient inequalities;
no eleventh-root surjectivity or maximality from repeated reduction.
The local field version is also recorded in foundation 17.

### Discovery, duplicate and failure check

Web queries actually made included `"X0(11)" "2-descent" local image`,
`"54a1" "descent" eleven`,
`"The generalized Fermat equation with exponents 2, 3, n" "7.2"`,
`"two-cover descent" "LocalImage" restricted p-adic`,
`"54a1" "11-adic" descent`,
`"X0(11)" "local" "square" "11"`,
`"x^2+y^3=z^11" unconditional proof`, and
`"primitive" "whole-fiber" "two-descent" eleven`.
The useful exact-family primary match was FNS; broad searches also
returned unrelated elliptic-curve material. No inspected theorem
settled this exact local set. Search snippets and unrelated code are
not evidence for it or for novelty. An author verification-code hit
for the different exponent 25 was not inspected and is not an input.
The FNS references to general descent and Chabauty supply context;
no new Chabauty theorem is needed for this local image target.

The ready assessments reused are
`drafts/literature/2026-10-15-eleven-adic-even-valuation-containment.md`,
`drafts/literature/2026-10-15-eleven-adic-two-descent-audit.md`,
`drafts/literature/2026-10-08-primitive-eleven-connecting-valuations.md`
and `drafts/literature/2026-10-16-primitive-dyadic-two-descent-image.md`.
The last concerns another prime, not approval to transfer its answer.
The relevant canonical proofs were consulted only for their current
statement, source interfaces and full-fiber tests. L073 already gives
explicit generators of the unrestricted full classes, in addition to
its stated valuation images; this is a useful existing baseline, not
a new result from this review.

ATTEMPTS/033 stops universal all-even containment, by an actual local
class; the proposed restricted set need not contain that point.
ATTEMPTS/014 concerns a different isogeny at two. ATTEMPTS/034–037
concern exhausted global unit lists or an uncertified class backend.
Their obstructions remain recorded and are not reopened by this target.
No matching completed correlated eleven-adic calculation was located
in the targeted notebook material. No sibling notebook was read.

### Approved continuation and discriminating test

Main gap: positive primitive integer emptiness. The intermediate target
is exactly TARGET, with plausible use as another necessary filter in
L084's supported primitive containing space. L084's verified upper
bound remains 13+dim ker(n_S), above eleven; there is no new bound here.

Use the canonical local arithmetic of L041/L042/L044 and the same
two-descent map of L069/L073, transported through L033/L034's entire
map. L044 restricts the admissible scalar residues; its fifth-power
vectors are not two-descent labels. L042 gives both reconstruction and
one entire-fiber realization, not a proof for every scalar in either
residue disk. These existing results reduce prerequisites, without
answering the proposed restricted image.

One bounded subsequent proof attempt is approved as REPRODUCTION.
First seek a uniform square-class reduction of the compatible fibers
within L044's domain, using cited Hensel and square-neighborhood
criteria. A finite computation is justified only after proving its
coverage. Keep one scalar throughout all three base factors, the
ordered rational factors, every Q11-embedding of the ramified field,
and the same theta under the origin-preserving change X=4x, Y=8y+4.
Any exceptional point or removable chart must be evaluated correctly
or excluded by an established scalar condition. A list of independently
possible component classes, even an exhaustive list in each factor,
is only an upper comparison.

Acceptance requires exhaustive containment and exact whole-fiber
realizations of every claimed class tuple, including unit square
classes and all collisions. Report a partial reduction honestly if
that is all the attempt establishes. Continue filtering work only if
the result gives a proper necessary set with a concrete subsequent
global-effect test; stop this filtering use upon proved equality or
redundancy. No subgroup closure, independent codimension, additional
removed unit, or Mordell–Weil rank consequence is preapproved. L084
concerns primitive point classes, not the entire global point image.
Class-kernel arithmetic, the other twists and rational/integer power
lifting remain independent unresolved assumptions. Mathlib full and
supporting coverage: not checked. No originality beyond the checked
sources is claimed.

## Exact proposed target and downstream test

The main gap remains positive primitive integer emptiness. L084 is now
critically verified, but its upper bound 13+dim ker(n_S) still exceeds
eleven and concerns primitive point classes rather than full rank.
The intermediate target proposed here is the exact local set of
three-component two-descent values of tautological points from all
isomorphisms of the entire modular fiber B_s with

    K tensor_Q Q11 = Q11 × Q11 × L,
    L=Q11[r]/(r^10+55).

Use precisely L044's finite s outside {0,1728}, one common nonzero
primitive triple a,b,c in Z11 satisfying a^3+b^4=c^11 and
s c^11=1728 a^3, and every rational-factor permutation and ramified
embedding. Use delta_2 from L069/L073, with the full cubic algebra
Q11 × Q11(sqrt(-11)) at EACH rational base factor and L × L × L
at the degree-ten factor. Preserve the same distinguished theta.
The desired output is the full square-class set, including unit
classes, not merely its valuation projection or an image formed by
independent choices of points in each factor. This is a specification,
not a calculation or a claimed lemma.

A computed proper subset could supply an additional primitive-point
filter for the same supported space as L084. Independence from its
existing tests would remain a separate question. Equality with the
full local image, or a precise proof that this filter cannot strengthen
the present intersection, would justify stopping that use. Any proposed
exact set must have both exhaustive containment and whole-fiber
realizations. Do not use quotient linear algebra unless subgroup status
is proved; a restricted set may fail to be a subgroup. No local set by
itself resolves the class kernel, other modular twists or integer lifting.

## Separate approval required

Essential inputs for source review are L033/L034's modular map, L041's
full base algebra, L042–L044's primitive scalar/whole-fiber results,
L069/L073's two-descent conventions and full local algebras, and L084
for the intended downstream comparison. These are local notebook inputs.
Inspect only necessary canonical proof ranges and reuse their existing
source assessments. Check standard terminology, stronger known results
and primary theorem hypotheses for full local two-descent at eleven
and correlated modular-fiber restriction. The previously reviewed
unrestricted image-size theorem does not alone evaluate a restricted
image. No new source access has been attempted or claimed here.

ATTEMPTS/014 concerns the different five-isogeny at two; 034–036 stop
specific global unit searches and 037 parks an uncertified class backend.
They are preserved. This target changes both the local prime and the
restricted image problem from the completed dyadic work, and needs no
class backend for its local test. Its coverage must nonetheless be
approved in a separate literature-only turn. Mathlib coverage is not
checked. No conclusion about novelty, subgroup status, image size or
additional global codimension is asserted.
