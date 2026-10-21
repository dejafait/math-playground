# Primitive eleven-adic filter versus the existing containing space

TARGET: Compare L085's primitive eleven-adic subgroup with localization of L084's containing space T, certifying redundancy or one additional independent global condition.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the combined-codimension and primitive-eleven assessments; checked the exact L084/L085 definitions, L073/L077 input ranges and ATTEMPTS/033–037; bounded exact-curve, localization/linear-algebra and Hilbert-reciprocity searches located general methods, without an inspected theorem deciding this T comparison. Queries and source reads are recorded below.
SOURCE_EVIDENCE: Bruin–Stoll, 14 March 2008 manuscript, Section 6 pp.11–12, full algorithm/explanation; BPT arXiv:2001.02263v3 Section 1 pp.3–4; FNS 10 June 2019 manuscript Section 7.2/Table 5 and its GRH premise; Milne CFT v4.03 III Theorem 4.4 pp.113–114, V Theorem 5.3/Example 5.4 p.179, VIII 5.8/5.10 pp.246–247 and archimedean cases p.248, freshly inspected.
COMPARISON: Known localization and quadratic Hilbert reciprocity permit a bounded dual-probe test without complete class data; neither computes loc_11(T). FNS's matching global Selmer data assume GRH and concern a different space. L077's complete rational-cubic unit generators can serve as probes, but its primal rank-two calculation and L085's local properness do not decide this target.
GAP: Ready for one separate proof attempt: certify reciprocity constraints with the five fixed L077 probes and test whether the resulting necessary local envelope is contained in J11. Containment could certify redundancy; failure of this sufficient test proves neither global independence nor nonredundancy. No field-specific pairing, envelope or new bound is established here.
REASON: Essential source coverage is adequate for the unchanged global comparison using a materially different bounded certificate mechanism; approve REPRODUCTION, with all specialized pairings and global applicability left to the research turn.
LITERATURE_REASON: This changed global comparison was REVIEW_REQUIRED; its essential new lead is global reciprocity applied to supported square classes, outside the ready local-image audits. Reuse those audits rather than repeat their arithmetic.
SCOPE: Exactly TARGET with the fixed K,D,theta, support and T of L084 and ordered J11 of audited L085. First bounded test uses only L077's five rational-cubic supported-unit generators as dual probes; no complete D-unit/class backend, enlarged affine search or extra full-local condition is assumed.

The main gap remains positive primitive integer emptiness. The proposed
intermediate target asks whether the audited local subgroup can actually
shrink the current primitive containing space. A proved independent
condition would justify a smaller containing space; a redundancy proof
would retire this filtering use. Neither conclusion is supplied here.

Essential local input is L085, with its fixed theta, full ordered algebra
and subgroup equality, together with L073's full local classes. The
global comparison must use exactly T as defined in L084, including
L074/L075's supported space, L076's class-kernel qualification,
L077's existing full-local conditions, L082's primitive dyadic subgroup
and L083's fixed global point. L033/L069 fix the field and coordinate
conventions. Read only the necessary ranges after notebook orientation.
There is no cross-notebook input.

For a strictness certificate require an actual class in T whose full
eleven-adic localization lies outside J11, with membership in every
defining condition proved. A tuple of independently selected local
classes or the properness of J11 alone is insufficient. For redundancy
require containment of the localization of all of T, retaining possible
localized class contributions. No class-kernel value, complete unit
basis, rational-point realization or rank bound may be assumed.

The later test must respect the existing stopped routes:
ATTEMPTS/033 disproves full-local even containment, 034–036 stop specific
affine unit searches, and 037 parks the uncertified class backend.
Reopening one needs a materially new discriminating test. The different
five-isogeny survivor remains intact. A blocker in a global basis
calculation is not evidence of redundancy or independence.

The preceding paragraphs preserve the proposed comparison and its
acceptance criteria. The completed review below approves a separate
attempt, not its mathematical conclusions. Mathlib coverage for this
comparison has not been checked.

## Completed source comparison — 2026-10-17

Main gap: positive primitive integer emptiness. Intermediate target:
decide redundancy or actual independence of this eleven-adic filter
on precisely T. A strict condition could shrink the primitive containing
space; redundancy would retire this filter. Neither would supply a rank
bound, integer lifting, other-twist coverage or a Beal resolution.

### Reused coverage and precise source scope

Reuse `2026-10-17-combined-primitive-supported-codimension.md` for
Simon (2002), Propositions 1.1–1.4, supported containment and the
localization interface; reuse `2026-10-17-primitive-eleven-two-descent-image.md`
and its audit assessment for the entire ordered local image. The
completed combined-space and local-image results are L084 and L085.
The rational-cubic supported-pruning assessment of 2026-10-16 covers
the completeness and support of L077's five generators. None of these
assessments already decides the new global comparison.

Fresh primary reads, with hypotheses retained:

- Bruin–Stoll, *Two-cover descent on hyperelliptic curves*, Math. Comp.
  **78** (2009), 2347–2370,
  [14 March 2008 manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
  Section 6, pp.11–12, all FakeSelmerSet steps and explanations,
  particularly ad 4, ad 8, ad 11 and ad 16. Over a number field,
  square-free f supplies finite supported square classes; odd degree
  uses the full algebra square classes. Norm filtering and localization
  preimages are computed on generators. Partial local testing gives an
  overestimate. The class-group enlargement is essential when claiming
  completeness; supported units alone do not suffice. The early-stop
  test ad 11 is a relevant known redundancy test, but requires the
  actual localized global set. This general method supplies no present
  T-basis or field-specific comparison. No reproof is needed.
- Barrera Salazar–Pacetti–Tornaría, *On 2-Selmer groups and quadratic
  twists of elliptic curves*, Math. Res. Lett. **28** (2021), 1633–1659,
  [arXiv:2001.02263v3, 17 September 2020](https://arxiv.org/pdf/2001.02263v3),
  Section 1, pp.3–4, Kummer construction, Lemmas 1.1/1.3 and Remark 1.4.
  Characteristic different from two and a monic square-free cubic give
  a homomorphism into full norm-square algebra classes, evaluating
  X−theta when invertible. The finite-local size statement uses the
  entire cubic algebra. These hypotheses cover the fixed characteristic-zero
  fields and nonzero-discriminant g. They imply neither arbitrary
  restricted-image subgroup status nor global independence. Here the
  needed subgroup assertions already come from L082/L085.
- Freitas–Naskręcki–Stoll, *The generalized Fermat equation with
  exponents 2, 3, n*, Compositio Math. **156** (2020), 77–113,
  [10 June 2019 final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
  Section 7.2, the paragraph introducing Table 5 and the matching 54a1
  row, PDF pp.26–27. The global Selmer computation explicitly assumes
  GRH. Its displayed dimension four is not an unconditional T-dimension
  or a statement about this primitive eleven-adic subgroup. The
  introduction, PDF p.4, identifies certification of degree-36 class
  groups as the conditional step. These passages do not remove the
  recorded backend/certification blocker.
- J.S. Milne, *Class Field Theory*,
  [v4.03, 6 August 2020](https://www.jmilne.org/math/CourseNotes/CFTc.pdf),
  III Theorem 4.4, pp.113–114, gives bilinearity, nondegeneracy and
  the norm criterion for the Hilbert symbol over a local field
  containing the nth roots of unity. V Theorem 5.3(a)/Example 5.4,
  p.179, gives the product over all places for two nonzero global
  elements. VIII 5.8 and its unramified calculation, pp.246–247,
  provide the residue-symbol formula away from the specified support;
  5.10, p.247, restates global reciprocity. The real and complex cases
  are stated on p.248. Read these statements, the local norm-criterion
  proof and the residue-formula proof. Here n=2 and all fields contain
  mu_2. The product includes every place of D. The Q2 formula on
  p.248 applies to Q2 only; it is not a formula for the degree-33
  dyadic field. No general dyadic-symbol backend is imported.

Only the named general results are imported. Their field-specific
application, omitted-place checks, pairings and resulting equations
are not derived in this literature turn. No essential unread primary
lead remains for the bounded test; no completeness or novelty claim
is inferred from search results. Mathlib full/supporting coverage is
not checked, and is not needed for this informal attempt.

### Concrete bounded continuation within TARGET

The proposed mechanism is a dual reciprocity certificate, rather than
searching for another primal supported unit. Fix F=Q(t) inside D as
in L071/L077. Use exactly the five certified F-supported units

    -1, v=-1/t, s=t+1, a=9-7t+5t^2, b=-4-8t-t^2

from L077, embedded in D via the same theta. They are probes, not
asserted elements of T. Their full F-unit square-class generation is
already known; they are not claimed to span D's unit group or its
reciprocity dual. L077's zero primal kernel on its norm-square
two-dimensional family is therefore not a duplicate of this test.

For a prospective general class of T, attempt to apply quadratic
Hilbert reciprocity against those five probes. First justify their
support after extension to D and removal of every other finite and
archimedean factor, using W_S's actual even-outside-S definition and
norm-square hypothesis. Retain possible localized class contributions;
do not replace a general class by an S-unit. Any archimedean sign
claim must be checked for W_S itself, rather than silently extended
from L069's ordinary-unit statement.

Keep both dyadic factors and L082's two alternatives. At eleven keep
the two rational full-local conditions actually imposed by T and the
ENTIRE norm-square ambient group at the degree-ten base place.
L084 does not impose the full Kummer subgroup at that last place.
Adding it would change T and cannot certify redundancy for TARGET.
Use L073's full algebra and L085's ordering throughout. Do not assume
the two rational coordinates agree unless a global argument proves it.

The bounded test is to compute exact pairing constraints for these
five probes, form the resulting necessary envelope of local tuples,
and test its eleven-adic projection for containment in J11. This is
a proposed calculation/proof, not a computed envelope or a theorem
about T. Certify all Hilbert symbols by the cited general properties
and exact local evidence; the Q2 formula must not be used in a
ramified extension. If an essential pairing remains uncomputed, save
that precise obstruction without declaring the test negative.

Success for redundancy requires a proved envelope containing loc(T)
whose eleven-adic projection is contained in J11. Such a certificate
would cover class contributions without computing them. If the exact
envelope still permits a tuple outside J11, stop this fixed five-probe
sufficient certificate: it does not prove that such a tuple globalizes.
An independence conclusion still requires an actual class in T,
with every defining membership verified, outside J11. A purely local
tuple cannot meet that alternative. Do not enlarge the probe family,
reopen affine searches or presume a new class backend in this step.
This supplies a discriminating bounded attempt even if neither desired
global conclusion follows.

### Search and recorded failures

Fresh queries were `"X0(11)" "2-descent" "local"`,
`"Two-cover descent" "linear algebra" localization`,
`"Selmer" "local conditions" "independent" localization number field`,
and `Hilbert reciprocity theorem Hilbert symbol number field product formula Milne class field theory local norms`.
Useful primary matches were the Bruin–Stoll and Milne texts above.
Other searches returned general Selmer theory and unrelated curves;
those snippets are not theorem evidence. Exact-family/stronger-result
searches in the ready L085 assessment are reused; FNS's GRH boundary
was checked directly here. No inspected theorem decides this exact T
comparison, and no literature-wide absence is claimed.

Narrow local checks covered L084's definition and audit interface,
L085's conclusion and proof, L073's full images, L077's family and
the explicit stops ATTEMPTS/033–037. Those stops concern deletion of
eleven, specified affine element/quotient lists, a fixed ideal-basis
list and an unavailable unconditional class backend. The dual-probe
test does not enlarge any stopped list or need that backend. It is a
new proposed sufficient certificate within the same global target;
no mathematical exploration budget is renewed by this review.

Outcome: literature EXPLORATION with completed SPECIALIZE coverage,
classification REPRODUCTION of known methods. No new lemma, script,
local pairing, global condition, dimension bound or integer exclusion
was produced. A separate research invocation must perform the test.
